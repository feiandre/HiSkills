# pstack

<!-- zh-CN:begin 362d5bc0650da0a5 -->

# pstack 工具集

<!-- zh-CN:end 362d5bc0650da0a5 -->

i'm [poteto](https://x.com/poteto). i'm not a president or ceo, but i've worked with millions of lines of code at Meta, Netflix, and Cursor. i'm also on the react core team where i help build and maintain react compiler.

<!-- zh-CN:begin d2e23076238de72a -->

我是 [poteto](https://x.com/poteto)。我不是总裁或 CEO，但在 Meta、Netflix 和 Cursor 处理过数百万行代码。我也是 React 核心团队成员，参与构建和维护 React Compiler。

<!-- zh-CN:end d2e23076238de72a -->

there's a growing sense that ai writes too much slop code. i agree. i don't want to ship like a team of twenty slop artists. throughput without quality is not a goal i aspire to. if you want to go fast, go deep first. 

<!-- zh-CN:begin e33628cbee457ee5 -->

越来越多人觉得 AI 写了太多劣质代码。我同意。我不想像二十个粗制滥造的人组成的团队那样交付。只有产量而没有质量并非我追求的目标。如果你想快，先做深。

<!-- zh-CN:end e33628cbee457ee5 -->

**pstack is my answer.** these are the same skills i use every day to ship high quality code at Cursor. this turns cursor into a real engineering team. the goal is not to maximize loc, in fact it's the opposite. pstack helps you write less, but higher quality code.

<!-- zh-CN:begin 8a18e7b623671c29 -->

**pstack 就是我的答案。** 这些就是我每天在 Cursor 用来交付高质量代码的技能。它让 Cursor 成为真正的工程团队。目标不是最大化代码行数，实际上恰恰相反。pstack 帮助你写更少、但质量更高的代码。

<!-- zh-CN:end 8a18e7b623671c29 -->

**pstack gives you fearless parallelism.** when you can go deep on one agent and trust it to write good, verifiable code, you can truly parallelize with confidence. start multiple agents up with `poteto-mode` and trust that they'll apply rigorous engineering principles to their work.

<!-- zh-CN:begin fe5f567e7457021a -->

**pstack 让你无惧并行。** 当你能让一个智能体深入工作，并信任它写出优质、可验证的代码时，你才能真正放心地并行。用 `poteto-mode` 启动多个智能体，相信它们会在工作中运用严格的工程原则。

<!-- zh-CN:end fe5f567e7457021a -->

**cursor gives you the best of all worlds.** every frontier model has its strengths and weaknesses. use any model with pstack. in fact, many of my skills use multi-model workflows to take advantage of each model's unique strengths.

<!-- zh-CN:begin e1a81892a9df1eb4 -->

**Cursor 让你兼得各家之长。** 每个前沿模型都有自己的优点和缺点。pstack 可搭配任何模型。事实上，我的许多技能采用多模型工作流，利用各个模型独特的优势。

<!-- zh-CN:end e1a81892a9df1eb4 -->

fork it. improve it. make it yours. PRs are welcome! 

<!-- zh-CN:begin d8f2655e02a05925 -->

派生它、改进它、让它成为你的工具。欢迎提交 PR！

<!-- zh-CN:end d8f2655e02a05925 -->

## install

<!-- zh-CN:begin 90915eba8c472f4e -->

## 安装

<!-- zh-CN:end 90915eba8c472f4e -->

```bash
/add-plugin pstack
```

in claude code:

<!-- zh-CN:begin 11857d35ab2836de -->

在 Claude Code 中：

<!-- zh-CN:end 11857d35ab2836de -->

```bash
/plugin marketplace add cursor/plugins
/plugin install pstack@cursor-plugins
```

claude code leaves auto-update off for third-party marketplaces, so pstack stays on the version you installed. to turn it on, run `/plugin`, open the **marketplaces** tab, select `cursor-plugins`, and choose **enable auto-update**. to update once by hand, run `claude plugin update pstack@cursor-plugins`.

<!-- zh-CN:begin ce099522ee516740 -->

Claude Code 默认关闭第三方市场的自动更新，因此 pstack 会停留在安装时的版本。要启用自动更新，运行 `/plugin`，打开**市场**选项卡，选择 `cursor-plugins`，再选择**启用自动更新**。要手动更新一次，运行 `claude plugin update pstack@cursor-plugins`。

<!-- zh-CN:end ce099522ee516740 -->

claude code prefixes plugin commands and agents, so `/poteto-mode` is `/pstack:poteto-mode`. the [claude code adapter](./docs/harness/claude-code.md) maps every other cursor name. in claude code, `/pstack:setup-pstack` writes your model choices to `~/.claude/rules/pstack-models.md`, and a step that needs a cursor-only feature, such as bugbot or automations, is skipped with a one-line note.

<!-- zh-CN:begin 18a59dd593db84fb -->

Claude Code 为插件命令和智能体添加前缀，因此 `/poteto-mode` 在这里是 `/pstack:poteto-mode`。[Claude Code 适配器](./docs/harness/claude-code.md) 提供其他所有 Cursor 名称的映射。在 Claude Code 中，`/pstack:setup-pstack` 会将你选择的模型写入 `~/.claude/rules/pstack-models.md`；需要 Bugbot 或 Automations 等 Cursor 专属功能的步骤会跳过，并用一行说明。

<!-- zh-CN:end 18a59dd593db84fb -->

claude code installs a generated copy of pstack, including this readme and the guide, from [`harness/pstack/`](https://github.com/cursor/plugins/tree/main/harness/pstack) at the repository root. after you change pstack, run `node scripts/generate-pstack-harness-trees.mjs` from the repository root and commit the result. ci fails while the generated copy is out of date.

<!-- zh-CN:begin f0bfacce71582ffa -->

Claude Code 从仓库根目录的 [`harness/pstack/`](https://github.com/cursor/plugins/tree/main/harness/pstack) 安装生成的 pstack 副本，其中包含本自述文件和指南。更改 pstack 后，在仓库根目录运行 `node scripts/generate-pstack-harness-trees.mjs` 并提交结果。只要生成副本未更新，CI 就会失败。

<!-- zh-CN:end f0bfacce71582ffa -->

## get started

<!-- zh-CN:begin 4fc021dca4368243 -->

## 入门

<!-- zh-CN:end 4fc021dca4368243 -->

two steps:

<!-- zh-CN:begin e823e9f973dcab76 -->

两个步骤：

<!-- zh-CN:end e823e9f973dcab76 -->

1. run [`/setup-pstack`](./skills/setup-pstack/SKILL.md), pick a reasoning budget, and choose which models you want.

<!-- zh-CN:begin f9b6bc2d7e9e132a -->

1. 运行 [`/setup-pstack`](./skills/setup-pstack/SKILL.md)，选择推理预算和要使用的模型。

<!-- zh-CN:end f9b6bc2d7e9e132a -->
2. use [`/poteto-mode`](./skills/poteto-mode/SKILL.md) whenever you're doing anything that requires rigor.

<!-- zh-CN:begin 6c3439915e199e74 -->

2. 凡是需要严谨处理的工作，都使用 [`/poteto-mode`](./skills/poteto-mode/SKILL.md)。

<!-- zh-CN:end 6c3439915e199e74 -->

new here? the [pstack guide](./docs/guide/README.md) walks you through a first real task, from setup and prompting through verification and overnight runs. stuck, or unsure which skill fits? ask [`/poteto-help`](./skills/poteto-help/SKILL.md).

<!-- zh-CN:begin 05e7dc6ecf0b4b5c -->

第一次使用？[pstack 指南](./docs/guide/README.md) 会带你完成第一个真实任务，从设置和提示词到验证与整夜运行。遇到困难，或不确定哪个技能合适？询问 [`/poteto-help`](./skills/poteto-help/SKILL.md)。

<!-- zh-CN:end 05e7dc6ecf0b4b5c -->

that's it. the other skills are situational, and the mode skill uses them for you as needed. out of the box the mode splits work by model strength: code delegates (feature, refactoring, bug fix, perf, hillclimb) go to grok, while the hardest changes, prose, and judgment go to opus 5.5. the default panel is opus 5.5 / grok. [`/setup-pstack`](./skills/setup-pstack/SKILL.md) changes any of it.

<!-- zh-CN:begin baca76f00270ee0d -->

就是这样。其他技能按场景使用，模式技能会根据需要替你调用它们。默认情况下，该模式按模型优势分工：代码委派任务（功能、重构、缺陷修复、性能、爬山优化）交给 Grok，最困难的改动、文字写作和判断交给 Opus 5.5。默认评审组是 Opus 5.5 / Grok。[`/setup-pstack`](./skills/setup-pstack/SKILL.md) 可以更改其中任何设置。

<!-- zh-CN:end baca76f00270ee0d -->

## usage

<!-- zh-CN:begin 32b86f6a215fcc96 -->

## 使用方式

<!-- zh-CN:end 32b86f6a215fcc96 -->

use [`/poteto-mode`](./skills/poteto-mode/SKILL.md) at the start of a task. it reads your request, picks from a set of playbooks, and runs the other skills as the steps need them.

<!-- zh-CN:begin 927965674eee29e2 -->

在任务开始时使用 [`/poteto-mode`](./skills/poteto-mode/SKILL.md)。它会读取你的请求，从一组操作手册中选择合适的手册，并在各步骤需要时运行其他技能。

<!-- zh-CN:end 927965674eee29e2 -->

pick `/poteto-mode` from the `/` menu before you type your task, so cursor attaches the skill to the message.

<!-- zh-CN:begin 27ad39432171cd9e -->

输入任务之前，先从 `/` 菜单选择 `/poteto-mode`，这样 Cursor 会把技能附加到消息中。

<!-- zh-CN:end 27ad39432171cd9e -->

### just use [`/poteto-mode`](./skills/poteto-mode/SKILL.md)

<!-- zh-CN:begin 45d39b244d7dc5ed -->

### 直接使用 [`/poteto-mode`](./skills/poteto-mode/SKILL.md)

<!-- zh-CN:end 45d39b244d7dc5ed -->

this skill is the main shortcut. i use it whenever i need the agent to do rigorous engineering work. it comes with twenty-three playbooks:

<!-- zh-CN:begin 1c4827e397758f6f -->

这个技能是主要入口。每当需要智能体进行严谨的工程工作时，我都会用它。它附带二十三份操作手册：

<!-- zh-CN:end 1c4827e397758f6f -->

```
/poteto-mode this pr has a subtle bug where the scroll drifts every 750ms even when idle. repro
first, then fix and verify.
```

<!-- zh-CN:begin 5acfe94d254357fd -->

```
/poteto-mode 这个 PR 有个隐蔽缺陷：即使空闲，滚动位置也会每隔 750ms 漂移。
先复现，再修复并验证。
```

<!-- zh-CN:end 5acfe94d254357fd -->

```
/poteto-mode i'm going to bed. land the stack even if ci flakes. i want everything merged by
morning.
```

<!-- zh-CN:begin 321cde9e4bf6bdd9 -->

```
/poteto-mode 我要睡觉了。即使 CI 偶发失败，也把这组堆叠 PR 落地。我希望到明天早上
全部合并。
```

<!-- zh-CN:end 321cde9e4bf6bdd9 -->

<details>
<summary>the twenty-three playbooks<!-- zh-CN:begin 75b6449ed2078875 --><br>二十三份操作手册<!-- zh-CN:end 75b6449ed2078875 --></summary>

| playbook | for |
|---|---|
| [investigation](./skills/poteto-mode/playbooks/investigation.md) | a read-only question. how does x work, why was y built this way, are we sure. |
| [bug fix](./skills/poteto-mode/playbooks/bug-fix.md) | reproduce a defect, root-cause it, and fix with runtime evidence. |
| [perf](./skills/poteto-mode/playbooks/perf-issue.md) | trace a measured slowness and improve it against a baseline. |
| [hillclimb](./skills/poteto-mode/playbooks/hillclimb.md) | sustained, scientific improvement of one metric against a target, looping hypotheses with before/after measurement and one commit per accepted win. |
| [runtime forensics](./skills/poteto-mode/playbooks/runtime-forensics.md) | diagnose a live symptom (leak, idle-cpu spin, glitch) from instrumentation. |
| [trace forensics](./skills/poteto-mode/playbooks/trace-forensics.md) | diagnose a captured profiling artifact (cpuprofile, trace, spindump, heap snapshot). |
| [feature](./skills/poteto-mode/playbooks/feature.md) | new or changed behavior, built from a named data shape. |
| [refactoring](./skills/poteto-mode/playbooks/refactoring.md) | a behavior-preserving change to structure or shape. |
| [prototype](./skills/poteto-mode/playbooks/prototype.md) | a throwaway sketch to make a design or behavioral decision cheaply, or to settle an empirical fork by observing it. |
| [visual parity](./skills/poteto-mode/playbooks/visual-parity.md) | pixel-exact ui equivalence between two implementations. |
| [authoring a skill](./skills/poteto-mode/playbooks/authoring-a-skill.md) | writing or editing a SKILL.md. |
| [eval](./skills/poteto-mode/playbooks/eval.md) | test how a skill or prompt change affects agent behavior, blinded. |
| [babysit](./skills/poteto-mode/playbooks/babysit.md) | drive a pr or a stack to merge-ready: conflicts, review threads, ci. |
| [shipping](./skills/poteto-mode/playbooks/shipping.md) | independently verify a green stack, then land the contiguous verified run bottom-up through github by default or origin when available. |
| [autonomous run](./skills/poteto-mode/playbooks/autonomous-run.md) | drive a long task to completion without stopping. |
| [orchestrate](./skills/poteto-mode/playbooks/orchestrate.md) | a standing project handed to one coordinator chat: multi-day, many stacked prs, fleets of subagents. |
| [autopilot-full](./skills/poteto-mode/playbooks/autopilot-full.md) | run independent prs to merged with one owner per pr. a swarm verifies each code-ready head, and every later change to the patch gets a fresh check. |
| [autopilot-stack](./skills/poteto-mode/playbooks/autopilot-stack.md) | autopilot-full without the merge. build and verify prs for the operator to review and land, stacking a pr only on a pr it builds on. |
| [session pickup](./skills/poteto-mode/playbooks/session-pickup.md) | resume or take over a prior agent's in-flight work. |
| [pause safely](./skills/poteto-mode/playbooks/pause-safely.md) | suspend in-flight work cleanly so it can be resumed later. |
| [multi-phase plan](./skills/poteto-mode/playbooks/multi-phase-plan.md) | work that spans phases or stacked PRs. |
| [worktree cleanup](./skills/poteto-mode/playbooks/worktree-cleanup.md) | reclaim disk by pruning merged or abandoned worktrees and stale ios simulators, safety-gated. |
| [opening a pr](./skills/poteto-mode/playbooks/opening-a-pr.md) | open a ready pr from small ordered commits with a conventional commits title and a briefing-style body. invoked at the end of every other playbook. |

<!-- zh-CN:begin a1224fd7e717b2fa -->

| 操作手册 | 适用场景 |
|---|---|
| [调查](./skills/poteto-mode/playbooks/investigation.md) | 只读问题：X 如何工作、为什么这样构建 Y、我们是否确定。 |
| [缺陷修复](./skills/poteto-mode/playbooks/bug-fix.md) | 复现缺陷、找出根因，并用运行时证据验证修复。 |
| [性能](./skills/poteto-mode/playbooks/perf-issue.md) | 追踪已测量的缓慢现象，并对照基线改进。 |
| [爬山优化](./skills/poteto-mode/playbooks/hillclimb.md) | 面向目标持续、科学地改进单一指标，循环提出假设、测量前后变化，每项被接受的收益单独提交。 |
| [运行时取证](./skills/poteto-mode/playbooks/runtime-forensics.md) | 通过插桩诊断正在发生的症状（泄漏、空闲时 CPU 空转、异常抖动）。 |
| [跟踪取证](./skills/poteto-mode/playbooks/trace-forensics.md) | 诊断捕获的性能分析产物（cpuprofile、trace、spindump、堆快照）。 |
| [功能](./skills/poteto-mode/playbooks/feature.md) | 从明确命名的数据结构出发，构建新增或变更行为。 |
| [重构](./skills/poteto-mode/playbooks/refactoring.md) | 在保持行为不变的前提下更改结构或形态。 |
| [原型](./skills/poteto-mode/playbooks/prototype.md) | 用一次性草图低成本决定设计或行为，或通过观察解决需要实证判断的分歧。 |
| [视觉一致性](./skills/poteto-mode/playbooks/visual-parity.md) | 两种实现之间精确到像素的 UI 等价。 |
| [编写技能](./skills/poteto-mode/playbooks/authoring-a-skill.md) | 编写或编辑 SKILL.md。 |
| [评测](./skills/poteto-mode/playbooks/eval.md) | 以盲测方式测试技能或提示词变更如何影响智能体行为。 |
| [看护](./skills/poteto-mode/playbooks/babysit.md) | 处理冲突、评审讨论和 CI，推动一个 PR 或一组堆叠 PR 达到可合并状态。 |
| [交付](./skills/poteto-mode/playbooks/shipping.md) | 独立验证全部通过的 PR 栈，再自底向上落地连续验证通过的部分，默认通过 GitHub，也可使用可用的 origin。 |
| [自主运行](./skills/poteto-mode/playbooks/autonomous-run.md) | 不停顿地推动长任务完成。 |
| [编排](./skills/poteto-mode/playbooks/orchestrate.md) | 将长期项目交给一个协调聊天：跨多天、涉及许多堆叠 PR 和成批子智能体。 |
| [全自动驾驶](./skills/poteto-mode/playbooks/autopilot-full.md) | 每个独立 PR 配一位负责人，推动至合并。工作群验证每个代码就绪的 head，补丁后续每次变动都重新检查。 |
| [堆叠自动驾驶](./skills/poteto-mode/playbooks/autopilot-stack.md) | 不执行合并的 autopilot-full。构建并验证 PR，供操作者审阅和落地；仅在一个 PR 依赖另一个 PR 时才将两者堆叠。 |
| [接续会话](./skills/poteto-mode/playbooks/session-pickup.md) | 恢复或接管先前智能体尚在进行的工作。 |
| [安全暂停](./skills/poteto-mode/playbooks/pause-safely.md) | 干净地暂停进行中的工作，以便稍后恢复。 |
| [多阶段计划](./skills/poteto-mode/playbooks/multi-phase-plan.md) | 跨阶段或跨堆叠 PR 的工作。 |
| [工作树清理](./skills/poteto-mode/playbooks/worktree-cleanup.md) | 在安全门控下修剪已合并或已放弃的工作树和陈旧 iOS 模拟器，回收磁盘空间。 |
| [创建 PR](./skills/poteto-mode/playbooks/opening-a-pr.md) | 用有序的小提交创建就绪 PR，采用 Conventional Commits 标题和简报式正文。其他每份操作手册结束时都会调用它。 |

<!-- zh-CN:end a1224fd7e717b2fa -->

</details>



when invoked it:

<!-- zh-CN:begin bef9baeadb6e9860 -->

调用时，它会：

<!-- zh-CN:end bef9baeadb6e9860 -->

1. matches your task to a [playbook](./skills/poteto-mode/playbooks/) and opens a todo list whose first items are its steps, copied in verbatim.

<!-- zh-CN:begin 49754832318db7cd -->

1. 为任务匹配一份[操作手册](./skills/poteto-mode/playbooks/)，并创建待办清单，把手册步骤逐字复制为前几项。

<!-- zh-CN:end 49754832318db7cd -->
2. routes to the other skills as the steps fire.

<!-- zh-CN:begin 14c5a452003f89b5 -->

2. 在执行各步骤时路由到其他技能。

<!-- zh-CN:end 14c5a452003f89b5 -->
3. writes unslopped replies framed for the consumer and the maintainer.

<!-- zh-CN:begin c963c291cd8e7a10 -->

3. 从使用者和维护者的角度组织回答，清除粗制滥造的措辞。

<!-- zh-CN:end c963c291cd8e7a10 -->

the full rules and playbooks live in [`skills/poteto-mode/SKILL.md`](./skills/poteto-mode/SKILL.md).

<!-- zh-CN:begin 624f0d9ad25d1d0c -->

完整规则和操作手册位于 [`skills/poteto-mode/SKILL.md`](./skills/poteto-mode/SKILL.md)。

<!-- zh-CN:end 624f0d9ad25d1d0c -->

to keep [`/poteto-mode`](./skills/poteto-mode/SKILL.md) on across turns, pick it from the `/` menu and press option+enter (mac) or alt+enter (windows) instead of enter. that makes it a [custom mode](https://cursor.com/docs/skills#using-a-skill-as-a-custom-mode), which cursor offers in the agents window and the cli. it stays in context every turn until you exit the mode. plain enter attaches it to one message only.

<!-- zh-CN:begin f0485262eb738fc6 -->

要让 [`/poteto-mode`](./skills/poteto-mode/SKILL.md) 跨轮次保持启用，请从 `/` 菜单选择它，并按 Option+Enter（Mac）或 Alt+Enter（Windows），而不是 Enter。这样它就成为一种[自定义模式](https://cursor.com/docs/skills#using-a-skill-as-a-custom-mode)，可在 Cursor 的智能体窗口和 CLI 中使用。退出模式前，每一轮它都会留在上下文中。普通 Enter 只会将它附加到一条消息。

<!-- zh-CN:end f0485262eb738fc6 -->

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) works extremely well with cursor's `/loop` command. you can make cursor work for many hours without sacrificing rigor.

<!-- zh-CN:begin 4e7e36c2aa1291e9 -->

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) 与 Cursor 的 `/loop` 命令配合得非常好。你可以让 Cursor 连续工作数小时，同时保持严谨。

<!-- zh-CN:end 4e7e36c2aa1291e9 -->

## skills

<!-- zh-CN:begin 47ef2423a5e59d22 -->

## 技能

<!-- zh-CN:end 47ef2423a5e59d22 -->

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) runs most of these for you when a step needs them (`how`, `why`, `architect`, `arena`, `swarm`, `interrogate`, `unslop`, `no-comments`, `technical-writing`, `tdd`, and the principles). the table below is for when you want one directly:

<!-- zh-CN:begin 7e2b553280084a9f -->

当步骤需要时，[`/poteto-mode`](./skills/poteto-mode/SKILL.md) 会替你运行下列大多数技能（`how`、`why`、`architect`、`arena`、`swarm`、`interrogate`、`unslop`、`no-comments`、`technical-writing`、`tdd`，以及各项原则）。想直接使用某个技能时，可参考下表：

<!-- zh-CN:end 7e2b553280084a9f -->

```
/how do we cancel runs? do we have an n+1 when we look up every run to cancel?
```

<!-- zh-CN:begin 0fc85151950f6dc9 -->

```
/how 我们如何取消运行？逐个查找要取消的运行时，会不会出现 n+1 问题？
```

<!-- zh-CN:end 0fc85151950f6dc9 -->

```
/interrogate review this pr.
```

<!-- zh-CN:begin fca3084bbd18c240 -->

```
/interrogate 审查这个 PR。
```

<!-- zh-CN:end fca3084bbd18c240 -->

<details>
<summary>all skills<!-- zh-CN:begin 4660a900b72be34a --><br>全部技能<!-- zh-CN:end 4660a900b72be34a --></summary>

| skill | use it when |
|---|---|
| [`/poteto-mode`](./skills/poteto-mode/SKILL.md) | default entry point for any non-trivial task. |
| [`/poteto-help`](./skills/poteto-help/SKILL.md) | you're new to pstack, or unsure which skill, playbook, or principle fits. finds out what you're trying to do, answers that part, and hands you a prompt to type. runs only when you type `/poteto-help`. |
| [`/in-your-own-words`](./skills/in-your-own-words/SKILL.md) | you want the agent to play back your goal and the problem before it starts. runs only when you type `/in-your-own-words`. |
| [`/sharpen`](./skills/sharpen/SKILL.md) | you want a prompt made deeper, not bigger, before you send it: what a top professional would do that you didn't ask for, the raw material they'd start from, their methods and tools, and an outside check that the result is right. hands back the rewritten prompt and leaves your choices open. doesn't do the task. runs only when you type `/sharpen`. |
| [`/how`](./skills/how/SKILL.md) | you want a walkthrough of how a subsystem works. |
| [`/why`](./skills/why/SKILL.md) | you want to know why something was built this way. discovers available MCPs at run time and queries each evidence category in parallel (source control, issue tracker, long-form docs, real-time chat, infra observability, error tracking, analytics warehouse). |
| [`/recall`](./skills/recall/SKILL.md) | you're starting or resuming work and want your recent context on a topic rebuilt from your own chat history and the shared record, handed back as a tight current-state brief. |
| [`/ketchup`](./skills/ketchup/SKILL.md) | you want what changed in this chat since your last message, in plain words and small visuals, with every item waiting on you listed and decidable from the reply alone, even when that makes the reply long. |
| [`/ketchup-video`](./skills/ketchup-video/SKILL.md) | you want the `/ketchup` catch-up as a short subtitled video of slides, with the calls waiting on you as text under it. |
| [`/blast-radius`](./skills/blast-radius/SKILL.md) | you have a small-looking change and want to know what else it could break, with the one fact it's safe because of proven by running code, not asserted. |
| [`/architect`](./skills/architect/SKILL.md) | you're about to write code that crosses a function boundary and want the caller's usage, types, and module shape settled first. |
| [`/arena`](./skills/arena/SKILL.md) | you want N parallel attempts at the same thing, then to grab the best parts of each. |
| [`/swarm`](./skills/swarm/SKILL.md) | you want N parallel workers across different slices or races, then one aggregated report. |
| [`/interrogate`](./skills/interrogate/SKILL.md) | you have a diff and want different models to try to break it, keeping only findings a run proves. |
| [`/automate-me`](./skills/automate-me/SKILL.md) | you want your own `-mode` skill, drafted from how you've actually worked. |
| [`/make-bot-ui`](./skills/make-bot-ui/SKILL.md) | you want a page or dashboard whose buttons wake a Grok Bot over a webhook, including the sender-key handoff and Tailscale. |
| [`/setup-pstack`](./skills/setup-pstack/SKILL.md) | you want to pick which models pstack uses per role. detects your models and writes a config rule. |
| [`/reflect`](./skills/reflect/SKILL.md) | a long task landed and you want the recipe captured as a skill edit. |
| [`/correct`](./skills/correct/SKILL.md) | you keep correcting agents for the same mistakes. mines history for mistake classes, fixes each at the highest level that works (architecture, then types, lint, and ci, then tests, with docs last), and keeps a table pairing each rule with what enforces it. |
| [`/teach`](./skills/teach/SKILL.md) | you want to actually understand a change or subsystem, not just have it summarized. runs how + why and weaves one plain explanation, built up diagram by diagram. |
| [`/tdd`](./skills/tdd/SKILL.md) | you're fixing a bug and there's a cheap local test path. write the failing test first, then the fix. |
| [`/benchmark-checklist`](./skills/benchmark-checklist/SKILL.md) | you ran a benchmark or measured a speedup or regression. vets the number (limiter, tuning, errors, repeat runs, end-to-end relevance) before you report or act on it. |
| [`/no-comments`](./skills/no-comments/SKILL.md) | strip comments before review; spawns Comment Sicko, fixes accepted findings, offers encodings for claimed constraints. |
| [`/typescript-best-practices`](./skills/typescript-best-practices/SKILL.md) | you're reading or editing typescript. grounds the type-system-discipline principle in syntax. |
| [`/figure-it-out`](./skills/figure-it-out/SKILL.md) | no bundled playbook fits. designs a rigorous, auditable playbook for the task. |
| [`/show-me-your-work`](./skills/show-me-your-work/SKILL.md) | you want a reviewable decision trail. logs decisions to a tsv you can commit. |
| [`/create-verification-skill`](./skills/create-verification-skill/SKILL.md) | your project has no scripted way to prove app behavior. generates a project-local verify skill with a feature map, for any language or platform. |
| [`/maintain-verification-skill`](./skills/maintain-verification-skill/SKILL.md) | your verify skill's feature map has drifted from the app. source wave + one live pass, at most one PR of proven corrections. |
| [`/create-formal-verification-skill`](./skills/create-formal-verification-skill/SKILL.md) | tests can't reach the case that breaks a race, retry, state machine, parser, or unsafe code. verifies one property with the tool that fits and generates a project-local skill to recheck it on every change. |
| [`/maintain-formal-verification-skill`](./skills/maintain-formal-verification-skill/SKILL.md) | code your formal verification covers has changed since it was last checked. updates the model, harness, or properties to match the code, reruns, and says whether each failure is drift in the verification or a bug in the code. |
| [`/statechart`](./skills/statechart/SKILL.md) | someone who owns the behavior needs to see it, not read a spec. checks a tla+ model, draws what the user sees as a mermaid statechart, marks each state that breaks a rule, and gives the shortest path to each one. |
| [`/unslop`](./skills/unslop/SKILL.md) | you're cleaning up writing. removes AI tells. |
| [`/bro`](./skills/bro/SKILL.md) | you want the last message restated in plain human language, no jargon. |
| [`/technical-writing`](./skills/technical-writing/SKILL.md) | layered doc standard (Diátaxis + Google developer style + STE + Global English) for docs, RFCs, readmes, PR descriptions, commit messages. |

<!-- zh-CN:begin b6df0be793b937a7 -->

| 技能 | 使用时机 |
|---|---|
| [`/poteto-mode`](./skills/poteto-mode/SKILL.md) | 任何非简单任务的默认入口。 |
| [`/poteto-help`](./skills/poteto-help/SKILL.md) | 你初次使用 pstack，或不确定哪个技能、手册或原则合适。它先了解你想做什么，回答相关部分，再给你一段可输入的提示词。仅在输入 `/poteto-help` 时运行。 |
| [`/in-your-own-words`](./skills/in-your-own-words/SKILL.md) | 你希望智能体开始前复述你的目标和问题。仅在输入 `/in-your-own-words` 时运行。 |
| [`/sharpen`](./skills/sharpen/SKILL.md) | 发送之前，希望提示词更深入而非更庞大：顶尖专业人士会做哪些你没要求的工作，会以哪些原始材料为起点，采用哪些方法和工具，以及如何独立确认结果正确。它返回改写的提示词，保留你的选择空间，不执行任务。仅在输入 `/sharpen` 时运行。 |
| [`/how`](./skills/how/SKILL.md) | 你希望逐步了解一个子系统如何工作。 |
| [`/why`](./skills/why/SKILL.md) | 你想知道为什么这样构建。运行时发现可用 MCP，并行查询每类证据（源代码管理、问题跟踪、长篇文档、实时聊天、基础设施可观测性、错误跟踪、分析数据仓库）。 |
| [`/recall`](./skills/recall/SKILL.md) | 开始或恢复工作时，你希望根据自己的聊天历史和共享记录重建某主题的近期背景，并获得简洁的当前状态简报。 |
| [`/ketchup`](./skills/ketchup/SKILL.md) | 你想用通俗语言和小型图示了解本聊天自上次消息以来的变化，并列出所有等你决定的事项；即使回答因此变长，也要让你仅凭回复就能决定。 |
| [`/ketchup-video`](./skills/ketchup-video/SKILL.md) | 你希望将 `/ketchup` 的进展回顾做成简短的带字幕幻灯片视频，并在下方用文字列出待你决定的事项。 |
| [`/blast-radius`](./skills/blast-radius/SKILL.md) | 你有一个看似很小的改动，想知道它还可能破坏什么，并通过运行代码证明它安全所依赖的那项事实，而非口头断言。 |
| [`/architect`](./skills/architect/SKILL.md) | 你即将编写跨函数边界的代码，希望先确定调用方用法、类型和模块结构。 |
| [`/arena`](./skills/arena/SKILL.md) | 你希望对同一任务并行尝试 N 种方案，然后取各家之长。 |
| [`/swarm`](./skills/swarm/SKILL.md) | 你希望 N 个工作者并行处理不同切片或竞速任务，再汇总成一份报告。 |
| [`/interrogate`](./skills/interrogate/SKILL.md) | 你已有差异，希望不同模型尝试找出破绽，并只保留运行能够证明的问题。 |
| [`/automate-me`](./skills/automate-me/SKILL.md) | 你希望根据自己的实际工作方式起草专属 `-mode` 技能。 |
| [`/make-bot-ui`](./skills/make-bot-ui/SKILL.md) | 你希望制作页面或仪表板，其按钮通过 Webhook 唤醒 Grok Bot，并涵盖发送方密钥交接和 Tailscale。 |
| [`/setup-pstack`](./skills/setup-pstack/SKILL.md) | 你希望选择 pstack 各角色使用的模型。它会检测模型并写入配置规则。 |
| [`/reflect`](./skills/reflect/SKILL.md) | 长任务落地后，你想把做法记录为技能修改。 |
| [`/correct`](./skills/correct/SKILL.md) | 你总在纠正智能体同样的错误。它从历史中挖掘错误类别，在能够奏效的最高层修复每一类（先架构，再类型、lint 和 CI，然后测试，最后才是文档），并维护一张规则与执行保障机制的对应表。 |
| [`/teach`](./skills/teach/SKILL.md) | 你希望真正理解某个改动或子系统，而不只是获得摘要。它运行 how + why，以逐张图解递进的方式组织成通俗解释。 |
| [`/tdd`](./skills/tdd/SKILL.md) | 你正在修复缺陷，并有低成本本地测试路径。先写失败测试，再修复。 |
| [`/benchmark-checklist`](./skills/benchmark-checklist/SKILL.md) | 你运行了基准测试，或测得加速或回退。报告或据此行动前，检查数字是否可靠（限制因素、调优、错误、重复运行、端到端相关性）。 |
| [`/no-comments`](./skills/no-comments/SKILL.md) | 评审前清理注释；启动 Comment Sicko，修复已接受的问题，并为声称的约束提供代码表达方案。 |
| [`/typescript-best-practices`](./skills/typescript-best-practices/SKILL.md) | 你正在阅读或编辑 TypeScript。它用具体语法落实类型系统纪律原则。 |
| [`/figure-it-out`](./skills/figure-it-out/SKILL.md) | 没有内置操作手册合适。它为任务设计严谨、可审计的手册。 |
| [`/show-me-your-work`](./skills/show-me-your-work/SKILL.md) | 你希望获得可审阅的决策轨迹。它把决策记录到可提交的 TSV 文件。 |
| [`/create-verification-skill`](./skills/create-verification-skill/SKILL.md) | 项目没有脚本化证明应用行为的方法。它为任何语言或平台生成一个包含功能映射的项目本地验证技能。 |
| [`/maintain-verification-skill`](./skills/maintain-verification-skill/SKILL.md) | 验证技能的功能映射已偏离应用。先检查源码，再进行一次真实运行，最多提交一个只包含已证明更正的 PR。 |
| [`/create-formal-verification-skill`](./skills/create-formal-verification-skill/SKILL.md) | 测试无法触及会破坏竞争、重试、状态机、解析器或不安全代码的情况。它用合适的工具验证一个性质，并生成项目本地技能，以便每次改动时重新检查。 |
| [`/maintain-formal-verification-skill`](./skills/maintain-formal-verification-skill/SKILL.md) | 形式化验证覆盖的代码自上次检查后发生了变化。它更新模型、测试框架或性质以匹配代码，重新运行，并说明每次失败是验证发生偏移还是代码存在缺陷。 |
| [`/statechart`](./skills/statechart/SKILL.md) | 行为负责人需要直接看到行为，而非阅读规格。它检查 TLA+ 模型，用 Mermaid 状态图画出用户所见，标记每个违反规则的状态，并给出到达各状态的最短路径。 |
| [`/unslop`](./skills/unslop/SKILL.md) | 你在润色文字，希望去除 AI 痕迹。 |
| [`/bro`](./skills/bro/SKILL.md) | 你希望用没有术语的普通人语言重述上一条消息。 |
| [`/technical-writing`](./skills/technical-writing/SKILL.md) | 用于文档、RFC、自述文件、PR 描述和提交消息的分层文档标准（Diátaxis + Google 开发者风格 + STE + Global English）。 |

<!-- zh-CN:end b6df0be793b937a7 -->

</details>



### examples

<!-- zh-CN:begin aa8d64ec8fb340e1 -->

### 示例

<!-- zh-CN:end aa8d64ec8fb340e1 -->

mostly i type [`/poteto-mode`](./skills/poteto-mode/SKILL.md) at the start of a task and let it route to a playbook. the other skills fire as the steps need them. a few i reach for directly.

<!-- zh-CN:begin f1361ebe175bc13f -->

我通常在任务开始时输入 [`/poteto-mode`](./skills/poteto-mode/SKILL.md)，让它路由到相应行动手册。其他技能会在步骤需要时触发。少数技能我会直接使用。

<!-- zh-CN:end f1361ebe175bc13f -->


<details>
<summary>all the examples<!-- zh-CN:begin 4f5ae4af2b97df87 --><br>全部示例<!-- zh-CN:end 4f5ae4af2b97df87 --></summary>

```
bug fix:           /poteto-mode this pr has a subtle bug where the scroll drifts every 750ms even
                   when idle. repro first, then fix and verify.
perf:              /poteto-mode a big list takes a second or two to load even though we virtualize.
                   run a cpu trace and tell me why.
feature:           /poteto-mode build a small feature behind a feature flag. verify it really works.
prototype:         /poteto-mode build two prototypes of the markdown renderer so we can compare.
                   spawn an agent for each.
multi-phase:       /poteto-mode open source these skills as a plugin. nothing internal leaks, work
                   in a temp dir, show me the dependency graph first.
overnight run:     /poteto-mode i'm going to bed. land the stack even if ci flakes. i want
                   everything merged by morning.
babysit:           /poteto-mode check on pr 123. anything outstanding?
visual parity:     /poteto-mode the row spacing is too tall when this flag is on. the second image
                   is correct. repro and fix until it matches.
figure it out:     /poteto-mode i'm stepping away. migrate every caller from the synchronous store
                   to the new async one, keeping behavior identical. i want to trust it was done
                   right when i'm back.
how:               /how do we cancel runs? do we have an n+1 when we look up every run to cancel?
why:               /why is this feature flag not on yet?
architect:         design this instrumentation to be high signal with no false positives. /architect
                   this first.
arena:             /arena take my prompt to the arena verbatim. i want to compare their proposals
                   with yours.
swarm:             /swarm check every package under packages/ against its check.sh. one worker per
                   package. one report.
interrogate:       /interrogate review this pr.
tdd:               /tdd implement
unslop:            can we unslop and tighten the new changes?
reflect:           /reflect that took too long. capture what we learned so the next run doesn't
                   repeat it.
correct:           /correct
show-me-your-work: /show-me-your-work keep a decision trail i can review when i'm back.
automate-me:       /automate-me
help:              /poteto-help which skill should i use to review this branch?
```

<!-- zh-CN:begin d4d17027c5cc2187 -->

```
缺陷修复：           /poteto-mode 这个 PR 有一个隐蔽缺陷：即使空闲时，滚动每 750ms 也会漂移。
                   先复现，再修复并验证。
性能：              /poteto-mode 大列表尽管已虚拟化，仍要一两秒才能加载。
                   运行 CPU 跟踪并告诉我原因。
功能：              /poteto-mode 在功能开关后构建一个小功能。验证它确实有效。
原型：              /poteto-mode 为 Markdown 渲染器构建两个原型，以便比较。
                   每个原型各生一个代理。
多阶段：            /poteto-mode 将这些技能作为插件开源。不要泄露任何内部内容，在临时目录中工作，
                   先给我看依赖图。
夜间运行：          /poteto-mode 我要睡觉了。即使 CI 偶发失败也要落地整叠变更。我希望
                   早上全部合并。
看护：              /poteto-mode 检查 PR 123。还有什么未完成？
视觉一致性：        /poteto-mode 开启这个开关时行距太高。第二张图片是正确的。
                   复现并修复直到匹配。
自行解决：          /poteto-mode 我要离开。把每位调用者从同步存储
                   迁移到新的异步存储，保持行为完全一致。我希望回来时
                   能信任它已正确完成。
如何：              /how 我们如何取消运行？查找每次运行以取消时是否存在 n+1？
为何：              /why 这个功能开关为什么还没开启？
架构：              设计此埋点，使其信噪比高且无误报。先执行 /architect。
竞技场：            /arena 将我的提示词原样送到竞技场。我想把他们的方案
                   与你的方案进行比较。
蜂群：              /swarm 对照 packages/ 下每个包的 check.sh 检查。每个包一个工作者。
                   一份报告。
质询：              /interrogate 审查此 PR。
tdd：               /tdd implement
去冗余：            能否对新增改动去冗余并收紧？
反思：              /reflect 这花了太久。记录我们学到的内容，避免下次运行
                   重复。
纠正：              /correct
展示工作：          /show-me-your-work 保留决策轨迹，供我回来时审查。
自动化我：          /automate-me
帮助：              /poteto-help 我应该用哪项技能审查这个分支？
```

<!-- zh-CN:end d4d17027c5cc2187 -->

</details>

## the `poteto-agent` and Comment Sicko subagents

<!-- zh-CN:begin 8146fc7c6f46b778 -->

## `poteto-agent` 与 Comment Sicko 子代理

<!-- zh-CN:end 8146fc7c6f46b778 -->

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) runs in the chat that receives it. that chat owns the playbook, the todo list, and every subagent spawn.

<!-- zh-CN:begin e1ab818c0386abca -->

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) 在接收它的聊天中运行。该聊天负责行动手册、待办列表以及每次子代理生成。

