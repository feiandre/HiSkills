## What it does

<!-- zh-CN:begin 3c2b492b1d2d4357 -->

## 它做什么

<!-- zh-CN:end 3c2b492b1d2d4357 -->

`diagnosing-bugs` runs a six-phase diagnosis on a hard bug or a performance regression: build a repro, minimise it, rank hypotheses, instrument, fix with a regression test, clean up.

<!-- zh-CN:begin b34482bc19a5fd09 -->

`diagnosing-bugs` 对困难缺陷或性能回归执行六阶段诊断：建立复现、最小化复现、给假设排序、插桩、用回归测试进行修复、清理。

<!-- zh-CN:end b34482bc19a5fd09 -->

It will not let the agent form a theory until a **tight** feedback loop exists: one named command, already run once, that goes red on *this* bug and green when it is fixed. Given a bug report, a coding agent by default reads code and guesses. This skill blocks that. If no red-capable command exists, there is no Phase 2. That single gate is what the skill is for. Once the loop exists, everything after it (bisection, hypothesis-testing, instrumentation) is mechanical.

<!-- zh-CN:begin c3742c3c4d2f0c1c -->

在存在**紧密**反馈循环之前，它不允许智能体形成理论：一个已运行过一次的具名命令，会在这个缺陷上变红，并在修复后变绿。收到缺陷报告时，编码智能体默认会阅读代码并猜测。本技能阻止这种行为。如果没有能产生红色结果的命令，就没有第 2 阶段。那道门控正是该技能存在的意义。循环建立后，后面的一切（二分查找、假设检验、插桩）都是机械操作。

<!-- zh-CN:end c3742c3c4d2f0c1c -->

## When to reach for it

<!-- zh-CN:begin 40bcdeefd6ebad4b -->

## 何时使用

<!-- zh-CN:end 40bcdeefd6ebad4b -->

Type `/diagnosing-bugs`, or the agent reaches for it on its own when a task fits. It is model-invoked, and fires on "diagnose" or "debug this", or on a report that something is broken, throwing, failing, or slow.

<!-- zh-CN:begin ce86bd0e92e6f484 -->

输入 `/diagnosing-bugs`，或任务适合时让智能体自行选择。它由模型调用，会在“诊断”或“调试这个”时触发，也会在报告某物损坏、抛异常、失败或很慢时触发。

<!-- zh-CN:end ce86bd0e92e6f484 -->

Reach for it on the hard ones: a bug you can't solve at first look, an intermittent flake, a regression introduced between two known-good states. It is slow and thorough on purpose, so it is the wrong tool for a question you want answered in one message.

<!-- zh-CN:begin f51c73e638f30e21 -->

困难场景应使用它：第一眼解决不了的缺陷、间歇性偶发失败、两个已知良好状态之间引入的回归。它刻意缓慢而彻底，因此不适合你希望一条消息就得到答案的问题。

<!-- zh-CN:end f51c73e638f30e21 -->

