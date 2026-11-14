> **Archived.** This skill was removed from the plugin in v1.3.0 and is no longer maintained. Nothing replaces it: the agent works through a merge or rebase conflict without a dedicated skill. The page stays up for reference.

<!-- zh-CN:begin d8b04c622bd9d944 -->

> **已归档。** 此技能在 v1.3.0 从插件移除，不再维护。没有替代品：代理通过普通流程处理合并或变基冲突。此页保留供参考。

<!-- zh-CN:end d8b04c622bd9d944 -->

## What it does

<!-- zh-CN:begin b87500ad356bafde -->

## 它做什么

<!-- zh-CN:end b87500ad356bafde -->

`resolving-merge-conflicts` works through an in-progress git merge or rebase, hunk by hunk, then runs the project's own checks and finishes the operation with a commit.

<!-- zh-CN:begin f39af7cf459b5ea9 -->

`resolving-merge-conflicts` 逐块处理进行中的 git merge 或 rebase，运行项目自身检查，并以提交完成操作。

<!-- zh-CN:end f39af7cf459b5ea9 -->

It refuses to treat a conflict as a text problem. Before touching a hunk it traces each side back to its **[primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source)** (the commit message, the PR, the original issue), so it is choosing between two intents rather than between two blocks of text, and it preserves both wherever they are compatible. Where they are not, it picks the side matching the merge's stated goal and names the trade-off. It invents no new behaviour to hide a clash, and it never uses `--abort`. It always takes the merge to a finished commit.

<!-- zh-CN:begin adc7cfeeea32b685 -->

它拒绝把冲突当纯文本问题。处理一个块前，将两边追溯到各自的**[一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)**（提交消息、PR、原始议题），在两种意图而非两段文本间选择；兼容之处保留双方。不兼容时，选择符合合并目标的版本并说明取舍。它不发明新行为掩盖冲突，也绝不用 `--abort`，始终推进至完成提交。

<!-- zh-CN:end adc7cfeeea32b685 -->

## When to reach for it

<!-- zh-CN:begin 2a29068342b62b49 -->

## 何时使用

<!-- zh-CN:end 2a29068342b62b49 -->

Type `/resolving-merge-conflicts`, or the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reaches for it automatically when a task fits.

<!-- zh-CN:begin 89d98d0e2b17f627 -->

