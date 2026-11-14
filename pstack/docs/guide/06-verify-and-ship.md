# Verify the result and open a PR

<!-- zh-CN:begin 39082b23f78f5026 -->

# 验证结果并创建 PR

<!-- zh-CN:end 39082b23f78f5026 -->

"It compiles" is not evidence. The [Prove It Works principle](../../skills/principle-prove-it-works/SKILL.md) makes the agent check the real artifact before it reports success, and your job is to make "the real artifact" checkable. This page covers stating a finish condition, vetting a measured number, generating a verification skill for your app, formally verifying a property tests rarely reach, opening the PR, and driving it to merged.

<!-- zh-CN:begin be002b158848d944 -->

“能编译”不是证据。[证明它有效原则](../../skills/principle-prove-it-works/SKILL.md) 要求智能体在报告成功前检查真实产物，你的责任是让“真实产物”可以检查。本页介绍如何声明完成条件、审查测量数字、为应用生成验证技能、形式化验证测试很少触及的性质、创建 PR 并推动合并。

<!-- zh-CN:end be002b158848d944 -->

Verification is the slowest step in most agent work, because it's the step that usually waits on a human. Make the agent able to do it, and you stop being the bottleneck. Skip it, and running more agents only gets you more unchecked work to review.

<!-- zh-CN:begin 9f9a6e31f660829b -->

验证通常是智能体工作最慢的一步，因为这一步往往要等人。让智能体能自行验证，你就不再是瓶颈。跳过验证，运行更多智能体只会带来更多未经检查、等待你评审的工作。

<!-- zh-CN:end 9f9a6e31f660829b -->

![A prototype plane flies a real test course while she times it with a stopwatch and robots film and checklist the run; the terminal reads verify: pass, evidence: captured.](./images/verification.jpg)

<!-- zh-CN:begin 3647b5b0071944c0 -->

![一架原型飞机在真实测试航线上飞行，她用秒表计时，机器人拍摄并逐项检查；终端显示“验证：通过，证据：已捕获”。](./images/verification.jpg)

<!-- zh-CN:end 3647b5b0071944c0 -->

## State the finish condition up front

<!-- zh-CN:begin 41923dde01b73259 -->

## 提前声明完成条件

<!-- zh-CN:end 41923dde01b73259 -->

Put what done means in the first prompt, in whatever words fit:

<!-- zh-CN:begin e1d8c38289fc5499 -->

在第一条提示词中，用合适的措辞写明怎样才算完成：

<!-- zh-CN:end e1d8c38289fc5499 -->

```text
/poteto-mode add json output to this command. text output stays byte-identical, the json parses, both run against the sample project. show me the evidence.
```

<!-- zh-CN:begin db2d123c12f6814b -->

```text
/poteto-mode 给这个命令添加 json 输出。文本输出逐字节保持一致，json 能解析，两种输出都对示例项目运行。给我看证据。
```

<!-- zh-CN:end db2d123c12f6814b -->

Now the agent has three checks it can run, not a mood to satisfy. When the reply comes back, it should carry the exact commands and outputs. If a check couldn't run, a good reply says "inconclusive". A confident reply without evidence is a warning sign.

<!-- zh-CN:begin 4bf97cec2f12d2bd -->

现在智能体有三项可执行检查，而不是一种要满足的感觉。回复应包含精确命令和输出。某项无法运行时，好的回答会说“无法得出结论”。充满自信却没有证据的回复是警讯。

<!-- zh-CN:end 4bf97cec2f12d2bd -->

Match the check to the change:

<!-- zh-CN:begin 79984835d10139c3 -->

让检查与改动相匹配：

<!-- zh-CN:end 79984835d10139c3 -->

- A CLI change runs the real command.

<!-- zh-CN:begin 35518523952953dd -->

- CLI 改动运行真实命令。

<!-- zh-CN:end 35518523952953dd -->
- A UI change walks the changed flow in the running app. When it must match a reference pixel for pixel, the [Visual parity playbook](../../skills/poteto-mode/playbooks/visual-parity.md) diffs screenshots against a frozen baseline instead of judging by eye.

