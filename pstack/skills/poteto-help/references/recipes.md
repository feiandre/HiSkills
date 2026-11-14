# 值得复制的提示

替换真实路径、技能和完成检查。非正式措辞也可以。

## 理解

- `/poteto-mode read <thread>. restate the underlying issue in your own words, in plain english.`（阅读指定线程，用平实中文重述底层问题。）

- `/in-your-own-words <long or messy ask>`（用自己的话重述冗长或混乱请求。）

- `/sharpen <the prompt you are about to send>`（打磨即将发送的提示。）；其中相关的字段或标识包括 `/sharpen <the prompt you're about to send>`。

- `/poteto-mode investigate why <symptom>. give me what we know, what data you used, and your best hypotheses. don’t change any code yet.`（调查症状，给出已知、所用数据和最佳假设，暂不改代码。）；其中相关的字段或标识包括 `/poteto-mode investigate why <symptom>. give me what we know, what data you used, and your best hypotheses. don't change any code yet.`。

- `use /how to understand <subsystem>. then use /why to find out why it broke recently.`（用 /how 理解子系统，再用 /why 查近期故障原因。）

- `/recall my work on <topic> from last week, then read <issue>.`（回忆上周主题工作，再阅读议题。）

- `/teach me why you implemented it this way and not <other way>. what did you trade off?`（说明为何采用此实现而非另一方式，做了什么取舍。）

- `/poteto-mode take over this branch. read the decision log, find what’s done, and continue. don’t redo finished work.`（接管分支，读决定日志，找出已完成部分并继续，不重做。）；其中相关的字段或标识包括 `/poteto-mode take over this branch. read the decision log, find what's done, and continue. don't redo finished work.`。

## 构建

- 缺陷：`/poteto-mode <symptom>. repro first, then fix and verify.`（先复现症状，再修复验证。）

- 应用缺陷：`/poteto-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.`（用验证技能复现；main 也复现则修复并提供视频证据。）

- 有低成本测试的缺陷：`/poteto-mode repro <bug> first. if there’s a cheap test path, /tdd it. then fix and rerun.`（先复现；有低成本测试路径则 TDD，再修复重跑。）；其中相关的字段或标识包括 `/poteto-mode repro <bug> first. if there's a cheap test path, /tdd it. then fix and rerun.`。

- 功能：`/poteto-mode add <behavior>. <current output> stays byte-identical. verify both.`（新增行为，保持现有输出逐字节相同，验证两者。）

- 重构：`/poteto-mode move <code> into one module, zero behavior change. record the current output first and prove it’s unchanged after.`（移入一个模块，行为零变化；先记录输出，事后证明不变。）；其中相关的字段或标识包括 `/poteto-mode move <code> into one module, zero behavior change. record the current output first and prove it's unchanged after.`。

- 性能：`/poteto-mode <operation> takes <time> on <fixture>. trace it, fix the measured cause, show me before and after.`（记录耗时，追踪并修复实测原因，展示前后。）

## 设计与计划

- `/poteto-mode prototype a few options for <feature>. take screenshots or videos for me to compare.`（为功能做多个原型，截图或录屏比较。）

- `/poteto-mode we need <feature>. /architect it first, and answer open questions with prototypes. let me review before proceeding.`（先架构设计，用原型回答未决问题，继续前让我审查。）

- `/poteto-mode write a tutorial for how i would use <new package> first. then /teach me why it beats the current one.`（先写使用教程，再解释为何优于当前方案。）

- `ask /arena for a second opinion on this thread and our approach.`（请 /arena 对线程和方法提供第二意见。）

- `/poteto-mode turn this design into a plan. small verifiable PRs, each with its own verification steps.`（把设计转计划，小型可验证 PR，每项独立验证。）

- `/poteto-mode plan the migration of <library> to <target>. small verifiable PRs. the result must match the original exactly, bugs included.`（规划迁移，小型可验证 PR，结果与原始完全一致，包括缺陷。）

## 审查与发布

- `/interrogate the whole branch, but skeptically. don’t change anything yet. no nitpicks unless it’s a real bug or regression.` 还要阅读 Dropped 列表。（怀疑式审问全分支，暂不改；只有真实缺陷/回归才报小问题。）；其中相关的字段或标识包括 `/interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's a real bug or regression.`。

- `/create-formal-verification-skill prove <property> holds in <module>, even when <steps> interleave or retry.` 该代码合并或重构后用 `/maintain-formal-verification-skill`。（证明性质在交错/重试下仍成立。）

- `/swarm check every package under <dir> against its check script. one worker per package. one report.`（逐个检查包，一个包一个工作者，一份报告。）

- `/poteto-mode open the pr. small ordered commits, evidence in the description.`（开 PR，小而有顺序提交，描述附证据。）

- `/poteto-mode babysit this pr. get it green.` 只看状态：`/poteto-mode check on pr <number>. anything outstanding?`（看护至绿色；或检查未完成项。）

- `/poteto-mode land the stack.`（落地整组堆叠。）

## 离开与返回

- `/poteto-mode im going to bed. <goal> in a fresh worktree off <base>. done means <checks>. keep a decision log. don’t ask me before committing. /loop until done. if you’re truly stuck after a few hours, stop and write up why.`（睡前自主执行，新工作树，记录决定，完成前不询问，持续至完成；真正卡住则停止并写明原因。）；其中相关的字段或标识包括 `/poteto-mode im going to bed. <goal> in a fresh worktree off <base>. done means <checks>. keep a decision log. don't ask me before committing. /loop until done. if you're truly stuck after a few hours, stop and write up why.`。

- `/show-me-your-work catch me up on what you did last night.` 先读 Attention 节。（补报昨夜工作。）

- `/ketchup` 补报自上次消息以来的聊天内容，并列出所有等待你的调用。

- `/poteto-mode full autopilot on this queue. each item is independent.`（队列全自动驾驶，每项独立。）

- `/poteto-mode autopilot these changes, but don’t merge. i’ll land them.`（自动执行改动但不合并，由我落地。）；其中相关的字段或标识包括 `/poteto-mode autopilot these changes, but don't merge. i'll land them.`。

- `/reflect capture what we learned so the next run doesn’t repeat it.` 只批准能改变未来决定的修改。（记录经验。）；其中相关的字段或标识包括 `/reflect capture what we learned so the next run doesn't repeat it.`。

- `/bro` 用平实语言重述上一条回复。
