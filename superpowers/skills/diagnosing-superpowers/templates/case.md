# 案例：<session-id>

工作区：~/.superpowers/diagnosing-superpowers/<session-id>/
创建时间：<ISO timestamp>

## 问题陈述（与人类伙伴确认）

目标是 superpowers 缺陷报告：是 | 否

## 会话

| 角色 | 会话 ID | 绝对路径 | 行数 | 字节数 | 最长行（字节） | 第一条提示（前 120 字符） | 首时间戳 |
|---|---|---|---|---|---|---|---|
| main | | | | | | | |
| subagent | | | | | | | |

拒绝的候选：<id — path — why rejected>，或“无”。

读取时仍在运行：是 | 否（mtime <ISO>，行数 <N>）

## 环境

- 操作系统：<name and version>

- 宿主：<name> <version>

- 见到的模型：<model id — where (main / subagent id)>

- Superpowers 安装根目录：<path>；版本 <x.y.z>；git sha <sha or "not a checkout">

- 会话期间读取或注入的技能文件：

| 技能／来源路径 | sha1 或不可用 | 来源 | 支持位置 |
|---|---|---|---|

将环境和技能观察标记为历史证据、未验证快照、当前观察或未知。宣布历史信息不可用前，检查提供的来源说明、归档和捕获的技能正文。原始路径缺失不会抹除保留副本。当前版本／mtime 不能证明历史版本；一个捕获技能正文不能认证整个安装。

- 配置的其他插件／扩展／MCP 服务器：<list, or "none found">

- 存在的指令文件（仅路径）：<list>

## 所有读者适用的上下文安全规则

- 读取此处列出的任何文件前，遵循 `references/context-safety.md`。

- 子智能体会话记录中，“user”是父智能体。

## 已发现来源及记录含义

- 查阅来源：<absolute path, tool, help, or documentation source>

- 提取命令或查询：<bounded commands or tool queries used for each source>

- 目标身份证据：<session id, working directory, timestamps, matching content, and supporting record locations>

- 关联会话：<session id, relationship, and supporting record locations, or "none found">

- 人类消息：<record shape and evidence for its meaning>

- 注入消息和父派发：<record shape and evidence for its meaning>

- 助手消息：<record shape and evidence for its meaning>

- 工具调用和结果：<record shapes, how they match, and evidence for those meanings>

- 使用计数：<fields, incremental or cumulative semantics, units, and evidence, or "unavailable">

- 计时：<fields, units, event boundaries, and evidence, or "unavailable">

- 其他相关记录：<models, versions, compactions, or other meanings and evidence>

- 未解决信息：<missing, inaccessible, ambiguous, or absent information, or "none">
