标题：<skill or symptom>：<one-line observable>（<harness>）

- [x] 已搜索现有 issue，确认不是重复（搜索词：<query terms>；最接近：<#n title，或“无”>）

## 谁提交本报告？（必填）

<本次会话使用的模型和运行环境>，代表<你的伙伴希望如何称呼，或“我的人类伙伴”>提交，其请求为：“<本次会话中导致诊断或 issue 的请求，已脱敏>”，相关标识为 <model> <how> <their>。

## 人类撰写的摘要（必填，200 词以内）

<你的伙伴用原话说明出了什么问题、本应发生什么，逐字粘贴。请向他们索取；此处只有占位符意味着 issue 尚未准备好提交。内容过长时请他们自行删减，而不是由你编辑其用词。>，相关标识为 <Your>。

## 环境（必填）

| 字段 | 值 | 来源／支持证据 |
|---|---|---|
| Superpowers 版本 | <version>（<sha，或“不是检出”>） | <历史证据／未验证快照／当前观察／未知>；<位置> |
| 运行环境（Claude Code、Cursor 等） | <harness> | <标签>；<位置> |
| 运行环境版本 | <version> | <标签>；<位置> |
| 你的模型及版本 | <model ids seen> | <标签>；<位置> |
| 已安装的所有插件 | <list> | <标签>；<位置> |
| 操作系统和 shell | <os version>, <shell> | <标签>；<位置> <historical> <location> <location> <location> <location> <location> <location> <label> <label> <label> <label> <label> |

## 这是 Superpowers 的问题还是平台问题？

- [ ] 已确认未安装 Superpowers 时该问题不会发生

我如何验证未安装 Superpowers 时问题不复现：
<“未尝试”，或伙伴在无 superpowers 时运行了什么、发生了什么，有记录时附路径。只有记录显示问题未复现时才勾选上方复选框。>

下方给出涉及 Superpowers 的证据；它不证明因果关系。

## 发生了什么？

<问题陈述，随后是分诊结论；将 `path:line` 引用改写为 `transcript line <n>`。>，相关标识为 <Problem>。

## 复现步骤

1. <第一条人类提示，已脱敏>，相关标识为 <first>。

2. <导致问题的各轮，每轮一行>，相关标识为 <the>。

3. <可观察结果>，相关标识为 <the>。

## 预期行为

<来自问题陈述>，相关标识为 <from>。

## 实际行为

<来自分诊结论>，相关标识为 <from>。

## 调试日志或对话记录

会话 id：<ids>。交付的本地归档：<path，脱敏级别 <level>

| 未构建>。附加包：<不声明；仅在批准后附加>。
诊断报告显示 Superpowers 参与程度：<可能 | 很可能>，证据位于<记录行>。本报告不提出修复。，相关标识为 <no> <possible> <transcript>。

使用 `diagnosing-superpowers` 技能提交。提交模型和运行环境见“谁提交本报告”；被诊断会话的模型、运行环境、版本和插件见环境表。