输入 `/resolving-merge-conflicts`，或任务适合时由[代理](https://www.aihero.dev/ai-coding-dictionary/agent)自动使用。

<!-- zh-CN:end 89d98d0e2b17f627 -->

Reach for it when git has already stopped on conflicts it could not resolve itself. It is scoped to the conflict in front of you, not to anything either side of it:

<!-- zh-CN:begin d524e677f188ddb6 -->

当 git 已因无法自行解决的冲突停下时使用。范围是眼前的冲突，不处理冲突任一侧的其他工作：

<!-- zh-CN:end d524e677f188ddb6 -->

| Your situation | Skill |
| --- | --- |
| Mid-merge or mid-rebase, conflict markers in the tree | This one |
| Merge finished, something now misbehaves for reasons you can't see | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |
| Planning how to slice work so branches collide less | Neither: see the parallel-work question below |

<!-- zh-CN:begin 86599e1ff0cbae97 -->

| 你的情况 | 技能 |
| --- | --- |
| 合并或变基进行中，树里有冲突标记 | 本技能 |
| 合并结束，但出现了看不出原因的异常 | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |
| 规划如何切分工作以减少分支碰撞 | 两者都不用：见下文并行工作问题 |

<!-- zh-CN:end 86599e1ff0cbae97 -->

## Primary sources over `ours` and `theirs`

<!-- zh-CN:begin 134c9830328dd6c1 -->

## 依据一手来源而非 `ours` 和 `theirs`

<!-- zh-CN:end 134c9830328dd6c1 -->

The skill exists to prevent resolving by flag: `--ours`, `--theirs`, or hand-deleting whichever block looks less important, so the markers go away and the build compiles. That resolution can be syntactically perfect and still silently drop a change somebody made on purpose.

<!-- zh-CN:begin a4dd7f91e2ec9e7a -->

技能用于防止按标志解决：用 `--ours`、`--theirs` 或手动删除看似不重要的块，只为清除标记并让构建通过。这种解决语法完美，却可能静默丢掉有人刻意做的改动。

<!-- zh-CN:end a4dd7f91e2ec9e7a -->

You cannot preserve an intent you have not read. So the work starts in the history (commits, PRs, [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket)) and only then moves to the diff. The check step exists for the same reason. The skill finds the repo's own [automated checks](https://www.aihero.dev/ai-coding-dictionary/automated-check) and runs them before committing, because a merge is the easiest place in git to produce code that satisfies both branches and passes neither's tests.

<!-- zh-CN:begin f769a85a04336ea6 -->

未阅读就无法保留意图，因此从历史（提交、PR、[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)）开始，再进入差异。检查步骤同理：找出仓库自己的[自动检查](https://www.aihero.dev/ai-coding-dictionary/automated-check)，提交前运行，因为合并最容易产生同时满足两边却都不通过各自测试的代码。

<!-- zh-CN:end f769a85a04336ea6 -->

## Common questions

<!-- zh-CN:begin 37500bfc5cd99c7e -->

## 常见问题

<!-- zh-CN:end 37500bfc5cd99c7e -->

**Claude Code already resolves conflicts pretty well on its own. Why does this need a skill?**

<!-- zh-CN:begin 628e90fd2c1210c2 -->

**Claude Code 已能自行解决冲突，为何需要技能？**

<!-- zh-CN:end 628e90fd2c1210c2 -->

The added value is the "find the primary sources" and "run feedback loops" steps, which you otherwise have to prompt by hand every time. An unprompted agent will usually produce a plausible resolution from the diff alone and stop there. The skill's value is the two steps it will not let the agent skip: reading why each side exists, and running the checks afterwards. That is a small gain over a good [model](https://www.aihero.dev/ai-coding-dictionary/model), and that is intended. At least one reader has predicted this is a whole skill that becomes a no-op as models improve.

<!-- zh-CN:begin 3fa57f7a0e96b054 -->

附加价值是“找一手来源”和“运行反馈循环”步骤，否则每次都要手动提示。无提示代理通常只凭差异给出合理方案便停下。技能确保不跳过两步：阅读双方为何存在，以及事后运行检查。对优秀[模型](https://www.aihero.dev/ai-coding-dictionary/model)收益很小，这也是预期的。至少一位读者预测模型进步后整个技能会变成无效指令。

<!-- zh-CN:end 3fa57f7a0e96b054 -->

**Should I keep parallel agents off the same files to avoid conflicts in the first place?**

<!-- zh-CN:begin de83464d5ba808a7 -->

**是否应让并行代理避开同一文件以避免冲突？**

<!-- zh-CN:end de83464d5ba808a7 -->

Mostly no. Zoning files off between parallel tasks costs more than it saves, because agents are good enough at merge conflicts that the tradeoff is not as harsh as it looks. The one piece of discipline worth keeping is to do large refactors first. A large rename landing after ten branches have forked off it is the case that stays expensive.

<!-- zh-CN:begin ec8b10091892d2d5 -->

大多不必。并行任务划文件区的成本高于收益；代理已足够擅长合并冲突，取舍没有看上去那么严苛。值得保留的纪律是先做大重构：大型重命名若在十个分支分叉后才落地，成本仍高。

<!-- zh-CN:end ec8b10091892d2d5 -->

One caveat from a user report on parallel worktrees: when sibling [sessions](https://www.aihero.dev/ai-coding-dictionary/session) each build a ticket in their own tree, the merge back is best done by the session that wrote the change, because it is the one that already knows the intent. If one agent resolves everybody's conflicts at the end, it loses the [context](https://www.aihero.dev/ai-coding-dictionary/context) that step 2 of this skill must then rebuild.

<!-- zh-CN:begin 28010d63aa9d5a7f -->

关于并行工作树的一条用户提醒：兄弟[会话](https://www.aihero.dev/ai-coding-dictionary/session)各自在自己的树里开发工单时，最好由编写改动的会话完成合并，因为它已知意图。若最后让一个代理解决所有人的冲突，会丢失[上下文](https://www.aihero.dev/ai-coding-dictionary/context)，本技能第 2 步又须重建。

<!-- zh-CN:end 28010d63aa9d5a7f -->

**Why never `--abort`?**

<!-- zh-CN:begin 97b0673505d7056f -->

**为什么绝不 `--abort`？**

<!-- zh-CN:end 97b0673505d7056f -->

Aborting throws away the resolution work and returns you to the same conflict, unchanged, the next time you try. The skill is written for the case where the merge is going to happen. If you have decided it should not happen, that is a decision to make before invoking, not a branch inside the loop.

<!-- zh-CN:begin fa7b43887bd07096 -->

中止会丢弃解决工作，下次仍回到相同冲突。技能假定合并最终会进行；若决定不应合并，应在调用前决定，而不是在循环中开分支。

<!-- zh-CN:end fa7b43887bd07096 -->

## It's working if

<!-- zh-CN:begin 15c4dc1d02cd31ef -->

## 怎样算正常工作

<!-- zh-CN:end 15c4dc1d02cd31ef -->

- The agent quotes commit messages, PRs or issues at you while resolving, not just diff hunks.

<!-- zh-CN:begin 1d782187c5e63da6 -->

- 解决时引用提交消息、PR 或议题，而非只看差异块。

<!-- zh-CN:end 1d782187c5e63da6 -->
- Every hunk ends up with both sides' behaviour, or with an explicit note naming what was dropped and why.

<!-- zh-CN:begin 178f4313c1695f72 -->

- 每个块最终包含双方行为，或明确说明舍弃什么及原因。

<!-- zh-CN:end 178f4313c1695f72 -->
- Nothing appears in the result that was on neither branch.

<!-- zh-CN:begin e9b7b12d99f1d9a6 -->

- 结果不出现两边都没有的内容。

<!-- zh-CN:end e9b7b12d99f1d9a6 -->
- The agent found typecheck, tests and format and ran them green *before* the commit, not after you noticed something broken.

<!-- zh-CN:begin 726a7b0f19e934a9 -->

- 代理找到类型检查、测试与格式化，并在提交*前*通过，而不是你发现异常后才跑。

<!-- zh-CN:end 726a7b0f19e934a9 -->
- You end on a clean tree with the operation completed, including every remaining commit in a multi-commit rebase.

<!-- zh-CN:begin adf0af0c53de0d02 -->

- 工作区干净且操作已完成；多提交 rebase 中剩余提交也已完成。

<!-- zh-CN:end adf0af0c53de0d02 -->

## Where it fits

<!-- zh-CN:begin e2467ef5079b2817 -->

## 适用范围

<!-- zh-CN:end e2467ef5079b2817 -->

A reach-for-it-anytime standalone with no dependencies on any other skill: it starts when git stalls and ends when the tree is clean and committed. Its only real neighbour is [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs), which takes over at the point where a merge resolved cleanly but the merged code misbehaves: a diagnosis problem, not a conflict one. It is outside the main idea-to-ship flow, so [ask-matt](https://aihero.dev/skills-ask-matt) is the map for what runs before and after it.

<!-- zh-CN:begin 1b070a623f531e99 -->

独立使用，无依赖：git 卡住时启动，树干净并提交后结束。唯一邻近的是[diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs)：合并干净但结果异常时，那是诊断问题。它不在想法到发布主流程中，[ask-matt](https://aihero.dev/skills-ask-matt) 是前后流程地图。

<!-- zh-CN:end 1b070a623f531e99 -->
