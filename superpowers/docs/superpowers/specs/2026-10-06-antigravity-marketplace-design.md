# Antigravity 市场插件

## 目标

与 Google 合作，将 Superpowers 列入 Google Antigravity 插件市场。需要含市场展示字段的原生 Antigravity 清单、logo，以及可在原生插件路径工作的会话引导。

来源：“Antigravity Plugin Marketplace Publishing Guide”（Google PDF）及下文 `agy` 1.3.1 探测。

## 当前状态（agy 1.3.1）

- `agy plugin install https://github.com/obra/superpowers` 成功，但仅通过 Gemini 扩展回退：`agy plugin list` 报告 `"source": "gemini-cli"`。引导依赖 `GEMINI.md` 的 `@` 行，模型当提示并 `view_file`。验收在此路径通过。

- agy 把 Claude 格式 `hooks/hooks.json` 复制为根 `hooks.json`，每次会话解析失败：`invalid hook "hooks": command hook must specify 'command'`。

- 对仓库运行 `agy plugin validate .` 报 `missing plugin.json`。

## 探测结果（agy 1.3.1）

每个探测安装临时插件、运行 `agy -p` 后卸载。

1. 钩子事件为 `PreToolUse`、`PostToolUse`、`PreInvocation`、`PostInvocation`、`Stop`，没有 `SessionStart`。内置文档使用命名顶层钩子（`{"<name>": {"PreToolUse": [...]}}`），与 PDF 的 `{"hooks": {...}}` 不同。

2. 插件中的 `rules/AGENTS.md` 在每次会话作为常驻规则加载。

3. 规则中以 `@` 开头的相对路径会改写为绝对安装路径（`@../skills/x/SKILL.md` 成为 `@/Users/<u>/.gemini/config/plugins/<plugin>/skills/x/SKILL.md`），内容不内联；规则中不替换 `${PLUGIN_ROOT}`，无法解析的路径保持原样。

4. 存在 `.antigravity-plugin/plugin.json` 时，agy 以 `"source": "antigravity"` 安装，发现15个技能并跳过钩子（无根 `hooks.json`），解析警告消失。

5. 带原生清单和一行 `rules/AGENTS.md`（`@../skills/using-superpowers/SKILL.md`）的暂存副本通过验收：模型依次读取 `using-superpowers`、`antigravity-tools.md`、`brainstorming`，提出澄清问题而不写代码。

6. 仓库根 `AGENTS.md` 会复制但不会作为规则加载，只有 `rules/AGENTS.md` 加载。

## 设计

### 1. 原生清单：`.antigravity-plugin/plugin.json`

指南允许该位置，与其他宿主点目录一致。字段： 清单位置仍是 `.antigravity-plugin/plugin.json`。

| 字段 | 值 |
|---|---|
| `name` | `superpowers` |
| `displayName` | `Superpowers` |
| `version` | 当前版本，由 `.version-bump.json` 维护 |
| `description` | `Make your coding agent a better engineer`（Jesse文案，短于指南推荐120–160，最多160） |
| `logo` | `assets/antigravity-logo.png` |
| `suggestedPrompts` | `I've got an idea for something I'd like to build`、`Let's figure out why this broke` |
| `category` | `Developer Tools` |
| `keywords` | 小写，与 `.claude-plugin/plugin.json` 一致 |
| `author` | `{ "name": "Jesse Vincent", "email": "jesse@fsck.com" }` |
| `homepage`、`repository` | `https://github.com/obra/superpowers` |
| `license` | `MIT` |（版本同 `.claude-plugin/plugin.json`）

不设 `skills` 或 `mcpServers`：默认 `skills/` 且无 MCP，探测4确认发现全部技能。

### 2. 引导：技能发现，无额外文件

agy 列出每个技能描述，`using-superpowers` 的“Use when starting any conversation”促使加载。插件不发布 `rules/` 或 `hooks.json`。

这替代早期一行 `rules/AGENTS.md` 指针方案：最终审查发现 Cursor 也会从同一根加载 `rules/*.md`。在 agy 1.3.1 探测后拒绝的替代项：

- `PreInvocation` 钩子每模型调用运行，`hooks.json` 必须在根。`ephemeralMessage` 下一次调用丢失；`userMessage` 持续，用 `invocationNum == 0` 和 `initialNumSteps == 1` 限制每对话一次，但每次仍启动钩子进程。

