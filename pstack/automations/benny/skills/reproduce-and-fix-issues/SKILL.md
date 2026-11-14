---
name: reproduce-and-fix-issues
description: Reproduce triaged Slack bugs through a configured app-control adapter, verify existing fixes, and open a bounded draft pull request only after before-and-after proof. Use only from the configured Benny repro automation.
disable-model-invocation: true

# zh-CN:begin fd305f4e7914cea4
# name: reproduce-and-fix-issues
# description: "通过已配置的应用控制适配器复现经过分诊的 Slack bug，验证已有修复，并且仅在具备修复前后证明之后，才创建范围受限的草稿拉取请求。仅从已配置的 Benny 复现自动化中使用。"
# disable-model-invocation: true
# zh-CN:end fd305f4e7914cea4
---

# Reproduce and fix issues

<!-- zh-CN:begin c341f326e7bc4013 -->

# 复现并修复问题

<!-- zh-CN:end c341f326e7bc4013 -->

Wait for a trusted triage marker in the source thread. Reproduce the exact symptom through the target app's real UI. Verify an existing fix when one exists. Attempt a bounded fix only after a confirmed repro.

<!-- zh-CN:begin 8cbfac58c347db8f -->

等待来源讨论串中出现可信的分诊标记。通过目标应用的真实 UI 复现完全相同的症状。如果已有修复，则验证它。只有确认复现后才尝试范围受限的修复。

<!-- zh-CN:end 8cbfac58c347db8f -->

Load the external Benny configuration supplied by the automation. If the config, required actions, control adapter, or completed feature map is missing, fail closed.

<!-- zh-CN:begin d96c180641bf6eb1 -->

加载自动化提供的外部 Benny 配置。如果缺少配置、必需操作、控制适配器或已完成的功能映射，应以拒绝继续的方式安全停止。

<!-- zh-CN:end d96c180641bf6eb1 -->

## Hard safety rules

<!-- zh-CN:begin 811529ccaa043adc -->

## 强制安全规则

<!-- zh-CN:end 811529ccaa043adc -->

- Freeze the source channel and root thread coordinates before doing any work.

<!-- zh-CN:begin 3ea92f98ba0f67e2 -->

- 做任何工作前，固定来源频道和根讨论串坐标。

<!-- zh-CN:end 3ea92f98ba0f67e2 -->
- Never post a root message in the source channel.

<!-- zh-CN:begin 51530371a1002994 -->

- 绝不在来源频道发布根消息。

<!-- zh-CN:end 51530371a1002994 -->
- Preflight the source parent before every source-thread post.

<!-- zh-CN:begin cf0877d93afb19ed -->

- 每次向来源讨论串发帖之前，预检来源父消息。

<!-- zh-CN:end cf0877d93afb19ed -->
- The coordinator is the only Slack poster.

<!-- zh-CN:begin e71730cc3f4f25c1 -->

- 协调者是唯一可以在 Slack 发帖的角色。

<!-- zh-CN:end e71730cc3f4f25c1 -->
- Delegated analysis workers are read-only and return findings or media notes.

<!-- zh-CN:begin 8b62237335d4fa7c -->

- 委派的分析工作代理只读，并返回发现或媒体说明。

<!-- zh-CN:end 8b62237335d4fa7c -->
- A fix-phase code worker may edit only when its environment provably excludes Slack credentials and every Slack write action. Otherwise the coordinator edits.

<!-- zh-CN:begin f18fa7c804b55646 -->

- 修复阶段的代码工作代理只有在能证明其环境排除了 Slack 凭据及所有 Slack 写操作时才可编辑。否则由协调者编辑。

<!-- zh-CN:end f18fa7c804b55646 -->
- Every child prompt must explicitly forbid `SendSlackMessage`, `PostToSlack`, `chat.postMessage`, and all other Slack writes.

<!-- zh-CN:begin f719c5ae51cc2739 -->

- 每个子代理提示词都必须明确禁止 `SendSlackMessage`、`PostToSlack`、`chat.postMessage` 及其他所有 Slack 写操作。

<!-- zh-CN:end f719c5ae51cc2739 -->
- Never give a child a Slack token, posting instructions, source coordinates for posting, or permission to report externally.

<!-- zh-CN:begin 647f6134aa0aa88e -->

- 绝不向子代理提供 Slack token、发帖指令、用于发帖的来源坐标或对外报告权限。

<!-- zh-CN:end 647f6134aa0aa88e -->
- If a child needs Slack write access to run, do not launch it.

<!-- zh-CN:begin 7b883ff7bf66bb0e -->

- 如果子代理需要 Slack 写权限才能运行，不要启动它。

<!-- zh-CN:end 7b883ff7bf66bb0e -->
- Utility bots are evidence sources. They do not own the fix unless a person explicitly delegated the fix to them.

<!-- zh-CN:begin 88b3b0aea7a5ee63 -->

- 工具机器人是证据来源。除非有人明确委派其修复，否则它们不负责修复。

<!-- zh-CN:end 88b3b0aea7a5ee63 -->
- The exact discriminating symptom must appear twice through real UI interaction.

<!-- zh-CN:begin 06a680d65c786877 -->

- 必须通过真实 UI 交互两次出现能够明确区分问题的相同症状。

<!-- zh-CN:end 06a680d65c786877 -->
- State inspection may confirm an observation. It must not inject or force the symptom.

<!-- zh-CN:begin 942d95b804890c32 -->

- 状态检查可以确认观察结果，但不得注入或强制制造症状。

<!-- zh-CN:end 942d95b804890c32 -->
- No confirmed repro means no authored fix.

<!-- zh-CN:begin e2845f2a8e34eefa -->

- 未确认复现，就不得编写修复。

<!-- zh-CN:end e2845f2a8e34eefa -->
- Existing pull requests or commits switch the run to verify mode. Do not author over them.

<!-- zh-CN:begin 666e5e2152922073 -->

- 已有拉取请求或提交时，运行切换为验证模式。不要在其上另写修复。

<!-- zh-CN:end 666e5e2152922073 -->
- Use `github.com` pull request links.

<!-- zh-CN:begin 563567597fb4daba -->

- 使用 `github.com` 拉取请求链接。

<!-- zh-CN:end 563567597fb4daba -->
- Keep captures, recordings, logs, and tokens out of source control.

<!-- zh-CN:begin e021430b1221d222 -->

- 截图、录屏、日志和 token 不得进入源代码版本控制。

