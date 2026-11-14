# 工作树全面重整：检测并优先使用原生支持

**日期：**2026-04-06
**状态：**草案
**工单：**PRI-974
**涵盖：**PRI-823（Codex App 兼容性）

## 问题

Superpowers 对工作树管理有固定主张——固定路径（`.worktrees/<branch>`）、固定命令（`git worktree add`）和固定清理方式（`git worktree remove`）。同时，Claude Code、Codex App、Gemini CLI 和 Cursor 都提供原生工作树支持，各有路径、生命周期和清理方式。

这造成三种失败模式：

1. **重复**——在 Claude Code 上，技能执行 `EnterWorktree`/`ExitWorktree` 已经负责的工作

2. **冲突**——在 Codex App 上，技能试图在已受管理工作树内部创建工作树

3. **幽灵状态**——技能在 `.worktrees/` 创建的工作树对宿主不可见；宿主在 `.claude/worktrees/` 创建的工作树对技能不可见

对于没有原生支持的宿主（Codex CLI、OpenCode、独立 Copilot），superpowers 填补了真实缺口。技能仍应存在，但存在原生支持时应让出控制权。

## 目标

1. 宿主有原生工作树系统时优先使用它

2. 继续为缺少原生支持的宿主提供工作树能力

3. 修复 finishing-a-development-branch 的三个已知 bug（#940、#999、#238）

4. 让工作树创建成为可选行为，而非强制（#991）

5. 用平台中立措辞替换硬编码 `CLAUDE.md` 引用（#1049）

## 非目标

- 每个工作树的环境约定（`.worktree-env.sh`、端口偏移）——第 4 阶段

- 用 PreToolUse 钩子强制路径——第 4 阶段

- 多仓库工作树文档——第 4 阶段

- 针对工作树的头脑风暴清单修改——第 4 阶段

- `.superpowers-session.json` 元数据跟踪（PR #997 的有趣想法，v1 不需要）

- 将钩子符号链接进工作树（PR #965 的独立事项）

## 设计原则

### 检测状态，不检测平台

用 `GIT_DIR != GIT_COMMON` 判断“是否已在工作树中”，无需通过环境变量识别宿主。这是稳定的 git 原语（git 2.5 起，2015 年），适用于所有宿主，新增宿主也无需维护。

### 声明意图，规定回退方案

技能说明目标（“确保工作在隔离工作区完成”），有原生工具时优先使用。只有宿主不支持原生工作树时，才规定具体 git 命令。第 1a 步先列出原生工具（`EnterWorktree`、`WorktreeCreate`、`/worktree`、`--worktree`），第 1b 步再给 git 回退。早期规格把 1a 写得很抽象（“你知道自己的工具”），TDD 证明 1a 太含糊时代理会锚定 1b 的具体命令。要让偏好可靠，需要明确工具名和同意授权桥梁。

### 按来源确定所有权

谁创建工作树，谁负责清理。宿主创建时，superpowers 不碰；superpowers 通过 git 回退创建时，由自己清理。判据：位于 `.worktrees/` 或 `worktrees/` 下的工作树归 superpowers；其他路径（`.claude/worktrees/`、`~/.codex/worktrees/`、`.gemini/worktrees/` 或旧用户全局路径）归宿主或用户，保持不变。

## 设计

### 1. 重写 `using-git-worktrees` 的 SKILL.md

技能在创建前新增三步，并简化创建流程。

#### 第 0 步：检测现有隔离

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

有三种结果：

| 条件 | 含义 | 操作 |
|-----------|---------|--------|
| `GIT_DIR == GIT_COMMON` | 普通仓库检出 | 继续第 0.5 步 |
| `GIT_DIR != GIT_COMMON`，具名分支 | 已在关联工作树中 | 跳到第 3 步（项目设置）。报告：“已在 `<path>` 的隔离工作区中，分支 `<name>`。” |
| `GIT_DIR != GIT_COMMON`，分离 HEAD | 外部管理工作树（例如 Codex App 沙箱） | 跳到第 3 步。报告：“已在 `<path>` 的隔离工作区中（分离 HEAD，由外部管理）。” |

第 0 步不关心工作树由谁创建或哪个宿主运行。只要在工作树中，来源无关。

**子模块防护：**git 子模块内部的 `GIT_DIR != GIT_COMMON` 也为真。确认“已在工作树”前，先检查不在子模块中：

```bash
git rev-parse --show-superproject-working-tree 2>/dev/null
```

若在子模块中，按 `GIT_DIR == GIT_COMMON` 处理（进入第 0.5 步）。

