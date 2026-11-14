# 进行中
测试阶段。这些技能有意公开：试用并告诉我哪里坏了。它们晋升到稳定分类前不会进入插件和顶层 README，没有文档页面，并且可能变更或消失且不另行通知。
插件不会提供这些技能。直接安装一个：
```bash
npx skills@latest add mattpocock/skills --skill=<name>
```
- **[loop-me](./loop-me/SKILL.md)**：在多个会话中把自己追问成可实施的工作流规格，把当前目录作为有状态工作区。由用户调用。
- **[writing-beats](./writing-beats/SKILL.md)**：把文章塑造成节拍旅程，采用自选冒险式结构。选择一个起始节拍，只写它，再转向下一节拍，直到文章自然结束。
- **[writing-fragments](./writing-fragments/SKILL.md)**：通过追问挖掘写作片段（异构的文字小料），追加到单个文档，作为未来文章的原料。
- **[writing-shape](./writing-shape/SKILL.md)**：取含原料的 Markdown 文件，逐段塑造成文章，并在每一步论证格式选择。
- **[claude-handoff](./claude-handoff/SKILL.md)**：把当前对话交给立即接手工作的新后台智能体，并通过 `claude --bg` 提供交接摘要。由用户调用。
- **[setup-ts-deep-modules](./setup-ts-deep-modules/SKILL.md)**：将 dependency-cruiser 接入 TypeScript 仓库，使每个包都是深模块：实现藏在子文件夹，只能通过入口文件到达，测试也通过入口进行。由用户调用。
