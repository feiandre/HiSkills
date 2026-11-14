# Steer with principle names

<!-- zh-CN:begin 5977d8c5b49bd8fe -->

# 用原则名称来引导

<!-- zh-CN:end 5977d8c5b49bd8fe -->

pstack ships 24 principles as individual skills. `/poteto-mode` reads their index at the start of every multi-step task, applies the ones the task triggers, and names each applied principle in its reply along with the decision it changed.

<!-- zh-CN:begin ab1cdc350cc921aa -->

pstack 以独立技能形式提供 24 条原则。`/poteto-mode` 在每个多步骤任务开始时读取索引，应用任务触发的原则，并在回复中说明每条原则改变了什么决策。

<!-- zh-CN:end ab1cdc350cc921aa -->

You don't invoke principles. You use their names to steer. Each name points at a complete rule the agent has already read, so one phrase redirects the work more precisely than a paragraph of instructions.

<!-- zh-CN:begin 8720e47ef6030cce -->

原则不需要调用，而是用名称来引导。每个名称指向智能体已读过的完整规则，因此一个短语比一整段指令更能精确改变工作方向。

<!-- zh-CN:end 8720e47ef6030cce -->

## Steering in practice

<!-- zh-CN:begin 9c4edd46ed5d4eb9 -->

## 实践中的引导

<!-- zh-CN:end 9c4edd46ed5d4eb9 -->

Say the agent is about to bolt a new adapter onto three existing ones:

<!-- zh-CN:begin 9250274f8d0b23ee -->

智能体要在三个现有适配器上加第四个时：

<!-- zh-CN:end 9250274f8d0b23ee -->

```text
use subtract before you add. delete the obsolete adapters first, then design what's left.
```

<!-- zh-CN:begin 9a066e511cbbfa66 -->

```text
先做减法再加。先删除过时适配器，再设计剩余部分。
```

<!-- zh-CN:end 9a066e511cbbfa66 -->

Say it claims success because the build passed:

<!-- zh-CN:begin 3612b3e865ec6524 -->

它因构建通过而宣称成功时：

<!-- zh-CN:end 3612b3e865ec6524 -->

```text
apply prove it works. run the real import flow and show me the written records.
```

<!-- zh-CN:begin 5f9844ed75b9a99b -->

```text
应用“证明它有效”。运行真实导入流程，展示实际写入的记录。
```

<!-- zh-CN:end 5f9844ed75b9a99b -->

Say two parallel attempts are about to write to the same branch:

<!-- zh-CN:begin e589576e6cce4692 -->

两个并行尝试要写同一分支时：

<!-- zh-CN:end e589576e6cce4692 -->

```text
separate before serializing shared state. give each attempt its own worktree, no locks.
```

<!-- zh-CN:begin 18c600ff83207efc -->

```text
序列化共享状态前先分离。让每个尝试使用自己的工作树，不要锁。
```

<!-- zh-CN:end 18c600ff83207efc -->

Each phrase lands because the rule behind it is specific. The agent still has to say, in its reply, which decision the rule changed. A principle citation with no decision behind it means the agent named the rule without applying it.

<!-- zh-CN:begin e1fe6edcdf98b5ca -->

每个短语有效，因为背后的规则足够具体。智能体必须在回复中说明规则改变了什么决策。只引用原则却说不出被改变的决定，意味着它只命名规则而未应用。

<!-- zh-CN:end e1fe6edcdf98b5ca -->

## The 24, briefly

<!-- zh-CN:begin a788b3b4d6f2c758 -->

## 24 条原则简述

<!-- zh-CN:end a788b3b4d6f2c758 -->

The core principles decide how much to build and when to rethink the design:

<!-- zh-CN:begin 9446d127d0c974e7 -->

核心原则决定构建多少及何时重新设计：

<!-- zh-CN:end 9446d127d0c974e7 -->

- [Laziness Protocol](../../skills/principle-laziness-protocol/SKILL.md) prefers deletion and the smallest change that solves the problem.

