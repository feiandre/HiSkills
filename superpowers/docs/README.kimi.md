# 面向 Kimi Code 的 Superpowers

在 [Kimi Code](https://github.com/MoonshotAI/kimi-code) 中使用 Superpowers 的完整指南。

## 安装

Superpowers 可在 Kimi Code 插件市场中找到。

打开插件管理器：

```text
/plugins
```

转到 `Marketplace` > `Superpowers` 并安装。

也可从本仓库安装：

```text
/plugins install https://github.com/obra/superpowers
```

若要针对 `dev` 做未发布验证，显式固定分支：

```text
/plugins install https://github.com/obra/superpowers/tree/dev
```

Kimi Code 将插件改动应用于新会话。安装、更新、启用、禁用或重载插件后，用 `/new` 启动全新会话。

## 工作原理

Kimi 插件清单位于 `.kimi-plugin/plugin.json`。

清单做三件事：

1. 指向现有 `skills/` 目录。

2. 通过 `sessionStart.skill` 在会话启动时加载 `using-superpowers`。

3. 通过 `skillInstructions` 提供 Kimi 专用工具映射。

Kimi Code 从此仓库读取 Superpowers 技能。没有复制技能、符号链接、钩子或额外运行时依赖。

## 工具映射

技能描述动作，而非硬编码某运行时的工具名。在 Kimi Code 上解析为：

- “询问用户”/“提出澄清问题” -> `AskUserQuestion`

- “创建待办”/“在待办中标记完成” -> `TodoList`

- “派发子代理” -> `Agent`

- “调用技能” -> Kimi Code 原生 `Skill` 工具

- “读取文件”/“写文件”/“编辑文件” -> `Read`、`Write`、`Edit`

- “运行 shell 命令” -> `Bash`

- “搜索文件内容” -> `Grep`

- “按路径或模式查找文件” -> `Glob`

- “获取 URL” -> `FetchURL`

- “搜索网络” -> `WebSearch`

## 更新

使用 Kimi Code 插件管理器：

```text
/plugins
```

选择 Superpowers 并在那里更新。更新后用 `/new` 启动全新会话。

## 故障排除

### 插件未加载

1. 运行 `/plugins info superpowers` 并检查诊断。

2. 确认插件已启用。

3. 安装或更新后用 `/new` 启动全新会话。

### 直接从 GitHub 安装却使用了旧版本

裸仓库 URL 存在最新 GitHub release 时，Kimi Code 会安装该 release。要在下一个 Superpowers 版本前测试未发布改动，请显式安装分支：

```text
/plugins install https://github.com/obra/superpowers/tree/dev
```

### 技能未触发

1. 确认 `/plugins info superpowers` 显示插件已启用。

2. 用 `/new` 启动全新会话。

3. 尝试验收提示：`Let's make a react todo list`（我们来做一个 React 待办列表）。正常安装应在写代码前加载 `brainstorming`。
