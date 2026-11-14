# Recipes and pitfalls

<!-- zh-CN:begin b94dd84f3d645986 -->

# 配方与陷阱

<!-- zh-CN:end b94dd84f3d645986 -->

Prompts worth copying, then the mistakes everyone makes once. Swap in your own paths and finish conditions. The recipes are deliberately informal. That's how they get typed in practice, and the skills read intent fine.

<!-- zh-CN:begin d54bc9eb9c2540ca -->

可复制提示，以及每个人都会犯一次的错。替换路径和完成条件。配方刻意非正式，实际输入就是这样，技能能理解意图。

<!-- zh-CN:end d54bc9eb9c2540ca -->

![She tastes a finished dish while robots cook from a recipe box, with pinned cards reading /how, /tdd, and /loop above the counter.](./images/recipes.jpg)

<!-- zh-CN:begin f71553c13ca64676 -->

![机器人按配方盒烹饪时，她品尝成品；柜台上方钉着写着 /how、/tdd、/loop 的卡片。](./images/recipes.jpg)

<!-- zh-CN:end f71553c13ca64676 -->

## Understand an unfamiliar subsystem

<!-- zh-CN:begin 2b7985756881e966 -->

## 理解陌生子系统

<!-- zh-CN:end 2b7985756881e966 -->

```text
use /how first to understand how this initialization works. then use /why to figure out why it broke recently.
```

<!-- zh-CN:begin 7c26821090a010b5 -->

```text
先用 /how 理解此初始化如何工作，再用 /why 查为什么近期坏掉。
```

<!-- zh-CN:end 7c26821090a010b5 -->

Mechanics first, history second. Each skill's report tells you which sources it searched, so you know what the answer is grounded in.

<!-- zh-CN:begin 587dfd3ab11c4d56 -->

先机制，后历史。每份报告列出搜索来源，可判断结论依据。

<!-- zh-CN:end 587dfd3ab11c4d56 -->

## Restate a noisy report before touching code

<!-- zh-CN:begin 858249c57d8591fd -->

## 碰代码前先复述嘈杂报告

<!-- zh-CN:end 858249c57d8591fd -->

```text
/poteto-mode read this thread. restate the underlying issue in your own words, in plain english. don't change any code yet.
```

<!-- zh-CN:begin 86bbc66781a23720 -->

```text
/poteto-mode 阅读此线程，用平实中文复述底层问题。暂不改任何代码。
```

<!-- zh-CN:end 86bbc66781a23720 -->

A misreading shows up in the restatement, where it costs one message to correct. Keep your own theory to yourself until the agent has stated its own. `/in-your-own-words` asks for the restatement alone, with no playbook.

<!-- zh-CN:begin 2b76a28e20bc3ad2 -->

误读会在复述里出现，修成本仅一条消息。代理说出自己的理解前，先保留你的原因理论。`/in-your-own-words` 只复述，不走手册。

<!-- zh-CN:end 2b76a28e20bc3ad2 -->

## Sharpen a prompt before you send it

<!-- zh-CN:begin f2d34c555496f9d4 -->

## 发送前打磨提示

<!-- zh-CN:end f2d34c555496f9d4 -->

```text
/sharpen write the onboarding doc for the new billing service.
```

<!-- zh-CN:begin 69ec2d24b78da169 -->

```text
/sharpen 为新计费服务写入门文档。
```

<!-- zh-CN:end 69ec2d24b78da169 -->

The agent names what an expert would do that you didn't ask for, the raw material they'd start from, their methods and tools, and an outside check that the result is right. It hands back your prompt rewritten to ask for that and doesn't do the task. Send the rewrite when it reads right.

<!-- zh-CN:begin 8a49fb83eea35e85 -->

代理说明专家会做而你没要求的内容、原始材料、方法工具、外部正确性检查，再重写提示而不执行任务。合适后发送。

<!-- zh-CN:end 8a49fb83eea35e85 -->

## Prototype before you pick

<!-- zh-CN:begin afc88ddc37d06568 -->

## 选择前先做原型

