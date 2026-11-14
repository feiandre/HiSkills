## What it does

<!-- zh-CN:begin f2becdd936bd21ad -->

## 功能

<!-- zh-CN:end f2becdd936bd21ad -->

`improve-codebase-architecture` surveys a codebase for **deepening opportunities**. These are places where a shallow module (an interface nearly as complex as the thing it hides) could become a deep one. It writes them up as a self-contained HTML report, and then [grills](https://www.aihero.dev/ai-coding-dictionary/grilling) you through the one you pick.

<!-- zh-CN:begin 0019cbc570303025 -->

`improve-codebase-architecture` 扫描代码库中的**加深机会**：浅模块（接口几乎和它隐藏的实现一样复杂）可以变成深模块的位置。它写成自包含 HTML 报告，再围绕你选中的一项[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)你。

<!-- zh-CN:end 0019cbc570303025 -->

It never changes the code. The whole run produces a conversation and one HTML file in your OS temp directory. You do the refactor later, in a separate [session](https://www.aihero.dev/ai-coding-dictionary/session), through the normal build flow. This makes it a survey, not a refactoring tool, so you can run it on a codebase you are not ready to touch yet.

<!-- zh-CN:begin abd02c1568cf7d79 -->

它绝不改代码。整次运行产生一场对话和操作系统临时目录中的一个 HTML 文件。你稍后在独立[会话](https://www.aihero.dev/ai-coding-dictionary/session)通过正常构建流程重构。这使它成为勘察工具，而不是重构工具，因此可先在暂时不准备改动的代码库上运行。

<!-- zh-CN:end abd02c1568cf7d79 -->

Two filters stop the report from becoming generic cleanup advice. First, every candidate must pass the **deletion test**: if you removed this module, would its complexity move behind a smaller interface, or spread across the callers? Only the first case gets a card. Second, unless you point it at a specific area, it reads recent commit history first and focuses the scan on paths that change often. A deepening in code that nobody touches is a refactor that never pays back.

<!-- zh-CN:begin 31ccdfeee7e80192 -->

两个筛选器防止报告退化为泛泛清理建议。第一，每个候选必须通过**删除测试**：若删除该模块，复杂性会集中到更小接口后，还是分散给调用者？只有前者才生成卡片。第二，未指定区域时先读取近期提交，把扫描集中在经常变化的路径。无人触碰代码中的加深机会永远无法回收成本。

<!-- zh-CN:end 31ccdfeee7e80192 -->

## When to reach for it

<!-- zh-CN:begin 727d49f5b390fd51 -->

## 何时使用

<!-- zh-CN:end 727d49f5b390fd51 -->

You invoke this by typing `/improve-codebase-architecture`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) will not reach for it on its own.

<!-- zh-CN:begin 1d28cd2d42ec9117 -->

输入 `/improve-codebase-architecture` 调用；[代理](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。

<!-- zh-CN:end 1d28cd2d42ec9117 -->

It is not a step in the main build loop. You run it periodically to queue up more work that improves the codebase. People use it in four situations:

<!-- zh-CN:begin ff71216bdd98623b -->

它不是主构建循环的一步。可定期运行，为后续改进排入工作。有四类使用场景：

<!-- zh-CN:end ff71216bdd98623b -->

| Situation | How it is used |
| --- | --- |
| Routine upkeep | Run it every few days, or when you have a spare moment, so the structure does not decay between features. |
| Before a big build | Point it at the [spec](https://www.aihero.dev/ai-coding-dictionary/spec) and ask "how can we make this change easy?" This is the most effective prompt for it. |
| Brownfield audit | Run it on a large, unstructured or [vibe-coded](https://www.aihero.dev/ai-coding-dictionary/vibe-coding) repo to find out what shape it is in. |
| Legacy test work | Use it to find the missing seams before you write tests against untestable code. |

<!-- zh-CN:begin 959c3301ce99a0fe -->

| 场景 | 用法 |
| --- | --- |
| 日常维护 | 每隔几天或有空时运行，防止结构在功能迭代中腐化。 |
| 大型构建前 | 指向[规格](https://www.aihero.dev/ai-coding-dictionary/spec)并问“怎样让这次改动容易？”这是最有效的提示。 |
| 既有项目审计 | 在大型、无结构或[随意生成](https://www.aihero.dev/ai-coding-dictionary/vibe-coding)的仓库中了解当前形态。 |
| 遗留测试工作 | 在测试不可测代码前寻找缺失接缝。 |

<!-- zh-CN:end 959c3301ce99a0fe -->

Where it is confusable with siblings:

<!-- zh-CN:begin a1b117906f2303ef -->

容易与相邻技能混淆的场景：

<!-- zh-CN:end a1b117906f2303ef -->

- To design one module you have already chosen, use [codebase-design](https://aihero.dev/skills-codebase-design). This skill finds the module to work on, and `codebase-design` is where you design it.

<!-- zh-CN:begin 10b699a0398f8a17 -->

- 要设计已经选定的一个模块，用 [codebase-design](https://aihero.dev/skills-codebase-design)。本技能寻找要处理的模块，`codebase-design` 负责设计它。

<!-- zh-CN:end 10b699a0398f8a17 -->
- For a whole effort too big to hold in one session, use [wayfinder](https://aihero.dev/skills-wayfinder).

<!-- zh-CN:begin f89d163c958f3ead -->

- 整个工作太大、一个会话容纳不下，用 [wayfinder](https://aihero.dev/skills-wayfinder)。

<!-- zh-CN:end f89d163c958f3ead -->
- For "this specific thing is broken," use [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs). It sends you back here when the real finding is that there is no good seam to lock the bug down.

<!-- zh-CN:begin 83cb436ec6ecf2cd -->

- “这个具体东西坏了”，用 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs)。若真正发现是没有好接缝锁定 bug，它会把你送回这里。

<!-- zh-CN:end 83cb436ec6ecf2cd -->

## Prerequisites

<!-- zh-CN:begin ad3723da6ea521a0 -->

## 前提条件

<!-- zh-CN:end ad3723da6ea521a0 -->

None to run it. If `GLOSSARY.md` or ADRs in `docs/adr/` exist, it reads them and uses your domain's own nouns. A candidate then reads as "deepen the Order intake module," not "refactor the FooBarHandler."

<!-- zh-CN:begin 4984228e1eb2a73c -->

运行无需前置。若存在 `GLOSSARY.md` 或 `docs/adr/` 中的 ADR，会读取并使用你的领域名词。候选会写成“加深 Order 接收模块”，而不是“重构 FooBarHandler”。

<!-- zh-CN:end 4984228e1eb2a73c -->

It writes in two places. The report goes to `<tmpdir>/architecture-review-<timestamp>.html`, outside the repo. During the grilling loop it adds or sharpens terms in `GLOSSARY.md`, and creates that file if it does not exist. It also offers to record a rejected candidate as an ADR, so a future run does not suggest it again.

<!-- zh-CN:begin 135125905fce541f -->

它写两处。报告写入仓库外的 `<tmpdir>/architecture-review-<timestamp>.html`。追问循环中会在 `GLOSSARY.md` 增加或精炼术语，文件不存在则创建。它还会询问是否把拒绝的候选记录为 ADR，避免未来再次建议。

<!-- zh-CN:end 135125905fce541f -->

## Depth, and the report that hunts for it

<!-- zh-CN:begin 665b52bcb170b749 -->

## 深度，以及寻找深度的报告

<!-- zh-CN:end 665b52bcb170b749 -->

The skill rests on one idea: **depth**. A deep module puts a lot of behaviour behind a small, stable interface. A shallow module exposes its implementation through an interface nearly as wide as the code beneath it. The report looks for three forms of shallowness:

<!-- zh-CN:begin b9ed0a8e635e5b02 -->

技能基于一个理念：**深度**。深模块用小巧稳定接口承载大量行为；浅模块通过几乎与下层代码一样宽的接口暴露实现。报告寻找三种浅薄：

<!-- zh-CN:end b9ed0a8e635e5b02 -->

- Pure functions extracted only for testability, while the real bugs are in how callers use them (no **locality**).

<!-- zh-CN:begin efa2bb55d8ba8e6a -->

- 只为可测性抽出的纯函数，真正 bug 却位于调用者使用方式中（缺少**局部性**）。

<!-- zh-CN:end efa2bb55d8ba8e6a -->
- Modules that leak across their **seams**.

<!-- zh-CN:begin e04d91ca3bee8fb6 -->

- 跨越**接缝**泄漏的模块。

<!-- zh-CN:end e04d91ca3bee8fb6 -->
- A concept you cannot understand without opening five files.

<!-- zh-CN:begin caf9d9a6fcdb593a -->

- 不打开五个文件就无法理解的概念。

<!-- zh-CN:end caf9d9a6fcdb593a -->

For each one, it proposes the deepening that fixes it.

<!-- zh-CN:begin 01c0bc9873829d3d -->

对每一种，提出可修复它的加深方案。

<!-- zh-CN:end 01c0bc9873829d3d -->

Each candidate is a card with the files involved, the friction, a plain-English solution, the benefit in terms of **locality** and **leverage**, a before/after diagram, and a strength badge.

<!-- zh-CN:begin 621d678c90c39523 -->

每个候选是一张卡，包含涉及文件、摩擦、通俗方案、从**局部性**与**杠杆**解释的收益、前后图以及强度徽章。

<!-- zh-CN:end 621d678c90c39523 -->

| Badge | What it means for you |
| --- | --- |
| `Strong` | The deletion test passes clearly and the friction is real. Take these seriously. |
| `Worth exploring` | Plausible deepening, but the payoff depends on where the code is going next. |
| `Speculative` | Included for completeness. You can ignore most of these. |

<!-- zh-CN:begin 3a3578b250c374a2 -->

| 徽章 | 对你的含义 |
| --- | --- |
| `Strong` | 删除测试明显通过，摩擦真实。认真处理。 |
| `Worth exploring` | 加深合理，但回报取决于代码下一阶段方向。 |
| `Speculative` | 为完整性列出，大多可忽略。 |

<!-- zh-CN:end 3a3578b250c374a2 -->

The report ends with a **Top recommendation**, the candidate it would do first. Then the skill stops and asks which candidate you want to explore. At that point you have decided nothing, and no code has changed.

<!-- zh-CN:begin 50bb0d9d4289657d -->

报告最后给出**首选建议**，即最先处理的候选。随后技能停止，询问你探索哪项。此时尚未作决定，也没有改代码。

<!-- zh-CN:end 50bb0d9d4289657d -->

## What happens after you pick one

<!-- zh-CN:begin 363591a585e187d0 -->

## 选中候选后

<!-- zh-CN:end 363591a585e187d0 -->

When you pick a candidate, a [grilling](https://aihero.dev/skills-grilling) session starts on it. It covers the constraints, what goes behind the seam, which tests survive, and what the deepened interface should look like. The output of that session is a decision, not a diff. From there the normal flow applies: take the decision into [to-spec](https://aihero.dev/skills-to-spec), then [to-tickets](https://aihero.dev/skills-to-tickets), then [implement](https://aihero.dev/skills-implement).

<!-- zh-CN:begin 9fd9d012e712f6c7 -->

选中候选后开始[追问](https://aihero.dev/skills-grilling)会话，覆盖约束、接缝后承载什么、哪些测试保留、加深后的接口形态。输出是决策，不是 diff。之后走正常流程：[to-spec](https://aihero.dev/skills-to-spec) → [to-tickets](https://aihero.dev/skills-to-tickets) → [implement](https://aihero.dev/skills-implement)。

<!-- zh-CN:end 9fd9d012e712f6c7 -->

## Common questions

<!-- zh-CN:begin 3f1de42574b05ea7 -->

## 常见问题

<!-- zh-CN:end 3f1de42574b05ea7 -->

**It grilled me for an hour about one idea instead of showing me options. Can I turn that off?**

<!-- zh-CN:begin 72f8fb04cc8a2918 -->

**围绕一个想法追问我一小时，却不展示选项。能关掉吗？**

<!-- zh-CN:end 72f8fb04cc8a2918 -->

Yes. Say so when you invoke it ("don't grill me, just show the report"). This is the most common complaint about the skill. One user liked it as "a convenient way to get a thorough analysis of improvements," but after the grilling loop was added, found it "borderline unusable." In their sessions it proposed a single solution and then asked "10's or 100's of questions." The design intent is that the report comes first, and the grilling starts only on a candidate you chose. But weaker [models](https://www.aihero.dev/ai-coding-dictionary/model) skip straight to an interview about the first idea they had. Results in that thread vary a lot by model. It is an open issue, and the skill does not yet have a documented no-grill mode.

<!-- zh-CN:begin fa522d20b61cb2b7 -->

可以。调用时说明“不要追问，只展示报告”。这是该技能最常见抱怨。一位用户喜欢它作为“获得全面改进分析”的便利方法，但加入追问循环后认为它“几乎不可用”：会话只提一种方案，然后问“几十或几百个问题”。设计意图是先给出报告，只对你选中的候选追问，但较弱[模型](https://www.aihero.dev/ai-coding-dictionary/model)会直接进入首个想法的访谈。结果因模型差异很大。这是未解决问题，技能尚无有文档的“不追问”模式。

<!-- zh-CN:end fa522d20b61cb2b7 -->

**The report opened as unstyled raw HTML with no diagrams. What happened?**

<!-- zh-CN:begin 12626697ffd7da8b -->

**报告打开后是没有样式的原始 HTML，也没有图。为什么？**

<!-- zh-CN:end 12626697ffd7da8b -->

The report loads Tailwind and Mermaid from CDNs, so it needs network access when you open it. If something blocks those scripts, the page breaks with no error. In the reported case, a security hook required SRI hashes. The agent added them, but the CDN served different bytes to the browser than to the `curl` that computed the hash, so the browser blocked the script. Offline and locked-down environments have the same problem. The agent cannot see it, because it never renders the page. As a workaround, ask for inline CSS and hand-built SVG diagrams instead of the CDN setup. This is an open issue.

<!-- zh-CN:begin ee221ffbfd7d296c -->

报告从 CDN 加载 Tailwind 和 Mermaid，打开时需要网络。脚本被阻止时页面无提示地损坏。报告案例中，安全钩子要求 SRI 哈希；代理添加后，CDN 给浏览器的字节与计算哈希时 `curl` 所得不同，浏览器阻止脚本。离线和锁定环境也有同样问题。代理看不到，因为它不会渲染页面。变通办法：要求内联 CSS 和手写 SVG 图，不使用 CDN。这是未解决问题。

<!-- zh-CN:end ee221ffbfd7d296c -->

**It gave me twelve candidates. Do I work through them in the same session or start a new one?**

<!-- zh-CN:begin f8048a59a9fa69f9 -->

**它给了我十二个候选。应该在同一会话处理，还是新开？**

<!-- zh-CN:end f8048a59a9fa69f9 -->

Use one candidate per session. If you work through several in one conversation, the [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) fills with the report, the grilling, the domain-model edits and the code changes all at once. The report is only a temp file, so carry the candidate forward, not the file. Pick one, grill it, and take the decision into `/to-spec`. Turn the rest into [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) that you can pick up separately later. Put the chosen improvement into a spec instead of going straight to implementation. People ask this often, and the skill itself documents no workflow for it.

<!-- zh-CN:begin dc4e2f399e189fe9 -->

每个会话处理一个候选。一个对话处理多个候选，会让报告、追问、领域模型修改和代码改动同时塞满[上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)。报告只是临时文件，应传递候选而不是文件。选一项、追问、把决策交给 `/to-spec`。其余变成以后单独领取的[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)。把选中的改进写成规格，再进入实施。很多人问这个，技能本身尚未记录相应流程。

<!-- zh-CN:end dc4e2f399e189fe9 -->

**How should I prompt it?**

<!-- zh-CN:begin 13b026aba2b41fd5 -->

**应该怎样提示？**

<!-- zh-CN:end 13b026aba2b41fd5 -->

Prompt it with the next thing you are building. If a big build is coming up, point it at the spec and ask "how can we make this change easy?" A run with no prompt looks for hot spots on its own. That is fine for routine upkeep, but a direction makes the report actionable.

<!-- zh-CN:begin 8f5377fe42355fcd -->

用下一项要做的工作提示。大型构建临近时，指向规格并问“怎样让这次改动容易？”无提示运行会自行寻找热点，日常维护尚可，但给出方向能让报告更可执行。

<!-- zh-CN:end 8f5377fe42355fcd -->

**Does it work on a large legacy codebase?**

<!-- zh-CN:begin 4be8fb007880688a -->

**适用于大型遗留代码库吗？**

<!-- zh-CN:end 4be8fb007880688a -->

Partly. It works well on big existing codebases that lack consistent structure, and it is the recommended upkeep tool after any one-time structural setup. But users with out-of-control projects report it "helped a little but still doesn't seem to cut it." One developer with an eight-year-old legacy codebase reported that the model went in circles, though the same skill produces a clean graph on a tidy repo. There is no dedicated `/refactor` skill for that case yet. If the codebase has no shared vocabulary, run [grill-with-docs](https://aihero.dev/skills-grill-with-docs) first to create one. That usually makes this skill's output much better.

<!-- zh-CN:begin 3b3fbbba0728ff41 -->

部分适用。对缺少一致结构的大型现有代码库效果不错，也是任何一次性结构设置后的推荐维护工具。但失控项目的用户反馈它“有一点帮助，仍不够”。一位维护八年遗留项目的开发者说模型会绕圈，而同样技能在整洁仓库能产生清晰图。目前没有专门的 `/refactor` 技能。若代码库没有共享词汇，先运行 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 创建词汇，通常会显著改善输出。

<!-- zh-CN:end 3b3fbbba0728ff41 -->

**How is this different from `/codebase-design`?**

<!-- zh-CN:begin 239dd5c83cb5aacc -->

**与 `/codebase-design` 有什么区别？**

<!-- zh-CN:end 239dd5c83cb5aacc -->

`/codebase-design` is a reference, not a session driver. It supplies the vocabulary (module, interface, depth, seam, adapter, leverage, locality), and this skill uses it. If you give a fresh agent `/codebase-design` as the task, it fails in a known way. It has no process of its own to follow, so the agent invents one, explores the code again, and runs for a very long time before it asks you anything. Run this skill, and let it use that one.

<!-- zh-CN:begin c9cd9c8de0b83540 -->

`/codebase-design` 是参考，不是会话驱动者。它提供词汇（模块、接口、深度、接缝、适配器、杠杆、局部性），本技能使用它们。若把 `/codebase-design` 直接当任务给新代理，它会以已知方式失败：没有流程可遵循，便自行发明、再次探索代码、运行很久才问你。应运行本技能，让它调用那个参考。

<!-- zh-CN:end c9cd9c8de0b83540 -->

**Will it ever tell me the codebase is fine?**

<!-- zh-CN:begin 5f25cc1d3f660060 -->

**它会告诉我代码库已经没问题吗？**

<!-- zh-CN:end 5f25cc1d3f660060 -->

Rarely, so know that before you start. The skill exists to output findings, so it tends to produce candidates instead of concluding that nothing is wrong. Use the strength badges to correct for this. If every candidate in a report is `Speculative`, the skill found nothing.

<!-- zh-CN:begin b3b52c883b9da6de -->

很少。技能存在意义是输出发现，因此倾向给出候选，而不是结论“哪里都没毛病”。用强度徽章校正。如果报告全部候选都是 `Speculative`，就表示没有发现。

<!-- zh-CN:end b3b52c883b9da6de -->

**Does it work in Codex or another harness?**

<!-- zh-CN:begin b0362bb022df6301 -->

**能在 Codex 或其他宿主中使用吗？**

<!-- zh-CN:end b0362bb022df6301 -->

Partly. The exploration step names Claude Code's `Agent` tool with `subagent_type=Explore` directly. A [harness](https://www.aihero.dev/ai-coding-dictionary/harness) without that tool may skip the parallel exploration instead of using its own equivalent. The skill still runs, but the scan is less thorough. Someone has proposed a harness-neutral rewrite, but it is not merged.

<!-- zh-CN:begin bea76398e547a387 -->

部分可以。探索步骤直接使用 Claude Code 的 `Agent` 工具和 `subagent_type=Explore`。没有该工具的[宿主](https://www.aihero.dev/ai-coding-dictionary/harness)可能跳过并行探索，而不使用自己的等价能力。技能仍运行，但扫描不够彻底。有人提议宿主中立重写，尚未合并。

<!-- zh-CN:end bea76398e547a387 -->

**How do I actually implement deep modules in TypeScript?**

<!-- zh-CN:begin 1dfea7918cb2c217 -->

**如何在 TypeScript 中真正实现深模块？**

<!-- zh-CN:end 1dfea7918cb2c217 -->

The skill does not ship a good answer. People often ask for a `TYPESCRIPT.md` with concrete file and module layouts for the principles, and it does not exist. The skill tells you where a deepening belongs and what goes behind the seam. You must turn that into a package or directory structure yourself.

<!-- zh-CN:begin 88e3081d4cad08e7 -->

技能没有提供好答案。人们常要一份按这些原则展示具体文件和模块布局的 `TYPESCRIPT.md`，目前不存在。技能说明加深应放在哪里以及接缝后承载什么；包或目录结构仍需你自己设计。

<!-- zh-CN:end 88e3081d4cad08e7 -->

## It's working if

<!-- zh-CN:begin f833ae849857ad5c -->

## 正常表现

<!-- zh-CN:end f833ae849857ad5c -->

- The candidates name your domain's concepts, not invented class names: "the Order intake module," not "the FooBarHandler."

<!-- zh-CN:begin c9fdddb3f2396525 -->

- 候选用你的领域概念，而非臆造类名：“Order 接收模块”，而非“FooBarHandler”。

<!-- zh-CN:end c9fdddb3f2396525 -->
- The candidates are in files you edited recently, not in parts of the repo nobody touches.

<!-- zh-CN:begin cca6e241d3a50526 -->

- 候选位于近期编辑文件，而非无人触碰的仓库区域。

<!-- zh-CN:end cca6e241d3a50526 -->
- No code changed during the run. The only new file is the HTML report in your temp directory.

<!-- zh-CN:begin 0e9e20f1b0b3fb09 -->

- 运行期间没有改代码；唯一新文件是临时目录中的 HTML 报告。

<!-- zh-CN:end 0e9e20f1b0b3fb09 -->
- It stops after the report and asks which candidate you want. It does not continue on its own.

<!-- zh-CN:begin 2b9624da61a7c637 -->

- 报告后停下，询问选择哪项，不自行继续。

<!-- zh-CN:end 2b9624da61a7c637 -->
- Each card explains the payoff as locality or leverage, and says which tests get simpler, not just "this is cleaner."

<!-- zh-CN:begin b823609bbc19918a -->

- 每张卡用局部性或杠杆解释回报，并说明哪些测试更简单，而非只说“更干净”。

<!-- zh-CN:end b823609bbc19918a -->
- When you reject a candidate for a lasting reason, it offers to record an ADR, so the next run does not suggest it again.

<!-- zh-CN:begin ba042c2847da699e -->

- 因长期理由拒绝候选时，提议记录 ADR，避免下次重提。

<!-- zh-CN:end ba042c2847da699e -->

## Where it fits

<!-- zh-CN:begin 999252d9cd630c6f -->

## 所处位置

<!-- zh-CN:end 999252d9cd630c6f -->

`improve-codebase-architecture` is **periodic maintenance**. You run it every few days, outside any chain, to queue up work, not to do it. Its neighbours:

<!-- zh-CN:begin 7ecaf16ef7a05b7d -->

`improve-codebase-architecture` 属于**周期维护**。每隔几天在任何流程外运行，用于排队工作而非执行。相邻技能：

<!-- zh-CN:end 7ecaf16ef7a05b7d -->

- [codebase-design](https://aihero.dev/skills-codebase-design) owns the depth-and-seam vocabulary that every candidate uses.

<!-- zh-CN:begin 26aac8796f5384df -->

- [codebase-design](https://aihero.dev/skills-codebase-design) 提供所有候选使用的深度与接缝词汇。

<!-- zh-CN:end 26aac8796f5384df -->
- [grilling](https://aihero.dev/skills-grilling) walks the decision tree after you choose a candidate.

<!-- zh-CN:begin dad00e11696a1e31 -->

- [grilling](https://aihero.dev/skills-grilling) 在你选候选后遍历决策树。

<!-- zh-CN:end dad00e11696a1e31 -->
- [domain-modeling](https://aihero.dev/skills-domain-modeling) keeps `GLOSSARY.md` and the ADRs current as you make the decision.

<!-- zh-CN:begin a598ef56d550138a -->

- [domain-modeling](https://aihero.dev/skills-domain-modeling) 在决策过程中保持 `GLOSSARY.md` 与 ADR 最新。

<!-- zh-CN:end a598ef56d550138a -->

Its output is an idea, which goes back into the main build flow at [grill-with-docs](https://aihero.dev/skills-grill-with-docs) or [to-spec](https://aihero.dev/skills-to-spec). Its counterpart at the end of the main flow is [retro](https://aihero.dev/skills-retro). This skill improves the code the agent works in, and `retro` improves the environment around it (checks, standards, steering files) after a build. For which skill fits a situation, [ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set.

<!-- zh-CN:begin d52cb29025e36964 -->

输出是一个想法，通过 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 或 [to-spec](https://aihero.dev/skills-to-spec) 回到主构建流程。主流程末端的对应工具是 [retro](https://aihero.dev/skills-retro)：本技能改善代理工作的代码，`retro` 在构建后改善其周围环境（检查、标准、引导文件）。判断该用哪个时，[ask-matt](https://aihero.dev/skills-ask-matt) 是整套技能的路由器。

<!-- zh-CN:end d52cb29025e36964 -->
