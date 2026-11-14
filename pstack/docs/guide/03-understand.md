# Understand the code before changing it

<!-- zh-CN:begin aef20a8cbea541e5 -->

# 改动前先理解代码

<!-- zh-CN:end aef20a8cbea541e5 -->

Editing code you don't understand is how subtle regressions ship, and that's as true for the agent as for you. Agents usually fail in one of two ways. They misread what you want, or they don't have the context to do the work right. [What goes in a prompt](./02-poteto-mode.md#what-goes-in-a-prompt) handles the first. This page handles the second.

<!-- zh-CN:begin 633b202497060b94 -->

编辑不理解的代码会发布隐蔽回归，对代理同样成立。代理通常有两种失败：误解需求，或缺少正确工作所需上下文。[提示词应包含什么](./02-poteto-mode.md#what-goes-in-a-prompt)处理前者，本页处理后者。

<!-- zh-CN:end 633b202497060b94 -->

pstack gives you four ways in. `/how` explains what the code does now. `/why` digs up the reasons it's shaped that way. `/teach` blends both into one explanation. `/recall` rebuilds your own recent context on a topic. Each one also makes the agent explain itself in words you can check. That's how you supervise an agent that may know the code better than you do.

<!-- zh-CN:begin 76064538ec15cede -->

pstack提供四种入口：`/how`解释现行行为，`/why`追踪形成原因，`/teach`把二者融合成说明，`/recall`重建你近期上下文。四者都让代理用可核验的话解释，从而监督可能比你更熟悉代码的代理。

<!-- zh-CN:end 76064538ec15cede -->

![A detective studies a machine blueprint with a magnifying glass while robots fetch case files; the evidence board behind her links clues under /how and /why.](./images/understanding.jpg)

<!-- zh-CN:begin 407cd89743d12298 -->

![侦探用放大镜研究机器蓝图，机器人递送案例文件；证据板把 `/how` 和 `/why` 的线索连起来。](./images/understanding.jpg)

<!-- zh-CN:end 407cd89743d12298 -->

## Start with a read-only investigation

<!-- zh-CN:begin be5d29fb54b852ca -->

## 先做只读调查

<!-- zh-CN:end be5d29fb54b852ca -->

When the cause is unclear, ask for findings, not a fix:

<!-- zh-CN:begin ffa4983cd9078e2f -->

原因不明时，要发现而非修复：

<!-- zh-CN:end ffa4983cd9078e2f -->

```text
/poteto-mode investigate why background jobs time out every few hours. give me what we know, what data you used, and your best hypotheses. don't change any code yet.
```

<!-- zh-CN:begin d7cc197399aa85dc -->

```text
/poteto-mode 调查后台作业为何每隔几小时超时。给出已知事实、所用数据和最佳假设，暂不改代码。
```

<!-- zh-CN:end d7cc197399aa85dc -->

"don't change any code yet" routes this to the [Investigation playbook](../../skills/poteto-mode/playbooks/investigation.md). It runs `/how`, adds `/why` for questions about motivation, and returns a cited explanation. For a choice between options, it returns a recommendation with a trade-offs table. Asking "what data you used" makes the agent separate its evidence from its guesses. When the findings point at a fix, start the fix as a new task.

<!-- zh-CN:begin c86434de6bd1158e -->

“暂不改代码”会路由到[调查手册](../../skills/poteto-mode/playbooks/investigation.md)，运行`/how`，关于动机的问题加`/why`，返回带引用解释。选项之间选择时给建议和取舍表。要求列出所用数据可分离证据与猜测；发现指向修复后，以新任务开始修复。

<!-- zh-CN:end c86434de6bd1158e -->

## Trace behavior with `/how`

<!-- zh-CN:begin db7a937cb63b701d -->

## 用 `/how` 追踪行为

<!-- zh-CN:end db7a937cb63b701d -->

```text
/how do we dedupe notifications? is there an n+1 when we look up subscribers?
```

<!-- zh-CN:begin b9a3f4f8751bff93 -->

```text
/how 我们如何给通知去重？查询订阅者时是否存在n+1问题？
```

<!-- zh-CN:end b9a3f4f8751bff93 -->

Ask the question you actually have. [`/how`](../../skills/how/SKILL.md) reads the code and answers at the level of a senior engineer onboarding you onto the subsystem, with the runtime flow, the key types, and the non-obvious parts. For a big subsystem it fans out two to four read-only explorers first. For a narrow question it just reads and explains.

<!-- zh-CN:begin d1acabb8e83db277 -->

提出真实问题。[`/how`](../../skills/how/SKILL.md)像资深工程师带新人一样解释子系统，包括运行流程、关键类型和不明显部分。大子系统先派出2–4个只读探索者，窄问题直接阅读解释。

<!-- zh-CN:end d1acabb8e83db277 -->

## Dig up history with `/why`

<!-- zh-CN:begin d7d05568f4b1d2f1 -->

## 用 `/why` 挖掘历史

<!-- zh-CN:end d7d05568f4b1d2f1 -->

```text
/why was the retry limit set to five? does the reason still hold?
```

<!-- zh-CN:begin acba4d1f727c8430 -->

```text
/why 重试上限为什么是五？理由仍成立吗？
```

<!-- zh-CN:end acba4d1f727c8430 -->

[`/why`](../../skills/why/SKILL.md) starts from source control, then queries whatever evidence categories your MCPs expose, such as the issue tracker, long-form docs, team chat, observability, error tracking, and analytics, all in parallel. The report cites everything, separates direct evidence from inference, and says "appears to" when the record is thin. A null result gets reported too, because "nobody wrote down why" is itself an answer.

<!-- zh-CN:begin bc7be452b0ddfd79 -->

[`/why`](../../skills/why/SKILL.md)从源码控制开始，并行查询 MCP 暴露的证据类别：issue跟踪器、长文档、团队聊天、可观测性、错误跟踪和分析。报告全带引用，分离直接证据与推断；记录不足时用“似乎”。无结果也报告，因为“没人写下原因”本身就是答案。

<!-- zh-CN:end bc7be452b0ddfd79 -->

The two compose naturally. `do why first then how` is a good prompt when you suspect the history explains the mess.

<!-- zh-CN:begin d6cdc60caa2d2583 -->

两者可组合；怀疑历史能解释乱象时用`先why再how`。 这句可用提示词 `do why first then how`。

<!-- zh-CN:end d6cdc60caa2d2583 -->

## Actually understand it with `/teach`

<!-- zh-CN:begin f7936c86f9fc4bde -->

## 用 `/teach` 真正理解

<!-- zh-CN:end f7936c86f9fc4bde -->

```text
/teach me how this PR changes retries. convince me it fixes the cause and not the symptom.
```

<!-- zh-CN:begin 7cc927380cfcb0cc -->

```text
/teach 讲清这个PR如何改变重试，说服我这个修复的是原因而非症状。
```

<!-- zh-CN:end 7cc927380cfcb0cc -->

[`/teach`](../../skills/teach/SKILL.md) is for when a summary isn't enough. It runs `/how` and `/why`, for a small change maybe just one of them, and weaves the findings into a plain explanation that builds up diagram by diagram. The "convince me" framing is worth reusing. It turns the explanation into an argument you can test instead of a tour.

<!-- zh-CN:begin e6017c8837ac0c03 -->

[`/teach`](../../skills/teach/SKILL.md)用于总结不够时；运行`/how`和`/why`（小改动可能只用其一），逐步配图形成通俗解释。“说服我”把说明变成可测试的论证而非导览。

<!-- zh-CN:end e6017c8837ac0c03 -->

It works on the agent's own choices too:

<!-- zh-CN:begin 6c59ca600d7c7ed8 -->

也能审查代理自身选择：

<!-- zh-CN:end 6c59ca600d7c7ed8 -->

```text
/teach me why you implemented it this way and not with a queue. what did you trade off, and why?
```

<!-- zh-CN:begin c2923a5f9aa88d0b -->

```text
/teach 讲清你为什么这样实现而不用队列，权衡了什么，为什么？
```

<!-- zh-CN:end c2923a5f9aa88d0b -->

Teaching helps the agent as much as you. An agent that has to explain its work must read the code and back each claim with evidence, instead of stating it confidently and moving on.

<!-- zh-CN:begin 7f9d9f809c12abe0 -->

教学也帮助代理：必须阅读代码并用证据支持断言，不能自信陈述后继续。

<!-- zh-CN:end 7f9d9f809c12abe0 -->

## Rebuild your own context with `/recall`

<!-- zh-CN:begin 3aaa4db3a36799f6 -->

## 用 `/recall` 重建自己的上下文

<!-- zh-CN:end 3aaa4db3a36799f6 -->

```text
/recall catch me up on the export work from last week
```

<!-- zh-CN:begin 8d31fe8994c54107 -->

```text
/recall 带我回顾上周导出工作的进展
```

<!-- zh-CN:end 8d31fe8994c54107 -->

[`/recall`](../../skills/recall/SKILL.md) mines your own recent chats plus the shared record (issues, prior fixes, errors still firing) and hands back a brief on where things stand and what's next. Your old chats hold context that a fresh agent lacks, so start new work on an old topic by loading it first, then hand over the new input:

<!-- zh-CN:begin a93e600ff82d4302 -->

[`/recall`](../../skills/recall/SKILL.md)挖掘你近期聊天和共享记录（issue、既往修复、仍在发生的错误），返回现状和下一步。旧聊天含新代理缺失的上下文，旧主题重新开工先加载：

<!-- zh-CN:end a93e600ff82d4302 -->

```text
/recall my work on the virtualized list from yesterday, then read this bug report.
```

<!-- zh-CN:begin 8dc404c94330321d -->

```text
/recall 带我回顾昨天虚拟列表的工作，然后阅读这个bug报告。
```

<!-- zh-CN:end 8dc404c94330321d -->

If you want to resume one specific chat, that's the Session pickup playbook below, not `/recall`.

<!-- zh-CN:begin b0a1a7744fbf25fc -->

恢复某个特定聊天应使用下方Session pickup，而不是`/recall`。

<!-- zh-CN:end b0a1a7744fbf25fc -->

## Take over prior work with Session pickup

<!-- zh-CN:begin 06f8ce0cfdb3d5e6 -->

## 用 Session pickup 接手先前工作

<!-- zh-CN:end 06f8ce0cfdb3d5e6 -->

When another agent (or you, last week) left a branch mid-flight:

<!-- zh-CN:begin 46aeb1fe1ae9fefd -->

另一代理（或上周的你）留下半成品分支时：

<!-- zh-CN:end 46aeb1fe1ae9fefd -->

```text
/poteto-mode take over this branch. read the decision log, figure out what's done, and continue from there. don't redo finished work.
```

<!-- zh-CN:begin acbab4e4aeca204e -->

```text
/poteto-mode 接手此分支，读决策日志，弄清已完成内容并从那里继续，不重做已完成工作。
```

<!-- zh-CN:end acbab4e4aeca204e -->

The [Session pickup playbook](../../skills/poteto-mode/playbooks/session-pickup.md) treats the prior trail as authoritative. It reconstructs the branch state and decisions, names the resume point, and verifies inherited claims against the original goal instead of re-deriving everything from scratch.

<!-- zh-CN:begin ecd52c2811c854fa -->

[Session pickup手册](../../skills/poteto-mode/playbooks/session-pickup.md)把先前轨迹当权威，重建分支状态与决策、命名恢复点，并依据原目标验证继承断言，而不从零重推。

<!-- zh-CN:end ecd52c2811c854fa -->

**Pitfall:** don't skip this page's skills because "the agent will read the code anyway." An agent that starts editing without a traced model tends to fix the symptom at the first plausible spot. `/how` first is cheaper than the second bug.

<!-- zh-CN:begin c96dac10b581ab66 -->

**陷阱：**不要以“代理反正会读代码”为由跳过本页。没有追踪模型就开始编辑，往往在第一个看似合理位置修复症状；先`/how`比产生第二个bug更便宜。

<!-- zh-CN:end c96dac10b581ab66 -->

Next: [Design the change](./04-design.md).

<!-- zh-CN:begin 8648da9a5e3058f8 -->

下一步：[设计改动](./04-design.md)。

<!-- zh-CN:end 8648da9a5e3058f8 -->