<!-- zh-CN:end e021430b1221d222 -->
- Use pstack's `principle-guard-the-context-window` for delegated analysis.

<!-- zh-CN:begin c1f6a896f540689a -->

- 对委派分析使用 pstack 的 `principle-guard-the-context-window`。

<!-- zh-CN:end c1f6a896f540689a -->
- Apply pstack's `principle-sequence-verifiable-units`, `principle-fix-root-causes`, and `principle-prove-it-works` through repro, fix, and verification.

<!-- zh-CN:begin 916d577732743cc8 -->

- 在复现、修复和验证全过程应用 pstack 的 `principle-sequence-verifiable-units`、`principle-fix-root-causes` 和 `principle-prove-it-works`。

<!-- zh-CN:end 916d577732743cc8 -->

## 1. Freeze source coordinates

<!-- zh-CN:begin 9496d737ebe42089 -->

## 1. 固定来源坐标

<!-- zh-CN:end 9496d737ebe42089 -->

Before making a work list or delegating:

<!-- zh-CN:begin 2ed063f801cfc5a0 -->

创建工作清单或委派前：

<!-- zh-CN:end 2ed063f801cfc5a0 -->

1. Require the trigger channel to equal the configured source channel.

<!-- zh-CN:begin ed65717fcf1a0335 -->

1. 要求触发器频道与配置的来源频道一致。

<!-- zh-CN:end ed65717fcf1a0335 -->
2. Set `SOURCE_THREAD_TS` to `trigger.thread_ts` when present. Otherwise use `trigger.ts`.

<!-- zh-CN:begin f7ec1aed1ea889dd -->

2. 若存在 `trigger.thread_ts`，将 `SOURCE_THREAD_TS` 设为它；否则使用 `trigger.ts`。

<!-- zh-CN:end f7ec1aed1ea889dd -->
3. Require a nonempty `SOURCE_THREAD_TS`.

<!-- zh-CN:begin afbda92d5af74111 -->

3. 要求 `SOURCE_THREAD_TS` 非空。

<!-- zh-CN:end afbda92d5af74111 -->
4. Store `SOURCE_CHANNEL_ID` and `SOURCE_THREAD_TS` as immutable values.

<!-- zh-CN:begin 5e0a618e5d8cde1c -->

4. 将 `SOURCE_CHANNEL_ID` 和 `SOURCE_THREAD_TS` 存为不可变值。

<!-- zh-CN:end 5e0a618e5d8cde1c -->
5. Read the source thread and verify its root has those exact coordinates.

<!-- zh-CN:begin 540b5fdc7f63b6bd -->

5. 读取来源讨论串，核实根消息坐标完全一致。

<!-- zh-CN:end 540b5fdc7f63b6bd -->
6. Fetch the source permalink.

<!-- zh-CN:begin c1a1ba9b791c9f50 -->

6. 获取来源永久链接。

<!-- zh-CN:end c1a1ba9b791c9f50 -->

Never replace these values with a reply timestamp, operations timestamp, or status-message timestamp.

<!-- zh-CN:begin 814bfcceaed351e2 -->

绝不把这些值替换为回复时间戳、运维时间戳或状态消息时间戳。

<!-- zh-CN:end 814bfcceaed351e2 -->

Before every source-channel post:

<!-- zh-CN:begin 5d683b90a7c17aca -->

每次向来源频道发帖前：

<!-- zh-CN:end 5d683b90a7c17aca -->

1. Read the thread by the immutable coordinates.

<!-- zh-CN:begin 0e685a3fe309f4e8 -->

1. 按不可变坐标读取讨论串。

<!-- zh-CN:end 0e685a3fe309f4e8 -->
2. Confirm the parent exists, is not deleted, and still belongs to the source channel.

<!-- zh-CN:begin a169fbf8a78a075d -->

2. 确认父消息存在、未被删除，且仍属于来源频道。

<!-- zh-CN:end a169fbf8a78a075d -->
3. Send only with `channel=SOURCE_CHANNEL_ID` and `thread_ts=SOURCE_THREAD_TS`.

<!-- zh-CN:begin 2ac52aab251617b2 -->

3. 仅使用 `channel=SOURCE_CHANNEL_ID` 和 `thread_ts=SOURCE_THREAD_TS` 发送。

<!-- zh-CN:end 2ac52aab251617b2 -->
4. Read the thread again and verify the new message is a reply.

<!-- zh-CN:begin d16b872e68c4c213 -->

4. 再读讨论串，核实新消息是回复。

<!-- zh-CN:end d16b872e68c4c213 -->

If any check fails, post nothing. Never retry at the root or in a fallback channel.

<!-- zh-CN:begin bab8cae9a74ced72 -->

任何检查失败，都不发帖。绝不在根层级或备用频道重试。

<!-- zh-CN:end bab8cae9a74ced72 -->

## 2. Wait for the triage contract

<!-- zh-CN:begin 6f42d3a89e2b6539 -->

## 2. 等待分诊约定

<!-- zh-CN:end 6f42d3a89e2b6539 -->

Watch the source thread for the configured verdict budget. Stay silent while waiting.

<!-- zh-CN:begin 9468d45f4db09b7a -->

在配置的结论等待预算内观察来源讨论串。等待时保持安静。

<!-- zh-CN:end 9468d45f4db09b7a -->

Accept a verdict only when:

<!-- zh-CN:begin 363824007535db46 -->

只有满足以下条件才接受结论：

<!-- zh-CN:end 363824007535db46 -->

- Its author matches `slack.triage_identity_user_id`.

<!-- zh-CN:begin dfaaca80d6d8aad3 -->

- 作者匹配 `slack.triage_identity_user_id`。

<!-- zh-CN:end dfaaca80d6d8aad3 -->
- It is a reply under `SOURCE_THREAD_TS`.

<!-- zh-CN:begin 658a28d8fd95cce0 -->

- 它是 `SOURCE_THREAD_TS` 下的回复。

<!-- zh-CN:end 658a28d8fd95cce0 -->
- It contains exactly one configured marker.

<!-- zh-CN:begin 52ec1a42913b27a0 -->

- 恰好包含一个已配置标记。

<!-- zh-CN:end 52ec1a42913b27a0 -->

Public marker forms:

<!-- zh-CN:begin 97d9d9efd2287ce8 -->

公开标记格式：

<!-- zh-CN:end 97d9d9efd2287ce8 -->

