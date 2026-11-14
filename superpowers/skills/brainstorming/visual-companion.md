# 可视化助手指南

用于展示界面稿、图表和选项的浏览器可视化头脑风暴助手。

## 何时使用

应按具体问题决定，不按整个会话决定。判断标准：**用户看到它是否比读文字更能理解？**

内容本身具有视觉性时**使用浏览器**：

- **UI 界面稿**——线框图、布局、导航结构、组件设计

- **架构图**——系统组件、数据流、关系图

- **并排视觉比较**——比较两个布局、两套配色或两个设计方向

- **设计打磨**——问题涉及外观、间距或视觉层级时

- **空间关系**——以图呈现状态机、流程图、实体关系

内容是文本或表格时**使用终端**：

- **需求与范围问题**——“X 是什么意思？”“哪些功能在范围内？”

- **概念性 A/B/C 选择**——在文字描述的方法之间选择

- **权衡清单**——优缺点、比较表

- **技术决策**——API 设计、数据建模、架构方法选择

- **澄清问题**——答案为文字而不是视觉偏好时

关于 UI 主题的问题并不自动属于视觉问题。“你想要哪种向导？”是概念问题，使用终端。“这些向导布局中哪个感觉合适？”是视觉问题，使用浏览器。

## 工作方式

服务器监视目录中的 HTML 文件，并向浏览器提供最新文件。你把 HTML 内容写入 `screen_dir`，用户会在浏览器中看到并点击选项。选择会记录到 `state_dir/events`，供你在下一轮读取。

**内容片段与完整文档：** 如果 HTML 文件以 `<!DOCTYPE` 或 `<html` 开头，服务器原样提供，仅注入辅助脚本。否则，服务器自动将内容包入框架模板，加入页眉、CSS 主题、连接状态和全部交互基础设施。**默认编写内容片段。** 只有需要完全控制页面时才编写完整文档。

## 启动会话

```bash
bash scripts/start-server.sh --project-dir /path/to/project --open
```

保存响应中的 `screen_dir` 和 `state_dir`。使用 `--open` 时，你推送第一屏后浏览器会自动打开，无需让用户手动打开，但仍应分享 URL 作为后备（无头／远程环境不会自动打开）。

**URL 含会话密钥（`?key=…`）。** 没有密钥的请求会被拒绝，因此始终把 `url` 字段中的**完整** URL 给用户；绝不删除查询字符串，绝不给裸 `http://host:port`。密钥把关 HTTP 和 WebSocket 访问，避免误开的浏览器标签页或网络中的其他机器读取页面或注入事件。首次加载后，浏览器通过 cookie 记住密钥，因此重新加载和 `/files/*` 资源无需重复携带。

**查找连接信息：** 服务器将启动 JSON 写入 `$STATE_DIR/server-info`。若在后台启动且未捕获标准输出，读取该文件获取 URL 和端口。使用 `--project-dir` 时，到 `<project>/.superpowers/brainstorm/` 查找会话目录。

**注意：** 将项目根目录作为 `--project-dir` 传入，使界面稿保存在 `.superpowers/brainstorm/` 并在服务器重启后保留。未提供时文件进入 `/tmp` 并被清理。如果 `.gitignore` 尚未包含 `.superpowers/`，提醒用户添加。

**按平台启动服务器：**

**Claude Code 平台：**

```bash
bash scripts/start-server.sh --project-dir /path/to/project --open
```

Windows 上脚本会自动检测并切换到前台模式，这会阻塞工具调用。Bash 工具调用使用 `run_in_background: true`，让服务器跨对话轮次继续运行，并在下一轮读取 `$STATE_DIR/server-info` 获取 URL 和端口。

**Codex 平台：**

```bash
bash scripts/start-server.sh --project-dir /path/to/project --open
```

**Gemini CLI 平台：**

```bash
bash scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**Copilot CLI 平台：**

```bash
bash scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**其他环境：** 服务器必须在对话轮次间持续后台运行。如果环境会清理分离进程，使用 `--foreground` 并通过平台的背景执行机制启动命令。

如果浏览器无法访问 URL（远程／容器环境常见），绑定非回环主机：

```bash
bash scripts/start-server.sh \
  --project-dir /path/to/project \
  --host 0.0.0.0 \
  --url-host localhost
```

使用 `--url-host` 控制返回 URL JSON 中打印的主机名。

## 循环

1. **确认服务器仍在运行**，然后**写入 HTML** 到 `screen_dir` 中的新文件：

- **必需：引用 URL 或推送页面前确认服务器仍在运行。** 检查 `$STATE_DIR/server-info` 存在且 `$STATE_DIR/server-stopped` 不存在。若已关闭，用**相同 `--project-dir`** 运行 `start-server.sh` 重启；它会复用同一端口，用户已打开的标签页会自动重连（服务器关闭期间显示“已暂停”覆盖层），无需发送新 URL。服务器空闲 4 小时后自动退出（可通过 `--idle-timeout-minutes` 配置）。

- 使用有语义的文件名：`platform.html`、`visual-style.html`、`layout.html`

- **绝不重复使用文件名**——每个页面使用新文件

- 使用文件创建工具——**绝不使用 cat/heredoc**（会把噪声倾倒进终端）

- 服务器自动提供最新文件

2. **告诉用户应期待什么，然后结束本轮：**

- 每一步都提醒 URL，不只第一步

- 用简短文字概述屏幕内容（例如“正在展示主页的 3 种布局选项”）

