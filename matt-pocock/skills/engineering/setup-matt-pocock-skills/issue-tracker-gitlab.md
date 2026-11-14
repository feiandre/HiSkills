# 问题跟踪器：GitLab

本仓库的问题和规格作为 GitLab 问题存在。所有操作使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI。

## 约定

- **创建问题**：`glab issue create --title "..." --description "..."`。多行描述使用 heredoc；传 `--description -` 可打开编辑器。

- **读取问题**：`glab issue view <number> --comments`。机器可读输出使用 `-F json`。

- **列出问题**：`glab issue list -O json`，配合适当 `--label` 过滤。

- **评论问题**：`glab issue note <number> --message "..."`。GitLab 把评论称为 notes。

- **添加／移除标签**：`glab issue update <number> --label "..."`／`--unlabel "..."`。多个标签可用逗号分隔或重复标志。

- **关闭**：`glab issue close <number>`。`glab issue close` 不接受关闭评论，因此先用 `glab issue note <number> --message "..."` 发布说明，再关闭。

- **合并请求**：GitLab 把 PR 称为 merge requests。使用 `glab mr create`、`glab mr view`、`glab mr note` 等，形状与 `gh pr ...` 相同，用 `mr` 替代 `pr`，用 `note`／`--message` 替代 `comment`／`--body`。

从 `git remote -v` 推断仓库；在克隆中运行时 `glab` 会自动这样做。

## 将合并请求作为分诊表面

**MR 作为请求表面：否。** *（若本仓库将外部合并请求视为功能请求，设为 `yes`；`/triage` 读取此标志。）*

设为 `yes` 时，MR 通过对应 `glab mr` 命令使用与问题相同的标签和状态：

- **读取 MR**：`glab mr view <number> --comments`，差异用 `glab mr diff <number>`。

- **列出待分诊外部 MR**：`glab mr list -O json`，只保留作者不是项目成员／所有者的 MR。

- **评论／标记／关闭**：`glab mr note`、`glab mr update --label`／`--unlabel`、`glab mr close`。

与 GitHub 不同，GitLab 分别编号问题和 MR，因此知道维护者指哪个表面后，`#42` 没有歧义。

## 技能要求“发布到问题跟踪器”时

创建 GitLab 问题。

## 技能要求“获取相关工单”时

运行 `glab issue view <number> --comments`。

## 寻路操作

供 `/wayfinder` 使用。**地图**是一个问题，**子**问题作为工单。

- **地图**：带 `wayfinder:map` 标签的问题，保存 Notes／Decisions-so-far／Fog 正文。`glab issue create --label wayfinder:map`。有原生史诗的 GitLab 层级可用史诗保存地图；带标签问题在各处都可用。

- **子工单**：描述顶部含 `Part of #<map>` 并链接到地图（`glab issue create --linked-issues <map> --link-type relates_to`）的问题，标签为 `wayfinder:<type>`（`research`／`prototype`／`grilling`／`task`）。认领后分配给执行开发者。

- **阻塞**：GitLab **原生阻塞链接**是界面可见的规范表示。用 `/blocked_by #<n>` 快捷动作作为 note 发布（`glab issue note <child> --message "/blocked_by #<blocker>"`）。原生阻塞链接属于 Premium／Ultimate；免费层或不可用时可退回到描述顶部写 `Blocked by: #<n>, #<n>`。所有阻塞项关闭时，工单解除阻塞。

- **前沿查询**：用 `glab api projects/:id/issues/<map>/links` 列出地图子项，保留带 `wayfinder:<type>` 标签的开放问题；剔除有开放阻塞项者：原生 `blocked_by` 指向开放问题（`glab api projects/:id/issues/<child-iid>/links`）、`Blocked by` 行中的开放问题，或已有受理人；地图顺序最早者优先。

- **认领**：`glab issue update <n> --assignee @me`，这是会话的第一次写入。

- **解决**：`glab issue note <n> --message "<answer>"`，再 `glab issue close <n>`，然后向地图 Decisions-so-far 追加上下文指针（gist + 链接）。
