# Notes 验证映射

此目录是验证 Notes 用户可见行为的维护来源。操作应用前先读索引，再按匹配功能文件执行。

## 基线前提

- 使用一次性数据目录在 `http://127.0.0.1:4173` 启动 Notes。

- 设置 `NOTES_DATA_DIR=/tmp/notes-verify-$RUN_ID`，避免并发运行共享状态。

- 预置标题 `Quarterly plan` 和 `Grocery list`。

- 将 `control-notes` 与 `notes` CLI 放入 `PATH`。

- 运行 `control-notes doctor`，要求 URL、数据目录与构建修订符合预期。

- 绝操作不是本次验证运行启动的实例。

## 操作约定

- 无特殊前提时，每条配方都从基线状态开始。

- 优先 ARIA 角色与可访问名称，不用 CSS 选择器或 DOM 位置。

- 命令按字面执行，引号内名称和标志保持不变。

- 浏览器操作通过 `control-notes browser`。

- 终端操作通过 `control-notes cli -- <command>`。

- 变更后恢复预置数据；清理时不得删除证据产物。

## 证据与跳过报告

- 捕获用户动作及结果状态，不只最终画面。

- UI 证据包含 ARIA 快照和可见应用身份的截图。

- CLI 证据包含命令、stdout、stderr 与退出码。

- 变更证据包含存储值的只读第二视图。

- 每个产物记录功能 ID 与入口点。

- 不可达路径报告尝试命令与未满足前提。

- 不得把跳过的入口说成已通过另一路径验证。

## 功能文件约定

每个功能文件以 H1 标题和一段用户可见行为说明开头，然后按顺序恰好使用四个 H2 节。

1. `Sub-features` 列出短 ID，每个行为一行。

2. `How to get to it (user POV)` 列出每个用户入口。

3. `Driving it with <harness>` 以 `Preconditions:` 开头，并用带标签项目把用户动作与确切命令、可观察结果配对。

4. `Gotchas` 列出可能浪费或使验证无效的陷阱。

映射中不写实现细节，只写用户路径、稳定句柄、所需状态、命令和可观察证据。

## 功能

- [创建笔记](./create-note.md) 覆盖浏览器与 CLI 创建、取消、持久化及清理。

- [搜索笔记](./search.md) 覆盖工具栏、键盘与 CLI 搜索，以及匹配、空状态和清除。
