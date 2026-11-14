---
name: poteto-help
description: "指导用户完成 pstack 设置、使用 /poteto-mode，并为任务选择技能、操作手册或原则。输入 /poteto-help 并附上问题。"
disable-model-invocation: true
---

# Poteto 帮助

回答用户关于 pstack 的问题，给他们一条可以发送的提示词，并链接到答案来源文件。对于求助问题，不要开始执行工作。用户问的是如何做，而运行 pstack 会实际消耗 token，因此应由他们发送提示词。

像“使用 pstack 修复这个 bug”这样要求执行工作的消息，不属于求助问题。阅读 [`poteto-mode`](../poteto-mode/SKILL.md)，按其要求完成工作，并提及一次：Custom Mode 可以使它持续启用。

本文件把问题映射到保存答案的技能和指南页面。细节以那些文件为准。引用前先阅读所指向的文件；如果它与本映射不一致，应相信它。这里的链接指向已安装的插件，用户可能无法打开，因此请提供文件的公开副本：`https://github.com/cursor/plugins/blob/main/pstack/` 加上它的路径。

## 了解他们需要什么

根据消息和对话推断需求。明确指出的情境，例如“哪个技能用来审查 PR？”，直接转到对应章节。如果需求仍然不清楚，提出一道包含以下选项的多选一问题，然后只回答他们选择的部分：

- 完成设置

- 使用 `/poteto-mode` 开始任务

- 为某个情境选择技能

- 修正一次出了问题的运行

- 定制自己的 pstack

检查会改变答案的状态，只有确实影响答案时才提及：

- 没有 `~/.cursor/rules/pstack-models.mdc` 意味着此用户尚未运行 `/setup-pstack`，所以每个角色都使用默认模型。

- 项目中没有 `verify-*` 技能或其他应用测试控制工具，意味着代理无法通过脚本操作应用。当问题涉及证明变更有效时，提及 `/create-verification-skill`。

- 项目中没有形式化验证技能，意味着检查范围无法超出测试所覆盖的属性。当问题涉及竞态、不变量或测试很少触及的其他情形时，提及 `/create-formal-verification-skill`。如果已经存在该技能，而它覆盖的代码在其记录的最后同步提交之后发生了变化，且问题涉及这些代码，则提及 `/maintain-formal-verification-skill`。

模型规则缺失且会影响答案时，询问用户是否现在为每个角色选择模型并设定推理预算。用户刚开始使用、问题涉及设置或成本，或者答案取决于运行哪些模型时，这一点会产生影响。每次聊天最多问一次。如果需求也不明确，把两个问题一起问。提供两个选项：

- 现在：告诉他们输入 `/setup-pstack`，同时也回答他们的问题。

- 以后：回答问题，并加上一行，说明在运行 `/setup-pstack` 之前，每个角色都会保留其默认模型。

## 完成设置

1. 在聊天中使用 `/add-plugin pstack` 安装，或从侧边栏的 Customize 安装。

2. 运行 [`/setup-pstack`](../setup-pstack/SKILL.md)。它会询问推理预算，为每个角色分配模型，并写入一条规则。该规则对新聊天生效。随后，除非项目已经有相应技能，否则会分别提出一次为项目生成验证技能和形式化验证技能的建议。

3. 使用 `/poteto-mode`、一个目标以及一项能够判定通过或失败的检查，开始真正的任务。

在用户调用技能之前，安装不会改变任何东西。只有 `/setup-pstack` 会根据用户措辞加载。[README](../../README.md) 和[指南第 1 页](../../docs/guide/01-setup.md) 提供了详细说明。按照 [`references/prompting.md`](references/prompting.md)，提出与用户一起组织第一条提示词。

如果用户担心成本，说明 token 花在哪里，以及如何减少消耗。pstack 会为子代理和审查小组额外消耗 token。重新运行 `/setup-pstack`，选择更小的预算或更便宜的模型。角色设置为 `auto` 或 `inherit-parent` 时，会使用聊天所用的模型；当聊天运行在 Auto 或较便宜的模型上时，这可以节省 token。缩短小组名单会减少子代理数量，每个条目对应一个。把 `/poteto-mode` 留给需要严谨处理的工作。

