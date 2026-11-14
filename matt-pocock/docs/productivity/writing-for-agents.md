## What it does

<!-- zh-CN:begin 3f980c46bc5fb98a -->

## 它的作用

<!-- zh-CN:end 3f980c46bc5fb98a -->

`writing-for-agents` is the reference for writing agent-facing documents: a skill, an `AGENTS.md` or `CLAUDE.md`, a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), a runtime prompt, a README, any doc an [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reads. The format differs, but the writing does not. The same levers make each one predictable, so the agent follows the same *process* on every run (not necessarily to the same output).

<!-- zh-CN:begin 576da47ebba144e7 -->

`writing-for-agents` 是面向代理文档的编写参考：技能、`AGENTS.md` 或 `CLAUDE.md`、[规格](https://www.aihero.dev/ai-coding-dictionary/spec)、运行时提示词、README，以及[代理](https://www.aihero.dev/ai-coding-dictionary/agent)读取的任何文档。格式不同，写法相同。相同杠杆让每类文档可预测，使代理每次运行遵循相同*过程*（输出不必相同）。

<!-- zh-CN:end 576da47ebba144e7 -->

Its default fix is to delete, not to explain. Ask an agent to write instructions for another agent and it spends most of its words explaining what the [model](https://www.aihero.dev/ai-coding-dictionary/model) already knows. Each of those lines is a **no-op**: it costs [context](https://www.aihero.dev/ai-coding-dictionary/context) and changes no behaviour. This reference helps you find them, so it is as useful on a document you already have as on a blank file.

<!-- zh-CN:begin 8733477d3e9c96d2 -->

默认修法是删除，不是解释。让代理为另一个代理写指令，它大部分文字会解释[模型](https://www.aihero.dev/ai-coding-dictionary/model)已知内容。这些行都是**无效项**：消耗[上下文](https://www.aihero.dev/ai-coding-dictionary/context)，却不改变行为。本参考帮助找出它们，因此对现有文档和空白文件同样有用。

<!-- zh-CN:end 8733477d3e9c96d2 -->

It was called `writing-great-skills` until v1.1. The new name fits what it always was. Almost none of it is specific to skills. The skill-only mechanics (frontmatter, the model- versus user-invoked choice, router skills) live in a linked `SKILL-MECHANICS.md` that you read only when the document in front of you is a skill.

<!-- zh-CN:begin 1aef8c5db84bf3b9 -->

v1.1 前它叫 `writing-great-skills`。新名称符合其本质：几乎没有内容只适用于技能。仅与技能有关的机制（frontmatter、模型调用 versus 用户调用、路由技能）位于链接的 `SKILL-MECHANICS.md`，仅当眼前文档是技能时阅读。

<!-- zh-CN:end 1aef8c5db84bf3b9 -->

## When to reach for it

<!-- zh-CN:begin 3431dc469dd59c31 -->

## 何时使用

<!-- zh-CN:end 3431dc469dd59c31 -->

Type `/writing-for-agents`, or the agent reaches for it on its own when you're creating or editing a skill, or modifying `AGENTS.md` or `CLAUDE.md`.

<!-- zh-CN:begin 488478cba50003ac -->

输入 `/writing-for-agents`；创建或编辑技能，或修改 `AGENTS.md`、`CLAUDE.md` 时，代理会自行使用。

<!-- zh-CN:end 488478cba50003ac -->

Reach for it by hand for everything else an agent reads: your docs, specs and [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket), system and [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) prompts. The test is one question: does an agent read this? It does not matter how the agent gets the document: a pointer names it, a human pastes it, or it is in the repo. To find out what a codebase contains, use [grill-with-docs](https://aihero.dev/skills-grill-with-docs). This reference controls how a document reads, not what it knows.

<!-- zh-CN:begin 39e08a9028d42cf8 -->

代理读取的其他内容应手动使用它：文档、规格和[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)、系统提示词与 [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) 提示词。判断只需一问：代理会读它吗？代理如何获得文档不重要：指针点名、人类粘贴或仓库内存在均可。要了解代码库内容，使用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。本参考控制文档如何表达，不控制它知道什么。

<!-- zh-CN:end 39e08a9028d42cf8 -->

## The two loads

<!-- zh-CN:begin b750160e6eeb3640 -->

## 两种负载

<!-- zh-CN:end b750160e6eeb3640 -->

The central idea is two budgets that every document and pointer spends:

<!-- zh-CN:begin 362ef13c381e3cff -->

核心思想是每份文档和指针都会支出两项预算：

<!-- zh-CN:end 362ef13c381e3cff -->

- **Context load**: the cost of always-loaded material on the agent's window: an `AGENTS.md` line, a skill description, anything sitting in context every [turn](https://www.aihero.dev/ai-coding-dictionary/turn) whether or not it fires.

<!-- zh-CN:begin 96eff99a55330140 -->

- **上下文负载**：常驻材料占用代理窗口的成本：`AGENTS.md` 一行、技能描述，以及每个[轮次](https://www.aihero.dev/ai-coding-dictionary/turn)无论是否触发都留在上下文中的内容。

<!-- zh-CN:end 96eff99a55330140 -->
- **Cognitive load**: the cost to you of remembering which documents exist and when to reach for each. You are the index. Do not try to minimise this cost, because it is the price of human agency.

<!-- zh-CN:begin 4af8ca7c0f652add -->

- **认知负载**：你记住有哪些文档、何时使用各自的成本。你就是索引。不要试图最小化这项成本，它是人类自主性的代价。

<!-- zh-CN:end 4af8ca7c0f652add -->

Once you think in these two loads, most authoring decisions (split or don't, inline or disclose, point or push) become the same trade made in different places.

<!-- zh-CN:begin 9df288d9882e1b07 -->

用这两项负载思考后，大多数编写决定（拆分与否、内联还是披露、指向还是推送）都是不同位置上的同一取舍。

<!-- zh-CN:end 9df288d9882e1b07 -->

## The levers

<!-- zh-CN:begin 6ab431489d9ab978 -->

## 杠杆

<!-- zh-CN:end 6ab431489d9ab978 -->

- **[Context pointers](https://www.aihero.dev/ai-coding-dictionary/context-pointer)**: the reference held in context that names out-of-context material and encodes when to reach it. A skill description and an `AGENTS.md` line naming a doc are the same thing. The pointer's *wording*, not its target, decides how reliably the agent follows it.

<!-- zh-CN:begin 3961dfd3b3e446d1 -->

- **[上下文指针](https://www.aihero.dev/ai-coding-dictionary/context-pointer)**：上下文内保存的引用，点名上下文外材料并编码何时使用。技能描述与 `AGENTS.md` 中指向文档的一行是同类东西。决定代理可靠遵循的不是指针目标，而是*措辞*。

<!-- zh-CN:end 3961dfd3b3e446d1 -->
- **Information hierarchy**: the ladder from in-file step, to in-file reference, to disclosed reference behind a pointer. **[Progressive disclosure](https://www.aihero.dev/ai-coding-dictionary/progressive-disclosure)** is moving material down that ladder so the top stays easy to read.

<!-- zh-CN:begin 556432aec5170b08 -->

- **信息层级**：从文件内步骤，到文件内参考，再到指针后的披露参考。**[渐进披露](https://www.aihero.dev/ai-coding-dictionary/progressive-disclosure)** 是把材料沿层级下移，让顶层保持易懂。

<!-- zh-CN:end 556432aec5170b08 -->
- **Completion criteria**: how clear and demanding each step's done-condition is, and the **legwork** that demand causes. They are the defence against **premature completion**.

<!-- zh-CN:begin 7a73dc725242d0cc -->

- **完成标准**：每一步完成条件有多清楚、严格，以及这要求造成多少**跑腿工作**。它们用于防范**过早完成**。

<!-- zh-CN:end 7a73dc725242d0cc -->
- **Leading words**: a compact concept already in the model's pretraining (*tight*, *red*, *tracer bullet*) that the agent thinks with while running the document. It works in two places. In the body it guides execution, and in the pointer it triggers invocation.

<!-- zh-CN:begin 6760a5afc4cf5c69 -->

- **引导词**：模型预训练中已有的紧凑概念（*tight*、*red*、*tracer bullet*），代理运行文档时以它思考。它有两处作用：正文中指导执行，指针中触发调用。

<!-- zh-CN:end 6760a5afc4cf5c69 -->
- **Pruning**: single source of truth, relevance, and the no-op test applied sentence by sentence, against **duplication**, **sediment** and **sprawl**.

<!-- zh-CN:begin 904bff313470b09c -->

- **修剪**：逐句应用单一事实来源、相关性和无效项测试，处理**重复**、**沉积**与**蔓延**。

<!-- zh-CN:end 904bff313470b09c -->

## Common questions

<!-- zh-CN:begin 4450929e0ce4c241 -->

## 常见问题

<!-- zh-CN:end 4450929e0ce4c241 -->

**Where did `/writing-great-skills` go?**
It is this skill, renamed in v1.1. Users pointed it at `AGENTS.md`, docs, specs, tickets and runtime prompts long before the rename. Structure, leading words and pruning apply to any text an agent reads. There is no alias. Reinstall under the new name.

<!-- zh-CN:begin ac8a537ac44d3315 -->

**`/writing-great-skills` 去哪了？**
就是本技能，v1.1 更名。更名前用户早已用它处理 `AGENTS.md`、文档、规格、工单和运行时提示词。结构、引导词和修剪适用于代理读取的任何文本。没有别名，请按新名称重装。

<!-- zh-CN:end ac8a537ac44d3315 -->

**"Writing for agents": so the agent does the writing?**
The other way round. You are the author; the agent is the reader. That is what makes it hard. You write for a reader that has already read everything, so explanation is waste and precision is the whole job.

<!-- zh-CN:begin 39b233dd196520a9 -->

**“为代理写作”：代理负责写吗？**
反过来。作者是你，读者是代理，因此才困难。你面向已读过一切的读者写作，解释是浪费，精确才是工作核心。

<!-- zh-CN:end 39b233dd196520a9 -->

**Can't I just ask the agent to write it for me?**
You can, and it will produce something verbose. Left alone the model explains what it already knows, and it will not apply the no-op test or reach for a leading word on its own. Use the reference to review the draft. Most of its value comes from that review pass.

<!-- zh-CN:begin d334248351424c06 -->

**不能直接让代理替我写吗？**
可以，但结果冗长。模型会解释已知内容，也不会自行应用无效项测试或想到引导词。用本参考审阅草稿，大多数价值来自这次审阅。

<!-- zh-CN:end d334248351424c06 -->

**I asked an agent to trim a document and it cut the functionality.**
Agents told to "streamline" optimise for length, because length is the thing they can see. The no-op test checks behaviour, not style: delete the line and ask whether the agent's behaviour changed. When a sentence fails, delete the whole sentence rather than trim words from it, and settle a disagreement about it by running the document, not by arguing.

<!-- zh-CN:begin ee7125787e0e06ee -->

**我让代理精简文档，它删掉了功能。**
被告知“精简”的代理会优化长度，因为长度看得见。无效项测试检查行为而非风格：删除该行，看代理行为是否变化。某句无效时，删除整句，不要只删词；分歧通过运行文档解决，而不是争论。

<!-- zh-CN:end ee7125787e0e06ee -->

**How do I know when it's done?**
When it works, and you can no longer find duplication, sediment or no-ops. There is no automated eval. You check by running the document by hand and using the failure-mode vocabulary to diagnose problems. When a document misbehaves, the same vocabulary helps you fix it: name the failure mode first, then fix that.

<!-- zh-CN:begin df93ad47fc5781c4 -->

**怎么知道完成了？**
当它有效，且再也找不到重复、沉积或无效项。没有自动 eval。你手工运行文档，并用失败模式词汇诊断。文档行为异常时，同一词汇帮助修复：先命名失败模式，再修它。

<!-- zh-CN:end df93ad47fc5781c4 -->

**Should this live in `CLAUDE.md` or somewhere else?**
Ask which load you want to pay. `CLAUDE.md` loads into every [session](https://www.aihero.dev/ai-coding-dictionary/session) unconditionally. Material behind a pointer costs only the pointer's own line until it fires. Anything that applies in one session out of ten costs context load in the other nine.

<!-- zh-CN:begin 392fdb9db468222b -->

**应放在 `CLAUDE.md` 还是别处？**
问你要支付哪种负载。`CLAUDE.md` 无条件加载到每个[会话](https://www.aihero.dev/ai-coding-dictionary/session)。指针后的材料在触发前只花指针自身一行。十个会话只用一次的内容，其余九个也要支付上下文负载。

<!-- zh-CN:end 392fdb9db468222b -->

**Do I need to rewrite my documents for each new model?**
Mostly no, and over-fitting to one model causes its own problems. Updating for a new model is usually another no-op pass rather than a rewrite.

<!-- zh-CN:begin ceb75e554ae46588 -->

**每个新模型都需要重写文档吗？**
大多不用，过度适配一个模型也有问题。更新新模型通常只是再做一轮无效项清理，而非重写。

<!-- zh-CN:end ceb75e554ae46588 -->

**My skill only works on the exact task I built it from.**
The common method (do the work once, then have the agent write it up as a skill) fits that one run too closely, and the examples come out too specific. Keep the run as evidence, then generalise on purpose: strip what belonged to that repo and those files, and write for the class of task.

<!-- zh-CN:begin 34fc3fe1a5e77c36 -->

**我的技能只适用于当初构建它的确切任务。**
常见方法（做一次工作，再让代理写成技能）过度贴合那一次运行，示例也过于具体。保留运行作为证据，再有意识地泛化：去掉属于该仓库和文件的内容，面向一类任务写作。

<!-- zh-CN:end 34fc3fe1a5e77c36 -->

**English isn't my first language. Do I lose the leading-word advantage?**
No. Finding the word that packs the most behaviour into the fewest [tokens](https://www.aihero.dev/ai-coding-dictionary/token) is work the reference does for you.

<!-- zh-CN:begin c4ee939995b358ce -->

**英语不是我的母语，会失去引导词优势吗？**
不会。找到用最少[词元](https://www.aihero.dev/ai-coding-dictionary/token)承载最多行为的词，正是本参考替你完成的工作。

<!-- zh-CN:end c4ee939995b358ce -->

## It's working if

<!-- zh-CN:begin 2d3c3f286e55024c -->

## 正常工作的表现

<!-- zh-CN:end 2d3c3f286e55024c -->

- The document gets shorter as it gets better, and you are surprised how little is left.

<!-- zh-CN:begin d8e3bf8c6faf763b -->

- 文档在变好时变短，你会惊讶剩下这么少。

<!-- zh-CN:end d8e3bf8c6faf763b -->
- You can point at a leading word and see it change the agent's behaviour in more than one place.

<!-- zh-CN:begin 0985937ab8df02c1 -->

- 我能指出一个引导词，并在不止一处看到它改变代理行为。

<!-- zh-CN:end 0985937ab8df02c1 -->
- Nothing is stated twice, in any form. Duplication is the most reliable sign a document was never tested.

<!-- zh-CN:begin f44fcb7f2168f0ba -->

- 任何形式都没有内容说两遍。重复是最可靠的“文档从未测试”迹象。

<!-- zh-CN:end f44fcb7f2168f0ba -->
- Reference that only one branch needs sits behind a pointer rather than in the main file.

<!-- zh-CN:begin c46718d5418e46fb -->

- 只有一个分支需要的参考位于指针后，而不是主文件中。

<!-- zh-CN:end c46718d5418e46fb -->

## Where it fits

<!-- zh-CN:begin 9c154cf218fbce8a -->

## 所处位置

<!-- zh-CN:end 9c154cf218fbce8a -->

This is a reach-for-it-anytime standalone reference. It applies to the whole set, not to one skill. Every skill here was written with it, and it also covers the documents the other skills produce (a `GLOSSARY.md` and its ADRs, a spec, a ticket) once an agent has to read them. Its one direct caller is [retro](https://aihero.dev/skills-retro), which loads it before proposing any steering file or skill. When you're unsure which skill or flow fits a task, [ask-matt](https://aihero.dev/skills-ask-matt) routes you over the whole set.

<!-- zh-CN:begin d5029a512b97b8e9 -->

这是随时可用的独立参考。它适用于整个集合，不限于一项技能。这里的每项技能都用它编写，也覆盖其他技能产生、并需由代理读取的文档（`GLOSSARY.md` 及其 ADR、规格、工单）。唯一直接调用者是 [retro](https://aihero.dev/skills-retro)，它在提议任何引导文件或技能前加载本参考。不确定技能或流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 在整套技能中为你路由。

<!-- zh-CN:end d5029a512b97b8e9 -->