<!-- zh-CN:end e1ab818c0386abca -->

pstack also ships [`subagent_type: "poteto-agent"`](./agents/poteto-agent.md) as the wrapper for delegates spawned during a run. it reads `poteto-mode` in full, including its inline principles index, before doing any work. substituting `generalPurpose` skips that read and drifts. do not spawn `poteto-agent` to run the playbook itself.

<!-- zh-CN:begin bbad27aab106bc16 -->

pstack 还提供 [`subagent_type: "poteto-agent"`](./agents/poteto-agent.md)，作为运行期间生成的代表代理的包装器。它会在做任何工作前完整阅读 `poteto-mode`，包括其内联原则索引。替换成 `generalPurpose` 会跳过该阅读并产生漂移。不要生成 `poteto-agent` 来运行行动手册本身。

<!-- zh-CN:end bbad27aab106bc16 -->

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) and [`subagent_type: "poteto-agent"`](./agents/poteto-agent.md) route through the same wrapper.

<!-- zh-CN:begin c443143d6cbcec2b -->

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) 和 [`subagent_type: "poteto-agent"`](./agents/poteto-agent.md) 通过同一包装器路由。

<!-- zh-CN:end c443143d6cbcec2b -->

pstack also ships [Comment Sicko](./agents/comment-sicko.md), a read-only comment reviewer available as `subagent_type: "comment-sicko"`. usually invoke it through [`/no-comments`](./skills/no-comments/SKILL.md), not directly.

