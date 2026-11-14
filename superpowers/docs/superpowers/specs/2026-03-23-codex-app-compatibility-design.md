# Codex 应用兼容性：工作树与收尾技能适配

使 superpowers 技能能在 Codex 应用的沙箱化工作树环境中工作，同时保持现有 Claude Code 或 Codex CLI 行为不变。

**工单：**PRI-823

## 动机

Codex 应用在由它管理的 git 工作树中运行代理——处于分离 HEAD（detached HEAD），位于 `$CODEX_HOME/worktrees/` 下，并受 Seatbelt 沙箱限制，阻止 `git checkout -b`、`git push` 和网络访问。三个 superpowers 技能假定 git 访问不受限制：`using-git-worktrees` 会创建带具名分支的手动工作树，`finishing-a-development-branch` 按分支名称合并/推送/创建 PR，`subagent-driven-development` 需要两者。

Codex CLI（开源终端工具）没有这种冲突——它没有内置工作树管理。我们的手动工作树方案在那里填补隔离方面的空白。问题特定于 Codex 应用。

## 实测发现

2026-03-23 在 Codex 应用中测试：

| 操作 | workspace-write 沙箱 | 完全访问沙箱 |
|---|---|---|
| `git add` | 可运行 | 可运行 |
| `git commit` | 可运行 | 可运行 |
| `git checkout -b` | **被阻止**（无法写入 `.git/refs/heads/`） | 可运行 |
| `git push` | **被阻止**（网络访问 + `.git/refs/remotes/`） | 可运行 |
| `gh pr create` | **被阻止**（网络访问） | 可运行 |
| `git status/diff/log` | 可运行 | 可运行 |

其他发现：

- `spawn_agent` 子代理**共享**父线程的文件系统（已通过标记文件测试确认）

- 无论工作树从哪个分支启动，应用头部都会显示“Create branch”（创建分支）按钮

- 应用的原生收尾流程：创建分支 → 提交对话框 → 提交并推送 / 提交并创建 PR

- `network_access = true` 配置在 macOS 上静默失效（问题 #10390）

## 设计：只读环境检测

三个只读 git 命令可无副作用地检测环境：

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

由此得出两个信号：

- **IN_LINKED_WORKTREE：**`GIT_DIR != GIT_COMMON`——代理位于由其他对象创建的工作树中（Codex 应用、Claude Code Agent 工具、先前技能运行或用户）

- **ON_DETACHED_HEAD：**`BRANCH` 为空——不存在具名分支

为什么检查 `git-dir != git-common-dir` 而不检查 `show-toplevel`：

- 普通仓库中，两者解析到同一个 `.git` 目录

- 链接工作树中，`git-dir` 是 `.git/worktrees/<name>`，`git-common-dir` 是 `.git`

- 子模块中两者相等——避免 `show-toplevel` 会产生的误报

- 通过 `cd && pwd -P` 解析可处理相对路径问题（在普通仓库中 `git-common-dir` 返回相对 `.git`，工作树中返回绝对路径）及符号链接（macOS `/tmp` → `/private/tmp`）

### 决策矩阵

| 链接工作树？ | 分离 HEAD？ | 环境 | 操作 |
|---|---|---|---|
| 否 | 否 | Claude Code / Codex CLI / 普通 git | 完整技能行为（不变） |
| 是 | 是 | Codex 应用工作树（workspace-write） | 跳过创建工作树；结束时提供交接载荷 |
| 是 | 否 | Codex 应用（完全访问）或手动工作树 | 跳过创建工作树；执行完整收尾流程 |
| 否 | 是 | 异常情况（手动分离 HEAD） | 正常创建工作树；收尾时警告 |

## 改动

### 1. `using-git-worktrees/SKILL.md`——添加步骤 0（约 12 行）

在“概览”与“目录选择流程”之间新增一节：

**步骤 0：检查是否已处于隔离工作区**

运行检测命令。如果 `GIT_DIR != GIT_COMMON`，完全跳过创建工作树。改为：

1. 跳到创建步骤下的“运行项目设置”小节——`npm install` 等操作是幂等的，为安全起见值得运行

2. 然后执行“验证干净基线”——运行测试

3. 按分支状态报告：

- 位于分支上：已在隔离工作区 `<path>`，所在分支为 `<name>`。测试通过。准备开始实现。

- 分离 HEAD：已处于位于 `<path>` 的隔离工作区（分离 HEAD，由外部管理）。测试通过。注意：收尾时需要创建分支。准备开始实现。

如果 `GIT_DIR == GIT_COMMON`，继续完整的工作树创建流程（不变）。

