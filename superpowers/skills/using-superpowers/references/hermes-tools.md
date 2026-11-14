# Hermes Agent 工具映射

技能用动作表达（“派发子代理”“创建待办”“读取文件”）。在 Hermes Agent 上映射如下。

## 工具

| 技能要求的动作 | Hermes 工具 |
|---|---|
| 读取文件 | `read_file` |
| 创建文件 | `write_file` |
| 编辑文件（定向补丁） | `patch` |
| 运行 shell 命令 | `terminal` |
| 搜索文件内容 | `search_files` |
| 按名称查找文件 | 使用 `find` 的 `terminal` |
| 获取 URL / 读取网页 | `web_extract(urls=[...])` |
| 搜索网络 | `web_search(query=...)` |
| 派发子代理 | `delegate_task(goal=..., context=..., toolsets=[...], role="leaf")` |
| 任务跟踪 | `todo` 工具 |
| 调用技能 | `skill_view("skill-name")` |

## 指令文件

技能提到“你的指令文件”时，Hermes Agent 中是项目目录的 **`AGENTS.md`**，或全局 **`~/.hermes/SOUL.md`** 的 **`SOUL.md`**。

## 调用技能

Hermes Agent 有 `skills` 工具集，包含 `skill_view` 与 `skills_list`。调用 superpowers 技能：

```
skill_view("brainstorming")
skill_view("test-driven-development")
```

`skill_view` 找不到 superpowers 技能时（插件完全注册前可能不在目录），回退直接读取 SKILL.md：

```
read_file(path="~/.hermes/plugins/superpowers/skills/<skill-name>/SKILL.md")
```

此回退方式与没有原生技能加载的其他平台相同。

## 子代理派发

用 `delegate_task` 为并行或顺序工作流生成隔离子代理：

```
delegate_task(goal="...", context="...", toolsets=[...], role="leaf")
```

`delegate_task` 不可用时在当前会话内工作，不要伪造工具调用。

## 任务跟踪

会话内用 `todo` 跟踪任务。多代理任务板可用时使用 `hermes kanban` CLI。旧 `TodoWrite` 引用按任务跟踪动作理解。
