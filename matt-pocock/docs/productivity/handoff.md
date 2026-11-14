## What it does

<!-- zh-CN:begin cab17638c77d0b77 -->

## 它的作用

<!-- zh-CN:end cab17638c77d0b77 -->

`handoff` compacts the conversation you are in into a **handoff document**: one markdown file, written to your OS's temporary directory rather than into the workspace, that a fresh [agent](https://www.aihero.dev/ai-coding-dictionary/agent) can read to pick the work up.

<!-- zh-CN:begin 88e67dcee08f6381 -->

`handoff` 将当前对话压缩成一份**交接文档**：一个 Markdown 文件，写入操作系统临时目录而非工作区，新[代理](https://www.aihero.dev/ai-coding-dictionary/agent)可读取它接续工作。

<!-- zh-CN:end 88e67dcee08f6381 -->

What it gives you is **portability**, not compression, so the skill is narrower than it sounds. You need a file only when the work has to *travel*: to a new [harness](https://www.aihero.dev/ai-coding-dictionary/harness), a new directory, a colleague, or a side task you want to fork off. If nothing is travelling, you do not need a handoff. Staying in the [session](https://www.aihero.dev/ai-coding-dictionary/session), `/clear`, a [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) and `/compact` cover the ordinary end-of-phase case, and `/compact` covers it more often than this skill does.

<!-- zh-CN:begin 52bb94e8e9e80684 -->

它提供的是**可移植性**，而非压缩，因此技能范围比听起来更窄。只有工作需要*转移*时才需要文件：到新[运行环境](https://www.aihero.dev/ai-coding-dictionary/harness)、新目录、同事处，或想分叉出的旁支任务。无需转移时，不需要交接。留在[会话](https://www.aihero.dev/ai-coding-dictionary/session)、`/clear`、[子代理](https://www.aihero.dev/ai-coding-dictionary/subagent) 与 `/compact` 足以覆盖常见阶段结束情形，而 `/compact` 比本技能更常用于此。

<!-- zh-CN:end 52bb94e8e9e80684 -->

## When to reach for it

<!-- zh-CN:begin b433948c82e56e31 -->

## 何时使用

<!-- zh-CN:end b433948c82e56e31 -->

You invoke this by typing `/handoff`; the agent won't reach for it on its own. Pass a note about what the next session is for, and the skill writes the document for that purpose.

<!-- zh-CN:begin c13598542e3c2095 -->

你通过输入 `/handoff` 调用；代理不会自行使用。说明下一会话用途，技能就按该用途写文档。

<!-- zh-CN:end c13598542e3c2095 -->

There are four triggers, and only four:

<!-- zh-CN:begin 1fb5e95ac6366cd9 -->

只有四种触发情形：

<!-- zh-CN:end 1fb5e95ac6366cd9 -->

| Situation | Why a file |
| --- | --- |
| Swapping harness (Claude → Codex) | The new harness cannot see the old [context](https://www.aihero.dev/ai-coding-dictionary/context) |
| Moving to a different directory or repo | A prototype directory is the common case |
| Sending the work to a colleague | They need something they can read |
| Forking a side task found mid-phase | You keep working; a second agent takes the fork |

<!-- zh-CN:begin 9c370cbe06d2c483 -->

| 情形 | 为什么需要文件 |
| --- | --- |
| 更换运行环境（Claude → Codex） | 新环境看不到旧[上下文](https://www.aihero.dev/ai-coding-dictionary/context) |
| 换到不同目录或仓库 | 常见情形是原型目录 |
| 将工作交给同事 | 对方需要可阅读的材料 |
| 分叉阶段中途发现的旁支任务 | 你继续工作，第二个代理接走分叉 |

<!-- zh-CN:end 9c370cbe06d2c483 -->

For anything else (same harness, same directory, you are done [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) and moving to implementation), use `/compact`. [ask-matt](https://aihero.dev/skills-ask-matt) has the ordered tree over all five options at a phase boundary.

<!-- zh-CN:begin 88e1daa0c0ba2697 -->

其他情况（同一运行环境、同一目录，你已完成[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)并进入实施）用 `/compact`。[ask-matt](https://aihero.dev/skills-ask-matt) 提供阶段边界五种选项的有序决策树。

<!-- zh-CN:end 88e1daa0c0ba2697 -->

## Branching is the use people skip

<!-- zh-CN:begin 925f7a5d26ae5d3e -->

## 分叉是人们常忽略的用法

<!-- zh-CN:end 925f7a5d26ae5d3e -->

The skill's description reads like session resumption: write a summary, end here, resume there. Read that way, it looks like a worse `/compact`, so people skip it. The fork case is the one worth knowing. You **stay in your session** and hand a copy of the accumulated context to a second agent working in parallel.

<!-- zh-CN:begin b599a6fa26d2054b -->

技能描述读起来像恢复会话：写总结、在此结束、到那里继续。这样理解，它像更差的 `/compact`，人们便跳过。分叉才值得了解。你**留在当前会话**，把已积累上下文的副本交给并行工作的第二个代理。

<!-- zh-CN:end b599a6fa26d2054b -->

That is what the detour through [prototype](https://aihero.dev/skills-prototype) uses. You are deep in a design conversation, you hit a question that only running code will settle, and you do not want to spend the thread you built on finding out. Hand off to a prototype session, get the answer, hand the answer back, and reference it from the original thread. The work crosses over twice, your original conversation stays live, and you re-explain nothing.

<!-- zh-CN:begin 3a4b479bcbcf0efc -->

经由 [prototype](https://aihero.dev/skills-prototype) 的绕行正使用这一方式。你深入设计讨论，遇到只有运行代码才能解决的问题，又不想把建立起来的对话线程花在调查上。交给原型会话，拿到答案，再交回来，并从原线程引用。工作往返两次，原对话保持活跃，你无需重新解释。

<!-- zh-CN:end 3a4b479bcbcf0efc -->

Three of the five options at a phase boundary preserve different things: `/compact` preserves your intent, `/clear` preserves nothing, `/handoff` preserves the work's ability to move.

<!-- zh-CN:begin 2acee41143e23cdc -->

阶段边界的五种选项中，三者保留不同内容：`/compact` 保留意图，`/clear` 什么都不保留，`/handoff` 保留工作转移的能力。

<!-- zh-CN:end 2acee41143e23cdc -->

## What travels, and what doesn't

<!-- zh-CN:begin e95b0bc04ed4879f -->

## 什么会转移，什么不会

<!-- zh-CN:end e95b0bc04ed4879f -->

The document carries the live thread (what's in flight, why, and what's next) plus a **suggested skills** section naming what the next agent should reach for. The skill redacts secrets before it writes the file.

<!-- zh-CN:begin 81f8b1b44c68bba2 -->

文档携带当前进行中的脉络（什么在进行、为什么、下一步），并有一个**建议技能**章节，指出下一位代理应使用的技能。技能写入前会脱敏秘密。

<!-- zh-CN:end 81f8b1b44c68bba2 -->

It deliberately does not carry anything already written down. The document references specs, plans, ADRs, issues, commits and diffs by path or URL, and never copies them. That keeps the file small, and it keeps the settled detail in one place instead of two copies that drift apart.

<!-- zh-CN:begin 0bce58734c77c9d4 -->

它刻意不携带已写下的内容。文档以路径或 URL 引用规格、计划、ADR、问题、提交和差异，绝不复制它们。这使文件较小，也让已确定的细节只有一个位置，而不是两份会漂移的副本。

<!-- zh-CN:end 0bce58734c77c9d4 -->

## Common questions

<!-- zh-CN:begin 3ece256473e9d3fa -->

## 常见问题

<!-- zh-CN:end 3ece256473e9d3fa -->

**Handoff or compact?**
`/compact` unless something is travelling. Staying on the same task is a compact, not a handoff. When the harness and directory stay the same and you need to stay in the loop, the phase-boundary tree ends at `/compact` most days. `/handoff` does not summarise better. Its advantage is that the result is a file you can carry somewhere `/compact` can't reach.

<!-- zh-CN:begin 401989d6bc516217 -->

**交接还是压缩？**
除非有内容需要转移，否则用 `/compact`。留在同一任务是压缩，不是交接。运行环境和目录不变且你需要留在循环中时，阶段边界决策树大多数时候落在 `/compact`。`/handoff` 并不会总结得更好，优势是结果成为可带到 `/compact` 到不了之处的文件。

<!-- zh-CN:end 401989d6bc516217 -->

**So what's the actual difference between compact, clear and handoff?**
Each one preserves something different. `/compact` compresses this context and continues in a fresh window, so your intent survives. `/clear` empties the window and starts from nothing. That is correct when everything behind you is disposable, and you cannot undo it if it isn't. `/handoff` writes a portable file, so the work survives the move to somewhere else. All three turn a **[primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source)** (the conversation as it happened) into a **[secondary source](https://www.aihero.dev/ai-coding-dictionary/secondary-source)** (a summary of it). Continuing is the only option that doesn't, which is why you rule it out first.

<!-- zh-CN:begin d4ba4e00be17537e -->

**压缩、清空和交接的实际区别是什么？**
各自保留不同内容。`/compact` 压缩当前上下文并在新窗口继续，因此意图保留。`/clear` 清空窗口，从零开始；身后内容都可丢弃时合适，若不可丢弃就无法撤销。`/handoff` 写出可移植文件，使工作能转移到别处。三者都把**[一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)**（按原样发生的对话）变成**[二手来源](https://www.aihero.dev/ai-coding-dictionary/secondary-source)**（它的总结）。直接继续是唯一不这样做的选项，因此先排除它。

<!-- zh-CN:end d4ba4e00be17537e -->

**Where did my handoff file go?**
It goes to the temp directory, which is the most-reported problem with the skill. The skill resolves it as `$TMPDIR`, else `/tmp` (`%TEMP%` on Windows), but the paths are long. Ask for the path back and keep it before you move on. Temp is deliberate, because a handoff is a document in transit, not an artifact you maintain. Temp is also not durable, as the next question explains.

<!-- zh-CN:begin 9b2562c24e7e6a1c -->

**交接文件去哪儿了？**
它写入临时目录，这是技能报告最多的问题。技能解析为 `$TMPDIR`，否则 `/tmp`（Windows 上 `%TEMP%`），路径很长。继续前要求返回路径并保留。使用临时目录是刻意的，因为交接是传输中的文档，不是维护的产物。临时目录也不持久，下一问题会解释。

<!-- zh-CN:end 9b2562c24e7e6a1c -->

**My handoff vanished between sessions.**
Some environments clear temp between sessions (Codex is the reported case), and a reboot empties `/private/tmp`. If the next session isn't starting within the hour, or is starting under a different harness, copy the file somewhere durable yourself as soon as it's written. The same applies to anything the document *points at*: if a dispatch references other files in temp, the next agent can't follow it.

<!-- zh-CN:begin 327e0a9eed8c5e6b -->

**我的交接文件在会话之间消失了。**
有些环境会在会话间清理临时目录（据报告 Codex 会如此），重启也会清空 `/private/tmp`。下一会话若不在小时内开始，或改在别的运行环境开始，就在文件写好后自行复制到持久位置。文档*指向*的内容也一样：分派若引用临时目录中的其他文件，下一位代理无法跟进。

<!-- zh-CN:end 327e0a9eed8c5e6b -->

**How do I actually hand it to the next agent?**
Open the fresh session and point it at the path: read this file, then continue. Point at the file rather than pasting the summary into a shell command. The shell mangles a summary that contains backticks or `$(...)` when you interpolate it into `claude "<summary>"`. The usual result is silent truncation rather than an error, so the new agent starts with an incomplete brief and nothing tells you.

<!-- zh-CN:begin d0c096bb9c3afaf9 -->

**实际如何交给下一位代理？**
打开新会话并指向路径：读取此文件，然后继续。指向文件，而不是把总结粘贴进 shell 命令。将含反引号或 `$(...)` 的总结插入 `claude "<summary>"` 时，shell 会破坏它。常见结果是静默截断而不是报错，于是新代理从残缺简报开始却没人告诉你。

<!-- zh-CN:end d0c096bb9c3afaf9 -->

**Is this the same as `/branch`, `--fork-session`, or the built-in `/handoff`?**
They are similar, not identical. `/branch` isn't a shipped skill here; `/handoff` is the canonical name. A fork inherits an exact copy of the context; this skill produces a *targeted* compression aimed at a stated next task, in a file. Where a fork will do (same machine, same harness, same directory), a fork is less work. The file is the better choice when the destination is somewhere the fork can't go.

<!-- zh-CN:begin eb98957343e9413e -->

**它与 `/branch`、`--fork-session` 或内置 `/handoff` 相同吗？**
相似但不相同。`/branch` 在此不是已发布技能；`/handoff` 是规范名称。分叉继承精确上下文副本；本技能面向指定下一任务生成*有目标*的压缩文件。同机器、同运行环境、同目录时，分叉更省事。目的地在分叉无法抵达之处时，文件更合适。

<!-- zh-CN:end eb98957343e9413e -->

**When does something belong in `CLAUDE.md` instead?**
Ask whether it's true next month. `CLAUDE.md` is standing context about the project, loaded into every session whether it's relevant or not. A handoff is about one piece of work in flight and is useless once that work lands. If you keep re-explaining a fact, it belongs in `CLAUDE.md`. A half-finished task belongs in a handoff.

<!-- zh-CN:begin 6129503fe0d87774 -->

**哪些内容应放进 `CLAUDE.md`？**
问它下个月是否仍成立。`CLAUDE.md` 是项目常驻上下文，每个会话无论是否相关都会加载。交接针对一项进行中的工作，工作完成后就无用。反复解释的事实属于 `CLAUDE.md`；半完成任务属于交接。

<!-- zh-CN:end 6129503fe0d87774 -->

**It captures the what, not the why.**
This is a fair criticism, and people raise it often. Two things help. Pass the argument (tell it what the next session is for), so the skill keeps the reasoning that bears on *that* rather than flattening it. And watch for confident claims the session never verified, such as "X isn't built" or "Y is done". The next agent trusts the document and does not re-check it, so a belief written as a fact becomes a false premise for everything that follows. Read the document before you hand it over, and downgrade anything you only assumed.

<!-- zh-CN:begin 3878aa23972c5602 -->

**它记录做什么，却没记录为什么。**
这是合理批评，常有人提出。两种办法有帮助：传入论点（告诉它下一会话用途），技能便保留与*该用途*有关的推理，而不是抹平；再留意会话从未验证却自信陈述的内容，例如“X 尚未构建”或“Y 已完成”。下一位代理信任文档且不再核查，因此把信念写成事实会成为后续一切的假前提。交付前阅读文档，把只是假定的内容降级。

<!-- zh-CN:end 3878aa23972c5602 -->

**Why is it a skill rather than a slash command?**
Both work; they suit different situations. As a skill, it ships and updates through the same install path as everything else here, which makes it shareable. Its frontmatter, not the mechanism, is what stops the agent from firing it on its own.

<!-- zh-CN:begin ce673996279dba2c -->

**为什么是技能而不是斜杠命令？**
两者都可行，适合不同情形。作为技能，它通过此仓库其他内容相同的安装路径发布更新，因而可分享。阻止代理自行触发的机制是 frontmatter，而非技能形式。

<!-- zh-CN:end ce673996279dba2c -->

## It's working if

<!-- zh-CN:begin 1b27a6d9d09593ed -->

## 正常工作的表现

<!-- zh-CN:end 1b27a6d9d09593ed -->

- The document is a small fraction of the conversation, and the specs, issues and diffs appear in it as paths and URLs rather than as copied text.

<!-- zh-CN:begin 432e12d2cd1a217a -->

- 文档只占对话很小比例，规格、问题和差异以路径与 URL 出现，并非复制文本。

<!-- zh-CN:end 432e12d2cd1a217a -->
- You can read it cold, without the original session open, and know what to do next.

<!-- zh-CN:begin 254bf2dc1af8b596 -->

- 不打开原会话也能冷读它，并知道下一步做什么。

<!-- zh-CN:end 254bf2dc1af8b596 -->
- The fresh agent starts working instead of asking you to re-explain the setup.

<!-- zh-CN:begin 85d7f84c64662cc9 -->

- 新代理直接开始工作，不要求你重新解释设置。

<!-- zh-CN:end 85d7f84c64662cc9 -->
- In the fork case, your original session is unchanged when you come back to it.

<!-- zh-CN:begin d76a1b5fec5e9f6c -->

- 分叉情形下，你返回原会话时它没有改变。

<!-- zh-CN:end d76a1b5fec5e9f6c -->
- The suggested-skills section names the skill you'd have reached for yourself.

<!-- zh-CN:begin e6a1fb3c1d0ac38f -->

- 建议技能章节点出你自己也会选择的技能。

<!-- zh-CN:end e6a1fb3c1d0ac38f -->
- Nothing in it is a key, a token, or a password.

<!-- zh-CN:begin fd7d83d24adce9c0 -->

- 其中没有密钥、令牌或密码。

<!-- zh-CN:end fd7d83d24adce9c0 -->

## Where it fits

<!-- zh-CN:begin a1ec33bc2b35819a -->

## 所处位置

<!-- zh-CN:end a1ec33bc2b35819a -->

`handoff` is a **reach-for-it-anytime standalone**. It works between sessions rather than inside a build chain. It is a narrow one, and you'll use it less often than the other four options at a phase boundary. Its closest neighbour is [prototype](https://aihero.dev/skills-prototype), because a prototype lives in its own directory and the round trip out and back is the move this skill is for. When you're at a boundary and unsure whether to continue, clear, hand off, delegate or compact, [ask-matt](https://aihero.dev/skills-ask-matt) has the tree that orders those five, and routes you across the rest of the set.

<!-- zh-CN:begin 79e53947f07aeef1 -->

`handoff` 是**随时可用的独立技能**。它在会话之间工作，不属于构建链内部。范围很窄，在阶段边界的其他四个选项中会较少使用。邻近技能是 [prototype](https://aihero.dev/skills-prototype)，因为原型位于自己的目录，而本技能正用于往返。处于边界且不确定继续、清空、交接、委派还是压缩时，[ask-matt](https://aihero.dev/skills-ask-matt) 提供五种选项的决策树并为你路由整个技能集。

<!-- zh-CN:end 79e53947f07aeef1 -->