pstack 为 Cursor 构建，也可以在 Claude Code 中通过 `/plugin marketplace add cursor/plugins`，再运行 `/plugin install pstack@cursor-plugins` 安装。在那里，每条命令都带有 `pstack:` 前缀，例如 `/pstack:poteto-mode`。[Claude Code 适配器](../../docs/harness/claude-code.md) 映射了 Cursor 名称；需要 Bugbot 或 Automations 等 Cursor 专属功能的步骤会跳过，并附上一行说明。

其他工具也能读取这些技能，因为它们使用 Agent Skills 格式。但包括 `/poteto-mode`、`/how`、`/why` 和 `/teach` 在内的大多数工作流技能会启动具有按角色配置模型的 Cursor 子代理，而且 Custom Modes 和 `/loop` 属于 Cursor 功能，因此这些部分在其他工具中可能无法工作。

## 使用 `/poteto-mode` 开始任务

`/poteto-mode` 会将任务匹配到一份操作手册，把手册步骤复制进待办清单，并在步骤需要时运行其他技能。被跳过的步骤仍保留在清单中，形式为 `skip: <reason>`。好的提示词会说明目标以及如何判定完成。它不列出技能，因为手工编排的顺序容易遗漏或重排手册原本会保留的步骤。帮助用户组织提示词前，先阅读 [`references/prompting.md`](references/prompting.md)。[指南第 2 页](../../docs/guide/02-poteto-mode.md) 提供了示例。

`/poteto-mode` 是否持续启用，取决于用户如何启动：

- 在 `/poteto-mode` 上按 Enter，会把技能附加到一条消息。随着聊天推进，它会逐渐淡出上下文。

- 在 Mac 上按 Option+Enter、在 Windows 上按 Alt+Enter，或在技能条目中选择 Use as Mode，会把它设为 Custom Mode。在用户退出模式之前，它每轮都会留在上下文中，同时不会介入随意闲聊的轮次。

- Cursor 文档列出了 Agents Window 和 CLI 中的 Custom Modes。在其他位置，每个新任务都以 `/poteto-mode` 开始。

