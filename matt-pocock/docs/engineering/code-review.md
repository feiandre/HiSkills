## What it does

<!-- zh-CN:begin dbc5ce439baa4cda -->

## 它的作用

<!-- zh-CN:end dbc5ce439baa4cda -->

`code-review` reviews the diff between `HEAD` and a fixed point you name (a commit, a branch, a tag, `main`, `HEAD~5`) along two axes. **Standards** asks whether the code follows how this repo writes code. **Spec** asks whether the code does what the originating issue or [spec](https://www.aihero.dev/ai-coding-dictionary/spec) asked for. Each axis runs in its own [sub-agent](https://www.aihero.dev/ai-coding-dictionary/subagent) so neither sees the other's reasoning.

<!-- zh-CN:begin 923b248be5cb4838 -->

`code-review` 沿两条轴线审查 `HEAD` 与你指定固定点（提交、分支、标签、`main`、`HEAD~5`）之间的差异。**标准**询问代码是否遵循本仓库写法。**规格**询问代码是否实现来源 issue 或[规格](https://www.aihero.dev/ai-coding-dictionary/spec)要求。每条轴在独立[子智能体](https://www.aihero.dev/ai-coding-dictionary/subagent)中运行，互不了解推理。

<!-- zh-CN:end 923b248be5cb4838 -->

The skill never merges or re-ranks the two axes. The report ends with a worst issue *per axis* and declines to name a single winner across them. A change can pass one axis and fail the other. Code that follows every convention but implements the wrong thing passes Standards and fails Spec. Code that does exactly what the [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) asked but breaks the repo's conventions does the reverse. A blended verdict lets the passing axis hide the failing one.

<!-- zh-CN:begin d6f27b1e582d107d -->

技能绝不合并或重新排序两轴。报告分别给出每轴最严重问题，拒绝选出跨轴唯一赢家。变更可通过一轴而失败另一轴。完全守约但实现错误内容，标准通过、规格失败。准确执行[票](https://www.aihero.dev/ai-coding-dictionary/ticket)要求却破坏仓库约定的代码相反。混合结论会让通过轴掩盖失败轴。

<!-- zh-CN:end d6f27b1e582d107d -->

## When to reach for it

<!-- zh-CN:begin a0cb2767402c2f2e -->

## 何时使用

<!-- zh-CN:end a0cb2767402c2f2e -->

Type `/code-review`, or the agent reaches for it automatically when you ask to review a branch, a PR, work in progress, or anything "since X".

<!-- zh-CN:begin 31d20568ab2c0a1e -->

输入 `/code-review`，或在你要求审查分支、PR、进行中工作或任何“自 X 以来”内容时由智能体自动使用。

<!-- zh-CN:end 31d20568ab2c0a1e -->

| Your situation | Reach for |
| --- | --- |
| A diff exists and you want to know if it is built right *and* is the right thing | `code-review` |
| You want bugs hunted in the diff: null paths, races, off-by-one | Claude Code's own built-in review, not this one (see the name clash below) |
| Nothing is written yet and you want it written test-first | [tdd](https://aihero.dev/skills-tdd) |
| A whole spec needs building, review included | [implement](https://aihero.dev/skills-implement), which calls this skill itself |
| The whole codebase has drifted, not one diff | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) |
| Something is broken and you do not know why | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

<!-- zh-CN:begin 774de44a0bd82a93 -->

| 情况 | 使用 |
|---|---|
| 已有差异，想知道构建是否正确*且*内容是否对 | `code-review` |
| 想在差异中抓 bug：空路径、竞态、差一错误 | Claude Code 自带审查，本技能不负责（见下方名称冲突） |
| 尚无代码，想测试先行编写 | [tdd](https://aihero.dev/skills-tdd) |
| 需要构建整个规格，包括审查 | [implement](https://aihero.dev/skills-implement)，它会自行调用本技能 |
| 整个代码库漂移，而非单个差异 | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) |
| 有东西坏了且不知道原因 | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

<!-- zh-CN:end 774de44a0bd82a93 -->

You must supply the fixed point. If you do not, the skill asks for one rather than guessing. Before it spawns anything, it checks that the ref resolves and that the diff is not empty, so a mistyped branch name fails in front of you instead of inside two sub-agents.

<!-- zh-CN:begin 28188023ea346b50 -->

必须提供固定点。未提供时技能会询问而不猜。启动任何内容前，它检查引用解析成功且差异非空，因此分支名拼错会在你眼前失败，而不是两个子智能体内部。

<!-- zh-CN:end 28188023ea346b50 -->

## Prerequisites

<!-- zh-CN:begin 3c50c82918b4c3fb -->

## 前提条件

<!-- zh-CN:end 3c50c82918b4c3fb -->

The Standards axis needs nothing. It reads whatever the repo documents (`CODING_STANDARDS.md`, `CONTRIBUTING.md`, and the like) and falls back on a built-in baseline when the repo documents nothing.

<!-- zh-CN:begin 1c6365edc7231c26 -->

标准轴无需前提，读取仓库文档（`CODING_STANDARDS.md`、`CONTRIBUTING.md` 等）；无文档时使用内建基线。

<!-- zh-CN:end 1c6365edc7231c26 -->

The Spec axis needs a spec to exist and be findable. It looks in this order:

<!-- zh-CN:begin 95d44816e0f606a5 -->

规格轴需要存在且可找到的规格。按此顺序查找：

<!-- zh-CN:end 95d44816e0f606a5 -->

1. Issue references in the commit messages (`#123`, `Closes #45`, a GitLab `!67`), fetched through the tracker doc.

<!-- zh-CN:begin 75879a0573cbda8f -->

1. 提交消息中的 issue 引用（`#123`、`Closes #45`、GitLab `!67`），通过跟踪器文档获取。

<!-- zh-CN:end 75879a0573cbda8f -->
2. A path you pass in as an argument.

<!-- zh-CN:begin e77b8c16924c3f68 -->

2. 作为参数传入的路径。

<!-- zh-CN:end e77b8c16924c3f68 -->
3. A spec file under `docs/`, `specs/`, or `.scratch/` matching the branch or feature name.

<!-- zh-CN:begin 2436ce146ffedaa1 -->

3. `docs/`、`specs/` 或 `.scratch/` 下匹配分支或功能名的规格文件。

<!-- zh-CN:end 2436ce146ffedaa1 -->
4. Asking you.

<!-- zh-CN:begin 128afd9fcb978efd -->

4. 询问你。

<!-- zh-CN:end 128afd9fcb978efd -->

Step 1 depends on the tracker doc, which [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) writes. Without it the axis still works if you hand it a path. With no spec at all, the skill skips the Spec sub-agent and the report says "no spec available" rather than inventing requirements.

<!-- zh-CN:begin 4e4151cc7e7d7ae6 -->

步骤 1 依赖 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 写入的跟踪器文档。没有它，只要提供路径，该轴仍工作。完全没有规格时跳过规格子智能体，报告“无可用规格”，不编造要求。

<!-- zh-CN:end 4e4151cc7e7d7ae6 -->

## The two axes

<!-- zh-CN:begin 2f4b3c34759d6195 -->

## 两条轴

<!-- zh-CN:end 2f4b3c34759d6195 -->

| | Standards | Spec |
| --- | --- | --- |
| Question | Is it built right? | Is it the right thing? |
| Reads | The repo's documented standards, plus the smell baseline | The originating issue or spec |
| Reports | Documented breaches (can be hard), and smells (always judgement calls) | Missing or partial requirements, scope creep, requirements implemented wrongly |
| Every finding cites | The standards file and the rule, or the named smell plus the hunk | The line of the spec |

<!-- zh-CN:begin 7cffb30af9c99998 -->

| | 标准 | 规格 |
|---|---|---|
| 问题 | 构建得对吗？ | 做的是正确的事吗？ |
| 读取 | 仓库记录标准及坏味道基线 | 来源 issue 或规格 |
| 报告 | 已记录违规（可算硬性问题）及坏味道（始终是判断性） | 缺失或部分要求、范围蔓延、实现错误要求 |
| 每个发现引用 | 标准文件及规则，或具名坏味道及代码块 | 规格相应行 |

<!-- zh-CN:end 7cffb30af9c99998 -->

This design exists to avoid a generic review skill that does not know your standards. Such a skill flags what is deliberate in your codebase and misses the invariants your codebase depends on. So the repo's own documentation is the [primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source) on the Standards axis, and **the repo always overrides**.

<!-- zh-CN:begin 0db28af11214fad7 -->

此设计避免不懂标准的通用审查技能。通用技能会把你的有意选择标成问题，漏掉代码库依赖的不变量。因此仓库文档是标准轴的[一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)，**仓库始终优先**。

<!-- zh-CN:end 0db28af11214fad7 -->

The **smell baseline** sits under the repo's standards. It is twelve code smells from chapter 3 of Fowler's _Refactoring_: Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest. Each is a labelled heuristic ("possible Feature Envy"), never a hard violation. Each states what the smell is and how to fix it, so a finding comes with a fix attached rather than only a complaint. Both axes skip anything your linter already enforces.

<!-- zh-CN:begin 0ee91ffdd71d5145 -->

**坏味道基线**位于仓库标准之下。它来自 Fowler《重构》第 3 章的十二种代码坏味道：神秘名称、重复代码、依恋情结、数据泥团、基本类型偏执、重复 switch、霰弹式修改、发散式变化、夸夸其谈通用性、消息链、中间人、被拒绝的遗赠。每种都标记为启发式（“可能有依恋情结”），绝不是硬性违规。每种说明是什么及如何修复，因此发现附带修复而不只是抱怨。两轴都跳过 linter 已强制执行的内容。

<!-- zh-CN:end 0ee91ffdd71d5145 -->

## Common questions

<!-- zh-CN:begin 5b84253839992a82 -->

## 常见问题

<!-- zh-CN:end 5b84253839992a82 -->

**It collides with Claude Code's own `/code-review`. What do I do?**

<!-- zh-CN:begin f6a20ba7afb8ee66 -->

**它与 Claude Code 自带 `/code-review` 冲突。怎么办？**

<!-- zh-CN:end f6a20ba7afb8ee66 -->

This is the most reported problem with the skill, and it is not fixed. Claude Code ships its own `/code-review`, which does something different: it hunts bugs in the diff, where this one checks spec compliance and repo standards. When you install this library, one of them wins, and which one depends on how you installed:

<!-- zh-CN:begin de12ebc82edb6f46 -->

这是报告最多的问题且未解决。Claude Code 自带命令抓差异中的 bug，本技能检查规格和仓库标准。安装本库时，两者之一胜出，取决于安装方式：，相关标识为 `/code-review`。

<!-- zh-CN:end de12ebc82edb6f46 -->

- **Plugin marketplace.** Every skill gets a `mattpocock-skills:` prefix, and the built-in becomes hard to reach at the unqualified name.

<!-- zh-CN:begin 9b25147dd8ad6a88 -->

- **插件市场。** 每个技能获得 `mattpocock-skills:` 前缀，内建功能在无前缀名称下较难到达。

<!-- zh-CN:end 9b25147dd8ad6a88 -->
- **Plain skills install.** The local file wins, and this skill shadows the built-in.

<!-- zh-CN:begin 49c1f6b4c9562091 -->

- **普通 skills 安装。** 本地文件胜出，本技能遮蔽内建功能。

<!-- zh-CN:end 49c1f6b4c9562091 -->

One answer is to remove Claude Code's built-in skills entirely. That saves a lot of [context](https://www.aihero.dev/ai-coding-dictionary/context), and the collision stops mattering. The shadowing itself is arguably a Claude Code [harness](https://www.aihero.dev/ai-coding-dictionary/harness) bug (a skill author should be free to name a skill anything), so the other answer is to rename the local copy. `npx skills update` undoes an edit to the frontmatter or a renamed directory. The durable workaround users report is to fork the skill to a new name and drop `code-review` from the managed set. Keep a note of the commit you forked from so you can re-sync by hand.

<!-- zh-CN:begin 56e6eafc67aed026 -->

一种办法彻底移除 Claude Code 内建技能，节省大量[上下文](https://www.aihero.dev/ai-coding-dictionary/context)，冲突消失。遮蔽本身可算 Claude Code [运行环境](https://www.aihero.dev/ai-coding-dictionary/harness)缺陷（技能作者应能给技能随意命名），另一种办法是重命名本地副本。`npx skills update` 会撤销 frontmatter 或目录重命名。用户报告的持久变通是 fork 技能为新名并从托管集合移除 `code-review`，记录 fork 提交以便手动重同步。

<!-- zh-CN:end 56e6eafc67aed026 -->

**Its sub-agents keep invoking `/code-review` again and spawn more agents.**

<!-- zh-CN:begin c6e3bebbc88a76fa -->

**子智能体反复调用 `/code-review` 并产生更多智能体。**

<!-- zh-CN:end c6e3bebbc88a76fa -->

This is a known open bug. Several people have reproduced it, in more than one harness. The Standards and Spec prompts do not forbid delegation, so a sub-agent can find the skill again and fan out again. One report reached more than 50 agents. The fix people have applied on forks is one line appended to both sub-agent briefs: "Do not invoke `/code-review` or spawn additional agents: perform this review directly." Some prefer to handle it at the harness level so every skill inherits the guard. Neither is in the shipped skill yet. If you run this unattended, watch the agent count.

<!-- zh-CN:begin df2064252fb6f67a -->

已知开放 bug，多人已在不止一个运行环境复现。标准和规格提示未禁止委派，子智能体可再次发现技能并展开。一份报告超过 50 个智能体。fork 的修复是一行追加到两个简报：“不要调用 `/code-review` 或启动额外智能体：直接执行本次审查。”也有人选运行环境级处理使所有技能继承保护。两者均未发布。无人值守运行时监控智能体数量。

<!-- zh-CN:end df2064252fb6f67a -->

**Should I run it in the same [session](https://www.aihero.dev/ai-coding-dictionary/session) that wrote the code?**

<!-- zh-CN:begin c6e3718e03e9a2e7 -->

**应在写代码的同一[会话](https://www.aihero.dev/ai-coding-dictionary/session)中运行吗？**

<!-- zh-CN:end c6e3718e03e9a2e7 -->

Prefer a fresh one. As one reader put it: "Same context reviewing itself isn't review, it's confirmation bias with a slash command." An agent that reviews in the authoring session has every assumption that shaped the code in its context. An independent reviewer would not have that context. This is also why people ask for [implement](https://aihero.dev/skills-implement) without its built-in review step, because that step runs the review inside the session that just wrote the diff. The independent version is to invoke `/code-review` yourself from a clean session.

<!-- zh-CN:begin 6e6af68ec86c0e0a -->

优先新会话。一位读者说：“相同上下文审查自己没有审查，只是带斜杠命令的确认偏误。”作者会话中的审查智能体携带所有塑造代码的假设；独立审查员没有。这也是人们要求 [implement](https://aihero.dev/skills-implement) 不带内建审查步骤的原因；该步骤刚写完差异就审查。独立做法是在干净会话自行调用 `/code-review`。

<!-- zh-CN:end 6e6af68ec86c0e0a -->

**After every ticket, or once at the end?**

<!-- zh-CN:begin 09fe6771707e7782 -->

**每张票后运行，还是最后一次？**

<!-- zh-CN:end 09fe6771707e7782 -->

Both work, and the skill does not decide for you. Per-ticket keeps each diff small enough that the Spec axis has one clear spec to check against, which is the mode `implement` uses. Batching to the end of a branch catches interactions between tickets that the per-ticket passes each miss. If you are unsure, review per ticket and run one final pass against the branch point.

<!-- zh-CN:begin b32a6a0f5b9564eb -->

两者都可行，技能不替你决定。逐票保持差异小，使规格轴有清楚规格，这是 `implement` 的模式。最后批审能发现逐票遗漏的票间交互。不确定时逐票审查，并在分支点做一次最终检查。

<!-- zh-CN:end b32a6a0f5b9564eb -->

**Can I trust the findings?**

<!-- zh-CN:begin f9086bd698b25b65 -->

**发现可信吗？**

<!-- zh-CN:end f9086bd698b25b65 -->

Not without checking. Sub-agent output is a hypothesis, not evidence. One team reported a dozen breaking changes that prose-based reviews had missed. The skill combines the two reports as they are, or lightly cleaned. It does not re-verify each claim against the files, so a finding can cite the wrong location or overstate an impact. Read the citation on each finding before you act on it. The skill requires every finding to carry a citation (a standards rule, a smell plus its hunk, or a spec line), and that is what makes the findings checkable.

<!-- zh-CN:begin 980f1a3a3575ae7b -->

不核对不可信。子智能体输出是假设而非证据。一个团队报告基于文字的审查漏掉十几个破坏性变更。技能按原样或轻度清理合并两份报告，不逐条对照文件复核，因此可能引用错误位置或夸大影响。行动前阅读每个引用。技能要求每个发现带引用（标准规则、坏味道加代码块或规格行），这使发现可检查。

<!-- zh-CN:end 980f1a3a3575ae7b -->

**Why does it find new problems every single time I run it?**

<!-- zh-CN:begin 0ac0525817d8541d -->

**为何每次运行都发现新问题？**

<!-- zh-CN:end 0ac0525817d8541d -->

Each fix adds new code to review, and the judgement-call half of the Standards axis gives different results from run to run. One reader described the loop: "/code-review and /improve-code-architecture always find new stuff every time. I implement fixes, rerun these skills, and again and again." There is no convergence guarantee. Treat a pass as a list of leads. Act on the ones with a cited rule behind them, then stop. Do not run it in a loop until it comes back clean, because it never will.

<!-- zh-CN:begin 63d55c8e922d8cfb -->

每次修复增加新审查代码，标准轴的判断部分每次不同。一位读者描述循环：“/code-review 和 /improve-code-architecture 每次都发现新东西。我修复、重跑、再次重复。”没有收敛保证。把一次审查当成线索列表，处理有引用规则支持的问题后停止。不要循环到干净，因为永远不会。

<!-- zh-CN:end 63d55c8e922d8cfb -->

**Does it review my uncommitted work?**

<!-- zh-CN:begin ad085bd6745e112e -->

**会审查未提交工作吗？**

<!-- zh-CN:end ad085bd6745e112e -->

No. It diffs `<fixed-point>...HEAD`. The three-dot form measures from the merge-base and excludes staged and working-tree changes. If `implement` has not made an interim commit, the review cannot see the work that is about to go into the next commit. Commit first, then review, then amend or add a fixup.

<!-- zh-CN:begin 3862bf0800b785e5 -->

不会。它比较 `<fixed-point>...HEAD`。三点形式从合并基开始，排除暂存和工作树变更。若 `implement` 尚未做临时提交，审查看不到即将进入下一提交的工作。先提交、审查，再 amend 或添加 fixup。

<!-- zh-CN:end 3862bf0800b785e5 -->

## It's working if

<!-- zh-CN:begin ea5e14081dabdcb9 -->

## 生效时

<!-- zh-CN:end ea5e14081dabdcb9 -->

- It refuses to start on a bad ref or an empty diff, before any sub-agent is spawned.

<!-- zh-CN:begin bf32977b7479328d -->

- 坏引用或空差异时，在启动子智能体前拒绝运行。

<!-- zh-CN:end bf32977b7479328d -->
- The report arrives as two separate blocks under `## Standards` and `## Spec`, not one merged list.

<!-- zh-CN:begin 4314d26ca03ff29f -->

- 报告作为 `## Standards` 和 `## Spec` 两个独立块，不合并成一份列表。

<!-- zh-CN:end 4314d26ca03ff29f -->
- Every Standards finding names either a rule in one of your repo's files or one of the twelve smells, with the hunk quoted; every Spec finding quotes a line of the spec.

<!-- zh-CN:begin b48e4fe0853ee0ae -->

- 每个标准发现引用仓库文件规则或十二种坏味道之一并引用代码块；每个规格发现引用规格一行。

<!-- zh-CN:end b48e4fe0853ee0ae -->
- The closing summary gives a worst issue per axis and declines to pick an overall winner.

<!-- zh-CN:begin c7906ae95fa02f6e -->

- 结尾摘要给出每轴最严重问题，拒绝跨轴总赢家。

<!-- zh-CN:end c7906ae95fa02f6e -->
- With no spec available, the Spec block says so instead of listing requirements it inferred from the code.

<!-- zh-CN:begin 0fed1c8dd87fb073 -->

- 无规格时规格块明确说明，不从代码推断需求。

<!-- zh-CN:end 0fed1c8dd87fb073 -->

## Where it fits

<!-- zh-CN:begin 1bfd43bb8af2f459 -->

## 适用范围

<!-- zh-CN:end 1bfd43bb8af2f459 -->

`code-review` is the review step near the tail of the build chain: `grill-with-docs → to-spec → to-tickets → implement → code-review → retro`. It also stands alone on any branch or PR you point it at.

<!-- zh-CN:begin e3120046509cab45 -->

`code-review` 是构建链尾部的审查步骤：`grill-with-docs → to-spec → to-tickets → implement → code-review → retro`。也可单独用于任何分支或 PR。

<!-- zh-CN:end e3120046509cab45 -->

- [implement](https://aihero.dev/skills-implement) is the closest neighbour. It drives the build and calls this skill as its own closing review before committing. [implement-spec](https://aihero.dev/skills-implement-spec) does the same once, over the whole integration branch.

<!-- zh-CN:begin 7d003038b088c282 -->

- [implement](https://aihero.dev/skills-implement) 是最近邻，驱动构建并在提交前调用本技能作收尾审查。[implement-spec](https://aihero.dev/skills-implement-spec) 对整合分支整体同样做一次。

<!-- zh-CN:end 7d003038b088c282 -->
- [retro](https://aihero.dev/skills-retro) comes after it and tunes it. When a session shows the review missing a class of mistake, `retro` proposes the check or the `CODING_STANDARDS.md` rule the Standards axis then reads.

<!-- zh-CN:begin e45d99b19488198c -->

- [retro](https://aihero.dev/skills-retro) 随后调优。会话显示审查漏掉一类错误时，`retro` 提议检查或标准轴读取的 `CODING_STANDARDS.md` 规则。

<!-- zh-CN:end e45d99b19488198c -->
- [pr](https://aihero.dev/skills-pr) writes the pull request body once the reviewed work goes up.

<!-- zh-CN:begin 8ed190f59d0af212 -->

- [pr](https://aihero.dev/skills-pr) 在受审工作上传后编写 PR 正文。

<!-- zh-CN:end 8ed190f59d0af212 -->
- [to-spec](https://aihero.dev/skills-to-spec) and [to-tickets](https://aihero.dev/skills-to-tickets) produce the document the Spec axis checks against, so a vague spec makes that axis vague.

<!-- zh-CN:begin 844289d845b42fb9 -->

- [to-spec](https://aihero.dev/skills-to-spec) 和 [to-tickets](https://aihero.dev/skills-to-tickets) 生成规格轴对照文档；含糊规格会让该轴含糊。

<!-- zh-CN:end 844289d845b42fb9 -->
- [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) is the whole-codebase counterpart, because this skill only looks at one diff.

<!-- zh-CN:begin 2dc334ca169027f0 -->

- [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 是整代码库对应物，本技能只看一个差异。

<!-- zh-CN:end 2dc334ca169027f0 -->

[ask-matt](https://aihero.dev/skills-ask-matt) routes across the whole set when you are unsure which skill the situation wants.

<!-- zh-CN:begin 6863909bc9507a38 -->

不确定整套中该用哪个时，[ask-matt](https://aihero.dev/skills-ask-matt) 路由。

<!-- zh-CN:end 6863909bc9507a38 -->
