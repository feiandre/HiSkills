# 面向 OpenCode 的 Superpowers

在 [OpenCode.ai](https://opencode.ai) 中使用 Superpowers 的完整指南。

## 安装

OpenCode V2 要求版本 2.0.4 或更高。

### OpenCode V1 配置

使用现有 V1 插件配置：

```json
{
  "plugin": ["superpowers@git+https://github.com/obra/superpowers.git"]
}
```

### OpenCode V2（2.0.4 或更高）配置

使用 V2 插件配置：

```json
{
  "plugins": ["superpowers@git+https://github.com/obra/superpowers.git"]
}
```

本地 V2 安装应配置包含 `index.js` 的仓库目录。OpenCode 2.0.4 与 2.0.7 会拒绝配置直接 JavaScript 文件路径。仍支持通过发现的插件符号链接安装。

重启 OpenCode。V2 使用 `opencode` 命令；可能提供别名 `opencode2`。插件通过 OpenCode 插件管理器安装并注册全部技能。

通过询问验证：“Tell me about your superpowers”（告诉我你的 superpowers）

### 从旧的基于符号链接的安装迁移（V1）

若此前用 `git clone` 和符号链接安装 superpowers，请移除旧设置：

```bash
rm -f ~/.config/opencode/plugins/superpowers.js
rm -rf ~/.config/opencode/skills/superpowers
rm -rf ~/.config/opencode/superpowers
```

然后遵循上述安装步骤。

## 使用

### 查找技能

使用 OpenCode 原生 `skill` 工具列出全部可用技能：

```
use skill tool to list skills
```

### 加载技能

```
use skill tool to load brainstorming
```

### 个人技能

在 `~/.config/opencode/skills/` 中创建自己的技能：

```bash
mkdir -p ~/.config/opencode/skills/my-skill
```

创建 `~/.config/opencode/skills/my-skill/SKILL.md`：

```markdown
---
name: my-skill
description: 在[条件]时使用 - [作用]
---

# My Skill

[在此填写技能内容]
```

### 项目技能

在项目内的 `.opencode/skills/` 中创建项目专用技能。

**V2 技能优先级：**项目技能 > 个人技能 > Superpowers 技能。在测试过的 V1 1.18.31 上，当个人或项目技能同名时，随附 Superpowers 技能优先；请为个人和项目技能使用不同名称。迁移不改变此行为。

## 更新

OpenCode 通过 git 支持的包规范安装 Superpowers。某些 OpenCode 与 Bun 版本会把解析后的 git 依赖固定在锁文件或缓存中，因此重启可能无法取得最新 Superpowers 提交。若看不到更新，请清理 OpenCode 包缓存或重装插件。

要固定特定版本，请向规范添加 tag 或 commit（V1 `plugin` 键与 V2 `plugins` 键形式相同）：

```json
{
  "plugin": ["superpowers@git+https://github.com/obra/superpowers.git#v7.0.1"]
}
```

在 V2 上，请固定 `v6.4.1` 或更高版本；`v6.3.0` 及更早版本只能在 V1 加载。

## 工作原理

插件使用宿主版本专属 API 完成两件事：

1. **注册技能目录**，让 OpenCode 无需符号链接或手动配置即可发现全部 superpowers 技能。

- **V1：**通过 `config` 钩子注入 `config.skills.paths`

- **V2：**通过 `setup()` 函数使用 `ctx.skill.transform()`（V2 原生 API，已确认运行时生效）

2. **注入引导上下文**及版本专属工具映射：V1 会话获得下方 V1 工具名，V2 会话获得 V2 名称。

- **V1：**通过 `experimental.chat.messages.transform` 钩子

- **V2：**通过 `ctx.session.hook("context")`——V2 等价机制（已确认运行时生效）

控制器会话在瞬态模型上下文中接收 using-superpowers 引导。委派子会话保留原生技能访问，但不接收控制器引导。没有父会话的手动分叉仍保留控制器行为。当 V2 原生压缩保留较早用户消息时（默认 `compaction.keep.tokens` 预算），引导会像未压缩会话一样放入检查点前第一条保留的用户消息。压缩移除所有用户消息时，插件在检查点后追加瞬态引导消息。无论哪种方式，保存的历史不变。

若会话查找失败，插件为该请求保留引导，并在下一请求重试。失败查找不会缓存为控制器决定。

### 工具映射

技能以动作而非某个运行时工具名表述。引导将其映射到你的 OpenCode 版本实际公开的工具。

**V1（`opencode` 1.x）工具映射：**

- “创建待办”/“在待办中标记完成” → `todowrite`

- `Subagent (general-purpose):` 模板 → OpenCode `task` 工具，使用 `subagent_type: "general"`（代码库探索用 `"explore"`）

- “调用技能” → OpenCode 原生 `skill` 工具

- “读取文件” → `read`

- “创建文件”/“编辑文件”/“删除文件” → `apply_patch`

- “运行 shell 命令” → `bash`

- “搜索文件内容”/“按名称查找文件” → `grep`、`glob`

- “获取 URL” → `webfetch`

**V2（`opencode` 2.0.4 或更高；可能提供别名 `opencode2`）工具映射：**

- “创建待办” → V2 没有任何待办工具；映射指示模型改用 Markdown 文件（或宿主的计划设施）跟踪计划

- `Subagent (general-purpose):` 模板 → OpenCode `subagent` 工具，使用 `agent: "general"`（或 `"explore"`）；传入 `sessionID` 继续先前子代理

- “调用技能” → OpenCode 原生 `skill` 工具

- “读取文件” → `read`

- “创建、编辑或删除文件” → 有 `patch` 时使用它及 `patchText`；否则用 `write` 创建或覆盖文件、用 `edit` 做定向修改、用 `shell` 删除

- “运行 shell 命令” → `shell`（`command`、`workdir`、`timeout`、`background`）

- “搜索文件内容”/“按名称查找文件” → `grep`、`glob`

- “获取 URL” → `webfetch`

- “搜索网络” → `websearch`

简言之，V2 将 `task` 改名为 `subagent`（代理名称从 `subagent_type` 移到 `agent`，继续时用 `sessionID` 重新调用），将 `apply_patch` 改为 `patch`，将 `bash` 改为 `shell`，并完全删除待办工具。可用修改工具取决于所选模型：选定 GPT 模型 ID 可用 `patch`，其他模型使用 `write` 和 `edit`。

（V1 清单已对照安装的 OpenCode 1.18.x CLI 工具清单验证；V2 清单已对照 OpenCode 2.0.4 与 2.0.7 宿主契约验证。）

## 故障排除

### 插件未加载

**V1：**检查 OpenCode 日志：

```
opencode run --print-logs "hello" 2>&1 | grep -i superpowers
```

**V2：**插件在后台服务器加载，只有使用 `--standalone` 时 `--print-logs` 才会显示其日志：

```
opencode run --standalone --print-logs "hello" 2>&1 | grep -i superpowers
```

或检查 `~/.local/share/opencode/log/opencode.log`，筛选 `role=server`。

还要验证 `opencode.json` 中插件路径正确，且运行的是较新 OpenCode 版本。

### Windows 安装问题

某些 Windows OpenCode 构建在 git 支持的插件规范上有上游安装器问题，包括 `git+https` URL 的缓存路径，以及 Bun 即使普通终端可用也找不到 `git.exe`。若 OpenCode 无法安装插件，尝试用系统 npm 安装，并让 OpenCode 指向本地包：

```powershell
npm install superpowers@git+https://github.com/obra/superpowers.git --prefix "$HOME\.config\opencode"
```

然后在 `opencode.json` 中按 OpenCode 版本使用已安装包的绝对路径。OpenCode 不展开 `~`；`~/...` 条目会被视为包名而非本地目录。

```json
{
  "plugin": ["C:\\Users\\<you>\\.config\\opencode\\node_modules\\superpowers"]
}
```

**V2（2.0.4 或更高）：**

```json
{
  "plugins": ["C:\\Users\\<you>\\.config\\opencode\\node_modules\\superpowers"]
}
```

### 找不到技能

1. 使用 OpenCode `skill` 工具列出可用技能

2. 确认插件已加载（见上文）

3. 每项技能都需要具有有效 YAML frontmatter 的 `SKILL.md` 文件

### 引导未出现

- **V1：**检查 OpenCode 版本是否支持 `experimental.chat.messages.transform` 钩子。配置改变后重启 OpenCode。

- **V2：**插件用 `ctx.session.hook("context")` 注入引导。通过 `opencode api get /api/plugin` 验证插件已加载。配置改变后运行 `opencode service restart` 重启。可能提供别名 `opencode2`。

## 获取帮助

- 报告 issue：https://github.com/obra/superpowers/issues

- 主文档：https://github.com/obra/superpowers

- OpenCode V2 文档：https://opencode.ai/v2/docs/

- OpenCode V1 文档：https://opencode.ai/docs/
