## What it does

<!-- zh-CN:begin 07b647ce35f13365 -->

## 它做什么

<!-- zh-CN:end 07b647ce35f13365 -->

`triage` works through the issues on your project's tracker. It moves each one through a small state machine of **triage roles** (a category role and a state role). Each issue ends as an agent-ready brief, a specific question for the reporter, or a closed issue with a recorded reason.

<!-- zh-CN:begin 157ff577d11c8698 -->

`triage` 处理项目跟踪器里的议题，让每项经过一个小型**分诊角色**状态机（类别角色与状态角色）。每项最终成为代理可执行简报、给报告者的具体问题，或带原因的关闭议题。

<!-- zh-CN:end 157ff577d11c8698 -->

It is only for issues **you didn't create**. That means raw bug reports, incoming feature requests, or an external pull request that arrived unannounced: work that came into the tracker from outside, in whatever shape the reporter left it. [Tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) from [to-tickets](https://aihero.dev/skills-to-tickets) are already agent-ready, so if you run `triage` over them, you waste the work. The rule is simple: `/triage` is only for incoming issues, not for issues you created yourself.

<!-- zh-CN:begin df1dcfb56672e9bf -->

它只处理**不是你创建的**议题：原始缺陷报告、新功能请求，或突然出现的外部 PR，即从外部进入跟踪器、保留报告者原始形态的工作。[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)由 [to-tickets](https://aihero.dev/skills-to-tickets) 生成时已可供代理执行，分诊它们会浪费工作。规则简单：`/triage` 只用于外部输入，不用于自己创建的议题；其中相关的字段或标识包括 `triage`。

<!-- zh-CN:end df1dcfb56672e9bf -->

It also differs from labelling by hand because it recommends and then waits. It gives you its category and state call with reasoning, plus what it found in the codebase, and applies nothing until you tell it to.

<!-- zh-CN:begin 9e737b736fcb151f -->

它也不同于手工打标签，因为先建议再等待：给出类别、状态判断、理由及代码库发现，只有你指示才应用。

<!-- zh-CN:end 9e737b736fcb151f -->

## When to reach for it

<!-- zh-CN:begin e2114f2f4b01e5b6 -->

## 何时使用

<!-- zh-CN:end e2114f2f4b01e5b6 -->

You invoke this by typing `/triage` and then describing what you want in plain language. The [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own. Examples: "Show me anything that needs my attention", "let's look at #42", "move #42 to ready-for-agent".

<!-- zh-CN:begin 7d4687e455472791 -->

输入 `/triage` 并平实描述。 [代理](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。例如：“显示需要我关注的事项”“看 #42”“把 #42 移到 ready-for-agent”。

<!-- zh-CN:end 7d4687e455472791 -->

| What you have | Where to go |
| --- | --- |
| A tracker full of raw reports from other people | `/triage` |
| A rough idea of your own, nothing written down | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| A settled conversation to turn into a [spec](https://www.aihero.dev/ai-coding-dictionary/spec) | [to-spec](https://aihero.dev/skills-to-spec) |
| A spec to split into agent-ready tickets | [to-tickets](https://aihero.dev/skills-to-tickets) |
| A confirmed bug that needs a root cause, not a label | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

<!-- zh-CN:begin 4a4548452b341a5a -->

| 你拥有的内容 | 去哪里 |
| --- | --- |
| 满是他人原始报告的跟踪器 | `/triage` |
| 自己尚未写下的粗略想法 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 已确定的对话，需转成[规格](https://www.aihero.dev/ai-coding-dictionary/spec) | [to-spec](https://aihero.dev/skills-to-spec) |
| 需拆成代理可执行工单的规格 | [to-tickets](https://aihero.dev/skills-to-tickets) |
| 已确认、需根因而非标签的缺陷 | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

<!-- zh-CN:end 4a4548452b341a5a -->

## Prerequisites

<!-- zh-CN:begin 58fec034856aec61 -->

## 前提

<!-- zh-CN:end 58fec034856aec61 -->

`triage` reads and writes your issue tracker, so [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) must first configure that tracker and its label vocabulary. The role names below are **canonical**. The label strings in your tracker may differ, and setup provides the mapping. If your tracker already uses the canonical names exactly, you have nothing to map and nothing to set up.

<!-- zh-CN:begin def39f44e495788c -->

`triage` 读写议题跟踪器，因此须先由 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置跟踪器及标签词汇。下列角色名是**规范名**；跟踪器标签字符串可不同，设置会提供映射。若已完全使用规范名，无需映射或设置。

<!-- zh-CN:end def39f44e495788c -->

The tracker config also decides whether external pull requests count as a request surface, and who counts as external. That flag is off by default, and setup no longer asks about it. To bring PRs into scope, turn it on in `docs/agents/issue-tracker.md`.

<!-- zh-CN:begin 9a7787c53e5aa8dd -->

跟踪器配置也决定外部 PR 是否算请求入口，及谁算外部。默认关闭，设置不再询问；在 `docs/agents/issue-tracker.md` 启用。

<!-- zh-CN:end 9a7787c53e5aa8dd -->

## The state machine

<!-- zh-CN:begin 94e648afdcfac6e9 -->

## 状态机

<!-- zh-CN:end 94e648afdcfac6e9 -->

Every triaged item ends with exactly one category role and one state role. There are two categories: `bug` (something is broken) and `enhancement` (new feature or improvement). There are five states:

<!-- zh-CN:begin b28f34bfef64f991 -->

每个分诊项恰有一个类别角色和一个状态角色。类别为 `bug`（坏掉）和 `enhancement`（新功能或改进）；状态有五个：

<!-- zh-CN:end b28f34bfef64f991 -->

| State | Means |
| --- | --- |
| `needs-triage` | You need to evaluate it. An unlabelled issue normally lands here first. |
| `needs-info` | Waiting on the reporter. Returns to `needs-triage` when they reply. |
| `ready-for-agent` | Fully specified, with an agent brief attached. An [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) agent can take it. |
| `ready-for-human` | The same brief, plus why an agent can't do it: judgment, external access, manual testing. |
| `wontfix` | Closed, with the reason recorded. |

<!-- zh-CN:begin 1d2257af12c72b8c -->

| 状态 | 含义 |
| --- | --- |
| `needs-triage` | 需要评估；无标签议题通常先落这里 |
| `needs-info` | 等待报告者；回复后回 `needs-triage` |
| `ready-for-agent` | 规格完整并附代理简报，[AFK](https://www.aihero.dev/ai-coding-dictionary/afk) 代理可接 |
| `ready-for-human` | 同一简报，并说明为何需人：判断、外部访问、手动测试 |
| `wontfix` | 已关闭并记录原因 |

<!-- zh-CN:end 1d2257af12c72b8c -->

That is the whole vocabulary. The rule of exactly one state role per item keeps the queries simple. The states are also the most-requested area of the [skill](https://www.aihero.dev/ai-coding-dictionary/skill). Users have asked for a state for work that is specified but blocked on another issue, a `deferred` state for work that waits on a future trigger, and a terminal `implemented` state. None of those has shipped. See the questions below.

<!-- zh-CN:begin 70c0b32745a04647 -->

这就是完整词汇。每项恰一个状态使查询简单。状态也是[技能](https://www.aihero.dev/ai-coding-dictionary/skill)请求最多之处：已指定但被另一议题阻塞、等待未来触发的 `deferred`、终态 `implemented` 均未发布，见下文问题。

<!-- zh-CN:end 70c0b32745a04647 -->

`wontfix` has three cases. The difference matters because only one of them writes to the knowledge base:

<!-- zh-CN:begin b51bb80e305e766c -->

`wontfix` 有三种情况，区别重要，因为只有一种写知识库：

<!-- zh-CN:end b51bb80e305e766c -->

| Why you're closing it | What happens |
| --- | --- |
| Already implemented | A comment that points to where the feature already lives. Nothing goes into `.out-of-scope/`, because it's a built feature, not a rejected one, and a file there would break the dedup checks. |
| Rejected bug | Polite explanation, then close. |
| Rejected enhancement | A file in `.out-of-scope/`, linked from the closing comment, then close. |

<!-- zh-CN:begin 4268adce042bc4d6 -->

| 关闭原因 | 发生什么 |
| --- | --- |
| 已实现 | 评论指向功能位置。`.out-of-scope/` 不写，因为已构建而非拒绝，文件会破坏去重检查 |
| 拒绝缺陷 | 礼貌解释后关闭 |
| 拒绝增强 | 在 `.out-of-scope/` 建文件，关闭评论链接它，再关闭 |

<!-- zh-CN:end 4268adce042bc4d6 -->

`.out-of-scope/` holds one markdown file per rejected **concept**, not per issue. Each file is a short design document, not a database row. It says what was rejected, why, and lists every issue that asked for it. `triage` reads the whole directory before it evaluates anything. It matches by concept, not keyword, so "night theme" matches `dark-mode.md`. When it finds a match, it shows you the old decision and asks if you still agree with it, instead of arguing the request again from the start.

<!-- zh-CN:begin dbdadd4bfc029397 -->

`.out-of-scope/` 每个被拒**概念**一个 Markdown 文件，不按议题：文件是短设计文档而非数据库行，写拒绝内容、原因及所有请求议题。`triage` 评估前读整个目录，按概念而非关键词匹配，因此“夜间主题”匹配 `dark-mode.md`。命中时展示旧决定并问是否仍同意，无需从头争论。

<!-- zh-CN:end dbdadd4bfc029397 -->

## Verify before you brief

<!-- zh-CN:begin 407b7fba28d0c683 -->

## 写简报前先验证

<!-- zh-CN:end 407b7fba28d0c683 -->

Before any [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling), `triage` checks that the claim holds. For a bug, it reproduces it from the reporter's steps. For a PR, it checks out the branch and runs the relevant tests. Then it reports one of three results:

<!-- zh-CN:begin 236f087e44095a95 -->

任何[追问](https://www.aihero.dev/ai-coding-dictionary/grilling)前，`triage` 验证主张：缺陷按报告步骤复现；PR 检出分支并跑相关测试。结果三种：

<!-- zh-CN:end 236f087e44095a95 -->

- Confirmed, with the code path.

<!-- zh-CN:begin c8f4ea81e0b0940e -->

- 已确认，并给出代码路径。

<!-- zh-CN:end c8f4ea81e0b0940e -->
- Failed to reproduce.

<!-- zh-CN:begin 2ff952c82b8ddc1e -->

- 无法复现。

<!-- zh-CN:end 2ff952c82b8ddc1e -->
- Not enough detail to try. This is the strongest `needs-info` signal there is.

<!-- zh-CN:begin 84e5440d43cb91f1 -->

- 细节不足，无法尝试；这是最强的 `needs-info` 信号。

<!-- zh-CN:end 84e5440d43cb91f1 -->

In the same pass, it runs two more checks against the codebase. The **redundancy** check asks if the feature is already implemented, and searches by domain concept, not by the reporter's wording. The **prior rejection** check asks if `.out-of-scope/` already says no. Both checks are cheap, and a hit on either produces a `wontfix`.

<!-- zh-CN:begin 4bc89ff6e0325e17 -->

同轮还做两项检查：**冗余**按领域概念而非报告措辞查找功能是否已实现；**既往拒绝**检查 `.out-of-scope/`。命中任一即 `wontfix`。

<!-- zh-CN:end 4bc89ff6e0325e17 -->

All of this work makes one artifact good: the **agent brief**. This is the structured comment that `triage` posts when an issue moves to `ready-for-agent`. After `triage` posts it, the brief is the contract and the original report is only context. Briefs are **durable** rather than precise, because an issue can sit in `ready-for-agent` for weeks while the code changes. So a brief names types, signatures and behavioural contracts, and never file paths or line numbers. A confirmed reproduction makes a much stronger brief than a guess.

<!-- zh-CN:begin 2fcb025c81a062fc -->

这些工作服务于一个好产物：**代理简报**。议题移至 `ready-for-agent` 时发布的结构化评论；发布后简报是契约，原报告只是上下文。简报应**耐久**而非精确，因为议题可能停留数周、代码已变；所以写类型、签名、行为契约，不写文件路径或行号。确认复现的简报强于猜测；其中相关的字段或标识包括 `triage`、`triage`、`ready-for-agent`。

<!-- zh-CN:end 2fcb025c81a062fc -->

## A PR is an issue with attached code

<!-- zh-CN:begin 578d2bbd67566e30 -->

## PR 是附带代码的议题

<!-- zh-CN:end 578d2bbd67566e30 -->

If the tracker treats external pull requests as a request surface, they go through the same machine, with the same categories, states and transitions. The states apply to the diff. `ready-for-agent` means a brief is attached and an agent should take the next step on the code. `ready-for-human` means a person can merge it. A brief on a PR describes what is left to do to the existing diff, not how to build the thing from nothing.

<!-- zh-CN:begin 6bcee9cb5398c509 -->

跟踪器把外部 PR 当请求入口时，它们经过同一状态机。状态作用于差异：`ready-for-agent` 表示附简报，代理应在代码上继续；`ready-for-human` 表示人可以合并。PR 简报说明现有差异还需做什么，不说如何从零构建。

<!-- zh-CN:end 6bcee9cb5398c509 -->

Discovery shows only *external* PRs, because a collaborator's in-progress branch is not triage work. That filter applies only to discovery. If you name a PR explicitly, `triage` handles it, whoever wrote it.

<!-- zh-CN:begin 74032731e53b6bdc -->

发现阶段只展示*外部* PR，协作者进行中的分支不是分诊工作。此过滤只用于发现；明确点名 PR 时，不论作者都处理；其中相关的字段或标识包括 `triage`。

<!-- zh-CN:end 74032731e53b6bdc -->

## Common questions

<!-- zh-CN:begin 7a78b0a71fbdafd4 -->

## 常见问题

<!-- zh-CN:end 7a78b0a71fbdafd4 -->

**I ran `/to-spec` and `/to-tickets`, and now those tickets are sitting there untriaged. Do I run `/triage` over them?**
No. They are already agent-ready. `to-tickets` applies the `ready-for-agent` label when it publishes them, so an AFK runner picks them up without another pass. The user who hit this had run the spec flow and seen `needs-triage` on the output, and their AFK runner ignored everything. `triage` is the on-ramp for work that arrives from outside. The spec flow is the lane for work you start yourself. The two meet at `ready-for-agent`, not before.

<!-- zh-CN:begin d5892e249f818c7a -->

**我运行了 `/to-spec` 和 `/to-tickets`，这些工单没分诊。要再跑 `/triage` 吗？**
不要。它们已可供代理执行。发布时带 `ready-for-agent`，AFK 运行器直接接。此前用户看到输出为 `needs-triage`，导致运行器忽略。`triage` 是外部工作入口，规格流程是自己启动工作的通道，两者在 `ready-for-agent` 汇合；其中相关的字段或标识包括 `to-tickets`。

<!-- zh-CN:end d5892e249f818c7a -->

**Is `triage` still relevant now that there's a `to-spec` → `to-tickets` → `implement` flow?**
Only if you have inbound work. `triage` is older than that flow and does a different job: it handles reports other people filed. If everything in your tracker came from your own planning, you will rarely use it. If you maintain anything public, or your team files bugs to you, it is where that work starts. The main use is open-source repos that take issues from external contributors.

<!-- zh-CN:begin f653789e8f22b8d8 -->

**有 `to-spec` → `to-tickets` → `implement` 流程后，还需要 `triage` 吗？**
仅在你有外部输入时。它处理别人提交的报告，若跟踪器全由自己规划产生则少用；维护公开项目或团队向你报缺陷时，它是起点。主要用例是接收外部贡献的开源仓库；其中相关的字段或标识包括 `triage`。

<!-- zh-CN:end f653789e8f22b8d8 -->

**The agent tried to apply `ready-for-agent` and `gh` said the label doesn't exist.**
This is a known open bug ([#616](https://github.com/mattpocock/skills/issues/616)). `setup-matt-pocock-skills` writes the label vocabulary into `docs/agents/triage-labels.md`, but does not create the labels in your tracker. Create the five state labels and two category labels yourself, once, with `gh label create` or the tracker's UI, and the error stops. The issue links to a community fix branch that has not been merged.

<!-- zh-CN:begin e7655c196a017171 -->

**代理要应用 `ready-for-agent`，但 `gh` 说标签不存在。**
这是已知开放缺陷（[#616](https://github.com/mattpocock/skills/issues/616)）。`setup-matt-pocock-skills` 把词汇写入 `docs/agents/issue-tracker.md`，但不创建标签。用 `gh label create` 或 UI 一次性创建五个状态和两个类别，错误即停。议题链接的社区修复分支尚未合并；其中相关的字段或标识包括 `docs/agents/triage-labels.md`。

<!-- zh-CN:end e7655c196a017171 -->

**Five states aren't enough. What about blocked, or deferred, or implemented?**
This is the most-filed gap on the skill. It comes in three forms:

<!-- zh-CN:begin 7d57cc1cab1d4c7f -->

**五个状态不够。阻塞、延迟或已实现呢？**
这是请求最多缺口，三种：

<!-- zh-CN:end 7d57cc1cab1d4c7f -->

- An issue that is fully specified but waits on another issue to close ([#139](https://github.com/mattpocock/skills/issues/139)). The reporter said `ready-for-agent` is "technically true" there but misleading, so an agent picks it up and gets stuck.

<!-- zh-CN:begin 72c6d9a431fc6c6d -->

- 已完整指定但等另一议题关闭（[#139](https://github.com/mattpocock/skills/issues/139)）。报告者指出 `ready-for-agent`“技术上正确”但误导，代理会卡住。

<!-- zh-CN:end 72c6d9a431fc6c6d -->
- Future work that is intended but waits on a trigger, so it is not actionable yet ([#297](https://github.com/mattpocock/skills/issues/297)).

<!-- zh-CN:begin b167ca797fa15262 -->

- 有意等待触发的未来工作，尚不可执行（[#297](https://github.com/mattpocock/skills/issues/297)）。

<!-- zh-CN:end b167ca797fa15262 -->
- A terminal state for "implemented, awaiting verification". Without it, an AFK runner can queue finished tickets again.

<!-- zh-CN:begin 1ce5489b08d94eeb -->

- 缺少“已实现，待验证”终态，AFK 运行器可能重复排队已完成工单。

<!-- zh-CN:end 1ce5489b08d94eeb -->

The blocked case is accepted as real, but the name is undecided (`blocked` versus `paused`). None of it has shipped. As a workaround, people add a repo-local extra label next to the category. The state slot then holds an accurate value, but the skill does not know about the extra label. One community fork goes further and adds `needs-slicing`, `tracking` and effort labels. That works, but it belongs to that fork, not to the skill.

<!-- zh-CN:begin e7641a8bd63deb74 -->

阻塞情况确认真实，但名称未定（`blocked` 与 `paused`），均未发布。临时做法是类别旁加仓库自定义标签，状态槽仍准确，技能不懂额外标签。某社区 fork 增加 `needs-slicing`、`tracking` 和工作量标签，有效但属于该 fork。

<!-- zh-CN:end e7641a8bd63deb74 -->

**How is this different from `/diagnosing-bugs`?**
The verification step here is shallow on purpose. It answers "is this real, and roughly where does it live", and does not look for a root cause. If a bug does not reproduce from the reporter's steps in a few minutes, use `needs-info`, or use [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) if you want to investigate it now. Neither skill's text mentions the other yet. A user reported that gap, and it is still open.

<!-- zh-CN:begin 715c89b267fe6de1 -->

**与 `/diagnosing-bugs` 有何不同？**
这里验证有意浅层：回答“是否真实、大致在哪”，不找根因。报告步骤几分钟内不复现就标 `needs-info`，或现在用 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs)。两技能尚无互相指引，用户已报告此缺口。

<!-- zh-CN:end 715c89b267fe6de1 -->

**Can I point it at my whole backlog and let it run?**
You can ask, but watch what it reads. The "show what needs attention" pass is a cheap listing for *selection*. You pick one issue, and then `triage` gathers full [context](https://www.aihero.dev/ai-coding-dictionary/context) on that issue. If you run it across twenty issues at once, the agent can use that cheap listing as its only evidence without telling you. The listing returns issue bodies but not comments. One user hit exactly this. Three issues already had a comment that said "already fixed, recommend closing", and all three got new agent briefs instead. For a bulk pass, say explicitly that it must read the comments on each issue.

<!-- zh-CN:begin c69105b1926fa9f8 -->

**能指向整个积压并让它运行吗？**
可要求，但注意读取范围。“显示需关注”只是用于*选择*的低成本列表；选定后再收集完整[上下文](https://www.aihero.dev/ai-coding-dictionary/context)。一次跑二十项时，代理可能把列表当唯一证据。列表返回正文不含评论；曾有议题评论已说“已修复建议关闭”，却仍生成新简报。批量时必须明确要求读每项评论；其中相关的字段或标识包括 `triage`。

<!-- zh-CN:end c69105b1926fa9f8 -->

**Does it work with Linear, or anything other than GitHub Issues?**
Yes. The tracker is config, not a hard-coded assumption. People run it against Linear (through the `linear` CLI), GitLab, and plain markdown files under `.scratch/`. A common split is Linear for issues and planning, and GitHub for code and PRs. Skills that say "issue tracker" then map to Linear, and skills that say "PR" map to GitHub. The local-markdown tracker has an open template bug: the generated file can contain the acceptance criteria twice, once at the top level and once inside the agent brief ([#200](https://github.com/mattpocock/skills/issues/200)).

<!-- zh-CN:begin b081a81109c9b88d -->

**支持 Linear 或 GitHub Issues 之外吗？**
支持。跟踪器是配置，不是硬编码。可运行于 Linear（`linear` CLI）、GitLab、`.scratch/` 下的 Markdown。常见组合是 Linear 管理议题规划、GitHub 管理代码 PR。本地 Markdown 跟踪器有开放模板缺陷：接受标准可能重复在顶层和代理简报中（[#200](https://github.com/mattpocock/skills/issues/200)）。

<!-- zh-CN:end b081a81109c9b88d -->

## It's working if

<!-- zh-CN:begin e47bab0f942b4d3e -->

## 怎样算正常工作

<!-- zh-CN:end e47bab0f942b4d3e -->

- Every item it touches ends with exactly one category role and one state role, never zero, and never two conflicting states.

<!-- zh-CN:begin ed6719565bcf8bad -->

- 每个接触项恰有一个类别和一个状态，不为零也不冲突。

<!-- zh-CN:end ed6719565bcf8bad -->
- It gives you a recommendation with reasoning and stops. It does not relabel the issue and move on.

<!-- zh-CN:begin bf368888158177eb -->

- 给出带理由建议后停止，不自动改标签。

<!-- zh-CN:end bf368888158177eb -->
- It reproduced the bug, or checked out and ran the PR, before anything reached `ready-for-agent`.

<!-- zh-CN:begin cec6b15473d4298d -->

- 任何进入 `ready-for-agent` 前已复现缺陷，或检出运行 PR。

<!-- zh-CN:end cec6b15473d4298d -->
- The briefs it writes name types and behaviours, and contain no file paths and no line numbers.

<!-- zh-CN:begin d4b401c25d162c49 -->

- 简报写类型和行为，不含文件路径或行号。

<!-- zh-CN:end d4b401c25d162c49 -->
- When a request you rejected six months ago comes back, it tells you and quotes the old reason instead of triaging it again.

<!-- zh-CN:begin 0548e27b4b390e88 -->

- 六个月前拒绝的请求回来时，引用旧理由而非重新分诊。

<!-- zh-CN:end 0548e27b4b390e88 -->
- Every comment it posts starts with `> *This was generated by AI during triage.*`

<!-- zh-CN:begin fc3a1f9e58f00911 -->

- 每条评论以 `> *This was generated by AI during triage.*` 开头。

<!-- zh-CN:end fc3a1f9e58f00911 -->

## Where it fits

<!-- zh-CN:begin 16aa304dfe7efdc4 -->

## 适用范围

<!-- zh-CN:end 16aa304dfe7efdc4 -->

`triage` is an **on-ramp**, not a step in the main chain. The main flow starts from an idea you had (grill, spec, tickets, implement, review). `triage` is the parallel lane for work that came from someone else. Both lanes end at the same place: an issue labelled `ready-for-agent` with a brief on it. [implement](https://aihero.dev/skills-implement) picks that up the same way it picks up a ticket from [to-tickets](https://aihero.dev/skills-to-tickets). When a request needs more detail before `triage` can brief it, `triage` runs [grilling](https://aihero.dev/skills-grilling) and [domain-modeling](https://aihero.dev/skills-domain-modeling) together, one round of questions at a time, so it records decisions in `GLOSSARY.md` and the ADRs as you make them. When you're not sure which lane you are in, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 6398bf2bb6376c08 -->

`triage` 是**入口**而非主链步骤。主流程从想法开始（追问、规格、工单、实施、审查）；`triage` 是他人工作的并行通道。两者都在带简报的 `ready-for-agent` 议题结束。[implement](https://aihero.dev/skills-implement) 与处理 [to-tickets](https://aihero.dev/skills-to-tickets) 工单一样接手。需要更多细节时，`triage` 同轮运行 [grilling](https://aihero.dev/skills-grilling) 和 [domain-modeling](https://aihero.dev/skills-domain-modeling)，把决定写入 `GLOSSARY.md` 和 ADR。不确定通道时用 [ask-matt](https://aihero.dev/skills-ask-matt)；其中相关的字段或标识包括 `triage`。

<!-- zh-CN:end 6398bf2bb6376c08 -->