当步骤 0 触发时跳过安全验证（.gitignore 检查）——这对由外部创建的工作树无关紧要。

更新集成部分中的“被调用者”条目。将每一处由上下文特定文本改为：“确保隔离工作区（创建一个或验证现有工作区）”。例如，`subagent-driven-development` 条目从“必需：开始前设置隔离工作区”改为“必需：确保隔离工作区（创建一个或验证现有工作区）”。

**沙箱回退：**如果 `GIT_DIR == GIT_COMMON` 且技能继续进入创建步骤，但 `git worktree add -b` 因权限错误失败（例如 Seatbelt 沙箱拒绝），将其视为较晚检测到的受限环境。回退到步骤 0 的“已处于工作区”行为——跳过创建，在当前目录运行设置与基线测试，并相应报告。

步骤 0 报告后停止。不要继续执行目录选择或创建步骤。

**其余内容不变：**目录选择、安全验证、创建步骤、项目设置、基线测试、快速参考、常见错误、危险信号。

### 2. `finishing-a-development-branch/SKILL.md`——添加步骤 1.5 + 清理保护（约 20 行）

**步骤 1.5：检测环境**（在步骤 1“验证测试”之后、步骤 2“确定基础分支”之前）

运行检测命令。有三种路径：

- **路径 A**完全跳过步骤 2 和 3（不需要基础分支或选项）。

- **路径 B 与 C**照常执行步骤 2（确定基础分支）和步骤 3（提供选项）。

**路径 A——外部管理的工作树 + 分离 HEAD**（`GIT_DIR != GIT_COMMON` 且 `BRANCH` 为空）：

首先确保所有工作均已暂存并提交（`git add` + `git commit`）。Codex 应用的收尾控件只处理已提交的工作。

然后向用户展示以下内容（不要展示 4 个选项的菜单）：

```
实现已完成。所有测试通过。
当前 HEAD：<full-commit-sha>

此工作区由外部管理（分离 HEAD）。
我无法在此创建分支、推送或打开 PR。

⚠ 这些提交位于分离 HEAD 上。如果你不创建分支，
它们可能会在工作区清理时丢失。

如果你的宿主应用提供这些控件：
- “Create branch”（创建分支）——命名分支，然后提交/推送/创建 PR
- “Hand off to local”（交接至本地）——将改动移至本地检出

建议的分支名称：<ticket-id/short-description>
建议的提交消息：<summary-of-work>
```

分支名称推导：如果可用，使用工单 ID（例如 `pri-823/codex-compat`）；否则将计划标题前 5 个词转换为短横线格式；若都没有则省略建议。避免在分支名称中包含敏感内容（漏洞描述、客户名称）。

跳到步骤 5（对外部管理的工作树而言，清理不执行操作）。

**路径 B——外部管理的工作树 + 具名分支**（`GIT_DIR != GIT_COMMON` 且 `BRANCH` 存在）：

照常展示 4 个选项的菜单。（步骤 5 的清理保护会独立重新检测外部管理状态。）

**路径 C——正常环境**（`GIT_DIR == GIT_COMMON`）：

按当前方式展示 4 个选项的菜单（不变）。

**步骤 5 清理保护：**

在清理时重新运行 `GIT_DIR` 与 `GIT_COMMON` 的检测（不要依赖先前技能输出——收尾技能可能在不同会话中运行）。如果 `GIT_DIR != GIT_COMMON`，跳过 `git worktree remove`——宿主环境拥有此工作区。

否则按当前方式检查并移除。注意：现有步骤 5 文本说“针对选项 1、2、4”，但快速参考表和常见错误部分说“仅选项 1 和 4”。新保护添加在此现有逻辑之前，不改变哪些选项会触发清理。

**其余内容不变：**选项 1-4 的逻辑、快速参考、常见错误、危险信号。

### 3. `subagent-driven-development/SKILL.md` 与 `executing-plans/SKILL.md`——各修改 1 行

两个技能的集成部分都有相同的一行。将：

```
- superpowers:using-git-worktrees - REQUIRED: Set up isolated workspace before starting
```

改为：

```
- superpowers:using-git-worktrees - REQUIRED: 确保隔离工作区（创建一个或验证现有工作区）
```

**其余内容不变：**派发/审查循环、提示词模板、模型选择、状态处理、危险信号。

### 4. `codex-tools.md`——添加环境检测文档（约 15 行）

末尾新增两节：

**环境检测：**