<!-- zh-CN:end afc88ddc37d06568 -->

```text
/poteto-mode prototype a few options for the settings layout. put them behind a switcher and send me screenshots of each.
```

<!-- zh-CN:begin dc97de0b25f02926 -->

```text
/poteto-mode 为设置布局做几个原型，用切换器展示并截图。
```

<!-- zh-CN:end dc97de0b25f02926 -->

You pick from things that run, not from descriptions. The agent answers its own layout and timing questions along the way.

<!-- zh-CN:begin 31df34bcdb569264 -->

从可运行方案而非描述中选，代理沿途解决布局和时序问题。

<!-- zh-CN:end 31df34bcdb569264 -->

## Turn a settled design into a plan

<!-- zh-CN:begin d7b8404f7d67ff4d -->

## 把确定设计转成计划

<!-- zh-CN:end d7b8404f7d67ff4d -->

```text
/poteto-mode turn this design into a plan. small verifiable PRs, each with its own proof.
```

<!-- zh-CN:begin b6753c698d86b7e1 -->

```text
/poteto-mode 把此设计转成计划。小型可验证 PR，每个带独立证据。
```

<!-- zh-CN:end b6753c698d86b7e1 -->

Ask only after the design settles. The plan is the deliverable, and it names the playbook that will execute it.

<!-- zh-CN:begin e3e04095a418ba8a -->

设计确定后再问。计划是交付物，并指明执行手册。

<!-- zh-CN:end e3e04095a418ba8a -->

## Get a second opinion on a design

<!-- zh-CN:begin db18e0fec19fea94 -->

## 为设计获得第二意见

<!-- zh-CN:end db18e0fec19fea94 -->

```text
ask /arena for a second opinion on this thread and our approach
```

<!-- zh-CN:begin db99deea9af8743a -->

```text
请 /arena 对此线程和方法给第二意见
```

<!-- zh-CN:end db99deea9af8743a -->

Your current design becomes one candidate among several, and the synthesis tells you whether the panel found something better or confirmed what you had. It costs little next to a design that is expensive to reverse.

<!-- zh-CN:begin 0bafb56ac82cf27f -->

当前设计成为多个候选之一，综合告诉你面板找到更好方案还是确认原方案。相比难逆设计，成本很低。

<!-- zh-CN:end 0bafb56ac82cf27f -->

## Check independent slices in parallel

<!-- zh-CN:begin a474529f7aa36d49 -->

## 并行检查独立切片

<!-- zh-CN:end a474529f7aa36d49 -->

```text
/swarm check every package under packages/ against its check.sh. one worker per package. one report.
```

<!-- zh-CN:begin 2acbe6667ab49eea -->

```text
/swarm 用各包 check.sh 检查 packages/ 下每个包。每包一个工作者，一份报告。
```

<!-- zh-CN:end 2acbe6667ab49eea -->

Each worker owns one package. The parent waits for every slice and returns one `PASS`, `ISSUES`, or `BLOCKED` report instead of raw worker dumps.

<!-- zh-CN:begin c70ce7ec9e7cb18c -->

每个工作者一个包。父级等待全部并返回一条 `PASS`、`ISSUES` 或 `BLOCKED`，不是原始倾倒。

<!-- zh-CN:end c70ce7ec9e7cb18c -->

## Review a branch skeptically

<!-- zh-CN:begin 4a72ac9cf335ac81 -->

## 怀疑式审查分支

<!-- zh-CN:end 4a72ac9cf335ac81 -->

```text
/interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's an actual bug or regression in behavior.
```

<!-- zh-CN:begin d6e25624ff234da2 -->

```text
/interrogate 怀疑式审问整个分支。暂不改。除非真实缺陷或行为回归，不报小问题。
```

<!-- zh-CN:end d6e25624ff234da2 -->

The qualifiers do real work. "don't change anything yet" keeps it read-only, and the nitpick rule pre-filters the noise so the verified findings are worth your time.

<!-- zh-CN:begin e388a50d760815fd -->

限定词有实际作用：“暂不改”保持只读，忽略小问题过滤噪声。