<!-- zh-CN:begin 782230b99a9a9dce -->

- UI 改动在运行中的应用里走一遍被修改的流程。需要与参考逐像素一致时，[视觉一致性手册](../../skills/poteto-mode/playbooks/visual-parity.md) 会将截图与冻结基线做差异比较，而非凭肉眼判断。

<!-- zh-CN:end 782230b99a9a9dce -->
- A parser or migration replays a saved input.

<!-- zh-CN:begin fb6cf61b1a3d2c13 -->

- 解析器或迁移重放保存的输入。

<!-- zh-CN:end fb6cf61b1a3d2c13 -->
- A perf change compares before and after profiles.

<!-- zh-CN:begin 07272bcd83b0acf8 -->

- 性能改动比较修改前后的性能分析结果。

<!-- zh-CN:end 07272bcd83b0acf8 -->
- A storage change reads back the written value.

<!-- zh-CN:begin 5b02813076b8ba12 -->

- 存储改动读回写入的值。

<!-- zh-CN:end 5b02813076b8ba12 -->

Ask for the proof as an artifact you can inspect yourself: the failing test and then the passing one, a before-and-after video, the trace, the screenshot. If the fix already merged, ask for the same check again on main. An artifact beats a plausible explanation, because you can challenge it without replaying the whole run.

<!-- zh-CN:begin c0270b3d010ab79a -->

要求提供你能亲自检查的证据产物：先失败再通过的测试、前后对比视频、跟踪记录或截图。若修复已合并，要求在 main 再做相同检查。产物胜过看似合理的解释，因为你能质疑它，而无需重演整个过程。

<!-- zh-CN:end c0270b3d010ab79a -->

For a small diff you don't fully trust, [`/blast-radius`](../../skills/blast-radius/SKILL.md) finds what it could break elsewhere. It finds the one fact that makes the change safe and proves that fact by running code, not by arguing for it.

<!-- zh-CN:begin 6089a2d31d1af80b -->

对于你不完全信任的小型差异，[`/blast-radius`](../../skills/blast-radius/SKILL.md) 会找出它可能破坏的其他地方。它寻找使改动安全的那项事实，并运行代码证明，而不是靠辩论。

<!-- zh-CN:end 6089a2d31d1af80b -->

## Vet a measured number with `/benchmark-checklist`

<!-- zh-CN:begin 8077573c62b62cf6 -->

## 用 `/benchmark-checklist` 审查测量数字

<!-- zh-CN:end 8077573c62b62cf6 -->

A before-and-after number is the easiest evidence to get wrong by accident. A warm cache, a debug build on one side, or work that never ran inside the timed region can each produce a convincing speedup. Before you report or act on a number, type:

<!-- zh-CN:begin a1aa7a95e4e95d89 -->

前后对比数字最容易无意中出错。热缓存、一侧使用调试构建、实际工作未在计时区间执行，都能产生看似可信的加速。报告数字或据此行动前，输入：

<!-- zh-CN:end a1aa7a95e4e95d89 -->

```text
/benchmark-checklist vet the export speedup before it goes in the pr
```

<!-- zh-CN:begin 3f5bdefa7f901f95 -->

```text
/benchmark-checklist 在把导出加速写进 pr 前，审查这个结果
```

<!-- zh-CN:end 3f5bdefa7f901f95 -->

[`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) asks seven questions and wants evidence from a run for each:

<!-- zh-CN:begin f087ddbaa78c9804 -->

[`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) 提出七个问题，每个问题都要求运行证据：

<!-- zh-CN:end f087ddbaa78c9804 -->

1. What limits the number, and why isn't it double?

<!-- zh-CN:begin 704d4a031d36d9e4 -->

1. 什么限制了这个数字，为什么不是它的两倍？

<!-- zh-CN:end 704d4a031d36d9e4 -->
2. Did every side run tuned the way production runs?

