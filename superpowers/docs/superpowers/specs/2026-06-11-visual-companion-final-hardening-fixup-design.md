# 视觉伴侣最终加固修补设计

**日期：** 2026-06-11
**状态：** 供 Drew 审阅的草稿

## 目标

完成 PR #1720 的视觉伴侣加固，使该分支具备干净的安全行为、确定性测试以及只包含
伴侣工作的 PR 差异，从而可以交给 Jesse 审阅。

这是在现有身份验证加固设计之上的修补。它不应重新设计伴侣，也不应扩大功能范围。

## 背景

上一轮加固加入了带密钥的会话、同源 WebSocket 检查、URL 密钥剥离、`/files/*` 边界限制、
减少泄漏的响应头、IPv6 URL 格式化、Windows 生命周期覆盖以及 PR 证据更新。

最终评审发现五个遗留问题：

1. 根路径 `GET /` 的屏幕选择可能继续提供 `content/` 下指向内容目录之外的符号链接或硬链接。

2. 首选端口被占用时，回退服务器可能复用持久化的 `.last-token`，产生两个使用相同 bearer 密钥的
   同项目活动伴侣服务器。

3. 没有强归属证明时，`stop-server.sh` 可能向无关的 `node server.cjs` 进程发送信号。

4. 一些测试可能针对错误的回退进程并通过、失败时泄漏后台进程，或假设 Windows 类宿主支持符号链接。

5. PR 当前存在冲突，因为分支包含一个单独处理的旧 `evals` 子模块版本提升。

## 非目标

- 本轮不添加 HTTPS 隧道或 `wss://` 来源语义。

- 不实现退出选择、自由文本或对比度辅助等伴侣功能。

- 不内置 Alpine、Three.js 或任何其他 JavaScript 库。

- 不尝试沙箱隔离恶意智能体编写的屏幕 HTML。

- 不为陈旧 stop-server PID 文件添加向后兼容，除非 Drew 明确批准该取舍。

## 继承的安全不变量

本修补保留已经设计并实现的身份验证加固：

- `.last-token` 和 `state/server-info` 保持仅属主可读的敏感状态。

- 回退令牌可出现在启动 JSON 和 `state/server-info` 中，但不得写入 `.last-token`。

- Cookie 继续按端口命名，并保持 `HttpOnly`、`SameSite=Strict`，作用域为 `/`。

- WebSocket 升级仍要求有效密钥或 Cookie。

- 浏览器提供 `Origin` 头时，仍执行 WebSocket `Origin` 检查。

- 无 `Origin` 的直连客户端只有在携带会话密钥时才被允许。

- 生成式同源屏幕 JavaScript 及未来同源内置库均受信任。恶意屏幕 HTML 的沙箱隔离仍延后处理。

## 设计

### 1. 变基到当前 `dev`

开始实现前，将 `brainstorming-companion` 变基到当前 `origin/dev`。解决 `evals` 子模块冲突时采用 `dev` 的内容。

变基后：

- `evals` 不得出现在 PR 差异中。

- PR #1720 仍可提到在其他地方运行的评测证据，但必须包含确切的外部证据：评测仓库提交、场景路径、
  命令、结果产物路径或 ID，以及 RED/GREEN 结果。

- PR 正文不得暗示 `evals` 子模块提升属于此 PR。

- 任何暗示包含子模块提升的早期 PR 正文或评论，都必须由最终 PR 正文证据取代。

### 2. 根屏幕边界限制

根屏幕路由必须使用与 `/files/*` 相同的边界。

`getNewestScreen()` 应忽略任何未通过“内容是目录内普通文件”保护的 `.html` 候选。该保护必须解析真实路径，
确保所提供文件位于 `CONTENT_DIR` 内。平台报告链接数时，它还必须拒绝链接数不等于一的文件，
以保留现有硬链接防护。

预期行为：

- `content/` 下指向 `content/` 之外的符号链接会被忽略。

- 当 `fs.linkSync` 成功且 `lstat.nlink > 1` 时，`content/` 下指向 `state/server-info` 的硬链接会被忽略。

- 若没有剩余的安全屏幕文件，则提供等待页。

- 现有 `/files/*` 边界行为保持不变：空名称、点文件、符号链接、硬链接和目录仍返回 404。

### 3. 回退令牌隔离