<!-- zh-CN:end e388a50d760815fd -->

## Fix a bug through a failing test

<!-- zh-CN:begin 40a7484a35566e32 -->

## 通过失败测试修缺陷

<!-- zh-CN:end 40a7484a35566e32 -->

```text
/poteto-mode repro the duplicate write first. if there's a cheap test path, /tdd it. then fix and rerun.
```

<!-- zh-CN:begin f38050b2c6dcf7bb -->

```text
/poteto-mode 先复现重复写入。若有低成本测试路径就 /tdd，然后修复重跑。
```

<!-- zh-CN:end f38050b2c6dcf7bb -->

"if there's a cheap test path" matters. Forcing a test through brittle mocks proves less than running the real command, and the playbook is allowed to say so.

<!-- zh-CN:begin 28501922ee3819b3 -->

“低成本测试路径”重要；脆弱模拟不如真实命令。手册允许说明这一点。

<!-- zh-CN:end 28501922ee3819b3 -->

## Repro and fix a report with proof

<!-- zh-CN:begin 7752a65058031102 -->

## 带证据复现与修复报告

<!-- zh-CN:end 7752a65058031102 -->

```text
/poteto-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.
```

<!-- zh-CN:begin efd4b888ef972e80 -->

```text
/poteto-mode 用 /verify-<app> 复现。若 main 也复现则修复并提供视频证据。
```

<!-- zh-CN:end efd4b888ef972e80 -->

"if it repros on main" lets the run stop early when the bug is already gone. The video lets you check the fix before you read the diff.

<!-- zh-CN:begin ead6bad224961800 -->

“若 main 也复现”允许缺陷已消失时提前停止；视频便于读差异前检查。

<!-- zh-CN:end ead6bad224961800 -->

## Prove a property tests rarely reach

<!-- zh-CN:begin c2f85e8ed94862a1 -->

## 证明测试难覆盖的性质

<!-- zh-CN:end c2f85e8ed94862a1 -->

```text
/create-formal-verification-skill the retry queue. a message must never be delivered twice.
```

<!-- zh-CN:begin 460349106a88c188 -->

```text
/create-formal-verification-skill 重试队列。消息绝不能投递两次。
```

<!-- zh-CN:end 460349106a88c188 -->

You get one property checked in every case within a stated scope, a counterexample in your code's terms if the code already breaks it, and a project skill the next agent runs on any change to that code.

<!-- zh-CN:begin cb8f5f32d0271528 -->

在指定范围每个情形验证一性质；已违反时给出代码语义反例；生成后续代理在代码变更时运行的技能。

<!-- zh-CN:end cb8f5f32d0271528 -->

## Vet a number before you post it

<!-- zh-CN:begin ea16988528afcb70 -->

## 发布数字前核验

<!-- zh-CN:end ea16988528afcb70 -->

```text
/benchmark-checklist vet this 40% speedup before it goes in the pr description
```

<!-- zh-CN:begin 74b4d8f5c555bdd0 -->

```text
/benchmark-checklist 在写入 PR 描述前核验 40% 提速
```

<!-- zh-CN:end 74b4d8f5c555bdd0 -->

You get faster, slower, no measurable difference, or inconclusive, with the run count, the range, and what limits the number.

<!-- zh-CN:begin 2ee860816cc0e6f8 -->

得到更快、更慢、无显著差异或不确定，附运行次数、范围与限制。

<!-- zh-CN:end 2ee860816cc0e6f8 -->

## Stop correcting the same mistake

<!-- zh-CN:begin abc2a4f06aa7930e -->

## 停止重复纠正同一错误

<!-- zh-CN:end abc2a4f06aa7930e -->

```text
/correct agents keep adding new config flags without registering them in the schema
```

<!-- zh-CN:begin a44235d35315f124 -->

```text
/correct agents 常添加配置标志却未注册到 schema
```

<!-- zh-CN:end a44235d35315f124 -->

The fix lands in the repo as architecture, a type, a lint, or a test, so the next agent can't make the mistake.

<!-- zh-CN:begin 075879e83e197a63 -->