<!-- zh-CN:begin 66a1517642a7391e -->

- [懒惰协议](../../skills/principle-laziness-protocol/SKILL.md)：优先删除和解决问题的最小变更。

<!-- zh-CN:end 66a1517642a7391e -->
- [Foundational Thinking](../../skills/principle-foundational-thinking/SKILL.md) chooses the core data structures before writing logic.

<!-- zh-CN:begin f8cd2810a6112049 -->

- [基础性思考](../../skills/principle-foundational-thinking/SKILL.md)：写逻辑前选好核心数据结构。

<!-- zh-CN:end f8cd2810a6112049 -->
- [Redesign from First Principles](../../skills/principle-redesign-from-first-principles/SKILL.md) integrates a new requirement as if it had been there from day one.

<!-- zh-CN:begin cfc77aca6fe94362 -->

- [从第一性原理重新设计](../../skills/principle-redesign-from-first-principles/SKILL.md)：把新需求当作从第一天就存在来整合。

<!-- zh-CN:end cfc77aca6fe94362 -->
- [Attack the Premise](../../skills/principle-attack-the-premise/SKILL.md) writes down the premise that two or more failed fixes shared and tests it directly before the next fix.

<!-- zh-CN:begin 46049cc9e876da55 -->

- [攻击前提](../../skills/principle-attack-the-premise/SKILL.md)：写下两个以上失败修复共享的前提，在下一次修复前直接检验。

<!-- zh-CN:end 46049cc9e876da55 -->
- [Subtract Before You Add](../../skills/principle-subtract-before-you-add/SKILL.md) removes dead weight before building on top of it.

<!-- zh-CN:begin 622420dd60e2dacb -->

- [先减后加](../../skills/principle-subtract-before-you-add/SKILL.md)：先移除无用的重量。

<!-- zh-CN:end 622420dd60e2dacb -->
- [Minimize Reader Load](../../skills/principle-minimize-reader-load/SKILL.md) collapses layers and hidden state a reader must hold in their head.

<!-- zh-CN:begin 3b700801ce8bb14b -->

- [最小化读者负担](../../skills/principle-minimize-reader-load/SKILL.md)：折叠读者必须记住的层次和隐藏状态。

<!-- zh-CN:end 3b700801ce8bb14b -->
- [Outcome-Oriented Execution](../../skills/principle-outcome-oriented-execution/SKILL.md) converges rewrites on the target design instead of preserving throwaway compatibility states.

<!-- zh-CN:begin 4a50fdf2108c700d -->

- [结果导向执行](../../skills/principle-outcome-oriented-execution/SKILL.md)：让重写收敛到目标设计，而非保留一次性兼容状态。

<!-- zh-CN:end 4a50fdf2108c700d -->
- [Experience First](../../skills/principle-experience-first/SKILL.md) chooses the user's result over implementation convenience.

<!-- zh-CN:begin 75cec79900228ed7 -->

- [体验优先](../../skills/principle-experience-first/SKILL.md)：优先用户结果而非实现便利。

<!-- zh-CN:end 75cec79900228ed7 -->
- [Exhaust the Design Space](../../skills/principle-exhaust-the-design-space/SKILL.md) builds two or three competing prototypes when there's no precedent.

<!-- zh-CN:begin b79dd0ab75271a19 -->

- [穷尽设计空间](../../skills/principle-exhaust-the-design-space/SKILL.md)：没有先例时构建两三个竞争原型。

<!-- zh-CN:end b79dd0ab75271a19 -->
- [Build the Lever](../../skills/principle-build-the-lever/SKILL.md) builds the script that does or proves the work, so a reviewer can rerun it. When an agent keeps doing the same thing by hand, have it write the tool or skill it wishes it had. If a script can do a step the same way every time, use the script, and save agents for the judgment calls.

<!-- zh-CN:begin a9da30ec19a5a526 -->

