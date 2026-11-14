# Hard limits on the number of questions during grilling

<!-- zh-CN:begin eaee57315e4b3d81 -->

# 追问问题数量的硬限制

<!-- zh-CN:end eaee57315e4b3d81 -->

The `/grill-me` skill (and grilling sessions inside other skills) does not enforce a maximum number of questions. Requests to add a configurable cap or hard ceiling are out of scope.

<!-- zh-CN:begin 59507293e80e36d3 -->

`/grill-me`（及其他技能中的追问会话）不强制最大问题数。添加可配置上限或硬顶的请求不在范围。

<!-- zh-CN:end 59507293e80e36d3 -->

## Why this is out of scope

<!-- zh-CN:begin 4384df0a2c9e3996 -->

## 为什么不在范围

<!-- zh-CN:end 4384df0a2c9e3996 -->

Grilling is intentionally open-ended. The point is to keep digging until each branch of the decision tree is resolved: some plans need three questions, some need fifty. A fixed cap would either cut off useful exploration on hard problems or feel arbitrary on easy ones.

<!-- zh-CN:begin 4e03ce483ffd7bb2 -->

追问有意开放，目标是持续挖掘到决策树每个分支解决：有些计划只需三个问题，有些需要五十个。固定上限会截断困难问题的有用探索，或在简单问题上显得任意。

<!-- zh-CN:end 4e03ce483ffd7bb2 -->

If a session feels too long, the right escape hatches already exist:

<!-- zh-CN:begin a29592d149820931 -->

会话过长时已有退出方式：

<!-- zh-CN:end a29592d149820931 -->

- The user can stop the session at any time and accept the current state of the plan.

<!-- zh-CN:begin a47c4173846277a5 -->

- 用户可随时停止并接受当前计划状态。

<!-- zh-CN:end a47c4173846277a5 -->
- The user can tell the model to wrap up, summarise, and move on, since natural-language steering is the intended control surface, not a numeric limit.

<!-- zh-CN:begin b118e72a44f659c8 -->

- 用户可让模型收尾、总结并继续；自然语言指导是预期的控制面，不是数字上限。

<!-- zh-CN:end b118e72a44f659c8 -->

Adding a hard cap would also conflate two different failure modes: a model that asks too many questions because the plan is genuinely under-specified (working as intended) vs. a model that asks redundant or low-value questions (a prompt-quality issue, not a quantity issue). The fix for the latter belongs in the skill prompt, not in a counter.

<!-- zh-CN:begin 8bd3a8144ff1e8c1 -->

硬上限还会混淆两种失败：计划确实不明确导致多问（正常工作），以及重复低价值提问（提示质量而非数量问题）。后者应在技能提示中修复，不用计数器。

<!-- zh-CN:end 8bd3a8144ff1e8c1 -->

## Prior requests

<!-- zh-CN:begin db630c81cc3143d2 -->

## 以往请求

<!-- zh-CN:end db630c81cc3143d2 -->

- #44: "Codex just asked me 200 questions"

<!-- zh-CN:begin 45d8c0d4ddfffd5a -->

- #44：“Codex 刚问了我 200 个问题”

<!-- zh-CN:end 45d8c0d4ddfffd5a -->
