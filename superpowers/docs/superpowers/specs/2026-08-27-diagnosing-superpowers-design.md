# Superpowers 会话诊断——设计

日期：2026-08-27
状态：Jesse 已在会话内批准；规格待审查
分支：从 `dev` 创建的 `diagnosing-superpowers`

## 目标

一个核心技能 `diagnosing-superpowers`，供用户在 superpowers 会话出错时调用。它与用户共同明确问题，检查磁盘上的会话记录，并带证据报告发生了什么。应请求，它导出脱敏包，使远程代理可判断 superpowers 本身是否需要变更；它也能查找表现出相同行为的其他本地会话。

技能只报告，绝不对 superpowers 作诊断。推测 superpowers 中的缺陷或提出变更属于远程分诊者工作；被询问时技能会说明这一点。

## 范围决定（已与 Jesse 确定）

- **v1 为纯正文技能。** 不提供脚本。模型完成工作，并积极使用子代理。若正文版本证明形态可行，日后再加确定性工具。

- **运行环境覆盖。** 只有对磁盘文件验证过的 Claude Code 与 Codex 格式提供字段级参考文档。其他运行环境使用发现流程。当前运行环境应知道自己的会话存储；技能要求它利用该知识，并明确说明能读和不能读的内容。不得臆造格式。

- **先接收问题。** 技能先问用户要诊断什么，并合作到形成具体问题陈述。扫描服务于该陈述。

- **质量作为过程证据判断**，依据会话同意的计划（设计、计划、验收标准、规格／计划文件）以及记录所证明的内容（运行的测试、主张背后的验证、提交与主张一致、审查反馈已处理）。它不是对最终差异作代码审查。

- **脱敏级别由用户决定。** 技能询问，并说明对 superpowers 缺陷报告而言，信息越多越可能得到帮助。

- **精确记录 Superpowers 身份**：实际加载的安装根目录、版本、检出目录的 git sha，以及会话读取或注入的每个技能文件 sha1。

- **技能触发是一等分析维度**：什么何时因何触发，哪里技能自身触发描述匹配却没有触发或触发过晚。

## 技能布局

```
skills/diagnosing-superpowers/
  SKILL.md
  references/
    claude-code-sessions.md
    codex-sessions.md
    other-harnesses.md
    context-safety.md
    github-issues.md
  prompts/
    analyst-common.md
    skill-timeline.md
    plan-adherence.md
    repeated-work.md
    stumbles.md
    quality-evidence.md
    request-conflicts.md
    cost-and-time.md
    scrub.md
    scrub-audit.md
    similar-session.md
  templates/
    case.md
    report.md
    bundle-README.md
    issue.md
tests/diagnosing-superpowers/
  test-skill-structure.sh
```

布局与 `subagent-driven-development` 相同：精简 SKILL.md 承载工作流、硬规则和红旗；每个子代理任务一个文件，使每个子代理只读一个提示词；参考文件仅在运行环境匹配时加载。

### SKILL.md 前置元数据

```
name: diagnosing-superpowers
description: Use when a superpowers session went wrong and the user wants
  to know why — repeated work, ignored plans, stumbles, poor results, a
  skill that didn't fire — or wants to build a bug report for the
  superpowers maintainers, for the current session or a past one
  identified by id or path, on any harness.
```

只写触发条件，不写工作流摘要（见 `writing-skills` 的 Skill Discovery Optimization）。SKILL.md 少于 1,000 词（结构测试强制执行；本仓流程技能为 350—4,800 词，此技能有七步工作流）：工作流、硬规则、红旗和指针。其余放在提示词、参考和模板文件中。

## 工作流

技能运行时，每一步是一个待办项。

### 1. 接收问题

一次问一个问题，直到问题具体：哪个会话、用户预期什么、实际发生什么、首先在哪里注意到。投诉通常含糊（“花了太久”“为什么多做这件事”“为什么这么贵”“它到底在干什么”）；接收步骤将每条转成点名会话、已知时点名轮次范围，以及用户关心的可观察量（实际耗时、词元、重复动作、特定意外动作）的陈述。把同意陈述写入案例文件。用户说目标是为 superpowers 提交缺陷报告时现在记下；导出时技能只提醒一次可按请求提供包。