- [构建杠杆](../../skills/principle-build-the-lever/SKILL.md)：构建执行或证明工作的脚本，让审阅者可重跑。重复手工工作时让它写出想要的工具或技能；脚本能稳定完成的步骤交给脚本，把智能体留给判断。

<!-- zh-CN:end a9da30ec19a5a526 -->

The architecture principles decide where state, validation, and compatibility live:

<!-- zh-CN:begin 5e07c1ec279fb0ba -->

架构原则决定状态、验证和兼容性放在哪里：

<!-- zh-CN:end 5e07c1ec279fb0ba -->

- [Model the Domain](../../skills/principle-model-the-domain/SKILL.md) encodes repeated rules in one structure, not scattered conditionals.

<!-- zh-CN:begin e655d13850e5d868 -->

- [领域建模](../../skills/principle-model-the-domain/SKILL.md)：把重复规则编码为一种结构，而非分散条件。

<!-- zh-CN:end e655d13850e5d868 -->
- [Boundary Discipline](../../skills/principle-boundary-discipline/SKILL.md) validates at the boundary and trusts internal types.

<!-- zh-CN:begin a13f0e7511497c8a -->

- [边界纪律](../../skills/principle-boundary-discipline/SKILL.md)：在边界验证，内部信任类型。

<!-- zh-CN:end a13f0e7511497c8a -->
- [Type System Discipline](../../skills/principle-type-system-discipline/SKILL.md) makes illegal states unrepresentable.

<!-- zh-CN:begin 0ff5f34386cda695 -->

- [类型系统纪律](../../skills/principle-type-system-discipline/SKILL.md)：让非法状态无法表示。

<!-- zh-CN:end 0ff5f34386cda695 -->
- [Make Operations Idempotent](../../skills/principle-make-operations-idempotent/SKILL.md) converges retries on the same end state.

<!-- zh-CN:begin 4465aaf83510f53b -->

- [操作幂等](../../skills/principle-make-operations-idempotent/SKILL.md)：让重试收敛到同一末态。

<!-- zh-CN:end 4465aaf83510f53b -->
- [Migrate Callers Then Delete Legacy APIs](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) migrates and deletes in one wave.

<!-- zh-CN:begin 83b1ea953299c7a4 -->

- [先迁移调用方再删除旧 API](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md)：迁移和删除一次完成。

<!-- zh-CN:end 83b1ea953299c7a4 -->
- [Separate Before Serializing Shared State](../../skills/principle-separate-before-serializing-shared-state/SKILL.md) removes the sharing before adding coordination.

<!-- zh-CN:begin 261a42c4698943f6 -->

- [共享状态先分离再序列化](../../skills/principle-separate-before-serializing-shared-state/SKILL.md)：协调前先移除共享。

<!-- zh-CN:end 261a42c4698943f6 -->

The verification principles define what counts as proof:

<!-- zh-CN:begin d9251fb1803fde51 -->

验证原则定义什么算证据：

<!-- zh-CN:end d9251fb1803fde51 -->

- [Prove It Works](../../skills/principle-prove-it-works/SKILL.md) verifies the real artifact, not a proxy.

<!-- zh-CN:begin 4cf9a0bbb9314dda -->

- [证明它有效](../../skills/principle-prove-it-works/SKILL.md)：验证真实产物而非代理指标。

<!-- zh-CN:end 4cf9a0bbb9314dda -->
- [Fix Root Causes](../../skills/principle-fix-root-causes/SKILL.md) reproduces and traces to the cause before changing code.

<!-- zh-CN:begin fd688461b0c1768e -->

- [修复根因](../../skills/principle-fix-root-causes/SKILL.md)：改代码前复现并追溯到根因。

<!-- zh-CN:end fd688461b0c1768e -->
- [Sequence Work into Verifiable Units](../../skills/principle-sequence-verifiable-units/SKILL.md) ends each small unit in a check before starting the next.

<!-- zh-CN:begin 772815ef65e3b210 -->