修复落在仓库架构、类型、lint 或测试中，后续代理无法再犯。

<!-- zh-CN:end 075879e83e197a63 -->

## Ask how without starting the work

<!-- zh-CN:begin a11f847ec74b15fa -->

## 只问怎么做而不启动工作

<!-- zh-CN:end a11f847ec74b15fa -->

```text
/poteto-help how do i get poteto-mode to stay on every turn?
```

<!-- zh-CN:begin 56a1ecefdf05b4a4 -->

```text
/poteto-help 怎么让 poteto-mode 每轮保持启用？
```

<!-- zh-CN:end 56a1ecefdf05b4a4 -->

You get an answer, a prompt to send, and a link to the source. Nothing runs until you send that prompt.

<!-- zh-CN:begin 9ae62d762df86387 -->

得到答案、可发送提示和来源链接；发送前不运行。

<!-- zh-CN:end 9ae62d762df86387 -->

## Keep a run honest while you're away

<!-- zh-CN:begin 67c7697ace9db3b6 -->

## 离开时保持运行诚实

<!-- zh-CN:end 67c7697ace9db3b6 -->

```text
im going to bed, keep going autonomously until every fixture passes. do not stop. keep a decision log i can audit in the morning.
```

<!-- zh-CN:begin ba5b633bb8564e91 -->

```text
我去睡觉，自主做到所有夹具通过。不要停。保留早晨可审计的决定日志。
```

<!-- zh-CN:end ba5b633bb8564e91 -->

The full contract is on the [overnight page](./07-overnight.md). The short form works once the task and finish condition are already in the conversation.

<!-- zh-CN:begin 0a90c2f9e429beb8 -->

完整契约见[通宵页](./07-overnight.md)；任务和完成条件已在对话时可用短句。

<!-- zh-CN:end 0a90c2f9e429beb8 -->

## Redirect a drifting run

<!-- zh-CN:begin 7ea9702f16b71a67 -->

## 重定向漂移运行

<!-- zh-CN:end 7ea9702f16b71a67 -->

Steering prompts are one line:

<!-- zh-CN:begin 0cb6cee2ba10a63e -->

指导提示只需一行：

<!-- zh-CN:end 0cb6cee2ba10a63e -->

```text
i said the goal is to repro. i did not ask for a fix yet.
```

<!-- zh-CN:begin f1faa8424026147d -->

```text
我说目标是复现，还没要求修复。
```

<!-- zh-CN:end f1faa8424026147d -->

```text
apply prove it works. show me the real output, not the build log.
```

<!-- zh-CN:begin 9c8a35e0a82439b6 -->

```text
应用“证明它有效”。给我真实输出，不要构建日志。
```

<!-- zh-CN:end 9c8a35e0a82439b6 -->

```text
/unslop that, no emdashes
```

<!-- zh-CN:begin c5c5381084c8a3e7 -->

```text
/unslop 把它改写清楚，不用长破折号
```

<!-- zh-CN:end c5c5381084c8a3e7 -->

You rarely need more words. You need the right name, and [the principles page](./08-principles.md) is the vocabulary.

<!-- zh-CN:begin 5b68c6e9a3c248d2 -->

很少需要更多字，需要正确名称；[原则页](./08-principles.md)是词汇表。

<!-- zh-CN:end 5b68c6e9a3c248d2 -->

## Get the reply in plain words

<!-- zh-CN:begin eb9c8721a3650820 -->

## 用平实语言重述回复

<!-- zh-CN:end eb9c8721a3650820 -->

```text
/bro
```

<!-- zh-CN:begin c47dc731d4296630 -->

```text
/bro
# 用平实语言重述上一条回复
```

<!-- zh-CN:end c47dc731d4296630 -->

That's the whole prompt. [`/bro`](../../skills/bro/SKILL.md) restates the last message like one human talking to another, no jargon, shorter. Use it when a reply is technically thorough and you still don't know what it said.

<!-- zh-CN:begin 8572585992ff39ff -->