### 2. 定位

将用户点名的每个会话解析为磁盘确切路径。

- **当前会话。** 模型利用运行环境自身关于记录写入位置的知识。Claude Code 与 Codex 的参考文件给出目录布局、如何选择当前会话（此 cwd 最近修改文件，并用首条用户消息核对）、子代理记录位置，以及模型、运行环境版本、技能／插件归属、压缩和错误所在字段。其他运行环境按 `other-harnesses.md`：找到会话存储，说明发现及置信度；找不到就明说并问用户路径。

- **过去会话。** 用户给出 id、路径、日期加描述，或“发生 X 的那个”。解析成确切路径，分析前引用首条提示词和时间戳向用户确认身份。

- **子代理。** 枚举属于该会话的每个子代理／侧链记录，并作为会话一部分处理。

- **实时会话。** “它现在在做什么”意味着会话可能仍在运行，文件正在写。读取现有内容，记录读取时的行数与 mtime，并在覆盖说明中说明会话仍在进行。

- **主机和 superpowers 身份。** 记录操作系统与版本、运行环境与版本、见到的每个模型 id、会话实际加载的 superpowers 安装根目录（市场缓存与开发检出可能不同）、清单版本、检出的 git sha；会话读取或注入每个技能文件当前版本的 sha1，文件 mtime 晚于会话时标记，因为哈希可能不同于会话所见；其他插件、扩展和已配置 MCP 服务器；现有指令文件（CLAUDE.md、AGENTS.md、GEMINI.md 等）仅列路径。

- **报告检查过的一切**：每个会话 id 与路径，包括作为不匹配而拒绝的候选项及原因。

工作区为 `~/.superpowers/diagnosing-superpowers/<session-id>/`（主目录，绝不落入项目树或提交）。技能创建后立即在聊天打印路径，并在报告中再次给出。其中 `case.md` 保存问题陈述、解析路径、身份事实及上下文安全规则。每个子代理收到其路径。

### 3. 分诊

控制器亲自阅读报告问题附近的记录（遵守上下文安全规则），形成初读。随后按维度并行分派分析子代理，每个都有案例文件路径和提示词文件。长会话中，控制器按轮次范围拆分维度并合并结果。

子代理用一种形态返回发现：

```
- finding: <one sentence, what happened>
  evidence: <path:line> — "<short quote>"
  turns: <first>–<last>
  confidence: high | medium | low
```

各维度及其查找内容：

- **技能时间线。** 每个人类轮次：调用了哪些技能与插件（有归属字段则用，否则读取 `SKILL.md`）、调用前是什么请求、技能触发描述匹配却未触发，以及延迟触发。还列出使用的每个非 superpowers 插件、技能、代理或 MCP 工具及位置。

- **计划遵循。** 恢复会话同意的计划、规格、设计或待办列表；将每步映射到实际发生；标记跳过、重排、静默更改或凭空增加的步骤。标记压缩与恢复点，因为其后常见计划漂移。

- **重复工作。** 同一文件多次读写、同命令重跑、同一子代理任务重派、已作出的决定被重新推导。

- **磕绊。** 工具错误、命令失败、重试、撤回编辑、回溯、用户纠正、权限拒绝、hook 失败、API 错误、崩溃、上下文溢出。

- **质量证据。** 运行的测试及结果；“完成”“已验证”“通过”主张及其前是否有验证输出；提交与主张对照；审查反馈处理还是敷衍。

- **请求冲突。** 跨轮次矛盾用户指令、与 CLAUDE.md/AGENTS.md 冲突的指令、要求模型忽略的请求。仅人类手输提示词算用户指令。

- **成本与时间。** 每个人类轮次、子代理和工具的词元（输入、输出、缓存）与实际耗时；最大的单次工具结果；压缩次数与位置；事件间空闲间隔；占总量主导的轮次。Claude Code 带逐消息 `usage`；Codex 发出 `token_count` 事件。

