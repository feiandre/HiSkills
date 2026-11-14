---
name: triage-issue-reports
description: Triage Slack issue reports with one thread-only verdict, evidence review, cause-aware routing, tracker dedupe, and fail-closed ticket creation. Use only from the configured Benny triage automation.
disable-model-invocation: true

# zh-CN:begin 4cb202f59c4554a6
# name: triage-issue-reports
# description: "对 Slack 问题报告进行分诊，在原讨论串内给出一次结论，审查证据、按原因路由、在跟踪器中去重，并在不能安全创建工单时拒绝写入。仅从已配置的 Benny 分诊自动化中使用。"
# disable-model-invocation: true
# zh-CN:end 4cb202f59c4554a6
---

# Triage issue reports

<!-- zh-CN:begin e1e9c34b98bd2d86 -->

# 对问题报告进行分诊

<!-- zh-CN:end e1e9c34b98bd2d86 -->

Classify one Slack report and post one useful verdict in its source thread. Create a tracker issue only for a clear, new bug. Do not reproduce or fix it here.

<!-- zh-CN:begin 6f3b6cff88dfb4b4 -->

将一份 Slack 报告分类，并在其来源讨论串发布一个有用的结论。仅对明确的新 bug 创建跟踪器问题。不要在这里复现或修复。

<!-- zh-CN:end 6f3b6cff88dfb4b4 -->

Load the external Benny configuration supplied by the automation. If the config is missing, malformed, or incomplete, stop without posting or writing to the tracker.

<!-- zh-CN:begin 26460b374ba531d5 -->

加载自动化提供的外部 Benny 配置。如果配置缺失、格式错误或不完整，停止，不发帖，也不写入跟踪器。

<!-- zh-CN:end 26460b374ba531d5 -->

## Hard safety rules

<!-- zh-CN:begin fef18b0b36aaccb0 -->

## 强制安全规则

<!-- zh-CN:end fef18b0b36aaccb0 -->

- The source channel and root thread coordinates are immutable.

<!-- zh-CN:begin 519a3f7591fc7303 -->

- 来源频道与根讨论串坐标不可变。

<!-- zh-CN:end 519a3f7591fc7303 -->
- Never post a root message in the source channel.

<!-- zh-CN:begin 69b0749ce6d7a484 -->

- 绝不在来源频道发布根消息。

<!-- zh-CN:end 69b0749ce6d7a484 -->
- Never post to another channel, broadcast a reply, send a DM, or start a replacement thread.

<!-- zh-CN:begin e47759354b8a869f -->

- 绝不发到其他频道、广播回复、发送私信或创建替代讨论串。

<!-- zh-CN:end e47759354b8a869f -->
- Preflight the source parent before any tracker write and immediately before the verdict post.

<!-- zh-CN:begin 94ebb322ff3b0a32 -->

- 在任何跟踪器写入前，以及发布结论前的最后一刻，预检来源父消息。

<!-- zh-CN:end 94ebb322ff3b0a32 -->
- If the parent is missing, deleted, inaccessible, or uncertain, stop with no writes.

<!-- zh-CN:begin aea456b4eb7beda0 -->

- 父消息缺失、已删除、无法访问或状态不确定时，停止且不写入。

<!-- zh-CN:end aea456b4eb7beda0 -->
- Post one substantive verdict. Do not narrate progress.

<!-- zh-CN:begin 42ffb2173da540de -->

- 发布一个实质性结论，不播报进度。

<!-- zh-CN:end 42ffb2173da540de -->
- The coordinator is the only Slack poster.

<!-- zh-CN:begin c61b884099d00f5b -->

- 协调者是唯一可以在 Slack 发帖的角色。

<!-- zh-CN:end c61b884099d00f5b -->
- Delegated workers return findings only. They must be read-only and receive no Slack credentials or write actions.

<!-- zh-CN:begin 86663f7d95989875 -->

- 委派工作代理仅返回发现。它们必须只读，且不得获得 Slack 凭据或写操作。

<!-- zh-CN:end 86663f7d95989875 -->
- Every child prompt must forbid `SendSlackMessage`, `PostToSlack`, `chat.postMessage`, and every other Slack write.

<!-- zh-CN:begin af67bd37f7a60250 -->

- 每个子代理提示词必须禁止 `SendSlackMessage`、`PostToSlack`、`chat.postMessage` 及所有其他 Slack 写入。

<!-- zh-CN:end af67bd37f7a60250 -->
- If worker isolation cannot enforce those limits, do the work in the coordinator.

<!-- zh-CN:begin e03655ecf30a905f -->

- 如果工作代理隔离无法强制这些限制，由协调者执行工作。

<!-- zh-CN:end e03655ecf30a905f -->
- Never create an issue that cannot link back to the source thread.

<!-- zh-CN:begin f85a48d7a1a54d25 -->