```markdown
## 环境检测

创建工作树或结束分支的技能应先用只读 git 命令
检测环境，再继续操作：

\```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
\```

- `GIT_DIR != GIT_COMMON` → 已处于链接工作树（跳过创建）
- `BRANCH` 为空 → 分离 HEAD（无法从沙箱创建分支/推送/创建 PR）

各技能如何使用这些信号，参见 `using-git-worktrees` 步骤 0
及 `finishing-a-development-branch` 步骤 1.5。
```

**Codex 应用收尾：**

```markdown
## Codex 应用收尾

沙箱阻止分支/推送操作时（由外部管理工作树中的
分离 HEAD），代理提交全部工作，并告知用户使用
应用的原生控件：

- **“Create branch”（创建分支）**——命名分支，然后通过应用 UI 提交/推送/创建 PR
- **“Hand off to local”（交接至本地）**——将工作转移到用户的本地检出

代理仍可运行测试、暂存文件，并输出供用户复制的建议分支名称、
提交消息和 PR 描述。
```

## 不改变的内容

- `implementer-prompt.md`、`spec-reviewer-prompt.md`、`code-quality-reviewer-prompt.md`——子代理提示词未改动

- `executing-plans/SKILL.md`——仅集成说明一行改变（同 `subagent-driven-development`）；全部运行时行为不变

- `dispatching-parallel-agents/SKILL.md`——不涉及工作树或收尾操作

- `.codex/INSTALL.md`——安装流程不变

- 4 个选项的收尾菜单——对 Claude Code 和 Codex CLI 精确保留

- 完整的工作树创建流程——对非工作树环境精确保留

- 子代理派发/审查/迭代循环——不变（已确认文件系统共享）

## 范围摘要

| 文件 | 改动 |
|---|---|
| `skills/using-git-worktrees/SKILL.md` | 增加 12 行（步骤 0） |
| `skills/finishing-a-development-branch/SKILL.md` | 增加 20 行（步骤 1.5 + 清理保护） |
| `skills/subagent-driven-development/SKILL.md` | 修改 1 行 |
| `skills/executing-plans/SKILL.md` | 修改 1 行 |
| `skills/using-superpowers/references/codex-tools.md` | 增加 15 行 |

5 个文件共新增/修改约 50 行。不新增文件。无破坏性变更。

## 未来考虑

如果第三个技能需要相同的检测模式，将其提取到共享的 `references/environment-detection.md`（方案 B）。现在不需要——目前只有 2 个技能使用。

## 测试计划

### 自动化测试（实现后在 Claude Code 中运行）

1. 普通仓库检测——断言 IN_LINKED_WORKTREE=false

2. 链接工作树检测——用 `git worktree add` 创建测试工作树，断言 IN_LINKED_WORKTREE=true

3. 分离 HEAD 检测——`git checkout --detach`，断言 ON_DETACHED_HEAD=true

4. 收尾技能交接输出——在受限环境中验证输出交接消息（而非 4 选项菜单）

5. **步骤 5 清理保护**——创建链接工作树（`git worktree add /tmp/test-cleanup -b test-cleanup`），`cd` 进入其中，运行步骤 5 清理检测（`GIT_DIR` 与 `GIT_COMMON`），断言它不会调用 `git worktree remove`。然后 `cd` 回主仓库，运行相同检测，断言它会调用 `git worktree remove`。之后清理测试工作树。

### Codex 应用手动测试（5 项）

1. 工作树线程中的检测（workspace-write）——验证 GIT_DIR != GIT_COMMON，且分支为空

2. 工作树线程中的检测（完全访问）——检测相同，但沙箱行为不同

3. 收尾技能交接格式——验证代理输出交接载荷，而非 4 选项菜单

4. 完整生命周期——检测 → 提交 → 收尾检测 → 正确行为 → 清理

5. **本地线程中的沙箱回退**——启动 Codex 应用**本地线程**（workspace-write 沙箱）。提示：“使用 superpowers 技能 `using-git-worktrees` 设置隔离工作区，以实施一项小改动。”预检查：`git checkout -b test-sandbox-check` 应以 `Operation not permitted` 失败。预期：技能检测到 `GIT_DIR == GIT_COMMON`（普通仓库），尝试 `git worktree add -b`，遇到 Seatbelt 拒绝，回退到步骤 0 的“已处于工作区”行为——运行设置、基线测试，并从当前目录报告准备就绪。通过：代理平稳恢复，不出现晦涩错误消息。失败：代理打印原始 Seatbelt 错误、反复重试，或因令人困惑的输出放弃。

### 回归

- 现有 Claude Code 技能触发测试仍通过

- 现有子代理驱动开发集成测试仍通过

- 普通 Claude Code 会话：完整工作树创建及四选项收尾仍工作