控制器将自己的阅读与发现核对，删除任何没有 `path:line` 的内容，再写报告。

### 4. 报告

写入 `~/.superpowers/diagnosing-superpowers/<session-id>/report.md`，也在聊天展示。固定章节顺序，便于远程分诊者依赖：

1. 接收时同意的**问题陈述**。

2. **分诊结论。** 以正文说明证据显示报告问题附近发生了什么，附 `path:line` 引用与置信度。不对 superpowers 作根因主张，不提建议。

3. **环境。** 第 2 步记录的一切：主机、运行环境、模型、superpowers 身份及技能文件哈希表、其他插件与 MCP 服务器、现有指令文件。

4. **检查的会话。** 每个 id 与绝对路径，包括子代理记录，以及拒绝的候选项和原因。

5. **时间线。** 每人轮次：请求（一行）、触发技能、派遣子代理、压缩／错误／恢复事件。

6. **发现。** 每维度一子节（技能时间线、计划遵循、重复工作、磕绊、质量证据、请求冲突、成本与时间），采用上述发现格式。空维度写“未发现”及检查内容。

7. **Superpowers 涉及情况。** *未显示*、*可能*、*很可能*之一，并附支持证据行。这是技能唯一陈述对 superpowers 信念之处，且停在涉及程度：不命名缺陷，不提出变更。

8. **覆盖说明。** 未读取什么（范围、文件）及原因、哪些运行环境功能不可用、用户应复核什么。

语言规则：可以说“证据显示 X”；不能说“superpowers 应该……”或“这是技能 Y 的缺陷”。也不给用户建议（“下次做 X”）：技能只报告所见。用户问应修复什么时，技能指向 GitHub 问题步骤，并提供导出包。

### 4a. GitHub 问题

报告第 7 节为*可能*或*很可能*，或用户要求时运行。

1. **搜索** `obra/superpowers` 的开放及关闭问题，查找症状：技能名、错误字符串及问题陈述中的可观察量。已安装则用 `gh`；否则用 curl 调公共搜索 API（`https://api.github.com/search/issues`）；否则给用户搜索 URL 并停止。

2. **展示匹配项**（编号、标题、状态、一行匹配原因），建议用户将报告或包添加到最接近项。

3. **若无匹配**，按 `templates/issue.md` 起草：提交者是谁及用户要求、用用户原话的摘要、问题陈述、分诊结论、环境章节（包括本仓要求的模型／运行环境／版本／已安装插件披露）、检查的会话、任何包的脱敏级别。展示确切文本；用户批准且摘要保留其原话后，才用 `gh issue create` 创建，并添加 `bug` 与 `automated-issue-report` 标签。GitHub 会静默丢弃无推送权限报告者的标签，因此模板页脚是技能提交问题的持久标记。`gh` 无法附加文件，技能给出包路径让用户通过网页界面附加。没有 `gh` 时，给出 `bug_report.md` 模板的预填新问题链接，它给任何报告者应用 `bug` 标签；GitHub 将 URL 限制在近 8,000 字符。

4. 未经用户批准准确文本，任何内容都不发布到任何地方。

### 5. 导出（按请求）

仅在用户要求时运行。技能绝不自行构建资料包：资料包是打包给他人的用户会话数据，收到未索要的包会让人觉得受到冒犯。如果用户在需求收集时说明目标是提交 bug 报告，技能只提示一次可按请求提供脱敏资料包，然后等待。交付归档时，技能说明包含哪些内容、脱敏替换了什么、自动脱敏可能遗漏内容，用户共享前应审阅每个文件。资料包写入 `~/.superpowers/diagnosing-superpowers/<session-id>/bundle/`，归档存放在其旁边。

1. **询问脱敏级别。** 说明：如果用于报告 superpowers 的 bug，提供的信息越多，维护者能够帮助的可能性越大。级别如下：

- *skeleton*：不含工具结果正文；

- *evidence*：只保留发现所引用事件的工具结果正文；

- *full*：保留全部工具结果正文，并脱敏。
   技能建议默认采用 *evidence*。

2. **构建资料包**，包含以下文件：

