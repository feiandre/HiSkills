# 可视头脑风暴重构：浏览器展示，终端命令

**日期：** 2026-02-19
**状态：** 已批准
**范围：** `lib/brainstorm-server/`、`skills/brainstorming/visual-companion.md`、`tests/brainstorm-server/`

## 问题

可视头脑风暴期间，Claude 将 `wait-for-feedback.sh` 作为后台任务运行，并在 `TaskOutput(block=true, timeout=600s)` 上阻塞。这会独占 TUI，用户在可视头脑风暴运行时无法向 Claude 输入。浏览器成为唯一输入通道。

Claude Code 执行模型按轮次运行。单轮内 Claude 无法同时监听两个通道。阻塞式 `TaskOutput` 模式是错误原语，它模拟平台并不支持的事件驱动行为。

## 设计

### 核心模型

**浏览器＝交互展示。** 显示模型稿，让用户点击选择；选择记录在服务端。

**终端＝会话通道。** 始终不阻塞、始终可用；用户在这里与 Claude 交谈。

### 循环

1. Claude 将会话 HTML 文件写入会话目录

2. 服务器通过 chokidar 检测，并通过 WebSocket 推送浏览器重载（不变）

3. Claude 结束轮次，告诉用户查看浏览器并在终端回应

4. 用户查看浏览器，可选点击选项，然后在终端输入反馈

5. 下一轮，Claude 读取 `$SCREEN_DIR/.events` 获取浏览器交互流（点击、选择），再与终端文字合并

6. 迭代或推进

没有后台任务，没有 `TaskOutput` 阻塞，没有轮询脚本。

### 关键删除：`wait-for-feedback.sh`

完全删除。其用途是桥接“服务器把事件日志写到 stdout”与“Claude 收到这些事件”。`.events` 文件取代它：服务器直接写入用户交互事件，Claude 用平台提供的文件读取机制读取。

### 关键新增：`.events` 文件（逐屏事件流）

服务器将所有用户交互事件写入 `$SCREEN_DIR/.events`，每行一个 JSON。这样 Claude 获得当前屏幕的完整交互流，不只最终选择，还包括探索路径（点 A、再点 B、最后选 C）。

用户探索选项后的示例：

```jsonl
{"type":"click","choice":"a","text":"Option A - Preset-First Wizard","timestamp":1706000101}
{"type":"click","choice":"c","text":"Option C - Manual Config","timestamp":1706000108}
{"type":"click","choice":"b","text":"Option B - Hybrid Approach","timestamp":1706000115}
```

- 在单屏内只追加。每个用户事件作为新行追加。

- chokidar 检测到新 HTML 文件（推送新屏）时删除该文件，防止旧事件延续。

- Claude 读取时文件不存在，表示未发生浏览器交互；Claude 只使用终端文字。

- 文件只含用户事件（`click` 等），不含服务器生命周期事件（`server-started`、`screen-added`），保持小而有针对性。

- Claude 可读完整流理解探索过程，或只看最后一个 `choice` 事件取得最终选择。

## 按文件变更

### `index.js`（服务器）

**A. 将用户事件写入 `.events` 文件。**

WebSocket `message` 处理器记录 stdout 后，用 `fs.appendFileSync` 将事件作为 JSON 行追加到 `$SCREEN_DIR/.events`。只写用户交互事件（`source: 'user-event'`），不写服务器生命周期事件。

**B. 新屏时清空 `.events`。**

chokidar `add` 处理器检测到新 `.html` 文件时，存在则删除 `$SCREEN_DIR/.events`。这是确定的“新屏”信号，优于 GET `/` 清空，因为后者每次重载都触发。

**C. 替换 `wrapInFrame` 的内容注入。**

现有正则锚定正在删除的 `<div class="feedback-footer">`。改为注释占位符：删除 `#claude-content` 内默认内容（`<h2>Visual Brainstorming</h2>` 和副标题段落），换成 `` 标记。内容注入变为 `frameTemplate.replace('', content)`。这更简单，也不怕模板格式变化。

### `frame-template.html`（UI 框架）

**移除：**

- `feedback-footer` div（textarea、Send 按钮、label、`.feedback-row`）

- 相关 CSS（`.feedback-footer`、`.feedback-footer label`、`.feedback-row`、其中 textarea 与按钮样式）

**新增：**

- `#claude-content` 内 `` 占位符，替代默认文本

