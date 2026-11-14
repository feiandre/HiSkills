# Make it yours

<!-- zh-CN:begin 6556f76a80f0fd3c -->

# 让它成为你的风格

<!-- zh-CN:end 6556f76a80f0fd3c -->

poteto-mode is one person's style. The playbooks, routing, and model roles underneath it work just as well with yours. This page covers generating a personal mode, capturing lessons from a session, fixing the repo so agents stop repeating mistakes, authoring a focused skill, and testing a skill change before you trust it.

<!-- zh-CN:begin 138b90a0cebf3bc0 -->

poteto-mode 是某一个人的风格。其下方的操作手册、路由和模型角色也完全适用于你的风格。本页介绍如何生成个人模式、从会话中捕获经验、修复仓库让智能体不再重复错误、编写聚焦技能，以及在信任技能改动前先进行测试。

<!-- zh-CN:end 138b90a0cebf3bc0 -->

Start smaller than you think. You don't need many skills on day one, or even this whole plugin. Prompt plainly, watch where agents fail, and add a skill or a check when the same failure shows up twice.

<!-- zh-CN:begin 82420531186a58fd -->

从比你想象中更小的起点开始。第一天不需要很多技能，甚至不需要整个插件。用普通提示词工作，观察智能体在哪里失败；同一种失败出现两次时，再加入技能或检查。

<!-- zh-CN:end 82420531186a58fd -->

## Generate your own mode with `/automate-me`

<!-- zh-CN:begin 21ae0fbb10d1bef9 -->

## 用 `/automate-me` 生成你的模式

<!-- zh-CN:end 21ae0fbb10d1bef9 -->

```text
/automate-me
```

You don't describe your style, because [`/automate-me`](../../skills/automate-me/SKILL.md) reads it out of your history. It mines your recent transcripts in the active workspace for repeated preferences, in how you like replies, delegation, verification, code, prose, and process, then asks you which patterns are really you. It drafts `.cursor/skills/<your-name>-mode/SKILL.md` through Cursor's built-in `create-skill` flow, runs the draft through [`/unslop`](../../skills/unslop/SKILL.md), and opens a PR from a worktree so you review it like any other change.

<!-- zh-CN:begin ca831d718e9ae51c -->

你不需要描述自己的风格，因为 [`/automate-me`](../../skills/automate-me/SKILL.md) 会从历史中读取它。它挖掘当前工作区的近期会话记录，寻找你在回复、委派、验证、代码、文字和流程上的重复偏好，再询问哪些模式确实属于你。它通过 Cursor 内置 `create-skill` 流程起草 `.cursor/skills/<your-name>-mode/SKILL.md`，让草稿经过 [`/unslop`](../../skills/unslop/SKILL.md)，并从工作树创建 PR，供你像审查其他改动一样审查。

<!-- zh-CN:end ca831d718e9ae51c -->

Run it again whenever your habits drift:

<!-- zh-CN:begin 5516da5e11675e01 -->

习惯发生变化时，再次运行：

<!-- zh-CN:end 5516da5e11675e01 -->

```text
/automate-me update my mode skill with everything since its last edit
```

<!-- zh-CN:begin cf04e86af4360783 -->

```text
/automate-me 用上次编辑以来的所有内容更新我的模式技能
```

<!-- zh-CN:end cf04e86af4360783 -->

Update mode mines only the history since the skill last changed. It keeps rules you haven't contradicted, revises the ones with new evidence, and adds sections only for new patterns.

<!-- zh-CN:begin 553de663a110051c -->

更新模式只挖掘技能上次更改后的历史。它保留未被你否定的规则，根据新证据修订规则，并仅为新模式添加章节。

<!-- zh-CN:end 553de663a110051c -->

## Capture a session's lessons with `/reflect`

<!-- zh-CN:begin 1932adcf7e01f95b -->

## 用 `/reflect` 捕获会话经验

<!-- zh-CN:end 1932adcf7e01f95b -->

Right after a task that taught you something, run:

<!-- zh-CN:begin 84a56fd8615e3429 -->

刚完成一次让你有所收获的任务后，运行：

<!-- zh-CN:end 84a56fd8615e3429 -->

```text
/reflect that took way too long. capture what we learned so the next run doesn't repeat it.
```

<!-- zh-CN:begin 55c2064ced92c403 -->

```text
/reflect 那花了太久。记录我们学到的内容，让下次运行不再重复。
```

<!-- zh-CN:end 55c2064ced92c403 -->

[`/reflect`](../../skills/reflect/SKILL.md) sends the transcript to three parallel reviewers, then a synthesizer sorts the proposals into `Accepted`, `Rejected`, and `Backlog` and waits for your approval before any skill changes. Approve a proposal only if it would change a future decision. One weird session is an anecdote, not a rule.

<!-- zh-CN:begin 1cf8d17a57069b93 -->