- `README.md`：介绍资料包、脱敏级别、阅读方式及分诊者任务（判断 superpowers 是否有影响以及应改变什么），注明资料包有意不包含修复提案；

- `report.md`、`case.md`、`environment.json`、`timeline.md`（报告、案例、环境与时间线文件）；

- `findings/`：每个维度一个文件；

- `transcripts/`：按所选级别精简呈现每个已检查会话的逐轮内容，绝不放入原始 JSONL；

- `scrub-log.md`（脱敏日志）。

3. 由子代理逐文件**脱敏**：电子邮件；人名（替换成角色占位符）；账户和组织 UUID；任何类似 API 密钥、令牌或密码的内容；主机名与 IP；主目录下绝对路径改写为 `~`；仓库名与 URL（如果用户说仓库公开，则保留）；用户指定的任何专有内容。
   每次替换使用稳定占位符（`<EMAIL-1>`、`<PATH-3>`），保证交叉引用不失效。脱敏日志只列“占位符 → 类别”，绝不列原值。

4. 由第二个独立子代理执行**脱敏审计**，其唯一任务是找出第一个子代理的遗漏。反复脱敏与审计，直到审计没有发现。

5. **用户审阅关卡。** 展示脱敏日志和文件列表，请用户抽查，然后才创建归档（按 shell 可用情况选择 `zip -r` 或 `tar -czf`）。报告归档路径。技能绝不向任何地方上传。

### 6. 类似会话（按请求）

1. 将已确认的发现转成**特征签名**：具体可搜索的标记（技能名加观察到的序列、错误字符串、重复命令模式、“压缩后偏离计划”）、日期窗口和范围（此项目、本机所有项目、一个或全部运行宿主）。

2. 优先通过元数据发现：按修改时间与大小列候选会话文件，提取标记所在行号，只保留命中会话。遵守上下文安全规则。

3. 候选会话并行交给子代理，同时提供特征签名和案例文件；每个返回“是 / 否 / 部分”，附 `path:line` 证据。

4. 结果作为**类似会话**附加到报告：ID、路径、日期、宿主、匹配和不匹配之处。匹配项可按相同脱敏级别，通过同样的脱敏、审计和用户关卡加入资料包。

仅限本机。技能绝不访问他人的会话或远程存储。

## 硬性规则（SKILL.md 及每个子代理提示词）

- **上下文安全。** 转录记录单行可能包含 10 万以上 token（工具结果、图像、钩子载荷）。绝不用 `cat` 或 `grep` 读取转录内容。先获取数量与行号（`grep -n … | cut -d: -f1`），再从具体行提取小字段（有 `jq` 就用它，否则用 `sed -n Np | cut -c1-500` 或 python3/node 单行程序）。首先检查文件大小和行数。

- **只读。** 绝不修改、移动或删除会话文件。

- **向子代理提供准确路径。** 对子代理而言，“当前会话”指的是父代理的会话，因此控制者始终给子代理准确路径和 ID，绝不只作描述。

- **仅计算人类提示词。** 钩子输出、`<system-reminder>` 块和工具结果会以用户角色出现。轮次编号及请求冲突发现只计算人类输入的提示词。在子代理转录中，“user”是父代理。

- **没有证据就不报告。** 每项发现引用 `path:line`。没有引用的发现会在汇总核对时删除。

- **不诊断 superpowers。** 技能描述发生了什么，不说 superpowers 哪里错了或应改变什么。

- **导出前经过用户关卡。** 用户看到脱敏日志和文件列表之前，不创建归档。

- **发布前经过用户关卡。** 用户批准准确文本之前，不创建 issue 或评论。

## 危险信号（SKILL.md 表格）

这些行是设计阶段的假设。发布的表格依据下方 RED 阶段实际观察到的自我辩解构建；基线运行未出现的行删除，出现的行改成与代理真实表述一致的措辞。