#### 第 0.5 步：征得同意

第 0 步未发现隔离（`GIT_DIR == GIT_COMMON`）时，创建前询问：

> “要我设置隔离工作树吗？它能保护当前分支不受改动影响。（y/n）”

若同意，进入第 1 步。若拒绝，在原处工作，跳到第 3 步且不创建工作树。

第 0 步发现已有隔离时完全跳过此步（没有必要询问已经存在的东西）。

#### 第 1a 步：原生工具（首选）

> 用户已要求隔离工作区（第 0 步同意）。检查可用工具：是否有 `EnterWorktree`、`WorktreeCreate`、`/worktree` 命令或 `--worktree` 标志？若有，用户创建工作树的同意就是使用它的授权。现在使用并跳到第 3 步。

使用原生工具后，跳到第 3 步（项目设置）。

**设计说明——TDD 修订：**早期规格刻意把第 1a 步写得很短、抽象（“你知道自己的工具，技能无需命名”）。TDD 证明这样不可行：代理锚定第 1b 步的具体 git 命令并忽略抽象指引（2/6 通过）。三项修改解决了问题（GREEN 和 PRESSURE 测试合计 50/50 通过）：

1. **明确工具名**——列出 `EnterWorktree`、`WorktreeCreate`、`/worktree`、`--worktree`，把“我有原生工具吗”的判断转为事实查询（“`EnterWorktree` 是否在工具列表？”）。没有这些工具的代理只需检查、找不到、再进入 1b；未观察到误判。

2. **同意桥梁**——“用户创建工作树的同意就是使用它的授权”直接对应 `EnterWorktree` 的工具级护栏（“仅当用户明确要求”）。工具描述优先于技能说明（Claude Code #29950），因此技能必须把用户同意表达成工具所需的授权。

3. **危险信号条目**——在 Red Flags 中命名具体反模式：“有原生工作树工具却使用 `git worktree add`——这是第一大错误”。

曾测试把第 1b 步拆到独立技能，证明没有必要。锚定问题由 1a 文案质量解决，无需物理隔离 git 命令。完整 240 行技能（所有 git 命令可见）的对照测试 20/20 通过。

#### 第 1b 步：git 工作树回退

没有原生工具时，手动创建工作树。

**目录选择**（优先级）：

1. 检查项目代理说明文件（CLAUDE.md、GEMINI.md、AGENTS.md、.cursorrules 或同类文件）中的工作树目录偏好。

2. 检查已有 `.worktrees/` 或 `worktrees/`；存在则使用。两者都有时优先 `.worktrees/`。

3. 默认使用 `.worktrees/`。

不弹出交互式目录选择。不检测或提供旧用户全局 superpowers 工作树路径；除非用户明确指定其他位置，新手动工作树都位于项目本地。

**安全验证**（仅项目本地目录）：

```bash
git check-ignore -q .worktrees 2>/dev/null
```

若未被忽略，先加入 `.gitignore` 并提交，再继续。

**创建：**

```bash
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"
```

**钩子感知：**git 工作树不会继承父仓库钩子目录。通过 1b 创建工作树后，若主仓库存在钩子目录，建立符号链接：

```bash
if [ -d "$MAIN_ROOT/.git/hooks" ]; then
    ln -sf "$MAIN_ROOT/.git/hooks" "$path/.git/hooks"
fi
```

这样，工作移至工作树后，预提交检查、linter 和其他钩子不会悄悄停止。（想法来自 PR #965。）

**沙箱回退：**若 `git worktree add` 因权限失败，视为受限环境。跳过创建，在当前目录工作并进入第 3 步。

**步骤编号说明：**现行技能使用扁平的步骤 1–4。本设计使用 0、0.5、1a、1b、3、4；没有第 2 步，因为旧的整体“创建隔离工作区”已拆为 1a/1b。实施时应重新干净编号（0→“第 0 步：检测”，0.5→并进第 0 步，1a/1b→“第 1 步”，3→“第 2 步”，4→“第 3 步”），也可保留现编号并加说明，由实施者选择。

#### 第 3–4 步：项目设置与基线测试（不变）

无论哪条路径建立工作区（第 0 步发现已有、1a 原生工具、1b git 回退或完全不建工作树），后续都汇合：

- **第 3 步：**自动检测并运行项目设置（`npm install`、`cargo build`、`pip install`、`go mod download` 等）

- **第 4 步：**运行测试套件。若失败，报告失败并询问是否继续。

### 2. 重写 `finishing-a-development-branch` 的 SKILL.md

收尾技能增加环境检测并修复三个 bug。

