## What it does

<!-- zh-CN:begin 534e5e0d4c1c0966 -->

## 它的作用

<!-- zh-CN:end 534e5e0d4c1c0966 -->

`grill-with-docs` interviews you about a plan or design until you and the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) share one understanding of it, and writes the vocabulary and the hard decisions into your repo while it does. It is the same interview [grill-me](https://aihero.dev/skills-grill-me) runs (a round of questions, then wait, then the next round), pointed at a codebase.

<!-- zh-CN:begin 2c27c8d0d585db0a -->

`grill-with-docs` 就计划或设计向你提问，直到你与[代理](https://www.aihero.dev/ai-coding-dictionary/agent)形成同一理解，并在过程中把词汇和困难决定写入仓库。它运行与 [grill-me](https://aihero.dev/skills-grill-me) 相同的访谈（先问一轮，等待，再问下一轮），只是面向代码库。

<!-- zh-CN:end 2c27c8d0d585db0a -->

It is **[stateful](https://www.aihero.dev/ai-coding-dictionary/stateful)**. Every other grilling skill leaves the [session](https://www.aihero.dev/ai-coding-dictionary/session) in your head; this one leaves files on disk. When a term resolves, the skill writes it to `GLOSSARY.md` at once, not in a batch at the end. When a decision passes three gates, the skill writes it as an ADR. That is the whole difference, and it also causes most of the trouble people have with the skill. The artifacts are real files in a real repo, so they can be missing when you expected them, and they can drift when more than one person writes them.

<!-- zh-CN:begin 5b266141bcac7c1d -->

它是**[有状态的](https://www.aihero.dev/ai-coding-dictionary/stateful)**。其他追问技能只把[会话](https://www.aihero.dev/ai-coding-dictionary/session)留在你脑中；这个技能会在磁盘留下文件。一个术语确定后，技能立即写入 `GLOSSARY.md`，不在末尾批量写。一个决定通过三道关卡后，技能把它写成 ADR。这就是全部区别，也正是大多数使用麻烦的来源。产物是真实仓库中的真实文件，因此它们可能在你以为存在时缺失，也可能因多人写入而漂移。

<!-- zh-CN:end 5b266141bcac7c1d -->

## When to reach for it

<!-- zh-CN:begin 50c128ab5c626466 -->

## 何时使用

<!-- zh-CN:end 50c128ab5c626466 -->

You invoke this by typing `/grill-with-docs`, and the agent won't reach for it on its own.

<!-- zh-CN:begin 45b852370f175087 -->

你通过输入 `/grill-with-docs` 调用它，代理不会自行使用。

<!-- zh-CN:end 45b852370f175087 -->

Reach for it at the start of a change, in a repo, when the plan is still fuzzy and the words for the thing are not settled yet. It is the single-session tool. Which grilling skill you want depends on what is in front of you:

<!-- zh-CN:begin 98fdadbf38001826 -->

在仓库里开始一项变更时使用，此时计划仍模糊、事物的名称尚未确定。它是单会话工具。选择哪种追问技能取决于眼前情况：

<!-- zh-CN:end 98fdadbf38001826 -->

| What you have | Reach for |
| --- | --- |
| You aren't working in a working directory at all | [grill-me](https://aihero.dev/skills-grill-me) |
| A repo, and a change you can settle in one session | `grill-with-docs` |
| An effort too big to hold in one session (a greenfield build, a large feature) | [wayfinder](https://aihero.dev/skills-wayfinder) |
| A repo with no domain docs at all, and no particular feature in mind | `grill-with-docs`, aimed at the repo rather than a change |
| A decision blocked on knowledge in someone else's head | [to-questionnaire](https://aihero.dev/skills-to-questionnaire) |

<!-- zh-CN:begin 6fa9ff4c0d0d4007 -->

| 你拥有的条件 | 使用 |
| --- | --- |
| 你根本不在工作目录中 | [grill-me](https://aihero.dev/skills-grill-me) |
| 有一个仓库，以及可在一次会话中定好的变更 | `grill-with-docs` |
| 工作大到一次会话装不下（全新构建、大型功能） | [wayfinder](https://aihero.dev/skills-wayfinder) |
| 仓库完全没有领域文档，也没有特定功能想法 | 使用 `grill-with-docs`，对象是仓库而非某项变更 |
| 决定受限于别人脑中的知识 | [to-questionnaire](https://aihero.dev/skills-to-questionnaire) |

<!-- zh-CN:end 6fa9ff4c0d0d4007 -->

The wayfinder split comes down to session count: `/grill-with-docs` for single-session planning, `/wayfinder` for multi-session planning.

<!-- zh-CN:begin e29ef13b534fd592 -->

Wayfinder 的分界取决于会话数：`/grill-with-docs` 用于单会话规划，`/wayfinder` 用于多会话规划。

<!-- zh-CN:end e29ef13b534fd592 -->

## Prerequisites

<!-- zh-CN:begin 7fdf09d18431831d -->

## 前置条件

<!-- zh-CN:end 7fdf09d18431831d -->

The skill writes into your repo, so you need to be somewhere it is safe to write. Resolved terms go to a `GLOSSARY.md` glossary at the root, or to the relevant context's `GLOSSARY.md`, if a `GLOSSARY-MAP.md` at the root marks the repo as multi-context. Decisions go to `docs/adr/`. The skill creates both only when it needs them. Nothing exists until the first term or decision is settled, so you set up nothing in advance.

<!-- zh-CN:begin 4fbb8d6ad2b67055 -->

技能会写入仓库，因此必须位于可安全写入的位置。已确定术语写入根目录 `GLOSSARY.md`；如果根目录 `GLOSSARY-MAP.md` 将仓库标记为多上下文，则写入相关上下文的 `GLOSSARY.md`。决定写入 `docs/adr/`。技能只在需要时创建二者。第一个术语或决定确定前什么都不存在，因此无需预配置。

<!-- zh-CN:end 4fbb8d6ad2b67055 -->

It also needs two other skills present, because its own `SKILL.md` is one line that delegates to them. [grilling](https://aihero.dev/skills-grilling) supplies the interview, and [domain-modeling](https://aihero.dev/skills-domain-modeling) supplies the writing. Installing `grill-with-docs` alone gets you a skill that does not work.

<!-- zh-CN:begin e1f509acf144384f -->

它还需要两个技能存在，因为自身 `SKILL.md` 只有一行，并委派给它们。[grilling](https://aihero.dev/skills-grilling) 提供访谈，[domain-modeling](https://aihero.dev/skills-domain-modeling) 提供写入。只安装 `grill-with-docs` 得到的是无法工作的技能。

<!-- zh-CN:end e1f509acf144384f -->

## The paper trail

<!-- zh-CN:begin 72e730285f90005b -->

## 留下的记录

<!-- zh-CN:end 72e730285f90005b -->

Three things come out of a session, and they are not equal.

<!-- zh-CN:begin 19b12590c07275cc -->

一次会话产生三样东西，价值并不相同。

<!-- zh-CN:end 19b12590c07275cc -->

| What resolved | Where it lands |
| --- | --- |
| A term: the project's own word for a thing | `GLOSSARY.md`, inline, the moment it resolves |
| A decision that is hard to reverse, surprising without context, and a real trade-off | An ADR under `docs/adr/` |
| Everything else you decided | The conversation, and nowhere else |

<!-- zh-CN:begin 87c027fb1347e22a -->

| 确定了什么 | 落到哪里 |
| --- | --- |
| 一个术语：项目对某事物的自己的称呼 | 在确定那一刻直接写入 `GLOSSARY.md` |
| 一个难以逆转、脱离上下文会令人意外且涉及真实取舍的决定 | `docs/adr/` 下的一个 ADR |
| 你作出的其他所有决定 | 对话中，除此之外没有别处 |

<!-- zh-CN:end 87c027fb1347e22a -->

That third row is the one that catches people out. `GLOSSARY.md` is only a glossary. It holds no implementation details, no [spec](https://www.aihero.dev/ai-coding-dictionary/spec), and no scratch notes. An ADR needs all three conditions at once, so most decisions do not qualify and most sessions produce none. A session that yields a sharper glossary and zero ADRs is working as designed, but it means most of what you agreed exists only in the [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) you agreed it in. Hand that same conversation to [to-spec](https://aihero.dev/skills-to-spec) rather than [clearing](https://www.aihero.dev/ai-coding-dictionary/clearing) it.

<!-- zh-CN:begin 52bb15e436ab97ae -->

第三行最容易让人误解。`GLOSSARY.md` 只是词汇表。它不包含实现细节、[规格](https://www.aihero.dev/ai-coding-dictionary/spec)或草稿笔记。ADR 必须同时满足三个条件，因此大多数决定不符合，绝大多数会话不会产生 ADR。一次会话得到更清晰的词汇表和零个 ADR 属于按设计工作，但这也意味着大多数已同意内容只存在于当时的[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)。此时应把同一段对话交给 [to-spec](https://aihero.dev/skills-to-spec)，而不是[清空](https://www.aihero.dev/ai-coding-dictionary/clearing)。

<!-- zh-CN:end 52bb15e436ab97ae -->

The glossary is the main output. This skill builds domain language: the project's own words, agreed once, so you, the agent and your colleagues do not have to work them out again. Not everyone agrees that this improves agent performance. The strongest objection is that a term and its plain-English expansion get the same result from the [model](https://www.aihero.dev/ai-coding-dictionary/model), and that the vocabulary mainly shortens communication between the humans who share it. On that view the glossary is still valuable, but the value goes to the humans.

<!-- zh-CN:begin 7ce449f9c85549d9 -->

词汇表是主要输出。该技能构建领域语言：项目自己的术语一次性达成共识，让你、代理和同事不必再次推敲。并非所有人都认为这能改善代理表现。最强的反对意见是：术语与其平实英文展开会从[模型](https://www.aihero.dev/ai-coding-dictionary/model)得到相同结果，词汇主要用于缩短共享它的人之间的沟通。按这种观点，词汇表仍然有价值，只是价值归于人类。

<!-- zh-CN:end 7ce449f9c85549d9 -->

## Common questions

<!-- zh-CN:begin 8e491bf9c43b04a5 -->

## 常见问题

<!-- zh-CN:end 8e491bf9c43b04a5 -->

**Should I use this or `/wayfinder`?**
Scope decides it. Use this for anything you can settle in one session; use [wayfinder](https://aihero.dev/skills-wayfinder) when the effort is too big to hold in one, and it charts the work as a map of decision [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) first. Wayfinder is slower and denser, and reaching for it on a well-scoped feature is the common mistake. It does not replace this skill, and it can start a grilling session for the parts of the map that suit one.

<!-- zh-CN:begin 6c6041ef856b564c -->

**应该用这个还是 `/wayfinder`？**
范围决定选择。一次会话能定好的工作用这个；大到一次会话装不下时使用 [wayfinder](https://aihero.dev/skills-wayfinder)，它先把工作绘制成决策[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)地图。Wayfinder 更慢、更密集；对范围明确的功能使用它很常见，也是错误所在。它不替代此技能，也可以为地图中适合追问的部分启动一次追问会话。

<!-- zh-CN:end 6c6041ef856b564c -->

**It ran, but no `GLOSSARY.md` and no ADRs appeared.**
There are two known causes. The first is that nothing qualified. ADRs need all three gates, and a session about a change with no new vocabulary has nothing to write. The second is a real bug. When the skill runs inside another orchestration layer (a spec-driven-development wrapper, a multi-agent framework, a rule that invokes it as a step in someone else's pipeline), users report that the file-writing half silently does not happen, while the interview still runs. The bug is filed and unfixed. If you are in that setup, check the working directory before you trust the session's output.

<!-- zh-CN:begin 5d0a892baa0fa628 -->

**它运行了，但没有出现 `GLOSSARY.md`，也没有 ADR。**
有两个已知原因。第一，没有内容符合条件。ADR 需要同时通过三道关卡；一次关于变更的会话若没有新词汇，也就没有内容可写。第二是真实缺陷。技能运行在另一编排层内部时（规格驱动开发包装器、多代理框架、把技能作为别人流水线步骤的规则），用户报告文件写入部分会静默不执行，而访谈仍照常运行。缺陷已记录但尚未修复。若处于这种设置，信任会话输出前先检查工作目录。

<!-- zh-CN:end 5d0a892baa0fa628 -->

**It asked everything at once, with no recommendations, and never mentioned `GLOSSARY.md`.**
That is the skill failing to load its two dependencies. Because `SKILL.md` is a one-line delegation, an agent that does not pick up [grilling](https://aihero.dev/skills-grilling) and [domain-modeling](https://aihero.dev/skills-domain-modeling) guesses at what grilling means, and you get every question at once with no structure. Partial loading is more confusing. `grilling` loads, `domain-modeling` does not, and you get a good interview with no paper trail. How often it happens depends on the model and the [effort](https://www.aihero.dev/ai-coding-dictionary/effort) level, and it is the most reported problem with this skill. If you suspect it, ask the agent directly which skills it loaded.

<!-- zh-CN:begin 6caf3eaea84a39e0 -->

**它一次问了全部问题，没有建议，也从未提到 `GLOSSARY.md`。**
这是技能未能加载两个依赖。由于 `SKILL.md` 只有一行委派，未获得 [grilling](https://aihero.dev/skills-grilling) 和 [domain-modeling](https://aihero.dev/skills-domain-modeling) 的代理会猜测追问的含义，于是你一次收到全部问题，没有结构。部分加载更令人困惑：`grilling` 已加载，`domain-modeling` 未加载，你得到不错的访谈却没有书面记录。发生频率取决于模型和[投入程度](https://www.aihero.dev/ai-coding-dictionary/effort)，也是此技能报告最多的问题。怀疑时，直接问代理加载了哪些技能。

<!-- zh-CN:end 6caf3eaea84a39e0 -->

**Where did all my other decisions go?**
Into the conversation only. This is the most serious open complaint about the skill. The glossary is not a spec, most answers do not earn an ADR, and no record links each resolved answer to a spec, a ticket and a test. Later steps soften precise answers (ordering guarantees, negative requirements, numeric defaults) into weaker prose, and the result can look complete while missing the thing you decided. For now, keep the session and feed it straight to [to-spec](https://aihero.dev/skills-to-spec). Then re-read the spec against your own answers rather than assuming it captured them.

<!-- zh-CN:begin 8e6e17777fcf969a -->

**我作出的其他决定去哪儿了？**
只留在对话中。这是对此技能最严重的未决抱怨。词汇表不是规格，大多数回答不足以成为 ADR，也没有记录把每个已确定回答链接到规格、工单和测试。后续步骤会把精确回答（顺序保证、否定性要求、数字默认值）弱化成含混文字，结果看似完整，却漏掉你决定的事项。目前应保留会话并直接交给 [to-spec](https://aihero.dev/skills-to-spec)，然后对照自己的回答重读规格，别假定它已捕捉全部内容。

<!-- zh-CN:end 8e6e17777fcf969a -->

**Can I point it at an existing repo that has no docs at all?**
Yes. This is the right skill for a codebase with no ADRs, no domain language and no design principles: invoke it and say "help me document my repo". Users often pair it with [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) for building or repairing a `GLOSSARY.md`. Expect to steer it. It reads code and asks you about what it finds, and you decide which of the words already in the codebase are the right ones.

<!-- zh-CN:begin b1a233900e298cf1 -->

**可以把它指向完全没有文档的现有仓库吗？**
可以。对于没有 ADR、领域语言和设计原则的代码库，这正是适合的技能：调用它并说“帮助我为仓库编写文档”。用户常把它与 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 搭配，用于构建或修复 `GLOSSARY.md`。要准备引导它。它读取代码并就发现提问，你决定代码库中哪些词才是正确术语。

<!-- zh-CN:end b1a233900e298cf1 -->

**What should I do when the session ends?**
The skill's closing message is often open-ended, which is a known problem. In the main flow the answer is [to-spec](https://aihero.dev/skills-to-spec), in the same conversation. If the change is small enough to build immediately, go straight to [implement](https://aihero.dev/skills-implement) instead.

<!-- zh-CN:begin cc18de4fa39d8d7e -->

**会话结束时应做什么？**
技能的结束消息通常开放式，这是已知问题。主流程中的答案是同一对话里的 [to-spec](https://aihero.dev/skills-to-spec)。如果变更小到可以立即构建，直接使用 [implement](https://aihero.dev/skills-implement)。

<!-- zh-CN:end cc18de4fa39d8d7e -->

**Why is it called that?**
Nobody is happy with the name. There is an open suggestion to rename it `grill-domain-model`, which describes the behaviour more accurately. Nothing has moved on it. If a rename ever lands, the docs page moves with it and the URL changes.

<!-- zh-CN:begin 1a536a38aeba3644 -->

**为什么叫这个名字？**
没人对这个名称满意。已有开放建议将其改名为 `grill-domain-model`，这更准确描述行为。改名尚未推进。若最终落地，文档页与 URL 会随之改变。

<!-- zh-CN:end 1a536a38aeba3644 -->

## It's working if

<!-- zh-CN:begin 2dd31e03c0a4a664 -->

## 正常工作的表现

<!-- zh-CN:end 2dd31e03c0a4a664 -->

- `GLOSSARY.md` changes *during* the session, term by term, rather than appearing in one lump at the end.

<!-- zh-CN:begin a05a91256778e46f -->

- `GLOSSARY.md` 在会话*过程中*逐个术语变化，而不是最后一次性出现。

<!-- zh-CN:end a05a91256778e46f -->
- The glossary reads as pure vocabulary (your project's words with tight definitions) and contains no implementation detail or spec-like prose.

<!-- zh-CN:begin 81299383912bb3ee -->

- 词汇表是纯词汇（项目用语及其严格定义），没有实现细节或类似规格的文字。

<!-- zh-CN:end 81299383912bb3ee -->
- Questions the codebase can answer get answered by reading the codebase, not asked of you.

<!-- zh-CN:begin 692e059f785670f7 -->

- 代码库能回答的问题通过阅读代码库回答，不拿来问你。

<!-- zh-CN:end 692e059f785670f7 -->
- You get few or no ADRs, and the ones you get are decisions you would be annoyed to have to argue again.

<!-- zh-CN:begin 1cb3a0ea4eaa1cc0 -->

- ADR 很少或没有；出现的是你不想再次争辩的决定。

<!-- zh-CN:end 1cb3a0ea4eaa1cc0 -->
- It challenges a word you used because your existing glossary defines it differently.

<!-- zh-CN:begin 65df8faf1fd85282 -->

- 你用了某个词时，技能会提出质疑，因为现有词汇表对它有不同定义。

<!-- zh-CN:end 65df8faf1fd85282 -->

## Where it fits

<!-- zh-CN:begin 6483ebeebc436b9a -->

## 所处位置

<!-- zh-CN:end 6483ebeebc436b9a -->

`grill-with-docs` is the head of the main build chain:

<!-- zh-CN:begin 41faec1612ebdeb9 -->

`grill-with-docs` 是主构建链的起点：

<!-- zh-CN:end 41faec1612ebdeb9 -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

It comes before anything is written down as a spec. It produces the shared understanding and settled vocabulary that [to-spec](https://aihero.dev/skills-to-spec) then synthesises without interviewing you again. Its close neighbours are [grill-me](https://aihero.dev/skills-grill-me), the same interview with no repo and no files, and [domain-modeling](https://aihero.dev/skills-domain-modeling), the glossary-and-ADR discipline it drives; both use the [grilling](https://aihero.dev/skills-grilling) primitive for the interview. Upstream of it, [wayfinder](https://aihero.dev/skills-wayfinder) charts efforts too large for one session and can hand parts of the map back down to it. When you're unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 62a8ad940492df98 -->

它位于任何内容写成规格之前。它产生共享理解和确定词汇，[to-spec](https://aihero.dev/skills-to-spec) 随后据此综合，而不再次访谈你。邻近技能包括 [grill-me](https://aihero.dev/skills-grill-me)（相同访谈，但没有仓库和文件）以及 [domain-modeling](https://aihero.dev/skills-domain-modeling)（它驱动的词汇表与 ADR 纪律）；两者都用 [grilling](https://aihero.dev/skills-grilling) 原语进行访谈。上游的 [wayfinder](https://aihero.dev/skills-wayfinder) 为超出一次会话的工作绘制地图，也可将地图的部分交回本技能。不确定哪个技能或流程适合时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。

<!-- zh-CN:end 62a8ad940492df98 -->