- 没有清单字段能移动 `hooks.json` 或 `rules/`。

无引导文件、12/12次验证：“做一个 React 待办列表”（3次）和“添加设置页”（3次）均在代码前加载 brainstorming；“这个测试失败，能修吗？”（3次）在编辑前加载 systematic-debugging；无关首轮后的 React 待办第二轮（3次）也加载 brainstorming。模型 Gemini 3.8 Flash。风险是触发依赖模型遵守描述；每次会话钩子是回退。

### 3. Logo：`assets/antigravity-logo.png`（中文说明）

512×512透明PNG。白色圆角方块（内缩31px、半径100）内放 `assets/superpowers-small.svg` 标志，颜色 `#1a1a1a`，宽度约70%并居中。无边框；浅色主题下表现为白底裸标志，可接受。

`scripts/render-antigravity-logo.sh` 从 `superpowers-small.svg` 生成并调用 `rsvg-convert` 栅格化；这是重新生成PNG的唯一方式，带帮助文本，缺少工具时明确失败。 生成依赖 `rsvg-convert`。

### 4. 版本提升

在 `.version-bump.json` 加入 `{ "path": ".antigravity-plugin/plugin.json", "field": "version" }`。

### 5. Codex 同步

在 `scripts/sync-to-codex-plugin.sh` 的 `EXCLUDES` 加 `/.antigravity-plugin/` 和 `/assets/antigravity-logo.png`，并在 `tests/codex-plugin-sync/test-sync-to-codex-plugin.sh` 覆盖。

### 6. README（中文说明）

安装命令保持 `agy plugin install https://github.com/obra/superpowers`；文字从“运行会话启动钩子”改为说明技能发现。市场路线存在后再写，当前不声称。

### 7. 测试：`tests/antigravity/`

- `test-plugin-manifest.sh`（CI安全，参照Kimi测试）： 参照路径 `tests/kimi/test-plugin-manifest.sh`。

- 清单可解析；`name`符合kebab-case且等于`superpowers`；

- 必需市场字段存在且非空：`name`、`description`、`displayName`、`logo`、`suggestedPrompts`（1–3个非空字符串）、`version`、`author`；

- `description`最多160字符；

- `version`等于 `.claude-plugin/plugin.json`；

- logo存在、PNG、正方形且至少128×128； 字段名为 `logo`。

- `.version-bump.json`列出该清单；

- `using-superpowers`描述仍含“Use when starting any conversation”；

- 不存在根 `plugin.json`、`hooks.json` 或 `rules/`。

- PATH有agy时运行 `agy plugin validate`，要求 `[ok]` 并处理技能。 运行器需在 `PATH` 中找到 `agy`。

- 更新 `test-antigravity-tools.sh` 头部注释中仍说SessionStart钩子的文字。

实际验收（非CI）：把分支安装到agy，在干净工作区至少三次运行“Let's make a react todo list”，每次任何代码前触发brainstorming；之后卸载。

### 8. 移植指南：独立提交

`docs/porting-to-a-new-harness.md` 描述了不存在的 `.antigravity-plugin/install.sh` 和生成的 `ANTIGRAVITY.md`，单独提交修复：

- 路由表：Antigravity使用技能索引。

- “无Skill工具”部分：替换Antigravity的`contextFileName`建议为技能索引引导，记录钩子/规则发现（无SessionStart、每次PreInvocation、钩子无`${PLUGIN_ROOT}`、共享插件根让`rules/`泄漏到Cursor）。 这替代了 `Skill` 工具和每次调用运行 `PreInvocation` 钩子的做法。

- 分发表：Antigravity从git URL安装（`agy plugin install <url>`）并列市场。

- 安装器剥离部分：删除`install.sh`/`ANTIGRAVITY.md`示例。

- 宿主索引表增加Antigravity（清单、引导、工具映射、测试、安装）。

## 范围之外

- 市场提交机制；指南未说明，走Jesse与Google联系人。

- Antigravity 2.0与IDE；本机未安装未验证，README不作声明。

- 开放PR #2350把`using-superpowers`复制进生成规则；本项落地后由Jesse决定回应，我起草答复。

- Codex同步排除项缺`.hermes-plugin/`和`.muse-plugin/`；另行修复。
