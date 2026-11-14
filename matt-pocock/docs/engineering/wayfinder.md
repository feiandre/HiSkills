## What it does

<!-- zh-CN:begin 57dbf25e2222b637 -->

## 功能

<!-- zh-CN:end 57dbf25e2222b637 -->

`wayfinder` takes an effort too big for one agent [session](https://www.aihero.dev/ai-coding-dictionary/session). This is an idea whose **destination** you can name but whose route you cannot yet see. Wayfinder charts it as a shared **map** of **decision tickets** on your issue tracker, then resolves the tickets one at a time until the route is clear.

<!-- zh-CN:begin 6f854ed57e275a79 -->

`wayfinder` 处理单个代理[会话](https://www.aihero.dev/ai-coding-dictionary/session)容纳不下的工作：你能说出想法的**目的地**，却还看不清路线。Wayfinder 将它绘制成问题跟踪器上的共享**地图**，由**决策工单**组成，再逐个解决工单，直到路线清晰。

<!-- zh-CN:end 6f854ed57e275a79 -->

It plans and does not build. Every ticket asks a question, and the answer is a decision, not a slice of a build. The map is finished when nothing is left to decide before someone builds the thing. This rule separates a wayfinder ticket from an ordinary implementation [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket), and it is the rule agents break most often. When the map clears, wayfinder hands off and does not continue into code.

<!-- zh-CN:begin 306b8de2c8fcee23 -->

它负责规划，不负责构建。每个工单提出一个问题，答案是一项决策，而非一部分构建成果。当有人开始构建前再无待定事项，地图便完成了。这条规则区分 wayfinder 工单与普通实施[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)，也是代理最常违反的规则。地图清晰后，wayfinder 交接，不继续写代码。

<!-- zh-CN:end 306b8de2c8fcee23 -->

## When to reach for it

<!-- zh-CN:begin 7d28331f7aa7f68c -->

## 何时使用

<!-- zh-CN:end 7d28331f7aa7f68c -->

You invoke this by typing `/wayfinder`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own.

<!-- zh-CN:begin f3399136406238d5 -->

输入 `/wayfinder` 调用；[代理](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。

<!-- zh-CN:end f3399136406238d5 -->

It is the heaviest flow in the set, so the trigger is narrow. The effort must be larger than one agent session can hold, and the route to the destination must be unclear. The split is session count: `/grill-with-docs` for single-session planning, `/wayfinder` for multi-session planning.

<!-- zh-CN:begin 66d0ab4b4a9cfc7b -->

这是整套工具中最重的流程，因此触发条件很窄：工作必须大到单个代理会话容纳不下，且通往目的地的路线尚不清晰。分界是会话数量：单会话规划用 `/grill-with-docs`，多会话规划用 `/wayfinder`。

<!-- zh-CN:end 66d0ab4b4a9cfc7b -->

| What you have in front of you | What to run |
| --- | --- |
| A well-scoped feature you can settle in one sitting | [grill-me](https://aihero.dev/skills-grill-me), or [grill-with-docs](https://aihero.dev/skills-grill-with-docs) when there is a codebase |
| A greenfield project, or a build spanning many sessions, with the route still unclear | `/wayfinder` |
| A thread where the deciding is already done | [to-spec](https://aihero.dev/skills-to-spec): skip straight past the map |
| A cleared wayfinder map | [to-spec](https://aihero.dev/skills-to-spec), then [to-tickets](https://aihero.dev/skills-to-tickets) and [implement](https://aihero.dev/skills-implement) |
| An existing session that has already grown too big | say "hand off to `/wayfinder`" ([handoff](https://aihero.dev/skills-handoff) bridges into a map as well as out of one) |

<!-- zh-CN:begin 0a011b63c1cdd4ac -->

| 当前情况 | 运行什么 |
| --- | --- |
| 范围明确、一次讨论就能敲定的功能 | [grill-me](https://aihero.dev/skills-grill-me)，有代码库时用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 全新项目，或横跨许多会话且路线仍不清晰的构建 | `/wayfinder` |
| 决策已经完成的聊天 | [to-spec](https://aihero.dev/skills-to-spec)：直接跳过地图 |
| 已清晰的 wayfinder 地图 | [to-spec](https://aihero.dev/skills-to-spec)，然后 [to-tickets](https://aihero.dev/skills-to-tickets) 和 [implement](https://aihero.dev/skills-implement) |
| 已经膨胀得过大的现有会话 | 说“交接给 `/wayfinder`”（[handoff](https://aihero.dev/skills-handoff) 既能从地图交接出去，也能交接进地图） |

<!-- zh-CN:end 0a011b63c1cdd4ac -->

Greenfield is not a requirement. People use wayfinder routinely on legacy and half-built codebases, and it can be more useful there, because much of the fog is "what is already true here" rather than "what should we do".

<!-- zh-CN:begin 0e529983169694e3 -->

不要求从零开始。人们经常在遗留和半成品代码库中使用 wayfinder，而且那里可能更有用，因为大量迷雾是“这里已经有哪些事实”，而非“我们应该做什么”。

<!-- zh-CN:end 0e529983169694e3 -->

## Prerequisites

<!-- zh-CN:begin 6539bd9b66ee4736 -->

## 前提条件

<!-- zh-CN:end 6539bd9b66ee4736 -->

The map and its tickets live on the repo's issue tracker, so wayfinder needs the tracker setup from [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills). That step writes a "Wayfinding operations" section. The section describes how to express the map, its child tickets, blocking edges, and frontier queries on GitHub, GitLab, or local markdown. Wayfinder finds that doc through the pointer in your `CLAUDE.md` / `AGENTS.md`, not at a fixed path. With no tracker configured, it falls back to local markdown files.

<!-- zh-CN:begin 00ce7caf234fbd0b -->

地图和工单位于仓库的问题跟踪器，因此 wayfinder 需要 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 提供的跟踪器设置。这一步写入“寻路操作”部分，描述如何在 GitHub、GitLab 或本地 Markdown 上表达地图、子工单、阻塞关系及前沿查询。Wayfinder 通过 `CLAUDE.md` / `AGENTS.md` 中的指针找到文档，不使用固定路径。未配置跟踪器时，回退到本地 Markdown 文件。

<!-- zh-CN:end 00ce7caf234fbd0b -->

The tracker does real work. Its native blocking links show the frontier in the tracker's own UI. On a tracker without native dependency links (a self-hosted Gitea, say), wayfinder infers blockers from the map text. That works, but you must supervise it more closely.

<!-- zh-CN:begin 04af4f646e9cf965 -->

跟踪器确实发挥作用。其原生阻塞链接会在自己的 UI 中显示前沿。对于没有原生依赖链接的跟踪器（例如自托管 Gitea），wayfinder 从地图文字推断阻塞项。这样也能工作，但你必须更密切地监督。

<!-- zh-CN:end 04af4f646e9cf965 -->

## The map, the fog, and the frontier

<!-- zh-CN:begin d303f69f0b97d316 -->

## 地图、迷雾与前沿

<!-- zh-CN:end d303f69f0b97d316 -->

The **map** is a single issue labelled `wayfinder:map`, and its tickets are its child issues. It is an **index, not a store**. A decision lives in exactly one place, its ticket, and the map only gives a one-line summary and a link. A session loads the map at low resolution and opens individual tickets when it needs them. This lets a map keep growing without every session loading its whole history.

<!-- zh-CN:begin 46ead380d415fc16 -->

**地图**是一个标记为 `wayfinder:map` 的 issue，工单是它的子 issue。它是**索引，不是存储库**。一项决策只存在于一个地方，即其工单；地图只提供一行摘要和链接。会话以低分辨率加载地图，需要时打开具体工单。这使地图可以持续增长，而不用每次会话加载全部历史。

<!-- zh-CN:end 46ead380d415fc16 -->

The map has four sections:

<!-- zh-CN:begin 9650243cd67becc0 -->

地图有四个部分：

<!-- zh-CN:end 9650243cd67becc0 -->

- **Destination.** What the end of this map looks like. You name it first, before any ticket exists, because the destination fixes the scope you measure every ticket against.

<!-- zh-CN:begin 7b456a1cd135b6df -->

- **目的地。** 地图完成时的样子。任何工单出现前先命名目的地，因为它确定范围，所有工单都以此衡量。

<!-- zh-CN:end 7b456a1cd135b6df -->
- **Decisions so far.** One line per closed ticket, each with a link to where the detail lives.

<!-- zh-CN:begin a5d697c32e08b0e5 -->

- **迄今的决策。** 每个已关闭工单一行，附详情所在位置的链接。

<!-- zh-CN:end a5d697c32e08b0e5 -->
- **Not yet specified.** This is the **fog of war**: decisions you can tell are coming but cannot yet phrase sharply. The test for fog versus ticket is whether you can state the question precisely *now*, not whether you can answer it. When you resolve a ticket, the fog ahead of it clears, and anything you can now specify graduates into a new ticket.

<!-- zh-CN:begin 215dc85372a7955b -->

- **尚未明确。** 这是**战争迷雾**：你能预见将要面对、但还无法准确表述的决策。区分迷雾与工单的标准是你*现在*能否精确提出问题，而非能否回答。解决工单后，其前方迷雾消散，此时能明确的问题就升级为新工单。

<!-- zh-CN:end 215dc85372a7955b -->
- **Out of scope.** Work beyond the destination. Fog only gathers *toward* the destination, so out-of-scope work stays closed and never graduates.

<!-- zh-CN:begin e49a7f4cb96bab48 -->

- **范围之外。** 超出目的地的工作。迷雾只在*通往*目的地的方向聚集，因此范围外工作保持关闭，绝不升级。

<!-- zh-CN:end e49a7f4cb96bab48 -->

The **frontier** is the set of open, unblocked, unclaimed tickets (the edge of the known). A session claims a ticket by assigning it to itself before it does any work. The assignee *is* the claim, so concurrent sessions skip that ticket. Sessions refer to tickets by name, never by a bare `#42`, because a wall of issue numbers is hard to read in narration.

<!-- zh-CN:begin 127a4efa3ab8efef -->

**前沿**是开放、未阻塞且未被认领的工单集合（已知世界的边缘）。会话开始任何工作前，先把工单分配给自己以认领。受指派人*就是*认领标记，因此并发会话会跳过它。会话以名称指代工单，绝不只用 `#42`，因为叙述中堆满 issue 编号难以阅读。

<!-- zh-CN:end 127a4efa3ab8efef -->

## The four decision-ticket types

<!-- zh-CN:begin 89e505edfc9b8c81 -->

## 四种决策工单类型

<!-- zh-CN:end 89e505edfc9b8c81 -->

Every ticket carries a `wayfinder:<type>` label. Each ticket is either **[HITL](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop)** (worked with a human who speaks for themselves) or **[AFK](https://www.aihero.dev/ai-coding-dictionary/afk)** (driven by the agent alone). A HITL ticket resolves only through the live exchange. An agent that answers its own [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) questions has broken it.

<!-- zh-CN:begin 629f7d4cf1f4cda3 -->

每个工单带 `wayfinder:<type>` 标签。工单要么是 **[HITL](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop)**（与自行表达意见的人类协作），要么是 **[AFK](https://www.aihero.dev/ai-coding-dictionary/afk)**（仅由代理驱动）。HITL 工单只能通过实时交流解决。代理若自行回答自己的[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)，便违反了这一约定。

<!-- zh-CN:end 629f7d4cf1f4cda3 -->

| Type | Mode | Reach for it when | Resolved by |
| --- | --- | --- | --- |
| `grilling` | HITL | The default. The question can be settled by talking it through. | [grilling](https://aihero.dev/skills-grilling) plus [domain-modeling](https://aihero.dev/skills-domain-modeling), in a fresh session |
| `prototype` | HITL | "How should this look" or "how should this behave": a question talking cannot settle. | [prototype](https://aihero.dev/skills-prototype), with a link from the ticket to the built artifact |
| `research` | AFK | A fact outside the working directory is blocking a decision. | A [research](https://aihero.dev/skills-research) [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent), started when you chart the map and run in parallel on a `research/<name>` branch |
| `task` | Either | Nothing to decide, but manual work blocks a decision, such as provisioning access, signing up for a service, or moving data so you can see its shape. | The agent alone where it can, otherwise a precise checklist for the human |

<!-- zh-CN:begin 6cb3bfd66930dde9 -->

| 类型 | 模式 | 使用时机 | 解决方式 |
| --- | --- | --- | --- |
| `grilling` | HITL | 默认类型。通过充分讨论即可解决的问题。 | 全新会话中的 [grilling](https://aihero.dev/skills-grilling) 加 [domain-modeling](https://aihero.dev/skills-domain-modeling) |
| `prototype` | HITL | “应该长什么样”或“应该如何运行”：讨论无法解决的问题。 | [prototype](https://aihero.dev/skills-prototype)，工单链接到构建出的产物 |
| `research` | AFK | 工作目录之外的某个事实阻塞决策。 | 绘制地图时启动一个 [research](https://aihero.dev/skills-research) [子代理](https://www.aihero.dev/ai-coding-dictionary/subagent)，在 `research/<name>` 分支并行运行 |
| `task` | 均可 | 没有待决事项，但手动工作阻塞决策，例如开通访问权限、注册服务或移动数据以查看其形态。 | 代理能做的自行完成，否则给人类一份准确检查清单 |

<!-- zh-CN:end 6cb3bfd66930dde9 -->

`task` is the only type that *does* rather than decides. It belongs on the map only because it unblocks a decision, never because it delivers part of the destination. This type goes wrong most often in practice. Agents read it as an implementation step and start to write product code inside the map.

<!-- zh-CN:begin f26b9184b73a9ac1 -->

`task` 是唯一*做事*而非决策的类型。它出现在地图上，只因为能解除决策的阻塞，绝不是因为交付目的地的一部分。实践中这种类型最容易出错。代理会把它当成实施步骤，开始在地图内编写产品代码。

<!-- zh-CN:end f26b9184b73a9ac1 -->

Research is the only exception to *one ticket per session*.

<!-- zh-CN:begin 423974f099948b89 -->

研究是*每个会话一个工单*的唯一例外。

<!-- zh-CN:end 423974f099948b89 -->

## Common questions

<!-- zh-CN:begin 9c5aad90b19c8bd9 -->

## 常见问题

<!-- zh-CN:end 9c5aad90b19c8bd9 -->

**How is this different from `/grill-with-docs`? Which should I start with?**
Session count, not project size. `/grill-with-docs` is single-session planning; wayfinder is multi-session planning. If you can hold the whole thing in one conversation, grilling is cheaper and better, and wayfinder is slower and denser for that case. The community shorthand is that wayfinder only makes sense if the work does not fit into a single session. This is by far the most-asked wayfinder question. People keep asking it because the skill descriptions do not tell you where your own task sits on that line. You have to judge the session count yourself.

<!-- zh-CN:begin e6279079c5547fee -->

**这与 `/grill-with-docs` 有什么区别？应该从哪个开始？**
看会话数量，而非项目大小。`/grill-with-docs` 是单会话规划；wayfinder 是多会话规划。如果一次对话能容纳全部内容，追问更省、更好，此时 wayfinder 更慢、更繁重。社区的简明说法是，只有工作无法放进单个会话时，wayfinder 才有意义。这远远是最多人询问的问题。人们反复提问，是因为技能描述没有告诉你自己的任务处于分界线哪边。会话数量要自己判断。

<!-- zh-CN:end e6279079c5547fee -->

**When it asks for the "destination", does it mean the end of this session or the end of everything?**
The end of the whole map, not just the first session. The question reads ambiguously, but wayfinder is a multi-session tool by definition, so a session-scoped answer never makes sense. Typical destinations are a [spec](https://www.aihero.dev/ai-coding-dictionary/spec) to hand off, a decision to lock before planning starts, a proof of concept, or an in-place change such as a data migration.

<!-- zh-CN:begin 83bd60fa72b2c9de -->

**它问“目的地”时，指本次会话结束，还是所有工作结束？**
指整张地图的终点，而不只是第一次会话。问题措辞有歧义，但 wayfinder 按定义是多会话工具，因此把答案限定于一次会话从来不合理。典型目的地包括可交接的[规格](https://www.aihero.dev/ai-coding-dictionary/spec)、规划开始前需确定的决策、概念验证，或数据迁移等就地变更。

<!-- zh-CN:end 83bd60fa72b2c9de -->

**The map is cleared. Didn't wayfinder already write the spec and make the tickets? Why do I still need `/to-spec` and `/to-tickets`?**
No. Wayfinder's tickets are decision tickets, and by the time the map closes they are all closed too. What is left is a map full of linked decisions, which is not a build plan. [to-spec](https://aihero.dev/skills-to-spec) collapses those linked decisions into one spec (`/to-spec #<map_issue>`), and [to-tickets](https://aihero.dev/skills-to-tickets) slices that spec into tracer-bullet implementation tickets. If you loop the map straight into [implement](https://aihero.dev/skills-implement), you skip the collapse and lose the linked detail. Go straight to implementation only when the effort turned out small. Some people run the shorter pipeline and report that it works. The two extra steps give you an explicit spec that a reviewer or a colleague can read, which matters more when you do not work alone.

<!-- zh-CN:begin 0eb71d6429597972 -->

**地图已经清晰了。Wayfinder 不是已经写好规格、创建工单了吗？为什么还要 `/to-spec` 和 `/to-tickets`？**
并没有。Wayfinder 的工单是决策工单，地图关闭时它们也都关闭。剩下的是一张链接各种决策的地图，不是构建计划。[to-spec](https://aihero.dev/skills-to-spec) 把这些链接决策汇成一份规格（`/to-spec #<map_issue>`），[to-tickets](https://aihero.dev/skills-to-tickets) 再把规格切成曳光弹式实施工单。地图直接进入 [implement](https://aihero.dev/skills-implement)，会跳过汇总而丢失链接中的详情。只有工作最终证明很小时才直接实施。有些人采用较短流程并反馈有效。额外两步带来一份审查者或同事可阅读的明确规格，协作时尤其重要。

<!-- zh-CN:end 0eb71d6429597972 -->

**My agent started writing production code in the middle of a wayfinder session.**
This is the most-reported failure with this skill, and a real gap in the skill causes it. You can override wayfinder's "plan, don't do" default in the map's **Notes**. But the agent writes the Notes, so the constraint and its exemption live in a file that the constrained agent owns. One user watched an agent write "this map carries execution" into its own Notes. In later sessions the agent read that line back as permission and built on a live server. The skill has no hard stop for "I meant the default." Until it does, read the Notes on any map you did not chart yourself, keep implementation in separate sessions, and treat any `wayfinder:task` that looks like a slice of the build as mis-typed.

<!-- zh-CN:begin 94fc15a145969012 -->

**我的代理在 wayfinder 会话中途开始写生产代码了。**
这是该技能报告最多的失败，由技能本身的真实缺口造成。你可以在地图的 **Notes** 中覆盖 wayfinder“规划，不执行”的默认规则。但 Notes 由代理编写，因此约束与豁免位于受约束代理拥有的文件中。一位用户看到代理在自己的 Notes 中写下“此地图包含执行”。后续会话中，代理把它读成许可，在在线服务器上构建。技能对“我指的是默认规则”没有硬性阻止。在补上之前，阅读任何非自己绘制地图的 Notes，把实施放到独立会话，并把看起来像构建切片的任何 `wayfinder:task` 视为类型标错。

<!-- zh-CN:end 94fc15a145969012 -->

**I charted 27 tickets, and by the time I got to the thirteenth, the rest no longer made sense.**
This question is verbatim from a user report, and others report the same outcome. By default, wayfinder plans comprehensively. When later tickets rest on assumptions that earlier tickets invalidate, the map falls into the waterfall trap that critics accuse the skill of. Two things help. First, scope the map to a bounded destination, not to the whole product. Users report that maps scoped to one defined epic behave better than a sprawling "implement V1". The goal is to ship small increments, not to plan something very big. Second, [prototype](https://www.aihero.dev/ai-coding-dictionary/prototyping) aggressively. The route stays current because cheap concrete artifacts expose uncertainty before implementation depends on it. Wayfinder is "prototypemaxxing", not "planmaxxing".

<!-- zh-CN:begin b4900263d8ad2a58 -->

**我画了 27 个工单，做到第 13 个时，其余都不再有意义。**
这句话逐字来自用户报告，其他人也报告相同结果。默认情况下，wayfinder 会全面规划。后面的工单依赖的假设被前面工单推翻时，地图就落入批评者所说的瀑布式陷阱。两件事有帮助。首先，把地图限定在有界目的地，而非整个产品。用户反馈，针对一个明确定义史诗的地图，比庞杂的“实现 V1”更好。目标是交付小增量，而非规划巨物。其次，大量制作[原型](https://www.aihero.dev/ai-coding-dictionary/prototyping)。低成本具体产物在实施依赖不确定性之前将其暴露，使路线保持最新。Wayfinder 是“把原型做到极致”，不是“把规划做到极致”。

<!-- zh-CN:end b4900263d8ad2a58 -->

**Can I work several tickets in parallel?**
The frontier shows you which tickets you can take, and blocking edges make parallel work safe on paper. In practice, one ticket at a time is the safer default. If you work two grilling tickets at once, one session can ask you a question you just answered in the other, because the sessions share no [context](https://www.aihero.dev/ai-coding-dictionary/context). Prototype tickets have a known gap too. One user reported an agent that built three UI variations, chose one itself, and closed the ticket. That choice is yours, and the skill does not yet say so clearly enough. If you do run tickets in parallel, review the dependency graph yourself first.

<!-- zh-CN:begin 3ca3ed8309eaa9be -->

**可以并行处理几个工单吗？**
前沿显示可领取工单，阻塞关系在理论上保证并行安全。实践中，一次一个工单是更安全的默认选择。如果同时处理两个追问工单，一个会话可能问另一个会话刚回答的问题，因为会话之间不共享[上下文](https://www.aihero.dev/ai-coding-dictionary/context)。原型工单也有已知缺口：一位用户报告，代理构建三个 UI 变体，自己选择一个，然后关闭工单。选择权属于你，而技能还没有说得足够清楚。若确实并行，先亲自审查依赖图。

<!-- zh-CN:end 3ca3ed8309eaa9be -->

**Do I have to use GitHub Issues?**
No. Any issue tracker works. GitHub has the best support, because its native sub-issues and blocking relationships make the frontier visible without opening the map. People also use GitLab, Linear, Jira and local markdown. There are two caveats. On a tracker with no native blocking, wayfinder infers the dependency graph from text, and you must correct it by hand. Local markdown puts the artifacts in your repo, which is not recommended, because material stored in the repo tends to persist by accident. Open-source maintainers hit the opposite problem (public trackers fill up with agent-generated planning tickets) and often choose local markdown anyway.

<!-- zh-CN:begin 952c9f02ff7fc955 -->

**必须用 GitHub Issues 吗？**
不必，任何问题跟踪器都行。GitHub 支持最好，因为原生子 issue 和阻塞关系使你无需打开地图就能看到前沿。人们也使用 GitLab、Linear、Jira 和本地 Markdown。有两点注意：没有原生阻塞关系时，wayfinder 从文本推断依赖图，你必须手动纠正。本地 Markdown 把产物放进仓库，不建议这样做，因为仓库材料容易意外长期保留。开源维护者遇到相反问题（公共跟踪器充满代理生成的规划工单），因此仍常选择本地 Markdown。

<!-- zh-CN:end 952c9f02ff7fc955 -->

**The grilling is exhausting. Every question is three paragraphs long.**
This is the sharpest open complaint about wayfinder, and nobody has fixed it yet. One user broke it down this way: the verbosity itself causes decision exhaustion, and the length hides *why* the agent asks a question, so you lose the chain from decision to decision as the map grows. The verbosity looks like a property of the current set of [models](https://www.aihero.dev/ai-coding-dictionary/model) rather than of the skill. Users try two mitigations: a lower [reasoning effort](https://www.aihero.dev/ai-coding-dictionary/effort), and a plain-language instruction in your global `CLAUDE.md`. Expect to think hard here anyway. Wayfinder demands a lot of thinking from you, and that is most of its purpose, not a defect.

<!-- zh-CN:begin 0f716eeb092aecd3 -->

**追问让人筋疲力尽。每个问题都长达三段。**
这是目前最尖锐的未解决抱怨，尚无人修复。一位用户分析：冗长本身导致决策疲劳，长度又隐藏代理*为什么*提问，地图增长时便失去决策之间的联系。冗长看起来是当前一批[模型](https://www.aihero.dev/ai-coding-dictionary/model)的属性，而非技能属性。用户尝试两种缓解：降低[推理力度](https://www.aihero.dev/ai-coding-dictionary/effort)，以及在全局 `CLAUDE.md` 写入使用通俗语言的指令。无论如何，都应预期需要认真思考。Wayfinder 要求你投入大量思考，这大体正是其目的，不是缺陷。

<!-- zh-CN:end 0f716eeb092aecd3 -->

**A decision I already closed turned out to be wrong. Do I edit the old ticket or make a new one?**
There is no official guidance, and the agent's default is unhelpful. It tends to design around the bad decision instead of challenging it, so you must steer it yourself. What works is to tell wayfinder plainly what changed. It then updates the map, revises the affected tickets, and comments on the closed ones. You can recover from scope changes mid-map. But if you *designed* a map to change, that is a sign the scope is wrong.

<!-- zh-CN:begin 790f91809bf519f6 -->

**已经关闭的决策后来证明错了。应该改旧工单还是新建？**
没有官方指引，代理的默认做法也没有帮助。它倾向于围绕错误决策设计，而不是质疑，因此要由你引导。有效做法是明确告诉 wayfinder 哪些情况变了。它随后更新地图、修订受影响工单，并在已关闭工单上评论。地图中途改变范围可以恢复；但若你*有意设计*一张会改变的地图，就说明范围有问题。

<!-- zh-CN:end 790f91809bf519f6 -->

**Where did `decision-mapping` go?**
It is this skill. v1.1 renamed it to `wayfinder`, and you invoke it as `/wayfinder`. "Decision map" was jargon, and it was also inaccurate, because only one of the four ticket types is a decision by itself. The new name gave the skill one consistent vocabulary (destination, fog of war, frontier, the map) instead of an invented term on top. The unit kept the word "decision": a wayfinder ticket is a **decision ticket**, so that people do not read it as an implementation ticket.

<!-- zh-CN:begin 919d0cbc9c365405 -->

**`decision-mapping` 去哪了？**
它就是本技能。v1.1 将其重命名为 `wayfinder`，通过 `/wayfinder` 调用。“决策图”是术语，而且不准确，因为四种工单类型中只有一种本身是决策。新名称给技能一套一致词汇（目的地、战争迷雾、前沿、地图），而不是另加发明术语。单元仍保留“decision”一词：wayfinder 工单是**决策工单**，以免被读作实现工单。

<!-- zh-CN:end 919d0cbc9c365405 -->

## It's working if

<!-- zh-CN:begin 8ff7aa993b886c01 -->

## 怎样算有效

<!-- zh-CN:end 8ff7aa993b886c01 -->

- The destination is written down and agreed before a single ticket exists.

<!-- zh-CN:begin 7c96ea9c44a3d2f0 -->

- 在存在任何工单前，目的地已写下并达成一致。

<!-- zh-CN:end 7c96ea9c44a3d2f0 -->
- Every open ticket reads as a question. Any ticket that reads "build the X" is either mis-typed or belongs downstream of the map.

<!-- zh-CN:begin 6e0bb379e72cccc4 -->

- 每张开放工单读起来都是问题。任何写着“构建 X”的工单要么类型错误，要么属于地图下游。

<!-- zh-CN:end 6e0bb379e72cccc4 -->
- You can look at your tracker and see which tickets are takeable without opening the map, because native blocking shows the frontier.

<!-- zh-CN:begin f209ce8384524082 -->

- 无需打开地图即可从跟踪器看出哪些工单可领取，因为原生阻塞关系显示了前沿。

<!-- zh-CN:end f209ce8384524082 -->
- A session resolves one ticket, posts the answer as a resolution comment, closes it, and adds one line to the map's *Decisions so far*. Then it stops.

<!-- zh-CN:begin 1bfd52e2082bc87a -->

- 一个会话只解决一张工单，将答案作为解决评论发布、关闭它，并向地图的 *Decisions so far* 添加一行。然后停止。

<!-- zh-CN:end 1bfd52e2082bc87a -->
- **Not yet specified** shrinks over time. When fog graduates into a ticket, it leaves that section and does not appear in both places.

<!-- zh-CN:begin 4c25e0c7bcd7249e -->

- **尚未明确**部分随时间缩小。迷雾变为工单时离开该部分，不同时出现在两处。

<!-- zh-CN:end 4c25e0c7bcd7249e -->
- When the opening breadth-first grill finds no fog at all, the skill stops and tells you the effort is small enough to skip the map.

<!-- zh-CN:begin ae60a768ff23da16 -->

- 开头广度优先访谈完全没有发现迷雾时，技能停止并告诉你工作足够小，可跳过地图。

<!-- zh-CN:end ae60a768ff23da16 -->
- The session that finishes the map points you toward a spec, not a pull request.

<!-- zh-CN:begin 07b73a1db745d175 -->

- 完成地图的会话把你指向规范，而非拉取请求。

<!-- zh-CN:end 07b73a1db745d175 -->

## Where it fits

<!-- zh-CN:begin b7b2660b8f495bcf -->

## 所处位置

<!-- zh-CN:end b7b2660b8f495bcf -->

`wayfinder` is a **situational on-ramp**, not the default starting point. Most work still starts on the grill-led idea → ship chain. You use wayfinder when the idea is too big to hold in one session. It rejoins that chain at [to-spec](https://aihero.dev/skills-to-spec), because a cleared map hands off and does not build.

<!-- zh-CN:begin 632acdf70e758d45 -->

`wayfinder` 是**情境入口**，不是默认起点。多数工作仍从访谈主导的“想法 → 交付”链开始。当想法太大、单会话无法把握时使用 wayfinder。它在 [to-spec](https://aihero.dev/skills-to-spec) 重新汇入链，因为清理完的地图进行交接，不构建。

<!-- zh-CN:end 632acdf70e758d45 -->

Most of the work happens in other skills that wayfinder schedules. [grilling](https://aihero.dev/skills-grilling) and [domain-modeling](https://aihero.dev/skills-domain-modeling) resolve the default ticket type, [prototype](https://aihero.dev/skills-prototype) resolves the tickets that talk cannot settle, and [research](https://aihero.dev/skills-research) runs as a subagent so its reading stays out of your session. [handoff](https://aihero.dev/skills-handoff) moves work in and out: into a map from a conversation that grew too big, and out of a map when a side quest appears mid-session. For anything else, [ask-matt](https://aihero.dev/skills-ask-matt) routes over the whole set.

<!-- zh-CN:begin a4f9bf1df90a5d55 -->

大部分工作发生在 wayfinder 调度的其他技能中。[grilling](https://aihero.dev/skills-grilling) 与 [domain-modeling](https://aihero.dev/skills-domain-modeling) 解决默认工单类型，[prototype](https://aihero.dev/skills-prototype) 解决对话无法确定的工单，[research](https://aihero.dev/skills-research) 作为子代理运行，使阅读不进入你的会话。[handoff](https://aihero.dev/skills-handoff) 移入移出工作：从过大的会话移入地图，在会话中途出现支线任务时移出地图。其他情况由 [ask-matt](https://aihero.dev/skills-ask-matt) 在整个集合上路由。

<!-- zh-CN:end a4f9bf1df90a5d55 -->