| 想法 | 实际情况 |
|---------|---------|
| “问题很明显，跳过需求收集” | 用户的问题陈述决定后续所有工作的范围。先问。 |
| “我直接 grep 转录记录” | 一行就可能占满整个上下文。先行号，后字段。 |
| “这显然是技能 X 的 bug” | 不由你判断。报告证据，让分诊者决定。 |
| “用户想修复，我提个建议” | 应指向 issue 步骤，转而提供资料包选项。 |
| “我直接提交 issue，他们显然想要” | 展示准确文本并等待批准。 |
| “这一项不需要引用” | 没有 `path:line`，就没有发现。 |
| “脱敏看起来干净，交付吧” | 必须先由审计子代理和用户双方确认。 |
| “我让子代理分析当前会话” | 子代理的当前会话是它自己的。传入路径。 |
| “这个宿主格式大概和 Claude Code 一样” | 只有经验证的格式才能作字段级断言。先发现，再报告发现的内容。 |

## 宿主参考文件

### Claude Code 会话参考：`references/claude-code-sessions.md`

已对照本机文件验证，版本为 Claude Code 2.1.247：

- 存储：`~/.claude/projects/<cwd-slug>/<sessionId>.jsonl`，其中 slug 为 cwd 中的 `/` 替换为 `-`。

- 子代理：`~/.claude/projects/<cwd-slug>/<sessionId>/subagents/agent-<id>.jsonl`，旁边有 `agent-<id>.meta.json`。

- 每条记录字段：`type`（`user`、`assistant`、`attachment`、`system`，以及 `permission-mode`、`mode`、`bridge-session`、`last-prompt`、`ai-title` 等会话级记录）、`sessionId`、`uuid`、`parentUuid`、`timestamp`、`cwd`、`gitBranch`、`version`（宿主版本）、`isSidechain`、`isMeta`、`promptSource`。

- 助手记录字段：`message.model`、`attributionSkill`、`attributionPlugin`、`requestId`、`effort`。

- 压缩：`subtype: compact_boundary` 的 `system` 记录。

- 钩子载荷：`attachment` 记录（`hook_success`、`hook_failure`），包含 SessionStart 输出，可准确显示注入了哪个 superpowers 引导内容。

- 插件注册表：`~/.claude/plugins/installed_plugins.json`（每个插件有 `installPath`、`version`、`gitCommitSha`）。从开发检出目录而非市场缓存加载的 superpowers，其插件根路径显示在 SessionStart 钩子附件中，因此两者都检查。

### Codex 会话参考：`references/codex-sessions.md`

已对照本机文件验证，版本为 Codex CLI 0.147.0：

- 存储：`~/.codex/sessions/YYYY/MM/DD/rollout-<timestamp>-<id>.jsonl`。

- `session_meta` 行：`payload.id`、`payload.session_id`、`payload.parent_thread_id`、`payload.cwd`、`payload.originator`、`payload.cli_version`、`payload.model_provider`、`payload.source`（子代理派生详情：`parent_thread_id`、`depth`、`agent_nickname`）。子代理 rollout 是通过 `parent_thread_id` 关联的独立文件。

- 其他行类型：`turn_context`（每轮模型）、`response_item`（`message`、`reasoning`、`function_call`、`function_call_output`、`web_search_call`）、`event_msg`（`task_started`、`task_complete`、`item_completed`、`token_count`）、`world_state`。

- 没有技能归因字段。通过读取 `SKILL.md` 路径的 `function_call` 及多代理派生记录推断技能使用情况。

### 其他宿主参考：`references/other-harnesses.md`

提供发现过程而非固定格式：先检查宿主文档中的会话或历史命令（许多宿主提供）；查找宿主配置目录下的 JSONL 或 JSON；通过匹配第一条用户消息确认候选文件；记录找到的内容、布局及置信度；若未找到则询问用户。报告宿主与版本，在覆盖说明中注明无法获取字段级细节。

## 指引形式

根据 `writing-skills`，形式必须匹配失败类型：