```text
[benny:bug]
[benny:bug] tracker=https://tracker.example/issue/123
[benny:performance]
[benny:performance] tracker=https://tracker.example/issue/123
[benny:other]
```

Proceed only for `bug` or `performance`. Capture the optional tracker URL. Stop silently for `other`, a missing verdict, an untrusted author, conflicting markers, or a timeout.

<!-- zh-CN:begin 1401c0d9fcf0bbae -->

只对 `bug` 或 `performance` 继续。记录可选的跟踪器 URL。遇到 `other`、缺少结论、不可信作者、标记冲突或超时，静默停止。

<!-- zh-CN:end 1401c0d9fcf0bbae -->

This marker replaces private bot identities and free-form verdict matching.

<!-- zh-CN:begin 8ff4474ca6aea5a4 -->

该标记取代私有机器人身份及自由文本结论匹配。

<!-- zh-CN:end 8ff4474ca6aea5a4 -->

## 3. Apply ownership and fix-artifact gates

<!-- zh-CN:begin dd314ee856fb4259 -->

## 3. 应用负责人及修复制品门槛

<!-- zh-CN:end dd314ee856fb4259 -->

Re-read the thread immediately before starting work.

<!-- zh-CN:begin 9f10644309eb5dad -->

开始工作前立即重新读取讨论串。

<!-- zh-CN:end 9f10644309eb5dad -->

### Someone is explicitly fixing it

<!-- zh-CN:begin e481f4654309f7c2 -->

### 有人明确正在修复

<!-- zh-CN:end e481f4654309f7c2 -->

Stop when a person clearly claims the fix, gives a concrete implementation plan, or asks another agent to implement, patch, fix, or open a pull request.

<!-- zh-CN:begin 8f005042f95aaee7 -->

当某人明确认领修复、给出具体实现计划，或要求另一个代理实现、打补丁、修复或创建拉取请求时，停止。

<!-- zh-CN:end 8f005042f95aaee7 -->

Do not treat these as fix ownership:

<!-- zh-CN:begin eac84876685bee94 -->

不要把以下情况视为认领修复：

<!-- zh-CN:end eac84876685bee94 -->

- A bot summarizes evidence.

<!-- zh-CN:begin 0086b47b0a1368cb -->

- 机器人总结证据。

<!-- zh-CN:end 0086b47b0a1368cb -->
- A tool looks up logs or tickets.

<!-- zh-CN:begin 2a7a33e187641cec -->

- 工具查找日志或工单。

<!-- zh-CN:end 2a7a33e187641cec -->
- Someone asks a bot to diagnose, explain, inspect, or reproduce.

<!-- zh-CN:begin 44fa37f0b8a4ee9a -->

- 有人要求机器人诊断、解释、检查或复现。

<!-- zh-CN:end 44fa37f0b8a4ee9a -->
- A bot posts a cause hypothesis without agreeing to implement it.

<!-- zh-CN:begin 9b4ea51139f90307 -->

- 机器人发布原因假设，却未同意实现。

<!-- zh-CN:end 9b4ea51139f90307 -->

Judge the requested action, not the presence of a bot.

<!-- zh-CN:begin 96e1a99f6523c1a5 -->

判断所请求的动作，而非是否出现机器人。

<!-- zh-CN:end 96e1a99f6523c1a5 -->

### A fix artifact already exists

<!-- zh-CN:begin a71333b3adaefee0 -->

### 已经存在修复制品

<!-- zh-CN:end a71333b3adaefee0 -->

If an open pull request or merged commit plausibly fixes this report, switch to `references/verify-existing-fix.md`.

<!-- zh-CN:begin 9f30783ca8e66a58 -->

如果一个未关闭的拉取请求或已合并提交可能修复此报告，切换到 `references/verify-existing-fix.md`。

<!-- zh-CN:end 9f30783ca8e66a58 -->

An artifact may come from the thread, tracker issue, repository history, or pull request search. A claim without a commit or pull request is not a fix artifact.

<!-- zh-CN:begin 294e0f954dff3158 -->

制品可能来自讨论串、跟踪器问题、仓库历史或拉取请求搜索。没有提交或拉取请求支撑的声称，不属于修复制品。

<!-- zh-CN:end 294e0f954dff3158 -->

If a person owns the work but has not produced an artifact, stop. Do not race them.

<!-- zh-CN:begin cdaa3d88fac373bf -->

如果有人负责此工作但尚未产生制品，停止。不要与其竞速。

<!-- zh-CN:end cdaa3d88fac373bf -->

## 4. Open an optional operations thread

<!-- zh-CN:begin eaad64b3449403e6 -->

## 4. 打开可选的运维讨论串

<!-- zh-CN:end eaad64b3449403e6 -->

If `slack.operations_channel_id` is configured, the coordinator may create one root status message there. This is the only allowed root post in the repro workflow.

<!-- zh-CN:begin 9592772fb3bd3934 -->

如果配置了 `slack.operations_channel_id`，协调者可以在那里创建一条根状态消息。这是复现工作流唯一允许的根发帖。

<!-- zh-CN:end 9592772fb3bd3934 -->

Store its coordinates as `OPERATIONS_CHANNEL_ID` and `OPERATIONS_THREAD_TS`. Never confuse them with the source coordinates.

<!-- zh-CN:begin fb0241056cf4b5e6 -->

将其坐标存为 `OPERATIONS_CHANNEL_ID` 和 `OPERATIONS_THREAD_TS`。绝不要与来源坐标混淆。

<!-- zh-CN:end fb0241056cf4b5e6 -->

Use the configured plain Unicode status strings. Keep status text short:

<!-- zh-CN:begin c8a257d8a31c0bc4 -->

使用配置的普通 Unicode 状态字符串。状态文字保持简短：

<!-- zh-CN:end c8a257d8a31c0bc4 -->

- Reproducing

<!-- zh-CN:begin 5e6ea76cd92cb6ab -->

- Reproducing（正在复现）

<!-- zh-CN:end 5e6ea76cd92cb6ab -->
- Could not reproduce

<!-- zh-CN:begin 97c0ec9f046c9fb2 -->

- Could not reproduce（无法复现）

<!-- zh-CN:end 97c0ec9f046c9fb2 -->
- Blocked

<!-- zh-CN:begin cbc224a7d58824e3 -->

- Blocked（受阻）

<!-- zh-CN:end cbc224a7d58824e3 -->
- Reproduced

<!-- zh-CN:begin 0fa390cd6fa52a06 -->

