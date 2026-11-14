# 平台无关配置文件引用——阶段 B 设计

## 背景

阶段 A（见 `2026-05-05-platform-neutral-prose-design.md`）将以第三人称泛化称呼“Claude”的文字替换为智能体中立形式。本阶段处理下一类：技能内对平台指令文件（CLAUDE.md、AGENTS.md、GEMINI.md）的引用。

插件运行于多个运行环境，各自读取自己的指令文件。技能把 CLAUDE.md 当作唯一文件，是 Claude Code 中心假设，在 Codex／Gemini CLI／OpenCode 上不成立。

## 范围内

活动技能中的两行：

1. **`skills/writing-skills/SKILL.md:58`**——`Project-specific conventions (put in CLAUDE.md)`（项目专属约定，放在 CLAUDE.md）

2. **`skills/receiving-code-review/SKILL.md:30`**——`"You're absolutely right!" (explicit CLAUDE.md violation)`（这句话明确违反了 CLAUDE.md）

## 范围外

- **`skills/using-superpowers/SKILL.md:22, 26`**——指令优先级列表已同时列出 CLAUDE.md、GEMINI.md、AGENTS.md，这是正确的：该节描述多平台插件中什么算用户指令。无需改动。

- **历史／示例产物**：

- `skills/systematic-debugging/CREATION-LOG.md`——`~/.claude/CLAUDE.md` 是历史事实。

- `skills/writing-skills/examples/CLAUDE_MD_TESTING.md`——整个文件是测试 CLAUDE.md 内容变体的完整示例。文件名、正文及 `testing-skills-with-subagents.md` 的引用都保留，规范化会破坏示例。

- **平台工具引用**——阶段 D 候选：

- `skills/using-superpowers/SKILL.md:40`（Gemini CLI 关于 GEMINI.md 的工具映射说明）

- `skills/using-superpowers/references/gemini-tools.md`（`save_memory` 保存到 GEMINI.md）

## 替换规则

两个明确调用，各对应一行。

### 规则 1：“项目专属约定放哪里”

`writing-skills/SKILL.md:58`（修改位置）：

- **之前：** `Project-specific conventions (put in CLAUDE.md)`（项目专属约定，放在 CLAUDE.md）

- **之后：** `Project-specific conventions (put in your instructions file)`（项目专属约定，放在你的指令文件）

使用通用短语而不选一个文件名。不同运行环境读取不同文件（CLAUDE.md、AGENTS.md、GEMINI.md 等），技能不应假设只有一个。平台工具参考文档（`references/{codex,copilot,gemini}-tools.md`）是说明各平台首选文件的位置。

### 规则 2：“(explicit CLAUDE.md violation)”括注

`receiving-code-review/SKILL.md:30`（修改位置）：

- **之前：** `"You're absolutely right!" (explicit CLAUDE.md violation)`（这句话明确违反了 CLAUDE.md）

- **之后：** `"You're absolutely right!" (explicit instruction-file violation)`（这句话明确违反了指令文件）

括注有实际作用：它说明该短语不只是风格差，而是主动违反许多用户写入指令文件的规则。“指令文件”是跨平台综合称呼 AGENTS.md／CLAUDE.md／GEMINI.md 的自然术语，保留原信号，不软化。

## 提交计划

按顺序原子提交：

1. **`writing-skills/SKILL.md`**——项目约定行将 CLAUDE.md 改为“你的指令文件”

2. **`receiving-code-review/SKILL.md`**——违规括注改为指令文件

3. **平台工具参考文档**——在各 `references/{codex,copilot,gemini}-tools.md` 加入平台首选指令文件名（CLAUDE.md、AGENTS.md、GEMINI.md 等），让读者解析真实文件。

每个提交消息说明“阶段 B”和切片。

## 验证

每次提交后：

- 阅读周边段落，确认语法和含义可解析。

- `grep -n "CLAUDE\.md" <touched-file>`——活动正文无剩余命中（已记录例外除外）。

两个提交后：

- `grep -rn "CLAUDE\.md" skills/` 只应返回已记录例外（CREATION-LOG、CLAUDE_MD_TESTING 及其入站引用、using-superpowers 优先级列表）。

## 非目标

- 不改 `using-superpowers/SKILL.md` 优先级顺序；重排只是审美，不在范围。

- 不重命名或修改 `examples/CLAUDE_MD_TESTING.md`。

- 不修改 Gemini CLI 专属工具引用（阶段 D 候选）。

## 实现说明

本设计覆盖三次提交和三个非 Claude Code 平台工具参考。实现进一步加入第四个 `references/claude-code-tools.md`，提交 `8505703`，使 Claude Code 指令文件约定和工具名列表与其他平台并列，而非隐式散在正文。规格未预料，但符合意图。
