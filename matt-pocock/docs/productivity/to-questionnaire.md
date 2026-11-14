## What it does

<!-- zh-CN:begin 6ab266a2fcf86ec8 -->

## 功能

<!-- zh-CN:end 6ab266a2fcf86ec8 -->

`to-questionnaire` turns a decision you can't settle on your own into a **questionnaire**: a Markdown document you hand to the one person who holds what you're missing, for them to fill in async or for the two of you to work through in a meeting.

<!-- zh-CN:begin fabfbc63a4c84bdc -->

`to-questionnaire` 把无法独自解决的决策转成一份 **Markdown 问卷**，交给掌握缺失信息的人异步填写，或在会议中共同完成。

<!-- zh-CN:end fabfbc63a4c84bdc -->

It grills you about the **send**, never the subject. An interview about the topic is pointless, because not knowing the topic is why you're writing to someone else. So it asks the two things you can always answer (who this is going to, and what you need back from them) and aims every question in the document at the **gap** between the two.

<!-- zh-CN:begin ef33a504df82d2f2 -->

它只追问**发送**，不追问主题。讨论主题毫无意义，因为不熟悉主题才需要询问别人。它收集你总能回答的两件事（发给谁、需要对方回传什么），并让每个问题瞄准两者之间的**缺口**。

<!-- zh-CN:end ef33a504df82d2f2 -->

## When to reach for it

<!-- zh-CN:begin d50b2c7151efa642 -->

## 何时使用

<!-- zh-CN:end d50b2c7151efa642 -->

You invoke this by typing `/to-questionnaire`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own.

<!-- zh-CN:begin 9ea546f55f8f11b2 -->

