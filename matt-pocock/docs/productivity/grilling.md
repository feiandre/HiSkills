## What it does

<!-- zh-CN:begin f8efc186d4b2d605 -->

## 它做什么

<!-- zh-CN:end f8efc186d4b2d605 -->

`grilling` is the interview loop that stress-tests a plan, a decision, or an idea before anyone acts on it. It maps the subject as a **design tree**: every decision branches into the decisions that hang off it, and interviews you branch by branch until no assumption stays unstated.

<!-- zh-CN:begin 6ad0bcf16f34218d -->

`grilling` 是在任何人行动前对计划、决策或想法进行压力检验的访谈循环。它把主题绘成**设计树**：每个决策分叉出依赖它的决策，再逐分支访谈直到没有未声明假设。

<!-- zh-CN:end 6ad0bcf16f34218d -->

It does not ask one question at a time, and it does not ask everything at once. Each **round** asks the whole **frontier**: every decision whose prerequisites are already settled, and nothing else. Two questions never share a round if one depends on the other; a question that hinges on an answer still open belongs to a later round. Your answers settle decisions, the frontier moves outward, and the next round asks what that unblocked. Thirteen questions typically land in about three rounds rather than thirteen.

<!-- zh-CN:begin 55c9bfd432448b24 -->

它既非一次一问，也非一次全问。每**轮**询问整个**前沿**：前置条件已确定的所有决策，别无其他。依赖关系的问题不同轮；依赖未决答案的问题留到之后。回答确定决策，前沿外扩，下一轮询问解锁内容。13 个问题通常约 3 轮完成。

<!-- zh-CN:end 55c9bfd432448b24 -->

## When to reach for it

<!-- zh-CN:begin e9f30bdb865950f2 -->

## 何时使用

<!-- zh-CN:end e9f30bdb865950f2 -->

