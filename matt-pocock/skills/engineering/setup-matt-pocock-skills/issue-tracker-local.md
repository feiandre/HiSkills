# Issue 跟踪器：本地 Markdown

本仓库的 issue 和规格位于 `.scratch/` 中的 markdown 文件。

## 约定

- 每个功能一个目录：`.scratch/<feature-slug>/`

- 规格为 `.scratch/<feature-slug>/spec.md`

- 实现 issue 每张票一个文件，位于 `.scratch/<feature-slug>/issues/<NN>-<slug>.md`，从 `01` 编号，绝不使用单个合并票文件

- 分诊状态记录为每个 issue 文件顶部附近的 `Status:` 行（角色字符串见 `triage-labels.md`）

- 评论和对话历史追加到文件底部 `## Comments` 标题下

## 技能说“发布到 issue 跟踪器”时

在 `.scratch/<feature-slug>/` 下创建新文件（需要时创目录）。

## 技能说“获取相关票”时

读取引用路径的文件。用户通常直接给出路径或 issue 编号。

## 寻路操作

由 `/wayfinder` 使用。**地图**是一个文件，每张票对应一个**子**文件。

- **地图**：`.scratch/<effort>/map.md`（Notes／Decisions-so-far／Fog 正文）。

- **子票**：`.scratch/<effort>/issues/NN-<slug>.md`，从 `01` 编号，正文写问题。`Type:` 行记录票类型（`research`/`prototype`/`grilling`/`task`）；`Status:` 行记录 `claimed`/`resolved`。

- **阻塞**：顶部附近的 `Blocked by: NN, NN` 行。其列出的每个文件都标记为 `resolved` 时，票才解除阻塞。

- **前沿**：扫描 `.scratch/<effort>/issues/` 中开放、未阻塞且未认领的文件；编号最小者优先。

- **认领**：任何工作前设置 `Status: claimed` 并保存。

- **解决**：在 `## Answer` 标题下追加答案，设置 `Status: resolved`，再向 `map.md` 的 Decisions-so-far 追加上下文指针（要点＋链接）。
