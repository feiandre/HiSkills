## What it does

<!-- zh-CN:begin 8e84d6a8b30cb293 -->

## 作用

<!-- zh-CN:end 8e84d6a8b30cb293 -->

`tdd` builds a feature or fixes a bug test-first: one failing test, then just enough code to pass it, then the next behaviour. It carries the standards that make that loop produce tests worth keeping: what a good test is, where tests go, what mocks are for, and the three anti-patterns that make a suite worthless.

<!-- zh-CN:begin a3229b60a1a8c0cd -->

`tdd` 以测试优先方式构建功能或修复缺陷：先写一个失败测试，再写刚好足以通过它的代码，然后处理下一种行为。它承载使该循环产出值得保留测试的标准：何为好测试、测试放在哪里、mock 的用途，以及使测试套件毫无价值的三种反模式。

<!-- zh-CN:end a3229b60a1a8c0cd -->

It writes no test at a seam you have not agreed to first. Before any test exists, it names the public boundaries it intends to test at and stops for your confirmation. Testing effort is finite, and this step spends it on the critical paths instead of on every edge case. `tdd` is also a **reference**, not a driver. It contains the rules of the loop, and something else (you, or [implement](https://aihero.dev/skills-implement)) runs the [session](https://www.aihero.dev/ai-coding-dictionary/session) that applies them.

<!-- zh-CN:begin a63ede9833141f76 -->

它不会在你尚未同意的接缝编写测试。任何测试存在前，它会列出计划测试的公开边界并停下来等待你确认。测试精力有限，这一步会将它用在关键路径上，而非每个边界情况。`tdd` 还是**参考**，不是驱动器。它包含循环规则，由其他对象（你，或 [implement](https://aihero.dev/skills-implement)）运行应用这些规则的[会话](https://www.aihero.dev/ai-coding-dictionary/session)。

<!-- zh-CN:end a63ede9833141f76 -->

## When to reach for it

<!-- zh-CN:begin 75327918974f261d -->

## 何时使用

<!-- zh-CN:end 75327918974f261d -->

Type `/tdd`, or the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reaches for it automatically when a task fits: building a feature or fixing a bug test-first, or when you say "red-green-refactor".

<!-- zh-CN:begin 7e06ac2857886001 -->

键入 `/tdd`，或任务适合时由[代理](https://www.aihero.dev/ai-coding-dictionary/agent)自动使用：以测试优先构建功能或修复缺陷，或你说“red-green-refactor”时。

<!-- zh-CN:end 7e06ac2857886001 -->

Reach for it when there is a concrete behaviour to build, with an input and an observable output, and you want tests that survive a refactor.

<!-- zh-CN:begin b2124169f601ff01 -->

当有具体行为要构建、具有输入和可观察输出，并且你希望测试能经受重构时使用。

<!-- zh-CN:end b2124169f601ff01 -->

| Your situation | Where to go |
| --- | --- |
| A behaviour with defined inputs and outputs (business logic, a request/response contract, a transformation, validation) | `tdd` |
| The behaviour isn't pinned down yet | [to-spec](https://aihero.dev/skills-to-spec), which also agrees the test seams before any code is written |
| The question is really the shape of the interface, not the tests | [codebase-design](https://aihero.dev/skills-codebase-design) |
| You have a [spec](https://www.aihero.dev/ai-coding-dictionary/spec) or [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) and want the whole build run for you | [implement](https://aihero.dev/skills-implement), which drives `tdd` per ticket |
| Config, wiring, glue, type annotations, straight CRUD delegation | Nothing here fits well; see the open gap below |

<!-- zh-CN:begin 3a4249467f22f4e0 -->

| 你的情况 | 去处 |
| --- | --- |
| 具有明确输入和输出的行为（业务逻辑、请求/响应契约、转换、验证） | `tdd` |
| 行为尚未确定 | [to-spec](https://aihero.dev/skills-to-spec)，它也会在写任何代码前约定测试接缝 |
| 真正的问题在于接口形状，而非测试 | [codebase-design](https://aihero.dev/skills-codebase-design) |
| 你有[规范](https://www.aihero.dev/ai-coding-dictionary/spec)或[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)，并希望替你运行整个构建 | [implement](https://aihero.dev/skills-implement)，它按工单驱动 `tdd` |
| 配置、接线、胶合代码、类型注解、直通的 CRUD 委派 | 此处没有很合适的技能；参见下方未覆盖空白 |

<!-- zh-CN:end 3a4249467f22f4e0 -->

That last row is a real gap. The skill decides *where* the seams go, but nothing in it decides *whether* a change is worth the loop at all. If you run it on a change with no independent source of truth to assert against, you get a test that restates the implementation. That is the tautological anti-pattern the skill warns about, reached from the other direction. It is [issue #746](https://github.com/mattpocock/skills/issues/746), and it is open. Until it closes, you make that call yourself, or write the rule into your `CLAUDE.md`.

<!-- zh-CN:begin 71eb0b9b3c663480 -->

最后一行是真实空白。技能决定接缝*在哪里*，但没有内容决定一项改动*是否*值得运行循环。若在没有独立事实来源可断言的改动上运行它，得到的测试只是重述实现。这就是技能警告的同义反复反模式，只是从另一方向到达。对应[问题 #746](https://github.com/mattpocock/skills/issues/746)，目前未解决。解决前，由你自行判断，或把规则写入 `CLAUDE.md`。

<!-- zh-CN:end 71eb0b9b3c663480 -->

## Prerequisites

<!-- zh-CN:begin a09d956f1d440d83 -->

## 前置条件

<!-- zh-CN:end a09d956f1d440d83 -->

[codebase-design](https://aihero.dev/skills-codebase-design) needs to be installed. `tdd` used to carry its own deep-module and interface-design notes; v1.0 deleted them in favour of the shared skill, and `tdd` now uses its interface-design vocabulary. Nothing else; the skill is [stateless](https://www.aihero.dev/ai-coding-dictionary/stateless) and writes no files of its own.

<!-- zh-CN:begin b225b65180d916ee -->

需要安装 [codebase-design](https://aihero.dev/skills-codebase-design)。`tdd` 过去自带深模块和接口设计说明；v1.0 删除它们，改为共享技能，`tdd` 现在使用其接口设计词汇。除此之外无需其他条件；该技能是[无状态的](https://www.aihero.dev/ai-coding-dictionary/stateless)，不自行写文件。

<!-- zh-CN:end b225b65180d916ee -->

## The loop, and the seam it runs at

<!-- zh-CN:begin 87d4eccd0a040e73 -->

## 循环及其运行接缝

<!-- zh-CN:end 87d4eccd0a040e73 -->

The skill rests on three terms.

<!-- zh-CN:begin 3f93b87024e27d51 -->

该技能依赖三个术语。

<!-- zh-CN:end 3f93b87024e27d51 -->

**Red-green.** Write the failing test, then only enough code to pass it. Do not write code for the test after next. There is no refactor phase. The skill dropped it in June 2026 because agents almost never performed it, and because review and implementation work better as separate sessions. Refactoring belongs to [code-review](https://aihero.dev/skills-code-review).

<!-- zh-CN:begin bcc01c08520f763f -->

**红绿。**编写失败测试，然后只写足够通过它的代码。不要为下一项之后的测试写代码。没有重构阶段。技能在 2026 年 6 月删除该阶段，因为代理几乎从不执行，而且将审查与实现分成不同会话效果更好。重构属于 [code-review](https://aihero.dev/skills-code-review)。

<!-- zh-CN:end bcc01c08520f763f -->

**Vertical slice.** Write one test at one seam, then the minimal implementation, then repeat. The first cycle is a **tracer bullet** that proves a single path end to end. The opposite is horizontal slicing: all the tests first, then all the code. Tests written in bulk verify *imagined* behaviour. They check the shape of things rather than what a user does, and they commit you to a test structure before you understand the implementation.

<!-- zh-CN:begin 7cfc8c1d56671405 -->

**垂直切片。**在一个接缝写一个测试，再写最小实现，然后重复。第一个循环是**示踪弹**，端到端证明一条路径。相反做法是水平切片：先写所有测试，再写所有代码。批量编写的测试验证*想象中的*行为。它们检查事物形状而非用户实际行为，并在你理解实现前就锁定测试结构。

<!-- zh-CN:end 7cfc8c1d56671405 -->

**Pre-agreed seam.** A seam is the public boundary you observe behaviour at without reaching inside. The rule has no exceptions. No test goes at an unconfirmed seam. In the full chain the seams are agreed earlier, during [to-spec](https://aihero.dev/skills-to-spec): "`/tdd` is told to only work at pre-agreed test seams, `/code-review` checks that only agreed-upon test seams were used." Invoked on its own, `tdd` asks you directly.

<!-- zh-CN:begin f83570eec8121b37 -->

**预先约定的接缝。**接缝是无需深入内部即可观察行为的公开边界。该规则没有例外。未确认的接缝不编写测试。完整链路中，接缝在 [to-spec](https://aihero.dev/skills-to-spec) 期间提前约定：“`/tdd` 只能使用预先约定的测试接缝，`/code-review` 检查只使用了约定接缝。”单独调用时，`tdd` 直接询问你。

<!-- zh-CN:end f83570eec8121b37 -->

The three anti-patterns it is written to prevent:

<!-- zh-CN:begin f85ca2a360fa30b0 -->

它用于防止的三种反模式：

<!-- zh-CN:end f85ca2a360fa30b0 -->

| Anti-pattern | The tell |
| --- | --- |
| Implementation-coupled | The test breaks when you rename an internal function, though behaviour did not change. Mocked internal collaborators, asserted call counts, database queries used to verify instead of the interface. |
| Tautological | The expected value is computed the way the code computes it, so the test passes by construction. Expected values have to come from somewhere else: a known-good literal, a worked example, the spec. |
| Horizontal slicing | A batch of tests landed before any implementation. |

<!-- zh-CN:begin 3d72a394f2daf25e -->

| 反模式 | 识别迹象 |
| --- | --- |
| 与实现耦合 | 重命名内部函数时测试失败，尽管行为未变。mock 内部协作者、断言调用次数、用数据库查询而非接口验证。 |
| 同义反复 | 期望值按代码计算方式算出，所以测试从构造上就会通过。期望值必须来自别处：已知良好字面量、手算示例、规范。 |
| 水平切片 | 在任何实现前一次性提交一批测试。 |

<!-- zh-CN:end 3d72a394f2daf25e -->

Mocks are for system boundaries only: external APIs, time, randomness, sometimes the filesystem or the database. Never mock your own modules.

<!-- zh-CN:begin e2d22a7c71cccc11 -->

mock 仅用于系统边界：外部 API、时间、随机性，有时为文件系统或数据库。绝不 mock 自己的模块。

<!-- zh-CN:end e2d22a7c71cccc11 -->

## Common questions

<!-- zh-CN:begin 15600856740ad9ef -->

## 常见问题

<!-- zh-CN:end 15600856740ad9ef -->

**Why doesn't it refactor? The description says "red-green-refactor".**

<!-- zh-CN:begin 8dc5701675d4143c -->

**为什么它不重构？描述却说“red-green-refactor”。**

<!-- zh-CN:end 8dc5701675d4143c -->

Because the refactor step was removed and the description was not. The removal was deliberate. Agents almost never did the step, and keeping implementation and review in separate sessions works better. Whether the result still counts as TDD by the book matters less than whether the loop produces better code. The mismatch between the trigger phrase and the body is filed as [issue #589](https://github.com/mattpocock/skills/issues/589) and is still open, so "red-green-refactor" continues to work as a phrase that fires the skill. What you get is red-green, with refactoring in [code-review](https://aihero.dev/skills-code-review).

<!-- zh-CN:begin 7e115e4923367d9c -->

因为重构步骤被删除，描述却没改。删除是有意的。代理几乎从不执行该步骤，而将实现与审查放在不同会话效果更好。结果是否仍按书本算作 TDD，不如循环是否产出更好代码重要。触发短语和正文之间的不一致记录为[问题 #589](https://github.com/mattpocock/skills/issues/589)，目前仍未解决，所以“red-green-refactor”仍可作为触发技能的短语。你得到的是红绿，重构在 [code-review](https://aihero.dev/skills-code-review) 中进行。

<!-- zh-CN:end 7e115e4923367d9c -->

**It asked me to choose a test seam and I had no idea which to pick.**

<!-- zh-CN:begin 6c6512bbe766d4e2 -->

**它要求我选择测试接缝，但我不知道选哪个。**

<!-- zh-CN:end 6c6512bbe766d4e2 -->

This is the most-reported friction with the skill ([issue #607](https://github.com/mattpocock/skills/issues/607)). The prompt lists candidate seams by name only, with nothing about what each one catches or misses, so you are choosing between labels. There is no fix shipped yet. The practical workaround is to ask the agent for the trade-offs before answering: what does the component-level seam miss that the integration seam catches, and how much slower is it. It is also why the chain agrees seams up front in `to-spec`, where you have the whole feature in view rather than one prompt.

<!-- zh-CN:begin 5486187c8b48b370 -->

这是关于该技能报告最多的摩擦（[问题 #607](https://github.com/mattpocock/skills/issues/607)）。提示只按名称列出候选接缝，没有说明各自能捕获或遗漏什么，所以你只能在标签间选择。目前没有修复。实际变通方法是在回答前请代理说明权衡：组件级接缝遗漏了什么而集成接缝能捕获，以及会慢多少。这也说明链路为何在 `to-spec` 中提前约定接缝：那时你能看到整个功能，而非单个提示。

<!-- zh-CN:end 5486187c8b48b370 -->

**It wrote the implementation before the test, even though the skill says red first.**

<!-- zh-CN:begin 9a2e99d7524e8df3 -->

**它先写了实现再写测试，尽管技能说先红。**

<!-- zh-CN:end 9a2e99d7524e8df3 -->

It happens. One user pushed the [model](https://www.aihero.dev/ai-coding-dictionary/model) on it and got an unusually honest answer: "I knew the skill said 'one test at a time, watch it fail for the right reason'. I read it. I just defaulted to my normal habit." The skill accepts this. No instruction makes an agent comply 100% of the time, and stricter wording restricts the agent's creativity for little gain. The loop is worth running even when the agent does not follow it strictly, because the results are still better overall. If strict adherence matters for a particular slice, watch the run rather than trusting the skill to enforce it.

<!-- zh-CN:begin 0b3d7ff5fc4bd4bb -->

确实会发生。一位用户追问[模型](https://www.aihero.dev/ai-coding-dictionary/model)，得到少见的诚实回答：“我知道技能说‘一次一个测试，观察它因正确原因失败’。我读过。我只是默认回了日常习惯。”技能接受这一点。没有任何指令能让代理 100% 遵循，更严格的措辞只会限制代理创造力而收益很小。即使代理不严格遵循，运行循环仍值得，因为整体结果仍更好。若某一切片必须严格遵循，请观察运行，不要指望技能强制执行。

<!-- zh-CN:end 0b3d7ff5fc4bd4bb -->

**Should it write browser or end-to-end tests first?**

<!-- zh-CN:begin 9f0780caef75840e -->

**应先写浏览器或端到端测试吗？**

<!-- zh-CN:end 9f0780caef75840e -->

Usually not, and the skill will not stop it. A user reported the agent writing a Playwright test first, then spending a long loop re-running it and concluding the *test* was broken for a feature that did not exist yet. Browser tests are slow enough that the red-green feedback loop stops paying for itself. State in your repo's `CLAUDE.md` that browser tests come after the behaviour works.

<!-- zh-CN:begin 23b4dfe62aa05ccf -->

通常不应，而且技能不会阻止。有用户报告代理先写 Playwright 测试，然后长时间反复运行，最后断定*测试*损坏，而功能尚不存在。浏览器测试足够慢，红绿反馈循环不再划算。在仓库的 `CLAUDE.md` 中说明浏览器测试应在行为可用之后进行。

<!-- zh-CN:end 23b4dfe62aa05ccf -->

**Does `/tdd` replace `/implement`, or the course's `/do-work`?**

<!-- zh-CN:begin c6dedecd4878eed3 -->

**`/tdd` 会替代 `/implement` 或课程中的 `/do-work` 吗？**

<!-- zh-CN:end c6dedecd4878eed3 -->

No. `/tdd` documents the methodology; `/implement` is a simple work→feedback→commit loop and is the direct stand-in for `/do-work`. The course's single `/do-work` step is now split across `/implement`, `/tdd` and `/code-review`. If you are asking which one to run against a ticket, the answer is almost always `/implement`.

<!-- zh-CN:begin 7afe7ca8cc88e2c8 -->

不会。`/tdd` 记录方法论；`/implement` 是简单的“工作→反馈→提交”循环，直接替代 `/do-work`。课程中单一的 `/do-work` 步骤现已拆分为 `/implement`、`/tdd` 和 `/code-review`。若问针对工单该运行哪一个，答案几乎总是 `/implement`。

<!-- zh-CN:end 7afe7ca8cc88e2c8 -->

**Where did the deep-modules and interface-design guidance go?**

<!-- zh-CN:begin 1201079172b5b810 -->

**深模块和接口设计指导去哪了？**

<!-- zh-CN:end 1201079172b5b810 -->

Into [codebase-design](https://aihero.dev/skills-codebase-design) in v1.0, generalised so several skills share one vocabulary. `refactoring.md` left at the same time; refactoring is now [code-review](https://aihero.dev/skills-code-review)'s job, and that skill carries the Fowler smell baseline.

<!-- zh-CN:begin 902ea793bd45c8bf -->

在 v1.0 并入 [codebase-design](https://aihero.dev/skills-codebase-design)，经泛化让多个技能共享一套词汇。`refactoring.md` 同时移出；重构现在由 [code-review](https://aihero.dev/skills-code-review) 负责，该技能带有 Fowler 坏味道基线。

<!-- zh-CN:end 902ea793bd45c8bf -->

**Does it know about my other tickets?**

<!-- zh-CN:begin 20cb7979e7f05382 -->

**它知道我的其他工单吗？**

<!-- zh-CN:end 20cb7979e7f05382 -->

No. Run against one ticket, it can propose work that belongs to a sibling ticket, because it has no view of the rest of the issue graph ([issue #129](https://github.com/mattpocock/skills/issues/129)). This is not `tdd`'s job. Passing the spec alongside the ticket helps; right-sizing the tickets in the first place helps more.

<!-- zh-CN:begin 118f8259412d97e5 -->

不知道。针对一个工单运行时，它可能提出属于相邻工单的工作，因为它看不到 issue 图其余部分（[问题 #129](https://github.com/mattpocock/skills/issues/129)）。这不是 `tdd` 的职责。连同工单一起提供规范会有帮助；一开始合理确定工单大小帮助更大。

<!-- zh-CN:end 118f8259412d97e5 -->

## It's working if

<!-- zh-CN:begin f69cd3ccd5550bbe -->

## 怎样算有效

<!-- zh-CN:end f69cd3ccd5550bbe -->

- It stops and names the seams it intends to test at, and waits, before any test file exists.

<!-- zh-CN:begin 71df44d760992b08 -->

- 任何测试文件存在前，它会停下并列出计划测试的接缝，然后等待。

<!-- zh-CN:end 71df44d760992b08 -->
- One test appears, goes red, gets just enough code to pass, and only then does the next test appear, not a batch of tests followed by a batch of code.

<!-- zh-CN:begin 1df32defd43151ad -->

- 一次只出现一个测试，它变红，获得刚好足够的代码通过，然后才出现下一个测试；不是一批测试后接一批代码。

<!-- zh-CN:end 1df32defd43151ad -->
- Test names read as capabilities ("user can checkout with valid cart"), not as internals ("checkout calls paymentService.process").

<!-- zh-CN:begin e0c2b752ad450422 -->

- 测试名称读起来是能力（“用户可用有效购物车结账”），而非内部实现（“结账调用 paymentService.process”）。

<!-- zh-CN:end e0c2b752ad450422 -->
- Expected values in assertions are literals you can trace to the spec, not values recomputed the way the code computes them.

<!-- zh-CN:begin 625ea4923f929af5 -->

- 断言中的期望值是可追溯到规范的字面量，不是按代码方式重新计算的值。

<!-- zh-CN:end 625ea4923f929af5 -->
- Renaming an internal function breaks nothing in the suite.

<!-- zh-CN:begin a7a734df5917b5f2 -->

- 重命名内部函数不会破坏测试套件中的任何内容。

<!-- zh-CN:end a7a734df5917b5f2 -->
- Mocks appear only at external boundaries (the payment API, the clock) and never around your own modules.

<!-- zh-CN:begin 7b4905e55b9438c9 -->

- mock 只出现在外部边界（支付 API、时钟），绝不围绕自己的模块。

<!-- zh-CN:end 7b4905e55b9438c9 -->

## Where it fits

<!-- zh-CN:begin db248cd686379abd -->

## 所处位置

<!-- zh-CN:end db248cd686379abd -->

`tdd` runs inside the build step of the main chain; it is not a step of its own:

<!-- zh-CN:begin 7858ee4166c7e798 -->

`tdd` 在主要链路的构建步骤内运行；它不是单独的一步：

<!-- zh-CN:end 7858ee4166c7e798 -->

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

[to-spec](https://aihero.dev/skills-to-spec) agrees the test seams up front, [implement](https://aihero.dev/skills-implement) drives `tdd` per ticket, and [code-review](https://aihero.dev/skills-code-review) checks afterwards that only the agreed seams were used, and owns the refactoring `tdd` no longer does. Its other neighbour is [codebase-design](https://aihero.dev/skills-codebase-design), the shared source of the seam and deep-module vocabulary that `tdd` uses. You can also reach for it on its own, whenever there is a concrete behaviour to build and no full spec in play. When you are unsure which skill fits your situation, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 2a3b1ad63b28eb58 -->

[to-spec](https://aihero.dev/skills-to-spec) 提前约定测试接缝，[implement](https://aihero.dev/skills-implement) 按工单驱动 `tdd`，[code-review](https://aihero.dev/skills-code-review) 事后检查只使用了约定接缝，并负责 `tdd` 不再做的重构。另一个相邻技能是 [codebase-design](https://aihero.dev/skills-codebase-design)，即 `tdd` 使用的接缝与深模块词汇的共享来源。只要存在具体行为要构建且没有完整规范，也可独立使用。若不确定哪项技能适合你的情况，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你路由。

<!-- zh-CN:end 2a3b1ad63b28eb58 -->