- Reproduced（已复现）

<!-- zh-CN:end 0fa390cd6fa52a06 -->
- Verifying existing fix

<!-- zh-CN:begin 3a9fba4feebb993c -->

- Verifying existing fix（正在验证已有修复）

<!-- zh-CN:end 3a9fba4feebb993c -->
- Attempting bounded fix

<!-- zh-CN:begin af1526d67d722ebe -->

- Attempting bounded fix（正在尝试范围受限的修复）

<!-- zh-CN:end af1526d67d722ebe -->
- Draft pull request opened

<!-- zh-CN:begin 21ea65437e1e22f1 -->

- Draft pull request opened（已创建草稿拉取请求）

<!-- zh-CN:end 21ea65437e1e22f1 -->
- Fix did not land

<!-- zh-CN:begin eeb7f9c05af7e70e -->

- Fix did not land（修复未能落地）

<!-- zh-CN:end eeb7f9c05af7e70e -->

Prefer configured Cursor Slack actions. Use `BENNY_SLACK_BOT_TOKEN` only when the user configured it for a narrow missing capability such as editing this one status message. Never expose the token to a worker.

<!-- zh-CN:begin ec30b0737cb88d26 -->

优先使用配置的 Cursor Slack 操作。仅当用户为某项狭窄的缺失能力配置了 `BENNY_SLACK_BOT_TOKEN` 时才使用它，例如编辑这一条状态消息。绝不向工作代理暴露 token。

<!-- zh-CN:end ec30b0737cb88d26 -->

If no operations channel is configured, keep detailed status in the automation run output. Do not substitute a source-channel root message.

<!-- zh-CN:begin 0ecd39f8eb930d6c -->

如果没有配置运维频道，把详细状态留在自动化运行输出中。不要用来源频道根消息代替。

<!-- zh-CN:end 0ecd39f8eb930d6c -->

## 5. Load and check the control adapter

<!-- zh-CN:begin ceb398a1116c8776 -->

## 5. 加载并检查控制适配器

<!-- zh-CN:end ceb398a1116c8776 -->

Read `references/control-adapter.md` and the completed map at `control.feature_map_path`, then invoke the skill named by `control.skill_name`.

<!-- zh-CN:begin 3803920c262743e9 -->

读取 `references/control-adapter.md` 及 `control.feature_map_path` 中已完成的映射，然后调用 `control.skill_name` 指定的技能。

<!-- zh-CN:end 3803920c262743e9 -->

Find the feature-map section that matches the reported user path. Read it before driving the app. If no section covers the feature, mark the run blocked instead of inventing a path or selector.

<!-- zh-CN:begin 061db46a98142e21 -->

找到与报告中用户路径匹配的功能映射章节。操作应用前先阅读它。若没有章节覆盖该功能，应把运行标为受阻，而非编造路径或选择器。

<!-- zh-CN:end 061db46a98142e21 -->

Require all seven capabilities:

<!-- zh-CN:begin 15cfd5f00cbb5cb0 -->

要求具备全部七项能力：

<!-- zh-CN:end 15cfd5f00cbb5cb0 -->

1. Bring up the configured target app and test environment.

<!-- zh-CN:begin e5ca4511d68605d6 -->

1. 启动配置的目标应用和测试环境。

<!-- zh-CN:end e5ca4511d68605d6 -->
2. Navigate the mapped feature and exercise its documented states.

<!-- zh-CN:begin 0717827f0c45a38a -->

2. 导航到映射的功能并操作其文档化状态。

<!-- zh-CN:end 0717827f0c45a38a -->
3. Drive the real UI with clicks, typing, keys, scrolling, drag, resize, or navigation.

<!-- zh-CN:begin cef111f6e3a39028 -->

3. 通过点击、输入、按键、滚动、拖动、调整大小或导航来操作真实 UI。

<!-- zh-CN:end cef111f6e3a39028 -->
4. Inspect state without mutating it.

<!-- zh-CN:begin 4137fb36e3869299 -->

4. 在不修改状态的情况下检查状态。

<!-- zh-CN:end 4137fb36e3869299 -->
5. Capture screenshots.

<!-- zh-CN:begin 9dc8f4c66a1de622 -->

5. 截图。

<!-- zh-CN:end 9dc8f4c66a1de622 -->
6. Start and stop a screen recording.

<!-- zh-CN:begin f02ed208193eee04 -->

6. 开始和停止录屏。

<!-- zh-CN:end f02ed208193eee04 -->
7. Clean up processes, sessions, profiles, and temporary data.

<!-- zh-CN:begin e6345ba9d7b1d7ce -->

7. 清理进程、会话、配置档和临时数据。

<!-- zh-CN:end e6345ba9d7b1d7ce -->

If the adapter is absent or any required capability is missing, mark the operations status as blocked and stop. Do not pretend a screenshot, unit test, state mutation, or source reading is a UI repro.

<!-- zh-CN:begin 164211157359a3bf -->

若缺少适配器或任何必需能力，将运维状态标为受阻并停止。不要把截图、单元测试、状态修改或阅读源码伪称为 UI 复现。

<!-- zh-CN:end 164211157359a3bf -->

## 6. Study the report

<!-- zh-CN:begin 45bdf8f6729e3cc3 -->

## 6. 研究报告

<!-- zh-CN:end 45bdf8f6729e3cc3 -->

Read the full source thread and tracker issue when present.

<!-- zh-CN:begin 1d1120f3c3f0ed9d -->

读取完整来源讨论串，以及存在时的跟踪器问题。

<!-- zh-CN:end 1d1120f3c3f0ed9d -->

Collect:

<!-- zh-CN:begin 10ce6118589163cd -->

收集：

<!-- zh-CN:end 10ce6118589163cd -->

- Exact action path

<!-- zh-CN:begin da379137e6f4d6b1 -->

- 精确操作路径

<!-- zh-CN:end da379137e6f4d6b1 -->
- Expected behavior

<!-- zh-CN:begin 200d9888a93a9670 -->

- 预期行为

<!-- zh-CN:end 200d9888a93a9670 -->
- Observed behavior

<!-- zh-CN:begin 64258ae4843a9841 -->

- 观察到的行为

<!-- zh-CN:end 64258ae4843a9841 -->
- Discriminating state where they diverge

<!-- zh-CN:begin f3c295b5040dc6aa -->

- 二者分歧处的判别状态

<!-- zh-CN:end f3c295b5040dc6aa -->
- Frequency