- 绝不创建无法反向链接至来源讨论串的问题。

<!-- zh-CN:end f85a48d7a1a54d25 -->
- Prefer no ticket over a guessed or duplicate ticket.

<!-- zh-CN:begin f0f9bb5b50b9a2da -->

- 宁可不建工单，也不要创建猜测或重复工单。

<!-- zh-CN:end f0f9bb5b50b9a2da -->
- Apply pstack's `principle-separate-before-serializing-shared-state` to source coordinates.

<!-- zh-CN:begin 542d3cfdf12ab1df -->

- 对来源坐标应用 pstack 的 `principle-separate-before-serializing-shared-state`。

<!-- zh-CN:end 542d3cfdf12ab1df -->
- Apply pstack's `principle-minimize-reader-load` and `unslop` skills to the final verdict.

<!-- zh-CN:begin 30c3d36eeff34b12 -->

- 对最终结论应用 pstack 的 `principle-minimize-reader-load` 和 `unslop` 技能。

<!-- zh-CN:end 30c3d36eeff34b12 -->

## 1. Freeze source coordinates

<!-- zh-CN:begin 07044cace07fc2e1 -->

## 1. 固定来源坐标

<!-- zh-CN:end 07044cace07fc2e1 -->

Before making a work list or delegating:

<!-- zh-CN:begin 94240ce700058380 -->

创建工作清单或委派前：

<!-- zh-CN:end 94240ce700058380 -->

1. Read `source_channel_id` from the trigger.

<!-- zh-CN:begin 4a4dbd4f96aebb4b -->

1. 从触发器读取 `source_channel_id`。

<!-- zh-CN:end 4a4dbd4f96aebb4b -->
2. Require it to equal the configured source channel.

<!-- zh-CN:begin 6af0355ae6adab2a -->

2. 要求它与配置的来源频道相等。

<!-- zh-CN:end 6af0355ae6adab2a -->
3. Set `SOURCE_THREAD_TS` to `trigger.thread_ts` when present. Otherwise use `trigger.ts`.

<!-- zh-CN:begin f297b4d9ef81862d -->

3. 若存在 `trigger.thread_ts`，将 `SOURCE_THREAD_TS` 设为它；否则使用 `trigger.ts`。

<!-- zh-CN:end f297b4d9ef81862d -->
4. Require a nonempty `SOURCE_THREAD_TS`.

<!-- zh-CN:begin a827a0f3d74a8c3c -->

4. 要求 `SOURCE_THREAD_TS` 非空。

<!-- zh-CN:end a827a0f3d74a8c3c -->
5. Store `SOURCE_CHANNEL_ID` and `SOURCE_THREAD_TS` as immutable values.

<!-- zh-CN:begin 8cf2efe3737e2cb2 -->

5. 将 `SOURCE_CHANNEL_ID` 和 `SOURCE_THREAD_TS` 存为不可变值。

<!-- zh-CN:end 8cf2efe3737e2cb2 -->
6. Read the thread and verify that its root has exactly those coordinates.

<!-- zh-CN:begin 1739df90d84210fd -->

6. 读取讨论串，核实根消息坐标完全一致。

<!-- zh-CN:end 1739df90d84210fd -->
7. Fetch a stable source permalink.

<!-- zh-CN:begin 6a7a474adad1f9c6 -->

7. 获取稳定的来源永久链接。

<!-- zh-CN:end 6a7a474adad1f9c6 -->

Every later source read and post must use those stored values. Never replace them with a reply timestamp or an operations-thread timestamp.

<!-- zh-CN:begin 51e4b4cb309bd9e2 -->

后续所有来源读取和发帖都必须使用这些存储值。绝不以回复时间戳或运维讨论串时间戳替换。

<!-- zh-CN:end 51e4b4cb309bd9e2 -->

## 2. Read the whole report

<!-- zh-CN:begin 7aa8d5c6e9872f43 -->

## 2. 阅读完整报告

<!-- zh-CN:end 7aa8d5c6e9872f43 -->

Read the root and current replies before deciding.

<!-- zh-CN:begin f5ad202ba9b631f9 -->

决定之前，读取根消息和当前回复。

<!-- zh-CN:end f5ad202ba9b631f9 -->

Capture:

<!-- zh-CN:begin be2b96e1032779f4 -->

记录：

<!-- zh-CN:end be2b96e1032779f4 -->

- Reporter wording

<!-- zh-CN:begin 3460664c46eb5179 -->

- 报告者的措辞

<!-- zh-CN:end 3460664c46eb5179 -->
- Product version, app build, environment, and platform when present

<!-- zh-CN:begin accb6f259893f97a -->

- 若提供，产品版本、应用构建、环境和平台

<!-- zh-CN:end accb6f259893f97a -->
- Expected behavior

<!-- zh-CN:begin 7579c21024f80895 -->

- 预期行为