<!-- zh-CN:begin 71a65b95b48b56f0 -->

2. 每一侧是否都按生产运行方式调优？

<!-- zh-CN:end 71a65b95b48b56f0 -->
3. Does the result break a physical limit, like disk bandwidth or core count?

<!-- zh-CN:begin 138aeb0465465a36 -->

3. 结果是否突破磁盘带宽或核心数等物理限制？

<!-- zh-CN:end 138aeb0465465a36 -->
4. Did anything error or return wrong output?

<!-- zh-CN:begin 81af0e2d331076e9 -->

4. 是否有错误或错误输出？

<!-- zh-CN:end 81af0e2d331076e9 -->
5. Does it reproduce over alternating runs, with a median and a range?

<!-- zh-CN:begin f4c3307bf292f123 -->

5. 交替重复运行能否复现，是否有中位数和取值范围？

<!-- zh-CN:end f4c3307bf292f123 -->
6. Does it matter end to end, on the path a user waits on?

<!-- zh-CN:begin fbee62aad550a31e -->

6. 在用户等待的端到端路径上，这项变化是否有意义？

<!-- zh-CN:end fbee62aad550a31e -->
7. Did the work actually happen inside the timed region?

<!-- zh-CN:begin 3c5ac8ff03b81c46 -->

7. 工作是否确实在计时区间内发生？

<!-- zh-CN:end 3c5ac8ff03b81c46 -->

The verdict comes back as faster, slower, no measurable difference, or inconclusive, with the run count, range, and limiter. It says inconclusive when it can't name the limiter or a side ran untuned. `/poteto-mode` already runs the checklist inside the Perf issue and Hillclimb playbooks, so you type it yourself when you measured something outside them, or when someone else's number looks too good. It's the working form of the [Explain the Number principle](../../skills/principle-explain-the-number/SKILL.md).

<!-- zh-CN:begin 60b23a1b0e038951 -->

结论会是更快、更慢、无可测差异或无法得出结论，并附运行次数、范围和限制因素。无法说明限制因素或某侧未经调优时，会判定无法得出结论。`/poteto-mode` 已在性能问题和爬山优化手册内部运行该清单；你在这些手册外测量，或觉得别人的数字好得可疑时，再自行输入它。这就是[解释数字原则](../../skills/principle-explain-the-number/SKILL.md) 的实际用法。

<!-- zh-CN:end 60b23a1b0e038951 -->

## Create a project verification skill

<!-- zh-CN:begin 7d2369d37be13cda -->

## 创建项目验证技能

<!-- zh-CN:end 7d2369d37be13cda -->

The UI bullet above hides a real requirement. The agent needs a scripted way to drive your app. If your project has one, great. If not, run:

<!-- zh-CN:begin 93185239334c15c1 -->

上述 UI 项背后有个实际要求：智能体需要脚本化驱动应用的方式。项目已有就很好；没有则运行：

<!-- zh-CN:end 93185239334c15c1 -->

```text
/create-verification-skill
```

[`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) interviews the repository, not you. It works out what a user touches, how the app launches locally, what can drive it (an existing harness first, otherwise browser and CDP, a PTY, or plain HTTP), what evidence proves behavior, and whether two instances can run side by side. It asks you only what the code can't answer.

<!-- zh-CN:begin 4c1cf5f465a11c88 -->

[`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) 调查的是仓库，而不是你。它弄清用户接触什么、应用如何本地启动、什么能驱动它（优先用已有测试框架，否则用浏览器与 CDP、PTY 或普通 HTTP）、什么证据能证明行为，以及两个实例能否并排运行。它只问代码无法回答的问题。

<!-- zh-CN:end 4c1cf5f465a11c88 -->

It writes `.cursor/skills/verify-<app>/`, agent-facing instructions with exact Launch, Doctor, Drive, Evidence, and Cleanup sections, a Helpers section for any script it ships, plus a feature map under `features/` that indexes what the app does and what result proves each feature works. The skill ships a [worked feature-map example](../../skills/create-verification-skill/references/feature-map-example/) with a README index and one file per feature using the four required H2s. Before handing it over, the generator proves the skill once end to end: launch, doctor check, drive one feature, capture evidence, clean up, then confirm the evidence survived the cleanup. If that proof fails, don't use the output.