<!-- zh-CN:begin 7f4c32a2152fe8ab -->

pstack 还提供 [Comment Sicko](./agents/comment-sicko.md)，一个只读评论审查者，可通过 `subagent_type: "comment-sicko"` 使用。通常通过 [`/no-comments`](./skills/no-comments/SKILL.md) 调用，而非直接调用。

<!-- zh-CN:end 7f4c32a2152fe8ab -->

## principles

<!-- zh-CN:begin 4cdc12617db968e2 -->

## 原则

<!-- zh-CN:end 4cdc12617db968e2 -->

twenty-four short skills, one principle each. `poteto-mode` indexes them inline and reads that index at task start. the standalone files are there so other skills can reference a principle by name, and so the index can point at the full rule for each.

<!-- zh-CN:begin f4c20d77aa725d9b -->

二十四个简短技能，每个一个原则。`poteto-mode` 内联索引它们，并在任务开始时读取该索引。独立文件存在，是为了其他技能能按名称引用原则，并使索引能指向每项原则的完整规则。

<!-- zh-CN:end f4c20d77aa725d9b -->

<details>
<summary>all twenty-four principles<!-- zh-CN:begin 51cac07ecbdeb15d --><br>全部二十四项原则<!-- zh-CN:end 51cac07ecbdeb15d --></summary>