<!-- zh-CN:end 7579c21024f80895 -->
- Observed behavior

<!-- zh-CN:begin 13efbd8f65e5d8ea -->

- 观察到的行为

<!-- zh-CN:end 13efbd8f65e5d8ea -->
- Frequency and trigger

<!-- zh-CN:begin 146f88f5e2b1374f -->

- 发生频率和触发条件

<!-- zh-CN:end 146f88f5e2b1374f -->
- Error text or stack signature

<!-- zh-CN:begin 41bebd20b221ae41 -->

- 错误文本或堆栈特征

<!-- zh-CN:end 41bebd20b221ae41 -->
- Existing issue, commit, or pull request links

<!-- zh-CN:begin f087e65ddb4a069a -->

- 已有问题、提交或拉取请求链接

<!-- zh-CN:end f087e65ddb4a069a -->
- Any explicit statement that someone is already fixing it

<!-- zh-CN:begin 4d69692f37b6abcf -->

- 任何明确说明有人已在修复的陈述

<!-- zh-CN:end 4d69692f37b6abcf -->

Inspect every relevant attachment.

<!-- zh-CN:begin 6c999064c7214f32 -->

检查每个相关附件。

<!-- zh-CN:end 6c999064c7214f32 -->

- Read screenshots at full useful resolution.

<!-- zh-CN:begin dd7aef048356b830 -->

- 以足够有用的完整分辨率读取截图。

<!-- zh-CN:end dd7aef048356b830 -->
- Review video for the state transition that separates correct and broken behavior.

<!-- zh-CN:begin a611fba921734060 -->

- 审查视频，寻找区分正确和错误行为的状态转换。

<!-- zh-CN:end a611fba921734060 -->
- Read logs, traces, and crash text for concrete signatures.

<!-- zh-CN:begin cf192fa5a800681b -->

- 阅读日志、跟踪和崩溃文本，寻找具体特征。

<!-- zh-CN:end cf192fa5a800681b -->
- If media needs specialist review, use a read-only media worker and ask a narrow question. The worker returns findings only.

<!-- zh-CN:begin 460ee7d9e8f1764d -->

- 如果媒体需要专业审查，使用只读媒体工作代理并提出范围狭窄的问题。它仅返回发现。

<!-- zh-CN:end 460ee7d9e8f1764d -->
- If an attachment cannot be read, say so in the verdict. Do not invent what it shows.

<!-- zh-CN:begin 30f07ebb12a0abc5 -->

- 附件无法读取时，在结论中说明。不要编造其内容。

<!-- zh-CN:end 30f07ebb12a0abc5 -->

Use evidence already in the thread before asking the reporter for more.

<!-- zh-CN:begin e5e1dc140462469b -->

要求报告者补充之前，先使用讨论串中已有的证据。

<!-- zh-CN:end e5e1dc140462469b -->

## 3. Trace cause before routing

<!-- zh-CN:begin 5273cbc951143627 -->

## 3. 路由前追踪原因

<!-- zh-CN:end 5273cbc951143627 -->

Do a bounded source and history pass before choosing an owner or destination. Use pstack's `how` skill to trace the path from the reported action to the observed result. Use `why` when the report looks like a regression or touches defensive code.

<!-- zh-CN:begin 415288dd3de6dc39 -->

选择负责人或目标位置前，进行一次有界的源码和历史检查。使用 pstack 的 `how` 技能，追踪从报告操作到观察结果的路径。当报告像是回归或涉及防御性代码时，使用 `why`。

<!-- zh-CN:end 415288dd3de6dc39 -->

1. Identify the likely code path from the reported action to the observed result.

<!-- zh-CN:begin 6db1f9d271df91bc -->

1. 识别从报告操作到观察结果的可能代码路径。

<!-- zh-CN:end 6db1f9d271df91bc -->
2. Check whether the visible symptom belongs to that code path or a dependency below it.

<!-- zh-CN:begin 2d56db39dd6ad220 -->

2. 检查可见症状属于该代码路径，还是其下层依赖。

<!-- zh-CN:end 2d56db39dd6ad220 -->
3. Check recent changes when the report looks like a regression.

<!-- zh-CN:begin bb82ebdeed907b7d -->

3. 当报告像是回归时，检查近期变更。

<!-- zh-CN:end bb82ebdeed907b7d -->
4. Check whether a merged commit or open pull request already addresses the same symptom.

<!-- zh-CN:begin 3774c6d7bd619efc -->

4. 检查已合并提交或未关闭拉取请求是否已处理同一症状。

<!-- zh-CN:end 3774c6d7bd619efc -->
5. Separate confirmed facts from hypotheses.

<!-- zh-CN:begin db9f6e3822e2c0a5 -->

5. 将确认事实与假设分开。

<!-- zh-CN:end db9f6e3822e2c0a5 -->

