# 可视化助手认证加固设计

**日期：**2026-06-10  
**状态：**供 Drew 审阅的草稿

## 目标

修复 PR #1720 头脑风暴可视化助手的安全和可靠性缺口，同时不改变核心工作流，也不增加运行时依赖。

修复必须测试先行，并留下明确自动化证据证明：

- 跨源浏览器标签不能借助 cookie 注入助手事件

- 重启重连不只依赖浏览器 cookie 行为

- bearer key 在引导后不留在可见 URL

- `/files/*` 不能提供内容目录外文件

- 未来同源内置 UI 库仍可工作

## 威胁模型

助手为单个头脑风暴会话提供智能体生成的本地 UI。重要资产：

- 助手提供的屏幕内容

- 会话密钥

- `state/events`，智能体将其读取为用户反馈

- 助手会话目录下本地文件

范围内的攻击者：

- 另一个 `localhost` 端口上的恶意标签页

- 能请求助手但不应认证为助手 UI 的网页

- 服务器绑定非回环接口时的远程客户端

- 通过 URL 历史、referrer 或提交本地状态意外泄漏

- 逃出 `/files/*` 的内容目录符号链接或路径技巧

本次修复范围外：

- 智能体编写的恶意屏幕 HTML

- 屏幕加载的同源内置恶意 JavaScript

边界是有意的：屏幕属于智能体 UI，可能使用内联脚本及 future 同源库（Alpine、Three.js）。防恶意 HTML 需要更大的沙箱 iframe 和窄消息桥，不属本加固 PR。

## 当前失败

自动和无头浏览器测试在 PR 分支发现：

1. 真实助手页面设 cookie 后，跨源 localhost 页面可打开 cookie 认证 WebSocket，把攻击者选择写入 `state/events`。

2. `/files/*` 提供指向 `content/` 外的符号链接，包括含密钥 URL 的 `state/server-info`。

3. 密钥留在屏幕 URL，同源 JavaScript、referrer 和历史可看到。

4. helper 用无密钥 `ws://host` 重连。有头 Chrome 同端口／同令牌重启后不再向新服务器呈现 cookie，标签停留墓碑页直到手动刷新。

5. shell lint 和生命周期测试需清理，使 Codex 中稳定通过。

## 设计

### 1. 带密钥的引导加载

`GET /?key=<token>` 返回引导响应，而非屏幕响应。

`GET /?key=<token>` 返回引导页而非屏幕。密钥有效时服务器：

1. 按现状设置 HttpOnly 会话 cookie

2. 返回小型 HTML 引导页

3. 引导页将密钥存入标签级 `sessionStorage`

4. 用 `location.replace('/')` 跳转 `/`

之后可见屏幕 URL 是裸 `/`，而非 `/?key=...`。

有效 cookie 的 `GET /` 提供当前屏幕；没有有效 cookie 的 `GET /` 仍返回友好 403；`GET /?key=<wrong>` 返回 403。

使用 `sessionStorage` 是因为重连凭据需跨同端口重启，不能只依赖 cookie。屏幕 HTML 属于可信同源 UI，因此在此威胁模型中标签级存储可接受，且比地址栏、历史和 referrer 泄漏明显更好。

### 2. WebSocket 同源强制

WebSocket 升级必须通过两项检查：

1. 通过查询密钥或 cookie 进行有效会话认证

2. 有 `Origin` 头时必须匹配请求目标 origin

检查：

```text
Origin === "http://" + req.headers.host
```

恶意页面示例：

```text
Origin: http://localhost:9999
Host: localhost:58088
```

即使浏览器发送助手 cookie，也必须拒绝。

即使浏览器发送助手 cookie 也必须拒绝。合法助手示例：

```text
Origin: http://localhost:58088
Host: localhost:58088
```

密钥或 cookie 有效时应接受。

密钥或 cookie 有效时接受。直接非浏览器客户端可省略 `Origin`，但仍需会话密钥。

### 3. helper 重连凭据

`helper.js` 从 `sessionStorage` 读取标签密钥并附加到 WebSocket URL：

