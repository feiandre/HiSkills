# 平台中立文字——A 阶段设计

## 背景

Superpowers 面向 Claude Code、Codex、Cursor、OpenCode、Copilot CLI、Gemini CLI 等运行时。技能和文档最初为 Claude Code 编写，通用语境仍使用“Claude”。OpenAI 的 vendored fork 曾整体改写并误改历史归属、模型名、安装说明；我们要避免此问题，同时移除真正附带平台假设的文字。

工作按引用类别分阶段。**本规格只涵盖 A 阶段**：非平台专属语境中的通用第三人称“Claude”。后续配置文件、营销文案、工具名引用另行规格。

## 范围

通用文字中的“Claude”：

- 活跃技能目录中的 `skills/*/SKILL.md` 及配套 `.md`

- `README.md`（仅通用文字，不是平台营销）

另重命名术语：**Claude Search Optimization (CSO) → Skill Discovery Optimization (SDO)**，位于 `skills/writing-skills/SKILL.md`。

## 不在范围

- **平台/运行时陈述**：“In Claude Code:”、安装说明、工具映射（D 阶段候选）。

- **配置文件引用**：CLAUDE.md、AGENTS.md、GEMINI.md 优先级和项目约定位置（B 阶段）。

- **工具名引用**：`Skill`、`Bash`、`Read`、`Task`、`TodoWrite`。技能使用 Claude Code 词汇，现有平台映射解释；本规格原计划延后，E 阶段最终改为动作语言并统一映射；其中相关的字段或标识包括 `references/{codex,copilot,gemini}-tools.md`。

- **营销文案**：README 的“Superpowers for Claude Code”和平台安装节（C 阶段）。

- **历史产物**：`docs/plans/*.md`、`docs/superpowers/specs/*.md`、`CREATION-LOG.md`；改写等于改写历史。

- **模型标识**：Claude Haiku / Sonnet / Opus 是真实产品名。

- **文件名/URL**：`CLAUDE.md`、`claude.com`、`claude-plugin/`、`~/.claude/` 下路径。

- **`anthropic-best-practices.md` 文件名**：正文重写但文件仍按来源命名。

## 替换风格

使用英文自然混合：

- **第二人称“your agent”**：向技能作者谈其运行时

- “你的代理阅读描述”

- **第三人称“the agent”/“agents”/“an agent”**：通用描述系统行为

- “未来代理会找到技能”

- “使用代理会搜索的词”

- “只有技能相关时代理才读 SKILL.md”

按句意选择，不为一致性牺牲自然表达。自然使用复数“未来代理”“代理阅读”，不必总说“该代理”。

### 保留“Claude”的例外

- 模型名：Claude Haiku、Claude Sonnet、Claude Opus

- 文件名与 URL：`CLAUDE.md`、`claude.com`、`~/.claude/`

- 品牌平台名“Claude Code”指运行时本身时保留（后续阶段处理）

### 术语重命名

- **Claude Search Optimization (CSO) → Skill Discovery Optimization (SDO)**（术语重命名）

- 出现在 `skills/writing-skills/SKILL.md` 标题及邻近文字。重命名标题、缩写和文件内引用。

## 影响文件

排除例外后的近似 `grep` 计数：

| 文件 | 通用文字出现次数 |
|------|------------------------|
| `skills/writing-skills/SKILL.md` | 约 12（含 CSO 标题与正文） |
| `skills/writing-skills/anthropic-best-practices.md` | 约 30 |
| `skills/writing-skills/examples/CLAUDE_MD_TESTING.md` | 约 1；文件名保留，它是 CLAUDE.md 测试产物；“Variant C: Claude.AI Emphatic Style”标题也保留，它是具体风格标签 |
| `README.md` | 约 1 |

实施时重跑过滤 grep 确认最终列表。

## 提交计划

四个原子提交，按顺序：

1. **CSO → SDO**：`skills/writing-skills/SKILL.md`，机械隔离，术语变动时可回退。

2. **活跃技能文字**：`skills/*/SKILL.md` 及配套 `.md` 的通用“Claude”改为 agent，排除 best-practices；其中相关的字段或标识包括 `anthropic-best-practices.md`。

3. **`anthropic-best-practices.md` 文字**：同一规则；单独提交因它是外部文档的 vendored 改编，便于与上游协调。

4. **README.md 文字**（仅过滤后仍有通用出现）。空则跳过。

每个提交注明 A 阶段和切片（“CSO 改 SDO”“活跃技能代理文字”等），使系列自说明。

## 验证

每次提交后：

- `grep -rn "Claude" <touched-paths>`：剩余命中必须属于记录例外（模型、文件名、URL、平台名、历史产物）。

- 从头到尾阅读改动文件：替换未破坏句子、代词一致和列表并列。

- 无测试，只改文字。

最终提交后：

- 在实时会话浏览每个修改技能，确认表达自然。

## 非目标

- 不改行为、结构、标题（CSO→SDO 除外）、示例、代码块或 YAML。

- 不新增章节、提示框或兼容说明。

- 编辑时不过度“改进”替换之外文字。