This pass does not need a complete root cause. It must be strong enough to avoid routing a visible symptom to the wrong owner.

<!-- zh-CN:begin 93d0b57312f1157e -->

这次检查不要求完整确定根因，但必须足以避免把可见症状路由给错误负责人。

<!-- zh-CN:end 93d0b57312f1157e -->

If the repository cannot be read, do not guess a code owner. Continue with a conservative classification and say that cause tracing was unavailable.

<!-- zh-CN:begin ef6e15c226174d82 -->

若无法读取仓库，不要猜测代码负责人。继续采用保守分类，并说明无法追踪原因。

<!-- zh-CN:end ef6e15c226174d82 -->

## 4. Classify

<!-- zh-CN:begin 3673e5d527fce27e -->

## 4. 分类

<!-- zh-CN:end 3673e5d527fce27e -->

Choose one category.

<!-- zh-CN:begin 496b55e1183a2239 -->

选择一个类别。

<!-- zh-CN:end 496b55e1183a2239 -->

### Bug

<!-- zh-CN:begin d313e42d647e9ee0 -->

### 缺陷（Bug）

<!-- zh-CN:end d313e42d647e9ee0 -->

Something violates intended behavior. Examples include wrong output, broken state, an error, a crash, a hang, a silent no-op, or a regression.

<!-- zh-CN:begin f076b13c42eb77a9 -->

某种行为违背了预期。示例包括输出错误、状态损坏、报错、崩溃、挂起、静默无操作或回归。

<!-- zh-CN:end f076b13c42eb77a9 -->

### Performance

<!-- zh-CN:begin 2ccfdbb065837e9c -->

### 性能

<!-- zh-CN:end 2ccfdbb065837e9c -->

The report describes measurable slowness, excess memory, battery drain, jank, or another resource problem. Treat it as a bug, but preserve measurements and profiles.

<!-- zh-CN:begin 5e4e8abcf0e7fafe -->

报告描述可测量的缓慢、过量内存占用、电池消耗、卡顿或其他资源问题。按 bug 处理，但保留测量数据和性能剖析。

<!-- zh-CN:end 5e4e8abcf0e7fafe -->

### Feature request

<!-- zh-CN:begin 835fa7f4a3a6e0b0 -->

### 功能请求

<!-- zh-CN:end 835fa7f4a3a6e0b0 -->

The current behavior appears intentional and the reporter wants a different behavior or affordance.

<!-- zh-CN:begin 29e60c58962b389c -->

当前行为看起来是有意设计的，而报告者想要不同的行为或操作功能。

<!-- zh-CN:end 29e60c58962b389c -->

### Question or feedback

<!-- zh-CN:begin 65371a63c322756e -->

### 问题或反馈

<!-- zh-CN:end 65371a63c322756e -->

The report asks how something works, expresses a preference without a concrete defect, or gives general feedback.

<!-- zh-CN:begin 74ed5b2ba13a18b8 -->

报告是在询问某功能如何工作、表达没有具体缺陷的偏好，或提供一般反馈。

<!-- zh-CN:end 74ed5b2ba13a18b8 -->

### Reroute

<!-- zh-CN:begin 1f78b44f2d9c055b -->

### 转交

<!-- zh-CN:end 1f78b44f2d9c055b -->

Cause tracing shows that another configured destination owns the issue.

<!-- zh-CN:begin e516a63f20baa38c -->

原因追踪显示，该问题属于另一个已配置的目标位置。

<!-- zh-CN:end e516a63f20baa38c -->

When the bug versus feature line is unclear, do not file. The one verdict may ask one focused question and use the `other` marker.

<!-- zh-CN:begin 6dbbfb2419ecb582 -->

若 bug 与功能请求的界限不清楚，不建单。唯一的一次结论可以提出一个聚焦问题，并使用 `other` 标记。

<!-- zh-CN:end 6dbbfb2419ecb582 -->

## 5. Apply configured routing

<!-- zh-CN:begin c4c48cbf320e443a -->

## 5. 应用配置的路由

<!-- zh-CN:end c4c48cbf320e443a -->

Read the optional routing map from `routing.map_path`.

<!-- zh-CN:begin 6a829a4480635502 -->

读取 `routing.map_path` 中可选的路由映射。

<!-- zh-CN:end 6a829a4480635502 -->

- Match on confirmed product area, code path, or error signature.

<!-- zh-CN:begin 057bfd22448ecc03 -->

- 根据已确认的产品区域、代码路径或错误特征匹配。

<!-- zh-CN:end 057bfd22448ecc03 -->
- A visible symptom alone is not enough when cause tracing points elsewhere.

<!-- zh-CN:begin 6198a3243fc71242 -->

- 当原因追踪指向别处时，仅凭可见症状不足以匹配。

<!-- zh-CN:end 6198a3243fc71242 -->
- If no route matches, say the owner is unclear. Do not guess.

