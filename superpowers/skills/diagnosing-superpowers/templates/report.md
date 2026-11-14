# 会话诊断：<session-id>

报告路径：~/.superpowers/diagnosing-superpowers/<session-id>/report.md
撰写时间：<ISO 时间戳>

## 1. 问题陈述（必填）

<Copied from the case file.>（从案例文件复制。）

## 2. 分诊结论（必填）

<What the evidence shows happened around the reported problem. Prose, with `path:line` after every claim. State confidence: high / medium / low, and what would raise it. No statement about what superpowers should do.> （中文：证据显示报告问题前后发生了什么。正文中每项断言后附 `path:line`。说明置信度：高／中／低，以及什么会提高它。不要说明 superpowers 应该做什么。）

## 3. 环境（必填）

- 操作系统：

- 运行环境与版本：

- 观察到的模型：

- Superpowers 安装根目录／版本／git sha：

- 读取或注入的技能文件（案例文件中的 sha1 表）：

- 其他插件、扩展、MCP 服务器：

- 存在的指令文件（仅路径）：

将每个环境字段及技能观察标为历史证据、未验证快照、当前观察或未知，并记录支持证据的位置。

## 4. 检查的会话（必填）

| 角色 | 会话 ID | 绝对路径 | 行数 | 字节数 |
|---|---|---|---|---|

被排除的候选项：<id — path — why>（ID——路径——原因），或“无”。

## 5. 时间线（必填）

每条人类手输提示词占一行。事件列列出技能调用、子代理派遣、上下文压缩、错误、恢复与中止。

| 轮次 | 行 | 时间 | 请求（一行） | 事件 |
|---|---|---|---|---|

## 6. 发现（必填，每个维度一个子节）

每项发现：

```
- finding: <one sentence>（一句话）
  evidence: <path:line> — “<short quote>”（简短引文）
  turns: <first>–<last>（首轮——末轮）
  confidence: 高 | 中 | 低
```

没有发现的维度写 `none found — checked: <what was checked>`（含义：未发现——已检查：<检查了什么>）。

### 6.1 技能时间线

### 6.2 计划遵循情况

### 6.3 重复工作

### 6.4 磕绊

### 6.5 质量证据

### 6.6 请求冲突

### 6.7 成本与时间

### 6.8 使用的其他插件与技能

## 7. Superpowers 是否涉及其中（必填）

未见迹象 | 可能 | 很可能

证据行：<path:line 列表>。本节只说明是否涉及，不指认缺陷，不提出变更。

## 8. 覆盖说明（必填）

- 未读取：<ranges, files, and why>（范围、文件和原因）

- 运行环境中不可用的功能：<list or none>（列表或无）

- 读取时会话仍在进行：是／否

- 供人类协作者复核：<list or none>（列表或无）

## 9. 相似会话（仅应请求提供）

| 会话 ID | 路径 | 日期 | 运行环境 | 匹配之处 | 不匹配之处 |
|---|---|---|---|---|---|