#### 第 1 步：验证测试（不变）

运行项目测试套件。失败即停止，不提供完成选项。

#### 第 1.5 步：检测环境（新增）

重新运行创建时的第 0 步检测：

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
```

三种情况：

| 状态 | 菜单 | 清理 |
|-------|------|---------|
| `GIT_DIR == GIT_COMMON`（普通仓库） | 标准 4 个选项 | 无需清理工作树 |
| `GIT_DIR != GIT_COMMON`，具名分支 | 标准 4 个选项 | 按来源判断（见第 5 步） |
| `GIT_DIR != GIT_COMMON`，分离 HEAD | 精简菜单：作为新分支推送并建立 PR、保持原样、丢弃 | 不能合并（无法从分离 HEAD 合并） |

#### 第 2 步：确定基础分支（不变）

#### 第 3 步：呈现选项

**普通仓库与具名分支工作树：**

1. 本地合并回 `<base-branch>`

2. 推送并创建拉取请求

3. 保持分支原样（稍后自己处理）

4. 丢弃此工作

**分离 HEAD：**

1. 作为新分支推送并创建拉取请求

2. 保持原样（稍后自己处理）

3. 丢弃此工作

#### 第 4 步：执行选择

**选项 1（本地合并）：**

```bash
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"
git checkout <base-branch>
git pull
git merge <feature-branch>
<run tests>
git worktree remove "$WORKTREE_PATH"  # 仅当 superpowers 拥有它
git branch -d <feature-branch>
```

顺序至关重要：合并 → 验证 → 移除工作树 → 删除分支。旧技能先删分支再移工作树（失败，因为工作树仍引用分支）。先移工作树同样错误——若随后合并失败，工作目录已消失且改动丢失。

**选项 2（创建 PR）：**

推送分支并创建 PR。不要清理工作树，用户还需要它迭代 PR。（修复 Bug #940：删除互相矛盾的“然后清理工作树”文字。）

**选项 3（保持原样）：**不操作。

**选项 4（丢弃）：**要求输入“discard”确认。然后移除工作树（若归 superpowers 所有），强制删除分支。

#### 第 5 步：清理（更新）

```
if GIT_DIR == GIT_COMMON:
    # 普通仓库，无需清理工作树
    done

if worktree path is under .worktrees/ or worktrees/:
    # Superpowers 创建了它，由我们负责清理
    cd to main repo root       # 修复 Bug #238
    git worktree remove <path>

else:
    # 宿主创建了它，不要碰
    # 平台提供退出工作区工具时使用它
    # 否则保持工作树原位