这就是完整提示。[`/bro`](../../skills/bro/SKILL.md) 把上一条像人对人一样用更短、无术语语言重述。适合技术详尽却仍看不懂时。

<!-- zh-CN:end 8572585992ff39ff -->

## Catch up on a chat you left running

<!-- zh-CN:begin dedc78d5ea44fed7 -->

## 补齐离开期间聊天

<!-- zh-CN:end dedc78d5ea44fed7 -->

```text
/ketchup
```

<!-- zh-CN:begin 0494a4c090124de6 -->

```text
/ketchup
# 补齐离开期间的聊天
```

<!-- zh-CN:end 0494a4c090124de6 -->

[`/ketchup`](../../skills/ketchup/SKILL.md) tells you in plain words what changed since your last message, then lists each call waiting on you with its pick, evidence, and risk. It changes nothing while it reports.

<!-- zh-CN:begin efbc077b77a5cf68 -->

[`/ketchup`](../../skills/ketchup/SKILL.md) 说明自上次消息变化，并列出每个等待你的调用及选择、证据、风险；报告期间不改变。

<!-- zh-CN:end efbc077b77a5cf68 -->

To watch the catch-up instead, run [`/ketchup-video`](../../skills/ketchup-video/SKILL.md). It shows what happened in a short subtitled video of slides, and lists the calls waiting on you as text under it.

<!-- zh-CN:begin a16f4d2e9fd649c0 -->

若要看视频补报，运行 [`/ketchup-video`](../../skills/ketchup-video/SKILL.md)，用字幕幻灯片展示并由文字列出等待调用。

<!-- zh-CN:end a16f4d2e9fd649c0 -->

## The pitfalls

<!-- zh-CN:begin be1a75cb6df71e5f -->

## 陷阱

<!-- zh-CN:end be1a75cb6df71e5f -->

- **Enumerating skills in the prompt.** "use /how then /architect then /arena" reorders steps the playbook already sequences. State the goal and constraints. Name a skill only to override a default.

<!-- zh-CN:begin ba6d8173f7de1a4b -->

- **在提示中枚举技能。** “先用 /how 再 /architect 再 /arena”会打乱手册顺序。说目标和约束；只有覆盖默认才点名。

<!-- zh-CN:end ba6d8173f7de1a4b -->
- **A vague finish condition.** "make it better" gives `/loop` nothing to check. Give a command or artifact that can pass or fail.

<!-- zh-CN:begin 0d9e1abc724ea0e4 -->

- **完成条件含糊。** “做得更好”让 `/loop` 无检查。给可通过或失败的命令/产物。

<!-- zh-CN:end 0d9e1abc724ea0e4 -->
- **Leading with your theory of the cause.** The agent searches wherever you pointed. Ask it to restate the problem first, then share your hunch.

<!-- zh-CN:begin 95e81227c159a7a0 -->

- **先讲原因理论。** 代理只追随你的方向。让它先复述问题，再分享直觉。

<!-- zh-CN:end 95e81227c159a7a0 -->
- **Taking the first design.** One attempt locks in the first shape the model thought of. Ask for prototypes or `/architect` and pick from evidence.

<!-- zh-CN:begin ba8e27f74403563b -->

- **接受第一个设计。** 一次尝试锁定模型首个形状。要求原型或 `/architect`，据证据选择。

<!-- zh-CN:end ba8e27f74403563b -->
- **Polishing an abstract plan.** Adversarial review of a plan with no code behind it invents risks that will never happen. Settle the open questions with prototypes, then review what got built.

<!-- zh-CN:begin cc58759c80347087 -->

- **打磨抽象计划。** 无代码计划对抗审查会发明不存在的风险。先用原型解决疑问，再审查真实产物。

<!-- zh-CN:end cc58759c80347087 -->
- **Parallel agents in one worktree.** They overwrite each other, and nobody can tell which agent changed what. Run them as cloud agents, or say "own worktree per attempt".

<!-- zh-CN:begin b6a11c5d296ace72 -->

- **一个工作树并行代理。** 互相覆盖且无法归因。用云代理，或要求每次尝试独立工作树。

