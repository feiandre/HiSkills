## What it does

<!-- zh-CN:begin 9a747e0102eb3a29 -->

## 它的作用

<!-- zh-CN:end 9a747e0102eb3a29 -->

`codebase-design` fixes the words you use to design a module: **module**, **interface**, **depth**, **seam**, **adapter**, **leverage**, **locality**. It defines each one precisely, bans the loose substitutes ("component", "service", "API", "boundary"), and states the handful of principles that follow from them.

<!-- zh-CN:begin 13a7304b469dbaeb -->

`codebase-design` 固定你在设计模块时使用的词：**模块**、**接口**、**深度**、**接缝**、**适配器**、**杠杆**、**局部性**。它精确定义每个词，禁止松散替代词（“组件”“服务”“API”“边界”），并陈述由这些词得出的几条原则。

<!-- zh-CN:end 13a7304b469dbaeb -->

It is a reference, not a process. It runs no loop, produces no artifact, and never stops to ask you a question. Every other skill that touches design uses its vocabulary. On its own, it gives you the words and stops. Know this before you invoke it. If you point a [session](https://www.aihero.dev/ai-coding-dictionary/session) at a skill with no process and no stopping rule and say "go", the agent invents a process. The questions below show what that looks like.

<!-- zh-CN:begin d6b62e5f38391194 -->

它是参考，不是流程。它不运行循环、不产生产物，也绝不停下来问你问题。其他涉及设计工作的技能都使用其词汇表。单独使用时，它给你这些词后停止。调用前应知道这一点。如果让一个[会话](https://www.aihero.dev/ai-coding-dictionary/session)面对没有流程和停止规则的技能并说“开始”，智能体会自行发明流程。下方问题展示了这种结果。

<!-- zh-CN:end d6b62e5f38391194 -->

## When to reach for it

<!-- zh-CN:begin c6e12c94d58729d1 -->

## 何时使用

<!-- zh-CN:end c6e12c94d58729d1 -->

Type `/codebase-design`, or the agent reaches for it automatically when a design task fits.

<!-- zh-CN:begin b74898fa61fe2a9f -->

输入 `/codebase-design`，或在设计任务符合时由智能体自动使用。

<!-- zh-CN:end b74898fa61fe2a9f -->

Reach for it when you already know which code you're redesigning and you need to think about its shape: where the seam goes, how small the interface can get, whether an extraction removes complexity from its callers. Also use it to settle an argument about what a design word means.

<!-- zh-CN:begin c665a763c5a1ad96 -->

已经知道要重新设计哪段代码，并需要思考其形态时使用：接缝放在哪里、接口能缩到多小、抽取是否能让调用方减少复杂性。也可用它解决关于某个设计词含义的争论。

<!-- zh-CN:end c665a763c5a1ad96 -->

Several skills are close to it. Pick by the problem you have:

<!-- zh-CN:begin 88969449451c408d -->

有几个技能与之接近。按问题选择：

<!-- zh-CN:end 88969449451c408d -->

| The problem | The skill |
|---|---|
| The shape of one module: its interface, its seam, its depth | `codebase-design` |
| The *words of the domain*: "account" means three things, two people mean different things by "cancellation" | [domain-modeling](https://aihero.dev/skills-domain-modeling) |
| You don't yet know *which* module to redesign | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) (the survey that finds candidates) |
| You want the design argued with, not just named | [grilling](https://aihero.dev/skills-grilling) |
| There's a concrete behaviour to build and you want tests that survive a refactor | [tdd](https://aihero.dev/skills-tdd) |

<!-- zh-CN:begin ea7c307db834e782 -->

| 问题 | 技能 |
|---|---|
| 一个模块的形态：接口、接缝、深度 | `codebase-design` |
| *领域用词*：“account”有三种含义，两个人对“cancellation”理解不同 | [domain-modeling](https://aihero.dev/skills-domain-modeling) |
| 尚不知道要重新设计*哪个*模块 | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture)（筛查候选的调查） |
| 想对设计进行论证，而不只是命名 | [grilling](https://aihero.dev/skills-grilling) |
| 有具体行为要构建，并希望测试经得起重构 | [tdd](https://aihero.dev/skills-tdd) |

<!-- zh-CN:end ea7c307db834e782 -->

## The vocabulary

<!-- zh-CN:begin 020f2325486b0870 -->

## 词汇表

<!-- zh-CN:end 020f2325486b0870 -->

The glossary is the skill. The skill defines every term against the others, and gives each one the word it replaces.

<!-- zh-CN:begin f7b6bd68a9e18b4d -->

词汇表就是技能。技能用这些词互相定义每个术语，并给出它替代的松散词。

<!-- zh-CN:end f7b6bd68a9e18b4d -->

| Term | What it means | Don't say |
|---|---|---|
| **Module** | Anything with an interface and an implementation. Deliberately scale-agnostic: a function, a class, a package, a slice spanning tiers. | unit, component, service |
| **Interface** | Everything a caller must know to use it correctly: the type signature, plus invariants, ordering constraints, error modes, required config, performance characteristics. | API, signature |
| **Depth** | Leverage at the interface: how much behaviour a caller or a test can exercise per unit of interface they have to learn. **Deep**: a lot of behaviour behind a small interface. **Shallow**: the interface is nearly as complex as the implementation. | none |
| **Seam** | Michael Feathers' term: a place you can alter behaviour without editing in that place. It is the *location* of an interface, and where to put it is its own decision, separate from what goes behind it. | boundary |
| **Adapter** | A concrete thing satisfying an interface at a seam. It names a role, not a kind of thing: an in-memory fake and a Postgres repo are both adapters. | none |
| **Leverage** | What callers get from depth: more capability per unit of interface learned. | none |
| **Locality** | What maintainers get from depth: changes, bugs and verification stay in one place, so one fix covers every caller. | none |

<!-- zh-CN:begin f37683182876487f -->

| 术语 | 含义 | 不应说 |
|---|---|---|
| **模块** | 任何具有接口和实现的东西。有意与尺度无关：函数、类、包、跨层切片均可。 | 单元、组件、服务 |
| **接口** | 调用方正确使用它必须知道的全部内容：类型签名，以及不变量、顺序约束、错误模式、必需配置、性能特征。 | API、签名 |
| **深度** | 接口处的杠杆：调用方或测试每学习一单位接口，可以驱动多少行为。**深**：小接口后的大量行为。**浅**：接口几乎与实现一样复杂。 | 无 |
| **接缝** | Michael Feathers 的术语：无需在该处编辑即可改变行为的位置。它是接口的*位置*，放在哪里是独立决定，与接口背后的内容不同。 | 边界 |
| **适配器** | 在接缝处满足接口的具体事物。它命名角色而非类别：内存中的假实现和 Postgres 仓库都是适配器。 | 无 |
| **杠杆** | 调用方从深度获得的东西：每学习一单位接口获得更多能力。 | 无 |
| **局部性** | 维护者从深度获得的东西：变更、缺陷和验证停留在一处，因此一个修复覆盖所有调用方。 | 无 |

<!-- zh-CN:end f37683182876487f -->

The skill does *not* define depth as the ratio of implementation lines to interface lines, which is Ousterhout's own definition. That metric rewards padding the implementation, so the skill uses depth-as-leverage instead.

<!-- zh-CN:begin 1b111f384a944acc -->

技能*不*把深度定义为实现行数与接口行数之比（Ousterhout 的定义）。该指标会奖励膨胀实现，因此技能采用“深度即杠杆”。

<!-- zh-CN:end 1b111f384a944acc -->

## The four principles

<!-- zh-CN:begin 74c940642ec6c28d -->

## 四项原则

<!-- zh-CN:end 74c940642ec6c28d -->

- **Depth is a property of the interface, not the implementation.** A deep module can be built internally from small swappable parts. Callers just don't see them. A module can have internal seams its own tests use, and one external seam at its interface.

<!-- zh-CN:begin 14147fc737f69290 -->

- **深度是接口属性，不是实现属性。** 深模块内部可由小型可替换部分构建，调用方看不到。模块可有供自身测试使用的内部接缝，以及接口处的一个外部接缝。

<!-- zh-CN:end 14147fc737f69290 -->
- **The deletion test.** Imagine deleting the module. If complexity disappears, the module was a pass-through. If it reappears across N callers, the module was hiding real complexity.

<!-- zh-CN:begin dcfccedb1abb2e32 -->

- **删除测试。** 想象删除该模块。复杂性若消失，它只是传递层；若在 N 个调用方中重新出现，它隐藏了真实复杂性。

<!-- zh-CN:end dcfccedb1abb2e32 -->
- **The interface is the test surface.** Callers and tests cross the same seam. If you want to test *past* the interface, the module is the wrong shape.

<!-- zh-CN:begin 4aba17c5fda6c84c -->

- **接口就是测试面。** 调用方和测试跨过同一接缝。若想测试*越过*接口，模块形态就错了。

<!-- zh-CN:end 4aba17c5fda6c84c -->
- **One adapter means a hypothetical seam. Two adapters means a real one.** Don't cut a seam until something varies across it. A single-adapter seam is just indirection.

<!-- zh-CN:begin d69360ca4da31daf -->

- **一个适配器意味着假设接缝，两个适配器才是真实接缝。** 接缝两侧没有变化时不要切开。单适配器接缝只是间接层。

<!-- zh-CN:end d69360ca4da31daf -->

Two supporting files go further, and the skill reads them on demand rather than up front. [DEEPENING.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/DEEPENING.md) classifies a candidate's dependencies into four categories (in-process, local-substitutable, remote-but-owned, true-external), because the category decides how you test the deepened module across its seam. [DESIGN-IT-TWICE.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/DESIGN-IT-TWICE.md) starts parallel [sub-agents](https://www.aihero.dev/ai-coding-dictionary/subagent) to produce three or more radically different interfaces for the same module, then compares them on depth, locality and seam placement.

<!-- zh-CN:begin c274ff8123ec3025 -->

另有配套文件按需读取。[DEEPENING.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/DEEPENING.md) 将候选依赖分为四类（进程内、本地可替换、远程但自有、真正外部），类别决定如何跨接缝测试深化模块。[DESIGN-IT-TWICE.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/DESIGN-IT-TWICE.md) 并行启动[子智能体](https://www.aihero.dev/ai-coding-dictionary/subagent)为同一模块产出三个以上差异极大的接口，再从深度、局部性和接缝位置比较。

<!-- zh-CN:end c274ff8123ec3025 -->

## Common questions

<!-- zh-CN:begin 898ae431ca5dcbd2 -->

## 常见问题

<!-- zh-CN:end 898ae431ca5dcbd2 -->

**How do I actually build a deep module in TypeScript?**

<!-- zh-CN:begin 8fc1ccf8cd41d03e -->

**我到底怎样在 TypeScript 中构建深模块？**

<!-- zh-CN:end 8fc1ccf8cd41d03e -->

This is the most-asked question about the skill and the skill does not answer it. It defines what a deep module *is*; it says nothing about how to stop a stray import from reaching past the interface. [Issue #458](https://github.com/mattpocock/skills/issues/458) put it plainly: "let's say we're happy with the interface, it hides the details, etc. But how do we enforce it? I think without linting or clear guardrails, humans and LLMs alike will start making it messy over time." The answer in that thread gave three options: wrap it in a class or IIFE and accept that the class gets enormous; make it a package in a monorepo and accept the monorepo tooling; or use a linter like [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) to forbid imports that bypass the interface. Of these mechanisms, Effect is the best and dependency-cruiser the second-best. There is a `setup-ts-deep-modules` skill in the repo's `in-progress/` bucket that lays down a `src/packages/<name>/index.ts` convention, but it is a beta-channel skill with no docs page, and it ships no lint rule.

<!-- zh-CN:begin aea9a3998c9b378f -->

这是关于技能最常见的问题，技能不回答。它定义深模块*是什么*，却没说如何阻止杂散导入越过接口。[Issue #458](https://github.com/mattpocock/skills/issues/458) 说得直接：“假设我们满意接口并隐藏了细节，但怎样强制执行？没有 lint 或清晰护栏，人和 LLM 都会逐渐弄乱。”该线程给三个选择：包进类或 IIFE 并接受类变巨大；放进 monorepo 包并接受其工具链；或用 [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) 禁止绕过接口的导入。这些机制中 Effect 最好，dependency-cruiser 次之。仓库 `in-progress/` 中有 `setup-ts-deep-modules` 技能建立 `src/packages/<name>/index.ts` 约定，但它是 beta 渠道、无文档页面，也不含 lint 规则。

<!-- zh-CN:end aea9a3998c9b378f -->

**I pointed a session at it and it burned 100k [tokens](https://www.aihero.dev/ai-coding-dictionary/token) redesigning things I never asked about.**

<!-- zh-CN:begin 261df20c4210d1d5 -->

**我让一个会话使用它，它花了 100k [token](https://www.aihero.dev/ai-coding-dictionary/token) 重新设计我从未要求的内容。**

<!-- zh-CN:end 261df20c4210d1d5 -->

This is a known problem, filed as [issue #449](https://github.com/mattpocock/skills/issues/449). The skill is model-invoked and describes itself as vocabulary, but nothing in it hard-stops an agent from treating it as a runnable process. Told to "resume in /codebase-design and drive the open decisions", an agent picked the part of the skill closest to a process: the parallel sub-agents in `DESIGN-IT-TWICE.md`. It re-explored code a previous session had already mapped, and worked for a long time before it asked anything. This skill has none of the guardrails a driver skill has (checkpoints, one question at a time, no auto-advance), because it is a reference. The workaround is to invoke a driver skill (`/grill-with-docs`, `/improve-codebase-architecture` or `/tdd`) and use `codebase-design` as its vocabulary. The issue is open.

<!-- zh-CN:begin 33d16ba2049d4719 -->

这是已知问题 [issue #449](https://github.com/mattpocock/skills/issues/449)。技能由模型调用并自称词汇表，但没有硬阻止智能体把它当流程。被要求“在 /codebase-design 中继续并推进开放决策”时，智能体选择了最像流程的部分：`DESIGN-IT-TWICE.md` 的并行子智能体。它重新探索前一会议已绘制过的代码，工作很久才提问。该技能没有驱动技能所有的护栏（检查点、一次一问、不自动推进），因为它是参考。变通方式是调用驱动技能（`/grill-with-docs`、`/improve-codebase-architecture` 或 `/tdd`），把 `codebase-design` 当作词汇层。issue 仍开放。

<!-- zh-CN:end 33d16ba2049d4719 -->

**Where did `design-an-interface` go? And is there an `/interface-design` skill?**

<!-- zh-CN:begin 25e8e8278a00a565 -->

**`design-an-interface` 去哪了？有 `/interface-design` 技能吗？**

<!-- zh-CN:end 25e8e8278a00a565 -->

This skill replaced `design-an-interface` and took over its content. Nothing is missing. Its "design it twice" technique (parallel sub-agents generating radically different designs, from Ousterhout) ships here as `DESIGN-IT-TWICE.md`. Separately, several people have asked for a dedicated `/interface-design` skill for the deep-module/thin-interface philosophy; this skill already covers that philosophy, and no separate skill is planned. If you came looking for either name, this is the page.

<!-- zh-CN:begin d3bc98d009430df7 -->

本技能取代 `design-an-interface` 并继承其内容，没有缺失。其“设计两遍”技术（并行子智能体产出截然不同设计，源自 Ousterhout）在此以 `DESIGN-IT-TWICE.md` 提供。另有用户要求专门的 `/interface-design` 技能；本技能已覆盖深模块／薄接口哲学，不计划单列。寻找任一名的人都应看此页。

<!-- zh-CN:end d3bc98d009430df7 -->

**Isn't this a file-structure convention, such as folders, barrel files, feature slices?**

<!-- zh-CN:begin 9a563be2d58b2dea -->

**这不是文件结构约定吗，例如文件夹、barrel 文件、功能切片？**

<!-- zh-CN:end 9a563be2d58b2dea -->

No. People have pushed back on this many times, and the skill has not changed. [Issue #95](https://github.com/mattpocock/skills/issues/95) proposed a formalised fractal-tree file structure as the concrete implementation of deep modules; the reply was that the two are independent: "deep modules are about the design of the interface and accessing through a strict interface, no matter what the file system looks like. It seems perfectly possible that you could have shallow modules with this approach." The same came up in #458: "I think you might be tying the concept of modules too closely to the file system. The file system can certainly be a useful hint to the shape of modules, but there's no need to use the file system in the construction of deep modules." The glossary defines **module** as scale-agnostic on purpose.

<!-- zh-CN:begin ccf59ae65c6f1471 -->

不是。已多次遭到质疑但技能未改变。[Issue #95](https://github.com/mattpocock/skills/issues/95) 提议形式化分形树文件结构来落实深模块；回复说两者独立：“深模块关乎接口设计并通过严格接口访问，与文件系统形态无关。用这种方法也完全可能有浅模块。” #458 再次出现：“你可能把模块概念与文件系统绑得太紧。文件系统可提示模块形态，但构建深模块未必需要使用文件系统。”词汇表有意把**模块**定义为尺度无关。

<!-- zh-CN:end ccf59ae65c6f1471 -->

**Does `tdd` actually use this vocabulary?**

<!-- zh-CN:begin 7449b3d94b36d08a -->

**`tdd` 真的使用这些词汇吗？**

<!-- zh-CN:end 7449b3d94b36d08a -->

It does now, but for a long time it did not. v1.0 removed the inline deep-module notes from `tdd` in favour of this shared skill, but nobody added a pointer to replace them, so `tdd` defined "seam" for itself and referenced nothing. The pointer is now in `tdd`, and the agent follows it when the open question is the shape of the interface, not the tests. `tdd` still owns "seam" as the boundary you *test* at; this skill owns the module shape behind it.

<!-- zh-CN:begin 147a2e8163a2ba78 -->

现在使用，但过去很久没有。v1.0 从 `tdd` 移除内联深模块说明以改用共享技能，却没人添加替代指针，于是 `tdd` 自行定义“接缝”且不引用。现在 `tdd` 有指针，开放问题是接口形态而非测试时，智能体遵循。`tdd` 仍拥有作为*测试边界*的“接缝”；本技能拥有背后的模块形态。

<!-- zh-CN:end 147a2e8163a2ba78 -->

**Does the design-it-twice pattern work outside Claude Code?**

<!-- zh-CN:begin bcb81a5b53269dce -->

**设计两遍模式在 Claude Code 外可用吗？**

<!-- zh-CN:end bcb81a5b53269dce -->

Not cleanly. `DESIGN-IT-TWICE.md` says "spawn 3+ sub-agents in parallel using the Agent tool", and "Agent" is the name of a Claude Code [tool](https://www.aihero.dev/ai-coding-dictionary/tool). The repo ships metadata for other [harnesses](https://www.aihero.dev/ai-coding-dictionary/harness), including Codex, and those may have no tool with that name. So the parallel-design phase is less portable than the skill's metadata suggests. [Issue #564](https://github.com/mattpocock/skills/issues/564) tracks this, and it is open.

<!-- zh-CN:begin 5a367cd50f50401b -->

不顺畅。`DESIGN-IT-TWICE.md` 说“使用 Agent 工具并行启动 3+ 子智能体”，而“Agent”是 Claude Code [工具](https://www.aihero.dev/ai-coding-dictionary/tool)名。仓库为其他[运行环境](https://www.aihero.dev/ai-coding-dictionary/harness)（包括 Codex）提供元数据，它们可能没有此名工具。所以并行设计阶段不如元数据所示可移植。[Issue #564](https://github.com/mattpocock/skills/issues/564) 跟踪此问题，仍开放。

<!-- zh-CN:end 5a367cd50f50401b -->

**Can I add my own concepts to the glossary, such as connascence, module secrets, [progressive disclosure](https://www.aihero.dev/ai-coding-dictionary/progressive-disclosure)?**

<!-- zh-CN:begin 818ff5d38442d270 -->

**我可以加入 connascence、模块秘密、[渐进式披露](https://www.aihero.dev/ai-coding-dictionary/progressive-disclosure)等概念吗？**

<!-- zh-CN:end 818ff5d38442d270 -->

People have proposed those. [Issue #180](https://github.com/mattpocock/skills/issues/180) adds Parnas's module secrets and Page-Jones's connascence as a naming layer for *what* is leaking across a seam, with a working diff attached; [issue #303](https://github.com/mattpocock/skills/issues/303) proposes progressive disclosure inside the implementation, so a module that is deep at its public interface also has structure inside it. Both are open and unmerged. The shipped glossary is small on purpose, and the skill itself gives the reason: consistent language is the whole point, and a term nobody uses consistently is worse than no term.

<!-- zh-CN:begin dc5f130a9faa4a82 -->

有人提议过。[Issue #180](https://github.com/mattpocock/skills/issues/180) 加入 Parnas 模块秘密和 Page-Jones 的 connascence，作为*跨接缝泄漏什么*的命名层，并附可运行差异；[issue #303](https://github.com/mattpocock/skills/issues/303) 提议在实现内部也渐进披露，使公开接口深的模块内部也有结构。两者均开放且未合并。发布的词汇表有意保持小，技能给的理由是：一致语言就是重点，人人都不一致使用的词比没有词更糟。

<!-- zh-CN:end dc5f130a9faa4a82 -->

## It's working if

<!-- zh-CN:begin 20b17359c6565471 -->

## 生效时

<!-- zh-CN:end 20b17359c6565471 -->

- The design conversation stops producing the words "component", "service" and "boundary", and starts producing "module", "interface" and "seam".

<!-- zh-CN:begin c8b1654e7e49571c -->

- 设计对话不再产出“组件”“服务”“边界”，而产出“模块”“接口”“接缝”。

<!-- zh-CN:end c8b1654e7e49571c -->
- Someone can point at a proposed extraction and say whether it passes the deletion test, without hedging.

<!-- zh-CN:begin 6f72efe2f222141e -->

- 某人能指着候选抽取并明确说它是否通过删除测试。

<!-- zh-CN:end 6f72efe2f222141e -->
- A proposed seam comes with a second adapter named, not just the first one.

<!-- zh-CN:begin 47cd21579ea8702b -->

- 提议接缝时能说出第二个适配器，而不只第一个。

<!-- zh-CN:end 47cd21579ea8702b -->
- Discussion of an interface covers invariants, ordering and error modes, not only the type signature.

<!-- zh-CN:begin a25dbca64553609e -->

- 接口讨论覆盖不变量、顺序、错误模式，不只类型签名。

<!-- zh-CN:end a25dbca64553609e -->
- Invoking it does not start a session. If the agent begins reading files and proposing refactors from `/codebase-design` alone, it has mistaken the reference for a driver.

<!-- zh-CN:begin ca824a2c8a454b24 -->

- 调用它不启动会话。若智能体仅凭 `/codebase-design` 开始读文件和提议重构，它把参考误当驱动器。

<!-- zh-CN:end ca824a2c8a454b24 -->

## Where it fits

<!-- zh-CN:begin 241460f4548d424f -->

## 适用范围

<!-- zh-CN:end 241460f4548d424f -->

`codebase-design` is a **reach-for-it-anytime standalone**, and the vocabulary layer underneath the engineering skills rather than a step in any chain. Its closest neighbour is [domain-modeling](https://aihero.dev/skills-domain-modeling), the parallel reference for the *problem domain*'s words rather than the module's shape. The two are usually wanted together, since naming a deep module well needs both. [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) is the other: it surveys a codebase for deepening candidates and writes every one of them in this glossary, so it finds the module and you design it in this skill's words. When you're unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 40f98054bd084f79 -->

`codebase-design` 是**随时独立使用的参考**，是工程技能下方的词汇层，不属于任何链中的步骤。最近邻是 [domain-modeling](https://aihero.dev/skills-domain-modeling)，它处理*问题领域*用词。两者通常一起需要，因为更好命名深模块需要二者。[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 用本词汇表调查并记录候选深化模块，所以它找模块，你用本技能词语设计。不确定使用哪个技能或流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 可路由。

<!-- zh-CN:end 40f98054bd084f79 -->
