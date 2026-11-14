# Muse 工具映射

技能用动作表达（“派发子智能体”“创建待办”“读取文件”）。在 Muse 上，这些对应以下工具。

| 技能请求的动作 | Muse 等价工具 |
|---|---|
| 读取文件 | `read_file` |
| 读取多个文件 | `read_file`（多次调用）或 `search` |
| 创建新文件 | `write_file` |
| 编辑文件 | `edit_file` |
| 运行 shell 命令 | `bash` |
| 搜索文件内容 | `search` |
| 按名称查找文件 | `search` 配合 `glob` |
| 获取 URL | `web_fetch` |
| 搜索网页 | `web_search` |
| 调用技能 | 对 `skills/<name>/SKILL.md` 使用 `read_file`，或原生技能工具 |
| 派发子智能体（`Subagent (general-purpose):` 模板） | `subagent_spawn` 并填写提示 |
| 任务跟踪（“创建待办”“标记完成”） | `write_todos` 或 `bash` 任务文件 |
| 向用户提问 | `request_user_input` |

## 指令文件

技能提到“你的指令文件”时，Muse 上指项目根目录中的 **`CLAUDE.md`** 或 **`AGENTS.md`**。Muse 在配置的位置按层级加载它们。

## 技能调用

Muse 通过 `muse skills` 提供原生技能支持。调用 Superpowers 技能时，读取其 `SKILL.md` 并遵循指令。引导（`using-superpowers`）通过插件钩子在 `SessionStart` 自动注入——你已经在遵循它，不要重新加载。

## 子智能体派发

使用 `subagent_spawn` 将工作委派给隔离子智能体。派发前填写提示模板（如 `implementer-prompt.md`、`task-reviewer-prompt.md`）。没有子智能体工具时，直接内联完成工作，不要编造工具调用。

## 任务跟踪

使用 `write_todos` 跟踪检查清单。每个技能清单项创建一个待办，并随进度标记为进行中／已完成。`write_todos` 不可用时，通过 `write_file`/`edit_file` 维护 markdown 任务文件。