<!-- zh-CN:end b6a11c5d296ace72 -->
- **Looping before you trust the loop.** A loop that can't verify its own work only makes unchecked work faster. Get the verification skill working first.

<!-- zh-CN:begin 807d9ca2a37ae915 -->

- **信任循环前就循环。** 不能自验的循环只会更快产生未检查工作。先让验证技能工作。

<!-- zh-CN:end 807d9ca2a37ae915 -->
- **Trusting an unvetted number.** A warm cache or a skipped code path can fake a speedup. Run `/benchmark-checklist` before the number goes anywhere.

<!-- zh-CN:begin bbd4a02a76ca616d -->

- **信任未核验数字。** 热缓存或跳过路径可伪造提速。发布前运行 `/benchmark-checklist`。

<!-- zh-CN:end bbd4a02a76ca616d -->
- **Correcting the same mistake by hand.** A correction in chat helps one run. `/correct` fixes the repo so no later run repeats it.

<!-- zh-CN:begin 91be350aa2fc9929 -->

- **手工反复纠正。** 聊天纠正只帮一次；`/correct` 修仓库防后续重犯。

<!-- zh-CN:end 91be350aa2fc9929 -->
- **Using `/arena` for coverage.** `/arena` repeats one design or code brief, then picks a base and grafts the best parts. `/swarm` partitions slices or declared race arms and aggregates one report.

<!-- zh-CN:begin 9ecd2b7f0fd35210 -->

- **用 `/arena` 做覆盖。** `/arena` 重复一个设计/代码简报后选基合并；`/swarm` 分片或竞速并汇总。

<!-- zh-CN:end 9ecd2b7f0fd35210 -->
- **Accepting every review comment.** Bots and humans both file real catches and noise in one list. `/interrogate` keeps only the findings a rerun proves and lists what it dropped and why, and you can override either way.

<!-- zh-CN:begin e1e9f9fa7e9313c5 -->

- **接受每条审查评论。** 机器人和人都会混入噪声；`/interrogate` 仅保留重跑可证明项并列出丢弃理由，你可覆盖。

<!-- zh-CN:end e1e9f9fa7e9313c5 -->
- **Treating `auto` as a model slug.** `auto` and `inherit-parent` mean "omit the model field so the subagent inherits the parent chat model." [Setup](./01-setup.md) covers the roles.

<!-- zh-CN:begin a7470da85b3a0573 -->

- **把 `auto` 当模型 slug。** `auto` 和 `inherit-parent` 都表示省略模型字段并继承父会话；[设置](./01-setup.md)说明角色。

<!-- zh-CN:end a7470da85b3a0573 -->
- **Reporting success off a green build.** A build proves it compiles. Ask for the real command, flow, stored value, or profile, and expect the evidence in the reply.

<!-- zh-CN:begin d28f93781c724420 -->

- **构建绿色就报成功。** 构建只证明编译。要求真实命令、流程、保存值或性能证据。

<!-- zh-CN:end d28f93781c724420 -->
- **Writing a `SKILL.md` freehand.** Route it through the [Authoring or modifying a skill playbook](../../skills/poteto-mode/playbooks/authoring-a-skill.md) so validation and review happen.

<!-- zh-CN:begin 4a073740ddaf5c3c -->

- **手写 `SKILL.md`。** 走[技能编写手册](../../skills/poteto-mode/playbooks/authoring-a-skill.md)以执行验证审查。

<!-- zh-CN:end 4a073740ddaf5c3c -->

That's the guide. If you skipped ahead, go back to [setup](./01-setup.md) and run one real task. The habits stick from use, not from reading.

<!-- zh-CN:begin c0acccb6d14ded43 -->

指南结束。若跳读，请回[设置](./01-setup.md)跑一个真实任务；习惯靠使用形成。

<!-- zh-CN:end c0acccb6d14ded43 -->

Back to the [guide index](./README.md).

<!-- zh-CN:begin 6ea93be0b868bf0e -->

返回[指南索引](./README.md)。

<!-- zh-CN:end 6ea93be0b868bf0e -->