<!-- zh-CN:begin 7972e0b6d4cac45f -->

它写入 `.cursor/skills/verify-<app>/`，提供面向智能体、明确分为启动、诊断、驱动、证据、清理的指令；交付脚本时还包含辅助工具部分，并在 `features/` 下提供功能映射，索引应用功能及证明各项有效的结果。技能附带[完整功能映射示例](../../skills/create-verification-skill/references/feature-map-example/)，包括 README 索引和每功能一个文件，均使用四个必需的 H2 标题。交付前，生成器会端到端证明技能一次：启动、诊断检查、驱动一个功能、捕获证据、清理，再确认证据在清理后仍保留。证明失败就不要使用产物。

<!-- zh-CN:end 7972e0b6d4cac45f -->

From then on, "verify it in the app" is a step any agent can execute, in this repo, with no setup conversation. Name it in the prompt when you want the proof in a specific form:

<!-- zh-CN:begin 05b99a547d26fafc -->

此后，在本仓库中，“到应用里验证”便成为任何智能体都能执行的步骤，无需再讨论设置。需要特定证据形式时，在提示词里点名它：

<!-- zh-CN:end 05b99a547d26fafc -->

```text
/poteto-mode build the bulk-archive action. use /verify-<app> to verify your changes and show me a video and screenshots as proof.
```

<!-- zh-CN:begin 6d7fa2e7bde85538 -->

```text
/poteto-mode 构建批量归档操作。用 /verify-<app> 验证改动，给我视频和截图作为证据。
```

<!-- zh-CN:end 6d7fa2e7bde85538 -->

```text
/poteto-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.
```

<!-- zh-CN:begin 905794e9fb9ced38 -->

```text
/poteto-mode 用 /verify-<app> 复现这个问题。如果在 main 上复现，就修复它并给我视频证据。
```

<!-- zh-CN:end 905794e9fb9ced38 -->

Once the verify skill works, a [`/swarm`](../../skills/swarm/SKILL.md) can split a full pass by feature-map entry and aggregate the results. A swarm of verifiers also confirms a perf win over a big enough sample, or fuzzes the app for regressions before a PR ships.

<!-- zh-CN:begin cc39be08e05fcecd -->

验证技能有效后，[`/swarm`](../../skills/swarm/SKILL.md) 可按功能映射条目拆分一次完整检查并汇总结果。验证者工作群也可用足够大的样本确认性能提升，或在 PR 交付前对应用做模糊测试，查找回归。

<!-- zh-CN:end cc39be08e05fcecd -->

Treat the verification skill as infrastructure, not a one-off. Commit it, so every person and every agent on the team drives the app the same way. Then [build the lever](../../skills/principle-build-the-lever/SKILL.md). When agents keep writing throwaway scripts to click through the app, ask for a small control CLI that the skill calls instead. Agents spend fewer tokens, and every run becomes repeatable. A CLI that agents use well has these traits:

<!-- zh-CN:begin 82c3c00c3abc5664 -->

把验证技能视为基础设施，而非一次性工作。将它提交，让团队每个人和每个智能体以同样方式驱动应用。然后[构建杠杆](../../skills/principle-build-the-lever/SKILL.md)。智能体不断编写一次性脚本点击应用时，要求制作小型控制 CLI，供技能调用。这样更省词元，每次运行也可重复。适合智能体的 CLI 具备以下特征：

<!-- zh-CN:end 82c3c00c3abc5664 -->

- A few composable commands, each doing real work, rather than many thin ones.

<!-- zh-CN:begin 8d903dd267aff4e1 -->

- 少量可组合、各自完成实际工作的命令，而非大量单薄命令。

<!-- zh-CN:end 8d903dd267aff4e1 -->
- A `--dry-run` option on anything destructive.

