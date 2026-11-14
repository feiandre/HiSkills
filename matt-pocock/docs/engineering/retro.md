## What it does

<!-- zh-CN:begin bb7035ac7ece3af7 -->

## 它做什么

<!-- zh-CN:end bb7035ac7ece3af7 -->

`retro` looks back over a coding [session](https://www.aihero.dev/ai-coding-dictionary/session) and suggests improvements to the agent's **[environment](https://www.aihero.dev/ai-coding-dictionary/environment)**, so the next run goes better. It reads the session's own record (the current one by default, or one you point it at in the session logs). It finds the moments where the agent struggled, and gives you a list of candidate fixes, most severe first.

<!-- zh-CN:begin 35b3731626987916 -->

`retro` 回顾编码[会话](https://www.aihero.dev/ai-coding-dictionary/session)，建议改进代理**[环境](https://www.aihero.dev/ai-coding-dictionary/environment)**，使下次更好。它读取会话记录（默认当前会话，也可指定日志），找出代理受阻时刻，并按严重度列出候选修复。

<!-- zh-CN:end 35b3731626987916 -->

It changes the environment, not the code. Take the bug the agent shipped, the file it needed twenty [tool calls](https://www.aihero.dev/ai-coding-dictionary/tool-call) to find, or the rule the reviewer missed. `retro` does not fix any of them directly. It asks what in the repo let them happen, and proposes the check, pointer, or standard that prevents them next time. It also only proposes. Nothing changes until you pick a candidate.

<!-- zh-CN:begin 74c2c1c763bc2e60 -->

它改环境，不改代码。无论代理交付了缺陷、为找文件用了二十次[工具调用](https://www.aihero.dev/ai-coding-dictionary/tool-call)，还是审查者漏掉规则，它都不直接修，而问仓库中什么导致发生，并提议防止复发的检查、指针或标准。它只提议；你选定前不改变；其中相关的字段或标识包括 `retro`。

<!-- zh-CN:end 74c2c1c763bc2e60 -->

## When to reach for it

<!-- zh-CN:begin 2ac2d52e280a577a -->

## 何时使用

<!-- zh-CN:end 2ac2d52e280a577a -->

You invoke this by typing `/retro`, and the agent won't reach for it on its own.

<!-- zh-CN:begin f771f4241c02242e -->

输入 `/retro`，代理不会自行使用。

<!-- zh-CN:end f771f4241c02242e -->

Reach for it at the end of a session that was harder than it should have been. For example, the agent searched too long for something, made a mistake a tool could have caught, or needed information it could not get. A smooth session has little to teach, and the findings come from the difficult ones. If you want a verdict on the code the session produced, use [code-review](https://aihero.dev/skills-code-review) instead.

<!-- zh-CN:begin 635406491e62e6ab -->

会话比应更难时使用：搜索过久、工具本可捕获的错误或无法获得必要信息。顺畅会话学不到什么，困难会话才有发现。要评判代码，使用 [code-review](https://aihero.dev/skills-code-review)。

<!-- zh-CN:end 635406491e62e6ab -->

## Where the findings land

<!-- zh-CN:begin 86d2e4428ab48aeb -->

## 发现落在哪里

<!-- zh-CN:end 86d2e4428ab48aeb -->

Each candidate belongs to one category, and the category decides where the fix goes:

<!-- zh-CN:begin 4cd5e3652c8dffc2 -->

每个候选项属一类，类别决定修复位置：

<!-- zh-CN:end 4cd5e3652c8dffc2 -->

| What went wrong in the session | Fix it with |
| --- | --- |
| The agent took a long time to find a file or fact | A **navigation pointer** from a file it already reads |
| It made a mistake a tool could have caught | An **[automated check](https://www.aihero.dev/ai-coding-dictionary/automated-check)**: lint rule, type, test, pre-commit hook, CI job |
| The reviewer missed a judgement-call mistake | A rule in `CODING_STANDARDS.md` for the reviewer agent |
| `AGENTS.md` or `CLAUDE.md` is large | Move its steering out, into standards or checks |
| A tool call was expensive for what it returned | Streamline the tool, or replace it |
| A steering file is full of lines that change nothing | Delete the **no-ops** |
| The agent needed information it couldn't reach | Widen its access: tee the dev server log to a file, give read-only access to a service |

<!-- zh-CN:begin 885a7014fd9708b6 -->

| 会话问题 | 修复方式 |
| --- | --- |
| 找文件/事实耗时 | 已读文件加**导航指针** |
| 工具可捕获的错误 | **[自动检查](https://www.aihero.dev/ai-coding-dictionary/automated-check)**：lint、类型、测试、钩子、CI |
| 审查者漏掉判断错误 | 审查代理读取的 `CODING_STANDARDS.md` 规则 |
| `AGENTS.md` 或 `CLAUDE.md` 过大 | 将指导移至标准或检查 |
| 工具调用与回报不划算 | 精简或替换 |
| 指导文件有无效行 | 删除**无效指令** |
| 代理无法访问所需信息 | 放宽访问：写日志到文件、给只读服务权限 |

<!-- zh-CN:end 885a7014fd9708b6 -->

The leading idea is that standards belong to the **reviewer**, not the implementer. The implementing agent has the most context pressure, because it explores, writes code, and debugs failures. The reviewing agent gets a diff and nothing else. So a new rule goes where there is room to apply it, which is review. It never goes in [AGENTS.md](https://www.aihero.dev/ai-coding-dictionary/agents-md), which loads into every session's [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) whether it is relevant or not.

<!-- zh-CN:begin 3dd18ee543a777de -->

核心理念：标准属于**审查者**而非实现者。实现代理上下文压力最大，审查者只拿差异，因此新规则放审查，不放每会话加载的 [AGENTS.md](https://www.aihero.dev/ai-coding-dictionary/agents-md)，也不放每会话的[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)。。

<!-- zh-CN:end 3dd18ee543a777de -->

Before `retro` writes any rule, it classifies the violation. A **mechanical** violation (a banned API, an import shape, a file-location rule) gets a deterministic check, because a check can fail and a sentence in a standards file can't. Only real judgement calls, which no linter can enforce, become prose. If the repo has no guardrail at all (no pre-commit hook, and no CI job that runs lint, typecheck, and tests), `retro` reports that as a finding of its own.

<!-- zh-CN:begin 5cf6625da8708b40 -->

写规则前先分类：**机械**违规（禁用 API、导入形状、文件位置）用确定性检查；只有 linter 无法执行的判断才写文字。若仓库无预提交钩子且 CI 不跑 lint、类型和测试，`retro` 将此 itself 报告为发现；其中相关的字段或标识包括 `retro`。

<!-- zh-CN:end 5cf6625da8708b40 -->

## Common questions

<!-- zh-CN:begin 2c82486435111a97 -->

## 常见问题

<!-- zh-CN:end 2c82486435111a97 -->

**Does it write the lint rule itself, or wait for a yes? Can I wire it to run after every session?**

<!-- zh-CN:begin cbf7b775193d54dd -->

**会自行写 lint 规则，还是等确认？能每会话后自动运行吗？**

<!-- zh-CN:end cbf7b775193d54dd -->

It waits. `retro` only proposes. Nothing changes until you pick a candidate, so it edits nothing by hand and installs no hook automatically. This is deliberate. One user asked for exactly this after being "burned by auto-hooks that blocked good changes." It takes judgement to decide what deserves a permanent check, so the skill stays [human-in-the-loop](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop) and user-invoked. Some users do run it after every implementation run. But a smooth session has little to teach, so a run after every session mostly produces rules nobody needed. There is no dry-run mode. A proposed check is code like any other, so try it against the repo before you let it block merges.

<!-- zh-CN:begin ae6f7004141953b2 -->

等待；只提议，你选择后才改。刻意不自动安装钩子。已有用户被“阻止好改动的自动钩子”坑过。是否值得永久检查需判断，所以技能保持[人在环中](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop)并用户调用。有人每次都运行，但顺畅会话只会生成无用规则。没有 dry-run；候选检查是代码，合并前应对仓库试用；其中相关的字段或标识包括 `retro`。

<!-- zh-CN:end ae6f7004141953b2 -->

**Won't this pile up lint rules forever? Does it ever suggest removing one?**

<!-- zh-CN:begin 0286f71345a38502 -->

**规则会无限累积吗？会建议删除吗？**

<!-- zh-CN:end 0286f71345a38502 -->

Partly, and this is its weakest spot. It can remove prose: no-ops in steering files, and steering in `AGENTS.md` or `CLAUDE.md` that belongs in standards or a check. It flags these for deletion when the files are large. It judges them against the one session it reads, so treat each one as a candidate for the deletion test, not a verdict. It does not audit the lint rules, hooks, or CI jobs it proposed last month. It sees one session, so it cannot tell you that a rule now fires too often or that the bug behind it is gone. You must still prune checks yourself. A rule that fires constantly on good code is the sign to remove it.

<!-- zh-CN:begin 99d6ea052c2700f0 -->

部分会，这是弱点。可删指导文件无效短语，以及属于标准/检查的 `AGENTS.md`/`CLAUDE.md` 内容；文件大时会标记。由于只读一个会话，删除候选需测试而非定论。它不审计过去提出的 lint、钩子或 CI；密集命中好代码的规则应删除。

<!-- zh-CN:end 99d6ea052c2700f0 -->

**Won't it just invent generic advice to fill its categories?**

<!-- zh-CN:begin 411ef98cbc46f155 -->

**会不会为填类别编造通用建议？**

<!-- zh-CN:end 411ef98cbc46f155 -->

This is the strongest criticism of it. One user found that "once the job is finished, the AI tends to forget the struggles from the middle of the session and invents generic advice to satisfy the retro categories." Every candidate must come from the session's own record, so the advice is specific to that session. This has a cost as well as a benefit. It rarely invents something irrelevant, but it can give too much weight to whatever this one session was about. Discard any candidate you can't trace to a specific moment. Treat the severity order as a first draft too, because a quiet, expensive mistake can rank below a loud, cheap one.

<!-- zh-CN:begin a0c4a53098467bdf -->

这是最强批评。有人观察到任务结束时代理会忘记中段困难，编造建议满足类别。每个候选必须来自记录；好处是少编无关，代价是过度关注本会话。追溯不到具体时刻的候选应丢弃；严重度排序也只是初稿，安静的高成本错误可能排在吵闹低成本错误之后。

<!-- zh-CN:end a0c4a53098467bdf -->

**My session is long. Run it now, or start fresh?**

<!-- zh-CN:begin 07699364b2dd0ef8 -->

**会话很长，现在跑还是新开？**

<!-- zh-CN:end 07699364b2dd0ef8 -->

By default it reviews the current session. That is the best case, because the struggles are still in the context window. If the session has already moved out of the [smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone), [clear](https://www.aihero.dev/ai-coding-dictionary/clearing) it, and point a fresh `/retro` at the previous session in the session logs.

<!-- zh-CN:begin 39462e7bb7c5dd4b -->

默认审查当前会话，困难仍在上下文最好。若已离开[智能区](https://www.aihero.dev/ai-coding-dictionary/smart-zone)，先[清理](https://www.aihero.dev/ai-coding-dictionary/clearing)，再让新 `/retro` 读旧日志。

<!-- zh-CN:end 39462e7bb7c5dd4b -->

**The agent keeps making the same mistake. Should I add a line to `CLAUDE.md`?**

<!-- zh-CN:begin 63ee000a228c18d9 -->

**代理反复犯同一错，该在 `CLAUDE.md` 加一行吗？**

<!-- zh-CN:end 63ee000a228c18d9 -->

Usually not, and `retro` pushes back on this more than anything else. A line in `CLAUDE.md` loads into every session, gives less weight to everything else in the file, and goes out of date as the code changes. If the mistake is mechanical, the fix is a check that fails. If it is a judgement call, it goes in the coding standards the reviewer reads. `AGENTS.md` and `CLAUDE.md` are for navigation pointers and little else. For the same reason, `retro` is not a [memory system](https://www.aihero.dev/ai-coding-dictionary/memory-system). It does not store what happened. It changes the environment so the mistake cannot happen again.

<!-- zh-CN:begin 66b43b737eb1e9ab -->

通常不。该行每会话加载、稀释其他内容且会过时。机械错误用失败检查；判断错误放审查标准。`AGENTS.md`/`CLAUDE.md` 主要放导航指针。因此 `retro` 也不是[记忆系统](https://www.aihero.dev/ai-coding-dictionary/memory-system)，不存发生内容，而改环境防复发；其中相关的字段或标识包括 `retro`、`CLAUDE.md`。

<!-- zh-CN:end 66b43b737eb1e9ab -->

**My setup mentions `CODING_STANDARDS.md` and I don't have one. Where does it come from?**

<!-- zh-CN:begin 82453607b64520c0 -->

**设置提到 `CODING_STANDARDS.md`，但我没有。它从哪来？**

<!-- zh-CN:end 82453607b64520c0 -->

No skill ships the file. The first time a session finds a judgement-call rule for the reviewer, `retro` proposes to create it. After you accept, [code-review](https://aihero.dev/skills-code-review) reads it. Any other standards doc you already keep, such as `CONTRIBUTING.md`, works the same way.

<!-- zh-CN:begin 5f2db30e3d490dc8 -->

无技能附带。首次出现审查判断规则时 `retro` 提议创建；接受后 [code-review](https://aihero.dev/skills-code-review) 读取。已有 `CONTRIBUTING.md` 等标准文档同样可用。

<!-- zh-CN:end 5f2db30e3d490dc8 -->

**How is it different from `improve-codebase-architecture`?**

<!-- zh-CN:begin bfa3138f889c28f9 -->

**与 `improve-codebase-architecture` 有何不同？**

<!-- zh-CN:end bfa3138f889c28f9 -->

The input is different. [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) needs only the code, and looks for structural improvements to it. `retro` needs a session history, and improves the environment the agent works in, not the code. You use both; neither replaces the other.

<!-- zh-CN:begin f97ea4ca9fd17745 -->

输入不同。 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 只需代码并改结构；`retro` 需会话历史并改代理环境。两者并用，互不替代。

<!-- zh-CN:end f97ea4ca9fd17745 -->

## It's working if

<!-- zh-CN:begin 80798437efa032ee -->

## 怎样算正常工作

<!-- zh-CN:end 80798437efa032ee -->

- Every candidate points back to a specific moment in the session, not a generic best practice.

<!-- zh-CN:begin 85475f4a53349c7e -->

- 每个候选指向会话具体时刻，不是通用最佳实践。

<!-- zh-CN:end 85475f4a53349c7e -->
- Repeat mistakes turn into failing checks, and your `AGENTS.md` gets shorter over time, not longer.

<!-- zh-CN:begin f22fea6d1628bd43 -->

- 反复错误变成失败检查，`AGENTS.md` 变短。

<!-- zh-CN:end f22fea6d1628bd43 -->
- If a check already existed but was not connected, the finding is to connect it, not a proposal to build a new one.

<!-- zh-CN:begin a3281eb825a9bcc8 -->

- 已有检查未接线时，发现是接线而非新建。

<!-- zh-CN:end a3281eb825a9bcc8 -->
- The next session on the same kind of task finds what it needs faster.

<!-- zh-CN:begin 76015c03b4ee1fa5 -->

- 下次同类任务更快找到所需。

<!-- zh-CN:end 76015c03b4ee1fa5 -->

## Where it fits

<!-- zh-CN:begin 15436c66f47c21fc -->

## 适用范围

<!-- zh-CN:end 15436c66f47c21fc -->

`retro` is the last step of the main chain, where you review how the chain went:

<!-- zh-CN:begin 78ad4ae146f063b1 -->

`retro` 是主链最后一步，回顾流程表现：

<!-- zh-CN:end 78ad4ae146f063b1 -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

<!-- zh-CN:begin f1379ebad6c8d1d7 -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
# 主链：从追问文档、规格、工单、实现、审查到回顾
```

<!-- zh-CN:end f1379ebad6c8d1d7 -->

Run it after a build worth learning from, in the same session or pointed at that session's log. You can skip it after a smooth build.

<!-- zh-CN:begin 8be878c74203105f -->

有学习价值的构建后，在同一会话或指定日志运行；顺畅构建可跳过。

<!-- zh-CN:end 8be878c74203105f -->

- [code-review](https://aihero.dev/skills-code-review) is the reviewer agent that `retro` most often tunes. New coding standards go where its Standards axis reads them.

<!-- zh-CN:begin 34bf016d3a1212ce -->

- [code-review](https://aihero.dev/skills-code-review) 是 `retro` 最常调优的审查代理，新标准放其标准轴读取处。

<!-- zh-CN:end 34bf016d3a1212ce -->
- [writing-for-agents](https://aihero.dev/skills-writing-for-agents) sets the writing style for every steering file and skill that `retro` proposes, and `retro` loads it before it starts.

<!-- zh-CN:begin 3c4e849588955e1d -->

- [writing-for-agents](https://aihero.dev/skills-writing-for-agents) 决定所有指导文件和技能写作风格，`retro` 开始时加载它；其中相关的字段或标识包括 `retro`。

<!-- zh-CN:end 3c4e849588955e1d -->

[ask-matt](https://aihero.dev/skills-ask-matt) routes across the whole set when you are unsure which skill the situation needs.

<!-- zh-CN:begin ecbaa6c8dbd34550 -->

不确定情境需要哪个技能时，由 [ask-matt](https://aihero.dev/skills-ask-matt) 全局路由。

<!-- zh-CN:end ecbaa6c8dbd34550 -->