<!-- zh-CN:begin 6b856ccf003c8ca1 -->

- 无匹配路由时，说明负责人不明确。不要猜测。

<!-- zh-CN:end 6b856ccf003c8ca1 -->
- Do not cross-post. Tell the reporter where to take the issue in the source thread.

<!-- zh-CN:begin 1899423d33f899a8 -->

- 不跨频道转发。在来源讨论串告诉报告者应去哪里报告。

<!-- zh-CN:end 1899423d33f899a8 -->

Owner pings are off by default. A ping is allowed only when all of these hold:

<!-- zh-CN:begin 774de88feb11ed38 -->

默认关闭负责人提醒。只有全部满足以下条件才允许 @：

<!-- zh-CN:end 774de88feb11ed38 -->

1. The routing map explicitly names the owner.

<!-- zh-CN:begin f1edd907482efbc9 -->

1. 路由映射明确列出负责人。

<!-- zh-CN:end f1edd907482efbc9 -->
2. The config allows that ping type.

<!-- zh-CN:begin e7b44ec3578f76bb -->

2. 配置允许该类型提醒。

<!-- zh-CN:end e7b44ec3578f76bb -->
3. The item is a feature request that needs owner input, or recent history identifies a likely regression author with strong evidence.

<!-- zh-CN:begin 2c8ff2c3f61c2404 -->

3. 此项是需要负责人意见的功能请求，或近期历史以强证据指出了可能的回归引入者。

<!-- zh-CN:end 2c8ff2c3f61c2404 -->
4. The owner is not a broad on-call group.

<!-- zh-CN:begin ae27e8f0e846fbe5 -->

4. 负责人不是范围宽泛的值班群组。

<!-- zh-CN:end ae27e8f0e846fbe5 -->

No other case gets a ping.

<!-- zh-CN:begin 6f70d453df6c1b4b -->

其他情况一律不提醒。

<!-- zh-CN:end 6f70d453df6c1b4b -->

## 6. Use the issue-tracker adapter

<!-- zh-CN:begin effcd6f194b34ab9 -->

## 6. 使用问题跟踪器适配器

<!-- zh-CN:end effcd6f194b34ab9 -->

The tracker is an adapter, not a required vendor. A Linear adapter is one valid example. A GitHub Issues adapter or another tracker may implement the same contract.

<!-- zh-CN:begin 3e9802961275bddb -->

跟踪器是一种适配器，而不是必须使用的供应商。Linear 适配器是有效示例之一。GitHub Issues 适配器或其他跟踪器也可以实现同样的约定。

<!-- zh-CN:end 3e9802961275bddb -->

The configured adapter must provide:

<!-- zh-CN:begin 9582d8b54cbd0fe0 -->

配置的适配器必须提供：

<!-- zh-CN:end 9582d8b54cbd0fe0 -->

- Search issues by text, state, label, source URL, and date range

<!-- zh-CN:begin 1ccd31bd7b797798 -->

- 按文本、状态、标签、来源 URL 和日期范围搜索问题

<!-- zh-CN:end 1ccd31bd7b797798 -->
- Read one issue and its links

<!-- zh-CN:begin 60f68081b87a95ae -->

- 读取一个问题及其链接

<!-- zh-CN:end 60f68081b87a95ae -->
- Create an issue with title, body, status, labels, and source URL

<!-- zh-CN:begin beee2e98c3519157 -->

- 创建具有标题、正文、状态、标签和来源 URL 的问题

<!-- zh-CN:end beee2e98c3519157 -->
- Update an existing issue without replacing unrelated fields

<!-- zh-CN:begin b81694356de30857 -->

- 更新已有问题，同时不替换无关字段

<!-- zh-CN:end b81694356de30857 -->
- Add a source link and recurrence note

<!-- zh-CN:begin 5bdecd223c5061bb -->

- 添加来源链接和复发说明

<!-- zh-CN:end 5bdecd223c5061bb -->
- Cancel, close, or delete an issue created by this run if the Slack handoff fails

<!-- zh-CN:begin 8e612f3874af70ec -->

- 若 Slack 交接失败，取消、关闭或删除本次运行创建的问题

<!-- zh-CN:end 8e612f3874af70ec -->

If a required operation is unavailable, fail closed for that write.

<!-- zh-CN:begin 166b382b4e5e7a84 -->

缺少必需操作时，对相应写入采取拒绝继续的方式。

<!-- zh-CN:end 166b382b4e5e7a84 -->

Resolve configured team, project, status, and labels at runtime. Do not invent IDs, create labels, assign owners, or set priority unless the config explicitly requires it.

<!-- zh-CN:begin 1e83c4ef2cef4fe5 -->

运行时解析配置的团队、项目、状态和标签。除非配置明确要求，不得编造 ID、创建标签、分配负责人或设置优先级。