输入 `/to-questionnaire` 调用；[代理](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。

<!-- zh-CN:end 9ea546f55f8f11b2 -->

Reach for it when a decision is blocked on knowledge that lives in one other person's head: a client, a domain expert, an exec who owns the business rules, a colleague on a team you don't sit with. Which skill you want depends on where the answers are:

<!-- zh-CN:begin e838c756d83e2e41 -->

决策受另一个人的知识阻塞时使用：客户、领域专家、掌握业务规则的管理者，或不与你同组的同事。选择何种技能取决于答案在哪里：

<!-- zh-CN:end e838c756d83e2e41 -->

| The answers are in… | Reach for |
| --- | --- |
| Your own head, unsharpened | [grill-me](https://aihero.dev/skills-grill-me) |
| The codebase | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| Someone else's head | `to-questionnaire` |
| Nobody's head yet, the question needs something to react to | [prototype](https://aihero.dev/skills-prototype) |

<!-- zh-CN:begin 3ccf1c086b172d20 -->

| 答案来源 | 使用 |
| --- | --- |
| 自己脑中但尚未理清 | [grill-me](https://aihero.dev/skills-grill-me) |
| 代码库 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 别人脑中 | `to-questionnaire` |
| 尚不存在，需要可反应之物 | [prototype](https://aihero.dev/skills-prototype) |

<!-- zh-CN:end 3ccf1c086b172d20 -->

The common case is a [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) session that stalls because some of the questions it raised aren't yours to answer. Run `/to-questionnaire` in that same conversation to take those questions offline, then bring the answers back and carry on.

<!-- zh-CN:begin 477caae0a7e5d801 -->

常见情况是[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)因部分问题不属于你而停滞。在同一对话运行 `/to-questionnaire`，把问题带去线下，再把答案带回继续。

<!-- zh-CN:end 477caae0a7e5d801 -->

## The send, not the subject

<!-- zh-CN:begin e8e62625adf75a46 -->

## 发送，而非主题

<!-- zh-CN:end e8e62625adf75a46 -->

The interview is two exchanges, and then it stops.

<!-- zh-CN:begin 6e70dc3e7ec1104d -->

访谈只有两轮，然后停止。

<!-- zh-CN:end 6e70dc3e7ec1104d -->

- **Who is it going to?** Their role, their expertise, their relationship to you. This sets the tone and how much context the document has to carry. An outside client needs orienting; a teammate does not.

<!-- zh-CN:begin 1ca170fb9ef31368 -->

- **发给谁？**角色、专长、与你的关系；这决定语气和所需上下文。外部客户需要背景，队友不需要。

<!-- zh-CN:end 1ca170fb9ef31368 -->
- **What do you need back?** The concrete decisions or facts you can't resolve alone. This becomes the checklist for the finished document. Every item you name gets a question aimed at it.

<!-- zh-CN:begin 707f65109e16637c -->

- **需要回传什么？**无法独自解决的具体决策或事实，成为文件检查清单；每项都要有对应问题。

<!-- zh-CN:end 707f65109e16637c -->

Everything after that is drafting. The skill writes the file to `to-questionnaire-<slug>.md` in the current directory. There is no setup, no workspace, and nothing to configure.

<!-- zh-CN:begin 3685ee0cf47778bf -->

之后只是起草。文件写入当前目录 `to-questionnaire-<slug>.md`。无设置、工作区或配置。

<!-- zh-CN:end 3685ee0cf47778bf -->

## The document

<!-- zh-CN:begin 278f02852e24e85c -->

## 文档内容

<!-- zh-CN:end 278f02852e24e85c -->

The document is a **discovery questionnaire**, because you lack the context and the recipient has it. That sets its shape:

<!-- zh-CN:begin 7415fc00279b1a1d -->

这是**发现问卷**：你缺背景，接收者拥有背景。结构如下：

<!-- zh-CN:end 7415fc00279b1a1d -->

- A purpose line naming the decision that depends on it, and a short context section for a recipient who knows none of your background.

<!-- zh-CN:begin 2373a65101a05e9b -->

- 目的行说明依赖该答案的决策，并给不熟悉背景的人简短上下文。

<!-- zh-CN:end 2373a65101a05e9b -->
- Questions ordered **most-important-first** and grouped under themed headings, because async means you may only get one pass.

<!-- zh-CN:begin cc0ee4e0312c30d4 -->

- 问题按**最重要优先**排序并按主题分组，因为异步可能只有一次回复机会。

<!-- zh-CN:end cc0ee4e0312c30d4 -->
- One idea per question, never compound, with an answer stub beneath it and a *why this matters* line only where a question could be misread.

<!-- zh-CN:begin 941e09a9f316ef10 -->

- 每问只含一个想法，绝无复合问题；下方留答案位，只在可能误解时写“为何重要”。

<!-- zh-CN:end 941e09a9f316ef10 -->
- Explicit permission to answer "I don't know", because a flagged uncertainty is useful and a confident guess that reads like a fact is not.

<!-- zh-CN:begin a8d390307ce46942 -->

- 明确允许回答“不知道”，因为标出的不确定有用，伪装事实的自信猜测无用。

<!-- zh-CN:end a8d390307ce46942 -->
- A closing catch-all: anything we didn't ask that we should know?

<!-- zh-CN:begin 8ea76700782fa3cc -->

- 结尾兜底问题：还有什么是我们没问但应当知道的？

<!-- zh-CN:end 8ea76700782fa3cc -->

The document is deliberately not two things. It isn't **branching**. The questions are a flat, grouped list, not a tree that skips section D if you answered A. It isn't **multi-recipient** either. One run produces one document for one person.

<!-- zh-CN:begin f307e14c2f2238d2 -->

文档刻意为非分支式：问题是分组平面列表，不按答案跳过后续。每次只为一人生成，不支持多收件人。

<!-- zh-CN:end f307e14c2f2238d2 -->

## Common questions

<!-- zh-CN:begin 3751c1b96853234e -->

## 常见问题

<!-- zh-CN:end 3751c1b96853234e -->

**Does it read my grilling session and extract the questions from it?**
Not as a step of its own. The skill has no ingest phase. It asks about the send, then drafts. What makes it work after a grilling session is that you run it in the **same conversation**, so the [session](https://www.aihero.dev/ai-coding-dictionary/session) is already in [context](https://www.aihero.dev/ai-coding-dictionary/context) and the drafting can draw on it. If you start it in a fresh session, it knows nothing about the grilling, and you supply the topic again yourself when you answer "what do you need back?".

<!-- zh-CN:begin e524fc4c47e468aa -->

**会读取追问会话并自动提取问题吗？**
没有独立读取阶段：先问发送方式再起草。同一对话中运行可利用已有 [session](https://www.aihero.dev/ai-coding-dictionary/session) 和 [context](https://www.aihero.dev/ai-coding-dictionary/context)；新会话则完全不知道追问内容，需要你再次提供问题。

<!-- zh-CN:end e524fc4c47e468aa -->

**The missing answers don't all live with the same person. Can it split them by recipient?**
No. Step one asks for *the* recipient, singular, and the skill pitches the tone and context of the whole document at them. If three people hold three parts of the answer, run it three times, once per person. People have asked for one document that routes questions by discipline or role, but that did not ship.

<!-- zh-CN:begin 506feac4c1e6911c -->

**缺失答案不属于同一个人，能按接收者拆分吗？**
不能。第一步只接受一个接收者，语气和上下文均面向此人。三个人各持答案时运行三次；按学科分流的单文档请求尚未实现。

<!-- zh-CN:end 506feac4c1e6911c -->

**Are the questions dependent: does it skip sections based on earlier answers?**
No. The dependent-question design was explored and did not ship. The output is a static document: themed groups, most-important-first, every question live. The objection to it is fair. A [model](https://www.aihero.dev/ai-coding-dictionary/model) that plans more than two or three questions ahead of a real answer plans badly, and a branching document has to plan all of them ahead of every answer.

<!-- zh-CN:begin c4ce0075fe5f55f2 -->

**问题会依赖前答并跳过章节吗？**
不会。依赖式设计已探索但未发布。输出是静态文档：主题分组、最重要优先、每题都必答。这个限制合理：模型提前规划两三个问题尚可，分支文档却要在答案前规划全部路径，容易规划糟糕。 [链接](https://www.aihero.dev/ai-coding-dictionary/model)

<!-- zh-CN:end c4ce0075fe5f55f2 -->

**What if the recipient doesn't know either?**
The document tells them to say so. It explicitly asks for "I don't know" and partial answers. A flagged uncertainty is worth more than a guess, because a vague answer and a confidently wrong one look identical once they're back in your context.

<!-- zh-CN:begin 2a76d5a08664175f -->

**接收者也不知道怎么办？**
文档要求说明不知道，明确接受部分答案；显式不确定比猜测有价值，模糊答案和自信错误回到上下文时可能看起来一样。

<!-- zh-CN:end 2a76d5a08664175f -->

**Does it send it anywhere (Slack, an issue tracker, email)?**
No. It writes a Markdown file in the current directory and tells you the path. Delivery is yours: paste it into a [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket), drop it in a Slack thread, attach it to an email, or open it on a shared screen and work through it live. People have done all four by hand.

<!-- zh-CN:begin b22f73acd8f6a5a3 -->

**会发送到 Slack、issue 跟踪器或邮件吗？**
不会，只写当前目录 Markdown 并给路径。交付由你完成：粘贴到[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)、Slack 线程、邮件附件，或共享屏幕共同填写。

<!-- zh-CN:end b22f73acd8f6a5a3 -->

**Isn't this just `/grill-me` in batch mode?**
No. `grill-me` already asks in **rounds**. It asks the whole frontier of open questions at once, then recomputes it from your answers, so it already meets the "give me all the questions at once" need. `to-questionnaire` differs on another axis. It is about whose head the answers are in, not how the questions are delivered. To answer them yourself faster, use `grill-me`. To get them out of someone else, use this.

<!-- zh-CN:begin 82d193940f053655 -->

**不就是批处理版 `/grill-me` 吗？**
不是。`grill-me` 已按轮次一次提出全部开放问题并依答案重算，满足“一次给所有问题”。本技能的不同维度是答案位于谁的脑中；自己快速回答用 `grill-me`，要问别人用本 `to-questionnaire` 技能。

<!-- zh-CN:end 82d193940f053655 -->

**Couldn't I just ask the agent for this without a skill?**
Yes, and plenty of people did before it existed: `OPEN_QUESTIONS.md` files, spreadsheets sent to clients, a "needs more info" ticket per unanswered question. The skill buys you two things: the interview never drifts onto the subject, and the document comes out in a shape a non-technical recipient can fill in. If you already have a house format that works, you don't need this.

<!-- zh-CN:begin 0d9a93d329c9fa65 -->

**能不能直接让代理做？**
可以，过去人们用 `OPEN_QUESTIONS.md`、发送给客户的表格、每个问题一条“需更多信息”工单。本技能保证访谈不漂向主题，并生成非技术接收者可填的格式；如果已有合适公司模板，就不需要它。

<!-- zh-CN:end 0d9a93d329c9fa65 -->

## It's working if

<!-- zh-CN:begin 79498d15fae13bff -->

## 正常表现

<!-- zh-CN:end 79498d15fae13bff -->

- It asks about the recipient and about what you need back, then stops asking. If it asks about the subject itself, the skill has gone wrong.

<!-- zh-CN:begin 85fd489edb0b8247 -->

- 只问接收者与需要回传内容，然后停止；若追问主题就错了。

<!-- zh-CN:end 85fd489edb0b8247 -->
- Every item you named as "what I need back" is traceable to a question in the file.

<!-- zh-CN:begin 23f1b857d65e843d -->

- 你列出的每个“需要回传项”都能追踪到文件问题。

<!-- zh-CN:end 23f1b857d65e843d -->
- The questions read as aimed at what the *recipient* knows, not as your own open questions copied down verbatim.

<!-- zh-CN:begin 82768171da9ae6c6 -->

- 问题针对接收者知道的内容，而非把你的开放问题原样抄下。

<!-- zh-CN:end 82768171da9ae6c6 -->
- You could hand the file to someone who wasn't in the conversation and they would know why they got it and by when to reply.

<!-- zh-CN:begin 62af0f8ffddfb8c2 -->

- 不在对话中的人拿到文件也知道为何收到、何时回复。

<!-- zh-CN:end 62af0f8ffddfb8c2 -->
- The answers that come back are usable input for a new grilling round, rather than a fresh set of questions.

<!-- zh-CN:begin 7cd3563ae39bb4b7 -->

- 返回答案是新一轮追问的可用输入，而非又一组问题。

<!-- zh-CN:end 7cd3563ae39bb4b7 -->

## Where it fits

<!-- zh-CN:begin 848ce5590bda2de5 -->

## 所处位置

<!-- zh-CN:end 848ce5590bda2de5 -->

`to-questionnaire` is a reach-for-it-anytime standalone. You use it where your own knowledge ends and the next move is to ask another person, not to run another skill. That is most often mid-flow, when planning has stalled on something that isn't yours to decide.

<!-- zh-CN:begin 1e5564beecf83c9f -->

`to-questionnaire` 是随时可用的独立工具：知识边界到此，下一步是问人而非运行其他技能。常用于流程中途、规划被非己职责阻塞时。

<!-- zh-CN:end 1e5564beecf83c9f -->

Its neighbour is [grill-me](https://aihero.dev/skills-grill-me), and the two differ on where the answers live. Grilling gets the answers from you; a questionnaire gets them from someone else. Feed what comes back into another grilling round, or into [grill-with-docs](https://aihero.dev/skills-grill-with-docs) or [to-spec](https://aihero.dev/skills-to-spec) if the work is heading for a build. When you're unsure which skill fits the moment, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin c69a5f9c5ffdfa29 -->

相邻工具是 [grill-me](https://aihero.dev/skills-grill-me)，区别在答案来源。追问从你处获得答案，问卷从别人处获得。把返回内容送入下一轮追问，或在准备构建时交给 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)/[to-spec](https://aihero.dev/skills-to-spec)。不确定时由 [ask-matt](https://aihero.dev/skills-ask-matt) 路由。

<!-- zh-CN:end c69a5f9c5ffdfa29 -->
