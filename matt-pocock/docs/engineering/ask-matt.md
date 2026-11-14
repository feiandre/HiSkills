## What it does

<!-- zh-CN:begin 1cc93f89b9fea1e7 -->

## 功能

<!-- zh-CN:end 1cc93f89b9fea1e7 -->

`ask-matt` is the router over the skills in this repo. You describe the situation you are in (an idea you cannot start, a pile of incoming bug reports, a [session](https://www.aihero.dev/ai-coding-dictionary/session) that has run long), and it names the skill or the sequence of skills that fits, plus where the human decisions in that sequence sit.

<!-- zh-CN:begin c39b179c37c7ceb0 -->

`ask-matt` 是本仓库技能的路由器。你描述处境（无法开始的点子、成堆接收的 bug 报告、运行太久的[会话](https://www.aihero.dev/ai-coding-dictionary/session)），它给出合适的技能或技能序列，并说明序列中哪里需要人类决策。

<!-- zh-CN:end c39b179c37c7ceb0 -->

It recommends and stops. It does not grill, write a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), open a file or fire the skill it just named; what you get back is the next thing to type, and you type it. It is also a hand-written map of the skills in this repo rather than a scan of what you have installed, so it will not route you over your own skills or another author's.

<!-- zh-CN:begin cb643c32957b0576 -->

它只建议然后停止。它不追问、不写[规格](https://www.aihero.dev/ai-coding-dictionary/spec)、不打开文件，也不启动刚命名的技能；你得到的是下一步要输入的命令，再由你输入。它也是本仓库技能的手写地图，而不是扫描已安装技能，因此不会路由到你自己的技能或他人作者的技能。

<!-- zh-CN:end cb643c32957b0576 -->

## When to reach for it

<!-- zh-CN:begin b4390efb24108945 -->

## 何时使用

<!-- zh-CN:end b4390efb24108945 -->

You invoke this by typing `/ask-matt`; the agent won't reach for it on its own.

<!-- zh-CN:begin 530dab177a82f08f -->

输入 `/ask-matt` 调用；代理不会自行使用。

<!-- zh-CN:end 530dab177a82f08f -->

| Your situation | What the router gives back |
| --- | --- |
| An idea, and no idea where to start | The head of the main flow, and whether the build is small enough to skip the spec |
| Bugs and requests arriving from other people | The [triage](https://aihero.dev/skills-triage) on-ramp, and why [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) you generated yourself don't belong on it |
| Two skills that look interchangeable | The line between them, and it is usually one concrete test rather than a matter of taste. [grill-me](https://aihero.dev/skills-grill-me) or [grill-with-docs](https://aihero.dev/skills-grill-with-docs) turns on whether you are in a working directory; [grill-with-docs](https://aihero.dev/skills-grill-with-docs) or [wayfinder](https://aihero.dev/skills-wayfinder) turns on whether the effort fits one session |
| A long session and a decision about the [context](https://www.aihero.dev/ai-coding-dictionary/context) | The ordered tree over the five options at a phase boundary |
| A skill you have already picked | Nothing useful. Invoke that skill directly. |

<!-- zh-CN:begin c43c0e6f585552eb -->

| 处境 | 路由器返回 |
| --- | --- |
| 有点子，不知从哪开始 | 主流程起点，以及构建是否小到可跳过规格 |
| 不断收到他人 bug 和请求 | [triage](https://aihero.dev/skills-triage) 入口，以及为什么自己生成的[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)不适用 |
| 两个技能看起来可互换 | 两者的分界，通常是一项具体检验而非偏好。[grill-me](https://aihero.dev/skills-grill-me) 或 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 取决于是否在工作目录；[grill-with-docs](https://aihero.dev/skills-grill-with-docs) 或 [wayfinder](https://aihero.dev/skills-wayfinder) 取决于工作能否放进一个会话 |
| 长会话及[上下文](https://www.aihero.dev/ai-coding-dictionary/context)决策 | 阶段边界五个选项的有序决策树 |
| 已经选好技能 | 没有有用内容，直接调用该技能。 |

<!-- zh-CN:end c43c0e6f585552eb -->

## Prerequisites

<!-- zh-CN:begin 787c72d6332d63e4 -->

## 前提条件

<!-- zh-CN:end 787c72d6332d63e4 -->

The router names skills; it does not install them. Everything it points at has to be installed for the recommendation to be actionable, and it only knows the promoted skills in this repo.

<!-- zh-CN:begin 75edb3570244efa8 -->

路由器只命名技能，不安装它们。它指向的每个技能都必须已安装，建议才可执行；它只认识本仓库正式发布的技能。

<!-- zh-CN:end 75edb3570244efa8 -->

The tracker-dependent routes (triage, `to-spec`, `to-tickets`, `implement`) assume [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) has already configured an issue tracker in the repo. The router recommends them even before that has happened.

<!-- zh-CN:begin 4b4b2326f769db95 -->

依赖跟踪器的路线（triage、`to-spec`、`to-tickets`、`implement`）假定 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 已配置问题跟踪器。即使尚未配置，路由器也会推荐它们。

<!-- zh-CN:end 4b4b2326f769db95 -->

## Flows, not skills

<!-- zh-CN:begin d000652359e50b23 -->

## 流程，而非技能

<!-- zh-CN:end d000652359e50b23 -->

The skill's leading word is **flow**, a path *through* the skills rather than a single skill. When you name your situation, the router places you at a step on a flow. That is a different answer from "here is the skill that matches your keywords". There are five kinds of route, and the skill itself describes them in full:

<!-- zh-CN:begin 44a1bfa632315986 -->

技能的关键词是**流程**：穿过技能的一条路径，而非单个技能。你说出处境，路由器把你放到流程某一步。这不是“按关键词匹配技能”的答案。共有五类路线，技能正文完整说明：

<!-- zh-CN:end 44a1bfa632315986 -->

- **The main flow**, idea to ship. Grill, spec, tickets, implement (one ticket at a time, or the whole task graph in parallel with [implement-spec](https://aihero.dev/skills-implement-spec)), review, then [retro](https://aihero.dev/skills-retro), which feeds what the build taught back into the agent's environment. It has two branches. One is a prototype detour, for when a question needs runnable code to settle it. The other is the spec-and-tickets split, which is only worth its cost when the build spans more than one session.

<!-- zh-CN:begin 1237d6f7ee59f069 -->

- **主流程**，从想法到交付。追问、规格、工单、实施（逐张工单，或用 [implement-spec](https://aihero.dev/skills-implement-spec) 并行整个任务图）、审查，最后 [retro](https://aihero.dev/skills-retro) 把构建经验反馈到代理环境。它有两个分支：需要可运行代码回答问题时，走原型旁路；构建跨一个会话以上时，才值得付出规格与工单拆分成本。

<!-- zh-CN:end 1237d6f7ee59f069 -->
- **On-ramps**, for a situation that generates work and then merges onto the main flow: incoming bug reports, something broken, or an effort too foggy and too large to hold in one session.

<!-- zh-CN:begin 23944704e03137b6 -->

- **入口路线**，处理先产生工作、再汇入主流程的情形：接收 bug、东西损坏、工作太模糊且一个会话容纳不下。

<!-- zh-CN:end 23944704e03137b6 -->
- **Codebase health**, upkeep rather than feature work. [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) surveys the code for deepening opportunities, and each one it finds re-enters the main flow as an idea.

<!-- zh-CN:begin d3fa57e03434e3c2 -->

- **代码库健康**，属于维护而非功能开发。[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 扫描代码的加深机会，每项发现作为想法重入主流程。

<!-- zh-CN:end d3fa57e03434e3c2 -->
- **Standalones**, which sit off every flow and which you use on their own: the prototype, the questionnaire, the research run.

<!-- zh-CN:begin c5f51a2b69ebf705 -->

- **独立工具**，不属于任何流程，可单独使用：原型、问卷、研究运行。

<!-- zh-CN:end c5f51a2b69ebf705 -->
- **A vocabulary layer underneath**, the two references the other skills pull in when the words rather than the process are the problem.

<!-- zh-CN:begin 4a56f36e4b9713f4 -->

- **底层词汇层**，问题在术语而非流程时，其他技能引用的两份参考。

<!-- zh-CN:end 4a56f36e4b9713f4 -->

## The phase boundary

<!-- zh-CN:begin 878d3b6190aa409e -->

## 阶段边界

<!-- zh-CN:end 878d3b6190aa409e -->

The skill's other key idea is the **phase boundary**. A phase is a chunk of work inside a session (the [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling), the implementation, the QA), and the boundary between two of them is the only place the question "what do I do with this context?" belongs. Mid-phase there is nothing to decide: continue, or split what is left into [subagents](https://www.aihero.dev/ai-coding-dictionary/subagent).

<!-- zh-CN:begin 78989a7f02a80e71 -->

另一个关键概念是**阶段边界**。阶段是会话中的一块工作（[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)、实施、QA），只有两个阶段的边界才适合问“这份上下文该怎么处理？”阶段中途无需决策：继续，或把剩余工作拆给[子代理](https://www.aihero.dev/ai-coding-dictionary/subagent)。

<!-- zh-CN:end 78989a7f02a80e71 -->

| Option | Take it when |
| --- | --- |
| **Continue** | The next phase wants this one verbatim, or you have [smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone) left. It is the only move that keeps the session as a [primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source), so rule it out first |
| **`/clear`** | Everything behind you is disposable. The cheapest option, and you cannot undo it if you were wrong |
| **[handoff](https://aihero.dev/skills-handoff)** | Something has to travel: a new [harness](https://www.aihero.dev/ai-coding-dictionary/harness), a new directory, a colleague, a side task forked mid-phase |
| **Subagent** | The task is scoped tightly enough to run with you [away from the keyboard](https://www.aihero.dev/ai-coding-dictionary/afk) |
| **`/compact`** | None of the above. It is the default, and the tree often ends here |

<!-- zh-CN:begin e7936d9af1a8887e -->

| 选项 | 何时采用 |
| --- | --- |
| **继续** | 下一阶段需要逐字使用当前上下文，或仍有[智能区间](https://www.aihero.dev/ai-coding-dictionary/smart-zone)。这是保留会话为[主要来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)的唯一动作，应最先排除其他选项 |
| **`/clear`** | 之前内容都可丢弃。最便宜，但判断错误后不可撤销 |
| **[handoff](https://aihero.dev/skills-handoff)** | 有东西必须传递：新[宿主](https://www.aihero.dev/ai-coding-dictionary/harness)、新目录、同事、阶段中途分出的旁支任务 |
| **子代理** | 任务范围足够窄，可在你[离开键盘](https://www.aihero.dev/ai-coding-dictionary/afk)时运行 |
| **`/compact`** | 以上都不适用。它是默认项，决策树常在这里结束 |

<!-- zh-CN:end e7936d9af1a8887e -->

People often get two of these wrong, which is why the router gives the order and not only the list. `/handoff` looks like the general way to move between context windows, but it is not. All it gives you is portability. `/compact` is the last option in the tree, not the first, because each of the four options above it is cheaper or more precise.

<!-- zh-CN:begin 732420472461d5da -->

人们常错用其中两项，因此路由器给出顺序而不只是列表。`/handoff` 看起来像跨上下文窗口的通用方法，实际只提供可移植性。`/compact` 是树中最后选项，因为上面四项都更便宜或精确。

<!-- zh-CN:end 732420472461d5da -->

## Common questions

<!-- zh-CN:begin e942311c9654c373 -->

## 常见问题

<!-- zh-CN:end e942311c9654c373 -->

**Isn't there just a list of the skills in the right order?**

<!-- zh-CN:begin aade873274a31413 -->

**难道不能按正确顺序列一张技能表？**

<!-- zh-CN:end aade873274a31413 -->

People keep asking for one in the README. This skill is that list. A static table would say `wayfinder → to-spec → to-tickets → implement → code-review → retro` and be wrong for most situations. The important parts are the branches: is there a codebase, does the build span sessions, can talking settle this question. The cost is that the router is maintained by hand, so it lags behind the repo. `/grilling` shipped long before the router named it.

<!-- zh-CN:begin f9713de7721067cb -->

README 中不断有人要求。本技能就是那张表。静态表会说 `wayfinder → to-spec → to-tickets → implement → code-review → retro`，对多数情况却错误。重点是分支：是否有代码库、构建是否跨会话、讨论能否回答问题。代价是路由器手工维护，会落后于仓库。`/grilling` 发布很久后路由器才列出它。

<!-- zh-CN:end f9713de7721067cb -->

**It told me half the skills aren't installed.**

<!-- zh-CN:begin 7534157482361865 -->

**它说半数组件没安装。**

<!-- zh-CN:end 7534157482361865 -->

This is a known bug, and it is not fixed. Most of the skills the router routes you through set `disable-model-invocation: true`, which means the harness leaves them out of the skill list it injects into the agent's context. The agent reads that list as exhaustive and reports them missing. In one reported session, it declared the whole spec-and-tickets flow absent and rerouted to bare `/grilling` and `/tdd`. Sixteen of the plugin's twenty-seven skills carry the flag, so this is the common case rather than an edge. They are installed. Type the slash command anyway, or check `.claude-plugin/plugin.json`, which is the authority on what is present.

<!-- zh-CN:begin 6f9a4f054671998e -->

这是已知且未修复的 bug。路由器经过的多数技能设置 `disable-model-invocation: true`，宿主不会把它们放进注入代理上下文的技能列表。代理把该列表当成完整列表并报告缺失。一次会话中，它宣称整个规格与工单流程不存在，改走裸 `/grilling` 和 `/tdd`。插件 27 个技能中有 16 个带该标志，因此这是常见情况而非边缘。它们实际已安装。照常输入斜杠命令，或检查 `.claude-plugin/plugin.json`，它以权威方式列出现存技能。

<!-- zh-CN:end 6f9a4f054671998e -->

**It described a skill's behaviour, and the skill doesn't do that.**

<!-- zh-CN:begin 6c8f12bbd2911d1a -->

**它描述了某技能行为，但技能并非如此。**

<!-- zh-CN:end 6c8f12bbd2911d1a -->

This is also a real bug, and also not fixed. The router answers from its own one-line summary of each skill rather than from the skill. One detailed report tracked three instances in a single session, including a recommendation to skip [to-spec](https://aihero.dev/skills-to-spec) based only on the summary "turn the thread into a spec". The router never opened `to-spec/SKILL.md`. In every case it verified only after the user pushed back, and never on its own initiative. Skipping `to-spec` there cost a real seam check, and the tickets that came out undercounted the work. When the router states something about another skill that you will act on, ask it to open that `SKILL.md` first. The same applies to questions the map does not cover at all, such as whether to use [plan mode](https://www.aihero.dev/ai-coding-dictionary/agent-mode): that answer is the [model](https://www.aihero.dev/ai-coding-dictionary/model)'s inference, not something written down here.

<!-- zh-CN:begin 8299a0ef3e849458 -->

这也是真实且未修复的 bug。路由器依据自己给每个技能写的一行摘要回答，而不读取技能。一份详细报告在一次会话中追踪到三次，包括仅凭“把讨论串转为规格”的摘要就建议跳过 [to-spec](https://aihero.dev/skills-to-spec)。路由器从未打开 `to-spec/SKILL.md`，每次都等用户反驳后才验证，从不主动。跳过 `to-spec` 会遗失一次真实接缝检查，产出工单低估工作。路由器将要据此让你行动的另一技能说明时，先要求它打开对应 `SKILL.md`。地图未覆盖的问题同样如此，例如是否使用[计划模式](https://www.aihero.dev/ai-coding-dictionary/agent-mode)：那答案是[模型](https://www.aihero.dev/ai-coding-dictionary/model)推断，不是本文件写下的内容。

<!-- zh-CN:end 8299a0ef3e849458 -->

**Why is it prose instead of a numbered checklist?**

<!-- zh-CN:begin 7b7891a5ef4b230d -->

**为什么用散文而非编号清单？**

<!-- zh-CN:end 7b7891a5ef4b230d -->

It is a fair complaint. An open issue argues that most of the routing is deterministic and that the narrative makes it hard to scan. Nothing stops you asking for the compressed form: "just give me the sequence" gets you the sequence. The prose carries the conditional part: the branches, where a human decision is expected, and where to clear or compact between steps. A flat checklist drops exactly that.

<!-- zh-CN:begin 0b66380d0c1afb68 -->

这个抱怨合理。未解决问题的意见认为大多数路由是确定性的，叙述难扫描。你随时可要求压缩形式：“只给序列”就能得到序列。散文承载条件部分：分支、何处需要人类决策、步骤之间何时 clear 或 compact。扁平清单会丢掉这些。

<!-- zh-CN:end 0b66380d0c1afb68 -->

**Can it route over my own skills, or another author's?**

<!-- zh-CN:begin d320d1936f1896af -->

**它能路由到我自己的或其他作者的技能吗？**

<!-- zh-CN:end d320d1936f1896af -->

No. Three separate proposals have asked for a router that reads your local `skills/` directory and recommends from whatever is installed. `ask-matt` is not that. It is a map of one set, maintained by hand, and it knows nothing about skills you wrote or installed from elsewhere.

<!-- zh-CN:begin e720fd01774b1e59 -->

不能。三次独立提案都希望路由器读取本地 `skills/` 并推荐已安装内容。`ask-matt` 不是这种工具。它是手工维护的一组技能地图，完全不认识你编写或从别处安装的技能。

<!-- zh-CN:end e720fd01774b1e59 -->

**It told me to edit a SKILL.md.**

<!-- zh-CN:begin c6cece8133e4e598 -->

**它让我编辑 SKILL.md。**

<!-- zh-CN:end c6cece8133e4e598 -->

That advice is often correct, but the edit rarely lasts. Someone asked it how to make [implement](https://aihero.dev/skills-implement) close tickets, was told to add a line to the skill, and saw the problem at once. `npx skills update` overwrites the file, and the plugin install is read-only. Put standing behaviour in your own `CLAUDE.md` or `AGENTS.md`, or say it in the invocation. Changes you make in the prompt survive updates. People point the flow at Linear instead of GitHub this way, or ask it which open tickets could run in parallel.

<!-- zh-CN:begin e489111324d1b4a9 -->

建议经常正确，但修改通常不持久。有人问怎样让 [implement](https://aihero.dev/skills-implement) 自动关闭工单，得到“在技能中加一行”的建议后立即发现问题。`npx skills update` 会覆盖文件，插件安装也是只读。把长期行为写入自己的 `CLAUDE.md` 或 `AGENTS.md`，或在调用时说明。提示词中的修改能跨更新保留。人们用这种方式让流程指向 Linear 而非 GitHub，或询问哪些开放工单可并行。

<!-- zh-CN:end e489111324d1b4a9 -->

**It named a skill I don't have, or missed one I do.**

<!-- zh-CN:begin 7645bce90cd8bcb0 -->

**它命名了没有的技能，或漏了我有的技能。**

<!-- zh-CN:end 7645bce90cd8bcb0 -->

Check the changelog for a rename before assuming it is gone. `writing-great-skills` became [writing-for-agents](https://aihero.dev/skills-writing-for-agents) with no alias, `to-prd` became [to-spec](https://aihero.dev/skills-to-spec), and `pathfinder` became [wayfinder](https://aihero.dev/skills-wayfinder). Four skills were retired outright into the skills that absorbed them: `ubiquitous-language`, `design-an-interface`, `qa` and `request-refactor-plan`. If it misses a skill you have, that is the router's own lag, described above.

<!-- zh-CN:begin 9ace3fff6068a0f5 -->

先查 changelog 是否改名。`writing-great-skills` 无别名改为 [writing-for-agents](https://aihero.dev/skills-writing-for-agents)，`to-prd` 改为 [to-spec](https://aihero.dev/skills-to-spec)，`pathfinder` 改为 [wayfinder](https://aihero.dev/skills-wayfinder)。四个技能已并入吸收它们的技能：`ubiquitous-language`、`design-an-interface`、`qa` 和 `request-refactor-plan`。若漏掉你拥有的技能，就是上文所述路由器自身滞后。

<!-- zh-CN:end 9ace3fff6068a0f5 -->

## It's working if

<!-- zh-CN:begin 9aeab22caaf0bf77 -->

## 正常表现

<!-- zh-CN:end 9aeab22caaf0bf77 -->

- It ends by naming what to type and stops there, instead of starting the work itself.

<!-- zh-CN:begin a91aae1730217ea8 -->

- 最后只命名下一步要输入的命令并停止，不自行开始工作。

<!-- zh-CN:end a91aae1730217ea8 -->
- The route it gives back mentions where to clear or compact context and where you are expected to review, not just a list of skill names.

<!-- zh-CN:begin aa74df768d001007 -->

- 返回路线说明何处清理或压缩上下文、何处需要审查，而非只给技能名。

<!-- zh-CN:end aa74df768d001007 -->
- Where two skills are close, it says which one and why the other is wrong for you.

<!-- zh-CN:begin 1f8d4101ffa3dcdc -->

- 两个技能接近时，说明选哪个以及另一个为何不适合。

<!-- zh-CN:end 1f8d4101ffa3dcdc -->
- Any claim it makes about another skill's behaviour shows up in the trace as it reading that skill's `SKILL.md`.

<!-- zh-CN:begin 25bebe8027815c57 -->

- 对另一技能行为的断言在轨迹中应有读取其 `SKILL.md` 的记录。

<!-- zh-CN:end 25bebe8027815c57 -->
- You recognise your own situation in what it hands back, rather than the nearest generic scenario.

<!-- zh-CN:begin 77963403e7bba244 -->

- 返回内容对应你的真实处境，而非最接近的通用场景。

<!-- zh-CN:end 77963403e7bba244 -->

## Where it fits

<!-- zh-CN:begin ea856f54ef2cc646 -->

## 所处位置

<!-- zh-CN:end ea856f54ef2cc646 -->

`ask-matt` is a **standalone router** that sits over the whole set. It is never a step in a chain. It points into every chain, and the other docs pages link back to it so none of them has to redraw the graph. From here you most often land on [grill-with-docs](https://aihero.dev/skills-grill-with-docs), the head of the main flow, or [triage](https://aihero.dev/skills-triage), the on-ramp for work that arrived rather than work you started.

<!-- zh-CN:begin 707149c7defda35e -->

`ask-matt` 是覆盖整套技能的**独立路由器**，从不属于任何链条。它指向所有链条，其他文档页也链接回来，避免重复画图。从这里最常进入 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)（主流程起点）或 [triage](https://aihero.dev/skills-triage)（接收外部工作的入口）。

<!-- zh-CN:end 707149c7defda35e -->

It is a [secondary source](https://www.aihero.dev/ai-coding-dictionary/secondary-source) over the skills it describes. Where the router and a `SKILL.md` disagree, the `SKILL.md` is right.

<!-- zh-CN:begin 7483618bd1b6fef3 -->

对于所描述技能，它是[次要来源](https://www.aihero.dev/ai-coding-dictionary/secondary-source)。路由器和 `SKILL.md` 冲突时，以 `SKILL.md` 为准。

<!-- zh-CN:end 7483618bd1b6fef3 -->