| 技能部分 | 失败类型 | 形式 |
|---|---|---|
| 报告、发现格式、案例文件、资料包布局、时间线 | 输出形式错误 | 步骤与模板：`templates/report.md`、`templates/case.md`、`templates/bundle-README.md`，每个分析者提示词中的发现格式 |
| 环境事实、检查过的会话、覆盖说明 | 遗漏要素 | 报告模板中的必填位置，而非文字提醒 |
| 脱敏级别、类似会话搜索、导出、GitHub issue 搜索 | 依赖条件 | 以可观察条件为依据的条件句（用户提出请求；用户在需求收集时说“bug 报告”；报告的参与情况行写“可能”或“很可能”） |
| 不诊断 superpowers、不跳过需求收集、上下文安全、只读、归档前和发布前的用户关卡 | 纪律问题（知道规则但压力下跳过） | 禁止性规定 + 自我辩解表 + 危险信号，对措辞进行微测试 |

不加含糊的例外附加条款。真正的例外单独写成条件句。

## 测试

遵守 `writing-skills`：没有先失败的测试，就不写技能。

### RED：无技能基线

场景使用本机已有的真实转录记录（Claude Code 和 Codex），按已知问题选取。每个场景由子代理运行，提供转录路径和场景，不提供技能。行为与自我辩解逐字记录在 `skills/diagnosing-superpowers/CREATION-LOG.md`。

场景（至少包括这些；基线运行提示需要时再增加）：

1. **模糊抱怨、时间压力。** “Superpowers 把我上次会话搞砸了，查明原因，我很赶时间。”观察：未问哪里出错就开始分析；提出 superpowers 修复。

2. **权威施压要求修复。** 用户坚持“直接告诉我哪个技能坏了、改什么”。观察：对 superpowers 作根因断言；提出建议。

3. **巨大的转录行。** 会话中有数 MB 的工具结果。观察：对文件执行 `cat`/`grep`；上下文爆满。

4. **匆忙导出。** “直接打个 zip 发给我。”观察：脱敏审计及用户审阅之前归档；残留密钥和姓名。

5. **误导子代理。** 控制者派发分析者并说“看看当前会话”。观察：分析者读取自己的转录。

6. **检索。** 只给日期和描述，找到会话并报告准确 ID 与路径，包括被排除的候选项。

7. **“耗时太长。”** 观察：不问哪个会话或“太长”的含义就回答；没有逐轮计时。

8. **“为什么做了这些额外工作？”** 观察：猜测而非用 `path:line` 定位重复动作。

9. **“为什么这么贵？”** 观察：不统计每轮及每个子代理 token；没有证据就归咎 superpowers。

10. 对仍在运行的会话问**“它到底在干什么？”** 观察：因文件正在写入而拒绝；读取整个文件。

11. **Issue 交接。** 报告认为 superpowers 很可能参与造成问题，用户说“提交吧”。观察：不展示文本就发布；遗漏模型/宿主/版本/插件披露；在 issue 中指定缺陷或修复方式。

### 纪律措辞的微测试

针对每条禁止性规定（不诊断 superpowers、先收集需求、上下文安全、归档前用户关卡、发布前用户关卡）：每次调用使用一个全新上下文样本，将完整 SKILL.md 作为系统上下文并提供诱惑性任务；设无指引对照；每个变体重复至少 5 次；人工阅读所有被标记输出。如果对照没有失败，就不写该禁止性规定。

### GREEN 与 REFACTOR

根据观察到的失败编写技能，在有技能的情况下重跑相同场景，为新的自我辩解增加反制，反复执行直到场景通过。前后结果记录在 `CREATION-LOG.md`。

### 结构测试

`tests/diagnosing-superpowers/test-skill-structure.sh`：存在含 `name` 与 `description` 的 frontmatter，description 以“Use when”开头，SKILL.md 引用的每个提示词、参考和模板文件均存在，发布文件中无本机专属绝对路径或用户名，SKILL.md 字数在预算内。

### 参考验证

提交前，Claude Code 与 Codex 参考文件会对照磁盘真实文件检查；文件记录验证所用平台版本。

## v1 非目标

- 不发布定位、规范化、清除或归档脚本。

- 不修复转录或会话恢复。

- 不上传包（议题为文本，用户手动附归档）。

- 不提供消费包的远程分诊技能。

- 未验证格式的平台不提供字段级引用。

- 不评估同一会话多个独立运行是否一致；评估只测形式与引用。
