# Gemini CLI 工具映射

技能用动作表达（“派发子代理”“创建待办”“读取文件”）。在 Gemini CLI 上，这些映射到下列工具。

| 技能要求的动作 | Gemini CLI 对应项 |
|----------------------|----------------------|
| 读取文件 | `read_file` |
| 一次读取多个文件 | `read_many_files` |
| 创建文件 | `write_file` |
| 编辑文件 | `replace` |
| 运行 shell 命令 | `run_shell_command` |
| 搜索文件内容 | `grep_search` |
| 按名称查找文件 | `glob` |
| 列出文件和子目录 | `list_directory` |
| 获取 URL | `web_fetch` |
| 搜索网络 | `google_web_search` |
| 调用技能 | `activate_skill` |
| 派发子代理（`Subagent (general-purpose):` 模板） | 用 `invoke_agent`，设置 `agent_name: "generalist"`（可经 `@generalist` 对话语法调用，见[子代理支持](#subagent-support)） |
| 多个并行派发 | 同一响应中多次 `invoke_agent` |
| 任务跟踪（“创建待办”“标记完成”） | `write_todos`（状态：pending、in_progress、completed、cancelled、blocked） |

## 指令文件

技能提到“你的指令文件”时，Gemini CLI 中为 **`GEMINI.md`**。它按层级加载：全局 `~/.gemini/GEMINI.md`、工作区目录和祖先目录的项目文件，以及工具访问子目录文件时的子目录 `GEMINI.md`；项目级 `GEMINI.md` 沿目录层级生效。

## 个人技能目录

用户级技能位于 **`~/.gemini/skills/`**，跨运行时别名是 **`~/.agents/skills/`**（与 Codex、Copilot CLI 共享）。同范围两目录都存在时 `.agents/skills/` 优先。每个技能是含 `SKILL.md` 的子目录（带 `name` 与 `description` 前置元数据）。

## 子代理支持

Gemini CLI 通过 `invoke_agent` 派发子代理，参数为 `agent_name` 和 `prompt`。聊天语法 `@generalist <prompt>` 等价于设置 `agent_name: "generalist"` 调用 `invoke_agent`。内置代理名包括 `generalist`、`cli_help`、`codebase_investigator`，启用浏览器工具时还有 `browser_agent`。

技能使用 `Subagent (general-purpose):` 派发，并引用提示模板（如 `superpowers:subagent-driven-development` 的 `./implementer-prompt.md`）或提供内联提示。Gemini CLI 对应方式：

| 技能派发形式 | Gemini CLI 对应方式 |
|---------------------|----------------------|
| 引用 `*-prompt.md` 模板（实现者、任务审查者、代码审查者等） | 填写模板，然后以 `agent_name: "generalist"` 和填好的提示调用 `invoke_agent` |
| 引用 `superpowers:requesting-code-review` 的 `./code-reviewer.md` | 以 `agent_name: "generalist"` 和填好的审查模板调用 `invoke_agent` |
| 内联提示（无模板） | 以 `agent_name: "generalist"` 和你的内联提示调用 `invoke_agent` |

### 填写提示

技能模板含 `{WHAT_WAS_IMPLEMENTED}` 或 `[FULL TEXT of task]` 等占位符。传给 `invoke_agent` 前填完。模板本身包含代理角色、审查标准和预期输出格式，子代理会遵循。

### 并行派发

Gemini CLI 支持并行子代理。可在同一响应中多次调用 `invoke_agent`（或一条提示中多次 `@generalist`）并行运行独立工作。依赖任务保持顺序，但不要仅为历史简单而串行执行独立任务。

## 其他 Gemini CLI 工具

这些工具为 Gemini CLI 特有：

| 工具 | 用途 |
|------|---------|
| `save_memory`（旧版） | `experimental.memoryV2 = false` 时跨会话保存事实 |
| `get_internal_docs` | 查阅 Gemini CLI 内置文档 |
| `ask_user` | 向用户提出结构化问题（文本 / 单选 / 多选） |
| `enter_plan_mode` / `exit_plan_mode` | 进入及退出只读计划模式 |
| `update_topic` | 更新当前对话主题/战略意图元数据 |
| `complete_task` | 通知 Gemini 子代理已完成，并将结果返回父代理 |
| `tracker_create_task`, `tracker_update_task`, `tracker_get_task`, `tracker_list_tasks`, `tracker_add_dependency`, `tracker_visualize` | 支持依赖与可视化的丰富任务跟踪器 |
| `read_mcp_resource`, `list_mcp_resources` | 访问 MCP 资源 |