<!-- zh-CN:begin 83d3499f88e4a361 -->

- 任何破坏性操作都提供 `--dry-run` 选项。

<!-- zh-CN:end 83d3499f88e4a361 -->
- Subcommands that reveal features gradually instead of all at once.

<!-- zh-CN:begin bf614bb51e4bb594 -->

- 子命令逐渐揭示功能，而非一次展示全部。

<!-- zh-CN:end bf614bb51e4bb594 -->
- Error messages that say what to do instead.

<!-- zh-CN:begin 2a4e021cef2a4ff8 -->

- 错误消息说明应该改做什么。

<!-- zh-CN:end 2a4e021cef2a4ff8 -->
- Rich `--help` text.

<!-- zh-CN:begin d35681610c11644f -->

- 丰富的 `--help` 文本。

<!-- zh-CN:end d35681610c11644f -->
- Machine-readable output, such as JSON.

<!-- zh-CN:begin 34021a2c28fd0770 -->

- JSON 等机器可读输出。

<!-- zh-CN:end 34021a2c28fd0770 -->

While you're there, make the dev setup repeatable too: seeded data, test users, and one command that brings the environment up the same way every time.

<!-- zh-CN:begin 80677f628451a59a -->

同时也让开发设置可重复：预置数据、测试用户，以及每次以相同方式启动环境的一条命令。

<!-- zh-CN:end 80677f628451a59a -->

## Keep the verification skill honest

<!-- zh-CN:begin 1f3be741f6421d9f -->

## 确保验证技能保持真实

<!-- zh-CN:end 1f3be741f6421d9f -->

Apps change, and feature maps go out of date. Run this at least once a day, ideally from a scheduled automation so nobody has to remember:

<!-- zh-CN:begin 368a128891d2b030 -->

应用会变，功能映射会过时。至少每天运行一次，最好配置定时自动化，免得靠人记住：

<!-- zh-CN:end 368a128891d2b030 -->

```text
/maintain-verification-skill
```

[`/maintain-verification-skill`](../../skills/maintain-verification-skill/SKILL.md) audits the generated skill: one read-only source reader per feature in parallel, then one live pass that drives every mapped feature. It ends in exactly one of three outcomes. `clean` means full coverage and nothing to ship. `changed` means one PR of proven corrections, confined to the verification skill's own directory. `blocked` names the blocker. It never edits product code. If the live pass catches a product regression, it reports the regression instead of hiding it with a doc edit.

<!-- zh-CN:begin f440de53efc9f8c7 -->

[`/maintain-verification-skill`](../../skills/maintain-verification-skill/SKILL.md) 审计生成的技能：每个功能各派一个只读源码阅读者并行检查，再实际驱动所有映射功能一遍。最终恰好三种结果之一：`clean` 表示覆盖完整、无需交付；`changed` 表示提交一个包含已证明更正的 PR，范围限于验证技能自己的目录；`blocked` 会点明阻碍。它绝不编辑产品代码。实际检查若发现产品回归，会报告回归，而不是靠修改文档掩盖。

<!-- zh-CN:end f440de53efc9f8c7 -->

## Prove a property with a formal verification skill

<!-- zh-CN:begin de95d099968fa086 -->

## 用形式化验证技能证明性质

<!-- zh-CN:end de95d099968fa086 -->

A verification skill proves the paths you drive. Some bugs live on paths nobody drives: two retries that overlap, a lock that expires mid-write, a state change that arrives out of order. Tests rarely reach those cases. For code where such a bug is costly, run:

<!-- zh-CN:begin 7c3953951335ed29 -->

验证技能证明你实际驱动过的路径。有些缺陷藏在没人驱动的路径上：两次重试重叠、写入中途锁过期、状态变化乱序到达。测试很少触及这些情况。如果此类缺陷在代码中代价很高，运行：

<!-- zh-CN:end 7c3953951335ed29 -->

```text
/create-formal-verification-skill
```

