# Build the change and clean the diff

<!-- zh-CN:begin 181b5fad266bf083 -->

# 构建改动并清理差异

<!-- zh-CN:end 181b5fad266bf083 -->

The build playbooks share one discipline. Say what you observed, and let the playbook demand the evidence. This page shows what to put in the prompt for each common build task, then the cleanup habit that keeps diffs reviewable.

<!-- zh-CN:begin 70e2a4fd6e4dc8dd -->

构建类操作手册共享同一套纪律：说明你观察到的内容，让手册要求证据。本页展示每种常见构建任务应在提示词中写什么，以及保持差异可审查的清理习惯。

<!-- zh-CN:end 70e2a4fd6e4dc8dd -->

## Prompt each build playbook with what you know

<!-- zh-CN:begin 6d6465c72796b60d -->

## 用已知事实提示每份构建手册

<!-- zh-CN:end 6d6465c72796b60d -->

A bug prompt states the symptom and asks for a reproduction first:

<!-- zh-CN:begin b952b34021d9c2d6 -->

缺陷提示词要说明症状，并要求先复现：

<!-- zh-CN:end b952b34021d9c2d6 -->

```text
/poteto-mode this command emits two records after a retry. repro first, then fix and verify.
```

<!-- zh-CN:begin d8fe4b12f559680d -->

```text
/poteto-mode 此命令在重试后输出两条记录。先复现，再修复并验证。
```

<!-- zh-CN:end d8fe4b12f559680d -->

A feature prompt states the behavior and what must not change:

<!-- zh-CN:begin 80d2306fb9cbbe85 -->

功能提示词要说明行为，以及哪些内容不得改变：

<!-- zh-CN:end 80d2306fb9cbbe85 -->

```text
/poteto-mode add a --json flag. text output stays byte-identical. verify both forms.
```

<!-- zh-CN:begin 44de316f714e3fe5 -->

```text
/poteto-mode 添加 --json 标志。文本输出保持逐字节相同。验证两种形式。
```

<!-- zh-CN:end 44de316f714e3fe5 -->

A refactoring prompt pins behavior before structure moves:

<!-- zh-CN:begin e868914155d623bb -->

重构提示词要在移动结构前锁定行为：

<!-- zh-CN:end e868914155d623bb -->

```text
/poteto-mode move parsing into one module, zero behavior change. record the current output first and prove it's unchanged after.
```

<!-- zh-CN:begin 74a45f4615701196 -->

```text
/poteto-mode 把解析移入一个模块，行为零变化。先记录当前输出，并证明之后未改变。
```

<!-- zh-CN:end 74a45f4615701196 -->

A perf prompt states the measurement, not an impression:

<!-- zh-CN:begin 81277eb87fc81888 -->

性能提示词要给出测量值，而非印象：

<!-- zh-CN:end 81277eb87fc81888 -->

```text
/poteto-mode startup takes 1.8s on this fixture. trace it, fix the measured cause, show me before and after.
```

<!-- zh-CN:begin 7d127ceffb95e546 -->

```text
/poteto-mode 启动在此夹具上耗时 1.8 秒。跟踪它，修复测得的原因，给我看前后对比。
```

<!-- zh-CN:end 7d127ceffb95e546 -->

Each of these routes to its playbook ([Bug fix](../../skills/poteto-mode/playbooks/bug-fix.md), [Feature](../../skills/poteto-mode/playbooks/feature.md), [Refactoring](../../skills/poteto-mode/playbooks/refactoring.md), [Perf issue](../../skills/poteto-mode/playbooks/perf-issue.md)), and the playbook supplies the steps you didn't type: reproduce before fixing, name the data shape before implementing, pin behavior before restructuring, profile before optimizing.

<!-- zh-CN:begin 9039392410782884 -->

这些提示词分别路由到[缺陷修复](../../skills/poteto-mode/playbooks/bug-fix.md)、[功能](../../skills/poteto-mode/playbooks/feature.md)、[重构](../../skills/poteto-mode/playbooks/refactoring.md)、[性能问题](../../skills/poteto-mode/playbooks/perf-issue.md)手册，手册补上你未输入的步骤：修复前复现、实现前命名数据结构、重构前锁定行为、优化前剖析。

<!-- zh-CN:end 9039392410782884 -->

For sustained improvement of one number, there's the [Hillclimb playbook](../../skills/poteto-mode/playbooks/hillclimb.md). Give it the metric, a target, and a floor on attempts, and it loops one hypothesis at a time with a frozen measurement harness. It keeps wins and reverts everything else.

<!-- zh-CN:begin b609dfdb7ca686ff -->

要持续改进一个数字，可使用[爬山优化手册](../../skills/poteto-mode/playbooks/hillclimb.md)。提供指标、目标和最少尝试次数，它借助冻结的测量框架逐个循环假设，保留收益并回退其他内容。

<!-- zh-CN:end b609dfdb7ca686ff -->