<!-- zh-CN:begin d68d0fd204b2cef5 -->

- 发生频率

<!-- zh-CN:end d68d0fd204b2cef5 -->
- Version, environment, and platform

<!-- zh-CN:begin ef5b2b53a66b4e70 -->

- 版本、环境和平台

<!-- zh-CN:end ef5b2b53a66b4e70 -->
- Attachments and error signatures

<!-- zh-CN:begin 2b7604c43b45fdb0 -->

- 附件及错误特征

<!-- zh-CN:end 2b7604c43b45fdb0 -->
- Candidate code area

<!-- zh-CN:begin 58bda34dc7b25611 -->

- 候选代码区域

<!-- zh-CN:end 58bda34dc7b25611 -->

Inspect screenshots and video. Use read-only parallel workers for code history, test ideas, blast-radius mapping, and media review when useful. Each worker gets a narrow question and the Slack-write prohibition.

<!-- zh-CN:begin 4dfde9c37b499600 -->

检查截图和视频。在有帮助时，使用只读并行工作代理研究代码历史、测试思路、影响范围映射及媒体审查。每个工作代理都获得一个范围狭窄的问题，以及禁止 Slack 写入的要求。

<!-- zh-CN:end 4dfde9c37b499600 -->

Use pstack's `how` skill to trace the action through the repository. Use `why` for regression history and defensive code. Form competing cause hypotheses and identify evidence that would separate them.

<!-- zh-CN:begin b5b439c52cbbc0e7 -->

使用 pstack 的 `how` 技能，在仓库中跟踪操作路径。对回归历史和防御性代码使用 `why`。形成相互竞争的原因假设，并找出可以区分它们的证据。

<!-- zh-CN:end b5b439c52cbbc0e7 -->

## 7. Reproduce

<!-- zh-CN:begin d34e8815f9419fce -->

## 7. 复现

<!-- zh-CN:end d34e8815f9419fce -->

Bring up the target app through the control adapter.

<!-- zh-CN:begin 4d2e2284e5fbe121 -->

通过控制适配器启动目标应用。

<!-- zh-CN:end 4d2e2284e5fbe121 -->

Confirm the correct app, workspace, account, data set, and feature state before acting. Use stable app markers. Do not rely on window order or a familiar title alone.

<!-- zh-CN:begin a992e0f0915db085 -->

操作前确认应用、工作区、账户、数据集及功能状态正确。使用稳定的应用标记。不要只依赖窗口顺序或熟悉的标题。

<!-- zh-CN:end a992e0f0915db085 -->

Drive the reported path through real UI actions.

<!-- zh-CN:begin cc43534a837dfea3 -->

通过真实 UI 操作执行报告路径。

<!-- zh-CN:end cc43534a837dfea3 -->

Before calling it reproduced:

<!-- zh-CN:begin 3f7abfe0edc9df8a -->

声称复现前：

<!-- zh-CN:end 3f7abfe0edc9df8a -->

1. Name the correct final state.

<!-- zh-CN:begin d3dd27ec5bbd2377 -->

1. 指明正确的最终状态。

<!-- zh-CN:end d3dd27ec5bbd2377 -->
2. Name the broken final state.

<!-- zh-CN:begin d7bd6c0b9dd46e8c -->

2. 指明出错的最终状态。

<!-- zh-CN:end d7bd6c0b9dd46e8c -->
3. Reach the point where they diverge.

<!-- zh-CN:begin 3fd10d3a26884dc9 -->

3. 到达二者发生分歧的位置。

<!-- zh-CN:end 3fd10d3a26884dc9 -->
4. Observe the broken state.

<!-- zh-CN:begin 3a81af782017b40e -->

4. 观察出错状态。

<!-- zh-CN:end 3a81af782017b40e -->
5. Reset enough state to make the second attempt independent.

<!-- zh-CN:begin 4f0996544887cecd -->

5. 重置足够的状态，使第二次尝试独立。

<!-- zh-CN:end 4f0996544887cecd -->
6. Repeat the same path and observe the same broken state again.

<!-- zh-CN:begin 511fb988ff675f07 -->

6. 重复相同路径，再次观察到相同的出错状态。

<!-- zh-CN:end 511fb988ff675f07 -->
7. Cross-check a real state value when possible.

<!-- zh-CN:begin 89582a1ab0a603c1 -->

7. 条件允许时，交叉检查一个真实状态值。

<!-- zh-CN:end 89582a1ab0a603c1 -->

An expected dialog, loading state, or setup step is not the bug. Capture the final state that distinguishes correct from broken behavior.

<!-- zh-CN:begin 8cc7b7b3c60f1695 -->

预期中的对话框、加载状态或设置步骤不是 bug。捕获能区分正确和错误行为的最终状态。

<!-- zh-CN:end 8cc7b7b3c60f1695 -->

Use the configured repro budget. If the symptom does not reproduce within it, report a clean `Could not reproduce` outcome. If the environment cannot provide a required capability, report `Blocked` and state what was missing.

<!-- zh-CN:begin 83b2b1e1fc896ab8 -->

使用配置的复现预算。若预算内症状未复现，明确报告 `Could not reproduce`。若环境无法提供某项必需能力，报告 `Blocked` 并说明缺少什么。

<!-- zh-CN:end 83b2b1e1fc896ab8 -->

## 8. Capture and review evidence

<!-- zh-CN:begin dc802ac4b469f475 -->

## 8. 捕获并审查证据

<!-- zh-CN:end dc802ac4b469f475 -->

For a successful repro:

<!-- zh-CN:begin adb4b793181f46d3 -->

成功复现时：

<!-- zh-CN:end adb4b793181f46d3 -->

- Record the full path through the symptom.

<!-- zh-CN:begin d10f89dfabdf5dbd -->

- 录下直至症状出现的完整路径。

<!-- zh-CN:end d10f89dfabdf5dbd -->
- Capture a screenshot of the broken final state.

<!-- zh-CN:begin f816642d449c1c82 -->

- 对出错的最终状态截图。

<!-- zh-CN:end f816642d449c1c82 -->
- Save a short note with the exact steps and observed state.

<!-- zh-CN:begin 98e3865f9b3de81d -->

- 保存简短说明，写明精确步骤和观察到的状态。

<!-- zh-CN:end 98e3865f9b3de81d -->
- Keep artifacts in the configured temporary artifact directory.

<!-- zh-CN:begin 0105b177ad811567 -->

- 将制品保存在配置的临时制品目录。

