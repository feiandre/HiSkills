## What it does

<!-- zh-CN:begin 2ebef7c1e4f9f0a4 -->

## 它做什么

<!-- zh-CN:end 2ebef7c1e4f9f0a4 -->

`to-tickets` takes a plan, a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), or the conversation you are in, and breaks it into a set of **[tickets](https://www.aihero.dev/ai-coding-dictionary/ticket)** on your issue tracker. Each ticket declares its **blocking edges**: the other tickets that have to finish before it can start.

<!-- zh-CN:begin 8d208b209b9861ac -->

`to-tickets` 把计划、[规格](https://www.aihero.dev/ai-coding-dictionary/spec)或当前对话拆成跟踪器中的一组**[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)**。每张声明**阻塞依赖边**：开始前必须完成的工单。

<!-- zh-CN:end 8d208b209b9861ac -->

Every ticket is a **tracer bullet**: a narrow but complete path through every layer of the change (schema, API, UI, tests) that you can demo on its own as soon as it lands. This is what makes the skill different from the obvious way to split work, which is to cut one layer at a time and integrate at the end. It also sizes each ticket to fit in a single fresh [context window](https://www.aihero.dev/ai-coding-dictionary/context-window), because a [session](https://www.aihero.dev/ai-coding-dictionary/session) that has never seen your spec will pick the ticket up.

<!-- zh-CN:begin 13959a351be58318 -->

每张都是**曳光弹**：贯穿模式、API、UI、测试全部层面的窄而完整路径，落地即可演示。它不同于逐层切分最后集成的做法，每张也控制在一个全新[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)，因为接手[会话](https://www.aihero.dev/ai-coding-dictionary/session)未见规格。

<!-- zh-CN:end 13959a351be58318 -->

## When to reach for it

<!-- zh-CN:begin 1334563e3894de4b -->

## 何时使用

<!-- zh-CN:end 1334563e3894de4b -->

You invoke this by typing `/to-tickets`. The [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own.

<!-- zh-CN:begin c7470dbb8f20b566 -->

输入 `/to-tickets`；[代理](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。

<!-- zh-CN:end c7470dbb8f20b566 -->

| Where you are | What to run |
| --- | --- |
| You have a spec issue and the build spans several sessions | `/to-tickets`, or `/to-tickets #<spec_issue>` |
| The plan is only in the conversation, never written up | `/to-tickets` reads the thread directly, no spec needed |
| The whole change fits in one context window | [implement](https://aihero.dev/skills-implement), skip the tickets |
| Nothing is decided yet | [grill-with-docs](https://aihero.dev/skills-grill-with-docs), then [to-spec](https://aihero.dev/skills-to-spec) |
| A [wayfinder](https://aihero.dev/skills-wayfinder) map has cleared | [to-spec](https://aihero.dev/skills-to-spec) first, to collapse the map, then `/to-tickets` |

<!-- zh-CN:begin 3e5e80dce8eb41eb -->

| 当前状态 | 操作 |
| --- | --- |
| 有规格议题，构建跨多会话 | `/to-tickets` 或 `/to-tickets #<spec_issue>` |
| 计划只在对话中，未成文 | `/to-tickets` 直接读线程，无需规格 |
| 整个改动能装进一个上下文窗口 | [implement](https://aihero.dev/skills-implement)，跳过工单 |
| 尚未确定 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，再 [to-spec](https://aihero.dev/skills-to-spec) |
| [wayfinder](https://aihero.dev/skills-wayfinder) 地图已清理 | 先用 [to-spec](https://aihero.dev/skills-to-spec) 收敛，再 `/to-tickets` |

<!-- zh-CN:end 3e5e80dce8eb41eb -->

Tickets that `to-tickets` produced are agent-ready by construction. Don't run [triage](https://aihero.dev/skills-triage) over them. Triage is for work that arrived from someone else.

<!-- zh-CN:begin 3ee7c6856f32935b -->

它生成的工单天然可供代理执行。不要运行 [triage](https://aihero.dev/skills-triage)；分诊用于他人输入；其中相关的字段或标识包括 `to-tickets`。

<!-- zh-CN:end 3ee7c6856f32935b -->

## Prerequisites

<!-- zh-CN:begin 8c45e8b560b1f69c -->

## 前提

<!-- zh-CN:end 8c45e8b560b1f69c -->

`to-tickets` publishes into a tracker, so [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) must have configured one for this repo, along with the triage-label vocabulary. Either kind works: a real tracker like GitHub or Linear, or local markdown files under `.scratch/`, which work with no extra setup.

<!-- zh-CN:begin e00a81838639e139 -->

`to-tickets` 发布到跟踪器，因此 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 必须为本仓库配置跟踪器及分诊标签词汇。GitHub/Linear 或 `.scratch/` 本地 Markdown 均可，后者无需额外设置。

<!-- zh-CN:end e00a81838639e139 -->

## Tracer bullets, not layers

<!-- zh-CN:begin a8ce5e224a322201 -->

## 曳光弹而非分层

<!-- zh-CN:end a8ce5e224a322201 -->

A **horizontal** slice ships one layer of the change. Nothing works until every layer has landed, and each ticket's acceptance criteria have to reach into work that another ticket owns. A **vertical** slice (the tracer bullet) ships one thin path through all the layers at once, so it is verifiable alone and owns everything it grades.

<!-- zh-CN:begin b54ae07018476b1b -->

**水平**切片一次发布一层：全部层落地前不可用，验收还要碰其他工单工作。**纵向**切片一次贯穿所有层，可单独验证并拥有全部评分内容。

<!-- zh-CN:end b54ae07018476b1b -->

This is the rule people break most often. One team ran a 26-ticket stack sliced by layer (corpus, producer, aggregator, selector) and got roughly twenty agent runs per closed ticket, about three quarters of them rework. Their own post-mortem traced every failure class back to the horizontal slicing rather than to the implementations.

<!-- zh-CN:begin 854c96f717148d71 -->

这是最常被破坏的规则。一团队用 26 张按层切片工单，每关闭一张约二十次代理运行，约四分之三重做；复盘将失败归因分层而非实现。

<!-- zh-CN:end 854c96f717148d71 -->

Two things happen before anything is published. `to-tickets` looks for prefactoring (the principle "make the change easy, then make the easy change") and orders that work first. Then it presents the breakdown as a numbered list and quizzes you on it: is the granularity right, are the blocking edges real, should anything merge or split. Nothing reaches the tracker until you approve, and that quiz is the place to push back.

<!-- zh-CN:begin 722719e667cb8088 -->

发布前先找预重构（原则“先让改动容易，再做容易的改动”）并优先排序；然后编号展示拆分并审问：粒度、阻塞边、合并拆分。你批准前不写跟踪器，此步用于反馈；其中相关的字段或标识包括 `to-tickets`。

<!-- zh-CN:end 722719e667cb8088 -->

## Blocking edges

<!-- zh-CN:begin f68de463bacece23 -->

## 阻塞依赖边

<!-- zh-CN:end f68de463bacece23 -->

The edges are the point of the artifact. They work in two ways, depending on the tracker:

<!-- zh-CN:begin 8972766732868cc9 -->

边是产物核心，按跟踪器两种方式体现：

<!-- zh-CN:end 8972766732868cc9 -->

| Tracker | Where the edges live | How you work them |
| --- | --- | --- |
| Local markdown | Text in one file per ticket under `.scratch/<feature>/issues/<NN>-<slug>.md`, numbered blockers-first | Top to bottom, by hand |
| A real tracker (GitHub, Linear) | Native blocking links, or sub-issues where the tracker has them | Any ticket whose blockers are done is on the **frontier** and can be grabbed |

<!-- zh-CN:begin 9d35a70b03536477 -->

| 跟踪器 | 边的位置 | 如何工作 |
| --- | --- | --- |
| 本地 Markdown | `.scratch/<feature>/issues/<NN>-<slug>.md` 每工单文本，阻塞者优先编号 | 手动从上到下 |
| 真实跟踪器（GitHub、Linear） | 原生阻塞链接，或子议题 | 阻塞项完成的工单进入**前沿**可领取 |

<!-- zh-CN:end 9d35a70b03536477 -->

The edges live in the ticket either way. The tracker only decides whether anything can act on them in parallel. `to-tickets` produces the artifact; running it (one session at a time, or a fleet) is your job, not the skill's.

<!-- zh-CN:begin 9b91163d304e2737 -->

依赖始终在工单中；媒介只决定是否并行处理。`to-tickets` 只生成产物，运行（逐会话或群组）是你的职责。

<!-- zh-CN:end 9b91163d304e2737 -->

## The wide-refactor exception

<!-- zh-CN:begin 446940736eb75282 -->

## 广泛重构例外

<!-- zh-CN:end 446940736eb75282 -->

One shape breaks the tracer-bullet rule. A **wide refactor** is a single mechanical change (rename a column, retype a shared symbol) whose **blast radius** covers the whole codebase. One edit breaks thousands of call sites, so no vertical slice can land green.

<!-- zh-CN:begin a8f6723cf96731c4 -->

一种形状破坏规则：**广泛重构**是单一机械改动（改列名、共享符号重定型），**影响范围**覆盖全库，一次破坏数千调用点，纵向切片不能独立通过。

<!-- zh-CN:end a8f6723cf96731c4 -->

`to-tickets` sequences that as **expand–contract** instead:

<!-- zh-CN:begin a3e3594ecdc29e3f -->

`to-tickets` 按**扩展—收缩**排序：

<!-- zh-CN:end a3e3594ecdc29e3f -->

- **Expand**: add the new form beside the old, so nothing breaks.

<!-- zh-CN:begin f90c2d7273e200c5 -->

- **扩展**：旧形式旁添加新形式，不破坏。

<!-- zh-CN:end f90c2d7273e200c5 -->
- **Migrate**: move call sites over in batches sized by blast radius (per package, per directory), one ticket per batch, each blocked by the expand. CI stays green because the old form still exists.

<!-- zh-CN:begin fa075b0efd2c9311 -->

- **迁移**：按影响范围分批迁移调用点（包/目录），每批一工单，均被扩展阻塞；旧形式尚在，CI 保持绿色。

<!-- zh-CN:end fa075b0efd2c9311 -->
- **Contract**: delete the old form once no caller remains, in a ticket blocked by every migrate batch.

<!-- zh-CN:begin 7a84977dba4e517b -->

- **收缩**：无调用者后删旧形式，被所有迁移批阻塞。

<!-- zh-CN:end 7a84977dba4e517b -->

Where even the batches can't stay green alone, they share an integration branch and all block a final integrate-and-verify ticket. CI only has to be green at that ticket.

<!-- zh-CN:begin c25b82081b77ab89 -->

批次也无法独立保持绿色时共享集成分支，全部阻塞最终集成验证工单；只有该工单须绿色。

<!-- zh-CN:end c25b82081b77ab89 -->

## Common questions

<!-- zh-CN:begin ca5936cd88bfdb5d -->

## 常见问题

<!-- zh-CN:end ca5936cd88bfdb5d -->

**It produced twelve tickets for a three-line change.**
Over-decomposition is the most reported problem with this skill, and many users see it. The [model](https://www.aihero.dev/ai-coding-dictionary/model) defaults to atomic units and loses the grouping that would make them meaningful. The quiz step is where you fix this. Ask it to merge tickets, and it will. There is also a lower limit. If the whole change fits in one context window, you don't need this skill at all. Go straight to [implement](https://aihero.dev/skills-implement).

<!-- zh-CN:begin 3d33249dfc6f92d6 -->

**三行改动生成十二张工单。**
过度拆分是最常报告问题。[模型](https://www.aihero.dev/ai-coding-dictionary/model)默认原子单位，丢失有意义的组合。在审问步骤要求合并。若改动能装入一个上下文窗口，完全无需此技能，直接用 [implement](https://aihero.dev/skills-implement)。

<!-- zh-CN:end 3d33249dfc6f92d6 -->

**The tickets came out one per layer: all the schema in one, all the API in another.**
This is the failure the vertical-slice rule is written against, and the skill still produces it sometimes. Catch it at the quiz step by asking one question per ticket: what can I demo when this is done? A ticket with no answer is a horizontal slice. Some people add a "demo path" line to each ticket for this reason, and report that it pushes the model toward vertical slices.

<!-- zh-CN:begin f6ef5a8ab29e8e33 -->

**每层一张，模式、API 分开。**
这是纵向规则防范的失败，仍偶尔出现。审问时每张问：完成时我能演示什么？答不出即水平切片。可在每张加工“演示路径”，通常推动模型采用纵向。

<!-- zh-CN:end f6ef5a8ab29e8e33 -->

**On GitHub the tickets weren't created as sub-issues of the spec issue.**
This was reported across a dozen runs and several models, [most fully in issue #554](https://github.com/mattpocock/skills/issues/554). Fixed: `to-tickets` now makes each ticket a sub-issue of its source issue, and the GitHub tracker template gives the command (`gh issue create --parent <n>`, `gh` 2.94+). Re-run [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) to refresh an older `docs/agents/issue-tracker.md`.

<!-- zh-CN:begin b5d58d1b44af4bec -->

**GitHub 上未创建为规格议题子议题。**
[议题 #554](https://github.com/mattpocock/skills/issues/554) 已记录。现已生成子议题；模板命令 `gh issue create --parent <n>`（`gh` 2.94+）。重跑 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 更新旧 `docs/agents/issue-tracker.md`；其中相关的字段或标识包括 `to-tickets`。

<!-- zh-CN:end b5d58d1b44af4bec -->

**"Blocked by" was written into the issue body instead of a real blocking link.**
This is the same kind of problem, [reported in issue #513](https://github.com/mattpocock/skills/issues/513), where the agent even stated that GitHub has no native blocking relationship at all. It does: `gh issue create --blocked-by 12,15`. Because the skill publishes blockers first, their numbers are always available at creation time. The body text is meant to be the fallback for trackers with no native edge, not the default. The ticket template now omits `## Blocked by` when the edges are native.

<!-- zh-CN:begin 173092d3faa02173 -->

**“Blocked by”写入正文而非真实链接。**
同类问题见[议题 #513](https://github.com/mattpocock/skills/issues/513)，代理甚至称 GitHub 无原生阻塞；实际 `gh issue create --blocked-by 12,15`。先发布阻塞者，创建时编号可用。正文回退仅用于无原生边的跟踪器；原生边时模板省略 `## Blocked by`。

<!-- zh-CN:end 173092d3faa02173 -->

**Where do the local tickets go? The v1.1 notes said a root-level `tickets.md`.**
They did, and that was a bug. A single shared file also caused race conditions when parallel agents wrote to it. Local mode now writes one file per ticket under `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, in dependency order, matching the layout the local tracker template already described. The `NN` prefix is a real ticket ID, so `/implement 03` works instead of retyping a long title.

<!-- zh-CN:begin 241a619f1baaa549 -->

**本地工单放哪？v1.1 说根 `tickets.md`。**
那是缺陷，共享文件并行写会竞态。本地模式现按依赖顺序每工单 `.scratch/<feature-slug>/issues/<NN>-<slug>.md`。`NN` 是真 ID，可用 `/implement 03`。

<!-- zh-CN:end 241a619f1baaa549 -->

**It kept truncating when it tried to read my spec.**
A very large spec can outgrow what a tracker issue serves back cleanly. There is no local copy to fall back on, so the agent spends [tool calls](https://www.aihero.dev/ai-coding-dictionary/tool-call) fetching chunks again and never reaches the end. Don't [clear](https://www.aihero.dev/ai-coding-dictionary/clearing) or [compact](https://www.aihero.dev/ai-coding-dictionary/compaction) between `/to-spec` and `/to-tickets`. Run them in the same context window and the agent never has to fetch the spec back.

<!-- zh-CN:begin 0347596901f9febc -->

**读取规格时一直截断。**
大规格可能超过议题返回能力，无本地副本，代理会耗费[工具调用](https://www.aihero.dev/ai-coding-dictionary/tool-call)反复取块。`/to-spec` 与 `/to-tickets` 之间不要[清理](https://www.aihero.dev/ai-coding-dictionary/clearing)或[压缩](https://www.aihero.dev/ai-coding-dictionary/compaction)，同上下文运行即可。

<!-- zh-CN:end 0347596901f9febc -->

**The acceptance criteria graded nothing: some passed before any work was done.**
The template asks for criteria and says nothing about whether they can fail, so this happens. Three shapes recur: a criterion already true at the base commit, a criterion that only work in another ticket can satisfy, and one that restates the request rather than deriving from the artifact. Vertical slicing prevents most of it, because a slice that delivers new behaviour fails at the base commit by construction. The check is still worth doing by hand. For each criterion, name the observation that would show it false, and confirm it fails at the commit the implementer starts from.

<!-- zh-CN:begin 21debfa981dfa4f1 -->

**验收标准评分无意义，工作前就通过。**
模板未要求能失败。常见三种：基础提交已满足、依赖其他工单、复述请求而非由产物推导。纵向切片能防止多数；仍应手查：为每项指出失败观察，并确认实施起点失败。

<!-- zh-CN:end 21debfa981dfa4f1 -->

**The tickets are published. How do I actually run them?**
The skill stops at the artifact, and there is no auto-dispatch mode. Dispatch is manual: look at the board, count the tickets with no open blockers, and open that many agent sessions. Give each ticket a fresh context, and clear between them. [implement](https://aihero.dev/skills-implement) does not reliably close or check off the ticket when it finishes, on GitHub or in local markdown, so you update the ticket's state yourself.

<!-- zh-CN:begin 23517b7618971e5a -->

**工单发布后如何运行？**
技能只到产物，无自动派发。人工看板，统计无未完成阻塞的工单，开同一数量会话说，逐项全新上下文并清理。 [implement](https://aihero.dev/skills-implement) 完成时不可靠地关闭/勾选，需手动更新状态。

<!-- zh-CN:end 23517b7618971e5a -->

## It's working if

<!-- zh-CN:begin 839887465497da73 -->

## 怎样算正常工作

<!-- zh-CN:end 839887465497da73 -->

- Every ticket has an answer to "what can I demo when this is done?", and the answer is behaviour, not a layer.

<!-- zh-CN:begin 5478dae1e49fe28e -->

- 每张能回答“完成时可演示什么”，答案是行为而非层。

<!-- zh-CN:end 5478dae1e49fe28e -->
- The list comes back to you numbered, with a "Blocked by" line on each, before anything is published.

<!-- zh-CN:begin 77203db47a8c132a -->

- 发布前编号返回，每张有“Blocked by”。

<!-- zh-CN:end 77203db47a8c132a -->
- The ticket at the top has no blockers and can be started immediately.

<!-- zh-CN:begin 1821ec35fdbb1e1c -->

- 首张无阻塞，可立即开始。

<!-- zh-CN:end 1821ec35fdbb1e1c -->
- Nothing in a ticket body is a file path or a line number, except a snippet a prototype produced.

<!-- zh-CN:begin f672bb28d1b53114 -->

- 正文无路径或行号，原型片段除外。

<!-- zh-CN:end f672bb28d1b53114 -->
- Each ticket reads like something a fresh session could finish without you in the room.

<!-- zh-CN:begin 53393d1de908b3ac -->

- 新会话无需你在场可完成。

<!-- zh-CN:end 53393d1de908b3ac -->
- Prefactoring, where it found any, is at the front of the order rather than mixed into feature tickets.

<!-- zh-CN:begin 78da57620ec150f1 -->

- 预重构在最前，不混入功能工单。

<!-- zh-CN:end 78da57620ec150f1 -->

## Where it fits

<!-- zh-CN:begin fa120a722e979013 -->

## 适用范围

<!-- zh-CN:end fa120a722e979013 -->

`to-tickets` is a step in the main build chain:

<!-- zh-CN:begin a190c5ace7a4c73c -->

`to-tickets` 位于主构建链：

<!-- zh-CN:end a190c5ace7a4c73c -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

<!-- zh-CN:begin be5821cecee2b79c -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
# 主链：追问文档 → 规格 → 工单 → 实现 → 审查 → 回顾
```

<!-- zh-CN:end be5821cecee2b79c -->

Upstream is [to-spec](https://aihero.dev/skills-to-spec), which hands it a settled spec to slice against. Keep both in one context window, with no clear between them. Downstream is [implement](https://aihero.dev/skills-implement), which builds one ticket per fresh session, driving [tdd](https://aihero.dev/skills-tdd) for the tests and closing with [code-review](https://aihero.dev/skills-code-review). [implement-spec](https://aihero.dev/skills-implement-spec) is the other way down. It reads the same blocking edges as a task graph and builds every ready ticket in parallel on one integration branch. When you're unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin ddd994f9c71b689a -->

上游 [to-spec](https://aihero.dev/skills-to-spec) 提供确定规格，二者应同一上下文且不清理。下游 [implement](https://aihero.dev/skills-implement) 每新会话一张，以 [tdd](https://aihero.dev/skills-tdd) 测试并用 [code-review](https://aihero.dev/skills-code-review) 收尾。[implement-spec](https://aihero.dev/skills-implement-spec) 把边当任务图并在一个集成分支并行构建就绪工单。不确定流程时 [ask-matt](https://aihero.dev/skills-ask-matt) 路由。

<!-- zh-CN:end ddd994f9c71b689a -->