涉及这一点时，链接 [Cursor 的技能文档](https://cursor.com/docs/skills)。聊天中途说“new task”会让该模式重新匹配一份手册。`/poteto-mode` 已经会为手册步骤启动的子代理使用 `poteto-agent`。若要让你自行创建的子代理具有同样风格，请以 `subagent_type: "poteto-agent"` 启动。

## 选择技能

默认答案是 `/poteto-mode`，它会在步骤需要时运行多数其他技能。当用户想要的某方面程度高于或低于手册提供的程度时，才直接指出某个技能。推荐前先阅读该技能，并给出一条示例提示词。

| 用户想要 | 技能 |
|---|---|
| 严谨完成任何非简单任务 | [`/poteto-mode`](../poteto-mode/SKILL.md) |
| 在开始前检查代理是否理解目标和问题 | [`/in-your-own-words`](../in-your-own-words/SKILL.md) |
| 发送前把提示词改得更深入，而非更冗长：加入顶尖专业人士会补充的内容、其原始素材与方法，以及外部核验。它返回提示词，不执行任务 | [`/sharpen`](../sharpen/SKILL.md) |
| 了解代码现在如何工作，或新代码应放在哪里 | [`/how`](../how/SKILL.md) |
| 了解代码为何采用这种结构，或某个数字来自哪里 | [`/why`](../why/SKILL.md) |
| 用通俗说明理解某项变更或子系统 | [`/teach`](../teach/SKILL.md) |
| 回顾自己近期围绕某个主题的工作 | [`/recall`](../recall/SKILL.md) |
| 用通俗文字和小型图示了解本聊天自其上一条消息以来的变化，并列出所有等待其处理的事项，使其仅凭回复就能决定 | [`/ketchup`](../ketchup/SKILL.md) |
| 像 `/ketchup` 一样回顾，但采用带字幕的简短幻灯片视频，并在下方以文字列出待决定事项 | [`/ketchup-video`](../ketchup-video/SKILL.md) |
| 了解一个小 diff 可能破坏其范围之外的哪些东西 | [`/blast-radius`](../blast-radius/SKILL.md) |
| 在编写跨函数边界的代码前确定类型和模块结构 | [`/architect`](../architect/SKILL.md) |
| 针对同一任务说明进行多次尝试，融合成最佳版本 | [`/arena`](../arena/SKILL.md) |
| 以云代理方式，对分片并行检查，或让多个工作代理竞赛 | [`/swarm`](../swarm/SKILL.md) |
| 让不同模型审查 diff 并尝试找出漏洞 | [`/interrogate`](../interrogate/SKILL.md) |
| 有低成本本地测试时，先写测试再修复 bug | [`/tdd`](../tdd/SKILL.md) |
| 在 `.ts` 或 `.tsx` 工作中应用 TypeScript 规则 | [`/typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| 审查前去除注释，并让未编写这些注释的审查者来执行 | [`/no-comments`](../no-comments/SKILL.md) |
| 清除文字中明显的 AI 痕迹 | [`/unslop`](../unslop/SKILL.md) |
| 按标准编写文档、RFC、README、PR 描述或提交消息 | [`/technical-writing`](../technical-writing/SKILL.md) |
| 用通俗语言重新听一遍上一条回复 | [`/bro`](../bro/SKILL.md) |
| 为代理提供以脚本操作应用并证明行为的方法 | [`/create-verification-skill`](../create-verification-skill/SKILL.md) |
| 让验证技能及其功能映射重新与应用一致 | [`/maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| 对竞态、不变量或测试很少触及的其他属性进行形式化验证 | [`/create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md) |
| 在所覆盖代码变化后重新对齐形式化验证，并判断失败源于偏离还是 bug | [`/maintain-formal-verification-skill`](../maintain-formal-verification-skill/SKILL.md) |
| 向产品经理或设计师展示用户所见，将其表示成由 TLA+ 模型检查的图，并给出到达每个违规状态的最短路径 | [`/statechart`](../statechart/SKILL.md) |
| 在报告性能数字或据其行动前进行核查 | [`/benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| 执行大型或横跨多个部分的变更，或在离开后再回来审查的变更 | [`/figure-it-out`](../figure-it-out/SKILL.md) |
| 在运行过程中记录决策日志，并在之后审查 | [`/show-me-your-work`](../show-me-your-work/SKILL.md) |
| 为每个角色选择模型及推理预算 | [`/setup-pstack`](../setup-pstack/SKILL.md) |
| 把自己的工作习惯转化成个人模式技能 | [`/automate-me`](../automate-me/SKILL.md) |
| 将完成任务后学到的东西转化为技能修改 | [`/reflect`](../reflect/SKILL.md) |
| 防止代理在此仓库重复犯同样的错 | [`/correct`](../correct/SKILL.md) |
| 构建一个页面，通过按钮经 webhook 唤醒 Grok Bot | [`/make-bot-ui`](../make-bot-ui/SKILL.md) |
| 了解如何使用 pstack | `/poteto-help` |

如果本目录旁的某个技能目录没有列在表中，阅读它的 frontmatter，并根据描述进行引导。`principle-*` 目录在下方原则部分说明。

容易混淆的情形：

- `/how` 解释代码做什么。`/why` 解释原因。`/teach` 运行其中一个或两个，并通俗解释结果。

- `/arena` 给每个工作代理同样的任务说明，并融合最佳部分。`/swarm` 将工作分成分片或竞赛，返回一份报告。

- `/architect` 确定设计后立即实现。添加“with checkpoint”可在它写代码前审查设计。

- `/interrogate` 审查 diff。`/blast-radius` 寻找 diff 之外的故障，并证明让变更安全的那一个事实。

- `/recall` 跨近期聊天重建上下文。`/ketchup` 仅覆盖本聊天中用户上一条消息以来的内容。恢复某个特定聊天或分支，应使用 Session pickup 手册。

- `/figure-it-out` 设计一次严谨执行。Orchestrate 手册运行的是横跨多天和多个 PR 的工作计划。Autonomous run 手册把单个任务推进到完成条件。

不属于 pstack 的内容：

- `/deslop`、`control-cli` 和 `control-ui` 随 `cursor-team-kit` 插件提供。

- `/loop` 和 `/create-skill` 是 Cursor 内置功能。

- pstack 没有 `/orchestrate` 技能。Orchestrate 是 `/poteto-mode` 的一份手册。如果斜杠菜单显示 `/orchestrate`，它来自其他插件。

## 操作手册与原则

手册是 `/poteto-mode` 内的步骤清单，不是技能，因此没有斜杠命令。在 `/poteto-mode` 中，描述任务即可选中一份手册，以下措辞可以直接指定：

- “babysit this pr”或“check on pr 123”运行 Babysit。它将 PR 推进到可合并状态并停在那里。除非用户要求 merge、land 或 ship，否则不会合并。

- “land the stack”运行 Shipping。

- “take over this branch”运行 Session pickup。

- “pause safely”运行 Pause safely。

- “full autopilot on this queue”运行 Autopilot-full。“autopilot, don't merge”运行 Autopilot-stack。

- “run the eval playbook”运行 Eval。

没有 `/poteto-mode` 时，“babysit this pr”之类措辞可能会启动 Cursor 自身完成同类工作的技能。[`poteto-mode`](../poteto-mode/SKILL.md) 的 Playbooks 部分列出了所有手册及其适用场景。[指南第 6 页](../../docs/guide/06-verify-and-ship.md) 介绍了创建、看护及合并 PR。

pstack 没有规划技能。Cursor 的 Plan Mode 可以与其配合使用。对于跨多个阶段或堆叠 PR 的工作，要求 `/poteto-mode` 制定计划会运行[多阶段规划手册](../poteto-mode/playbooks/multi-phase-plan.md)，它只写计划，不实现。对于设计问题，Prototype 手册或 `/architect` 会先通过代码确定答案。

原则是单条规则技能，`/poteto-mode` 会读取并在回复中引用。用户很少直接调用，而用名称引导，如“应用证明它有效，给我看真实输出”。输入 `/principle-<name>` 仍可按需加载。[指南第 8 页](../../docs/guide/08-principles.md)列出了全部原则。

## 修正出错的运行

| 症状 | 解决方法 |
|---|---|
| 模式几轮后不再应用 | 它通过 Enter 启动。改用 Custom Mode 启动，或每个任务都以 `/poteto-mode` 开始。 |
| 一个问题被当作上一任务的下一步 | 说“新任务”，或说明本轮不需要该模式。 |
| 新模型选择没有效果 | `/setup-pstack` 的规则应用于新聊天，请开始新聊天。 |
| 运行成本高于预期 | 参见“完成设置”下的成本段落。 |
| 技能没有自行加载 | 只有 `/setup-pstack` 会根据用户话语加载；其他技能在用户输入命令或 `/poteto-mode` 运行时加载，而模式不会运行所有技能。 |
| 并行代理互相覆盖 | 给每个代理独立工作树，或作为各自拥有机器的云代理运行。 |
| 通宵运行有进展却没有完成 | `/loop` 需要能通过或失败的检查，而非时长。参见[指南第 7 页](../../docs/guide/07-overnight.md)。 |
| 回复仅凭构建通过宣称成功 | 要求真实命令、流程、存储值或性能剖析。这就是“证明它有效”原则。 |

运行偏离时，[`references/prompting.md`](references/prompting.md)提供一行式引导。[指南第 10 页](../../docs/guide/10-recipes-and-pitfalls.md)有更多陷阱与值得复制的配方。

## 定制自己的 pstack

- [`/automate-me`](../automate-me/SKILL.md)根据用户自己的历史起草个人模式技能，与 `/poteto-mode` 配合。

- 会话后使用 [`/reflect`](../reflect/SKILL.md)，把经验转为用户批准的技能修改。

- `/poteto-mode write a skill for <workflow>` 运行编写手册；评估手册会盲测技能变更。

- 修正行为不当的技能应单独开 PR，不夹在它出错时正在开发的功能工作里。

[指南第 9 页](../../docs/guide/09-make-it-yours.md)介绍上述每项。

## 回复

先给答案。最多提供一个代码块示例提示词，合适时改写自 [`references/recipes.md`](references/recipes.md)，然后给出该文件链接。除非用户要求完整映射，否则保持简短。
