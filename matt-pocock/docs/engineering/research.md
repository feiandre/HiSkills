## What it does

<!-- zh-CN:begin c7356a5ca8ad8593 -->

## 它做什么

<!-- zh-CN:end c7356a5ca8ad8593 -->

`research` answers a question by reading the sources that own the answer, then leaves a cited Markdown file in the repo. It works only from **[primary sources](https://www.aihero.dev/ai-coding-dictionary/primary-source)**: official docs, source code, specs, first-party APIs. It follows every claim back to the source that owns it, so it will not repeat a blog post's account of an API when the API's own docs are reachable.

<!-- zh-CN:begin 3d74e854a447a2cc -->

`research` 通过阅读拥有答案的来源来回答问题，然后留下一个带引用的 Markdown 文件。它只使用**[一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)**：官方文档、源代码、规格和第一方 API。它把每项主张追溯到拥有该主张的来源；API 自身文档可访问时，它不会重复博客文章对 API 的二手叙述。

<!-- zh-CN:end 3d74e854a447a2cc -->

It does not answer you in the conversation. The output is a file, written where the repo already keeps such notes, with a link on each claim. You get a document you can react to, hand to another agent, or throw away, rather than an answer that is gone when the [session](https://www.aihero.dev/ai-coding-dictionary/session) ends.

<!-- zh-CN:begin 2b4b6992b7a1de32 -->

它不会在对话中答复你。输出是文件，写入仓库既有的笔记位置，每项主张都有链接。你得到一份可回应、可交给另一智能体或可丢弃的文档，而不是在[会话](https://www.aihero.dev/ai-coding-dictionary/session)结束后就消失的答案。

<!-- zh-CN:end 2b4b6992b7a1de32 -->

## When to reach for it

<!-- zh-CN:begin d347a005da1b3efc -->

## 何时使用

<!-- zh-CN:end d347a005da1b3efc -->

Type `/research`, or the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reaches for it automatically when a task turns into reading legwork.

<!-- zh-CN:begin ada29f64719c093c -->

输入 `/research`，或任务变成阅读跑腿时让[智能体](https://www.aihero.dev/ai-coding-dictionary/agent)自动选择它。

<!-- zh-CN:end ada29f64719c093c -->

Reach for it when the next step is *finding something out* from outside the working directory (how a third-party API behaves, what a spec says, whether a version claim holds), and you'd rather not stall your own thread doing the reading. What you need decides which skill:

<!-- zh-CN:begin c7a9274d3e9c8e36 -->

当下一步需要从工作目录之外*查明某些内容*（第三方 API 如何表现、规格怎么规定、某个版本声明是否成立），而你不想为此停下自己的线程阅读时，使用它。需求类型决定使用哪个技能：

<!-- zh-CN:end c7a9274d3e9c8e36 -->

| What you need | Reach for |
| --- | --- |
| An external fact a decision is waiting on | `research` |
| A decision made *with* you, by interview | [grilling](https://aihero.dev/skills-grilling) |
| A durable architecture decision, written into `GLOSSARY.md` and ADRs | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| To find out whether an approach works in your codebase | [prototype](https://aihero.dev/skills-prototype) |
| A plan too big to hold in one session | [wayfinder](https://aihero.dev/skills-wayfinder) |

<!-- zh-CN:begin dde6855f3242a6ed -->

| 你需要什么 | 应使用 |
| --- | --- |
| 决策正在等待的外部事实 | `research` |
| 通过访谈与你共同作出的决定 | [质询](https://aihero.dev/skills-grilling) |
| 写入 `GLOSSARY.md` 和 ADR 的持久架构决策 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 查明某种方法在代码库中是否有效 | [原型](https://aihero.dev/skills-prototype) |
| 大到单个会话容纳不下的计划 | [wayfinder](https://aihero.dev/skills-wayfinder) |

<!-- zh-CN:end dde6855f3242a6ed -->

The line between `research` and `grill-with-docs` is the **shelf life of what comes back**. Research produces short-lived facts, such as what this library's auth mechanism does as of this week. An ADR records a decision you keep. If what you are producing is a decision rather than a fact, you are [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling), not researching.

<!-- zh-CN:begin 26a7a504307f88d1 -->

`research` 与 `grill-with-docs` 的区别在于**返回内容的保质期**。研究会产出短生命周期事实，例如本库的认证机制截至本周如何工作。ADR 记录你长期保留的决定。你产出的是决定而非事实时，你在[质询](https://www.aihero.dev/ai-coding-dictionary/grilling)，而不是研究。

<!-- zh-CN:end 26a7a504307f88d1 -->

## Delegated legwork

<!-- zh-CN:begin cc03fa98b66f77ba -->

## 委派的跑腿工作

<!-- zh-CN:end cc03fa98b66f77ba -->

The reading runs as a **background agent**. You keep working while it follows each claim to its primary source, writes one Markdown file, and reports back. Research is legwork you delegate, not thinking you outsource. You get a document to grill, plan, or design against, and you still make the decision.

<!-- zh-CN:begin f31326f3ebd8ec8d -->

阅读由**后台智能体**执行。你继续工作，它把每项主张追溯到一手来源，写入一个 Markdown 文件并回报。研究是你委派的跑腿工作，不是外包思考。你得到一份可供质询、规划或设计依据的文档，最终决定仍由你作出。

<!-- zh-CN:end f31326f3ebd8ec8d -->

Nothing stops the background agent from spawning another background agent of its own. This is the skill's best-documented problem.

<!-- zh-CN:begin b04efa0f94f0da5b -->

没有任何机制阻止后台智能体再生成自己的另一个后台智能体。这是本技能记录最充分的问题。

<!-- zh-CN:end b04efa0f94f0da5b -->

The repo decides where the file goes, not the skill. It follows whatever convention already exists for notes. If there is none, it picks a sensible place and tells you where. It writes one file per run.

<!-- zh-CN:begin f445a1c07ea3b711 -->

文件位置由仓库决定，而非技能决定。它遵循现有笔记约定。若不存在，选择合理位置并告诉你。每次运行写一个文件。

<!-- zh-CN:end f445a1c07ea3b711 -->

## Common questions

<!-- zh-CN:begin 116d08ed967b6740 -->

## 常见问题

<!-- zh-CN:end 116d08ed967b6740 -->

**It spawned a second research agent. Is that meant to happen?**

<!-- zh-CN:begin 8123433ca1ee2318 -->

**它又生成了一个研究智能体。应该这样吗？**

<!-- zh-CN:end 8123433ca1ee2318 -->

No. This is an open bug, [issue #530](https://github.com/mattpocock/skills/issues/530). The skill tells its caller to spin up a background agent but does not restrict the agent type. So the caller spawns a `general-purpose` agent, which has the `Agent` tool and the same instructions, and follows them again. One reporter measured a single research task costing roughly 450k [tokens](https://www.aihero.dev/ai-coding-dictionary/token) across three overlapping runs, and the duplicate finished half an hour later where the user could not see it. It also happens outside Claude Code. Users confirmed the same nesting in Codex with GPT-5.6-sol. There is no shipped fix. Users have patched their own installed copy with a line telling an agent that is already a [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) to do the work itself, That helps, but it is only an instruction, not a structural fix. After you invoke the skill, watch your background task list and stop the duplicate.

<!-- zh-CN:begin c591a188f62aaea8 -->

不应该。这是尚未修复的缺陷，[问题 #530](https://github.com/mattpocock/skills/issues/530)。技能告诉调用者启动后台智能体，却没有限制智能体类型。于是调用者生成具有 `Agent` 工具和相同指令的 `general-purpose` 智能体，后者再次遵循指令。一名报告者测得单个研究任务在三次重叠运行中消耗约 45 万[词元](https://www.aihero.dev/ai-coding-dictionary/token)，重复任务在半小时后才结束，而用户看不到它。Claude Code 之外也会发生。用户确认在 Codex 配合 GPT-5.6-sol 时存在同样嵌套。尚无已发布修复。用户给本地已安装副本加了一行，要求已经是[子智能体](https://www.aihero.dev/ai-coding-dictionary/subagent)的智能体自行完成工作。这有帮助，但只是指令，不是结构性修复。调用技能后，请观察后台任务列表并停止重复任务。

<!-- zh-CN:end c591a188f62aaea8 -->

The opposite failure also happens. If your own global instructions forbid an agent from re-delegating work, the background agent declines the task, and the skill does nothing without telling you.

<!-- zh-CN:begin f98cbe91ea4a697f -->

相反方向的失败也会发生。若你的全局指令禁止智能体再次委派工作，后台智能体会拒绝任务，技能就什么也不做，也不告诉你。

<!-- zh-CN:end f98cbe91ea4a697f -->

**Where should the file live, and should I commit it?**

<!-- zh-CN:begin 710cef68624f9238 -->

**文件应放在哪里，应该提交吗？**

<!-- zh-CN:end 710cef68624f9238 -->

The skill puts the file where the repo already keeps notes and has no further opinion. The community view is mostly settled: keep ADRs, not research files. One Discord thread on this question put it most clearly: "ADRs yes. Everything else archive or delete after done. It otherwise becomes cruft of work and can poison future repo reads if you've drifted away from the spec/research." A research file records what was true on the day it was written, so a stale one is worse than none. On balance, these files don't belong in git, and there is no standard home for them. People use Obsidian, a separate knowledge repo, or the issue tracker instead.

<!-- zh-CN:begin d3c21fbc2e9c2b54 -->

技能把文件放在仓库现有笔记位置，没有进一步主张。社区看法大体一致：保留 ADR，不保留研究文件。一场 Discord 讨论说得最清楚：“ADR 要保留。其他内容完成后归档或删除。否则会变成工作残渣，而且当你已经偏离规格／研究时，还可能污染未来的仓库读取。”研究文件记录撰写当日何为真，因此陈旧文件比没有更糟。总体而言，这些文件不适合进入 Git，也没有标准存放位置。人们改用 Obsidian、独立知识仓库或问题跟踪器。

<!-- zh-CN:end d3c21fbc2e9c2b54 -->

**What counts as a "high-trust" primary source, and who decides?**

<!-- zh-CN:begin 95290dda93d931df -->

**什么算“高可信”的一手来源，由谁决定？**

<!-- zh-CN:end 95290dda93d931df -->

The [model](https://www.aihero.dev/ai-coding-dictionary/model) does. The skill names the *kinds* of source that qualify (official docs, source code, specs, first-party APIs), and there is no allowlist, no domain gate, and no verification pass. This was the loudest objection when the skill was first proposed, and nobody has answered it publicly: "Five research subagents pointed at junk just gives you five confident wrong answers faster. How are you gating what counts as high-trust sources?" Your only protection is the citation on each claim. Follow two or three of them. If they land on a summary of the thing rather than the thing, the run failed.

<!-- zh-CN:begin 7ea6505469b9854b -->

由[模型](https://www.aihero.dev/ai-coding-dictionary/model)决定。技能只列出符合要求的来源*类别*（官方文档、源代码、规格、第一方 API），没有允许列表、域名门控或验证流程。这是技能最初提出时最强烈的反对意见，至今无人公开回答：“五个研究子智能体指向垃圾来源，只会更快给你五个自信的错误答案。你如何门控什么算高可信来源？”唯一保护是每项主张的引用。随机跟进两三个。如果它们只落在某物的摘要而不是原物上，此次运行失败。

<!-- zh-CN:end 7ea6505469b9854b -->

**Does a later session reuse what an earlier run found?**

<!-- zh-CN:begin 47a6b0cb168ae354 -->

**后续会话会复用先前运行的发现吗？**

<!-- zh-CN:end 47a6b0cb168ae354 -->

No. Nothing loads a past research file automatically. The file stays in the repo until a human or a skill points at it. This was the strongest early challenge to the design: "the value's the markdown becoming context the agent re-reads later, not the fetch itself. A write-once dead file is just a fancy search." The shipped skill does not solve it. In practice, the file is useful only when you feed it into the next step yourself: attach it to a spec, quote it into a grilling session, point a [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) at it.

<!-- zh-CN:begin a19faac6e5ce2f10 -->

不会。没有东西自动加载过去的研究文件。文件会一直留在仓库中，直到人或技能指向它。这是设计早期最有力的挑战：“价值在于 Markdown 成为智能体以后重读的上下文，而不是抓取行为。只写一次的死文件只是花哨的搜索。”已发布技能没有解决它。实践中，只有当你自己把文件送入下一步时才有用：附加到规格、在质询会话中引用，或把[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)指向它。

<!-- zh-CN:end a19faac6e5ce2f10 -->

**Why not just ask the agent to go read the docs?**

<!-- zh-CN:begin 80aa7b9124de2640 -->

**为什么不直接让智能体去读文档？**

<!-- zh-CN:end 80aa7b9124de2640 -->

You can, and a two-line prompt saying exactly that was the practice this skill replaced. The skill gives you two things the prompt does not. It runs in the background, so your session's [context](https://www.aihero.dev/ai-coding-dictionary/context) stays clean. And the primary-source constraint and the cited-file output are the same every time, rather than depending on how you phrased the prompt. Compared with a [harness](https://www.aihero.dev/ai-coding-dictionary/harness)'s own deep-research mode, the difference is the file and the primary-source rule, not the search. If a two-line prompt gets you what you need on a small question, use the two-line prompt.

<!-- zh-CN:begin 06fa27e2c92718bc -->

可以；两行提示词正是本技能所替代的做法。技能提供提示词没有的两点：它在后台运行，使你的会话[上下文](https://www.aihero.dev/ai-coding-dictionary/context)保持干净；一手来源约束和带引用文件输出每次都一致，不依赖你的提示词措辞。与[宿主](https://www.aihero.dev/ai-coding-dictionary/harness)自带深度研究模式相比，区别在文件和一手来源规则，而不在搜索。若两行提示词就能解决小问题，请使用它。

<!-- zh-CN:end 06fa27e2c92718bc -->

**When does it stop reading?**

<!-- zh-CN:begin c38c525e4f17a6df -->

**它何时停止阅读？**

<!-- zh-CN:end c38c525e4f17a6df -->

The skill has no stopping criterion. This shows up as two complaints that look opposite but have the same cause: agents that go far too deep, and agents that cover a topic broadly but miss the one detail that mattered. One practitioner put it as "deep-research skills are a bit too deep sometimes. And telling an agent to research usually results in missing crucial details." You have to set the scope. A narrow, answerable question (one API, one behaviour, one version claim) comes back far better than "research X".

<!-- zh-CN:begin 09bfa71681411246 -->

技能没有停止条件。这表现为两个看似相反、成因相同的抱怨：智能体钻得太深，或智能体广泛覆盖主题却漏掉关键细节。一位实践者说：“深度研究技能有时钻得太深。而让人研究，通常又会漏掉关键细节。”你必须设定范围。狭窄、可回答的问题（一个 API、一种行为、一项版本声明）返回结果远好于“研究 X”。

<!-- zh-CN:end 09bfa71681411246 -->

**`/wayfinder` created research tickets. Do I resolve those myself?**

<!-- zh-CN:begin 2b24c805af1c5c03 -->

**`/wayfinder` 创建了研究工单。我需要自行解决它们吗？**

<!-- zh-CN:end 2b24c805af1c5c03 -->

No, it now fires them for you. In the unreleased changes since v1.1, a charting session spawns one `/research` subagent per research ticket and runs them in parallel. Each one records its findings on a throwaway `research/<name>` branch, with a [context pointer](https://www.aihero.dev/ai-coding-dictionary/context-pointer) from the ticket. Research tickets are the one exception to wayfinder's one-ticket-per-session rule, because they are [AFK](https://www.aihero.dev/ai-coding-dictionary/afk): nothing waits on you. One known problem: deleting the branch later breaks the context pointers in the tickets.

<!-- zh-CN:begin afedf5b9b8a6e89b -->

不需要，现在它会替你触发。自 v1.1 以来尚未发布的改动中，制图会话会为每个研究工单生成一个 `/research` 子智能体并并行运行。每个子智能体把发现记录在一次性 `research/<name>` 分支上，并从工单提供[上下文指针](https://www.aihero.dev/ai-coding-dictionary/context-pointer)。研究工单是 wayfinder“每会话一个工单”规则唯一的例外，因为它们是 [AFK](https://www.aihero.dev/ai-coding-dictionary/afk)：无需等待你。已知问题：以后删除分支会破坏工单中的上下文指针。

<!-- zh-CN:end afedf5b9b8a6e89b -->

## It's working if

<!-- zh-CN:begin ee0b104479391865 -->

## 正常工作时的表现

<!-- zh-CN:end ee0b104479391865 -->

- Your own session keeps going. If you are sitting watching it read, the delegation didn't happen.

<!-- zh-CN:begin 29dfec1f85dadb2c -->

- 你的会话继续运行。如果你坐着看它阅读，说明委派没有发生。

<!-- zh-CN:end 29dfec1f85dadb2c -->
- Exactly one new background task appears. A second one with a near-identical name is the nesting bug.

<!-- zh-CN:begin a9c2e1dfc8c5f13d -->

- 恰好出现一个新的后台任务。出现第二个名称近乎相同的任务，就是嵌套缺陷。

<!-- zh-CN:end a9c2e1dfc8c5f13d -->
- One new Markdown file shows up, in the folder the repo already uses for notes, and the agent tells you the path.

<!-- zh-CN:begin 6824be8165eb56bc -->

- 出现一个新 Markdown 文件，位于仓库现有笔记文件夹中，智能体会告诉你路径。

<!-- zh-CN:end 6824be8165eb56bc -->
- Every claim in it carries a link, and following two at random lands you on an official doc, a spec, or the source file itself, not on someone's write-up of it.

<!-- zh-CN:begin 46b25362d9bc0896 -->

- 文件中的每项主张都有链接；随机跟进两条，会落到官方文档、规格或源文件本身，而不是他人撰写的说明。

<!-- zh-CN:end 46b25362d9bc0896 -->
- You can make the decision you were stuck on from the file alone, without going back to the sources yourself.

<!-- zh-CN:begin 8253938f3a81d985 -->

- 你能仅凭文件作出原本卡住的决定，而不必自行回查来源。

<!-- zh-CN:end 8253938f3a81d985 -->

## Where it fits

<!-- zh-CN:begin 9699516f0a3df1f5 -->

## 所处位置

<!-- zh-CN:end 9699516f0a3df1f5 -->

`research` is a reach-for-it-anytime standalone. It feeds the thinking skills and is not a step in the build chain. You take its file *into* the flow. [grilling](https://aihero.dev/skills-grilling) and [grill-with-docs](https://aihero.dev/skills-grill-with-docs) ask sharper questions when they already have the facts, and [to-spec](https://aihero.dev/skills-to-spec) can synthesise against it. [wayfinder](https://aihero.dev/skills-wayfinder) is the one skill that invokes it directly. It resolves each research ticket on its map with a `/research` subagent. For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

<!-- zh-CN:begin 9ee563fceb67e7a9 -->

`research` 是可随时使用的独立技能。它为思考类技能提供输入，不是构建链的步骤。你把它的文件*带入*流程。已有事实时，[质询](https://aihero.dev/skills-grilling)和 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 能提出更精准的问题；[to-spec](https://aihero.dev/skills-to-spec) 可据此综合。直接调用它的是 [wayfinder](https://aihero.dev/skills-wayfinder)，它通过 `/research` 子智能体解决地图上的每个研究工单。如需查看整个地图，见 [ask-matt](https://aihero.dev/skills-ask-matt)。

<!-- zh-CN:end 9ee563fceb67e7a9 -->