端口回退不得复用从持久化 `.last-token` 加载的令牌。

代码中的令牌来源应明确：

- 来自环境的 `BRAINSTORM_TOKEN` 是操作者／测试有意提供的覆盖值。设置显式环境令牌且首选端口被占用时，
  服务器必须失败关闭而不能回退，因为占用该端口的服务器可能使用相同令牌。

- `.last-token` 是为同端口重连便利而持久化的状态。若服务器因首选端口被占用而回退，应丢弃已加载令牌，
  并为回退进程生成未持久化的新令牌。

- 并非从 `.last-token` 加载的新生成令牌可在同一进程内复用，因为已知没有其他活动进程持有它。

回退服务器必须继续避免覆盖 `.last-port` 和 `.last-token`。

### 4. Stop-Server 归属证明

`start-server.sh` 应为每次启动创建服务器实例 ID，并作为惰性命令行参数传给 Node，例如：

```text
node server.cjs --brainstorm-server-id=<id>
```

此 ID 不是身份验证凭据，只是本地生命周期脚本使用的进程归属证据。`server.cjs` 可以忽略该参数。

ID 必须使用 shell/MSYS 安全字符集，例如 `^[A-Za-z0-9_-]{32,64}$`。将它保存在 `state/server-instance-id`，
权限设为仅属主可用。

`stop-server.sh` 应从状态中读取预期 ID，只有目标进程 argv 以完整 argv 词元形式包含精确参数
`--brainstorm-server-id=<id>`（而不是松散子串）时，才向该 PID 发信号。优先使用可用的
`/proc/<pid>/cmdline`，再回退到宽 `ps` 输出。即使 `server-info` 缺失或 `lsof` 不可用，
匹配实例 ID 也足以作为证据。现有端口到 PID 检查可保留作为补充证据。

无法证明归属时失败关闭：

- PID 文件缺失

- 服务器 ID 缺失或格式错误

- 目标命令行不可用

- 目标命令行不包含预期 ID

- 旧／陈旧会话元数据不包含新 ID

这有意优先保留陈旧进程，而不是杀死无关进程。

操作者可见的结果应明确：

- PID 文件缺失返回 `not_running`

- 服务器 ID 缺失或格式错误返回 `stale_pid`

- 命令行不可用返回 `stale_pid`

- argv ID 错误或缺失返回 `stale_pid`

- 成功停止返回 `stopped`

出现 `stale_pid` 和 `stopped` 结果时，移除 `server.pid` 和 `server-instance-id`，
避免后续停止尝试继续针对同一个含糊进程。不要移除持久会话内容。

### 5. 测试加固

测试必须在 macOS 和用于验证的 Windows Git Bash 宿主上具有确定性。

必须更改：

- 固定端口测试套件若服务器报告回退端口，必须快速失败；或者让所有客户端使用报告的启动端口。

- `stop-server.test.sh` 必须在启动任何后台进程前设置顶层清理 trap。

- 符号链接专用断言应探测符号链接能力；宿主无法创建可用测试符号链接时，只跳过该断言。

- 创建冒名进程的测试必须断言：生命周期元数据缺失或不足时，冒名进程仍然存活。

- Windows/MSYS start-server 测试必须断言 Windows 类检测仍清除 `BRAINSTORM_OWNER_PID`、
  在适当时仍自动转到前台，并仍精确传递实例 ID argv。

### 6. 文档与 PR 一致性

Jesse 审阅前，协调评审者可见的文档和 PR 元数据：

- 更新问题目录，使处理结果与此 PR 实际交付相符。

- 让自动打开文档与已实现的 `--open` 行为一致。

- 在所有地方保持记录的默认空闲超时为 4 小时。

- 变基后按模板审阅 PR 正文。

- 在 PR 正文中记录 macOS、Windows、浏览器／人工及外部评测证据，并附具体命令和结果。

## 测试策略

每项行为变化都采用 TDD：

1. 添加或加强聚焦的回归测试。

2. 运行并确认它因预期原因失败。

3. 实施最小修复。

4. 重新运行聚焦测试。

5. 重新运行完整 brainstorm-server 套件。

必需的聚焦回归：