| Your situation | Where to go |
| --- | --- |
| A specific defect you can describe as a symptom | This skill |
| A slow endpoint or a timing regression with a known before-and-after | This skill. It has a performance branch (measure a baseline, then bisect) |
| "Where are the bottlenecks in this codebase?", no specific symptom | Not this skill. It diagnoses one known failure, it does not audit |
| A raw bug report from someone else, not yet confirmed or written up | [triage](https://aihero.dev/skills-triage) first |
| Throwaway code to answer a design question, not chase a defect | [prototype](https://aihero.dev/skills-prototype) |
| Building a planned behaviour test-first | [tdd](https://aihero.dev/skills-tdd) |
| Asking what would have prevented the bug, once it is fixed | [retro](https://aihero.dev/skills-retro), run in the same session |
| No good seam exists to lock the bug down | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture), which you start yourself |

<!-- zh-CN:begin 41020c217e98abb0 -->

| 你的情况 | 应使用 |
| --- | --- |
| 可以描述为症状的具体缺陷 | 本技能 |
| 已知修改前后情况的缓慢端点或时序回归 | 本技能。它有性能分支（测量基线，再二分） |
| “这个代码库的瓶颈在哪里？”，没有具体症状 | 不是本技能。它诊断一个已知故障，不做全面审计 |
| 来自他人、尚未确认或整理的原始缺陷报告 | 先使用[分诊](https://aihero.dev/skills-triage) |
| 为回答设计问题而写一次性代码，不追查缺陷 | [原型](https://aihero.dev/skills-prototype) |
| 按测试优先构建计划好的行为 | [tdd](https://aihero.dev/skills-tdd) |
| 缺陷修复后询问什么本可防止它 | [回顾](https://aihero.dev/skills-retro)，在同一会话中运行 |
| 没有合适接缝来锁定该缺陷 | [改进代码库架构](https://aihero.dev/skills-improve-codebase-architecture)，由你自行启动 |

<!-- zh-CN:end 41020c217e98abb0 -->

## The tight loop is the skill

<!-- zh-CN:begin 0aaf21eecda68e4a -->

## 紧密循环就是技能核心

<!-- zh-CN:end 0aaf21eecda68e4a -->

Phase 1 gets the most effort because it is the only hard phase. The skill lists ways to build the loop, roughly in order of preference:

<!-- zh-CN:begin d847a11f6b78aa67 -->

第 1 阶段投入最多，因为它是唯一困难阶段。技能列出建立循环的方法，大致按优先级排序：

<!-- zh-CN:end d847a11f6b78aa67 -->

1. A failing test at whatever seam reaches the bug.

<!-- zh-CN:begin ffffa871ae52342c -->

1. 在能够触及缺陷的任意接缝处编写失败测试。

<!-- zh-CN:end ffffa871ae52342c -->
2. A curl or HTTP script against a running dev server.

<!-- zh-CN:begin 73a47b2785100ffd -->

2. 针对运行中的开发服务器编写 curl 或 HTTP 脚本。

<!-- zh-CN:end 73a47b2785100ffd -->
3. A CLI invocation with a fixture input, diffed against a known-good snapshot.

<!-- zh-CN:begin d49ad425c52db814 -->

3. 使用夹具输入执行 CLI 调用，并与已知良好快照比较。

<!-- zh-CN:end d49ad425c52db814 -->
4. A headless browser script asserting on DOM, console, or network.

<!-- zh-CN:begin a3052a900f15e823 -->

4. 对 DOM、控制台或网络作断言的无头浏览器脚本。

<!-- zh-CN:end a3052a900f15e823 -->
5. A replayed capture: a saved request, payload, or event log, run through the code path in isolation.

<!-- zh-CN:begin c647ff6cbe7132ca -->

5. 重放捕获内容：保存的请求、载荷或事件日志，在隔离的代码路径中运行。

<!-- zh-CN:end c647ff6cbe7132ca -->
6. A throwaway harness: a minimal subset of the system, one function call.

<!-- zh-CN:begin ba913e7cbede2a73 -->

6. 一次性测试框架：系统的最小切片，只调用一个函数。

<!-- zh-CN:end ba913e7cbede2a73 -->
7. A property or fuzz loop, for "sometimes wrong output".

<!-- zh-CN:begin a5a7af2a8ad778dd -->

7. 属性或模糊循环，用于“有时输出错误”。

<!-- zh-CN:end a5a7af2a8ad778dd -->
8. A bisection harness you can hand to `git bisect run`.

<!-- zh-CN:begin faa4552f3a2f5be6 -->

8. 可交给 `git bisect run` 的二分测试框架。

<!-- zh-CN:end faa4552f3a2f5be6 -->
9. A differential loop: same input, old version against new.

<!-- zh-CN:begin 7b622debd8e9f7fd -->

9. 差分循环：相同输入，旧版本与新版本比较。

<!-- zh-CN:end 7b622debd8e9f7fd -->
10. A [human-in-the-loop](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop) bash script, last resort. The skill ships `scripts/hitl-loop.template.sh` for this: the agent runs the script, you follow prompts in your terminal, and your answers come back as parseable output.

<!-- zh-CN:begin 585669ecff0b501b -->

10. [人在回路](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop) bash 脚本，作为最后手段。技能附带 `scripts/hitl-loop.template.sh`：智能体运行脚本，你在终端按提示操作，回答以可解析输出返回。

<!-- zh-CN:end 585669ecff0b501b -->

*A* loop is not the goal. **Tight** is: fast (seconds), deterministic (same verdict every run), sharp (asserts your exact symptom, not "didn't crash"), and runnable by the agent without you. A 30-second flaky loop is barely better than none. For a bug that only shows up sometimes, the target is not a clean repro but a **higher reproduction rate**: loop the trigger, parallelise, add stress, inject sleeps, until the flake rate is high enough to debug against.

<!-- zh-CN:begin a1b1bfc7b5167b8d -->

目标不是建立*某个*循环，而是建立**紧密**循环：快速（数秒）、确定性（每次结论相同）、精确（断言你的确切症状，而非“没有崩溃”），并且无需你介入就能由智能体运行。30 秒且偶发失败的循环比没有循环好不了多少。对于只偶尔出现的缺陷，目标不是干净复现，而是**提高复现率**：循环触发、并行执行、增加压力、注入等待，直到偶发率足够高、可以据此调试。

<!-- zh-CN:end a1b1bfc7b5167b8d -->

When the agent cannot build one, the skill tells it to stop and say so, list what it tried, and ask you for [environment](https://www.aihero.dev/ai-coding-dictionary/environment) access, a captured artifact, or permission to add temporary instrumentation. It must not go on to form hypotheses anyway.

<!-- zh-CN:begin ee2662533f231e71 -->

智能体无法建立循环时，技能要求它停下来说明情况、列出尝试过的方法，并请求[环境](https://www.aihero.dev/ai-coding-dictionary/environment)访问、捕获产物，或添加临时插桩的许可。它绝不能继续形成假设。

<!-- zh-CN:end ee2662533f231e71 -->

## The gates between phases

<!-- zh-CN:begin d98c5e4d63a5d079 -->

## 阶段之间的门控

<!-- zh-CN:end d98c5e4d63a5d079 -->

The phases are gates, not a checklist. The agent cannot enter a phase until a specific condition is true.

<!-- zh-CN:begin 7aded4883a88cdce -->

这些阶段是门控，不是检查清单。特定条件成立前，智能体不能进入下一阶段。

<!-- zh-CN:end 7aded4883a88cdce -->

| Gate | What has to be true |
| --- | --- |
| Into Phase 2 | A named command, already run and pasted with its output, that can go red on this bug |
| Into Phase 3 | The repro is reproduced *and* minimised: every remaining element is needed to reproduce the bug |
| Into Phase 4 | 3–5 ranked, falsifiable hypotheses exist, each stating its prediction, shown to you before any is tested |
| Into Phase 5 | Probes map to a specific prediction, one variable at a time, every debug log has a tag like `[DEBUG-a4f2]`, so one grep finds them all for cleanup |
| Done | The original repro no longer reproduces, the instrumentation is gone, and the commit message names the hypothesis that turned out correct |

<!-- zh-CN:begin eed255f474048213 -->

| 门控 | 必须成立的条件 |
| --- | --- |
| 进入第 2 阶段 | 一个已运行且粘贴了输出的具名命令，它能在此缺陷上变红 |
| 进入第 3 阶段 | 缺陷已复现*并且*已最小化：每个剩余元素都是复现所必需的 |
| 进入第 4 阶段 | 存在 3–5 个有排序、可证伪的假设，每个都给出预测，并在任何测试前向你展示 |
| 进入第 5 阶段 | 探针对应特定预测，一次只改变一个变量；每个调试日志都有 `[DEBUG-a4f2]` 一类标签，方便一次 grep 全部找到并清理 |
| 完成 | 原始复现不再出现，插桩已移除，提交消息写明最终正确的假设 |

<!-- zh-CN:end eed255f474048213 -->

Phase 5 has one exception. The agent writes the regression test before the fix, but only if a **correct seam** exists for it: one where the test exercises the real bug pattern as it occurs at the call site. Where the only available seam is too shallow, the skill tells the agent to say so instead of writing a test that gives false confidence. The missing seam is itself a finding, and the agent records it instead of hiding it.

<!-- zh-CN:begin 13b163ff12ab0230 -->

第 5 阶段有一个例外。智能体在修复前编写回归测试，但前提是存在**正确接缝**：测试在该接缝上按调用位置发生的真实缺陷模式执行。唯一可用接缝太浅时，技能要求智能体明确说明，而不是编写给出虚假信心的测试。缺少接缝本身就是发现，智能体应记录它，而不是掩盖它。

<!-- zh-CN:end 13b163ff12ab0230 -->

## Common questions

<!-- zh-CN:begin 7b6ef9f697a77a8b -->

## 常见问题

<!-- zh-CN:end 7b6ef9f697a77a8b -->

**It fires on quick questions where I just wanted a direct answer.**
This is the most-reported problem with the skill. On GPT-5.6-Sol especially, users report it triggering on a plain description of a problem: "the model triggers the rather formal diagnosing-bugs skill instead. It then goes on to construct a reproduction scenario (often building a mock scenario with limited value) before giving me a response or suggestion. This results in considerable reply delays." Four separate people reported the same problem on [issue #578](https://github.com/mattpocock/skills/issues/578). The accepted fix is to start with a lighter approach and move to the full diagnosis only when the problem needs it, but that change has not shipped. The skill is tuned for Claude Code's invocation behaviour, and a [model](https://www.aihero.dev/ai-coding-dictionary/model) with a lower activation threshold fires it too often. Until the fix ships, the workaround is to say what you want ("just answer this, don't diagnose") or to disable model invocation for it in your [harness](https://www.aihero.dev/ai-coding-dictionary/harness).

<!-- zh-CN:begin 88acac4f2758b87e -->

**它会在我只想要直接答案的快速问题上触发。**
这是本技能被报告最多的问题。尤其在 GPT-5.6-Sol 上，用户报告它会在普通问题描述上触发：“模型反而触发了相当正式的 diagnosing-bugs 技能。随后它构建复现场景（通常是价值有限的模拟场景），然后才给我回答或建议。这导致回复明显延迟。”有四位不同的人在[问题 #578](https://github.com/mattpocock/skills/issues/578) 报告相同问题。已接受的修复是先采用更轻量的方法，只有问题确实需要时才进入完整诊断，但该改动尚未发布。技能针对 Claude Code 的调用行为调校，激活阈值较低的[模型](https://www.aihero.dev/ai-coding-dictionary/model)会触发得太频繁。修复发布前，可明确说明需求（“直接回答，不要诊断”），或在[宿主](https://www.aihero.dev/ai-coding-dictionary/harness)中禁用模型调用。

<!-- zh-CN:end 88acac4f2758b87e -->

**Can I point it at a codebase and ask where the performance problems are?**
No. It diagnoses one failure you can already name. Its performance branch is for a regression with a symptom (establish a baseline measurement, then bisect, measure first and fix second), not for a proactive sweep. A skill for the proactive version was [proposed and closed](https://github.com/mattpocock/skills/issues/431); no skill does it now.

<!-- zh-CN:begin c6d08b54bbb8c0bd -->

**可以指向一个代码库，询问性能问题在哪里吗？**
不能。它诊断你能说出的一个故障。它的性能分支用于有症状的回归（先建立基线测量，再二分，先测量后修复），不用于主动扫描。主动扫描版本曾被[提出并关闭](https://github.com/mattpocock/skills/issues/431)；目前没有技能执行该功能。

<!-- zh-CN:end c6d08b54bbb8c0bd -->

**Does it stop and ask me before it writes the fix?**
No. Only Phase 3 has a human checkpoint: the ranked hypothesis list is shown to you before any is tested, and the agent continues with its own ranking if you are away. There is no gate between instrumentation and the fix, so the agent can start writing code before you have agreed with its root cause. [Issue #124](https://github.com/mattpocock/skills/issues/124) asks for that gate and is still open. If you want it, say so when you invoke the skill.

<!-- zh-CN:begin 3b1085874ab6dc20 -->

**写修复前会停下来问我吗？**
不会。只有第 3 阶段有人类检查点：在任何测试前向你展示有排序的假设列表；你若离开，智能体会按自己的排序继续。插桩和修复之间没有门控，因此智能体可能在尚未与你确认根因时就开始写代码。[问题 #124](https://github.com/mattpocock/skills/issues/124) 请求增加该门控，但仍未关闭。若需要，请在调用技能时说明。

<!-- zh-CN:end 3b1085874ab6dc20 -->

**I already ran `/triage` on this bug report. Is this the same work again?**
Partly, and neither skill says so. As one reader put it: "Triage's step 3 is essentially a shallow, bounded instance of diagnosing-bugs Phase 1–2, but neither file mentions the other." Triage does a bounded "is this actually a bug, and what is the surface" pass; this skill does the thorough version. Running triage first is not wasted, because its verification often gives you most of Phase 1's raw material. But expect this skill to redo that work in full, and expect no cross-reference to tell you so.

<!-- zh-CN:begin 009c72c08965a3be -->

**我已经对这个缺陷报告运行 `/triage`。这是重复工作吗？**
部分是，而且两个技能均未说明。某位读者说：“Triage 的第 3 步基本上就是 diagnosing-bugs 第 1–2 阶段的浅层、受限版本，但两个文件都没有提到对方。”分诊执行有限的“这确实是缺陷吗，涉及面是什么”检查；本技能执行完整版本。先运行分诊不算浪费，因为它的验证往往提供第 1 阶段的大部分原始材料。但本技能会完整重做这些工作，也不会有交叉引用提醒你。

<!-- zh-CN:end 009c72c08965a3be -->

**Will the repro output it pastes leak secrets?**
It might. The skill asks the agent to paste the invocation and its output, and to request artifacts like HAR files, log dumps, and core dumps. No instruction tells the agent to sanitise them. [Issue #674](https://github.com/mattpocock/skills/issues/674) raises exactly this (credentials, tokens, cookies, and personal data copied into a chat, an issue, or a PR) and proposes a redaction guardrail. It is open and unimplemented. Treat redaction as your job for now, particularly before the output goes anywhere public.

<!-- zh-CN:begin e0b141b230cfe2f4 -->

**它粘贴的复现输出会泄漏机密吗？**
可能会。技能要求智能体粘贴调用及输出，并请求 HAR 文件、日志转储和核心转储等产物。没有指令要求脱敏。[问题 #674](https://github.com/mattpocock/skills/issues/674) 正好指出这一点（凭据、令牌、Cookie 和个人数据被复制到聊天、问题或 PR），并提出脱敏防护。该问题仍未实现。目前请自行负责脱敏，尤其在输出会进入公开位置前。

<!-- zh-CN:end e0b141b230cfe2f4 -->

**My security scanner flagged this skill as high risk.**
Snyk flags it, and the flag is a false positive. It is the only skill in the set that ships an executable shell script (`hitl-loop.template.sh`) alongside instructions to run it and to curl a dev server. A shipped `.sh` file, instructions to run it, and outbound HTTP together are enough to trigger a static scanner. The script itself is about 30 lines of `read -r -p` prompts that pause for human input. The scanner rates what the skill could do, not a proven exploit.

<!-- zh-CN:begin 3d3e5f25dd9bddee -->

**我的安全扫描器把此技能标为高风险。**
Snyk 会标记它，但这是误报。它是整套技能中唯一附带可执行 shell 脚本（`hitl-loop.template.sh`）、同时提供运行该脚本及 curl 开发服务器的说明。附带的 `.sh` 文件、运行说明和出站 HTTP 足以触发静态扫描器。脚本本身约 30 行 `read -r -p` 提示，等待人工输入。扫描器评估的是技能*可能*做什么，而不是已证明的漏洞利用。

<!-- zh-CN:end 3d3e5f25dd9bddee -->

**What happened to `/diagnose`?**
v1.0.0 renamed it to `/diagnosing-bugs`. The old name no longer exists. Anything of yours that chains `/diagnose` (a wrapper skill, a saved prompt) needs updating.

<!-- zh-CN:begin 4a30ec1b4219aba5 -->

**`/diagnose` 发生了什么？**
v1.0.0 将其重命名为 `/diagnosing-bugs`。旧名称已不存在。任何链接 `/diagnose` 的封装技能或保存提示词都需要更新。

<!-- zh-CN:end 4a30ec1b4219aba5 -->

## It's working if

<!-- zh-CN:begin 1da23e58dc062655 -->

## 正常工作时的表现

<!-- zh-CN:end 1da23e58dc062655 -->

- It shows you a command and its red output before it offers a single theory. If theory arrives first, the skill is not running.

<!-- zh-CN:begin 18a63686f98d7cc5 -->

- 在提出任何理论前，它先向你展示一条命令及其红色输出。若先出现理论，说明技能没有正常运行。

<!-- zh-CN:end 18a63686f98d7cc5 -->
- The failure it reproduces is the one you reported, not a nearby one it found on the way.

<!-- zh-CN:begin f286fbe9a0b145a8 -->

- 它复现的失败正是你报告的失败，而不是途中碰到的邻近失败。

<!-- zh-CN:end f286fbe9a0b145a8 -->
- It shrinks the repro before it starts guessing, and can tell you why it needs each remaining piece.

<!-- zh-CN:begin 47adb185d9da56f2 -->

- 它在猜测前缩小复现，并能说明每个剩余元素为何必要。

<!-- zh-CN:end 47adb185d9da56f2 -->
- It shows you a ranked list of 3–5 hypotheses, each with a prediction you could falsify, before it tests any of them.

<!-- zh-CN:begin c33107f17541326e -->

- 在测试任何假设前，它向你展示 3–5 个有排序、各带可证伪预测的假设。

<!-- zh-CN:end c33107f17541326e -->
- Every debug log it adds carries a tag like `[DEBUG-a4f2]`, and a grep for that tag comes back empty when it declares done.

<!-- zh-CN:begin 85c25b618e22f8b2 -->

- 它添加的每个调试日志都带 `[DEBUG-a4f2]` 一类标签；宣布完成时，按此标签 grep 应无结果。

<!-- zh-CN:end 85c25b618e22f8b2 -->
- The commit or PR message names which hypothesis was right.

<!-- zh-CN:begin b1866bd7046e23c0 -->

- 提交或 PR 消息说明哪个假设正确。

<!-- zh-CN:end b1866bd7046e23c0 -->
- When it cannot lock the bug down with a test, it says so instead of writing a shallow one.

<!-- zh-CN:begin a5780b7e2db381eb -->

- 无法用测试锁定缺陷时，它会直说，而不是写一个浅层测试。

<!-- zh-CN:end a5780b7e2db381eb -->

## Where it fits

<!-- zh-CN:begin 069b9a6b6f2ac667 -->

## 所处位置

<!-- zh-CN:end 069b9a6b6f2ac667 -->

`diagnosing-bugs` is a reach-for-it-anytime standalone. You start it when something is broken, and it ends when the fix and its regression test are in. It keeps no state and needs no prior setup. [ask-matt](https://aihero.dev/skills-ask-matt) routes "Something's broken" here.

<!-- zh-CN:begin e911266481620e8e -->

`diagnosing-bugs` 是可随时使用的独立技能。问题出现时启动，修复与回归测试落地时结束。它不保存状态，也不需要预先设置。[ask-matt](https://aihero.dev/skills-ask-matt) 会把“有东西坏了”路由到这里。

<!-- zh-CN:end e911266481620e8e -->

Two neighbours matter. [retro](https://aihero.dev/skills-retro) comes after it: once the fix is in, run it in the same session to ask what would have prevented the bug, while the session has more information than it had at the start. `diagnosing-bugs` never invokes `retro` itself, because `retro` is user-invoked. [triage](https://aihero.dev/skills-triage) comes before it for bugs that arrive as raw reports from other people, and does a shallower version of the same first two phases.

<!-- zh-CN:begin f1a124ec4647db6c -->

两个相邻技能很重要。[回顾](https://aihero.dev/skills-retro) 在其后使用：修复落地后，在同一会话中运行它，趁会话掌握比开始时更多信息，询问什么本可防止缺陷。`diagnosing-bugs` 从不自行调用 `retro`，因为 `retro` 由用户调用。[分诊](https://aihero.dev/skills-triage) 用于以他人原始报告形式到达的缺陷，会在前面执行相同前两阶段的浅层版本。

<!-- zh-CN:end f1a124ec4647db6c -->
