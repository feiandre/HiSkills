## What it does

<!-- zh-CN:begin 1c63c92841b5e2fb -->

## 它做什么

<!-- zh-CN:end 1c63c92841b5e2fb -->

`domain-modeling` builds and sharpens a project's **ubiquitous language** while you are designing. It challenges a term that conflicts with the glossary, asks for a precise word where you used a vague one, and tests a relationship against a concrete scenario until the boundaries are exact.

<!-- zh-CN:begin e094b76bc8bce72c -->

`domain-modeling` 在设计时构建并完善项目**通用语言**：挑战与术语表冲突的词，为含糊用语要求精确词，并用具体场景检验关系直到边界准确。

<!-- zh-CN:end e094b76bc8bce72c -->

It is the **active** discipline, not the passive one. Any skill can read `GLOSSARY.md` to borrow its vocabulary. This skill is for when you are *changing* the model, which is why it interrupts you. It writes a term into `GLOSSARY.md` at the moment you settle it, in the middle of the conversation, rather than producing a tidy glossary at the end. A glossary written at the end is a summary of a [session](https://www.aihero.dev/ai-coding-dictionary/session); the inline version is the session's output.

<!-- zh-CN:begin be0b3eb181df4ae1 -->

这是**主动**纪律。任何技能都可读取 `GLOSSARY.md` 借用词汇；本技能用于你正在*改变*模型，因此会打断你。术语一确定就在对话中写入 `GLOSSARY.md`，而非最后整理。末尾写成的术语表只是[会话](https://www.aihero.dev/ai-coding-dictionary/session)摘要，内联更新才是会话产物。

<!-- zh-CN:end be0b3eb181df4ae1 -->

## When to reach for it

<!-- zh-CN:begin 00c1896c44920b35 -->

## 何时使用

<!-- zh-CN:end 00c1896c44920b35 -->

Type `/domain-modeling`, or the agent reaches for it automatically when a task fits. In practice, automatic invocation is the weakest part of the skill. When `grill-with-docs` or `wayfinder` say to load it, [models](https://www.aihero.dev/ai-coding-dictionary/model) often load `grilling` and skip this one. If a [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) session runs and `GLOSSARY.md` is unchanged at the end, that is what happened. Invoke it by name alongside the other skill.

<!-- zh-CN:begin e5dee7d54e98f9b9 -->

输入 `/domain-modeling`，或任务适合时由代理自动使用。实践中自动调用最弱：`grill-with-docs` 或 `wayfinder` 要求加载时，[模型](https://www.aihero.dev/ai-coding-dictionary/model)常只加载 `grilling` 而跳过本技能；[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)结束 `GLOSSARY.md` 未变通常如此。应与另一技能并列按名调用。

<!-- zh-CN:end e5dee7d54e98f9b9 -->

Reach for it when the *words* are the problem:

<!-- zh-CN:begin 74d7372931d76c0d -->

问题在*词语*时使用：

<!-- zh-CN:end 74d7372931d76c0d -->

| The situation | The move |
| --- | --- |
| Two people mean different things by "cancellation" | `domain-modeling`: pick the canonical term, list the other under `_Avoid_` |
| "Account" is doing three jobs in three files | `domain-modeling`: split it into Customer and User |
| You just made a hard-to-reverse architectural choice | `domain-modeling`: it offers an ADR, if the choice clears the bar |
| The module's *shape* is the problem: where the seam goes, how deep the interface is | [codebase-design](https://aihero.dev/skills-codebase-design) |
| You want the whole plan interrogated before you build | [grill-with-docs](https://aihero.dev/skills-grill-with-docs), which drives this skill underneath |
| You want a term looked up, not changed | Nothing. Read `GLOSSARY.md`. It is a file. |

<!-- zh-CN:begin f9333bcf99185287 -->

| 情况 | 动作 |
| --- | --- |
| 两人对“取消”含义不同 | `domain-modeling`：选规范词，另一词列入 `_Avoid_` |
| “账户”在三个文件承担三种职责 | `domain-modeling`：拆为 Customer 与 User |
| 刚做出难逆架构决定 | `domain-modeling`：达标时提供 ADR |
| 模块*形状*是问题：接缝位置、接口深度 | [codebase-design](https://aihero.dev/skills-codebase-design) |
| 构建前要审问整个计划 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，底层驱动本技能 |
| 只想查词，不想改 | 无需技能，阅读 `GLOSSARY.md` |

<!-- zh-CN:end f9333bcf99185287 -->

## Prerequisites

<!-- zh-CN:begin e59353891fdef02b -->

## 前提

<!-- zh-CN:end e59353891fdef02b -->

None up front. The skill writes into two places and creates both lazily:

<!-- zh-CN:begin 8ac79822adfba00a -->

无需预先准备。技能写两处并延迟创建：

<!-- zh-CN:end 8ac79822adfba00a -->

- **`GLOSSARY.md`** at the repo root. The skill creates it when you settle the first term. In a repo with a `GLOSSARY-MAP.md` at the root, terms go into the per-context `GLOSSARY.md` the map points at instead.

<!-- zh-CN:begin ec653b6c23579e14 -->

- 仓库根 **`GLOSSARY.md`**：确定首个术语时创建。根有 `GLOSSARY-MAP.md` 时写入映射指向的逐上下文 `GLOSSARY.md`。

<!-- zh-CN:end ec653b6c23579e14 -->
- **`docs/adr/`**. The skill creates it with the first ADR that clears the bar.

<!-- zh-CN:begin 7489595763376601 -->

- **`docs/adr/`**：首个达标 ADR 时创建。

<!-- zh-CN:end 7489595763376601 -->

Nothing needs to exist before you start, and the skill creates nothing in advance.

<!-- zh-CN:begin d9371cd04781f1e1 -->

开始前无文件必须存在，技能也不提前创建。

<!-- zh-CN:end d9371cd04781f1e1 -->

## Two artifacts, two bars

<!-- zh-CN:begin 39dc0a464e84bc00 -->

## 两个产物、两套标准

<!-- zh-CN:end 39dc0a464e84bc00 -->

The glossary and the ADR have different bars. Most of the trouble with this skill comes from mixing them up.

<!-- zh-CN:begin e1086b898e915efc -->

术语表与 ADR 标准不同，本技能多数问题来自混淆。

<!-- zh-CN:end e1086b898e915efc -->

| | `GLOSSARY.md` | `docs/adr/NNNN-slug.md` |
| --- | --- | --- |
| Holds | Terms. What a thing **is**, in one or two sentences, with rejected synonyms under `_Avoid_` | One decision, in one to three sentences: context, choice, reason |
| Bar to write | A vague term became canonical | **All three**: hard to reverse, surprising without context, the result of a real trade-off |
| Written | Inline, the moment the term is settled | Offered, not assumed |
| Never holds | Implementation details, a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), a scratch pad, general programming concepts | A diary of every choice made this session |

<!-- zh-CN:begin 92fb1f6be37e650f -->

| | `GLOSSARY.md` | `docs/adr/NNNN-slug.md` |
| --- | --- | --- |
| 内容 | 术语；用一两句说明事物**是什么**，拒绝同义词列入 `_Avoid_` | 一个决策，一两到三句：上下文、选择、原因 |
| 写入标准 | 模糊词成为规范名 | **三项全符合**：难逆、无上下文会意外、真实取舍结果 |
| 写入时机 | 术语确定时内联写 | 提议而非假定 |
| 禁止内容 | 实现细节、[规格](https://www.aihero.dev/ai-coding-dictionary/spec)、草稿、通用编程概念 | 本会话每个选择日记 |

<!-- zh-CN:end 92fb1f6be37e650f -->

Miss any one of the ADR's three tests and there is no ADR. An easily-reversed decision will just get reversed; an unsurprising one is nobody's question; one with no real alternative records that you did the obvious thing.

<!-- zh-CN:begin 9121ae8cc92bd9a3 -->

ADR 三项测试缺一不写。易逆决定会被反转；不意外者无人提问；无真实替代说明做了显然之事。

<!-- zh-CN:end 9121ae8cc92bd9a3 -->

The `GLOSSARY.md` rule matters most, because it is the one that breaks in practice. **It is a glossary and nothing else.** Left unchecked, models treat "write to `GLOSSARY.md`" as permission to persist every answer you give, and the file turns into a running spec. This is the most-reported problem with the skill, across several models.

<!-- zh-CN:begin efce311a192b5549 -->

`GLOSSARY.md` 规则最重要，因实践常坏。**它只是术语表。** 不限制时，模型把“写 `GLOSSARY.md`”理解为保存每项回答，文件变成流动规格。这是多模型最常见的问题。

<!-- zh-CN:end efce311a192b5549 -->

## Cross-referencing, and where it stops

<!-- zh-CN:begin bcf15e01da34e4d3 -->

## 交叉引用及其边界

<!-- zh-CN:end bcf15e01da34e4d3 -->

When you state how something works, the skill checks the code and points out any contradiction. *"Your code cancels entire Orders, but you just said partial cancellation is possible, which is right?"* The skill makes the language and the code agree, out loud, before it changes either.

<!-- zh-CN:begin 6f8689e47365dc9f -->

你陈述行为时，技能检查代码并指出矛盾：*“代码取消整个订单，但你刚说可部分取消，哪个对？”* 在改动任一方前，让语言与代码明确一致。

<!-- zh-CN:end 6f8689e47365dc9f -->

It cross-references **code** and the committed `GLOSSARY.md` and ADRs, and nothing else. It does not search your issue tracker. If your team argued out a naming collision and settled it in a closed issue months ago, the skill raises it again as if it were new. There is [an open request](https://github.com/mattpocock/skills/issues/717) to fix this. Until then, the workaround is to put the instruction in your own `docs/agents/domain.md`, which the skills already read.

<!-- zh-CN:begin c155920112dd0d42 -->

只交叉引用**代码**、已提交 `GLOSSARY.md` 和 ADR，不搜索议题跟踪器。团队数月前在关闭议题解决命名冲突时，它会重新提出。[已有开放请求](https://github.com/mattpocock/skills/issues/717)；临时做法是写入技能已读取的 `docs/agents/domain.md`。

<!-- zh-CN:end c155920112dd0d42 -->

## Common questions

<!-- zh-CN:begin 0024d7fba92b9c07 -->

## 常见问题

<!-- zh-CN:end 0024d7fba92b9c07 -->

**My `GLOSSARY.md` is 500 lines. 1,000. 3,000. What do I do?**
The size is a symptom. The cause is that the file has taken in implementation detail and decisions that never belonged in a glossary. The fix is a direct instruction: `/grill-with-docs make my GLOSSARY.md more concise and remove any implementation details from it`. Run it against a bloated file and most of it goes. Only split it with a `GLOSSARY-MAP.md` once the file is lean and still covers two domains that a reader would not want to hold at once. Splitting a bloated file gives you several bloated files. The skill's guidance here is not yet strong enough to prevent the growth in the first place, and the issue tracking that is still open.

<!-- zh-CN:begin caadd2369c09119c -->

**术语表 500、1000、3000 行怎么办？**
大小是症状；原因是写入实现细节和不属于术语表的决策。直接指示：`/grill-with-docs make my GLOSSARY.md more concise and remove any implementation details from it`，多数膨胀内容会删除。只有精简后仍覆盖两个读时不宜同时持有的领域，才用 `GLOSSARY-MAP.md` 拆分；拆膨胀文件只会得到多个膨胀文件。技能尚未足够防止最初增长，议题仍开放；其中相关的字段或标识包括 `GLOSSARY.md`。

<!-- zh-CN:end caadd2369c09119c -->

**Why is it `GLOSSARY.md` and not `CONTEXT.md`?**
It was `CONTEXT.md` (and `CONTEXT-MAP.md`) until 1.3.0. The file is a glossary and nothing else, so `GLOSSARY.md` says so, and, as one reader put it, "with ai agents everything is [context](https://www.aihero.dev/ai-coding-dictionary/context)". If your repo still has a `CONTEXT.md`, re-run `/setup-matt-pocock-skills`: it offers to `git mv` the file and update `docs/agents/domain.md`. Every skill in the set looks for `GLOSSARY.md`, so keeping the old name means patching all of them.

<!-- zh-CN:begin 780e9e81bfa897e8 -->

**为什么是 `GLOSSARY.md` 而不是 `CONTEXT.md`？**
1.3.0 前名为 `CONTEXT.md`（及 `CONTEXT-MAP.md`）。文件只是术语表，因此改名；有读者说“有了 AI 代理，一切皆为[上下文](https://www.aihero.dev/ai-coding-dictionary/context)”。若仍有 `CONTEXT.md`，重跑 `/setup-matt-pocock-skills`，可选择 `git mv` 并更新 `docs/agents/domain.md`。所有技能查找 `GLOSSARY.md`，保留旧名需逐个修改；其中相关的字段或标识包括 `GLOSSARY.md`。

<!-- zh-CN:end 780e9e81bfa897e8 -->

**Where did `/ubiquitous-language` go?**
It was removed, and it was not deprecated. Its job moved into `domain-modeling`, which maintains the whole model continuously rather than dumping a glossary out of one conversation. Vocabulary enforcement now matters more, not less. It runs underneath grilling, triage and mapping rather than as a separate pass you have to remember.

<!-- zh-CN:begin 9516574f2817980d -->

**`/ubiquitous-language` 去哪了？**
已移除而非废弃。职责移入 `domain-modeling`，持续维护整体模型，而非从单次对话倾倒术语。词汇约束更重要，并在追问、分诊和映射下层运行。

<!-- zh-CN:end 9516574f2817980d -->

**How do I get a glossary for a codebase that has none?**
Ask for it explicitly rather than waiting for it to accumulate. `/grill-with-docs help me scaffold my existing repo with a GLOSSARY.md` is the documented route. Expect a long interrogation. One user reported more than 50 questions before the file was in shape. Incidental use builds the glossary far too slowly on a brownfield repo.

<!-- zh-CN:begin de1866dd23af5f54 -->

**没有术语表的代码库如何建立？**
明确请求，不等待积累：`/grill-with-docs help me scaffold my existing repo with a GLOSSARY.md`。预期长时间审问，一用户报告 50 多问。棕地仓库偶发使用积累太慢。

<!-- zh-CN:end de1866dd23af5f54 -->

**Can I keep the domain model and use my own ADR format?**
Not cleanly today. The glossary half and the ADR half ship in one skill, so a team with an established ADR convention (different template, different location, different naming) gets instructions that conflict with its house style. The current options are to copy the skill locally and edit it, or to override the ADR conventions in your repo's own agent docs. Splitting the two apart is [an open request](https://github.com/mattpocock/skills/issues/557).

<!-- zh-CN:begin ae97756f0c09f1e0 -->

**能保留领域模型并使用自己的 ADR 格式吗？**
目前不能干净做到。术语与 ADR 同技能，已采用自有模板/位置/命名的团队会冲突。可本地复制技能修改，或在仓库代理文档覆盖 ADR 约定。拆分已提出（[#557](https://github.com/mattpocock/skills/issues/557)）。

<!-- zh-CN:end ae97756f0c09f1e0 -->

**Does a glossary actually earn its keep? It is one more artifact to review, and it can go stale.**
Sometimes it does not. DDD gets less useful the closer it gets to the implementation. The payoff is upstream, in naming and concept alignment, not in aggregates and layer ceremony. Synonym control matters at naming boundaries: module names, table names, status enums, issue titles, CLI commands. It matters much less in ordinary prose. There is also an objection that domain terms compress communication *between humans* who already share them, and that an agent responds the same way to the plain-English description. On that reading, the glossary's value is keeping you and your reviewers aligned with what the agent is doing, not making the agent better. On a one-day build, skip it. And an unreviewed, agent-authored glossary is worse than none: it fills with confident claims that later sessions treat as true.

<!-- zh-CN:begin 465e454acd6e9a61 -->

**术语表值得维护吗？多一个产物且会过期。**
有时不值得。DDD 越接近实现越不有用；收益在上游命名与概念对齐，不在聚合与分层仪式。同义控制适合命名边界：模块、表、状态枚举、议题标题、CLI 命令；普通文字中较少。也有人说领域词压缩的是已共享词汇的人类沟通，代理对平实说明反应相同。因此其价值可能是让你与审查者理解代理行为，而非让代理更好。一天内构建可跳过。未经审阅、代理生成的术语表比没有更糟：自信断言会被后续会话当成事实。

<!-- zh-CN:end 465e454acd6e9a61 -->

**Can it turn my vague prompts into domain language for me?**
No, and there is no plan for a skill that does. A domain language you do not understand yourself is meaningless once written down. This skill enforces precision once you have the understanding; it does not invent vocabulary you do not have. The related trap is using domain words without doing the modelling. The right nouns on top of the wrong concepts produce output that reads as correct and is not.

<!-- zh-CN:begin 2f071781e3ef346e -->

**能把含糊提示自动变成领域语言吗？**
不能，也无计划。自己不理解的领域语言写下来无意义。技能在已有理解上强化精确性，不发明词汇。相关陷阱是用了领域词却未建模；正确名词套在错误概念上，输出看似正确实则错误。

<!-- zh-CN:end 2f071781e3ef346e -->

## It's working if

<!-- zh-CN:begin 4a09866c4f1a7e98 -->

## 怎样算正常工作

<!-- zh-CN:end 4a09866c4f1a7e98 -->

- It stops you mid-sentence to ask which of two things you meant, instead of picking one and moving on.

<!-- zh-CN:begin 672efd0c9a8225e8 -->

- 在句子中停下问两个意思哪个正确，而非自选一个继续。

<!-- zh-CN:end 672efd0c9a8225e8 -->
- `GLOSSARY.md` changes **during** the conversation, not in a burst at the end.

<!-- zh-CN:begin f2e94acfb743bd8b -->

- `GLOSSARY.md` 在对话**期间**变化，不是末尾爆发。

<!-- zh-CN:end f2e94acfb743bd8b -->
- It refuses to write an ADR for something you could undo tomorrow, and says which of the three tests failed.

<!-- zh-CN:begin 748a22cc417ed2e6 -->

- 拒绝为明天可撤销事项写 ADR，并说明三项测试哪项未过。

<!-- zh-CN:end 748a22cc417ed2e6 -->
- New entries define what a thing *is* in one or two sentences and name the words you are giving up under `_Avoid_`.

<!-- zh-CN:begin fdca705d7eaf3d37 -->

- 新条目用一两句说明事物是什么，并在 `_Avoid_` 列出放弃的词。

<!-- zh-CN:end fdca705d7eaf3d37 -->
- It quotes your code back at you when your code and your sentence disagree.

<!-- zh-CN:begin e27b9672ff55cb09 -->

- 代码与陈述不一致时引用代码。

<!-- zh-CN:end e27b9672ff55cb09 -->
- `GLOSSARY.md` gets shorter as often as it gets longer.

<!-- zh-CN:begin 7c713d070e86cbc8 -->

- 术语表缩短的次数和增长的次数相当；其中相关的字段或标识包括 `GLOSSARY.md`。

<!-- zh-CN:end 7c713d070e86cbc8 -->

## Where it fits

<!-- zh-CN:begin a4c337b774019ca9 -->

## 适用范围

<!-- zh-CN:end a4c337b774019ca9 -->

`domain-modeling` is a **model-invoked reference** that runs *underneath* other skills more often than it runs on its own. [grill-with-docs](https://aihero.dev/skills-grill-with-docs) drives it through a grilling session, [wayfinder](https://aihero.dev/skills-wayfinder) loads it while charting a map, [triage](https://aihero.dev/skills-triage) uses it to keep [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) in the project's own words, and [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) calls it as decisions settle. Its closest sibling is [codebase-design](https://aihero.dev/skills-codebase-design). Together they are the vocabulary layer under everything else, this one for the *domain*, that one for the module's *shape*. It is also reachable directly, when you want the discipline without committing to the steps of whatever skill would normally load it. When you are unsure which skill fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 423643f192f6b477 -->

`domain-modeling` 是**模型调用参考**，更多运行在其他技能*之下*。[grill-with-docs](https://aihero.dev/skills-grill-with-docs) 通过追问驱动；[wayfinder](https://aihero.dev/skills-wayfinder) 绘图时加载；[triage](https://aihero.dev/skills-triage) 保持[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)使用项目语言；[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 在决定形成时调用。最邻近的是 [codebase-design](https://aihero.dev/skills-codebase-design)：二者构成底层词汇层，本技能负责*领域*，后者负责模块*形状*。无需常规加载它时也可直接调用。不确定时 [ask-matt](https://aihero.dev/skills-ask-matt) 路由。

<!-- zh-CN:end 423643f192f6b477 -->
