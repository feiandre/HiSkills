## What it does

<!-- zh-CN:begin 3d6001ed41cc1467 -->

## 它做什么

<!-- zh-CN:end 3d6001ed41cc1467 -->

`grill-me` takes a **loose idea** and interviews you until you can commit to it. You do not need a worked-out plan to start, because the [session](https://www.aihero.dev/ai-coding-dictionary/session) exists to produce one. It asks in **rounds**. Each round is the whole **frontier**, which is every question whose prerequisites you have already settled. So it never asks you something that depends on an answer it hasn't heard yet.

<!-- zh-CN:begin 8a4b234ca7dad004 -->

`grill-me` 接收一个**粗略想法**，通过访谈你直到你能承诺实施。开始时不需要完整计划，因为[会话](https://www.aihero.dev/ai-coding-dictionary/session)就是为了产出一个计划。它分**轮次**提问。每轮覆盖整个**前沿**，即所有前置条件已经确定的问题。因此它绝不会询问依赖尚未听到答案的内容。

<!-- zh-CN:end 8a4b234ca7dad004 -->

It is **[stateless](https://www.aihero.dev/ai-coding-dictionary/stateless)**. It writes no files and leaves no workspace behind. The only result is a clearer version of the idea, in your own head.

<!-- zh-CN:begin 4fd597d0af2517b4 -->

它是**[无状态](https://www.aihero.dev/ai-coding-dictionary/stateless)**的。不写文件，不留下工作区。唯一结果是更清楚的想法，存在于你的脑中。

<!-- zh-CN:end 4fd597d0af2517b4 -->

## When to reach for it

<!-- zh-CN:begin f9b8272943701fb5 -->

## 何时使用

<!-- zh-CN:end f9b8272943701fb5 -->

You invoke this by typing `/grill-me`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own. Start it in a **fresh conversation**, not on top of a plan you already had an agent write.

<!-- zh-CN:begin a67f61b8739179c6 -->

由你输入 `/grill-me` 调用；[智能体](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行选择。请在**全新对话**中启动，不要在智能体已写好的计划之上启动。

<!-- zh-CN:end a67f61b8739179c6 -->

Reach for it as soon as you have an idea worth taking seriously (a feature, a product direction, a business call, a piece of writing), and long before you have worked out what it involves. Vagueness is not a reason to wait, because the session exists to remove it. If you can already specify the thing precisely, you don't need to grill it.

<!-- zh-CN:begin 625d02f99a98b552 -->

一旦有了值得认真对待的想法（功能、产品方向、商业决定、一篇文章），并在弄清它涉及什么之前尽早使用。含糊不是等待的理由，因为会话正是为了消除含糊。若你已能精确说明该事物，就不需要质询。

<!-- zh-CN:end 625d02f99a98b552 -->

Which of the three grilling skills you want depends on what is in front of you:

<!-- zh-CN:begin ebda503218d1fad2 -->

选择三种质询技能中的哪一种，取决于眼前事物：

<!-- zh-CN:end ebda503218d1fad2 -->

- **Anything, anywhere.** Use `grill-me`. It needs no repo and writes no files, and the subject doesn't have to be code.

<!-- zh-CN:begin a565b8bc72c38300 -->

- **任何事物、任何地方。** 使用 `grill-me`。无需仓库、不写文件，主题也不必是代码。

<!-- zh-CN:end a565b8bc72c38300 -->
- **A codebase to align against.** Use [grill-with-docs](https://aihero.dev/skills-grill-with-docs). It is the same interview, but [stateful](https://www.aihero.dev/ai-coding-dictionary/stateful): it reads your code and keeps what it learns in `GLOSSARY.md` and ADRs.

<!-- zh-CN:begin 6a4a84725934ea85 -->

- **需要对齐代码库。** 使用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。访谈相同，但有[状态](https://www.aihero.dev/ai-coding-dictionary/stateful)：它阅读代码，并把所学记录在 `GLOSSARY.md` 和 ADR 中。

<!-- zh-CN:end 6a4a84725934ea85 -->
- **Too big for one session.** Use [wayfinder](https://aihero.dev/skills-wayfinder). It charts the effort as a map and runs grilling sessions inside it.

<!-- zh-CN:begin d9c8033a270a3f77 -->

- **单个会话容纳不下。** 使用 [wayfinder](https://aihero.dev/skills-wayfinder)。它把工作绘制成地图，并在其中运行质询会话。

<!-- zh-CN:end d9c8033a270a3f77 -->

Leave [plan mode](https://www.aihero.dev/ai-coding-dictionary/agent-mode) off. Plan mode makes the agent hurry to produce a plan, when you want it to keep asking questions.

<!-- zh-CN:begin 68f533d8a808823a -->

关闭[计划模式](https://www.aihero.dev/ai-coding-dictionary/agent-mode)。计划模式会让智能体急于产出计划，而你希望它持续提问。

<!-- zh-CN:end 68f533d8a808823a -->

## It's a conversation, not an interview

<!-- zh-CN:begin b0da539608feffb0 -->

## 这是对话，不是审讯

<!-- zh-CN:end b0da539608feffb0 -->

The skill asks the questions, but **you** own the scope. People often miss this. It is the difference between a session that turns an idea into decisions and one that produces confident nonsense.

<!-- zh-CN:begin 2e1724499e33bb16 -->

技能负责提问，但范围由**你**掌控。人们常忽略这一点。它决定会话是把想法变成决定，还是产出自信的空话。

<!-- zh-CN:end 2e1724499e33bb16 -->

The failure mode is **passivity**: answering "agreed, agreed, agreed" for forty questions and coming out with a plan the agent wrote and you nodded at. It feels productive because it was long. But you decided nothing, and the result looks more certain than it is.

<!-- zh-CN:begin 080d4a1d3e629147 -->

失败模式是**被动**：对四十个问题回答“同意、同意、同意”，最后得到一份智能体编写、你点头的计划。它让人觉得有成效，因为它很长，但你什么也没决定，结果比实际更确定。

<!-- zh-CN:end 080d4a1d3e629147 -->

Being active means steering. Push back on a question that is less detailed than you need. Say when the scope is drifting. Answer "I don't know" and mean it. This skill helps an engineer and does not replace one. The quality of the result depends on the quality of your answers, not on the number of questions.

<!-- zh-CN:begin 2910407f18cf9b8b -->

主动意味着掌舵。问题不够详细时要反驳；范围漂移时要说出来；回答“我不知道”并且是真的。本技能帮助工程师，不替代工程师。结果质量取决于回答质量，而不是问题数量。

<!-- zh-CN:end 2910407f18cf9b8b -->

The opposite error is real but rarer: staying in the interview so long you never reach code.

<!-- zh-CN:begin dd86034231975eeb -->

相反错误真实存在但较少见：访谈太久，始终到不了代码。

<!-- zh-CN:end dd86034231975eeb -->

## Grillable and ungrillable

<!-- zh-CN:begin ea18cad7d568d012 -->

## 可质询与不可质询

<!-- zh-CN:end ea18cad7d568d012 -->

Some questions can be answered by talking. Others can't, and no amount of grilling will get you there.

<!-- zh-CN:begin 5a21bc5429834876 -->

有些问题可以通过谈话回答，另一些不能，再质询也到不了答案。

<!-- zh-CN:end 5a21bc5429834876 -->

"One long form or three pages?" and "how should this interaction feel?" are **ungrillable**. You need something to react to before you can answer them. When you hit one, stop grilling. Build the throwaway version with [prototype](https://aihero.dev/skills-prototype), look at it, then come back and answer in one line.

<!-- zh-CN:begin 0ed0acb2feca497a -->

“要一长页还是三页？”以及“这个交互应该有什么感觉？”无法靠质询解决。你需要先有东西可反应。遇到这种问题就停止质询，使用[原型](https://aihero.dev/skills-prototype)构建一次性版本，观察后回来用一句话回答。

<!-- zh-CN:end 0ed0acb2feca497a -->

Sessions grow too long when you try to talk through an ungrillable question. The agent keeps rephrasing, you keep guessing, and the scope grows with the uncertainty.

<!-- zh-CN:begin 3c1caed6aec64de7 -->

试图谈清不可质询的问题时，会话会过长。智能体反复改写，你不停猜，范围随不确定性增长。

<!-- zh-CN:end 3c1caed6aec64de7 -->

## It's working if

<!-- zh-CN:begin 8abe9eb534b17b68 -->

## 正常工作时的表现

<!-- zh-CN:end 8abe9eb534b17b68 -->

- You disagree with something. A session with no pushback from you is a session you didn't need.

<!-- zh-CN:begin d5f52d47bea3325c -->

- 你会不同意某些内容。完全没有你反驳的会话，是你并不需要的会话。

<!-- zh-CN:end d5f52d47bea3325c -->
- Questions arrive in a few rounds, not one at a time for a long time, and later rounds clearly build on what you said earlier.

<!-- zh-CN:begin e20e6fd7367e19d4 -->

- 问题按几轮到达，而非很久才问一个；后续轮次明显建立在你先前回答上。

<!-- zh-CN:end e20e6fd7367e19d4 -->
- You end up somewhere you didn't expect, because a question showed you a decision you had been making without noticing.

<!-- zh-CN:begin 37aa8830aa109c6b -->

- 你最终到达意料之外的位置，因为某个问题揭示了你在无意中作出的决定。

<!-- zh-CN:end 37aa8830aa109c6b -->
- At the end you could defend each choice to someone who wasn't there.

<!-- zh-CN:begin c6fae46517dfdace -->

- 结束时，你能向不在场者说明每个选择。

<!-- zh-CN:end c6fae46517dfdace -->

## Common questions

<!-- zh-CN:begin bab97fc7002eddc8 -->

## 常见问题

<!-- zh-CN:end bab97fc7002eddc8 -->

**How many questions should I expect, and how do I know when it ends?**
Count rounds, not questions. Forty-six questions across four rounds is an ordinary session. It ends when the frontier is empty: it has visited every branch, and nothing is left as an unstated assumption.

<!-- zh-CN:begin c8feae1ad1569b6c -->

**应该预期多少问题，怎样知道结束？**
数轮次，不数问题。四轮共四十六个问题很正常。前沿为空时结束：每个分支都已访问，没有未声明的假设。

<!-- zh-CN:end c8feae1ad1569b6c -->

**It asked me two hundred questions. What went wrong?**
Usually the scope was too large. Ask the agent to break the work into smaller pieces first, then grill each one. Very long sessions also drift into the **[dumb zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone)**, where the [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) is full enough that the questions get worse.

<!-- zh-CN:begin 1274c11a34e85113 -->

**它问了我两百个问题。哪里错了？**
通常范围太大。先让智能体把工作拆成更小部分，再逐一质询。超长会话也会漂移到**[迟钝区](https://www.aihero.dev/ai-coding-dictionary/smart-zone)**，此时[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)已太满，问题会变差。

<!-- zh-CN:end 1274c11a34e85113 -->

**Can I go back to one question at a time?**
Yes. Add this to your global `CLAUDE.md`:

<!-- zh-CN:begin 912d084d080c1a7d -->

**可以恢复一次只问一个问题吗？**
可以。把以下内容加入全局 `CLAUDE.md`：

<!-- zh-CN:end 912d084d080c1a7d -->

```
When grilling, ask one question at a time.
```

<!-- zh-CN:begin cfa4d909d6711a13 -->

```
质询时，一次只问一个问题。
```

<!-- zh-CN:end cfa4d909d6711a13 -->

**What if I genuinely don't know the answer?**
Say so. "I don't know" is a real answer, and a question you can't answer is usually a sign to prototype rather than to guess.

<!-- zh-CN:begin 7fe9e32c6325f8b1 -->

**如果我真的不知道答案呢？**
直说。“我不知道”是真实答案，无法回答的问题通常意味着应该做原型，而不是猜。

<!-- zh-CN:end 7fe9e32c6325f8b1 -->

**Do I start a fresh session before writing the spec?**
No. The value of the session is the [context](https://www.aihero.dev/ai-coding-dictionary/context) you just built. Hand the same conversation straight to [to-spec](https://aihero.dev/skills-to-spec).

<!-- zh-CN:begin bba4c18c9fce9041 -->

**写规格前要开新会话吗？**
不要。会话的价值是你刚构建的[上下文](https://www.aihero.dev/ai-coding-dictionary/context)。直接把同一对话交给 [to-spec](https://aihero.dev/skills-to-spec)。

<!-- zh-CN:end bba4c18c9fce9041 -->

**Does the model matter?**
More than for most skills. Grilling depends on the [model](https://www.aihero.dev/ai-coding-dictionary/model)'s own knowledge of how systems break, so use your best one. Implementation mostly follows context, so a cheaper model is fine there.

<!-- zh-CN:begin fba3d7a9559e828c -->

**模型重要吗？**
比多数技能更重要。质询依赖[模型](https://www.aihero.dev/ai-coding-dictionary/model)自身关于系统如何损坏的知识，应使用最好的模型。实现主要遵循上下文，较便宜的模型即可。

<!-- zh-CN:end fba3d7a9559e828c -->

## Where it fits

<!-- zh-CN:begin 6d82577e405e8ab1 -->

## 所处位置

<!-- zh-CN:end 6d82577e405e8ab1 -->

`grill-me` is a **standalone you can run anywhere, on anything**. Because it is stateless, it is portable. It needs no repo, workspace, or setup, and does not assume the idea is about software. People use it for business decisions, for writing, and for what to do next: anything they cannot think through clearly on their own.

<!-- zh-CN:begin 9d53769782e523be -->

`grill-me` 是**可在任何地方对任何事物运行的独立技能**。因为无状态，所以可移植。无需仓库、工作区或设置，也不假设想法与软件有关。人们用它处理商业决定、写作和下一步行动，即任何无法独自想清楚的事。

<!-- zh-CN:end 9d53769782e523be -->

Portability is the only difference from [grill-with-docs](https://aihero.dev/skills-grill-with-docs). That skill runs the same interview, but reads a codebase to align against and records what it learns as `GLOSSARY.md` and ADRs. Both use the [grilling](https://aihero.dev/skills-grilling) skill underneath. `grill-me` is the user-invoked entry point that keeps no state.

<!-- zh-CN:begin 20f128904b938d7e -->

可移植性是它与 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 的唯一区别。后者执行同样访谈，但会读取代码库以对齐，并把所学记录为 `GLOSSARY.md` 和 ADR。两者底层都使用[质询](https://aihero.dev/skills-grilling)技能。`grill-me` 是用户调用且不保存状态的入口。

<!-- zh-CN:end 20f128904b938d7e -->

If what you grilled does turn out to be software, you can hand the same conversation to [to-spec](https://aihero.dev/skills-to-spec) and carry on into the build flow (an option, not the point of the skill). When you're unsure which flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 1f95c007c1d92161 -->

如果你质询的内容确实是软件，可把同一对话交给 [to-spec](https://aihero.dev/skills-to-spec)，继续进入构建流程（这是选项，不是技能目的）。不确定流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你路由。

<!-- zh-CN:end 1f95c007c1d92161 -->