Both perf playbooks run [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) on their numbers. Perf issue vets its baseline and every number after it, and Hillclimb vets its harness before freezing it. [Verify and ship](./06-verify-and-ship.md#vet-a-measured-number-with-benchmark-checklist) shows when to type it yourself.

<!-- zh-CN:begin 5ced92d171d54087 -->

两个性能手册都会对数字运行 [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md)。性能问题会核验基线及后续每个数字，爬山优化在冻结前核验框架。[验证与交付](./06-verify-and-ship.md#vet-a-measured-number-with-benchmark-checklist) 说明何时应自行运行。

<!-- zh-CN:end 5ced92d171d54087 -->

Sometimes you want the cause before any fix. For a live symptom, such as a leak, an idle CPU spin, or a visual glitch, the [Runtime forensics playbook](../../skills/poteto-mode/playbooks/runtime-forensics.md) instruments the running process. For a profile you already captured, the [Trace forensics playbook](../../skills/poteto-mode/playbooks/trace-forensics.md) reads the artifact and maps the hot frame to source. Both return a diagnosis, not a fix:

<!-- zh-CN:begin da129f947c899798 -->

有时需要先找原因再修复。对于泄漏、空闲 CPU 空转或视觉故障等实时症状，[运行时取证手册](../../skills/poteto-mode/playbooks/runtime-forensics.md) 对运行中进程插桩。已经捕获性能分析时，[跟踪取证手册](../../skills/poteto-mode/playbooks/trace-forensics.md) 读取产物并把热点帧映射到源码。二者都返回诊断而非修复：

<!-- zh-CN:end da129f947c899798 -->

```text
/poteto-mode here's a cpuprofile from the slow startup. tell me where the time goes and which source lines own it. no fix yet.
```

<!-- zh-CN:begin 2547b3eb90d57936 -->

```text
/poteto-mode 这是启动缓慢的 cpuprofile。告诉我时间花在哪里，哪些源码行负责它。暂时不要修复。
```

<!-- zh-CN:end 2547b3eb90d57936 -->

## Write the failing test first with `/tdd`

<!-- zh-CN:begin bf7be0286bbdf07d -->

## 用 `/tdd` 先写失败测试

<!-- zh-CN:end bf7be0286bbdf07d -->

When a bug has a cheap local test path, the whole prompt can be two words:

<!-- zh-CN:begin 7f22b69bb3caa219 -->

缺陷有低成本本地测试路径时，整条提示词可以只有两个词：

<!-- zh-CN:end 7f22b69bb3caa219 -->

```text
/tdd implement
```

In context, that's enough. [`/tdd`](../../skills/tdd/SKILL.md) writes the smallest test that fails for the intended reason, then the fix, then reruns the test. If a test would need broad harness setup or brittle mocks, the skill says so and uses the closest executable check instead. Don't force a test where a real command is stronger evidence.

<!-- zh-CN:begin b096a580f7258446 -->

在上下文中，这已足够。[`/tdd`](../../skills/tdd/SKILL.md) 编写会因预期原因失败的最小测试，再修复并重跑测试。若测试需要庞大框架准备或脆弱 mock，技能会说明，并改用最接近的可执行检查。真实命令证据更强时，不要强行写测试。

<!-- zh-CN:end b096a580f7258446 -->

## Load the TypeScript rules by name

<!-- zh-CN:begin fefdb752e136c567 -->

## 按名称加载 TypeScript 规则

<!-- zh-CN:end fefdb752e136c567 -->

[`typescript-best-practices`](../../skills/typescript-best-practices/SKILL.md) turns the type-system principles into concrete rules: discriminated unions, `unknown` at boundaries, exhaustive variants, schema-derived types. It doesn't load on its own, so type `/typescript-best-practices` when a task touches `.ts` or `.tsx` files.

<!-- zh-CN:begin ba679b8c053750cc -->

[`typescript-best-practices`](../../skills/typescript-best-practices/SKILL.md) 把类型系统原则变成具体规则：可辨识联合、边界使用 `unknown`、穷尽变体、从 schema 派生类型。它不会自行加载，因此任务涉及 `.ts` 或 `.tsx` 文件时，输入 `/typescript-best-practices`。

<!-- zh-CN:end ba679b8c053750cc -->

## Clean before you commit

<!-- zh-CN:begin 06f129b034c9d604 -->

## 提交前清理

<!-- zh-CN:end 06f129b034c9d604 -->

The [Opening a PR playbook](../../skills/poteto-mode/playbooks/opening-a-pr.md) runs `/deslop` on the diff before each commit and applies [`/unslop`](../../skills/unslop/SKILL.md) to the PR description and commit bodies. `/deslop` ships in the `cursor-team-kit` plugin, not in pstack. If you don't have it, ask for the same outcome in plain words: remove narrating comments, unsupported guards, dead compatibility paths, and unrelated edits.

<!-- zh-CN:begin e019560ee781cfb2 -->

[创建 PR 手册](../../skills/poteto-mode/playbooks/opening-a-pr.md) 在每次提交前对差异运行 `/deslop`，并对 PR 描述和提交正文应用 [`/unslop`](../../skills/unslop/SKILL.md)。`/deslop` 随 `cursor-team-kit` 插件发布，不在 pstack 中。没有它时，用普通语言要求同样结果：移除叙述性注释、无依据的防护、死兼容路径和无关编辑。

<!-- zh-CN:end e019560ee781cfb2 -->

For prose, `/unslop` takes a target and any extra rules you have:

<!-- zh-CN:begin 95fb1f6e4ee98154 -->

对于文字，`/unslop` 接收目标和附加规则：

<!-- zh-CN:end 95fb1f6e4ee98154 -->

```text
/unslop the readme changes, no emdashes
```

<!-- zh-CN:begin 7b43442b936b05ed -->

```text
/unslop README 改动，不要长破折号
```

<!-- zh-CN:end 7b43442b936b05ed -->

You'll develop your own shorthand. The skill reads intent fine from terse prompts like `unslop that, tighten it`.

<!-- zh-CN:begin 2587ff4a3ae6b1d9 -->

你会形成自己的简写。技能可从 `unslop that, tighten it` 这样的简短提示中读取意图。

<!-- zh-CN:end 2587ff4a3ae6b1d9 -->

## Strip the comments with `/no-comments`

<!-- zh-CN:begin 106b3ae8c4a3ff01 -->

## 用 `/no-comments` 清理注释

<!-- zh-CN:end 106b3ae8c4a3ff01 -->

Comments need their own pass, and not from the agent that wrote them. An author defends its comments the way you'd defend yours. So before review, hand them to fresh eyes:

<!-- zh-CN:begin 27e49c4bcfd861ae -->

注释需要单独一轮检查，而且不应由编写它们的智能体执行。作者会像维护自己观点一样维护其注释。因此评审前，交给新视角：

<!-- zh-CN:end 27e49c4bcfd861ae -->

```text
/no-comments the diff
```

<!-- zh-CN:begin 316981fd7f698a1e -->

```text
/no-comments 差异
```

<!-- zh-CN:end 316981fd7f698a1e -->

[`/no-comments`](../../skills/no-comments/SKILL.md) spawns [Comment Sicko](../../agents/comment-sicko.md), a read-only reviewer with a short keep list: license headers, doc comments on a public API, links that explain what code can't, behavior forced by an external dependency you can't reshape. Everything else goes. A surprise in your own code gets no such pass. The comment comes back as a refactor flag, and `/no-comments` fixes the flags it accepts at the root cause. When a comment claims a constraint, "do not remove", the skill offers to encode the claim as a type, test, or lint. Either way, the comment comes out.

<!-- zh-CN:begin b3256f4a52049218 -->

[`/no-comments`](../../skills/no-comments/SKILL.md) 启动 [Comment Sicko](../../agents/comment-sicko.md)，这是只读评审者，保留清单很短：许可证头、公共 API 的文档注释、解释代码无法表达内容的链接、由你无法改变的外部依赖强制形成的行为。其余全部删除。你自己代码中的意外不享有例外。注释会变回重构标记，`/no-comments` 在其接受的标记根因处修复。注释声称约束（“不要移除”）时，技能提出把声明编码为类型、测试或 lint。无论怎样，注释都会移除。

<!-- zh-CN:end b3256f4a52049218 -->

The division of labor is worth keeping straight. `/deslop` cleans slop out of the code, `/unslop` cleans it out of prose, and `/no-comments` hands the comments to a reviewer who didn't write them.

<!-- zh-CN:begin 7dad49de08c16914 -->

分工需要分清：`/deslop` 清理代码中的垃圾，`/unslop` 清理文字中的垃圾，`/no-comments` 把注释交给未写它们的评审者。

<!-- zh-CN:end 7dad49de08c16914 -->

**Pitfall:** cleanup is not optional polish. A diff with narrating comments and defensive dead weight reads as unfinished to reviewers, and the extra code is where the next bug hides. If the diff feels padded, say `deslop it` before you commit, not after review calls it out.

<!-- zh-CN:begin 6ce8561118c7261f -->

**陷阱：** 清理不是可选润色。带有叙事注释和防御性死重量的差异在评审者看来就是未完成，而额外代码正是下一个缺陷藏身处。差异显得臃肿时，在提交前说 `deslop it`，不要等评审指出。

<!-- zh-CN:end 6ce8561118c7261f -->

Next: [Verify and ship](./06-verify-and-ship.md).

<!-- zh-CN:begin 7d3bd4d5d0e7b03d -->

下一步：[验证与交付](./06-verify-and-ship.md)。

<!-- zh-CN:end 7d3bd4d5d0e7b03d -->