- 请用户在终端回复：“看一下并告诉我你的想法。愿意的话可以点击选择选项。”

3. **下一轮**——用户终端回复之后：

- 若 `$STATE_DIR/events` 存在就读取，其中包含用户浏览器交互（点击、选择），每行一个 JSON

- 与用户终端文字合并以获得完整情况

- 终端消息是主要反馈；`state_dir/events` 提供结构化交互数据

4. **迭代或前进**——反馈要求修改当前屏幕时写入新文件（如 `layout-v2.html`）。当前步骤验证通过后才推进下一问题。

5. **返回终端时卸载页面**——下一步无需浏览器时（如澄清问题、权衡讨论），推送等待页面清除旧内容：

```html
   
   <div style="display:flex;align-items:center;justify-content:center;min-height:60vh">
     <p class="subtitle">继续在终端中进行……</p>
   </div>
   ```

这避免对话已继续时用户仍盯着已解决的问题。下一次视觉问题出现时，照常推送新内容文件。

6. 重复直到完成。

## 编写内容片段

只写页面内部内容。服务器会自动用框架模板包裹（页眉、主题 CSS、连接状态和全部交互设施）。

**最小示例：**

```html
<h2>哪种布局更好？</h2>
<p class="subtitle">考虑可读性和视觉层级</p>

<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>单栏</h3>
      <p>干净、专注的阅读体验</p>
    </div>
  </div>
  <div class="option" data-choice="b" onclick="toggleSelect(this)">
    <div class="letter">B</div>
    <div class="content">
      <h3>双栏</h3>
      <p>侧边栏导航加主内容</p>
    </div>
  </div>
</div>
```

就这些。无需 `<html>`、CSS 或 `<script>` 标签。服务器提供这一切。

## 可用 CSS 类

框架模板为内容提供以下 CSS 类：

### 选项（A/B/C 选择）

```html
<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>标题</h3>
      <p>描述</p>
    </div>
  </div>
</div>
```

**多选：** 给容器添加 `data-multiselect`，允许用户选择多个选项。每次点击切换条目的选中样式。

```html
<div class="options" data-multiselect>
  
</div>
```

### 卡片（视觉设计）

```html
<div class="cards">
  <div class="card" data-choice="design1" onclick="toggleSelect(this)">
    <div class="card-image"></div>
    <div class="card-body">
      <h3>名称</h3>
      <p>描述</p>
    </div>
  </div>
</div>
```

### 界面稿容器

```html
<div class="mockup">
  <div class="mockup-header">预览：仪表板布局</div>
  <div class="mockup-body"></div>
</div>
```

### 分栏视图（并排）

```html
<div class="split">
  <div class="mockup"></div>
  <div class="mockup"></div>
</div>
```

### 优点／缺点

```html
<div class="pros-cons">
  <div class="pros"><h4>优点</h4><ul><li>好处</li></ul></div>
  <div class="cons"><h4>缺点</h4><ul><li>不足</li></ul></div>
</div>
```

### 界面稿元素（线框构建块）

```html
<div class="mock-nav">标志 | 首页 | 关于 | 联系</div>
<div style="display: flex;">
  <div class="mock-sidebar">导航</div>
  <div class="mock-content">主内容区</div>
</div>
<button class="mock-button">操作按钮</button>
<input class="mock-input" placeholder="输入字段">
<div class="placeholder">占位区域</div>
```

### 排版和章节

- `h2`——页面标题

- `h3`——章节标题

- `.subtitle`——标题下方的次要文字

- `.section`——带下边距的内容块

- `.label`——小号大写标签文字

## 浏览器事件格式

用户点击浏览器选项时，交互记录到 `$STATE_DIR/events`（每行一个 JSON 对象）。推送新页面时该文件自动清空。

```jsonl
{"type":"click","choice":"a","text":"选项 A - 简单布局","timestamp":1706000101}
{"type":"click","choice":"c","text":"选项 C - 复杂网格","timestamp":1706000108}
{"type":"click","choice":"b","text":"选项 B - 混合布局","timestamp":1706000115}
```

完整事件流显示用户的探索路径：他们可能先点击多个选项再确定。最后一个 `choice` 事件通常是最终选择，但点击模式可揭示值得询问的犹豫或偏好。

如果 `$STATE_DIR/events` 不存在，说明用户未与浏览器交互，仅使用其终端文字。

## 设计提示

- **细节程度与问题匹配**——布局问题用线框图，打磨问题用精细稿

- **每页说明问题**——写“哪种布局更专业？”而不是“选一个”

- **前进前先迭代**——反馈要求修改当前屏幕时写新版本

- 每屏最多 **2 至 4 个选项**

- **需要时使用真实内容**——摄影作品集使用真实图片（Unsplash）。占位内容会掩盖设计问题。

- **保持界面稿简单**——聚焦布局和结构，而非像素级完美设计

## 文件命名

- 使用有语义的名称：`platform.html`、`visual-style.html`、`layout.html`

- 绝不重复使用文件名——每屏必须使用新文件

- 迭代时添加版本后缀，如 `layout-v2.html`、`layout-v3.html`

- 服务器按修改时间提供最新文件

## 清理

```bash
bash scripts/stop-server.sh $SESSION_DIR
```

如果会话使用 `--project-dir`，界面稿文件保留在 `.superpowers/brainstorm/` 供以后参考。只有 `/tmp` 会话会在停止时删除。

## 参考

- 框架模板（CSS 参考）：`scripts/frame-template.html`

- 辅助脚本（客户端）：`scripts/helper.js`