| 行为 | 测试文件 | 聚焦命令 | 预期 RED | 预期 GREEN |
| --- | --- | --- | --- | --- |
| 根路由忽略符号链接逃逸 | `tests/brainstorm-server/server.test.js` | `node tests/brainstorm-server/server.test.js` | 已认证的 `GET /` 提供指向内容外部的链接 | 响应提供等待页或安全屏幕 |
| 根路由忽略受支持的硬链接逃逸 | `tests/brainstorm-server/server.test.js` | `node tests/brainstorm-server/server.test.js` | 已认证的 `GET /` 提供硬链接的 `server-info` | `nlink > 1` 时忽略硬链接候选 |
| `/files/*` 边界限制保持不变 | `tests/brainstorm-server/server.test.js` | `node tests/brainstorm-server/server.test.js` | 现有边界测试回归 | 空名称、点文件、目录、符号链接、硬链接情况仍为 404 |
| 持久令牌回退轮换令牌 | `tests/brainstorm-server/lifecycle.test.js` | `node tests/brainstorm-server/lifecycle.test.js` | 回退 URL 密钥等于为首选端口持久化的密钥 | 回退 URL 密钥不同，且未写入 `.last-token` |
| 显式令牌回退失败关闭 | `tests/brainstorm-server/lifecycle.test.js` | `node tests/brainstorm-server/lifecycle.test.js` | 设置 `BRAINSTORM_TOKEN` 时服务器仍回退 | 进程以非零状态退出，不启动回退 |
| 回退密钥不能认证原服务器 | `tests/brainstorm-server/lifecycle.test.js` | `node tests/brainstorm-server/lifecycle.test.js` | 原端口对回退密钥返回 200 | 原端口拒绝回退密钥 |
| 正确实例 ID 允许停止 | `tests/brainstorm-server/stop-server.test.sh` | `bash tests/brainstorm-server/stop-server.test.sh` | 由真实 start-server 启动的服务器仍存活 | 停止返回 `stopped` 且进程退出 |
| 错误、缺失、格式错误或陈旧 ID 均安全 | `tests/brainstorm-server/stop-server.test.sh` | `bash tests/brainstorm-server/stop-server.test.sh` | 冒名进程收到信号 | 停止返回 `stale_pid`，冒名进程存活 |
| 固定端口套件不能通过回退端口误通过 | `tests/brainstorm-server/server.test.js`、`tests/brainstorm-server/auth.test.js` | 各自的 `node` 命令 | 测试静默与回退端口通信 | 测试明确失败，或有意使用报告的端口 |
| shell 清理 trap 在失败时运行 | `tests/brainstorm-server/stop-server.test.sh` | `bash tests/brainstorm-server/stop-server.test.sh` | 失败时遗留子进程 | trap 回收后台子进程 |
| Windows/MSYS 启动行为保持生命周期不变量 | `tests/brainstorm-server/start-server.test.sh`、`tests/brainstorm-server/windows-lifecycle.test.sh` | macOS 和 `ballmer` 上的 `bash` 测试命令 | 属主 PID 或 argv 处理回归 | 清除属主 PID、前台检测成立、存在 ID argv |

每个 RED/GREEN 循环都应为 PR 正文留下简短证据说明：聚焦命令、修复前失败断言、修复后通过断言，
以及证据来自 macOS 还是 Windows。

## 验证

宣布修补完成前，运行：

- TDD 期间使用的相关聚焦测试命令

- 对改动 JavaScript 文件进行 Node 语法检查

- 对改动 shell 文件进行 shell lint

- 在 `ballmer` 上进行 Windows 验证：完整可运行 brainstorm-server 套件及独立 Windows 生命周期探针

自动检查全部通过后，才进行人工／浏览器测试。

## 验收标准

- PR #1720 可以干净地变基到当前 `dev`。

- PR 差异中不存在 `evals`。

- 根屏幕服务不能通过符号链接或受支持硬链接逃逸读取 `content/` 之外的内容。

- `/files/*` 边界保护保持不变。

- 回退服务器不得使用可能与已占用的首选端口服务器共享的令牌运行。

- 归属证明缺失或含糊时，`stop-server.sh` 不得向无关进程发信号。

- `server-info` 或 `lsof` 不可用时，只要实例 ID 匹配，`stop-server.sh` 仍能停止合法服务器。

- 为每个回归记录聚焦 RED/GREEN 证据。

- 在 PR 正文中记录 macOS 和 Windows 验证证据。

- PR 正文准确描述分支内容和外部收集的证据。