```text
ws://<host>/?key=<stored-key>
```

没有存储密钥时回退仅 cookie 的 `ws://<host>`，兼容已加载页面。

### 4. `/files/*` 隔离

文件服务器继续拒绝空名和点文件，并确保文件是 `CONTENT_DIR` 内真实普通文件。

使用 realpath 边界：

- 计算 `realContentDir = fs.realpathSync(CONTENT_DIR)`

- 计算 `realFilePath = fs.realpathSync(filePath)`

- 仅当 `realFilePath` 是 `realContentDir` 后代时提供

- 对符号链接和内容目录外内容返回 404

继续使用 `path.basename`，不支持嵌套路径。

### 5. 减少泄漏的响应头

添加不阻止内联脚本或未来同源库的保守头：

```text
Referrer-Policy: no-referrer
Cache-Control: no-store
X-Frame-Options: DENY
Content-Security-Policy: frame-ancestors 'none'
Cross-Origin-Resource-Policy: same-origin
```

本次不添加限制 `script-src` 的 CSP；助手注入内联帮助脚本，未来屏幕可能加载同源库。

### 6. Gitignore 持久会话状态

根 `.gitignore` 添加 `.superpowers/`，防止 `--project-dir` 持久状态和 `.last-token` 被提交。

### 7. 测试稳定性与 lint

清理触碰的 start/stop 脚本中的 shell lint 警告。

清理触碰脚本的 shell lint 警告。更新调用 `start-server.sh --idle-timeout-minutes` 的生命周期测试，使用 `--background` 强制后台，防止 Codex 的 `CODEX_CI` 前台检测挂起。

## 测试策略

所有行为变更 TDD：先写失败聚焦测试，确认按预期失败，最小修复，重跑聚焦测试，再跑完整 brainstorm-server 套件。

1. 编写失败的聚焦测试

2. 运行并确认它按预期原因失败

3. 实现最小修复

4. 重跑聚焦测试

5. 重跑完整 brainstorm-server 套件

必须覆盖：有效密钥 `/` 返回引导；引导存密钥到 `sessionStorage` 并去掉 URL；cookie `/` 仍提供屏幕；helper 用存储密钥连 WebSocket；同源 cookie 开启；跨源 cookie 被拒绝且不写事件；直接密钥无 `Origin` 开启；指向 `state/server-info` 的链接返回 404；正常 HTML、引导、403 和文件响应含安全头；同端口／令牌重启用存储密钥重连；触碰 shell 脚本 lint 通过；Codex 下生命周期套件不挂起。

- 有效密钥 `/` 返回引导，而非屏幕内容

- 引导将密钥存入 `sessionStorage` 并移除 URL 密钥

- 仅 cookie 的 `/` 仍提供屏幕内容

- helper 使用 `sessionStorage` 密钥构造 WebSocket URL

- 同源 cookie WebSocket 可打开

- 跨源 cookie WebSocket 被拒绝且不写事件

- 直接密钥 WebSocket 无 `Origin` 仍可打开

- `content/` 下指向 `state/server-info` 的符号链接返回 404

- 正常 HTML、引导、403 和文件响应均含安全头

- 同端口／同令牌重启可用存储密钥认证重连

- 触碰的 shell 脚本通过 shell lint

- 生命周期套件在 Codex 下不挂起

## 验收标准

- `cd tests/brainstorm-server && npm test` 反复通过且不挂起。

- 此前从另一 localhost 源写入 `attacker-injected` 的安全探针无法开 WebSocket，`state/events` 不变。

- 指向 `server-info` 的符号链接探针返回 404。

- 有头或无头浏览器带密钥加载最终裸 `/`，状态药丸变为 Connected。

- 同端口／同令牌重启自动重连无需刷新。

- `scripts/lint-shell.sh` 对触碰脚本通过。

## 延后工作

未来需把屏幕 HTML 视为不可信时，另设计沙箱 iframe：在独立 origin 或沙箱 frame 隔离屏幕，只暴露窄 `postMessage` 桥传递用户选择。不要塞进本次修复。
