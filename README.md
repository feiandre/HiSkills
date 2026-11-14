# Skills 中英对照学习资料

本目录收集 Matt Pocock Skills、Superpowers 和 Pstack 的固定版本源码，并为三个项目全部英文 Markdown 文档补充中文翻译。中文紧跟对应英文，保持原有 Markdown 形式。

## 来源与版本

| 子目录 | 上游来源 | 下载提交 | 全部 Markdown | 其中 SKILL.md | 许可证 |
| --- | --- | --- | ---: | ---: | --- |
| [matt-pocock](matt-pocock/) | [mattpocock/skills](https://github.com/mattpocock/skills) | `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa` | 118 | 38 | MIT |
| [superpowers](superpowers/) | [obra/superpowers](https://github.com/obra/superpowers) | `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` | 112 | 15 | MIT |
| [pstack](pstack/) | [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack) | `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe` | 169 | 61 | MIT |

下载日期：2026-10-31（北京时间）。Pstack 直接取自 Lauren Tan（Poteto）维护的原始项目目录；其 61 份技能包括 `skills/` 下的 58 份和 `automations/benny/skills/` 下的 3 份。

## 阅读入口

- [全部 399 份 Markdown 文档索引](DOCUMENTS.zh-CN.md)：包含 README、技能、references、playbooks、设计文档、实施计划、测试说明、贡献指南和版本记录。
- [114 份技能的中文索引](SKILLS.zh-CN.md)：按项目和原始目录分类。
- Matt Pocock 可从 `ask-matt`、`grilling`、`tdd`、`code-review` 和 `writing-for-agents` 开始。
- Superpowers 可从 `using-superpowers`、`brainstorming` 和 `writing-plans` 开始。
- Pstack 可从 `poteto-help`、`setup-pstack`、`poteto-mode` 和 `principle-*` 开始。

## 中英对照形式

1. 标题后紧接同层级中文标题；每个英文段落后紧接中文段落。
2. 列表项逐项对照，中文保留相同缩进、项目符号或编号；表格后紧接相同行列结构的中文表格。
3. 引用保留引用形式；代码块中的英文说明、提示词及注释提供对应中文，命令、路径、参数、API 名称和标识符保留。
4. YAML frontmatter 的原字段和值保持原样，中文对照作为注释放在 frontmatter 中，保留元数据的可解析性。
5. 每个译文块以不可见的 `zh-CN:begin` / `zh-CN:end` 标记关联原文，便于核验与维护。英文原文的文字及顺序完整保留；移除译文插入块后，可以重建原始文件并核对 SHA-256。
6. 翻译覆盖所有英文 `.md` 文档。纯命令、路径、机器标识和无自然语言的代码不需要语言转换，按原样保留并在核验数据中记录原因。

中文译文是本地学习补充，不属于上游官方译文。上游技能中的环境要求按原文保留，Pstack 的部分工作流依赖 Cursor 功能。下载过程没有执行上游脚本或工作流，也没有把这些副本注册为全局技能。

## 来源与核验

- [`matt-pocock.source.json`](matt-pocock.source.json)、[`superpowers.source.json`](superpowers.source.json)、[`pstack.source.json`](pstack.source.json)：上游地址、完整提交号、下载时间、原始压缩包和文件的 SHA-256。
- `.downloads/`：原始下载压缩包。
- `.inline-translation/`：分段、译文映射和上一版资料备份，供维护及核验使用。
- [`verification-report.json`](verification-report.json)：文档覆盖、相邻译文块、原文重建哈希和配套文件完整性核验结果。
- [`translation-audit.json`](translation-audit.json)：标题、列表、表格、代码围栏、链接目标和行内标识的结构审计结果。
- 重新核验：`python -X utf8 tools/inline_translation.py verify`。

核验涵盖本地文件完整性与中英对照结构。上游技能是否适用于具体代理环境，需要在对应环境中另行验证。许可证和版权声明保留在各自项目目录中。