<!-- zh-CN:end 0105b177ad811567 -->

Have a read-only media reviewer answer one question: does the evidence visibly show the discriminating broken state?

<!-- zh-CN:begin 90ba2ee1b10024e3 -->

让一位只读媒体审查者回答一个问题：证据是否清楚展示了具有判别作用的出错状态？

<!-- zh-CN:end 90ba2ee1b10024e3 -->

If the answer is no or uncertain, the repro is not confirmed. Capture better evidence or use `Could not reproduce`.

<!-- zh-CN:begin 75bb3af945e41b7a -->

如果答案是否定或不确定，则复现尚未确认。获取更好的证据，或使用 `Could not reproduce`。

<!-- zh-CN:end 75bb3af945e41b7a -->

Post detailed evidence only in the operations thread when configured. Keep the source update concise.

<!-- zh-CN:begin 08af4ce0f1f55d09 -->

若配置了运维讨论串，仅在那里发布详细证据。来源更新保持简洁。

<!-- zh-CN:end 08af4ce0f1f55d09 -->

## 9. Report the repro outcome

<!-- zh-CN:begin 5bbebbda67af25f4 -->

## 9. 报告复现结果

<!-- zh-CN:end 5bbebbda67af25f4 -->

Update the operations status first.

<!-- zh-CN:begin f973d69da2e169b4 -->

先更新运维状态。

<!-- zh-CN:end f973d69da2e169b4 -->

For `Could not reproduce` or `Blocked`, post nothing in the source thread. The operations thread or run output carries the result.

<!-- zh-CN:begin 423264bc673e3630 -->

对于 `Could not reproduce` 或 `Blocked`，不在来源讨论串发帖。结果放在运维讨论串或运行输出中。

<!-- zh-CN:end 423264bc673e3630 -->

For a confirmed repro, run the source preflight and post at most one unprompted source reply:

<!-- zh-CN:begin a0627aaf8e61e381 -->

对于已确认复现，执行来源预检，并最多主动发布一条来源回复：

<!-- zh-CN:end a0627aaf8e61e381 -->

- Say the issue reproduced.

<!-- zh-CN:begin f7c2acf39dd95ec7 -->

- 说明问题已复现。

<!-- zh-CN:end f7c2acf39dd95ec7 -->
- Link the operations evidence thread when one exists.

<!-- zh-CN:begin 1ff651baa77fcbab -->

- 如有运维证据讨论串，附上链接。

<!-- zh-CN:end 1ff651baa77fcbab -->
- Include at most three short findings.

<!-- zh-CN:begin d476b142c0c088ba -->

- 最多包含三条简短发现。

<!-- zh-CN:end d476b142c0c088ba -->
- Link the tracker issue when one exists.

<!-- zh-CN:begin e7ac8e71777f098c -->

- 如有跟踪器问题，附上链接。

<!-- zh-CN:end e7ac8e71777f098c -->
- Do not ping an owner by default.

<!-- zh-CN:begin 755448bbd60fc4aa -->

- 默认不 @ 负责人。

<!-- zh-CN:end 755448bbd60fc4aa -->

Attach evidence only when the configured Slack action keeps it inside the same source thread and the organization's retention policy allows it.

<!-- zh-CN:begin 301ce58d165617f6 -->

只有已配置的 Slack 操作能使证据留在同一来源讨论串，且组织保留策略允许时，才附加证据。

<!-- zh-CN:end 301ce58d165617f6 -->

Wait for the configured rejection window. If a person shows that the setup or interpretation was wrong, correct the repro once. Do not start the fix phase until the window closes without a valid rejection.

<!-- zh-CN:begin d69d55836c6f691a -->

等待配置的异议窗口。如果有人证明设置或理解有误，修正一次复现。窗口结束且没有有效异议前，不得开始修复阶段。

<!-- zh-CN:end d69d55836c6f691a -->

## 10. Verify an existing fix

<!-- zh-CN:begin 5fd51ec4caca2699 -->

## 10. 验证已有修复

<!-- zh-CN:end 5fd51ec4caca2699 -->

When a fix artifact exists, follow `references/verify-existing-fix.md`.

<!-- zh-CN:begin b6cee8947f987cd3 -->

已有修复制品时，遵循 `references/verify-existing-fix.md`。

<!-- zh-CN:end b6cee8947f987cd3 -->

Verification must show the symptom on the baseline and its absence on the patched build. Both paths use the real UI twice.

<!-- zh-CN:begin 73a8b8f6c55c66ed -->

验证必须展示：症状在基线版本出现，在补丁构建中消失。两条路径都要通过真实 UI 各执行两次。

<!-- zh-CN:end 73a8b8f6c55c66ed -->

Do not edit the existing fix, add a competing patch, or open a replacement pull request.

<!-- zh-CN:begin 951be712a37eca31 -->

不要编辑已有修复、添加竞争补丁或创建替代拉取请求。

<!-- zh-CN:end 951be712a37eca31 -->

## 11. Qualify a bounded fix

<!-- zh-CN:begin ca92ff07cf67f128 -->

## 11. 判断是否可尝试范围受限的修复

<!-- zh-CN:end ca92ff07cf67f128 -->

Attempt a fix only when all of these hold:

<!-- zh-CN:begin 2ebb9ade82d862b6 -->

只有全部满足以下条件，才尝试修复：

<!-- zh-CN:end 2ebb9ade82d862b6 -->

- The outcome is a plain confirmed repro.

<!-- zh-CN:begin 5fa28fb5164ce304 -->

- 结果是明确确认的复现。

<!-- zh-CN:end 5fa28fb5164ce304 -->
- Media review confirmed the broken final state.

<!-- zh-CN:begin 1addb1ef1f302a88 -->

- 媒体审查确认了出错的最终状态。

<!-- zh-CN:end 1addb1ef1f302a88 -->
- No existing fix artifact appeared.

<!-- zh-CN:begin 62d46690f5e455f0 -->

- 没有出现已有修复制品。

<!-- zh-CN:end 62d46690f5e455f0 -->
- No person claimed the fix during the rejection window.

<!-- zh-CN:begin 296926860071085c -->

- 异议窗口内无人认领修复。

<!-- zh-CN:end 296926860071085c -->
- Runtime evidence identifies the root cause.

<!-- zh-CN:begin 9da6fad18287873a -->

- 运行时证据确定了根因。

<!-- zh-CN:end 9da6fad18287873a -->
- The likely change fits the configured fix budget and repository scope.

