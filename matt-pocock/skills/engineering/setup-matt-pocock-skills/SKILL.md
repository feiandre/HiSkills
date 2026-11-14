---
name: setup-matt-pocock-skills
description: "为工程技能配置此仓库：设置 issue 跟踪器、分诊标签词汇及领域文档布局。首次使用其他工程技能前运行一次。"
disable-model-invocation: true
---

# 设置 Matt Pocock 的技能

搭建工程技能所需的逐仓库配置：

- **Issue 跟踪器**：issue 所在位置（默认 GitHub；也开箱支持本地 Markdown）

- **分诊标签**：用于五个标准分诊角色的字符串

- **领域文档**：`GLOSSARY.md` 与 ADR 所在位置，以及读取它们的消费者规则

这是提示词驱动的技能，不是确定性脚本。探索、呈现发现、与用户确认，然后写入。

## 流程

### 1. 探索

查看当前仓库以理解起始状态。阅读现有内容；不要假定：

- `git remote -v` 和 `.git/config`：这是 GitHub 仓库吗？是哪一个？

- 仓库根目录的 `AGENTS.md` 与 `CLAUDE.md`：任一存在吗？其中是否已有 `## Agent skills` 部分？

- 仓库根目录的 `GLOSSARY.md` 与 `GLOSSARY-MAP.md`，以及遗留的 `CONTEXT.md` / `CONTEXT-MAP.md`。若存在遗留文件，提议用 `git mv` 改为 `GLOSSARY` 名称，并改写 `docs/agents/domain.md` 中的名称。

- `docs/adr/` 及任何 `src/*/docs/adr/` 目录

- `docs/agents/`：本技能先前输出是否存在？

- `.scratch/`：表明已在使用本地 Markdown issue 跟踪器约定

- `triage` 技能是否安装？（与本技能并列的 `triage` 技能文件夹，或可用技能中存在 `triage`。）这决定 B 部分是否运行。

- Monorepo 信号：`pnpm-workspace.yaml`、`package.json` 中的 `workspaces` 字段，或含独立 `src/` 的已填充 `packages/*`。只有真正大型多包仓库才存在；缺失意味着单上下文，几乎所有仓库都是如此。

### 2. 呈现发现并询问

总结现有与缺失内容。然后按顺序处理各部分。一部分一问，然后下一部分。

每部分先给推荐答案，使用户一词即可接受。只有选择确会分叉时才给一行解释；探索已确定的部分完全跳过（未安装 `triage` 时跳过 B 部分，无 monorepo 时跳过 C 部分）。

**A 部分：Issue 跟踪器。**

> 解释：这里的“issue 跟踪器”是本仓库 issue 所在地。`to-tickets`、`triage`、`to-spec` 等技能都会读写它。它们需要知道是调用 `gh issue create`、在 `.scratch/` 下写 Markdown 文件，还是遵循你描述的其他工作流。请选择你实际跟踪此仓库工作的地方。

默认姿态：这些技能为 GitHub 设计。若 `git remote` 指向 GitHub，则提议它。若 `git remote` 指向 GitLab（`gitlab.com` 或自托管主机），则提议 GitLab。其他情况（或用户偏好）提供：

- **GitHub**：issue 位于仓库 GitHub Issues（使用 `gh` CLI）

- **GitLab**：issue 位于仓库 GitLab Issues（使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI）

- **本地 Markdown**：issue 作为 `.scratch/<feature>/` 下文件存在于本仓库（适合个人项目或无远程仓库）

- **其他**（Jira、Linear 等）：请用户用一段话描述工作流；技能将其记录为自由形式正文

在 `docs/agents/issue-tracker.md` 记录选择。GitHub 与 GitLab 模板带有“PR 作为请求入口”标志，默认**关闭**。保持关闭且不要主动提及：想让外部 PR 进入分诊队列的用户之后可在文件中打开。

GitHub 或 GitLab 跟踪器需要可访问仓库。用户选择后，若无 `git remote` 指向该主机，则从其获取仓库 URL 并接好（需要时 `git init`、`git remote add origin <url>`），再继续。完成条件是从此目录内运行 `gh repo view` / `glab repo view` 能打印项目；若不能，停止并告诉用户缺少什么。

**B 部分：分诊标签词汇。**若未安装 `triage` 技能（探索会告诉你），完全跳过，因为未安装技能不需要标签。

若已安装，只问一个问题：

> 你要保留默认分诊标签吗？（推荐：**是**）

默认值为五个标准角色，每个标签字符串等于名称：`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix`。回答**是**，原样写入。只有用户说否时（通常因跟踪器已使用其他名称，如用 `bug:triage` 代表 `needs-triage`），收集覆盖项，让 `triage` 应用现有标签而非创建重复项。

**C 部分：领域文档。**默认**单上下文**（仓库根目录一个 `GLOSSARY.md` + `docs/adr/`）。几乎适合所有仓库；无需询问直接写入。

仅当探索发现 monorepo 信号时提供**多上下文**（根 `GLOSSARY-MAP.md` 指向各上下文 `GLOSSARY.md`）。随后确认所需布局。

### 3. 确认并编辑

向用户展示以下草稿：

- 要加入所编辑 `CLAUDE.md` / `AGENTS.md` 的 `## Agent skills` 块（选择规则见步骤 4）

- `docs/agents/issue-tracker.md`、`docs/agents/domain.md` 和 `docs/agents/triage-labels.md` 的内容（最后一项仅安装 `triage` 时）

让用户在写入前编辑。

### 4. 写入

**选择要编辑的文件：**

- 若 `CLAUDE.md` 存在，编辑它。

- 否则若 `AGENTS.md` 存在，编辑它。

- 若两者都不存在，询问用户创建哪一个；不要替他们选择。

`CLAUDE.md` 已存在时绝不创建 `AGENTS.md`（反之亦然）；始终编辑已有文件。

若所选文件已有 `## Agent skills` 块，就地更新内容，而非追加重复块。不要覆盖用户对周围部分的编辑。

该块：

```markdown
## Agent skills

### Issue tracker

[issue 跟踪位置的一行摘要]。参见 `docs/agents/issue-tracker.md`。

### Triage labels

[标签词汇的一行摘要]。参见 `docs/agents/triage-labels.md`。

### Domain docs

[布局的一行摘要：“单上下文”或“多上下文”]。参见 `docs/agents/domain.md`。
```

只有在安装 `triage` 且 B 部分运行时，才包含 `### Triage labels` 子块并写 `docs/agents/triage-labels.md`。否则两者都省略。

当 B 部分在 GitHub 或 GitLab 上运行，为跟踪器缺少的每个配置标签创建（`gh label create` / `glab label create`）。

然后用此技能文件夹中的种子模板作为起点写文档：

- [issue-tracker-github.md](./issue-tracker-github.md)：GitHub issue 跟踪器

- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md)：GitLab issue 跟踪器

- [issue-tracker-local.md](./issue-tracker-local.md)：本地 Markdown issue 跟踪器

- [triage-labels.md](./triage-labels.md)：标签映射（仅安装 `triage` 时）

- [domain.md](./domain.md)：领域文档消费者规则 + 布局

对“其他”issue 跟踪器，根据用户描述从头写 `docs/agents/issue-tracker.md`。

### 5. 完成

告诉用户设置完成，以及哪些工程技能之后会读取这些文件。说明他们可稍后直接编辑 `docs/agents/*.md`；只有切换 issue 跟踪器或从头重来时才需重跑本技能。