[`/reflect`](../../skills/reflect/SKILL.md) 把会话记录交给三个并行评审者，再由综合者把建议分为 `Accepted`、`Rejected` 和 `Backlog`，并在修改技能前等待你批准。只有建议会改变未来决策时才批准。一次异常会话只是轶事，不是规则。

<!-- zh-CN:end 1cf8d17a57069b93 -->

## Fix the environment with `/correct`

<!-- zh-CN:begin d3dd178e25454dcf -->

## 用 `/correct` 修复环境

<!-- zh-CN:end d3dd178e25454dcf -->

When you correct agents for the same mistake again and again, the fix belongs in the repo, not in your next prompt. Rank the options by how well they hold:

<!-- zh-CN:begin ffb22b0525113146 -->

当你一遍又一遍纠正智能体同一个错误时，修复应落在仓库中，而不是下一条提示词里。按可靠程度给方案排序：

<!-- zh-CN:end ffb22b0525113146 -->

1. Make the mistake impossible with architecture or a better data structure.

<!-- zh-CN:begin fdb91d76710397ed -->

1. 用架构或更好的数据结构让错误无法发生。

<!-- zh-CN:end fdb91d76710397ed -->
2. Block it with types, or with a lint or CI check whose error names the fix.

<!-- zh-CN:begin 0c71843de5b71809 -->

2. 用类型、lint 或 CI 检查阻止它，并让错误点名修复方式。

<!-- zh-CN:end 0c71843de5b71809 -->
3. Catch it with a test.

<!-- zh-CN:begin 9b6471892dd6fae8 -->

3. 用测试捕获它。

<!-- zh-CN:end 9b6471892dd6fae8 -->
4. Write it down as a doc or agent rule. Nothing fails when an agent skips a rule, so this comes last.

<!-- zh-CN:begin 5136bcdd01b98f1e -->

4. 把它写成文档或智能体规则。智能体跳过规则时不会有任何失败，因此放在最后。

<!-- zh-CN:end 5136bcdd01b98f1e -->

Human review isn't on the list. A reviewer who must catch the same mistake on every PR is the problem this fixes. [`/correct`](../../skills/correct/SKILL.md) does the work:

<!-- zh-CN:begin 9c287ab4c772c7a7 -->

人工审查不在列表中。每个 PR 都要求评审者捕获同一错误，正是本技能要解决的问题。[`/correct`](../../skills/correct/SKILL.md) 执行这些工作：

<!-- zh-CN:end 9c287ab4c772c7a7 -->

```text
/correct agents keep calling the database client directly instead of going through the repository layer
```

<!-- zh-CN:begin 99ad8eb9db0e5e96 -->

```text
/correct 智能体总是直接调用数据库客户端，而不是经过仓库层
```

<!-- zh-CN:end 99ad8eb9db0e5e96 -->

It reads recent commits, reverts, review comments, and comments that explain workarounds, then groups the mistakes into classes. A class counts once it has happened twice. It fixes the most frequent classes one commit each, at the highest level that works, and proves each new check fails on a real past mistake. It also keeps a table in the agent instruction file that pairs each rule with what enforces it, so a rule that nothing enforces shows up as a repeat. The reply lists each class with its evidence, the level chosen, and why a higher level didn't work.

<!-- zh-CN:begin 097b336f7f2bb77a -->

它读取近期提交、回退、评审评论和解释变通办法的评论，然后把错误分成类别。一个类别发生两次才计入。它在能够奏效的最高层修复最频繁的类别，每类一个提交，并证明每项新检查会在真实历史错误上失败。它还在智能体指令文件中维护一张表，把每条规则和执行机制配对，使无人执行的规则显示为重复项。回复列出每个类别、证据、所选层级，以及更高层为何无效。

<!-- zh-CN:end 097b336f7f2bb77a -->

Run it with no argument and it finds the classes from history on its own. `/reflect` and `/correct` split the work. `/reflect` improves skills from one session. `/correct` changes the repo so a mistake class can't come back. Pair it with `/architect` when the fix is a new boundary. [Run many projects in parallel](./07-overnight.md#run-many-projects-in-parallel) has a prompt that does both across a whole repo.

<!-- zh-CN:begin f2a23bb06c95b70b -->

