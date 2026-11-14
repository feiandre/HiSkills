## What it does

<!-- zh-CN:begin 3118cb01d2139263 -->

## 它做什么

<!-- zh-CN:end 3118cb01d2139263 -->

`implement` builds work that has already been decided. You point it at a [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket), a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), or the plan you just agreed in the conversation, and it writes the code, drives [tdd](https://aihero.dev/skills-tdd) at the seams, typechecks as it goes, runs [code-review](https://aihero.dev/skills-code-review) at the end, and commits to the current branch.

<!-- zh-CN:begin 62cade1794c4a820 -->

`implement` 构建已经决定好的工作。你可以让它处理[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)、[规格](https://www.aihero.dev/ai-coding-dictionary/spec)，或刚在对话中商定的计划；它编写代码，在各接缝驱动 [tdd](https://aihero.dev/skills-tdd)，在执行中类型检查，最后运行 [code-review](https://aihero.dev/skills-code-review)，并提交到当前分支。

<!-- zh-CN:end 62cade1794c4a820 -->

It never reopens the plan. There is no interview, no clarifying round, no proposal of a different approach. Whatever was settled upstream is the input, and the skill's whole job is to turn that into a commit. That is what separates it from typing "build this" at a fresh [agent](https://www.aihero.dev/ai-coding-dictionary/agent), which often redesigns the work while it builds it.

<!-- zh-CN:begin 558c469563efa227 -->

它绝不会重新打开计划。没有访谈、没有澄清轮次，也不提出不同方案。上游已经确定的内容就是输入，技能的全部工作就是把它变成提交。这正是它与在新[智能体](https://www.aihero.dev/ai-coding-dictionary/agent)中输入“构建这个”的区别：后者经常一边构建一边重新设计。

<!-- zh-CN:end 558c469563efa227 -->

## When to reach for it

<!-- zh-CN:begin 3090085e47fab985 -->

## 何时使用

<!-- zh-CN:end 3090085e47fab985 -->

You invoke this by typing `/implement` yourself, and the agent won't reach for it on its own. It ships with `disable-model-invocation: true`, so no other skill can call it either. Wherever [ask-matt](https://aihero.dev/skills-ask-matt) or [to-tickets](https://aihero.dev/skills-to-tickets) says "then `/implement` per ticket", that is an instruction to you, not something the agent will do unprompted.

<!-- zh-CN:begin a11f00825467a8ca -->

由你输入 `/implement` 自行调用，智能体不会主动选择。它带有 `disable-model-invocation: true`，其他技能也无法调用。无论 [ask-matt](https://aihero.dev/skills-ask-matt) 或 [to-tickets](https://aihero.dev/skills-to-tickets) 何时说“然后逐工单 `/implement`”，那都是给你的指令，智能体不会未经提示执行。

<!-- zh-CN:end a11f00825467a8ca -->

Where the work currently lives decides whether this is the right skill:

<!-- zh-CN:begin 7cbc343440526df8 -->

工作当前存在于哪里，决定这是否是正确技能：

<!-- zh-CN:end 7cbc343440526df8 -->

| The work is… | Reach for |
| --- | --- |
| A ticket on the tracker | `/implement #42`, one ticket per [session](https://www.aihero.dev/ai-coding-dictionary/session), [clearing](https://www.aihero.dev/ai-coding-dictionary/clearing) context between tickets |
| A spec, not yet split up, and the build spans sessions | [to-tickets](https://aihero.dev/skills-to-tickets) first, then `/implement` per ticket |
| A spec, and the build is small | `/implement` directly against the spec |
| Only in the conversation you just had, and it's still small | `/implement` right there, in the same window |
| Not written down anywhere yet | [grill-with-docs](https://aihero.dev/skills-grill-with-docs), or [grill-me](https://aihero.dev/skills-grill-me) if there's no codebase |
| One concrete behaviour you want test-first, with no spec | [tdd](https://aihero.dev/skills-tdd) directly |
| Already built, and you want it checked | [code-review](https://aihero.dev/skills-code-review) directly |

<!-- zh-CN:begin 7792773f2fe764b6 -->

| 工作位于…… | 应使用 |
| --- | --- |
| 跟踪器中的工单 | `/implement #42`，每个[会话](https://www.aihero.dev/ai-coding-dictionary/session)一个工单，在工单间[清理](https://www.aihero.dev/ai-coding-dictionary/clearing)上下文 |
| 尚未拆分且构建跨越多个会话的规格 | 先用 [to-tickets](https://aihero.dev/skills-to-tickets)，再逐工单 `/implement` |
| 规格且构建规模小 | 直接对该规格运行 `/implement` |
| 只存在于刚结束的对话中，仍然很小 | 就在同一个窗口中运行 `/implement` |
| 尚未写在任何地方 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs)；没有代码库时用 [grill-me](https://aihero.dev/skills-grill-me) |
| 一个具体行为，希望测试优先，且没有规格 | 直接使用 [tdd](https://aihero.dev/skills-tdd) |
| 已构建，想检查 | 直接使用 [code-review](https://aihero.dev/skills-code-review) |

<!-- zh-CN:end 7792773f2fe764b6 -->

The same-session case is worth naming because the skill's own first line doesn't cover it. `SKILL.md` says "the spec or tickets", which pushes the [model](https://www.aihero.dev/ai-coding-dictionary/model) to look for a file that doesn't exist. If the plan lives only in the thread, say so when you invoke it.

<!-- zh-CN:begin 76c5b207f2dc1b59 -->

同会话情况值得特别说明，因为技能自己的首行没有涵盖它。`SKILL.md` 说“规格或工单”，这会促使[模型](https://www.aihero.dev/ai-coding-dictionary/model)寻找并不存在的文件。如果计划只存在于线程中，请在调用时说明。

<!-- zh-CN:end 76c5b207f2dc1b59 -->

## Prerequisites

<!-- zh-CN:begin a1853ffb49c4f4ed -->

## 前置条件

<!-- zh-CN:end a1853ffb49c4f4ed -->

`implement` commits to the branch you are on. It does not create one, and it does not ask. Check you are on the branch you want the work on before you start.

<!-- zh-CN:begin 9154c558fd191d45 -->

`implement` 会提交到你当前所在分支。它不创建分支，也不询问。开始前确认自己在希望接收工作的分支上。

<!-- zh-CN:end 9154c558fd191d45 -->

If the tickets came from [to-tickets](https://aihero.dev/skills-to-tickets), [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) configured the tracker they live on. `code-review` reads the same configuration to find the originating spec at close-out.

<!-- zh-CN:begin 52ce19c5d9b6befc -->

若工单来自 [to-tickets](https://aihero.dev/skills-to-tickets)，[setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 已配置它们所在的跟踪器。`code-review` 在收尾时读取相同配置来寻找原始规格。

<!-- zh-CN:end 52ce19c5d9b6befc -->

## What one run does

<!-- zh-CN:begin 3dc22059eee68c22 -->

## 一次运行做什么

<!-- zh-CN:end 3dc22059eee68c22 -->

A run has five steps, in order:

<!-- zh-CN:begin e08afbd3054528af -->

一次运行按顺序包含五步：

<!-- zh-CN:end e08afbd3054528af -->

1. Read the ticket or spec and work out the seams.

<!-- zh-CN:begin 77a984efa5219b97 -->

1. 阅读工单或规格，确定接缝。

<!-- zh-CN:end 77a984efa5219b97 -->
2. Drive [tdd](https://aihero.dev/skills-tdd) at the pre-agreed seams, one red-green slice at a time.

<!-- zh-CN:begin 6cec16d3b3dec9fd -->

2. 在预先商定的接缝上驱动 [tdd](https://aihero.dev/skills-tdd)，逐个完成红绿切片。

<!-- zh-CN:end 6cec16d3b3dec9fd -->
3. Typecheck often, run single test files as it goes.

<!-- zh-CN:begin 3daf34f398b49d02 -->

3. 经常类型检查，并随进度运行单个测试文件。

<!-- zh-CN:end 3daf34f398b49d02 -->
4. Run the full test suite once, at the end.

<!-- zh-CN:begin f8fb1434cb9a76a0 -->

4. 最后运行一次完整测试套件。

<!-- zh-CN:end f8fb1434cb9a76a0 -->
5. Run [code-review](https://aihero.dev/skills-code-review), then commit to the current branch.

<!-- zh-CN:begin b93aca541c2ef4f1 -->

5. 运行 [code-review](https://aihero.dev/skills-code-review)，再提交到当前分支。

<!-- zh-CN:end b93aca541c2ef4f1 -->

One run covers one ticket. The tickets [to-tickets](https://aihero.dev/skills-to-tickets) produces are tracer-bullet vertical slices sized to fit a single fresh [context window](https://www.aihero.dev/ai-coding-dictionary/context-window), so the intended rhythm is: clear context, implement one ticket, commit, clear again. Each ticket is self-contained, so you can discard the previous ticket's context.

<!-- zh-CN:begin 54a3bc9fb1a7850a -->

一次运行处理一个工单。[to-tickets](https://aihero.dev/skills-to-tickets) 生成的工单是按单个全新[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)大小切分的示踪弹垂直切片，因此预期节奏是：清理上下文、实现一个工单、提交、再次清理。每个工单自包含，因此可以丢弃前一个工单的上下文。

<!-- zh-CN:end 54a3bc9fb1a7850a -->

## Pre-agreed seams

<!-- zh-CN:begin db9e93204fc102d2 -->

## 预先商定的接缝

<!-- zh-CN:end db9e93204fc102d2 -->

The skill's central idea is the **seam**, the public boundary you observe behaviour at without reaching inside. Tests live at seams. When the seam is agreed before any code exists, the tests last, and you can rewrite the implementation underneath without changing them.

<!-- zh-CN:begin 1d4ca01ec25dc65b -->

技能的核心思想是**接缝**：观察行为时无需进入内部而依赖的公开边界。测试放在接缝处。若在任何代码存在前就商定接缝，这些测试便能持久；你可以重写下方实现而不改测试。

<!-- zh-CN:end 1d4ca01ec25dc65b -->

The "pre-agreed" part matters, and it is also the skill's weakest point. Nothing inside `implement` agrees the seams. `tdd` is the skill that asks, and it refuses to write a test at an unconfirmed seam. So in practice the agreement happens either upstream in the spec, or in the first exchange of the run. If it happens nowhere, the run becomes "just write the code" and nothing warns you. Naming the seams in the spec is what stops that.

<!-- zh-CN:begin 7e63f48769462bf0 -->

“预先商定”很重要，也是技能最薄弱之处。`implement` 内部没有任何步骤商定接缝。负责询问的是 `tdd`，而它会拒绝在未确认接缝上写测试。所以实际商定发生在规格上游，或运行的第一轮交流中。若哪里都没有发生，运行就会变成“只管写代码”，而且没有任何警告。在规格中命名接缝可以阻止这种情况。

<!-- zh-CN:end 7e63f48769462bf0 -->

## Common questions

<!-- zh-CN:begin bf6fdf420d6a3ad1 -->

## 常见问题

<!-- zh-CN:end bf6fdf420d6a3ad1 -->

**It finished, but my ticket is still open and the acceptance criteria are still unchecked.**

<!-- zh-CN:begin 367431c8b6da97b8 -->

**它完成了，但我的工单仍未关闭，验收标准也未勾选。**

<!-- zh-CN:end 367431c8b6da97b8 -->

Correct, and expected. `implement` has no completion step. It ends at the commit and never touches the work item. This is the same on GitHub Issues and on the local markdown tracker, so it is not a tracker integration problem. It also does not act on the findings `code-review` produced, and does not tick the `- [ ]` boxes on the originating issue. Close the ticket and reconcile the criteria yourself. This matters most on a dependency chain, because `to-tickets` defines the frontier as tickets whose blockers are all closed. If nothing gets closed, nothing ever becomes visibly unblocked.

<!-- zh-CN:begin dff83045aaeb7231 -->

正确，且符合预期。`implement` 没有完成步骤。它在提交处结束，绝不触碰工作项。GitHub Issues 和本地 Markdown 跟踪器均如此，因此这不是跟踪器集成问题。它也不会处理 `code-review` 产生的问题，或勾选原始问题上的 `- [ ]` 复选框。请自行关闭工单并核对标准。在依赖链中尤其重要，因为 `to-tickets` 把前沿定义为所有阻塞项均已关闭的工单。如果什么都未关闭，就永远没有工单会显示为已解除阻塞。

<!-- zh-CN:end dff83045aaeb7231 -->

**Can I point it at all my tickets at once, or run several in parallel?**

<!-- zh-CN:begin 47e29c1afec26af3 -->

**可以一次指向所有工单，或并行运行多个吗？**

<!-- zh-CN:end 47e29c1afec26af3 -->

Not with `/implement`: one invocation, one ticket. For a whole spec in one run, use [implement-spec](https://aihero.dev/skills-implement-spec), which gives each ticket on the ready frontier to a [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) in its own worktree, then merges the results onto one integration branch. Running several `/implement` sessions side by side in one checkout is worse than unsupported. One field report describes a `git commit --amend` in one session landing on another session's commit, a stash vanishing from `refs/stash`, and commits landing on the wrong branch, all in a single afternoon across three issues. The sessions share one working directory, one index, and one HEAD. Users work around this with git worktrees, but `refs/stash` is shared across worktrees too, so worktrees alone do not fix the stash case.

<!-- zh-CN:begin df479d28c43b3ff3 -->

用 `/implement` 不可以：一次调用一个工单。要一次运行整个规格，请使用 [implement-spec](https://aihero.dev/skills-implement-spec)，它把就绪前沿中的每个工单交给各自工作树中的[子智能体](https://www.aihero.dev/ai-coding-dictionary/subagent)，再将结果合并到一个集成分支。在同一检出中并行运行多个 `/implement` 会话比不受支持更糟。一份现场报告描述，一个下午跨三个问题发生了：一个会话中的 `git commit --amend` 落到另一会话的提交上，stash 从 `refs/stash` 消失，提交落到错误分支。这些会话共享一个工作目录、一个索引和一个 HEAD。用户用 Git 工作树绕过，但 `refs/stash` 也在工作树间共享，因此仅靠工作树无法修复 stash 情况。

<!-- zh-CN:end df479d28c43b3ff3 -->

**Can it open a pull request instead of committing?**

<!-- zh-CN:begin 2838deed44ecfefc -->

**可以创建拉取请求而不是直接提交吗？**

<!-- zh-CN:end 2838deed44ecfefc -->

Not built in. It commits straight to the current branch. Several people find this too eager, because the code lands before they can verify it works. There is no configuration flag and no PR mode. People override it in the invocation ("commit to a branch and open a PR") or by editing their local copy of the skill. When the agent does write the PR, [pr](https://aihero.dev/skills-pr) shapes its body.

<!-- zh-CN:begin b5ed032470f1c02b -->

没有内置该功能。它会直接提交到当前分支。若干人觉得这样太急，因为代码在能够验证可用前就已落地。没有配置标志或 PR 模式。人们可在调用时改写（“提交到分支并创建 PR”），或编辑本地技能副本。智能体确实编写 PR 时，[pr](https://aihero.dev/skills-pr) 会组织正文。

<!-- zh-CN:end b5ed032470f1c02b -->

**`code-review` says it cannot see my changes.**

<!-- zh-CN:begin 3935a4c8cb2024a2 -->

**`code-review` 说看不到我的改动。**

<!-- zh-CN:end 3935a4c8cb2024a2 -->

`code-review` reviews `git diff <fixed-point>...HEAD`, which excludes staged and working-tree changes. `implement` runs it before committing, so unless an interim commit already exists there is nothing in that diff to review. Multiple people have reported this and it is unfixed on both sides. Commit first, then review against the point you branched from.

<!-- zh-CN:begin 43179262b35e3115 -->

`code-review` 审查 `git diff <fixed-point>...HEAD`，其中不包含已暂存和工作树更改。`implement` 在提交前运行它，因此除非已有临时提交，否则差异中没有可审查内容。多人报告过，两边都未修复。先提交，再对照分支起点审查。

<!-- zh-CN:end 43179262b35e3115 -->

Separately, some people do not want the review inside the run at all, because an agent reviewing the code it just wrote is biased toward its own solution. Running [code-review](https://aihero.dev/skills-code-review) in a fresh session against a fixed point is a valid alternative. The same bias is why that skill runs its two axes in separate sub-agents.

<!-- zh-CN:begin 43aef60f01409f28 -->

另外，有人完全不想在运行中审查，因为智能体审查刚写的代码会偏向自己的方案。在新会话中对照固定点运行 [code-review](https://aihero.dev/skills-code-review) 是合理替代方案。该技能用分离的子智能体执行两个审查轴，也是出于同样的偏差控制。

<!-- zh-CN:end 43aef60f01409f28 -->

**One ticket burned 150k tokens. Am I using it wrong?**

<!-- zh-CN:begin 47f252afa14f23b2 -->

**一个工单消耗了 15 万词元。我是否用错了？**

<!-- zh-CN:end 47f252afa14f23b2 -->

Probably not. The ticket is more likely too big. A run does codebase exploration, a red-green loop per seam, a full suite, and a review, so a non-trivial ticket exceeding 100k [tokens](https://www.aihero.dev/ai-coding-dictionary/token) is normal rather than a sign something broke. The fix is upstream. Right-size the tickets in [to-tickets](https://aihero.dev/skills-to-tickets) so each fits one fresh window. If a single ticket keeps going over, split it rather than raising the [effort](https://www.aihero.dev/ai-coding-dictionary/effort) level.

<!-- zh-CN:begin e780a7f7ad64b07a -->

大概没有。更可能是工单太大。一次运行包括代码库探索、每个接缝的红绿循环、完整套件和审查，因此非简单工单超过 10 万[词元](https://www.aihero.dev/ai-coding-dictionary/token)很正常，并非故障征兆。修复在上游：在 [to-tickets](https://aihero.dev/skills-to-tickets) 中调整工单粒度，使每项适合一个全新窗口。如果单个工单持续超限，应拆分而非提高[投入](https://www.aihero.dev/ai-coding-dictionary/effort)级别。

<!-- zh-CN:end e780a7f7ad64b07a -->

**`/implement #2` in a fresh session worked on something completely unrelated.**

<!-- zh-CN:begin 56417af6d5c85aae -->

**在新会话中运行 `/implement #2`，它处理了完全不相关的内容。**

<!-- zh-CN:end 56417af6d5c85aae -->

The agent resolved `#2` against another numbered list in context, such as a todo file or checklist, rather than the configured tracker. `implement` now fetches a passed reference from the issue tracker and states its title before starting, and asks when the reference is ambiguous. Check that title matches the ticket you meant; passing the issue URL or `owner/repo#2` removes the ambiguity entirely.

<!-- zh-CN:begin 2c400ada747b70cd -->

智能体把 `#2` 解析成上下文里另一份编号列表（例如 todo 文件或检查清单）中的项目，而不是配置的跟踪器。`implement` 现在会从问题跟踪器获取传入引用，并在开始前说明标题；引用含糊时会询问。请检查标题是否符合目标工单；传递问题 URL 或 `owner/repo#2` 可完全消除歧义。

<!-- zh-CN:end 2c400ada747b70cd -->

## It's working if

<!-- zh-CN:begin 9a703753d409ea0f -->

## 正常工作时的表现

<!-- zh-CN:end 9a703753d409ea0f -->

- The session opens by reading the ticket or spec and restating what it will build, rather than asking you what to build.

<!-- zh-CN:begin b4a55917a9c59931 -->

- 会话先阅读工单或规格并复述将构建什么，而不是询问你要构建什么。

<!-- zh-CN:end b4a55917a9c59931 -->
- You can see an actual `tdd` Skill tool call in the trace, not just tests appearing in the diff.

<!-- zh-CN:begin bcba7ee5cb17fffa -->

- 轨迹中可见真正的 `tdd` Skill 工具调用，而不只是差异中出现测试。

<!-- zh-CN:end bcba7ee5cb17fffa -->
- Typechecks and single test files run repeatedly during the run, and the full suite runs once near the end.

<!-- zh-CN:begin 7d2c10110eee6d0d -->

- 运行中反复执行类型检查和单文件测试，末尾附近运行一次完整套件。

<!-- zh-CN:end 7d2c10110eee6d0d -->
- The run reaches a commit on your current branch without you prompting it to carry on.

<!-- zh-CN:begin efb509775dbaa535 -->

- 无需你提示继续，运行便在当前分支到达提交。

<!-- zh-CN:end efb509775dbaa535 -->
- The diff is one ticket's worth of change: a vertical slice through every layer, not several tickets swept together.

<!-- zh-CN:begin c88a039ace120aec -->

- 差异是一个工单范围的变化：贯穿每一层的垂直切片，而不是多个工单混在一起。

<!-- zh-CN:end c88a039ace120aec -->

## Where it fits

<!-- zh-CN:begin 7e1e98f4318a1644 -->

## 所处位置

<!-- zh-CN:end 7e1e98f4318a1644 -->

`implement` is the build step of the main chain:

<!-- zh-CN:begin 2084e4af71c688f6 -->

`implement` 是主链的构建步骤：

<!-- zh-CN:end 2084e4af71c688f6 -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

Its neighbours are [to-tickets](https://aihero.dev/skills-to-tickets), which produces the tickets it consumes and declares the blocking edges that decide their order; [tdd](https://aihero.dev/skills-tdd), which it drives internally at each seam; and [code-review](https://aihero.dev/skills-code-review), which it runs before committing. It sits downstream of the planning skills and trusts them. It does not re-validate the shape of what it was handed, so a badly-structured map or a horizontally-layered ticket gets built as written.

<!-- zh-CN:begin 3c31a514025e4743 -->

相邻技能包括：[to-tickets](https://aihero.dev/skills-to-tickets)，生成它所消费的工单并声明决定顺序的阻塞边；[tdd](https://aihero.dev/skills-tdd)，它在每个接缝内部驱动；以及 [code-review](https://aihero.dev/skills-code-review)，它在提交前运行。它位于规划技能下游并信任这些技能。它不会重新验证收到内容的结构，因此结构糟糕的地图或横切分层的工单会按原样构建。

<!-- zh-CN:end 3c31a514025e4743 -->

That trust is why [wayfinder](https://aihero.dev/skills-wayfinder) merges onto the chain at [to-spec](https://aihero.dev/skills-to-spec) rather than looping its map straight into `implement`. Go straight to `implement` from a map only when the effort turned out small.

<!-- zh-CN:begin fc377c9838ef2f3e -->

这种信任是 [wayfinder](https://aihero.dev/skills-wayfinder) 在 [to-spec](https://aihero.dev/skills-to-spec) 处并入主链、而非直接把地图循环输入 `implement` 的原因。只有工作规模确实很小时，才从地图直接进入 `implement`。

<!-- zh-CN:end fc377c9838ef2f3e -->

[ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set when you are not sure which flow you are in.

<!-- zh-CN:begin 3899136933ae59c0 -->

当你不确定处于哪个流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 是整个技能集的路由器。

<!-- zh-CN:end 3899136933ae59c0 -->