- 在原底部位置增加选择指示栏，两种状态：

- 默认：“Click an option above, then return to the terminal”（点击上方选项，然后返回终端）

- 选择后：“Option B selected — return to terminal to continue”（已选选项 B——返回终端继续）

- 指示栏 CSS（克制，视觉权重接近现有页头）

**保持不变：**

- 标题为“Brainstorm Companion”的页头和连接状态

- `.main` 包装器与 `#claude-content` 容器

- 所有组件 CSS（`.options`、`.cards`、`.mockup`、`.split`、`.pros-cons`、占位符、模拟元素）

- 暗／亮主题变量与媒体查询

### `helper.js`（客户端脚本）

**移除：**

- `sendToClaude()` 函数及“Sent to Claude”整页覆盖

- `window.send()` 函数（与已移除 Send 按钮绑定）

- 表单提交处理器——没有反馈 textarea 后无用，还会制造日志噪声

- 输入变化处理器——同理

- `pageshow` 事件监听器（为修复 textarea 持久性而加，现在没有 textarea）

**保留：**

- WebSocket 连接、重连逻辑、事件队列

- 服务器推送时 `window.location.reload()` 重载处理器

- `window.toggleSelect()` 选择高亮

- `window.selectedChoice` 跟踪

- `window.brainstorm.send()` 与 `window.brainstorm.choice()`——不同于已删除的 `window.send()`；它们调用 `sendEvent` 通过 WebSocket 记录到服务器，对自定义整页文档有用。

**收窄：**

- 点击处理器只捕获 `[data-choice]` 点击，不捕获所有按钮／链接。浏览器作为反馈通道时需要广捕获，现在只跟踪选择。

**新增：**

- 点击 `data-choice` 时更新选择指示栏文字，显示所选选项。

**从 `window.brainstorm` API 移除：**

- `brainstorm.sendToClaude`——已不存在

### `visual-companion.md`（技能指令）

**重写“The Loop”章节**为上述非阻塞流程。删除以下所有引用：

- `TaskOutput` 阻塞

- 超时／重试逻辑（600 秒超时、30 分钟上限）

- 描述 `send-to-claude` JSON 的“User Feedback Format”章节

**替换为：**

- 新循环（写 HTML → 结束轮次 → 用户在终端回应 → 读 `.events` → 迭代）

- `.events` 文件格式文档

- 说明终端消息是主要反馈；`.events` 提供完整浏览器交互流作为附加上下文

**保留：**

- 服务器启动／关闭说明

- 内容片段与完整文档指导

- CSS 类参考及可用组件

- 设计提示（保真度与问题匹配、每屏 2—4 个选项等）

### `wait-for-feedback.sh` 测试文件

**完全删除。**

### `tests/brainstorm-server/server.test.js` 测试文件

需要更新的测试：

- 断言片段响应含 `feedback-footer` 的测试——改为断言选择指示栏或 `` 替换

- 断言 `helper.js` 含 `send` 的测试——按收窄 API 更新

- 断言 `sendToClaude` CSS 变量使用的测试——删除（函数不存在）

## 平台兼容性

服务器代码（`index.js`、`helper.js`、`frame-template.html`）完全与平台无关，是纯 Node.js 和浏览器 JavaScript，无 Claude Code 专用引用。已证明可通过后台终端交互在 Codex 上运行。

技能指令（`visual-companion.md`）是平台适配层。各平台的 Claude 用自身工具启动服务器、读取 `.events`。非阻塞模型不依赖平台专用阻塞原语，因此自然跨平台工作。

## 由此获得的能力

- 可视头脑风暴期间 **TUI 始终可响应**

- **混合输入**——浏览器点击加终端输入，自然合并

- **优雅降级**——浏览器故障或用户不打开？终端仍可用

- **更简单架构**——无后台任务、轮询脚本或超时管理

- **跨平台**——相同服务器代码在 Claude Code、Codex 及未来平台工作

## 放弃的内容

- **纯浏览器反馈工作流**——用户必须回终端继续。选择指示栏会引导，但比过去点击 Send 并等待多一步。

- **浏览器内联文字反馈**——textarea 已移除。所有文字反馈经终端；这是刻意的，终端比框架内小 textarea 更适合输入文字。

- **点击浏览器 Send 后立即响应**——旧系统在点击 Send 时立即回应。现在用户切回终端有间隔，实际只有几秒，且可趁机补充上下文。