<!-- zh-CN:end 1e83c4ef2cef4fe5 -->

## 7. Dedupe

<!-- zh-CN:begin 23242db1f70d3621 -->

## 7. 去重

<!-- zh-CN:end 23242db1f70d3621 -->

Always check whether this source permalink is already linked to a tracker issue or a prior triage reply. If so, do not post or create a duplicate.

<!-- zh-CN:begin 7437b0629f6e0d6b -->

始终检查此来源永久链接是否已关联到跟踪器问题或先前的分诊回复。如果是，不重复发帖或创建。

<!-- zh-CN:end 7437b0629f6e0d6b -->

For bugs and performance reports, search the tracker using:

<!-- zh-CN:begin 788a843c5fd1dbfa -->

对 bug 和性能报告，用以下信息搜索跟踪器：

<!-- zh-CN:end 788a843c5fd1dbfa -->

- Exact error or crash signature

<!-- zh-CN:begin baed4f4da76ef469 -->

- 完全一致的错误或崩溃特征

<!-- zh-CN:end baed4f4da76ef469 -->
- Product area

<!-- zh-CN:begin f74fe4f5ceddc6da -->

- 产品区域

<!-- zh-CN:end f74fe4f5ceddc6da -->
- Trigger

<!-- zh-CN:begin 78a5eeae53bd07dd -->

- 触发条件

<!-- zh-CN:end 78a5eeae53bd07dd -->
- Symptom

<!-- zh-CN:begin 975854620221fa11 -->

- 症状

<!-- zh-CN:end 975854620221fa11 -->
- Version or date window

<!-- zh-CN:begin 05f00624ca6e0fdf -->

- 版本或日期窗口

<!-- zh-CN:end 05f00624ca6e0fdf -->
- Suspected regression commit

<!-- zh-CN:begin 62549cd69b09d5d1 -->

- 疑似回归提交

<!-- zh-CN:end 62549cd69b09d5d1 -->
- Source permalink

<!-- zh-CN:begin da14f125216078a4 -->

- 来源永久链接

<!-- zh-CN:end da14f125216078a4 -->

Choose one outcome:

<!-- zh-CN:begin 4a275b86f8c4a0d3 -->

选择一个结果：

<!-- zh-CN:end 4a275b86f8c4a0d3 -->

- Confident duplicate: same signature, or the same area, trigger, and symptom, or a confirmed shared cause.

<!-- zh-CN:begin bbec2e6d73a86957 -->

- 确定重复：特征相同，或区域、触发条件和症状相同，或已确认共同原因。

<!-- zh-CN:end bbec2e6d73a86957 -->
- Possibly related: a shared cause is plausible but not proven.

<!-- zh-CN:begin 728a06caba11e534 -->

- 可能相关：共同原因合理但尚未证明。

<!-- zh-CN:end 728a06caba11e534 -->
- Weak resemblance: similarity is superficial.

<!-- zh-CN:begin 1b65651592d760a2 -->

- 弱相似：仅有表面相似。

<!-- zh-CN:end 1b65651592d760a2 -->
- No match.

<!-- zh-CN:begin 6ba295d4b9a23f99 -->

- 无匹配。

<!-- zh-CN:end 6ba295d4b9a23f99 -->

For a confident duplicate, update the existing issue with the source permalink and one short recurrence note. Do not reopen, relabel, or reassign it unless the config says to.

<!-- zh-CN:begin 83a40bbbd62dedc9 -->

确定重复时，将来源永久链接和一条简短复发说明添加到已有问题。除非配置要求，否则不要重新打开、更改标签或重新分配。

<!-- zh-CN:end 83a40bbbd62dedc9 -->

For a possible match, link it in the verdict as uncertain and create nothing.

<!-- zh-CN:begin 33f6451ca401f07d -->

可能匹配时，在结论中链接它并注明不确定，不创建任何问题。

<!-- zh-CN:end 33f6451ca401f07d -->

A long-closed issue is a regression lead, not automatically a live duplicate.

<!-- zh-CN:begin ec10139198ed6a8c -->

关闭已久的问题是回归线索，并不自动意味着它是当前有效的重复项。

<!-- zh-CN:end ec10139198ed6a8c -->

## 8. Decide whether to create

<!-- zh-CN:begin 2fd0a3de0fb6e7db -->

## 8. 决定是否创建

<!-- zh-CN:end 2fd0a3de0fb6e7db -->

Create only when all of these are true:

<!-- zh-CN:begin 1500504067b6f8ff -->

仅在以下条件全部为真时创建：

<!-- zh-CN:end 1500504067b6f8ff -->

1. The classification is bug or performance.

<!-- zh-CN:begin 2e0248de7993e968 -->

1. 分类为 bug 或性能。

<!-- zh-CN:end 2e0248de7993e968 -->
2. The behavior is clearly broken.

