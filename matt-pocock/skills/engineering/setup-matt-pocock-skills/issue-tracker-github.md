# 问题跟踪器：GitHub

本仓库的问题与规格作为 GitHub 问题保存。所有操作使用 `gh` CLI。

## 约定

- **创建问题**：`gh issue create --title "..." --body "..."`。多行正文使用 heredoc。

- **读取问题**：`gh issue view <number> --json number,title,body,labels,comments`。

- **列出问题**：`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`，配合适当的 `--label` 与 `--state` 筛选。

- **把问题设成父问题的子问题**：`gh issue create --parent <parent> ...`，之后也可 `gh issue edit <parent> --add-sub-issue <child>`（`gh` 2.94+）。较旧 `gh`：`gh api --method POST repos/<owner>/<repo>/issues/<parent>/sub_issues -F sub_issue_id=<child-db-id>`（数据库 id，如下文 **Blocking**）。不支持子问题时，在子问题正文顶部写 `Part of #<parent>`。

- **阻塞**：GitHub 的**原生问题依赖**，即标准且 UI 可见的表示。用 `gh issue create --blocked-by <n>,<n> ...` 或 `gh issue edit <child> --add-blocked-by <blocker>`（`gh` 2.94+）添加边。较旧 `gh`：`gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`，其中 `<blocker-db-id>` 是阻塞者的数字**数据库 id**（`gh api repos/<owner>/<repo>/issues/<n> --jq .id`，_不是_ `#number` 或 `node_id`）。依赖不可用时，回退到子正文顶部一行 `Blocked by: #<n>, #<n>`。所有阻塞者关闭后，工单才解除阻塞。

- **统计未关闭阻塞者**：`gh api repos/<owner>/<repo>/issues/<n> --jq .issue_dependencies_summary.blocked_by`（仅未关闭阻塞者；0 表示可开始）。`gh issue view <n> --json blockedBy` 也会列已关闭阻塞者，故要筛选：`--jq '[.blockedBy.nodes[] | select(.state == "OPEN")] | length'`。

- **评论问题**：`gh issue comment <number> --body "..."`

- **添加／移除标签**：`gh issue edit <number> --add-label "..."` / `--remove-label "..."`

- **关闭**：用 `gh issue comment <number> --body "..."` 发布说明，再 `gh issue close <number>`。对已关闭问题使用 `gh issue close --comment` 会丢弃评论且仍以 0 退出。

从 `git remote -v` 推断仓库；`gh` 在克隆内运行时会自动处理。

只向用户自己的仓库提交问题。绝不要提交到 `mattpocock/skills`（这些技能的来源仓库），除非用户拥有它。在 fork 中，`gh` 可能默认上游父仓库，因此会话第一次 `gh issue create` 前，用 `gh repo view --json nameWithOwner` 检查目标；若不是用户仓库，与其确认。

## 拉取请求作为分诊界面

**PR 作为请求界面：否。** _（仓库把外部 PR 当作功能请求时设为 `yes`；`/triage` 读取此标志。）_

设为 `yes` 时，PR 通过相同标签与状态流转，使用对应 `gh pr` 命令：

- **读取 PR**：`gh pr view <number>`，再 `gh pr view <number> --comments`（非 TTY 下 `--comments` 只打印评论，不含正文），差异用 `gh pr diff <number>`。

- **列出待分诊外部 PR**：`gh api --paginate 'repos/{owner}/{repo}/pulls?state=open' --jq '.[] | select(.author_association | IN("OWNER","MEMBER","COLLABORATOR") | not) | {number, title, author: .user.login, author_association, labels: [.labels[].name]}'`。

- **评论／标签／关闭**：`gh pr comment`、`gh pr edit --add-label`/`--remove-label`、`gh pr close`。

GitHub 的问题和 PR 共用编号空间，因此裸 `#42` 可能指任一者：先 `gh pr view 42`，失败再 `gh issue view 42`。

## 技能说“发布到问题跟踪器”时

创建一个 GitHub 问题。

## 技能说“获取相关工单”时

按上文**读取问题**操作。

## 寻路操作

供 `/wayfinder` 使用。**地图**是一个问题，**子**问题作为工单。

- **地图**：一个标记 `wayfinder:map` 的问题，包含 Notes / Decisions-so-far / Fog 正文。`gh issue create --label wayfinder:map`。

- **子工单**：作为 GitHub 子问题链接到地图的问题（见**把问题设成父问题的子问题**）。未启用子问题时，把子问题加入地图正文任务列表，并在子正文顶部写 `Part of #<map>`。标签：`wayfinder:<type>`（`research`/`prototype`/`grilling`/`task`）。认领后，工单分配给推动工作的开发者。

- **阻塞**：见约定中的 **Blocking**。

- **前沿查询**：列出地图的未关闭子问题（`gh issue list --state open`，限定为地图子问题／任务列表），排除有未关闭阻塞者（见 **Count open blockers**，或 `Blocked by` 行中有未关闭问题）或有受让人的项；地图顺序最前者优先。

- **认领**：`gh issue edit <n> --add-assignee @me`，会话第一次写入。

- **解决**：`gh issue comment <n> --body "<answer>"`，再 `gh issue close <n>`，然后向地图的 Decisions-so-far 追加上下文指针（概要 + 链接）。
