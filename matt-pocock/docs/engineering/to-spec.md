## What it does

<!-- zh-CN:begin 677f875c9e339682 -->

## 它的作用

<!-- zh-CN:end 677f875c9e339682 -->

`to-spec` turns the conversation you have just had into a **[spec](https://www.aihero.dev/ai-coding-dictionary/spec)**, and publishes it to your issue tracker as a single issue.

<!-- zh-CN:begin 769526618202fa6e -->

`to-spec` 将刚完成的对话转成**[规格](https://www.aihero.dev/ai-coding-dictionary/spec)**，并作为一个问题发布到问题跟踪器。

<!-- zh-CN:end 769526618202fa6e -->

It does not interview you. When you reach for it, the deciding is already done. So it synthesises what is known (from the thread, the codebase, your `GLOSSARY.md` and ADRs) and does not start a new round of questions. The spec records decisions you already made. It is not a place to make new ones.

<!-- zh-CN:begin 167d4fc8ecff5ab5 -->

它不访谈你。使用它时，决定已经完成。技能综合已知内容（来自对话线程、代码库、`GLOSSARY.md` 与 ADR），不开始新一轮问题。规格记录已经作出的决定，不是作新决定的地方。

<!-- zh-CN:end 167d4fc8ecff5ab5 -->

## When to reach for it

<!-- zh-CN:begin a048507821ee82b7 -->

## 何时使用

<!-- zh-CN:end a048507821ee82b7 -->

You invoke this by typing `/to-spec`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own.

<!-- zh-CN:begin e880842217500a2f -->

你通过输入 `/to-spec` 调用；[代理](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。

<!-- zh-CN:end e880842217500a2f -->

Reach for it when the build is too big for one agent [session](https://www.aihero.dev/ai-coding-dictionary/session) and must be split across several. That is the whole trigger:

<!-- zh-CN:begin 3c8a287503fb830f -->

构建大到一次代理[会话](https://www.aihero.dev/ai-coding-dictionary/session)容纳不下、必须拆成多次时使用。这就是全部触发条件：

<!-- zh-CN:end 3c8a287503fb830f -->

| Where you are | What to run |
| --- | --- |
| You haven't decided anything yet | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) first |
| Decided, and the work fits one [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) | [implement](https://aihero.dev/skills-implement): skip the spec |
| Decided, and the work spans several sessions | `/to-spec`, then [to-tickets](https://aihero.dev/skills-to-tickets) |
| A [wayfinder](https://aihero.dev/skills-wayfinder) map has cleared | `/to-spec #<map_issue>` |

<!-- zh-CN:begin f99d2ddc6dc05a07 -->

| 当前状态 | 应运行 |
| --- | --- |
| 尚未作任何决定 | 先运行 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 已决定，工作能装进一个[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window) | [implement](https://aihero.dev/skills-implement)：跳过规格 |
| 已决定，工作跨越多次会话 | `/to-spec`，然后 [to-tickets](https://aihero.dev/skills-to-tickets) |
| [wayfinder](https://aihero.dev/skills-wayfinder) 地图已理清 | `/to-spec #<map_issue>` |

<!-- zh-CN:end f99d2ddc6dc05a07 -->

## Prerequisites

<!-- zh-CN:begin d10a43aed7ec1a25 -->

## 前置条件

<!-- zh-CN:end d10a43aed7ec1a25 -->

`to-spec` publishes the spec as an issue, so [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) must first configure a tracker and the triage-label vocabulary for this repo. Either kind of tracker works: a real tracker like GitHub, or local markdown files under `.scratch/`, which work with no extra setup.

<!-- zh-CN:begin c2c3a03d6f414d3e -->

`to-spec` 将规格作为问题发布，因此 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 必须先为此仓库配置跟踪器及分诊标签词汇。两类跟踪器均可：GitHub 等真实跟踪器，或 `.scratch/` 下的本地 Markdown 文件，后者无需额外设置。

<!-- zh-CN:end c2c3a03d6f414d3e -->

## The spec is a decision record

<!-- zh-CN:begin ed793c8922ed7a68 -->

## 规格是决定记录

<!-- zh-CN:end ed793c8922ed7a68 -->

The spec exists because context windows end. You settled many things while [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling): the shape of the solution, the choices you argued through, and what you deliberately refused. All of that is in one conversation that you are about to clear. The spec keeps it.

<!-- zh-CN:begin b37c140df06ed6ee -->

规格存在是因为上下文窗口会结束。你在[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)中确定了很多事：解决方案形态、争辩过的选择、刻意拒绝的内容。这些都在一段你即将清空的对话里。规格保存它们。

<!-- zh-CN:end b37c140df06ed6ee -->

So the spec does not validate or decide anything. It records what you decided, in your project's own vocabulary, so a fresh session can pick up the work without you explaining it again. If the spec states something you never said, that is a defect.

<!-- zh-CN:begin 3d07a687580f188b -->

因此规格不验证或决定任何事情。它用项目自己的词汇记录你的决定，使新会话无需再次解释就能接力。规格若写了你从未说过的事，就是缺陷。

<!-- zh-CN:end 3d07a687580f188b -->

## Seams before prose

<!-- zh-CN:begin 00908b710d3e1e1d -->

## 先定接缝，再写正文

<!-- zh-CN:end 00908b710d3e1e1d -->

Before it writes anything, `to-spec` sketches the **seams** where the feature will be tested, and checks them with you. It prefers existing seams to new ones, and picks the highest seam it can. The ideal number of seams for a change is one.

<!-- zh-CN:begin 83223d260f48c424 -->

写任何内容前，`to-spec` 先草拟功能测试的**接缝**，与你核对。它偏好现有接缝，选择尽可能高的接缝。一次变更的理想接缝数量是一个。

<!-- zh-CN:end 83223d260f48c424 -->

Other skills use those agreed seams later. [tdd](https://aihero.dev/skills-tdd) works only at seams you agreed in advance. [code-review](https://aihero.dev/skills-code-review) reviews the diff against the spec, so a seam nobody agreed to shows up as a review finding. Both connections go through this document. That is why you should take the seam conversation seriously here, and not leave it for implementation.

<!-- zh-CN:begin 149daca37e7c7d27 -->

其他技能之后使用这些约定接缝。[tdd](https://aihero.dev/skills-tdd) 只在预先约定的接缝工作。[code-review](https://aihero.dev/skills-code-review) 依据规格审查差异，未约定的接缝会成为审查发现。两种连接都经过此文档。因此要在此认真处理接缝对话，不要留到实施阶段。

<!-- zh-CN:end 149daca37e7c7d27 -->

## Common questions

<!-- zh-CN:begin d589baa6f5207a2b -->

## 常见问题

<!-- zh-CN:end d589baa6f5207a2b -->

**Where did `/to-prd` go?**
It is this skill, renamed in v1.1. "Spec" is now the one term used throughout, and the old `to-prd` slug no longer works, so reinstall under the new name. The old vocabulary is replaced by the pair *spec* and *tickets*. The spec is the destination and the decisions that fix it. The [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) are the steps that get there. If you change direction, delete the unfinished tickets and keep the spec.

<!-- zh-CN:begin 25b5d2d61f295d34 -->

**`/to-prd` 去哪儿了？**
它就是本技能在 v1.1 更名后的内容。“规格”现为统一术语，旧 `to-prd` slug 不再可用，请按新名称重装。旧词汇由 *spec* 与 *tickets* 取代。规格是目的地及锁定目的地的决定，[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)是到达那里的步骤。方向改变时，删除未完成工单，保留规格。

<!-- zh-CN:end 25b5d2d61f295d34 -->

**Why does the spec get the `ready-for-agent` label? I don't want an agent implementing off it.**
The label means "no further triage needed": the document is complete enough for an agent to work from. It marks an input, not a work order. But [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) agents that poll for `ready-for-agent` cannot see that difference. They will try to build the whole spec in one run instead of picking up the ticket slices. This is the most-reported problem with the skill. Until it changes, exclude the parent spec explicitly in your AFK agent's prompt, or remove the label after `/to-tickets` has run.

<!-- zh-CN:begin e9bb6a8cdbcfdcc0 -->

**为什么规格带 `ready-for-agent` 标签？我不想代理据此实施。**
该标签表示“无需进一步分诊”：文档完整到代理能据此工作。它标记输入，不是工作指令。但轮询 `ready-for-agent` 的 [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) 代理看不出区别，会试图一次构建整份规格，而不是拾取工单切片。这是本技能报告最多的问题。改变前，请在 AFK 代理提示词中明确排除父规格，或在 `/to-tickets` 运行后移除标签。

<!-- zh-CN:end e9bb6a8cdbcfdcc0 -->

**Why not go straight from grilling to `/to-tickets` and skip the spec?**
Often you should. The spec is worth its step only on multi-session work. Its value is that the tickets are disposable and the spec is not. Each ticket is sized for one fresh context window and then gets deleted or closed, while the spec stays as the one place that records the reasoning behind them. On a single-session change, that gives you nothing, and you pay for an extra synthesis step where the [model](https://www.aihero.dev/ai-coding-dictionary/model) can drift. Go from grilling to `/implement`.

<!-- zh-CN:begin beb7fc02861e8f4d -->

**为什么不从追问直接到 `/to-tickets`，跳过规格？**
通常应该如此。只有多会话工作值得设置规格步骤。其价值在于工单可丢弃而规格不可：每张工单适配一个全新上下文窗口，随后删除或关闭；规格保留为记录其推理的唯一位置。单会话变更得不到价值，还要承担额外综合步骤并让[模型](https://www.aihero.dev/ai-coding-dictionary/model)漂移。此时从追问直接到 `/implement`。

<!-- zh-CN:end beb7fc02861e8f4d -->

**I just finished a wayfinder map. What do I feed it?**
Give it the main map issue, `/to-spec #<map_issue>`, not the individual decision tickets. [wayfinder](https://aihero.dev/skills-wayfinder) produces decisions spread across a map, not deliverables. `to-spec` collapses them into one document you can build from. If you loop the map straight into `/implement`, you lose that step.

<!-- zh-CN:begin aea03625ae231d82 -->

**刚完成 wayfinder 地图，应把什么交给它？**
给主地图问题，即 `/to-spec #<map_issue>`，不是各决策工单。[wayfinder](https://aihero.dev/skills-wayfinder) 产生的决定分散在地图中，不是交付物；`to-spec` 把它们收拢成一份可据此构建的文档。直接把地图投入 `/implement` 会丢掉这一步。

<!-- zh-CN:end aea03625ae231d82 -->

**Is the spec for me to review, or is it just for the agent?**
Mostly for the agent, and it reads that way: complete, dense, and full of references. Read the seams and the out-of-scope section. In those two places, a wrong decision is cheapest to catch now and most expensive to find later. People do complain about reading the whole thing, and there is no summary mode. But if the spec surprises you, the grilling was too shallow; the spec is not too long.

<!-- zh-CN:begin 798ac26c4bafcfc6 -->

**规格是供我审阅，还是仅供代理使用？**
主要供代理使用，读起来也是如此：完整、密集、引用很多。你应阅读接缝与范围外章节，因为错误决定在这里最容易尽早发现，拖到后来代价最大。有人抱怨要读全文，且没有摘要模式。但规格若让你意外，说明追问太浅；规格并不算太长。

<!-- zh-CN:end 798ac26c4bafcfc6 -->

**Do I keep the spec frozen once tickets start, or let the agent rewrite it?**
Nothing keeps it in sync. In practice it is a snapshot of what you knew at that moment, and it goes out of date the first time implementation teaches you something. Treat it as disposable after the work ships. Your `GLOSSARY.md` and ADRs are the files meant to last. If you learn something during implementation that should last, put it there, not in an edited spec.

<!-- zh-CN:begin e346729e451a1939 -->

**工单开始后应冻结规格，还是让代理重写？**
没有机制保持同步。实际它是当时知识的快照，实施第一次带来新知识时就过时。工作发布后可丢弃。`GLOSSARY.md` 和 ADR 才是应长期保留的文件。实施中学到长期知识，应放那里，而非编辑规格。

<!-- zh-CN:end e346729e451a1939 -->

**My work is a refactor or a module boundary, not a feature. Does the template fit?**
Less well, and this is a known limitation. The template relies heavily on user stories, which do not fit architectural work. You end up writing stories nobody asked for around decisions that are really about interfaces and invariants. Use the implementation-decisions and testing-decisions sections instead. Record the lasting architectural decisions as ADRs through [grill-with-docs](https://aihero.dev/skills-grill-with-docs), not in the spec.

<!-- zh-CN:begin 98ab9c4170c08685 -->

**我的工作是重构或模块边界，模板适合吗？**
适合度较低，这是已知限制。模板高度依赖用户故事，不适合架构工作；你会围绕真正关于接口与不变量的决定，编写没人要求的用户故事。改用实施决定与测试决定章节。长期架构决定通过 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 记录为 ADR，不写在规格中。

<!-- zh-CN:end 98ab9c4170c08685 -->

**Will it check the tracker for related work, or cite the ADRs it's respecting?**
No to both. It reads and follows the ADRs for the area it touches, but it does not link them. It also does not search the tracker for overlapping issues before it writes, so a spec can duplicate work that someone already filed, and nothing warns you. If the area is busy, search the tracker yourself first.

<!-- zh-CN:begin 31366da374c2a4a9 -->

**它会检查跟踪器中的相关工作，或引用遵守的 ADR 吗？**
两者都不会。它读取并遵守涉及区域的 ADR，却不链接它们；写入前也不搜索重叠问题，因此规格可能与已提交工作重复，且没有警告。区域繁忙时，先自行搜索跟踪器。

<!-- zh-CN:end 31366da374c2a4a9 -->

**`/to-tickets` couldn't read my spec: it kept truncating.**
A tracker issue may not return a very large spec in full, and there is no local copy to use instead. To fix this, do not [clear](https://www.aihero.dev/ai-coding-dictionary/clearing) or [compact](https://www.aihero.dev/ai-coding-dictionary/compaction) between `/to-spec` and `/to-tickets`. Run them in the same window, and `/to-tickets` never has to fetch the spec again.

<!-- zh-CN:begin 881ab182f269e678 -->

**`/to-tickets` 无法读取规格，总是被截断。**
跟踪器问题可能无法完整返回超长规格，也没有本地副本替代。解决办法是不要在 `/to-spec` 与 `/to-tickets` 之间[清空](https://www.aihero.dev/ai-coding-dictionary/clearing)或[压缩](https://www.aihero.dev/ai-coding-dictionary/compaction)。同一窗口运行，`/to-tickets` 就不必再次获取规格。

<!-- zh-CN:end 881ab182f269e678 -->

## It's working if

<!-- zh-CN:begin 60ae5b17729e7cc1 -->

## 正常工作的表现

<!-- zh-CN:end 60ae5b17729e7cc1 -->

- It starts writing instead of asking you a new round of questions.

<!-- zh-CN:begin 8c7fcf6ea1198b07 -->

- 它开始写作，而不是再问你一轮问题。

<!-- zh-CN:end 8c7fcf6ea1198b07 -->
- It shows you the seams before it writes, and proposes as few as it can.

<!-- zh-CN:begin 696c92179fda3cbc -->

- 写入前展示接缝，并尽可能少提议。

<!-- zh-CN:end 696c92179fda3cbc -->
- It uses your project's nouns, not generic product-management boilerplate.

<!-- zh-CN:begin ae6bb815f3c6e30b -->

- 使用项目名词，而不是通用产品管理套话。

<!-- zh-CN:end ae6bb815f3c6e30b -->
- You remember making every decision in it. It invented nothing to fill a section.

<!-- zh-CN:begin d4193e79b1d34afd -->

- 你记得其中每个决定，没有为填满章节而编造。

<!-- zh-CN:end d4193e79b1d34afd -->
- The out-of-scope section lists real things. The things you refused are usually the most useful lines on the page.

<!-- zh-CN:begin f592e314d281f7b8 -->

- 范围外章节列出真实内容。你拒绝的事项通常是页面上最有用的行。

<!-- zh-CN:end f592e314d281f7b8 -->

## Where it fits

<!-- zh-CN:begin 4054ebeb0e7045bb -->

## 所处位置

<!-- zh-CN:end 4054ebeb0e7045bb -->

`to-spec` is a step in the main build chain, but only on the multi-session branch of it:

<!-- zh-CN:begin 39ab22277f8f3995 -->

`to-spec` 是主构建链的一步，但仅处于多会话分支：

<!-- zh-CN:end 39ab22277f8f3995 -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

Upstream, [grill-with-docs](https://aihero.dev/skills-grill-with-docs) makes the decisions that this skill only records, and a finished [wayfinder](https://aihero.dev/skills-wayfinder) map joins the chain here. Downstream, [to-tickets](https://aihero.dev/skills-to-tickets) cuts the spec into tracer-bullet tickets for [implement](https://aihero.dev/skills-implement) to build. When you're unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 3271d7706026bbdf -->

上游 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 作出本技能只负责记录的决定，完成后的 [wayfinder](https://aihero.dev/skills-wayfinder) 地图在此加入链条。下游 [to-tickets](https://aihero.dev/skills-to-tickets) 把规格切成曳光弹工单，供 [implement](https://aihero.dev/skills-implement) 构建。不确定哪个技能或流程适合时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。

<!-- zh-CN:end 3271d7706026bbdf -->