[`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md) picks the target from the code: a promise the code makes, where a break harms users and tests rarely reach the case that breaks it. It picks the strongest target, not the easiest to verify. Name an area or a bug to start there instead:

<!-- zh-CN:begin 2094a3bcf05016a6 -->

[`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md) 从代码中挑选目标：代码作出的某项承诺，违背时会伤害用户，而测试很少触及破坏它的情况。它选择最重要的目标，而非最容易验证的目标。也可指定区域或缺陷作为起点：

<!-- zh-CN:end 2094a3bcf05016a6 -->

```text
/create-formal-verification-skill the job lease and retry logic. a job must never run twice at once.
```

<!-- zh-CN:begin 4d3f7d2955f23dbd -->

```text
/create-formal-verification-skill 任务租约和重试逻辑。同一个任务绝不能同时运行两次。
```

<!-- zh-CN:end 4d3f7d2955f23dbd -->

The question picks the tool. Whether events can happen in a bad order suits a model checker over a small model of the design, and TLA+ is the default for that in any language. Whether the code behaves for every input suits a verifier that runs on the code. If no verifier runs on your language, the agent says so and tests the real code with generated inputs, not a hand-written model of the function. A property that must hold at every size can need a proof. The agent tells you which tool it chose and why.

<!-- zh-CN:begin 5c61ee20f2065174 -->

问题决定工具。事件是否可能按有害顺序发生，适合用模型检查器检查设计的小型模型；对于任何语言，默认选择 TLA+。代码是否对每个输入都正确，适合直接作用于代码的验证器。若你的语言没有可用验证器，智能体会说明，并用生成的输入测试真实代码，而非手写函数模型。必须对任意规模成立的性质，可能需要证明。智能体会说明选择了什么工具以及原因。

<!-- zh-CN:end 5c61ee20f2065174 -->

It verifies one property and shows that property failing on a broken variant of the code, because a check you've never seen fail proves nothing. When the current code already breaks the property, you get the counterexample as a short sequence of steps in your code's terms. The property stays as stated, so the finding stays a finding. Product code doesn't change unless you ask.

<!-- zh-CN:begin ec863914f3917504 -->

它验证一个性质，并展示该性质在故意破坏的代码变体上失败，因为从未见过失败的检查不能证明任何事。当前代码已违反性质时，你会得到以代码术语表述的简短步骤反例。性质保持原样，使发现仍然成立。未经你要求，不改产品代码。

<!-- zh-CN:end ec863914f3917504 -->

It writes a project-local skill that tells the next agent whether a change touches the verified code, how to run the check with one command, and how to tell a real bug from a modeling error. Before handing it over, the generator follows that skill once on a scratch change that breaks the property, and the check must catch it. The handoff says what was verified, with which tool and bounds, what the check found, and what it doesn't cover. A pass covers the model or the bound, not the whole system.

<!-- zh-CN:begin a01812c1c914fd52 -->

它编写项目本地技能，告诉下一个智能体如何判断改动是否触及已验证代码、如何用一条命令检查，以及如何区分真实缺陷与建模错误。交付前，生成器会按技能流程对临时破坏性质的改动执行一次，检查必须捕获它。交接说明验证了什么、工具与边界、检查结果以及未覆盖内容。通过只覆盖模型或给定边界，并不覆盖整个系统。

<!-- zh-CN:end a01812c1c914fd52 -->

The skill also records which code each check covers and the commit where the check last matched it. Merges and refactors that skip the skill can leave the check passing on a description of code that's gone. After them, run [`/maintain-formal-verification-skill`](../../skills/maintain-formal-verification-skill/SKILL.md). It updates the verification from the code, reruns it, shows that each updated check can still fail, and tells you whether each failure is drift in the verification or a bug in the code.

<!-- zh-CN:begin df5839ae2c019ebb -->

