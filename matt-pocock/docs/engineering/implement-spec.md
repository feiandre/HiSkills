## What it does

<!-- zh-CN:begin e969efc2b2f49f48 -->

## 它的作用

<!-- zh-CN:end e969efc2b2f49f48 -->

`implement-spec` takes a [spec](https://www.aihero.dev/ai-coding-dictionary/spec) and its [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) and lands the whole thing in one run. The orchestrating [agent](https://www.aihero.dev/ai-coding-dictionary/agent) hands each ticket to an implementer [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) working in its own git worktree, merges each finished branch into a single **integration branch**, runs [code-review](https://aihero.dev/skills-code-review) over the result, and resolves the tickets.

<!-- zh-CN:begin 27cc3cdf9da1419a -->

`implement-spec` 接收一份[规格](https://www.aihero.dev/ai-coding-dictionary/spec)及其[票](https://www.aihero.dev/ai-coding-dictionary/ticket)，在一次运行中全部落地。编排[智能体](https://www.aihero.dev/ai-coding-dictionary/agent)把每张票交给在独立 git 工作树中工作的实现[子智能体](https://www.aihero.dev/ai-coding-dictionary/subagent)，将完成分支合并到一个**整合分支**，对结果运行 [code-review](https://aihero.dev/skills-code-review)，并解决票。

<!-- zh-CN:end 27cc3cdf9da1419a -->

It reads the tickets as a **task graph**, not a list. Blocking edges decide what can start, so at any moment there is a **frontier** of tickets whose blockers have all landed, and every ticket on the frontier runs at once. That is the difference from working the tickets one by one. The graph's shape sets the pace, not the tickets' order on the tracker.

<!-- zh-CN:begin 219d0e2837e3aac5 -->

它把票读作**任务图**，不是列表。阻塞边决定什么能开始，因此任意时刻都有阻塞项全部落地的**前沿**，前沿上的每张票同时运行。这不同于逐票处理。节奏由图形态决定，不由跟踪器上的票顺序决定。

<!-- zh-CN:end 219d0e2837e3aac5 -->

## When to reach for it

<!-- zh-CN:begin 1b07b905fac192cb -->

## 何时使用

<!-- zh-CN:end 1b07b905fac192cb -->

You invoke this by typing `/implement-spec`, and the agent won't reach for it on its own.

<!-- zh-CN:begin f79a321ce09163b7 -->

输入 `/implement-spec` 调用；智能体不会自行使用。

<!-- zh-CN:end f79a321ce09163b7 -->

| Your situation | Reach for |
| --- | --- |
| A spec, split into tickets with blocking edges, that you want landed in one run | `/implement-spec` |
| One ticket at a time, in your own [context window](https://www.aihero.dev/ai-coding-dictionary/context-window), [clearing](https://www.aihero.dev/ai-coding-dictionary/clearing) between tickets | [implement](https://aihero.dev/skills-implement) |
| A spec that isn't split into tickets yet | [to-tickets](https://aihero.dev/skills-to-tickets) first |
| A small piece of work with no real graph to it | [implement](https://aihero.dev/skills-implement) directly |

<!-- zh-CN:begin 9d29c6ec060751ed -->

| 情况 | 使用 |
|---|---|
| 规格已拆成带阻塞边的票，想一次运行落地 | `/implement-spec` |
| 逐票处理，在自己的[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)中，票间[清理](https://www.aihero.dev/ai-coding-dictionary/clearing) | [implement](https://aihero.dev/skills-implement) |
| 规格尚未拆票 | 先 [to-tickets](https://aihero.dev/skills-to-tickets) |
| 没有真实任务图的小工作 | 直接 [implement](https://aihero.dev/skills-implement) |

<!-- zh-CN:end 9d29c6ec060751ed -->

## Prerequisites

<!-- zh-CN:begin 3192b51c93a0fa2b -->

## 前提条件

<!-- zh-CN:end 3192b51c93a0fa2b -->

- **An issue tracker.** The skill reads the tickets from, and resolves them on, the tracker [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) configured. If none has been configured, it stops and tells you to run that first rather than guessing.

<!-- zh-CN:begin 91c61c1c1c5b5e1d -->

- **一个 issue 跟踪器。** 技能从 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置的跟踪器读取并解决票。未配置时停止并提示先运行，而不是猜测。

<!-- zh-CN:end 91c61c1c1c5b5e1d -->
- **Tickets with blocking edges**, as [to-tickets](https://aihero.dev/skills-to-tickets) writes them. Without edges the graph is flat and every ticket starts at once.

<!-- zh-CN:begin c36c9307e086384e -->

- **含阻塞边的票**，按 [to-tickets](https://aihero.dev/skills-to-tickets) 写入。无边则图扁平且所有票同时开始。

<!-- zh-CN:end c36c9307e086384e -->
- **A [harness](https://www.aihero.dev/ai-coding-dictionary/harness) that runs subagents in the background and gives each one a git worktree.** The skill exists to run tickets at the same time, so on a harness that runs subagents one at a time, it is only a slower `implement`.

<!-- zh-CN:begin 1d2de718f7bc5592 -->

- **能后台运行子智能体并给每个独立 git 工作树的[运行环境](https://www.aihero.dev/ai-coding-dictionary/harness)。** 技能目的是同时运行票；逐个子智能体运行的环境上，它只是更慢的 `implement`。

<!-- zh-CN:end 1d2de718f7bc5592 -->

## The integration branch

<!-- zh-CN:begin 1425f59bdc1fdf2c -->

## 整合分支

<!-- zh-CN:end 1425f59bdc1fdf2c -->

Everything lands on one branch. Each implementer:

<!-- zh-CN:begin ae593fa1bbd35d6e -->

所有工作落在一个分支。每个实现者：

<!-- zh-CN:end ae593fa1bbd35d6e -->

1. confirms its worktree is based on the integration branch before it starts,

<!-- zh-CN:begin 29550757d96c286f -->

1. 开始前确认工作树基于整合分支，

<!-- zh-CN:end 29550757d96c286f -->
2. builds its ticket with [tdd](https://aihero.dev/skills-tdd), red-green one slice at a time,

<!-- zh-CN:begin e5d881b6970ba6cd -->

2. 用 [tdd](https://aihero.dev/skills-tdd) 构建票，一次一个切片红绿循环，

<!-- zh-CN:end e5d881b6970ba6cd -->
3. merges the integration branch tip into its own branch before reporting done, so landing it is a fast-forward.

<!-- zh-CN:begin 0f3d756057cf9f8e -->

3. 报告完成前将整合分支尖端合并到自身分支，使落地成为快进。

<!-- zh-CN:end 0f3d756057cf9f8e -->

The tracker decides whether a pull request exists at all. If your tracker closes work through PRs, or you ask for one, the skill opens a draft PR after the first merge and marks it ready at the end. Otherwise the run stops on the integration branch with every ticket resolved the way your tracker closes work, which works fully offline against a local markdown tracker.

<!-- zh-CN:begin 6f9b43fadb4a3f2c -->

跟踪器决定是否创建 PR。若跟踪器通过 PR 关闭工作或你要求，技能在首次合并后创建草稿 PR，结束时标为就绪。否则运行停在整合分支，每张票按跟踪器关闭方式解决；本地 markdown 跟踪器也可完全离线工作。

<!-- zh-CN:end 6f9b43fadb4a3f2c -->

Implementers talk to the orchestrator through [context pointers](https://www.aihero.dev/ai-coding-dictionary/context-pointer) (the spec, the ticket, shared exploration notes, earlier commits) rather than pasted summaries. This keeps each subagent's prompt small and leaves room in the orchestrator's window for the graph.

<!-- zh-CN:begin fa5bf361ab84b3fe -->

实现者通过[上下文指针](https://www.aihero.dev/ai-coding-dictionary/context-pointer)（规格、票、共享探索笔记、早先提交）与编排器交流，不粘贴摘要。子智能体提示更小，编排窗口为图留出空间。

<!-- zh-CN:end fa5bf361ab84b3fe -->

## Common questions

<!-- zh-CN:begin db1eb408749305bb -->

## 常见问题

<!-- zh-CN:end db1eb408749305bb -->

**How is this different from running `/implement` on each ticket myself?**

<!-- zh-CN:begin b7f8e449d138b191 -->

**这与我自己对每张票运行 `/implement` 有何不同？**

<!-- zh-CN:end b7f8e449d138b191 -->

This is the question the skill exists to answer. Before it shipped, people kept building their own versions, and one user described the need: they wanted "subagents implement the tickets" instead of having "to individually create new session and tell them to implement a ticket one by one, when a spec may contain over 5 tickets." With `implement` you are the dispatcher: one [session](https://www.aihero.dev/ai-coding-dictionary/session) per ticket, clearing in between, and keeping track yourself of which tickets are unblocked. `implement-spec` hands that job to one orchestrating session. The price is that you no longer read each ticket's work as it lands; you review the integration branch at the end. To start a run, clear the context and type `/implement-spec` with a pointer to the spec (an issue number or a file path). For a small change with no real graph, skip it and use `implement` directly.

<!-- zh-CN:begin 65c4626cff7b8036 -->

这正是技能要回答的问题。发布前人们自行构建版本；一位用户说想要“子智能体实现票”，而不是“在规格可能包含 5 张以上票时逐票创建新会话并告诉它们实现”。用 `implement` 时你是派发者：每票一个[会话](https://www.aihero.dev/ai-coding-dictionary/session)，中间清理，并自行跟踪解除阻塞的票。`implement-spec` 交给一个编排会话。代价是工作落地时你不再逐票阅读，而在最后审查整合分支。开始运行时清理上下文并输入 `/implement-spec` 和规格指针（issue 编号或文件路径）。没有真实任务图的小变更直接使用 `implement`。

<!-- zh-CN:end 65c4626cff7b8036 -->

**Does it need GitHub? I want it to stop at the branch.**

<!-- zh-CN:begin 2d6bce88a7ef847e -->

**需要 GitHub 吗？我想在分支停下。**

<!-- zh-CN:end 2d6bce88a7ef847e -->

No, not any more. One user who liked the in-progress version had exactly this complaint: "it creates a PR at the end, which requires an online repository like GitHub. I wish it could do the same work offline and stop at the branch where all the work is merged." The run now ends on the integration branch. A PR opens only when the configured tracker closes work through PRs or you ask for one, so on a local markdown tracker the run ends with every ticket resolved and the work merged on the branch.

<!-- zh-CN:begin 897a98f683f418c5 -->

现在不需要。一位喜欢进行中版本的用户正好抱怨：“最后创建 PR，要求 GitHub 这类在线仓库。希望它能离线完成并停在所有工作已合并的分支。”现在运行结束于整合分支。只有跟踪器通过 PR 关闭工作或你要求时才开 PR；本地 markdown 跟踪器会让运行以所有票解决并在分支合并结束。

<!-- zh-CN:end 897a98f683f418c5 -->

**Its review and fix loop ran for hours, or kept "fixing" tickets that hadn't been built yet.**

<!-- zh-CN:begin 9b5b1f1a7af70f0a -->

**其审查与修复循环运行数小时，或不断“修复”尚未构建的票。**

<!-- zh-CN:end 9b5b1f1a7af70f0a -->

Both happen when `code-review` runs anywhere other than the one point the skill gives it. It compares the code against the whole spec, so it only makes sense once every ticket has landed. If it runs mid-run, every unbuilt ticket reads as a failure. The agent then builds that ticket, and that triggers another review. At the end, the skill runs `code-review` once and sends every finding to one fix subagent, but it doesn't yet say when to stop after that fix. One user reported a five-ticket feature where "the review and fix loop took roughly four hours". If you see a second broad review start, tell it to run focused checks for the fixed findings and stop. Expect that first review to find real problems. The run's output is a draft that the review completes, not something to ship on its own.

<!-- zh-CN:begin 58b4cd4e982c03ad -->

两者都发生在 `code-review` 不在技能指定时刻运行。它对照整个规格，因此只有所有票落地才合理。中途运行会把未构建票读成失败，智能体随后构建该票又触发审查。结束时技能运行一次 `code-review`，把所有发现交给一个修复子智能体，但尚未规定修复后何时停止。一位用户说五票功能“审查和修复循环约四小时”。若出现第二次宽泛审查，告诉它针对已修复发现做聚焦检查后停止。首次审查可能发现真实问题；运行输出是审查补全后的草稿，不应直接发布。

<!-- zh-CN:end 58b4cd4e982c03ad -->

**Does it drive tdd like implement does?**

<!-- zh-CN:begin fc786af48a35b1ab -->

**它像 implement 一样驱动 tdd 吗？**

<!-- zh-CN:end fc786af48a35b1ab -->

It does now, though it didn't at first. Users running the in-progress version noticed that "the implementer subagents don't inherit the /tdd directive", so red-green stopped as soon as they scaled up from one ticket to a whole spec. Each implementer now builds its ticket with `tdd`. There is still no step where you agree seams interactively, as there is in an `implement` session, so name the seams in the spec or the tickets if you want them pinned.

<!-- zh-CN:begin 07a021dba62a4545 -->

现在会，最初不会。用户发现“实现子智能体不继承 /tdd 指令”，从一票扩展到整规格时红绿停止。现在每个实现者用 `tdd` 构建。仍没有 `implement` 会话中交互商定接缝的步骤，因此想把接缝钉死就在规格或票中写明。

<!-- zh-CN:end 07a021dba62a4545 -->

**Two implementers running in parallel collided on the same file, or picked different names for the same thing.**

<!-- zh-CN:begin 327df911e720a04a -->

**并行实现者在同一文件冲突，或给同一事物取不同名称。**

<!-- zh-CN:end 327df911e720a04a -->

Worktrees don't remove collisions; they postpone them to merge time. A blocking edge written from ticket text is a guess about which files each ticket will touch, and two tickets on "different parts of the codebase" still share a message catalogue, a config registry, or a type. Each implementer sees only its own ticket and the shared notes, never the other's work in progress, so one user's web and mobile tickets added the same string as `blockedSince` and `blockedOn`. When two frontier tickets touch one shared file, either add a blocking edge between them so they run one after the other, or have the exploration notes fix the exact names each ticket adds.

<!-- zh-CN:begin 548f81830c22b774 -->

工作树不会消除冲突，只推迟到合并。根据票文字写阻塞边只是猜测会触哪些文件；两个“代码库不同部分”的票仍可能共享消息目录、配置注册表或类型。每个实现者只看到自身票和共享笔记，看不到对方进行中工作，所以一位用户的 web 和 mobile 票同名添加 `blockedSince` 和 `blockedOn`。两张前沿票触及同一共享文件时，在二者间加阻塞边使其串行，或让探索笔记固定每票添加的准确名称。

<!-- zh-CN:end 548f81830c22b774 -->

**Blocked tickets never start, even after their blocker has merged.**

<!-- zh-CN:begin 6c30678cbe79b46c -->

**阻塞票在阻塞项合并后仍不开始。**

<!-- zh-CN:end 6c30678cbe79b46c -->

This is a known problem on GitHub. The tracker's blocked-by count only drops when a blocker *closes*, and tickets typically close when the PR merges, which is the end of the run. The tracker is the right source for the starting graph but a stale one mid-run. Tell the orchestrator to track which tickets have merged into the integration branch itself and compute the frontier from that.

<!-- zh-CN:begin a9c59bdf34e1cba3 -->

GitHub 上的已知问题。跟踪器 blocked-by 计数只在阻塞项*关闭*时下降，而票通常在 PR 合并时关闭，即运行结束。跟踪器适合起始图，运行中数据会过期。告诉编排器自行跟踪哪些票已合并进整合分支，并据此计算前沿。

<!-- zh-CN:end a9c59bdf34e1cba3 -->

**Does this replace Sandcastle or an AFK script?**

<!-- zh-CN:begin 9a742ec4562e3e4c -->

**这取代 Sandcastle 或离线脚本吗？**

<!-- zh-CN:end 9a742ec4562e3e4c -->

No. People ask because the skills now reach into implementation: "is Sandcastle still relevant? Your skills now seem to be able to handle implementation as well." `implement-spec` puts an agent in charge of orchestration inside one harness session, which needs no infrastructure and lets you watch and steer. For work that is truly [AFK](https://www.aihero.dev/ai-coding-dictionary/afk), a deterministic loop ([Sandcastle](https://github.com/mattpocock/sandcastle), a shell script, a CI job) is faster, cheaper, and more reliable, because no agent makes the orchestration decisions.

<!-- zh-CN:begin 2a80d50e03e10917 -->

不。人们问“Sandcastle 还有用吗？你的技能现在似乎也能处理实现。”`implement-spec` 在一个运行环境会话中用智能体编排，不需基础设施，可观察和转向。真正[离线](https://www.aihero.dev/ai-coding-dictionary/afk)的工作，确定性循环（[Sandcastle](https://github.com/mattpocock/sandcastle)、shell 脚本、CI 作业）更快、更便宜、更可靠，因为没有智能体做编排决策。

<!-- zh-CN:end 2a80d50e03e10917 -->

**A ticket's key test was skipped inside its worktree, and it reported green.**

<!-- zh-CN:begin 5c66dc822cec2be6 -->

**票的关键测试在工作树内跳过却报告绿色。**

<!-- zh-CN:end 5c66dc822cec2be6 -->

A worktree holds only what git tracks. Tests that read gitignored fixtures, local databases, or credentials can silently skip there. For a ticket whose verification depends on untracked material, tell the orchestrator to run it in the main checkout instead.

<!-- zh-CN:begin e6da1e0b3316edef -->

工作树只有 git 跟踪内容。读取 gitignore 夹具、本地数据库或凭据的测试可能静默跳过。验证依赖未跟踪材料的票，让编排器在主检出中运行。

<!-- zh-CN:end e6da1e0b3316edef -->

## It's working if

<!-- zh-CN:begin c8c258da35516b1e -->

## 生效时

<!-- zh-CN:end c8c258da35516b1e -->

- Several implementers are running at once whenever the graph allows, not one after another.

<!-- zh-CN:begin 1c6d4688dcd76f99 -->

- 图允许时多个实现者同时运行，不串行。

<!-- zh-CN:end 1c6d4688dcd76f99 -->
- A ticket starts as soon as its last blocker lands on the integration branch, not when the whole run ends.

<!-- zh-CN:begin 01bafd6caf23fa62 -->

- 最后阻塞项落到整合分支后票立即开始，不等整个运行结束。

<!-- zh-CN:end 01bafd6caf23fa62 -->
- Every ticket's trace shows `tdd` running, with a failing test before the code.

<!-- zh-CN:begin 99034f38f54b91be -->

- 每票轨迹显示 `tdd`，代码前有失败测试。

<!-- zh-CN:end 99034f38f54b91be -->
- Merges into the integration branch are fast-forwards, not conflict resolutions.

<!-- zh-CN:begin eb6a48dfde23cd27 -->

- 合并进整合分支是快进，需解决冲突则不符合。

<!-- zh-CN:end eb6a48dfde23cd27 -->
- The run ends on one branch with every ticket resolved, and a PR only if your tracker wanted one.

<!-- zh-CN:begin 121b9bf874191f43 -->

- 运行结束于一个分支，所有票已解决，仅当跟踪器需要时才有 PR。

<!-- zh-CN:end 121b9bf874191f43 -->

## Where it fits

<!-- zh-CN:begin 114cfde95864b0c5 -->

## 适用范围

<!-- zh-CN:end 114cfde95864b0c5 -->

`implement-spec` is the build step of the main chain, as the parallel alternative to running [implement](https://aihero.dev/skills-implement) once per ticket:

<!-- zh-CN:begin a168752f6aa44c13 -->

`implement-spec` 是主链构建步骤，作为逐票运行 [implement](https://aihero.dev/skills-implement) 的并行替代：

<!-- zh-CN:end a168752f6aa44c13 -->

```txt
grill-with-docs → to-spec → to-tickets → implement-spec → retro
```

<!-- zh-CN:begin bbaa58d22c5570a3 -->

```txt
# 主线工作流
grill-with-docs → to-spec → to-tickets → implement-spec → retro
```

<!-- zh-CN:end bbaa58d22c5570a3 -->

Its neighbours are [to-tickets](https://aihero.dev/skills-to-tickets), which declares the blocking edges it reads as a task graph, and [code-review](https://aihero.dev/skills-code-review), which it runs over the integration branch before closing out. [ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set when you are not sure which flow you are in.

<!-- zh-CN:begin ac994662eef1c6f9 -->

邻接技能是 [to-tickets](https://aihero.dev/skills-to-tickets)（声明作为任务图读取的阻塞边）与 [code-review](https://aihero.dev/skills-code-review)（关闭前审查整合分支）。不确定处于哪个流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 路由整套技能。

<!-- zh-CN:end ac994662eef1c6f9 -->