| principle | group | rule |
|---|---|---|
| [laziness-protocol](./skills/principle-laziness-protocol/SKILL.md) | core | Bias toward deletion and the smallest change that solves the problem. |
| [foundational-thinking](./skills/principle-foundational-thinking/SKILL.md) | core | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious. |
| [redesign-from-first-principles](./skills/principle-redesign-from-first-principles/SKILL.md) | core | Redesign as if the requirement had been a foundational assumption from day one, instead of bolting it on. |
| [attack-the-premise](./skills/principle-attack-the-premise/SKILL.md) | core | Apply when two or more fixes that share one premise have failed the same gate. Write the premise down and test it directly before you write another fix that assumes it. |
| [subtract-before-you-add](./skills/principle-subtract-before-you-add/SKILL.md) | core | Remove dead weight, redundant validators, and stub references first, then build on the simpler base. |
| [minimize-reader-load](./skills/principle-minimize-reader-load/SKILL.md) | core | Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope. |
| [outcome-oriented-execution](./skills/principle-outcome-oriented-execution/SKILL.md) | core | Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code. |
| [experience-first](./skills/principle-experience-first/SKILL.md) | core | Choose user delight over implementation convenience; ship fewer polished features over more rough ones. |
| [exhaust-the-design-space](./skills/principle-exhaust-the-design-space/SKILL.md) | core | Build 2-3 competing prototypes and compare side by side before committing. |
| [build-the-lever](./skills/principle-build-the-lever/SKILL.md) | core | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The tool is the artifact a reviewer can rerun. |
| [model-the-domain](./skills/principle-model-the-domain/SKILL.md) | architecture | Encode the domain in a structure instead of scattered conditionals. |
| [boundary-discipline](./skills/principle-boundary-discipline/SKILL.md) | architecture | Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions. |
| [type-system-discipline](./skills/principle-type-system-discipline/SKILL.md) | architecture | Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, exhaust variants, derive from authoritative schemas. |
| [make-operations-idempotent](./skills/principle-make-operations-idempotent/SKILL.md) | architecture | Converge to the same end state regardless of partial prior runs. |
| [migrate-callers-then-delete-legacy-apis](./skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | architecture | Migrate callers and delete the old API in the same wave instead of preserving compatibility layers. |
| [separate-before-serializing-shared-state](./skills/principle-separate-before-serializing-shared-state/SKILL.md) | architecture | Eliminate the sharing first; serialize structurally only when one shared writer is a real invariant. |
| [prove-it-works](./skills/principle-prove-it-works/SKILL.md) | verification | Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.'. |
| [fix-root-causes](./skills/principle-fix-root-causes/SKILL.md) | verification | Trace each symptom back to the first place the system went wrong and fix it there. A guard is a fix only when the state it handles is legitimate. |
| [sequence-verifiable-units](./skills/principle-sequence-verifiable-units/SKILL.md) | verification | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer. |
| [test-behavior-not-implementation](./skills/principle-test-behavior-not-implementation/SKILL.md) | verification | Apply when you write, change, or keep a test. Assert what the code's users can observe, so the test fails when that behavior breaks and keeps passing when only the internals change. |
| [explain-the-number](./skills/principle-explain-the-number/SKILL.md) | verification | Apply before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it, and rule out that it measured something other than the work you think. |
| [guard-the-context-window](./skills/principle-guard-the-context-window/SKILL.md) | delegation | Route bulk to subagents; keep summaries in the main thread, not raw payloads. |
| [never-block-on-the-human](./skills/principle-never-block-on-the-human/SKILL.md) | delegation | Proceed, present the result, let the human course-correct after the fact; reserve confirmation for irreversible actions. |
| [encode-lessons-in-structure](./skills/principle-encode-lessons-in-structure/SKILL.md) | meta | Encode the rule as a lint, metadata flag, runtime check, or script instead of more text. |

<!-- zh-CN:begin 4d7fe3b628ebe6ec -->

| 原则 | 组别 | 规则 |
|---|---|---|
| [懒惰协议](./skills/principle-laziness-protocol/SKILL.md) | 核心 | 倾向于删除，以及能解决问题的最小改动。 |
| [基础思考](./skills/principle-foundational-thinking/SKILL.md) | 核心 | 编写逻辑前应用：选择核心类型和数据结构，安排脚手架与功能工作的顺序，询问并行参与者共享什么。把数据结构做对，使下游代码变得显而易见。 |
| [从第一原理重新设计](./skills/principle-redesign-from-first-principles/SKILL.md) | 核心 | 把需求视为第一天就存在的基础假设来重新设计，而不是事后硬加。 |
| [攻击前提](./skills/principle-attack-the-premise/SKILL.md) | 核心 | 两个或更多共享同一前提的修复在同一门槛失败时应用。写下前提并直接测试，再编写另一个假定该前提的修复。 |
| [先减后加](./skills/principle-subtract-before-you-add/SKILL.md) | 核心 | 先移除无用负担、冗余验证器和桩引用，再在更简单的基础上构建。 |
| [降低读者负担](./skills/principle-minimize-reader-load/SKILL.md) | 核心 | 计算问题与答案之间的层级，以及读者脑中的隐藏状态；合并只有单个调用者的包装器，缩小可变作用域。 |
| [结果导向执行](./skills/principle-outcome-oriented-execution/SKILL.md) | 核心 | 在具有明确阶段边界的计划重写和迁移中使用。向目标架构收敛；不要用一次性兼容代码保留平滑的中间状态。 |
| [体验优先](./skills/principle-experience-first/SKILL.md) | 核心 | 选择用户愉悦而非实现便利；发布少量精致功能而非更多粗糙功能。 |
| [穷尽设计空间](./skills/principle-exhaust-the-design-space/SKILL.md) | 核心 | 提交前构建 2-3 个竞争原型并排比较。 |
| [构建省力工具](./skills/principle-build-the-lever/SKILL.md) | 核心 | 适用于任何非简单工作，不只是批量工作：编辑、迁移、分析、检查。构建完成或证明工作的工具（codemod、脚本、生成器，或子代理遵循的技能），而非手工工作。工具是审查者可重跑的制品。 |
| [领域建模](./skills/principle-model-the-domain/SKILL.md) | 架构 | 用结构表达领域，而非分散条件语句。 |
| [边界纪律](./skills/principle-boundary-discipline/SKILL.md) | 架构 | 将守卫集中在系统边界（CLI、配置、网络、外部 API）；信任内部类型，并将业务逻辑留在纯函数中。 |
| [类型系统纪律](./skills/principle-type-system-discipline/SKILL.md) | 架构 | 让非法状态无法表示，标记语义原语，在边界解析外部数据，穷尽变体，从权威 schema 派生。 |
| [使操作幂等](./skills/principle-make-operations-idempotent/SKILL.md) | 架构 | 无论此前是否部分运行，都收敛到相同最终状态。 |
| [先迁移调用者再删除旧 API](./skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | 架构 | 在同一波次迁移调用者并删除旧 API，而非保留兼容层。 |
| [序列化共享状态前先分离](./skills/principle-separate-before-serializing-shared-state/SKILL.md) | 架构 | 先消除共享；只有单一共享写入者是真实不变量时，才从结构上串行化。 |
| [证明它有效](./skills/principle-prove-it-works/SKILL.md) | 验证 | 完成任务后、宣布完成前应用。验证真实制品（运行功能、读取实际值、检查差异），而非代用信号、自我报告或“它能编译”。 |
| [修复根因](./skills/principle-fix-root-causes/SKILL.md) | 验证 | 将每个症状追溯到系统首次出错之处，并在那里修复。只有处理的状态合法时，守卫才是修复。 |
| [排列可验证单元](./skills/principle-sequence-verifiable-units/SKILL.md) | 验证 | 适用于多步骤工作（扫描、迁移、连续类似编辑），以及堆叠提交与 PR 的方式。将工作拆成各自以可验证状态结束的小单元，在下一单元前检查每个单元，并安排交付顺序，使序列向审查者证明自身。 |
| [测试行为而非实现](./skills/principle-test-behavior-not-implementation/SKILL.md) | 验证 | 在编写、修改或保留测试时应用。断言代码用户可观察到的内容，使该行为破坏时测试失败，而仅内部变化时仍通过。 |
| [解释数字](./skills/principle-explain-the-number/SKILL.md) | 验证 | 在信任、报告或依据测量数字行动前应用：加速、回归、吞吐量、延迟或评估结果。找出限制因素，排除它测量了你以为之外内容的可能。 |
| [守护上下文窗口](./skills/principle-guard-the-context-window/SKILL.md) | 委派 | 将批量工作路由到子代理；主线程保留摘要，而不是原始载荷。 |
| [绝不阻塞在人类身上](./skills/principle-never-block-on-the-human/SKILL.md) | 委派 | 继续执行并展示结果，让人类事后纠正；只为不可逆操作保留确认。 |
| [将经验编码进结构](./skills/principle-encode-lessons-in-structure/SKILL.md) | 元 | 将规则编码为 lint、元数据标志、运行时检查或脚本，而非更多文本。 |

<!-- zh-CN:end 4d7fe3b628ebe6ec -->

</details>

## not shipped here

<!-- zh-CN:begin 72c112a3f81c96c7 -->

## 此处未随附

<!-- zh-CN:end 72c112a3f81c96c7 -->

a few things `poteto-mode` references but doesn't bundle:

<!-- zh-CN:begin 2201f17d5c2c91dc -->

`poteto-mode` 引用但未随包提供的一些内容：

<!-- zh-CN:end 2201f17d5c2c91dc -->

- `/deslop` and the `deslop` skill ship in the `cursor-team-kit` plugin.

<!-- zh-CN:begin df820bf48a966883 -->

- `/deslop` 和 `deslop` 技能随 `cursor-team-kit` 插件提供。

<!-- zh-CN:end df820bf48a966883 -->
- `control-cli` (for CLIs and TUIs) and `control-ui` (for browser, Electron, web) ship in `cursor-team-kit` too.

<!-- zh-CN:begin 60da8230d8926fdb -->

- `control-cli`（用于 CLI 和 TUI）及 `control-ui`（用于浏览器、Electron、Web）也随 `cursor-team-kit` 提供。

<!-- zh-CN:end 60da8230d8926fdb -->
- `/create-skill` is a cursor built-in. cursor also ships a built-in `/autopilot` that watches a pr. inside `poteto-mode`, pr-status requests go to the [babysit playbook](./skills/poteto-mode/playbooks/babysit.md) instead.

<!-- zh-CN:begin 26e4fb6a2084827d -->

- `/create-skill` 是 Cursor 内置功能。Cursor 还提供内置 `/autopilot` 来监视 PR。在 `poteto-mode` 内，PR 状态请求改为进入[看护行动手册](./skills/poteto-mode/playbooks/babysit.md)。

<!-- zh-CN:end 26e4fb6a2084827d -->

install `cursor-team-kit` alongside pstack if you want the full set.

<!-- zh-CN:begin 837f1871d401514f -->

若要获得完整集合，请同时安装 `cursor-team-kit` 与 pstack。

<!-- zh-CN:end 837f1871d401514f -->

## why are there no planning skills?

<!-- zh-CN:begin 85c57e9da728d10d -->

## 为什么没有规划技能？

<!-- zh-CN:end 85c57e9da728d10d -->

cursor already has a great plan mode which works great with pstack. but personally, i don't believe in planning. the best spec is code. if you do want to make a plan, [`/poteto-mode`](./skills/poteto-mode/SKILL.md) covers it, but it's not a default. 

<!-- zh-CN:begin 91d72bc7319829e2 -->

Cursor 已有出色的计划模式，与 pstack 配合得很好。但个人而言，我不相信规划。最好的规范就是代码。若你确实要制定计划，[`/poteto-mode`](./skills/poteto-mode/SKILL.md) 可以覆盖，但它不是默认流程。

<!-- zh-CN:end 91d72bc7319829e2 -->

## make it yours

<!-- zh-CN:begin 996be3d438053270 -->

## 按你的方式使用

<!-- zh-CN:end 996be3d438053270 -->

`poteto-mode` is my style. you may not want exactly that.

<!-- zh-CN:begin f1775d56a0092c5c -->

`poteto-mode` 是我的风格。你可能不想要完全相同的做法。

<!-- zh-CN:end f1775d56a0092c5c -->

type [`/automate-me`](./skills/automate-me/SKILL.md). it mines your recent transcripts, drafts a `<your-name>-mode` skill from how you've actually worked, and routes through pstack underneath. you keep pstack as the base and end up with your own routing skill alongside `poteto-mode`.

<!-- zh-CN:begin 75c1ad28130f7500 -->

输入 [`/automate-me`](./skills/automate-me/SKILL.md)。它会挖掘你最近的记录，根据你实际工作方式起草 `<your-name>-mode` 技能，并在底层通过 pstack 路由。你保留 pstack 作为基础，同时在 `poteto-mode` 旁得到自己的路由技能。

<!-- zh-CN:end 75c1ad28130f7500 -->

models are configurable too. type [`/setup-pstack`](./skills/setup-pstack/SKILL.md). it detects the models you have access to and writes a small always-applied rule mapping each role (code, judgment, the review panels) to a model. every skill reads it and falls back to sensible defaults when the rule is absent, so you override only what you want.

<!-- zh-CN:begin 1c2cad9cd4a23b8b -->

模型也可配置。输入 [`/setup-pstack`](./skills/setup-pstack/SKILL.md)。它会检测你可访问的模型，并写入一条始终应用的小规则，将每个角色（代码、判断、审查小组）映射到模型。每项技能都会读取它；规则缺失时回退到合理默认值，因此只覆盖你想改变的部分。

<!-- zh-CN:end 1c2cad9cd4a23b8b -->

when a default changes, a rule written before the change still pins the old default. delete those role lines, or delete the file, then run `/setup-pstack` again. a rerun keeps any role whose model differs from the default.

<!-- zh-CN:begin d89e8d960dc7156d -->

默认值变化时，早于该变化写下的规则仍固定旧默认值。删除这些角色行或删除文件，再运行 `/setup-pstack`。重跑会保留任何模型与默认值不同的角色。

<!-- zh-CN:end d89e8d960dc7156d -->

## automations

<!-- zh-CN:begin 710709ccca7d9be0 -->

## 自动化

<!-- zh-CN:end 710709ccca7d9be0 -->

pstack also ships a dormant [benny automation pack](./automations/benny/). benny triages slack issue reports, then reproduces and fixes confirmed bugs with real ui evidence. its files are not registered as slash skills.

<!-- zh-CN:begin 4aaba314a891de2d -->

pstack 还随附一个休眠的 [benny 自动化包](./automations/benny/)。benny 分诊 Slack 问题报告，然后用真实 UI 证据复现并修复确认的缺陷。其文件未注册为斜杠技能。

<!-- zh-CN:end 4aaba314a891de2d -->

to set it up, point cursor at [`FOR_AGENTS.md`](./automations/benny/FOR_AGENTS.md). setup copies the pack into the target repository at `.cursor/automations/benny/`, enables pstack there for shared skills, and keeps user configuration outside the copied pack. benny runs on cursor automations, so it is cursor-only.

<!-- zh-CN:begin c777daf0616cdf16 -->

要设置它，将 Cursor 指向 [`FOR_AGENTS.md`](./automations/benny/FOR_AGENTS.md)。设置会把该包复制到目标仓库的 `.cursor/automations/benny/`，在那里为共享技能启用 pstack，并将用户配置保留在复制的包之外。benny 运行在 Cursor automations 上，因此仅支持 Cursor。

<!-- zh-CN:end c777daf0616cdf16 -->

## license

<!-- zh-CN:begin c51369c9e1aa2c0e -->

## 许可证

<!-- zh-CN:end c51369c9e1aa2c0e -->

MIT

<!-- zh-CN:begin 337a48b729c8715e -->

MIT（麻省理工学院许可证）

<!-- zh-CN:end 337a48b729c8715e -->
