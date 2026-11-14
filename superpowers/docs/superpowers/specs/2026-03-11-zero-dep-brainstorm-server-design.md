# 零依赖头脑风暴服务器

将头脑风暴伴随服务器中内置的 node_modules（express、ws、chokidar，共 714 个跟踪文件）替换为一个仅使用 Node.js 内置模块的零依赖 `server.js`。

## 动机

将 node_modules 纳入 git 仓库产生供应链风险：冻结依赖无法获得安全补丁，714 个第三方文件未经审计即提交，内置代码修改看起来与普通提交无异。实际风险较低（仅本机开发服务器），但消除它很直接。

## 架构

单个 `server.js` 文件（约 250—300 行），使用 `http`、`crypto`、`fs` 和 `path`。文件承担两种角色：

- **直接运行时**（`node server.js`）：启动 HTTP/WebSocket 服务器

- **被 require 时**（`require('./server.js')`）：导出 WebSocket 协议函数供单元测试

### WebSocket 协议

仅针对文本帧实现 RFC 6455：

**握手：** 用 SHA-1 和 RFC 6455 魔法 GUID，由客户端 `Sec-WebSocket-Key` 计算 `Sec-WebSocket-Accept`。返回 101 Switching Protocols。

**帧解码（客户端到服务器）：** 处理三种带掩码长度编码：

- 小：负载少于 126 字节

- 中：126—65535 字节（16 位扩展）

- 大：超过 65535 字节（64 位扩展）

用 4 字节掩码键对负载做 XOR 去掩码。返回 `{ opcode, payload, bytesConsumed }`，缓冲区不完整时返回 `null`。拒绝未掩码帧。

**帧编码（服务器到客户端）：** 使用相同三种长度编码发送未掩码帧。

**处理的 opcode：** TEXT（0x01）、CLOSE（0x08）、PING（0x09）、PONG（0x0A）。无法识别的 opcode 返回状态 1003（Unsupported Data）的关闭帧。

**刻意跳过：** 二进制帧、分片消息、扩展（permessage-deflate）、子协议。本机客户端之间的小型 JSON 文本消息不需要这些。扩展和子协议在握手协商；不声明即永不启用。

**缓冲区累积：** 每个连接维持缓冲区。收到 `data` 时追加，循环 `decodeFrame` 直到返回 null 或缓冲区为空。

### HTTP 服务器

三个路由：

1. **`GET /`**——按 mtime 提供屏幕目录中最新的 `.html`。检测完整文档与片段，将片段包入框架模板并注入 helper.js。返回 `text/html`。没有 `.html` 时提供硬编码等待页（“Waiting for Claude to push a screen...”）并注入 helper.js。

2. **`GET /files/*`**——从屏幕目录提供静态文件，从硬编码扩展名映射（html、css、js、png、jpg、gif、svg、json）查找 MIME 类型。找不到返回 404。

3. **其他一切**——404。

WebSocket 升级由 HTTP 服务器 `'upgrade'` 事件处理，与请求处理器分开。

### 配置

环境变量（均可选）：

- `BRAINSTORM_PORT`——绑定端口（默认随机高端口 49152—65535）

- `BRAINSTORM_HOST`——绑定接口（默认 `127.0.0.1`）

- `BRAINSTORM_URL_HOST`——启动 JSON 中 URL 的主机名（host 为 `127.0.0.1` 时默认 `localhost`，否则同 host）

- `BRAINSTORM_DIR`——屏幕目录路径（默认 `/tmp/brainstorm`）

### 启动顺序

1. `SCREEN_DIR` 不存在时创建（`mkdirSync` 递归）

2. 从 `__dirname` 加载框架模板与 helper.js

3. 在配置的 host/port 启动 HTTP 服务器

4. 对 `SCREEN_DIR` 启动 `fs.watch`

5. 监听成功后向 stdout 输出 `server-started` JSON：`{ type, port, host, url_host, url, screen_dir }`

6. 将相同 JSON 写入 `SCREEN_DIR/.server-info`，使 stdout 被隐藏（后台执行）时代理仍能找到连接信息

### 应用层 WebSocket 消息

客户端 TEXT 帧到达时：

1. 解析为 JSON。失败则记录到 stderr 并继续。

2. 以 `{ source: 'user-event', ...event }` 记录到 stdout。

3. 事件含 `choice` 属性时，将 JSON 追加到 `SCREEN_DIR/.events`（每事件一行）。

### 文件监视

`fs.watch(SCREEN_DIR)` 替代 chokidar。HTML 文件事件时：

- 新文件（存在文件的 `rename` 事件）：存在则删除 `.events`（`unlinkSync`），向 stdout 记录 `screen-added` JSON

- 文件变化（`change` 事件）：向 stdout 记录 `screen-updated` JSON（不要清空 `.events`）

- 两种事件都向所有已连接 WebSocket 客户端发送 `{ type: 'reload' }`

按文件名以约 100ms 超时防抖，避免重复事件（macOS 和 Linux 上常见）。

### 错误处理

- WebSocket 客户端发来格式错误 JSON：记录到 stderr 并继续

- 未处理 opcode：以状态 1003 关闭

- 客户端断开：从广播集合移除

- `fs.watch` 错误：记录到 stderr 并继续

- 没有优雅关闭逻辑；shell 脚本通过 SIGTERM 管理进程生命周期

## 变更内容

| 之前 | 之后 |
|---|---|
| `index.js` + `package.json` + `package-lock.json` + 714 个 `node_modules` 文件 | `server.js`（单文件） |
| express、ws、chokidar 依赖 | 无 |
| 不提供静态文件 | `/files/*` 从屏幕目录提供 |

## 保持不变

- `helper.js`——不变

- `frame-template.html`——不变

- `start-server.sh`——一行更新：`index.js` 改为 `server.js`

- `stop-server.sh`——不变

- `visual-companion.md`——不变

- 所有现有服务器行为与外部契约

## 平台兼容性

- `server.js` 只使用跨平台 Node 内置模块

- `fs.watch` 在 macOS、Linux 和 Windows 的单一扁平目录上可靠

- Shell 脚本需要 bash（Windows 上 Git Bash，Claude Code 已要求）

## 测试

**单元测试**（`ws-protocol.test.js`）：通过 require `server.js` 导出，直接测试 WebSocket 帧编码／解码、握手计算和协议边界情况。

**集成测试**（`server.test.js`）：测试完整服务器行为——HTTP 提供、WebSocket 通信、文件监视、头脑风暴工作流。使用 `ws` npm 包作为仅测试客户端依赖（不交付给最终用户）。