<!-- zh-CN:begin 7d3c3c385a995937 -->

- 预计变更符合配置的修复预算和仓库范围。

<!-- zh-CN:end 7d3c3c385a995937 -->
- The control adapter can run both baseline and patched builds.

<!-- zh-CN:begin 1bbbedcbc6d2c4ca -->

- 控制适配器能运行基线和补丁构建。

<!-- zh-CN:end 1bbbedcbc6d2c4ca -->

If any condition fails, keep the repro report and stop without a pull request.

<!-- zh-CN:begin 602cfb9470d0c13f -->

任何条件不满足，保留复现报告并停止，不创建拉取请求。

<!-- zh-CN:end 602cfb9470d0c13f -->

When the gate passes, update operations status to `Attempting bounded fix`.

<!-- zh-CN:begin aaebd151581e0d72 -->

通过门槛后，将运维状态更新为 `Attempting bounded fix`。

<!-- zh-CN:end aaebd151581e0d72 -->

## 12. Root-cause and implement

<!-- zh-CN:begin 92640943c2122855 -->

## 12. 确定根因并实现

<!-- zh-CN:end 92640943c2122855 -->

The coordinator owns every Slack post, the final diff review, commits, and the pull request.

<!-- zh-CN:begin d4a39fc7838095fd -->

协调者负责每一次 Slack 发帖、最终 diff 审查、提交和拉取请求。

<!-- zh-CN:end d4a39fc7838095fd -->

Read-only workers may:

<!-- zh-CN:begin 331805cb1f9bb795 -->

只读工作代理可以：

<!-- zh-CN:end 331805cb1f9bb795 -->

- Trace code and history

<!-- zh-CN:begin 35e73afb9cd8f328 -->

- 跟踪代码和历史

<!-- zh-CN:end 35e73afb9cd8f328 -->
- Propose tests

<!-- zh-CN:begin b84ffa1336d3cb9e -->

- 提出测试

<!-- zh-CN:end b84ffa1336d3cb9e -->
- Map blast radius

<!-- zh-CN:begin 5fc06609df20ddd1 -->

- 映射影响范围

<!-- zh-CN:end 5fc06609df20ddd1 -->
- Review a diff

<!-- zh-CN:begin 27fab4cf55285cb4 -->

- 审查 diff

<!-- zh-CN:end 27fab4cf55285cb4 -->
- Review media

<!-- zh-CN:begin d2e18b6b4b32cf50 -->

- 审查媒体

<!-- zh-CN:end d2e18b6b4b32cf50 -->

They do not edit, run external writes, post status, or own the fix.

<!-- zh-CN:begin ff302913feb0e121 -->

它们不得编辑、执行外部写入、发布状态或负责修复。

<!-- zh-CN:end ff302913feb0e121 -->

A tightly scoped code edit may be delegated during this phase only when tool isolation removes Slack credentials and every Slack write action from that worker. Its prompt must still carry the explicit Slack-write ban. The coordinator reviews the edit and runs or verifies the required tests. If tool isolation is uncertain, keep the edit in the coordinator.

<!-- zh-CN:begin 97252993ecbe0bf3 -->

在此阶段，只有工具隔离已从工作代理移除 Slack 凭据及所有 Slack 写操作时，才可委派范围严格受限的代码编辑。其提示词仍必须明确禁止 Slack 写入。协调者审查编辑，并运行或验证所需测试。如果无法确定工具隔离有效，编辑工作保留给协调者。

<!-- zh-CN:end 97252993ecbe0bf3 -->

Confirm the mechanism with runtime evidence. Eliminate competing hypotheses before editing.

<!-- zh-CN:begin 47d4b2cb32f4c64d -->

用运行时证据确认机制。编辑前排除相互竞争的假设。

<!-- zh-CN:end 47d4b2cb32f4c64d -->

Fix the root cause with the smallest justified change.

<!-- zh-CN:begin 8f36112789f0317c -->

以最小且有依据的变更修复根因。

<!-- zh-CN:end 8f36112789f0317c -->

- Invoke pstack's `tdd` skill when there is a cheap local test target, and write the failing test before the fix.

<!-- zh-CN:begin a8738366b01ba585 -->

- 存在低成本本地测试目标时，调用 pstack 的 `tdd` 技能，并在修复前先写失败测试。

<!-- zh-CN:end a8738366b01ba585 -->
- State why TDD was skipped when the path is expensive, unclear, or integration-heavy.

<!-- zh-CN:begin 3ec97229dc2ff2cf -->

- 路径成本高、不明确或高度依赖集成时，说明跳过 TDD 的原因。

<!-- zh-CN:end 3ec97229dc2ff2cf -->
- Keep unrelated cleanup out.

<!-- zh-CN:begin b980eb552541de4d -->

- 不加入无关清理。

<!-- zh-CN:end b980eb552541de4d -->
- Stop if the change grows beyond the configured effort or risk budget.

<!-- zh-CN:begin 051e28a44dbdbcc5 -->

- 若变更超出配置的工作量或风险预算，停止。

<!-- zh-CN:end 051e28a44dbdbcc5 -->

## 13. Prove the fix

<!-- zh-CN:begin b2fda54bfa4cef8d -->

## 13. 证明修复有效

<!-- zh-CN:end b2fda54bfa4cef8d -->

Keep the original baseline evidence.

<!-- zh-CN:begin 353d9dd7e1e13d08 -->

保留原始基线证据。

<!-- zh-CN:end 353d9dd7e1e13d08 -->

On the patched build:

<!-- zh-CN:begin 7b86147659ad1479 -->

在补丁构建上：

<!-- zh-CN:end 7b86147659ad1479 -->

1. Run the same real UI path.

<!-- zh-CN:begin 3ca087d8f3a3a4fb -->

1. 执行相同的真实 UI 路径。

<!-- zh-CN:end 3ca087d8f3a3a4fb -->
2. Repeat it twice.

<!-- zh-CN:begin 89f75dea50caa17e -->

2. 重复执行两次。

<!-- zh-CN:end 89f75dea50caa17e -->
3. Show that the broken state is gone.

<!-- zh-CN:begin 1cbce40c8b3f6d62 -->

3. 展示出错状态已经消失。

<!-- zh-CN:end 1cbce40c8b3f6d62 -->
4. Show the expected state in its place.

<!-- zh-CN:begin d90ff40d58b0beb1 -->

4. 展示其位置出现了预期状态。