技能还记录每项检查覆盖哪些代码，以及检查最后与代码一致时的提交。绕过技能的合并和重构可能让检查仍在验证已经不存在的代码描述，并一直通过。这些操作后运行 [`/maintain-formal-verification-skill`](../../skills/maintain-formal-verification-skill/SKILL.md)。它根据代码更新验证、重新运行、展示每项更新后的检查仍可失败，并说明每次失败是验证偏移还是代码缺陷。

<!-- zh-CN:end df5839ae2c019ebb -->

## Show the behavior as a statechart

<!-- zh-CN:begin 87912f9053d8d8bd -->

## 用状态图展示行为

<!-- zh-CN:end 87912f9053d8d8bd -->

A counterexample in model terms convinces you. The PM or designer who owns the behavior needs to see it in their terms. Run:

<!-- zh-CN:begin 183b1d19dd0463b2 -->

模型术语表达的反例能说服你，但负责行为的产品经理或设计师需要用他们的术语看懂。运行：

<!-- zh-CN:end 183b1d19dd0463b2 -->

```text
/statechart what the user sees when they edit a note offline
```

<!-- zh-CN:begin 14927d2485e03864 -->

```text
/statechart 用户离线编辑笔记时会看到什么
```

<!-- zh-CN:end 14927d2485e03864 -->

[`/statechart`](../../skills/statechart/SKILL.md) draws a Mermaid statechart of what the user sees, generated from a TLA+ model, so the picture and the checked model can't drift apart. The reader's rules ("you never see Synced while you're offline") become invariants. The chart marks each state that breaks a rule, and the report gives the shortest path to it in the reader's words. Before the hand-off, the agent reproduces each bug path in the real code, so a modeling error doesn't reach the reader as a bug.

<!-- zh-CN:begin c386260a15c8d23b -->

[`/statechart`](../../skills/statechart/SKILL.md) 根据 TLA+ 模型生成描述用户所见的 Mermaid 状态图，让图与已检查模型不会偏离。读者的规则（“离线时绝不会看到已同步”）成为不变量。图标记每个违反规则的状态，报告用读者的语言给出到达它的最短路径。交接前，智能体在真实代码中复现每条缺陷路径，避免把建模错误作为缺陷呈交读者。

<!-- zh-CN:end c386260a15c8d23b -->

## Open the PR

<!-- zh-CN:begin 8c0bf107a6c87437 -->

## 创建 PR

<!-- zh-CN:end 8c0bf107a6c87437 -->

```text
/poteto-mode open the pr. small ordered commits, evidence in the description.
```

<!-- zh-CN:begin dee040e5bdee28f8 -->

```text
/poteto-mode 创建 pr。提交要小且有序，描述里附证据。
```

<!-- zh-CN:end dee040e5bdee28f8 -->

The [Opening a PR playbook](../../skills/poteto-mode/playbooks/opening-a-pr.md) works from a worktree, rebases the work into small ordered commits, cleans the diff, unslops the prose, and returns the PR link. Five narrow PRs beat one fat one, and stacked follow-ups beat a growing branch.

<!-- zh-CN:begin 96becff389a42e50 -->

[创建 PR 手册](../../skills/poteto-mode/playbooks/opening-a-pr.md) 从工作树开始，把工作变基为小而有序的提交，清理差异和文字，最后返回 PR 链接。五个范围窄的 PR 胜过一个臃肿 PR，堆叠后续 PR 胜过不断膨胀的分支。

<!-- zh-CN:end 96becff389a42e50 -->

## Drive the PR to merge-ready with Babysit

<!-- zh-CN:begin 25059c29339640f8 -->

## 用 Babysit 推动 PR 达到可合并状态

<!-- zh-CN:end 25059c29339640f8 -->

An open PR starts collecting blockers immediately. Checks fail, reviewers comment, trunk moves. Hand that churn to the [Babysit playbook](../../skills/poteto-mode/playbooks/babysit.md):

<!-- zh-CN:begin b7188baf87ec4dfe -->

PR 一创建便开始积累阻碍：检查失败、评审者留言、主干前移。将这些反复变动交给[看护手册](../../skills/poteto-mode/playbooks/babysit.md)：