<!-- zh-CN:begin 88fdea87545ac188 -->

2. 行为明显出错。

<!-- zh-CN:end 88fdea87545ac188 -->
3. The issue is still live or not known to be fixed.

<!-- zh-CN:begin 3f65d0a05dfc9bbc -->

3. 问题仍然存在，或尚不知已被修复。

<!-- zh-CN:end 3f65d0a05dfc9bbc -->
4. Dedupe found no confident or plausible live match.

<!-- zh-CN:begin 559ea774f4adba04 -->

4. 去重未发现确定或合理可能的有效匹配。

<!-- zh-CN:end 559ea774f4adba04 -->
5. The source parent and permalink passed preflight.

<!-- zh-CN:begin 0c53bb6296336853 -->

5. 来源父消息和永久链接通过预检。

<!-- zh-CN:end 0c53bb6296336853 -->
6. The tracker target fields resolved.

<!-- zh-CN:begin 7605d29fd70d59d1 -->

6. 跟踪器目标字段已解析。

<!-- zh-CN:end 7605d29fd70d59d1 -->
7. The adapter can compensate if the verdict post fails.

<!-- zh-CN:begin fbde49c4e997cffb -->

7. 适配器能在结论发帖失败时补偿回滚。

<!-- zh-CN:end fbde49c4e997cffb -->

Never create for a feature request, question, feedback item, reroute, possible duplicate, confident duplicate, or already-fixed issue.

<!-- zh-CN:begin bb1b0ca0460a62ba -->

绝不为功能请求、问题、反馈、转交、可能重复、确定重复或已经修复的问题建单。

<!-- zh-CN:end bb1b0ca0460a62ba -->

The new issue must be self-contained:

<!-- zh-CN:begin 13c4b9d2680f04ff -->

新问题必须自成一体：

<!-- zh-CN:end 13c4b9d2680f04ff -->

- Plain title that names the area and symptom

<!-- zh-CN:begin e99f9f57ddf30a43 -->

- 直白标题，指出区域与症状

<!-- zh-CN:end e99f9f57ddf30a43 -->
- Reporter quote

<!-- zh-CN:begin b241c1701771e44a -->

- 报告者引文

<!-- zh-CN:end b241c1701771e44a -->
- Expected and observed behavior

<!-- zh-CN:begin 69a1c4528053a994 -->

- 预期行为与观察行为

<!-- zh-CN:end 69a1c4528053a994 -->
- Version and environment, or `unknown`

<!-- zh-CN:begin 0fcc708929d5c4bc -->

- 版本和环境，或 `unknown`

<!-- zh-CN:end 0fcc708929d5c4bc -->
- Trigger and frequency

<!-- zh-CN:begin fb54b789bc56e06a -->

- 触发条件与频率

<!-- zh-CN:end fb54b789bc56e06a -->
- Source thread permalink

<!-- zh-CN:begin 49970ae82a0c8573 -->

- 来源讨论串永久链接

<!-- zh-CN:end 49970ae82a0c8573 -->
- Short cause-tracing findings with hypotheses labeled as hypotheses

<!-- zh-CN:begin 3a61bf9ae28b69a5 -->

- 简短的原因追踪发现，假设须明确标为假设

<!-- zh-CN:end 3a61bf9ae28b69a5 -->
- Inline screenshot or representative video frame when supported

<!-- zh-CN:begin 7f3ac354562c2937 -->

- 支持时加入内嵌截图或有代表性的视频帧

<!-- zh-CN:end 7f3ac354562c2937 -->
- Links to remaining artifacts

<!-- zh-CN:begin cb3eb342c312fc84 -->

- 剩余制品的链接

<!-- zh-CN:end cb3eb342c312fc84 -->
- Configured intake status and labels

<!-- zh-CN:begin 1b89aa32893dae24 -->

- 配置的接收状态和标签

<!-- zh-CN:end 1b89aa32893dae24 -->

Do not put a guessed root cause in the title.

<!-- zh-CN:begin 98f052a535567662 -->

不要把猜测的根因写进标题。

<!-- zh-CN:end 98f052a535567662 -->

## 9. Post one verdict

<!-- zh-CN:begin ea464153310a0f96 -->

## 9. 发布一个结论

<!-- zh-CN:end ea464153310a0f96 -->

Run a fresh source-parent preflight. Then post exactly one reply with `channel=SOURCE_CHANNEL_ID` and `thread_ts=SOURCE_THREAD_TS`.

<!-- zh-CN:begin 855eff211ccb69dd -->

重新执行来源父消息预检。随后使用 `channel=SOURCE_CHANNEL_ID` 和 `thread_ts=SOURCE_THREAD_TS` 恰好发布一条回复。

<!-- zh-CN:end 855eff211ccb69dd -->

Never call a source-channel posting action without a nonempty `thread_ts`.

<!-- zh-CN:begin 6e9876ab03f4ff38 -->

