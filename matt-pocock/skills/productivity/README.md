# 生产力

通用工作流工具，不专门针对代码。

## 用户调用

只有输入名称时才可到达（Claude Code：`disable-model-invocation: true`；Codex：`agents/openai.yaml` 中 `policy.allow_implicit_invocation: false`）。

- **[grill-me](./grill-me/SKILL.md)**：就计划或设计持续深入访谈，直到设计树每个分支都解决。
- **[handoff](./handoff/SKILL.md)**：把当前对话压缩成交接文档，供另一代理继续。
- **[teach](./teach/SKILL.md)**：跨多次会话教授新技能或概念，以当前目录作为有状态教学空间。
- **[to-questionnaire](./to-questionnaire/SKILL.md)**：把你无法独自回答的决策转成 Markdown 问卷，交给能回答的人（异步填写或会议共同完成）。
- **[wait-what](./wait-what/SKILL.md)**：消息没讲清时立即使用；代理用 `GLOSSARY.md` 词汇和通俗易懂的语言补充缺失上下文后重讲。

## 模型调用

模型或用户可到达（触发措辞丰富，便于模型自行使用）。

- **[grilling](./grilling/SKILL.md)**：就计划、决策或想法持续深入访谈，直到设计树每个分支解决。
- **[writing-for-agents](./writing-for-agents/SKILL.md)**：为代理写文档：技能、`AGENTS.md`/`CLAUDE.md`，以及任何由指针到达的文档。