<!-- zh-CN:end b7188baf87ec4dfe -->

```text
/poteto-mode babysit this pr. get it green.
```

<!-- zh-CN:begin 300981feb2e3636e -->

```text
/poteto-mode 看护这个 pr，让检查全部通过。
```

<!-- zh-CN:end 300981feb2e3636e -->

Babysit watches the PR, with a bundled watcher on GitHub or the Origin CLI when it's available, and takes blockers in order: conflicts, then review threads, then CI. Every known fix batches into one push, so the checks restart once instead of after every fix. The comment triage is skeptical, because humans and bots file real catches and noise in the same list. A real finding gets a fix, and noise gets dismissed with the disproof posted on the thread. When all you want is status, ask smaller and Babysit answers without starting the loop:

<!-- zh-CN:begin 7bf3d25b861afaa1 -->

Babysit 使用内置 GitHub 监视器，或可用时的 Origin CLI 观察 PR，依次处理冲突、评审讨论、CI。所有已知修复汇成一次推送，让检查只重启一次，而不是每修一次就重启。它谨慎分流评论，因为人和机器人都会在同一列表提交真实发现和噪声。真实问题得到修复，噪声则用讨论中发布的反证驳回。只想知道状态时，缩小要求，Babysit 会直接回答而不启动循环：

<!-- zh-CN:end 7bf3d25b861afaa1 -->

```text
/poteto-mode check on pr 123. anything outstanding?
```

<!-- zh-CN:begin 292bbf8f2fe3bb2c -->

```text
/poteto-mode 检查 pr 123，还有什么未完成？
```

<!-- zh-CN:end 292bbf8f2fe3bb2c -->

Babysit stops at merge-ready. It never merges, even with everything green, because merging is a different decision.

<!-- zh-CN:begin 50485925877d384f -->

Babysit 到可合并状态即停止。即使全部通过，它也从不合并，因为合并是另一项决策。

<!-- zh-CN:end 50485925877d384f -->

## Land the stack with Shipping

<!-- zh-CN:begin 0563b81c212cd3d8 -->

## 用 Shipping 落地 PR 栈

<!-- zh-CN:end 0563b81c212cd3d8 -->

Green is not the same as safe. When you're ready to land, say so:

<!-- zh-CN:begin f00735a05bdbe91b -->

全部通过不等于安全。准备落地时，明确说：

<!-- zh-CN:end f00735a05bdbe91b -->

```text
/poteto-mode land the stack.
```

<!-- zh-CN:begin e4aaeeddbeaa3691 -->

```text
/poteto-mode 落地这组堆叠 PR。
```

<!-- zh-CN:end e4aaeeddbeaa3691 -->

The [Shipping playbook](../../skills/poteto-mode/playbooks/shipping.md) verifies each PR independently before it arms anything. One fresh agent per PR proves the behavior live, and the agent that judges a change is never the one that wrote it. Then Shipping lands only the contiguous verified run from the bottom, one PR at a time through GitHub by default or Origin when its CLI is available, and reports the first PR that breaks the chain. A verified PR sitting above an unverified one waits, because merging it would pull the gap in underneath.

<!-- zh-CN:begin 736361335c45d93d -->

[交付手册](../../skills/poteto-mode/playbooks/shipping.md) 在启用任何合并操作前独立验证每个 PR。每个 PR 使用一个全新智能体实际证明行为，评判改动的智能体绝不是编写者。随后仅从底部开始逐个落地连续验证通过的 PR，默认通过 GitHub，可用时也使用 Origin CLI，并报告第一个打断连续链条的 PR。已验证 PR 若位于未验证 PR 之上，就必须等待，因为合并它会把下方验证缺口一并带入。

<!-- zh-CN:end 736361335c45d93d -->

Next: [Run work while you sleep](./07-overnight.md).

<!-- zh-CN:begin 3868d229a993c9a7 -->

下一步：[在你睡觉时运行工作](./07-overnight.md)。

<!-- zh-CN:end 3868d229a993c9a7 -->