Type `/grilling`, or the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reaches for it on its own when a task fits. It is the only [skill](https://www.aihero.dev/ai-coding-dictionary/skill) in the grilling family that is model-invoked, so you rarely type it. Usually a skill you *did* type runs it for you.

<!-- zh-CN:begin 7520660411ed5898 -->

输入 `/grilling`，或任务适合时[代理](https://www.aihero.dev/ai-coding-dictionary/agent)自行使用。它是追问家族唯一模型调用[技能](https://www.aihero.dev/ai-coding-dictionary/skill)，很少手动输入；通常由你调用的另一技能运行。

<!-- zh-CN:end 7520660411ed5898 -->

Typing `/grilling` directly gets you the plain interview and nothing else. Where you want something more than that:

<!-- zh-CN:begin ec7036d06abadde2 -->

直接 `/grilling` 只得到普通访谈。需要更多时：

<!-- zh-CN:end ec7036d06abadde2 -->

| What you have | Reach for |
| --- | --- |
| You aren't working in a working directory | [grill-me](https://aihero.dev/skills-grill-me): the same [session](https://www.aihero.dev/ai-coding-dictionary/session), under a name the agent will never fire by itself |
| You are in a working directory | [grill-with-docs](https://aihero.dev/skills-grill-with-docs): the same session, and it writes `GLOSSARY.md` and ADRs as it goes |
| An effort too big to hold in one session | [wayfinder](https://aihero.dev/skills-wayfinder): it charts a map and runs grilling inside the decision tickets |
| A question that talking cannot settle: how something should look or feel | [prototype](https://aihero.dev/skills-prototype): build the throwaway version, then come back |
| A skill of your own that needs an interview | Invoke `/grilling` from it, rather than writing another interview |

<!-- zh-CN:begin d07746c682e0a275 -->

| 你拥有 | 使用 |
| --- | --- |
| 不在工作目录 | [grill-me](https://aihero.dev/skills-grill-me)：同一[会话](https://www.aihero.dev/ai-coding-dictionary/session)，代理不会自行触发 |
| 在工作目录 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs)：同一会话，并同步写 `GLOSSARY.md` 与 ADR |
| 工作大到单次会话放不下 | [wayfinder](https://aihero.dev/skills-wayfinder)：绘制地图并在决策工单内追问 |
| 谈话无法确定的观感问题 | [prototype](https://aihero.dev/skills-prototype)：做一次性原型再回来 |
| 自有技能需要访谈 | 在其中调用 `/grilling`，不再新写访谈 |

<!-- zh-CN:end d07746c682e0a275 -->

## The round, the frontier, and who decides

<!-- zh-CN:begin 604ffc41729d4516 -->

## 轮次、前沿与决策者

<!-- zh-CN:end 604ffc41729d4516 -->

The skill rests on three ideas.

<!-- zh-CN:begin e10a9590cb735ad5 -->

技能基于三个想法。

<!-- zh-CN:end e10a9590cb735ad5 -->

The **design tree** is the model of the subject: decisions with decisions hanging off them. The **frontier** is the set of decisions whose prerequisites are all settled: the only questions the agent can ask yet. A **round** is one frontier, asked in full and answered in full.

<!-- zh-CN:begin d863b2e8f46ca48b -->

**设计树**是主题模型：决策及其分叉。**前沿**是前置条件均确定的决策集合，也是代理当下仅能问的问题。**轮次**是一整个前沿，完整询问并完整回答。

<!-- zh-CN:end d863b2e8f46ca48b -->

Inside a round, every question has a fixed format: numbered and titled behind a `❓`, then the body, then the agent's recommended answer alone on a `➡️` line. This format lets you answer a round by number ("1 yes, 2 the second option, 3 no, here's why") instead of by quoting questions back. The format has one known problem. The recommendation sometimes argues *against* the question as it was worded, so agreeing with the recommendation means answering "no" to the question. When that happens, answer the recommendation and say so.

<!-- zh-CN:begin 8f2736fc6715a654 -->

轮内问题格式固定：`❓` 后编号标题、正文、随后建议独占 `➡️` 行。可按编号回答整轮（“1 是，2 第二项，3 否，因为……”）。已知问题：建议有时与问题措辞相反，赞同建议意味着回答“否”。此时回答建议并说明。

<!-- zh-CN:end 8f2736fc6715a654 -->

The other half of the design is the split between facts and decisions. Facts are the skill's own job. When a frontier question needs something the [environment](https://www.aihero.dev/ai-coding-dictionary/environment) can settle, the agent dispatches a [sub-agent](https://www.aihero.dev/ai-coding-dictionary/subagent) to find out rather than asking you. The round does not wait for that research; only the questions that depend on it wait. Decisions are yours, and the agent must wait for them. An agent running `grilling` that answers its own decisions has broken the skill. The session ends when the frontier is empty. The agent then waits for you to confirm a shared understanding before it acts on what you agreed.

<!-- zh-CN:begin 33ae89cb7e98d62a -->

设计另一半是事实与决策分离。事实由技能自己查；前沿问题需要[环境](https://www.aihero.dev/ai-coding-dictionary/environment)确认时，代理派[子代理](https://www.aihero.dev/ai-coding-dictionary/subagent)查而不问你。该轮不等待研究，只有依赖研究的问题等待。决策属于你，代理必须等待；自行回答即破坏技能。前沿为空时会话结束，代理在你确认共同理解后再行动；其中相关的字段或标识包括 `grilling`。

<!-- zh-CN:end 33ae89cb7e98d62a -->

The frontier has one limit. The agent chooses it by judgement; it does not compute it from a graph. So it can put two questions in one round and only later find that one answer should have changed the other. The only guard is to tell it. That reopens the affected branch in the next round.

<!-- zh-CN:begin 2737759e810cad58 -->

前沿有局限：代理凭判断选择，不从图计算，因此可能同轮问两个问题，之后才发现答案应改变另一个。唯一防护是告知它；下轮重开受影响分支。

<!-- zh-CN:end 2737759e810cad58 -->

## What lives here and what lives in the wrappers

<!-- zh-CN:begin b3997823d466645f -->

## 本页与包装技能各管什么

<!-- zh-CN:end b3997823d466645f -->

This page covers the mechanism. The wrapper skills' pages answer the questions people ask most often.

<!-- zh-CN:begin 3c3acdcfb6528156 -->

本页说明机制；包装技能页回答最常见问题。

<!-- zh-CN:end 3c3acdcfb6528156 -->

| Question | Where it is answered |
| --- | --- |
| The tree, the frontier, rounds, the question format, facts vs decisions | Here |
| How long a session should run, what to do with a question you can't answer by talking, how to avoid nodding along | [grill-me](https://aihero.dev/skills-grill-me) |
| What gets written to `GLOSSARY.md`, what becomes an ADR | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |

<!-- zh-CN:begin f087cf1242dc6a2f -->

| 问题 | 位置 |
| --- | --- |
| 树、前沿、轮次、问题格式、事实与决策 | 本页 |
| 会话多长、谈话无法回答的问题、避免盲目点头 | [grill-me](https://aihero.dev/skills-grill-me) |
| 什么写入 `GLOSSARY.md`，什么成为 ADR | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |

<!-- zh-CN:end f087cf1242dc6a2f -->

## Common questions

<!-- zh-CN:begin 7fbd1b9ec994943c -->

## 常见问题

<!-- zh-CN:end 7fbd1b9ec994943c -->

**Can I go back to one question at a time?**
Yes, and a large part of the audience does. Add this to your global `CLAUDE.md`:

<!-- zh-CN:begin b8f94f6a556c9069 -->

**能改回一次一问吗？**
可以，很多用户如此。在全局 `CLAUDE.md` 加：

<!-- zh-CN:end b8f94f6a556c9069 -->

```
When grilling, ask one question at a time.
```

<!-- zh-CN:begin f0a4f89735aa2e6d -->

```
深入追问时，一次只问一个问题。
```

<!-- zh-CN:end f0a4f89735aa2e6d -->

Not everyone prefers the round-based default. Users who read slowly, who work in a second language, or who use the sequential format to help them focus report that one question at a time works better for them. The opt-out is a supported setting, not a workaround.

<!-- zh-CN:begin e14aff2fa4050fe5 -->

不是所有人喜欢逐轮。阅读慢、使用第二语言或靠顺序格式集中注意力者报告一次一问更好。退出是受支持设置，不是绕过。

<!-- zh-CN:end e14aff2fa4050fe5 -->

**Where did `/batch-grill-me` go?**
Into this skill. Round-based questioning shipped briefly as a separate skill, then moved into `grilling` itself, so everything built on the primitive (`grill-me`, `grill-with-docs`, `triage`, `wayfinder`) got it at once. There is no `batch-grill-me` to install, and no separate sequential skill either; the `CLAUDE.md` line above is the way back to one-at-a-time.

<!-- zh-CN:begin d8e29d5434ef0f70 -->

**`/batch-grill-me` 去哪了？**
并入本技能。逐轮曾短暂独立，后来进入 `grilling`，所有包装技能同时获得。无需安装 `batch-grill-me`，也无独立顺序技能；上述 `CLAUDE.md` 行恢复一次一问；其中相关的字段或标识包括 `grill-me`、`grill-with-docs`、`triage`、`wayfinder`。

<!-- zh-CN:end d8e29d5434ef0f70 -->

**Asking a whole round at once must lose the questions my earlier answers would have raised. Doesn't it?**
This is the most common objection to rounds, and the frontier answers it. A round only contains questions that do not depend on each other, so no answer in a round can invalidate another question in that round. Your answers still change what comes after them, because the agent works out each next round from scratch. You do lose something, but less than "all questions at once" implies. See the frontier's limit above.

<!-- zh-CN:begin 7988967b4d8a8f60 -->

**一次问整轮会丢失早先答案引出的问题吗？**
这是最常见反对，前沿解决它：轮内问题互不依赖，任一回答不会使同轮另一问题失效。回答仍改变后续，因代理从零计算下一轮。确实失去一些内容，但少于“一次全问”。见前沿局限。

<!-- zh-CN:end 7988967b4d8a8f60 -->

**It ran out of questions and started building.**
The confirmation gate exists for this. The skill is finished when you say the understanding is shared, not when the frontier empties. Weaker and faster [models](https://www.aihero.dev/ai-coding-dictionary/model) still skip the gate. Users report this most often on lower-effort or non-frontier models, which collapse "interview until shared understanding" into a couple of questions and an outline. If yours does it, the reliable fix is a line in your own `AGENTS.md` or `CLAUDE.md` telling the agent not to implement without permission.

<!-- zh-CN:begin 3ef48e19d2b1b3d1 -->

**问题问完就开始构建。**
确认关卡就是为此存在：你确认共同理解才算完成，不是前沿为空。较弱快速[模型](https://www.aihero.dev/ai-coding-dictionary/model)仍会跳过。低努力或非前沿模型常把“访谈至共同理解”压缩成几个问题和提纲。可靠修复是在自有 `AGENTS.md` 或 `CLAUDE.md` 要求未经许可不实施。

<!-- zh-CN:end 3ef48e19d2b1b3d1 -->

**It answered its own questions instead of asking me.**
That is a bug in the run, and it is the reason the skill's text separates facts from decisions. It happens most when another skill runs `grilling` to resolve a ticket, and the agent takes that task as permission to keep moving. The same constraint is why there is no async mode. People have asked for a variant that reads a GitHub issue and posts one consolidated decision memo, and that is a different skill, because a grilling session that nobody answers has produced the agent's opinion rather than yours.

<!-- zh-CN:begin 52ad67be0e391504 -->

**它自问自答。**
这是运行缺陷，也是技能区分事实与决策的原因。常见于其他技能为解决工单运行追问，代理把任务当继续推进许可。异步模式也因同一约束不提供：读取 GitHub 议题并发布汇总决策备忘录会被无人回答的代理意见替代；其中相关的字段或标识包括 `grilling`。

<!-- zh-CN:end 52ad67be0e391504 -->

**Can I cap the number of questions?**
No, and a cap is out of scope on purpose. Some plans need three questions and some need fifty; a fixed ceiling either truncates the hard case or feels arbitrary on the easy one. The intended control is plain language. Tell it to wrap up, or stop and accept the plan where it stands. If a session is running very long, the cause is usually that the scope was too big; break the work up and grill the pieces.

<!-- zh-CN:begin cdb7bf88bde30532 -->

**能给问题数量设上限吗？**
不能，上限有意排除。有些计划需三问，有些五十问；固定上限会截断困难情形或让简单情形任意。控制方式是平实语言：要求收尾，或停止并接受当前计划。会话过久通常范围太大，拆分后逐块追问。

<!-- zh-CN:end cdb7bf88bde30532 -->

**I installed `grill-me` on its own and nothing happens.**
`grill-me` is a one-line skill whose whole body is "run a `/grilling` session", so it needs this skill installed too. The same is true of `grill-with-docs`, which additionally needs [domain-modeling](https://aihero.dev/skills-domain-modeling). Installing the whole set avoids the problem; installing selectively means installing the primitives as well.

<!-- zh-CN:begin 4ed42886f5be8947 -->

**单独安装 `grill-me` 后什么都不发生。**
`grill-me` 一行技能，正文是“运行 `/grilling`”，因此也需本技能。`grill-with-docs` 还依赖 [domain-modeling](https://aihero.dev/skills-domain-modeling)。安装整套可避免；选择性安装也要装基础技能。

<!-- zh-CN:end 4ed42886f5be8947 -->

**`grill-with-docs` ran, but it never loaded `grilling`.**
This is a real bug, still unfixed, and users report it across [harnesses](https://www.aihero.dev/ai-coding-dictionary/harness) and models. A skill that names another skill does not reliably cause that skill to load, and `grill-with-docs` names two. The sign is a session that asks everything at once with no recommendations. That means the model is improvising an interview rather than running this one. Asking the agent directly whether it loaded `grilling` and `domain-modeling` usually recovers it.

<!-- zh-CN:begin 66623e0e408b1ca5 -->

**`grill-with-docs` 运行但未加载 `grilling`。**
真实未修复缺陷，多[平台](https://www.aihero.dev/ai-coding-dictionary/harness)和模型均有报告。点名另一技能不保证加载；迹象是一次问完且无建议。直接问代理是否加载 `grilling` 与 `domain-modeling` 通常恢复；其中相关的字段或标识包括 `grill-with-docs`。

<!-- zh-CN:end 66623e0e408b1ca5 -->

## It's working if

<!-- zh-CN:begin 828f4eb74da7ee33 -->

## 怎样算正常工作

<!-- zh-CN:end 828f4eb74da7ee33 -->

- A round arrives as a numbered list, each question with its recommendation on a separate `➡️` line, and you can answer the whole round by number.

<!-- zh-CN:begin ae426ca3c87db7cd -->

- 一轮是编号列表，每题建议独占 `➡️` 行，可按编号答完。

<!-- zh-CN:end ae426ca3c87db7cd -->
- Nothing in a round needs another question in the same round answered first.

<!-- zh-CN:begin ced8af5eb7a2ad04 -->

- 同轮问题无相互依赖。

<!-- zh-CN:end ced8af5eb7a2ad04 -->
- Later rounds ask things the first round could not have asked.

<!-- zh-CN:begin 8b68531a73980f29 -->

- 后续轮问第一轮无法问的内容。

<!-- zh-CN:end 8b68531a73980f29 -->
- It goes and looks facts up (reading files, dispatching a sub-agent) rather than asking you something it could have found out.

<!-- zh-CN:begin 8c84626d7ecfa758 -->

- 代理查事实（读文件、派子代理）而非问本可查明的事。

<!-- zh-CN:end 8c84626d7ecfa758 -->
- Research running in the background does not stall the round; only the questions that depend on it wait.

<!-- zh-CN:begin 9d03d0c48f5be930 -->

- 后台研究不阻塞整轮，只有依赖问题等待。

<!-- zh-CN:end 9d03d0c48f5be930 -->
- It stops at the end and asks you to confirm the understanding is shared, instead of starting work.

<!-- zh-CN:begin 4a575e4907d0b7be -->

- 末尾停下要求确认共同理解，不自行开始工作。

<!-- zh-CN:end 4a575e4907d0b7be -->
- Question count stays high while round count stays low.

<!-- zh-CN:begin aa2e15e001336ce8 -->

- 问题数保持高，轮次保持低。

<!-- zh-CN:end aa2e15e001336ce8 -->

## Where it fits

<!-- zh-CN:begin ebb237bf5f4a5d70 -->

## 适用范围

<!-- zh-CN:end ebb237bf5f4a5d70 -->

`grilling` is a **primitive**, not a step you schedule: the single source of truth for the interview technique, kept in one place so every skill that needs an interview reaches for it instead of inventing one. [grill-me](https://aihero.dev/skills-grill-me) and [grill-with-docs](https://aihero.dev/skills-grill-with-docs) are its two user-invoked front doors, and `grill-with-docs` is where the main build chain begins, ahead of [to-spec](https://aihero.dev/skills-to-spec). [wayfinder](https://aihero.dev/skills-wayfinder) runs it to resolve decision tickets, [triage](https://aihero.dev/skills-triage) to grill a vague report into a workable one, and [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) to walk the tree once you have picked a candidate to deepen. When you are unsure which entry point fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin bf23e028a52d782f -->

`grilling` 是**原语**而非排定步骤：访谈技术唯一来源，所有需要访谈的技能调用它。 [grill-me](https://aihero.dev/skills-grill-me) 与 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 是用户调用正门，主构建链从 `grill-with-docs` 开始，在 [to-spec](https://aihero.dev/skills-to-spec) 前。[wayfinder](https://aihero.dev/skills-wayfinder) 解决决策工单，[triage](https://aihero.dev/skills-triage) 把含糊报告追问成可执行内容，[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 在选好深化候选后遍历树。不确定入口时 [ask-matt](https://aihero.dev/skills-ask-matt) 路由。

<!-- zh-CN:end bf23e028a52d782f -->