绝不在 `thread_ts` 非空这一条件未满足时调用来源频道发帖操作。

<!-- zh-CN:end 6e9876ab03f4ff38 -->

Keep the reply short:

<!-- zh-CN:begin 145a9fe0de8109e4 -->

回复保持简短：

<!-- zh-CN:end 145a9fe0de8109e4 -->

- Lead with the outcome.

<!-- zh-CN:begin 1dc105755ff1ad2c -->

- 先说明结果。

<!-- zh-CN:end 1dc105755ff1ad2c -->
- Link the existing or new tracker issue when there is one.

<!-- zh-CN:begin 1159b96200b8ab78 -->

- 存在已有或新建跟踪器问题时，附链接。

<!-- zh-CN:end 1159b96200b8ab78 -->
- Mention a reroute or one missing fact when needed.

<!-- zh-CN:begin 36b49912be7c546e -->

- 必要时提及转交或一项缺失事实。

<!-- zh-CN:end 36b49912be7c546e -->
- Include at most one allowed owner ping.

<!-- zh-CN:begin 37e0e82524b6fceb -->

- 最多包含一次允许的负责人提醒。

<!-- zh-CN:end 37e0e82524b6fceb -->
- End with exactly one marker line.

<!-- zh-CN:begin f4c4667a549b49ea -->

- 结尾恰好附一行标记。

<!-- zh-CN:end f4c4667a549b49ea -->

Marker contract:

<!-- zh-CN:begin 81dc8518d8c6f578 -->

标记约定：

<!-- zh-CN:end 81dc8518d8c6f578 -->

```text
[benny:bug]
[benny:bug] tracker=https://tracker.example/issue/123
[benny:performance]
[benny:performance] tracker=https://tracker.example/issue/123
[benny:other]
```

Use only the configured marker strings. The repro automation trusts the marker only when it comes from the configured triage identity in this source thread.

<!-- zh-CN:begin a3dfceffab3fb920 -->

仅使用配置的标记字符串。复现自动化只有在标记来自此来源讨论串中配置的分诊身份时才信任它。

<!-- zh-CN:end a3dfceffab3fb920 -->

After posting, read the same source thread and verify the verdict appears under `SOURCE_THREAD_TS`. If it does not, never retry at the root.

<!-- zh-CN:begin 906e05bcbe9e6477 -->

发帖后，读取同一来源讨论串，核实结论出现在 `SOURCE_THREAD_TS` 之下。若未出现，绝不在根层级重试。

<!-- zh-CN:end 906e05bcbe9e6477 -->

If this run created a tracker issue and the verdict did not land, use the adapter's compensation action. Verify that the issue is canceled, closed, or deleted. If compensation cannot be verified, report the failure only in the automation run output.

<!-- zh-CN:begin db7e6c283042921b -->

若本次运行创建了跟踪器问题，而结论未成功发布，使用适配器的补偿操作。核实问题已取消、关闭或删除。若无法验证补偿，仅在自动化运行输出中报告失败。

<!-- zh-CN:end db7e6c283042921b -->

## 10. Watch one follow-up window

<!-- zh-CN:begin 19c729402756883a -->

## 10. 观察一个跟进窗口

<!-- zh-CN:end 19c729402756883a -->

Watch the source thread for the configured follow-up window, then stop.

<!-- zh-CN:begin 8355536a4bab9e73 -->

在配置的跟进窗口内观察来源讨论串，然后停止。

<!-- zh-CN:end 8355536a4bab9e73 -->

- Answer only a direct question to the triage identity.

<!-- zh-CN:begin b45c6db2f5433874 -->

- 只回答直接向分诊身份提出的问题。

<!-- zh-CN:end b45c6db2f5433874 -->
- Apply a concrete correction to the tracker issue when safe.

<!-- zh-CN:begin 1ab77f6e8673baba -->

- 安全时，对跟踪器问题应用具体更正。

<!-- zh-CN:end 1ab77f6e8673baba -->
- Do not emit a second marker in the same run.

<!-- zh-CN:begin ba135a3624c31b9d -->

- 同次运行不再输出第二个标记。

<!-- zh-CN:end ba135a3624c31b9d -->
- Stay out of human coordination and side chatter.

<!-- zh-CN:begin c40504268b076614 -->

- 不介入人与人之间的协调和闲聊。

<!-- zh-CN:end c40504268b076614 -->
- Stop early if someone asks the automation to stop.

<!-- zh-CN:begin 578f780a6ded5a26 -->

- 有人要求自动化停止时，提前停止。

<!-- zh-CN:end 578f780a6ded5a26 -->

Do not extend the window more than once. A new report should start a new run.

<!-- zh-CN:begin 8770563df2148db6 -->

窗口最多延长一次。新报告应启动新运行。

<!-- zh-CN:end 8770563df2148db6 -->
