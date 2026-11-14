# Antigravity CLI（`agy`）工具映射

技能以动作表述要求（“派遣子代理”“创建待办”“读取文件”）。在 Antigravity CLI（`agy`）中，这些对应以下工具。

| 技能请求的动作 | Antigravity CLI 对应能力 |
|----------------------|----------------------|
| 派遣子代理（`Subagent (general-purpose):` 模板） | `invoke_subagent` 配合内置 `TypeName`：完整能力工作用 `self`，只读用 `research` |
| 任务跟踪（“创建待办”“标记完成”） | **任务产物**：用 `write_to_file`，设置 `IsArtifact: true` 与 `ArtifactType: "task"`（参见[任务跟踪](#task-tracking)）。**不是** `manage_task`，后者管理后台进程。 |

## 任务跟踪

Antigravity **没有待办工具**（`manage_task` 管理后台进程，即 `list`／`kill`／`status`／`send_input`，*不是*检查清单）。技能要求创建待办列表或跟踪任务时，维护一份**任务产物**：以 `write_to_file` 保存的 Markdown 检查清单（`IsArtifact: true`、`ArtifactMetadata.ArtifactType: "task"`），随工作进展用 `replace_file_content`／`multi_replace_file_content` 编辑。

任何多步骤任务开始时，创建列出计划每个步骤的任务产物。每完成一步，编辑产物标记完成（`- [x]`）。计划改变就更新清单。保持最新：它是剩余工作的事实来源；对话变长后，每步开始前重新读取。