```

仅选项 1 和 4 执行清理；选项 2 和 3 始终保留工作树。（修复 Bug #940。）

**清理陈旧工作树：**任何 `git worktree remove` 后运行 `git worktree prune` 进行自愈。工作树目录可能被带外删除（宿主清理、手动 `rm` 或 `.claude/` 清理），留下导致困惑错误的陈旧登记。一行命令可防止无声腐坏。（想法来自 PR #1072。）

### 3. 集成更新

#### `subagent-driven-development` 与 `executing-plans`

二者目前在集成部分都列`using-git-worktrees`为必需项，改为：

> `using-git-worktrees`——确保隔离工作区（创建或确认已有）。

技能本身现在处理同意（0.5步）和检测（0步），调用技能无需再加关卡或提示。

#### `writing-plans`（中文说明）

删除过时说法“应在专用工作树运行（由头脑风暴技能创建）”。头脑风暴是设计技能，不创建工作树；执行时由`using-git-worktrees`处理工作树提示。

### 4. 平台中立的说明文件引用

工作树技能中所有硬编码`CLAUDE.md`替换为：

> “项目的代理说明文件（CLAUDE.md、GEMINI.md、AGENTS.md、.cursorrules或等价文件）”

这适用于1b步的目录偏好检查。

## 一并修复的bug

| Bug | 问题 | 修复 | 位置 |
|-----|---------|-----|----------|
| #940 | 选项2文字说“然后清理工作树（第5步）”，但速查表说保留；第5步说选项1、2、4，常见错误说仅1和4。 | 从选项2删除清理；第5步只适用1和4。 | finishing SKILL.md |
| #999 | 选项1先删分支再移除工作树；`git branch -d`因工作树仍引用分支而失败。 | 顺序改为合并→验证测试→移除工作树→删除分支；合并成功前不得删除。 | finishing SKILL.md |
| #238 | 当前目录在被删除工作树内时，`git worktree remove`静默失败。 | 使用 `git worktree remove` 前先 `cd` 到主仓库根目录。 | finishing SKILL.md |

## 已解决issue

| Issue | 解决方式 |
|-------|-----------|
| #940 | 直接修复Bug #940 |
| #991 | 0.5步选择加入同意 |
| #918 | 0步检测+1.5步收尾检测 |
| #1009 | 1a步使用宿主原生工具（如`EnterWorktree`）自动解决；依赖1a有效，见风险 |
| #999 | 直接修复 |
| #238 | 直接修复 |
| #1049 | 平台中立说明引用 |
| #279 | 检测并让路；不覆盖原生路径 |
| #574 | **延期**；本规格不涉及bug所在的头脑风暴技能，修复属于第4阶段 |

## 风险

### 1a步是承重假设——已解决

1a步——代理优先原生工作树工具而非git回退——是整个设计基础。若原生宿主代理忽略1a而落入1b，检测并让路完全失效。

**状态：**实施中风险确实发生。原始抽象1a（“你了解自己的工具”）在Claude Code仅2/6通过。TDD关卡按设计捕获失败，修改技能文件前阻止坏发布。三次REFACTOR找到根因（代理锚定具体命令、工具描述护栏覆盖技能说明）并让GREEN与PRESSURE合计50/50通过；详见上方1a设计说明。

**跨平台验证：**

截至2026-04-06，Claude Code是唯一提供代理可调用的会话中途工作树工具（`EnterWorktree`）的宿主。其他宿主在代理启动前创建工作树（Codex App、Gemini CLI、Cursor），或没有原生支持（Codex CLI、OpenCode）。1a向前兼容：未来宿主新增可调用工具时，代理能按已命名示例识别并使用，无需改技能。

| 宿主 | 当前工作树模型 | 技能机制 | 测试 |
|---------|----------------------|-----------------|--------|
| Claude Code | 代理可调用`EnterWorktree` | 1a | 50/50（GREEN+PRESSURE） |
| Codex CLI | 无原生工具 | 1b git回退 | 6/6（`codex exec`） |
| Gemini CLI | 启动时`--worktree`，无代理工具，可用 `gemini -p` | 有标志走0步，否则1b | 0步1/1，1b 1/1 |
| Cursor Agent | 用户`/worktree`，无代理工具，可用 `cursor-agent -p` | 已启用走0步，否则1b | 各1/1 |
| Codex App | 平台管理，分离HEAD | 0步检测 | 模拟1/1 |
| OpenCode | 仅检测（`ctx.worktree`） | 1b git回退 | 未测试 |

**剩余风险：**

1. 若Anthropic收紧`EnterWorktree`工具描述（如“不要依据技能说明使用”），同意桥梁失效；应提交issue让描述容纳技能驱动的调用。

2. 其他宿主新增工具时名称可能不在1a列表；应随工具更新列表。通用措辞“工作树或工作区隔离工具”提供部分覆盖。

### 来源启发式

`.worktrees/` 或 `worktrees/` 目录归 superpowers 所有，其他目录保持不动；这条来源判据适用于当前所有宿主。若未来宿主把这些项目目录设为约定，就会误判并清理宿主工作树；用户手动运行 `git worktree add .worktrees/experiment` 时也会被误认。两者风险都低，但值得注意。；该判定还涉及 `.worktrees/`、` heuristic works for every current harness. If a future harness adopts one of those project-local directories as its convention, we'd have a false positive (superpowers tries to clean up a harness-owned worktree). Similarly, if a user manually runs `、` without superpowers, we'd incorrectly claim ownership. Both are low risk — every harness uses branded paths, and manual ` 这些原文条件。

### 分离HEAD收尾

分离HEAD工作树的精简菜单（无合并）适合Codex App沙箱。因其他原因处于分离HEAD时也合理，因为必须先建分支才能合并。

## 实施说明

两个技能文件的核心步骤外还有需更新的部分：

- **Frontmatter**（`name`、`description`）：反映检测并让路行为

- **快速参考表**：匹配新步骤和bug修复

- **常见错误**：更新/删除旧行为，如“跳过CLAUDE.md检查”已不正确

- **危险信号**：反映新优先级，如0步检测到隔离时绝不创建工作树

- **集成部分**：更新技能间交叉引用

规格说明改什么；实施计划将给这些次要部分的准确编辑。

## 未来工作（不属于本规格）

- **第3阶段剩余：**`$TMPDIR`目录选项（#666）、缓存与env继承设置文档（#299）

- **第4阶段：**PreToolUse路径强制（#1040）、每工作树环境约定（#597）、头脑风暴清单工作树步骤（#574）、多仓库文档（#710）