- [把工作划分为可验证单元](../../skills/principle-sequence-verifiable-units/SKILL.md)：每个小单元检查通过后才开始下一单元。

<!-- zh-CN:end 772815ef65e3b210 -->
- [Test Behavior, Not Implementation](../../skills/principle-test-behavior-not-implementation/SKILL.md) asserts what the code's users can observe, so a test fails when that behavior breaks and survives a change to the internals.

<!-- zh-CN:begin 3ec2dc3e91db6413 -->

- [测试行为而非实现](../../skills/principle-test-behavior-not-implementation/SKILL.md)：断言用户可观察内容，使行为破坏时失败、内部变化时仍通过。

<!-- zh-CN:end 3ec2dc3e91db6413 -->
- [Explain the Number](../../skills/principle-explain-the-number/SKILL.md) names what limits a measured number and rules out that it measured something else, before anyone trusts or reports it. [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) turns it into seven questions you answer from real runs.

<!-- zh-CN:begin 50025e7c77600aa2 -->

- [解释数字](../../skills/principle-explain-the-number/SKILL.md)：说明数字的限制并排除测错对象后才信任或报告；[`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) 将其化为七个真实运行问题。

<!-- zh-CN:end 50025e7c77600aa2 -->

The delegation principles keep parallel work sane:

<!-- zh-CN:begin 9eb05bbad16dfa81 -->

委派原则保证并行工作有序：

<!-- zh-CN:end 9eb05bbad16dfa81 -->

- [Guard the Context Window](../../skills/principle-guard-the-context-window/SKILL.md) routes bulk reading to subagents and keeps findings in the main chat.

<!-- zh-CN:begin 1b09b5f5ce1d007e -->

- [保护上下文窗口](../../skills/principle-guard-the-context-window/SKILL.md)：把批量阅读交给子智能体，主聊天只保留发现。

<!-- zh-CN:end 1b09b5f5ce1d007e -->
- [Never Block on the Human](../../skills/principle-never-block-on-the-human/SKILL.md) proceeds on reversible work and presents the result.

<!-- zh-CN:begin 50e7d6ec8a0dea88 -->

- [绝不要被人阻塞](../../skills/principle-never-block-on-the-human/SKILL.md)：继续可逆工作并呈现结果。

<!-- zh-CN:end 50e7d6ec8a0dea88 -->

And one meta principle:

<!-- zh-CN:begin e367a46930e19ad9 -->

还有一条元原则：

<!-- zh-CN:end e367a46930e19ad9 -->

- [Encode Lessons in Structure](../../skills/principle-encode-lessons-in-structure/SKILL.md) turns advice you've repeated twice into a lint, check, or script. [`/correct`](../../skills/correct/SKILL.md) applies it to a whole repo, as shown in [Make it yours](./09-make-it-yours.md#fix-the-environment-with-correct).

<!-- zh-CN:begin cda25da10f8d09bc -->

- [把经验编码进结构](../../skills/principle-encode-lessons-in-structure/SKILL.md)：把重复两次的建议变成 lint、检查或脚本。[`/correct`](../../skills/correct/SKILL.md) 将其应用于整个仓库，见[让它成为你的](./09-make-it-yours.md#fix-the-environment-with-correct)。

<!-- zh-CN:end cda25da10f8d09bc -->

Don't memorize the list. Skim it now, then come back when you catch the agent doing something a name here would have prevented. That's how the vocabulary sticks.

<!-- zh-CN:begin 9b848e1314d21f21 -->

不必背清单。现在浏览，日后看到智能体做了某个名称本应阻止的事再回来。词汇表就是这样记住的。

<!-- zh-CN:end 9b848e1314d21f21 -->

Next: [Make it yours](./09-make-it-yours.md).

<!-- zh-CN:begin a7d9adca1b8ce6da -->

下一步：[让它成为你的](./09-make-it-yours.md)。

<!-- zh-CN:end a7d9adca1b8ce6da -->