<!-- zh-CN:end d90ff40d58b0beb1 -->
5. Capture an after recording and screenshot.

<!-- zh-CN:begin 742c2096de835a15 -->

5. 捕获修复后录屏和截图。

<!-- zh-CN:end 742c2096de835a15 -->
6. Cross-check the same real state value used for the baseline.

<!-- zh-CN:begin d938566ddf61f6cc -->

6. 交叉检查基线所用的同一个真实状态值。

<!-- zh-CN:end d938566ddf61f6cc -->

A compile, unit test, code review, or plausible diff is not after evidence.

<!-- zh-CN:begin e95dd32698446e09 -->

编译、单元测试、代码审查或看似合理的 diff，都不是修复后证据。

<!-- zh-CN:end e95dd32698446e09 -->

Run focused tests, then smoke the blast radius around the changed behavior. Cover nearby states, inputs, permissions, platforms, and failure paths that the change could affect. Stop without a pull request if a regression remains.

<!-- zh-CN:begin 3297c29534d89f47 -->

运行聚焦测试，然后对变更行为周边的影响范围做冒烟检查。覆盖变更可能影响的邻近状态、输入、权限、平台和失败路径。如果仍有回归，停止，不创建拉取请求。

<!-- zh-CN:end 3297c29534d89f47 -->

## 14. Open a draft pull request

<!-- zh-CN:begin d8590d57f0eb1c57 -->

## 14. 创建草稿拉取请求

<!-- zh-CN:end d8590d57f0eb1c57 -->

Only after before-and-after proof:

<!-- zh-CN:begin c0ed55b0040e9d82 -->

只有具备修复前后证明后：

<!-- zh-CN:end c0ed55b0040e9d82 -->

- Review the final diff for unrelated changes and secrets.

<!-- zh-CN:begin f655e2fdab2f80df -->

- 审查最终 diff，查找无关变更和机密。

<!-- zh-CN:end f655e2fdab2f80df -->
- Run the repository's required checks.

<!-- zh-CN:begin eb5eb130dee90787 -->

- 运行仓库要求的检查。

<!-- zh-CN:end eb5eb130dee90787 -->
- Create small ordered commits when the repository workflow allows it.

<!-- zh-CN:begin c3e20c6633d94b77 -->

- 仓库工作流允许时，创建小型、有序的提交。

<!-- zh-CN:end c3e20c6633d94b77 -->
- Open a draft pull request. Never merge or deploy from this workflow.

<!-- zh-CN:begin dc2176c256a2293c -->

- 创建草稿拉取请求。绝不从此工作流合并或部署。

<!-- zh-CN:end dc2176c256a2293c -->
- Link the configured tracker issue using the tracker's supported pull request syntax.

<!-- zh-CN:begin 15d68f38b0643a12 -->

- 使用跟踪器支持的拉取请求语法，关联已配置的跟踪器问题。

<!-- zh-CN:end 15d68f38b0643a12 -->
- Use the configured public URL form, normally `https://github.com/{owner}/{repo}/pull/{number}`.

<!-- zh-CN:begin ddc878edb3b33920 -->

- 使用已配置的公开 URL 形式，通常为 `https://github.com/{owner}/{repo}/pull/{number}`。

<!-- zh-CN:end ddc878edb3b33920 -->
- Include the repro steps, root cause, test result, before and after evidence, and blast-radius checks.

<!-- zh-CN:begin 54d0c43ddbfd69e7 -->

- 包含复现步骤、根因、测试结果、修改前后证据及影响范围检查。

<!-- zh-CN:end 54d0c43ddbfd69e7 -->
- Run the pull request text and all Slack updates through pstack's `unslop` skill.

<!-- zh-CN:begin 00a3c7f136f5ef94 -->

- 对拉取请求文字及所有 Slack 更新运行 pstack 的 `unslop` 技能。

<!-- zh-CN:end 00a3c7f136f5ef94 -->

If pull request creation fails, do not claim success. Keep the commit or branch state in the run output and mark operations status `Fix did not land`.

<!-- zh-CN:begin 1e4e4803f0b5d90d -->

若创建拉取请求失败，不要声称成功。保留运行输出中的提交或分支状态，并将操作状态标为 `Fix did not land`（修复未落地）。

<!-- zh-CN:end 1e4e4803f0b5d90d -->

On success, mark operations status `Draft pull request opened` and post one concise reply in the operations thread with the linked pull request. Do not create a second source-channel root or unprompted source reply.

<!-- zh-CN:begin 7257a6e88c65aa31 -->

成功后将操作状态标为 `Draft pull request opened`（已打开草稿拉取请求），并在操作线程发布一条简洁回复及拉取请求链接。不要创建第二个 source-channel 根帖或未经提示的 source 回复。

<!-- zh-CN:end 7257a6e88c65aa31 -->

## 15. Follow-ups and cleanup

<!-- zh-CN:begin 0123c0a897d05d6a -->

## 15. 后续事项与清理

<!-- zh-CN:end 0123c0a897d05d6a -->

Watch the configured operations thread for one follow-up window.

<!-- zh-CN:begin 950f3416369c6aa1 -->

观察配置的操作线程一个后续窗口。

<!-- zh-CN:end 950f3416369c6aa1 -->

- Answer a direct question from evidence already gathered.

<!-- zh-CN:begin cb51d562243c78d2 -->

- 根据已收集证据回答直接问题。

<!-- zh-CN:end cb51d562243c78d2 -->
- Apply one concrete correction and rerun the repro once when it invalidates the setup.

<!-- zh-CN:begin 36a06fcbf854eb2b -->

- 应用一项具体纠正，若它使设置失效，重新运行一次复现。

<!-- zh-CN:end 36a06fcbf854eb2b -->
- Stay out of human coordination and side chatter.

<!-- zh-CN:begin 4f176de86d1f6c42 -->

- 不要介入人类协调和闲聊。

<!-- zh-CN:end 4f176de86d1f6c42 -->
- Stop when asked.

<!-- zh-CN:begin 38743e0153f49993 -->

- 被要求时停止。

<!-- zh-CN:end 38743e0153f49993 -->

Always call the control adapter's cleanup capability. Keep artifacts only as long as the configured retention policy allows.

<!-- zh-CN:begin 4f0c899735d36039 -->

始终调用控制适配器的清理能力。仅在配置保留政策允许的期限内保留制品。

<!-- zh-CN:end 4f0c899735d36039 -->