不带参数运行，它会自行从历史中发现类别。`/reflect` 与 `/correct` 分担工作：`/reflect` 从一次会话改进技能；`/correct` 修改仓库，使某类错误无法回来。修复需要新边界时，与 `/architect` 搭配。[并行运行多个项目](./07-overnight.md#run-many-projects-in-parallel) 提供一个可跨整个仓库完成二者的提示词。

<!-- zh-CN:end f2a23bb06c95b70b -->

## Author a focused skill

<!-- zh-CN:begin 45af922924f7db1b -->

## 编写聚焦技能

<!-- zh-CN:end 45af922924f7db1b -->

When you already know the workflow you want to capture:

<!-- zh-CN:begin abd5d6c2ee1874db -->

已经知道要记录的工作流时：

<!-- zh-CN:end abd5d6c2ee1874db -->

```text
/poteto-mode write a skill for verifying database migrations in this repo
```

<!-- zh-CN:begin fed2afe45ff72eae -->

```text
/poteto-mode 为在此仓库验证数据库迁移编写一个技能
```

<!-- zh-CN:end fed2afe45ff72eae -->

Writing a skill matches the [Authoring or modifying a skill playbook](../../skills/poteto-mode/playbooks/authoring-a-skill.md), which routes through Cursor's built-in `create-skill`, validates the frontmatter and links, and ships the result through the Opening a PR playbook. Agent-facing prose has a higher bar than human prose, because an unhelpful sentence becomes an instruction some future agent follows. Let the playbook hold that bar rather than writing a `SKILL.md` freehand.

<!-- zh-CN:begin 343256fa00c9792d -->

编写技能会匹配[编写或修改技能手册](../../skills/poteto-mode/playbooks/authoring-a-skill.md)，后者通过 Cursor 内置 `create-skill` 路由，验证前置元数据和链接，并通过创建 PR 手册交付结果。面向智能体的文字标准高于面向人类的文字，因为无用句子会变成未来智能体遵循的指令。让手册承担这一标准，不要手写 `SKILL.md`。

<!-- zh-CN:end 343256fa00c9792d -->

Two special cases have their own generators. A skill that must drive your app and prove behavior is a verification skill, so use [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) and [`/maintain-verification-skill`](../../skills/maintain-verification-skill/SKILL.md) instead. A skill that checks a property of your code with a model checker, a proof, or another verifier is a formal verification skill, so use [`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md) and [`/maintain-formal-verification-skill`](../../skills/maintain-formal-verification-skill/SKILL.md). [Verify and ship](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill) covers both kinds.

<!-- zh-CN:begin ab0bda7379316c8a -->

两个特殊情况各有生成器。必须驱动应用并证明行为的技能属于验证技能，应使用 [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) 和 [`/maintain-verification-skill`](../../skills/maintain-verification-skill/SKILL.md)。通过模型检查器、证明或其他验证器检查代码性质的技能属于形式化验证技能，应使用 [`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md) 和 [`/maintain-formal-verification-skill`](../../skills/maintain-formal-verification-skill/SKILL.md)。[验证与交付](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill) 涵盖两类。

<!-- zh-CN:end ab0bda7379316c8a -->

## Write docs to a standard with `/technical-writing`

<!-- zh-CN:begin 014f1e47cfe63fe4 -->

## 用 `/technical-writing` 按标准编写文档

<!-- zh-CN:end 014f1e47cfe63fe4 -->

Skills aren't the only prose you ship. For docs, RFCs, readmes, PR descriptions, and commit messages:

<!-- zh-CN:begin d761de188b187a32 -->

技能不是唯一需要交付的文字。对于文档、RFC、README、PR 描述和提交消息：

<!-- zh-CN:end d761de188b187a32 -->

```text
/technical-writing review the readme changes
```

<!-- zh-CN:begin 70ec5bfbca782dea -->

```text
/technical-writing 审查 README 改动
```

<!-- zh-CN:end 70ec5bfbca782dea -->

[`/technical-writing`](../../skills/technical-writing/SKILL.md) applies a layered standard. Its goal is prose that a tired engineer understands on the first read. It picks the document's mode first (tutorial, how-to, reference, or explanation), then works sentence by sentence: who does what, one thought per sentence, nothing readable two ways. Use it to review what you or an agent just wrote, or name it up front when you ask for a doc.

<!-- zh-CN:begin 0bf47a01e4d667ee -->

[`/technical-writing`](../../skills/technical-writing/SKILL.md) 应用分层标准，目标是让疲惫工程师第一次阅读就能理解。它先确定文档模式（教程、操作指南、参考或解释），再逐句处理：谁做什么、一句一个想法、不留下两种读法。可用它审查你或智能体刚写的文字，或在请求文档时预先点名。

<!-- zh-CN:end 0bf47a01e4d667ee -->

## Test a skill change blind

<!-- zh-CN:begin 1a4d6696c3e4715c -->

## 盲测技能改动

<!-- zh-CN:end 1a4d6696c3e4715c -->

A skill edit affects every future session, so test it like the experiment it is. The same goes for adopting someone else's skill. Check that it makes the agent better on your work before you keep it.

<!-- zh-CN:begin c3adf4bba276c562 -->

技能编辑会影响未来每个会话，因此应像实验一样测试。采用别人的技能也一样。保留前先确认它确实能改进智能体在你的工作上的表现。

<!-- zh-CN:end c3adf4bba276c562 -->

```text
/poteto-mode run the eval playbook on this skill change. same task for both variants, candidates stay blind.
```

<!-- zh-CN:begin c4eae81d4b2525f3 -->

```text
/poteto-mode 对这个技能改动运行评测手册。两个变体使用同一任务，候选保持盲测。
```

<!-- zh-CN:end c4eae81d4b2525f3 -->

When a skill keeps missing and you know what it should do, change and test it in one task:

<!-- zh-CN:begin bfff4a97ee348cf9 -->

技能一直遗漏，而你又知道它该做什么时，在同一任务中修改并测试：

<!-- zh-CN:end bfff4a97ee348cf9 -->

```text
/poteto-mode update the review skill so it flags missing migrations, and eval the change.
```

<!-- zh-CN:begin cc55aca96a657efb -->

```text
/poteto-mode 更新审查技能，使它标记缺失的迁移，并评测改动。
```

<!-- zh-CN:end cc55aca96a657efb -->

Asking for the eval up front keeps the edit honest. A fix written from one bad session tends to overfit that session, and over many edits the skill drifts. The eval catches the drift before it ships.

<!-- zh-CN:begin 7de5b337e4523cb2 -->

预先要求评测能让编辑保持诚实。因一次糟糕会话写出的修复容易过拟合该会话，经过多次编辑后技能会漂移。评测在交付前捕获漂移。

<!-- zh-CN:end 7de5b337e4523cb2 -->

The [Eval playbook](../../skills/poteto-mode/playbooks/eval.md) is built around one failure mode, the observer effect. An agent that knows it's being evaluated behaves differently. So candidate agents get an organic-looking task in sanitized directories, never the words "eval" or "candidate", and never each other's existence. One judge scores all outputs under neutral labels, and chain-following gets graded from which files each candidate actually read, not from what it claims.

<!-- zh-CN:begin 8d5efb4215e4fbcf -->

[评测手册](../../skills/poteto-mode/playbooks/eval.md) 围绕一个故障模式设计：观察者效应。知道自己在被评测的智能体行为会不同。因此候选智能体在净化目录中收到看起来自然的任务，其中绝不出现“eval”或“candidate”字样，也互不知道对方存在。一名裁判在匿名标签下为所有输出评分，链式跟进依据候选实际读取的文件评分，而非其自称。

<!-- zh-CN:end 8d5efb4215e4fbcf -->

Read every output yourself before accepting the verdict. If you disagree with the judge, suspect the rubric before you suspect your judgment.

<!-- zh-CN:begin 9b52bc9697830f4f -->

接受判决前亲自阅读每个输出。若不同意裁判，先怀疑评分标准，再怀疑自己的判断。

<!-- zh-CN:end 9b52bc9697830f4f -->

## Build a bot UI with `/make-bot-ui`

<!-- zh-CN:begin cb44b836d2ba78dd -->

## 用 `/make-bot-ui` 构建机器人 UI

<!-- zh-CN:end cb44b836d2ba78dd -->

One situational skill is for Grok Bot users. [`/make-bot-ui`](../../skills/make-bot-ui/SKILL.md) builds a small page whose buttons wake a bot over a webhook routine. For example, you could swipe through a review queue and have each swipe ask the bot to act on that item. A server on your machine holds the webhook's sender key, so the key never reaches the browser or the chat. The skill also covers exposing the page on Tailscale.

<!-- zh-CN:begin ff4b0d8128c6b4cb -->

有一个适合 Grok Bot 用户的情境技能。[`/make-bot-ui`](../../skills/make-bot-ui/SKILL.md) 构建一个小页面，其按钮通过 Webhook routine 唤醒机器人。例如，你可以在评审队列中滑动，每次滑动请求机器人处理该项。本机服务器保存 Webhook 的发送方密钥，因此密钥不会进入浏览器或聊天。技能还涵盖通过 Tailscale 公开页面。

<!-- zh-CN:end ff4b0d8128c6b4cb -->

**Pitfall:** don't edit a skill mid-task because it's misbehaving. Fix it in its own PR and keep the task moving. A skill edit that ships tangled into feature work is invisible to review and impossible to evaluate.

<!-- zh-CN:begin 8cdca998fcf45544 -->

**陷阱：** 不要因为技能表现不佳就在任务中途编辑它。另开 PR 修复，并让当前任务继续。纠缠进功能工作的技能编辑无法被审查，也无法被评测。

<!-- zh-CN:end 8cdca998fcf45544 -->

Next: [Recipes and pitfalls](./10-recipes-and-pitfalls.md).

<!-- zh-CN:begin fa69cbcf60765bb8 -->

下一步：[配方与陷阱](./10-recipes-and-pitfalls.md)。

<!-- zh-CN:end fa69cbcf60765bb8 -->
