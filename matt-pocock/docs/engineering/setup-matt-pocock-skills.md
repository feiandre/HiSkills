## What it does

<!-- zh-CN:begin daee92d02ba1ab44 -->

## 它的作用

<!-- zh-CN:end daee92d02ba1ab44 -->

`setup-matt-pocock-skills` answers three questions about one repo: where issues live, what the triage labels are called, and where the domain docs sit. It records the answers as markdown files under `docs/agents/`.

<!-- zh-CN:begin 1afbbdc86066c6f8 -->

`setup-matt-pocock-skills` 回答关于一个仓库的三个问题：issue 在哪里、分诊标签叫什么、领域文档在哪里。答案记录为 `docs/agents/` 下 markdown。

<!-- zh-CN:end 1afbbdc86066c6f8 -->

Those files are the only thing that varies between repos. The skills themselves are identical everywhere. They read `docs/agents/issue-tracker.md` at run time and do what it says. That is why the set is not tied to GitHub, and why you never edit a skill file to point it at another tracker. Invoking it with "link the skills to a custom issue tracker" works with anything you can connect to programmatically, with no changes to the skills.

<!-- zh-CN:begin aa8ebc51b8d8b4da -->

这些文件是仓库之间唯一变化的部分。技能本身处处相同；运行时读取 `docs/agents/issue-tracker.md` 并照做。因此这套技能不绑定 GitHub，也永远不改技能文件来指向其他跟踪器。以“将技能链接到自定义 issue 跟踪器”调用即可接入任何可程序化连接的系统。

<!-- zh-CN:end aa8ebc51b8d8b4da -->

It is a prompt-driven skill, not a deterministic script. It reads your `git remote`, `CLAUDE.md` and `GLOSSARY.md`, proposes what it found, and waits for you to confirm before it writes anything.

<!-- zh-CN:begin f8d9b4f6babaf218 -->

它是提示驱动技能，不是确定性脚本。读取 `git remote`、`CLAUDE.md` 和 `GLOSSARY.md`，提出发现，写入前等待你确认。

<!-- zh-CN:end f8d9b4f6babaf218 -->

## When to reach for it

<!-- zh-CN:begin 89b2f66c6c5781d3 -->

## 何时使用

<!-- zh-CN:end 89b2f66c6c5781d3 -->

You invoke this by typing `/setup-matt-pocock-skills`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own. Its metadata marks it non-invokable on purpose, so no other skill can fire it for you.

<!-- zh-CN:begin 8dc1a439f5eca75f -->

输入 `/setup-matt-pocock-skills`；[智能体](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。元数据有意标为不可调用，其他技能无法替你触发。

<!-- zh-CN:end 8dc1a439f5eca75f -->

Reach for it once per repo, before the first use of any other engineering skill. If [triage](https://aihero.dev/skills-triage), [to-spec](https://aihero.dev/skills-to-spec), [to-tickets](https://aihero.dev/skills-to-tickets) or [wayfinder](https://aihero.dev/skills-wayfinder) start guessing where your issues go, or apply labels your tracker doesn't have, this repo has not been set up yet. You can run it in a repo halfway through a project. The skill reads what is already there, so no earlier work is lost.

<!-- zh-CN:begin 69a52cd525b223ff -->

每个仓库在首次使用其他工程技能前运行一次。如果 [triage](https://aihero.dev/skills-triage)、[to-spec](https://aihero.dev/skills-to-spec)、[to-tickets](https://aihero.dev/skills-to-tickets) 或 [wayfinder](https://aihero.dev/skills-wayfinder) 开始猜 issue 去向，或使用跟踪器没有的标签，就尚未设置。项目中途可运行；它读取已有内容，不丢失先前工作。

<!-- zh-CN:end 69a52cd525b223ff -->

## Prerequisites

<!-- zh-CN:begin 45453376dfb94c60 -->

## 前提条件

<!-- zh-CN:end 45453376dfb94c60 -->

It writes into the repo you run it in:

<!-- zh-CN:begin eaed4647173ac94f -->

它写入当前仓库：

<!-- zh-CN:end eaed4647173ac94f -->

| It writes | Where |
| --- | --- |
| `issue-tracker.md` | `docs/agents/` |
| `domain.md` | `docs/agents/` |
| `triage-labels.md` | `docs/agents/`, only when the `triage` skill is installed |
| An `## Agent skills` block | whichever of `CLAUDE.md` or `AGENTS.md` already exists |

<!-- zh-CN:begin 0af03ac6d5989d38 -->

| 写入 | 位置 |
|---|---|
| `issue-tracker.md` | `docs/agents/` |
| `domain.md` | `docs/agents/` |
| `triage-labels.md` | `docs/agents/`，仅安装 `triage` 技能时 |
| `## Agent skills` 块 | 已存在的 `CLAUDE.md` 或 `AGENTS.md` |

<!-- zh-CN:end 0af03ac6d5989d38 -->

You commit all of it as markdown. There is no user-level or global mode. The config lives in the repo, so every repo gets its own copy.

<!-- zh-CN:begin e5af031d5197328f -->

全部作为 markdown 提交。没有用户级或全局模式；配置在仓库中，每个仓库一份。

<!-- zh-CN:end e5af031d5197328f -->

## The three decisions

<!-- zh-CN:begin 2db220c1161434c8 -->

## 三个决定

<!-- zh-CN:end 2db220c1161434c8 -->

It starts each section with the recommended answer, and skips any question its exploration already answered. Most runs need only two confirmations.

<!-- zh-CN:begin bb2b65d499b88080 -->

每节先给推荐答案，跳过探索已回答的问题。大多数运行只需两次确认。

<!-- zh-CN:end bb2b65d499b88080 -->

| Decision | What it proposes | When it asks |
| --- | --- | --- |
| **Issue tracker** | the one matching your `git remote` | always, because this is the one real choice |
| **Triage labels** | keep the five canonical names (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`) | only if the `triage` skill is installed |
| **Domain docs** | single-context: one `GLOSSARY.md` plus `docs/adr/` at the root | only if it spots monorepo signals, and then it offers a multi-context `GLOSSARY-MAP.md` |

<!-- zh-CN:begin ba8d8b4fd812e662 -->

| 决定 | 提议 | 何时询问 |
|---|---|---|
| **Issue 跟踪器** | 匹配 `git remote` 的 | 始终，因为这是唯一真正选择 |
| **分诊标签** | 保留五个标准名（`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix`） | 仅安装 `triage` 技能时 |
| **领域文档** | 单上下文：根目录一个 `GLOSSARY.md` 和 `docs/adr/` | 仅发现 monorepo 信号时，并提议多上下文 `GLOSSARY-MAP.md` |

<!-- zh-CN:end ba8d8b4fd812e662 -->

The tracker options:

<!-- zh-CN:begin 390e2c5fc1a74555 -->

跟踪器选项：

<!-- zh-CN:end 390e2c5fc1a74555 -->

| Option | Where issues live | Needs |
| --- | --- | --- |
| **GitHub** | the repo's GitHub Issues | the `gh` CLI |
| **GitLab** | the repo's GitLab Issues | the `glab` CLI |
| **Local markdown** | files under `.scratch/<feature>/` in this repo | nothing, not even a remote |
| **Other** | wherever you say | one paragraph from you describing the workflow |

<!-- zh-CN:begin 98d378b76d4b156d -->

| 选项 | issue 位置 | 需求 |
|---|---|---|
| **GitHub** | 仓库 GitHub Issues | `gh` CLI |
| **GitLab** | 仓库 GitLab Issues | `glab` CLI |
| **本地 markdown** | 本仓库 `.scratch/<feature>/` 文件 | 无需任何内容，甚至无需远程 |
| **其他** | 你指定处 | 你写一段工作流说明 |

<!-- zh-CN:end 98d378b76d4b156d -->

The first three ship as templates in the skill and work out of the box. Local markdown is a full option, not a fallback. The skill supports a solo project with no remote. One caveat: don't use local markdown if you use GitHub. They are alternatives, so pick one.

<!-- zh-CN:begin 30622f6ad8c33e77 -->

前三个内置模板可直接工作。本地 markdown 是完整选项，不是降级；支持无远程的单人项目。注意：使用 GitHub 时不要用本地 markdown，它们是互斥选择。

<!-- zh-CN:end 30622f6ad8c33e77 -->

"Other" is a full option too. It is how Jira, Linear, Azure DevOps and Beads all work. You describe the workflow, the skill records your prose in `docs/agents/issue-tracker.md`, and the downstream skills follow the prose. Users have already built this: a Jira-over-[MCP](https://www.aihero.dev/ai-coding-dictionary/mcp) variant, a Gitea CLI shaped like `gh`, a hand-built local dashboard.

<!-- zh-CN:begin 7e7275c77449003f -->

“其他”也是完整选项，Jira、Linear、Azure DevOps、Beads 均如此。你描述工作流，技能把文字写入 `docs/agents/issue-tracker.md`，下游技能遵循。用户已构建基于 Jira 的 [MCP](https://www.aihero.dev/ai-coding-dictionary/mcp) 变体、形似 `gh` 的 Gitea CLI 和手工本地仪表板。

<!-- zh-CN:end 7e7275c77449003f -->

## Common questions

<!-- zh-CN:begin 6e4cc5f9bc54e973 -->

## 常见问题

<!-- zh-CN:end 6e4cc5f9bc54e973 -->

**Do I have to use GitHub?**

<!-- zh-CN:begin b94379dd25d72772 -->

**必须用 GitHub 吗？**

<!-- zh-CN:end b94379dd25d72772 -->

No. GitHub, GitLab and local markdown under `.scratch/` all ship as ready-made templates, and anything else works through the "other" path. This is the most-repeated question, in roughly these words: *"hard locked to github"*, *"can I use GitLab / Jira"*, *"what about Azure DevOps"*. The answer is always the same: setup chooses the tracker, not the skill.

<!-- zh-CN:begin bb66ce35934b716c -->

不必。GitHub、GitLab 和 `.scratch/` 本地 markdown 都内置，其他通过“其他”路径。最常问的是“硬锁 GitHub 吗”“能用 GitLab/Jira 吗”“Azure DevOps 呢”。答案始终是：设置选择跟踪器，不是技能。

<!-- zh-CN:end bb66ce35934b716c -->

**Do I need to re-run it after updating the skills?**

<!-- zh-CN:begin a1721cb8bd44cd54 -->

**更新技能后需要重跑吗？**

<!-- zh-CN:end a1721cb8bd44cd54 -->

The direct answer after v1.1 was yes. The skill's own closing message is softer. It tells you to re-run only to switch trackers or start over. Both are defensible. The seed templates change between versions, so a `docs/agents/issue-tracker.md` from an older release can go out of date against the skills that now read it. If a downstream skill does something different from what the docs describe, re-run setup. It is cheap.

<!-- zh-CN:begin 0b84c9247f0b4ef3 -->

v1.1 后直接答案是需要；技能结束语更宽松，只建议切换跟踪器或重来时重跑。两者都合理。种子模板会变，旧版 `docs/agents/issue-tracker.md` 可能相对新技能过时。下游技能与文档不符时重跑设置，成本低。

<!-- zh-CN:end 0b84c9247f0b4ef3 -->

**It wrote to `CLAUDE.md`, but I'm on Codex.**

<!-- zh-CN:begin 418a497b91b04a7c -->

**它写入 `CLAUDE.md`，但我用 Codex。**

<!-- zh-CN:end 418a497b91b04a7c -->

This is a known gap, and still open. The file-selection rule is "edit `CLAUDE.md` if it exists, else `AGENTS.md`". It checks which file exists, not which [harness](https://www.aihero.dev/ai-coding-dictionary/harness) is running. In a repo with a `CLAUDE.md` left over from Claude Code, the skill writes its `## Agent skills` block to a file Codex never reads. Users have two workarounds: move the block to `AGENTS.md` by hand, or keep `AGENTS.md` canonical and make `CLAUDE.md` a one-line pointer at it. If neither file exists, the skill asks you which to create instead of picking one. This has confused people who expected it to decide.

<!-- zh-CN:begin 50b5b0c232cc346c -->

这是已知开放缺口。文件选择规则是“存在 `CLAUDE.md` 就编辑它，否则 `AGENTS.md`”；它检查文件存在而非当前[运行环境](https://www.aihero.dev/ai-coding-dictionary/harness)。遗留 Claude Code `CLAUDE.md` 时，块会写进 Codex 不读的文件。变通：手工移动块到 `AGENTS.md`，或让 `AGENTS.md` 成为准据，`CLAUDE.md` 只留一行指针。两文件都不存在时它会询问创建哪个。，相关标识为 `## Agent skills`。

<!-- zh-CN:end 50b5b0c232cc346c -->

**It didn't create my triage labels.**

<!-- zh-CN:begin 1f671d9571593258 -->

**它没有创建分诊标签。**

<!-- zh-CN:end 1f671d9571593258 -->

It doesn't. `docs/agents/triage-labels.md` is a *mapping*: it tells `/triage` which strings in your tracker correspond to the five canonical roles. It does not run `gh label create`. On a fresh GitHub repo the labels do not exist yet, and users have filed this as a bug more than once. Two consequences:

<!-- zh-CN:begin ac41ec1ca25cece0 -->

确实不会。`docs/agents/triage-labels.md` 是*映射*，告诉 `/triage` 跟踪器中哪些字符串对应五个标准角色，不运行 `gh label create`。新 GitHub 仓库标签不存在，用户多次报为 bug。两个后果：

<!-- zh-CN:end ac41ec1ca25cece0 -->

- If your tracker already uses the canonical names, the mapping is an identity table and there is nothing to configure. That is the intended common case, not a missing step.

<!-- zh-CN:begin d04fa005ad9b08f3 -->

- 跟踪器已用标准名时，映射是恒等表，无需配置。这是预期常见情况。

<!-- zh-CN:end d04fa005ad9b08f3 -->
- This skill does not create [wayfinder](https://aihero.dev/skills-wayfinder)'s `wayfinder:map` and `wayfinder:<type>` labels either, and `gh issue create --label <missing>` fails instead of creating the label. Create them by hand before the first wayfinder run on a GitHub repo.

<!-- zh-CN:begin 0d7d5410fda98b38 -->

- 它也不创建 [wayfinder](https://aihero.dev/skills-wayfinder) 的 `wayfinder:map` 和 `wayfinder:<type>` 标签，`gh issue create --label <missing>` 会失败而非创建标签。GitHub 首次运行 wayfinder 前手工创建。

<!-- zh-CN:end 0d7d5410fda98b38 -->

**Can I configure the other skills' behaviour here ([grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) cadence, question format, tone)?**

<!-- zh-CN:begin 57de11d398f2ec76 -->

**可以在这里配置其他技能行为（追问节奏、问题格式、语气）吗？**，相关标识为 [原文链接](https://www.aihero.dev/ai-coding-dictionary/grilling)。

<!-- zh-CN:end 57de11d398f2ec76 -->

No. It configures three things: tracker, labels, doc layout. Users have asked to make it the place for per-user preferences. The answer is that skills stay opinionated and take no per-user config. Preferences belong in your `CLAUDE.md` as plain instructions, which every skill already reads.

<!-- zh-CN:begin 77d62cfc8fb23d40 -->

不可以。它配置跟踪器、标签、文档布局三项。技能保持有主张、无用户级配置。偏好写入 `CLAUDE.md` 普通指令，所有技能都会读取。

<!-- zh-CN:end 77d62cfc8fb23d40 -->

**Can I keep the config in `~/.claude` instead of committing it to every repo?**

<!-- zh-CN:begin 13d6b80174eeaa61 -->

**配置能放在 `~/.claude` 而不提交每个仓库吗？**

<!-- zh-CN:end 13d6b80174eeaa61 -->

Not today. A user who runs the skills across many repos has an open request for this, but no user-level mode exists. Every repo carries its own `docs/agents/`.

<!-- zh-CN:begin 5f40c1e00329bf97 -->

目前不能。跨多仓库用户已有请求，但没有用户级模式；每个仓库带自己的 `docs/agents/`。

<!-- zh-CN:end 5f40c1e00329bf97 -->

**Isn't it strange to have a skill that configures the other skills?**

<!-- zh-CN:begin 5f5ffb98a0b81b3d -->

**用一个技能配置其他技能是否奇怪？**

<!-- zh-CN:end 5f5ffb98a0b81b3d -->

One long-standing complaint says yes, in these words: *"having a skill to set up the other skill does not feel right to me: that means the LLM is configuring its own skills."* The trade-off is real. Without a setup step, every skill that touches issues would need its own copy of the tracker instructions. The output is markdown you can read and edit, and that limits the risk. You can read every file it wrote and change it by hand. Make day-to-day changes that way, not with another run.

<!-- zh-CN:begin add6fed3e9ae4f71 -->

长期反馈认为奇怪：“用技能设置其他技能感觉不对，意味着 LLM 在配置自己的技能。”权衡真实存在：没有设置步骤，每个处理 issue 的技能都要自带跟踪器说明。输出是可读可编辑 markdown，限制风险。可阅读并手工修改它写的每个文件。日常修改这样做，不再重跑。

<!-- zh-CN:end add6fed3e9ae4f71 -->

## It's working if

<!-- zh-CN:begin e79fbc3e8631b880 -->

## 生效时

<!-- zh-CN:end e79fbc3e8631b880 -->

- `docs/agents/issue-tracker.md` and `docs/agents/domain.md` exist, plus `triage-labels.md` if `triage` is installed.

<!-- zh-CN:begin 2ca87ec76d576dc6 -->

- `docs/agents/issue-tracker.md` 和 `domain.md` 存在；安装 `triage` 时还有 `triage-labels.md`。，相关标识为 `docs/agents/domain.md`。

<!-- zh-CN:end 2ca87ec76d576dc6 -->
- An `## Agent skills` section appears in the instruction file your harness reads, with a one-line summary pointing at each of those files.

<!-- zh-CN:begin 929ea9bf0cea5323 -->

- 运行环境读取的指令文件出现 `## Agent skills` 章节，逐文件一行摘要。

<!-- zh-CN:end 929ea9bf0cea5323 -->
- The tracker it proposed matches the remote you use, and the label strings match labels that exist in your tracker.

<!-- zh-CN:begin 59459216333824e2 -->

- 提议跟踪器匹配远程，标签字符串匹配现有标签。

<!-- zh-CN:end 59459216333824e2 -->
- Afterwards, `/to-tickets` publishes without asking you where issues live, and `/triage` applies labels rather than inventing them.

<!-- zh-CN:begin 836c4d0ddbab6db8 -->

- 之后 `/to-tickets` 发布时无需询问 issue 位置，`/triage` 应用标签而非发明标签。

<!-- zh-CN:end 836c4d0ddbab6db8 -->
- Nothing in the skill files themselves changed. If setup edited a `SKILL.md`, something went wrong.

<!-- zh-CN:begin 985c06a112818d39 -->

- 技能文件本身未变；设置若编辑 `SKILL.md`，就是出错。

<!-- zh-CN:end 985c06a112818d39 -->

## Where it fits

<!-- zh-CN:begin b0a7f936f2186bae -->

## 适用范围

<!-- zh-CN:end b0a7f936f2186bae -->

`setup-matt-pocock-skills` is the **run-once setup** for the engineering flow, the precondition everything else assumes rather than a step in the chain. Its neighbours are its readers: [triage](https://aihero.dev/skills-triage), which applies the label vocabulary written here; [to-spec](https://aihero.dev/skills-to-spec) and [to-tickets](https://aihero.dev/skills-to-tickets), which publish into the tracker named here; and [wayfinder](https://aihero.dev/skills-wayfinder), which reads the "Wayfinding operations" section of the same tracker file to learn how to store maps and child [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket). [domain-modeling](https://aihero.dev/skills-domain-modeling) later fills in the domain-doc layout that setup records. It creates `GLOSSARY.md` and ADRs only when you resolve a term or decision, so a repo with no domain docs after setup is normal. For which skill to reach for next, [ask-matt](https://aihero.dev/skills-ask-matt) routes the whole set.

<!-- zh-CN:begin 544f9c15a881b7f2 -->

`setup-matt-pocock-skills` 是工程流程的**一次设置**，是所有其他技能假定而非链中步骤。它的邻居是读取者：[triage](https://aihero.dev/skills-triage)（应用标签词表）、[to-spec](https://aihero.dev/skills-to-spec) 与 [to-tickets](https://aihero.dev/skills-to-tickets)（发布到跟踪器）、[wayfinder](https://aihero.dev/skills-wayfinder)（读取同一跟踪器文档“寻路操作”章节）。[domain-modeling](https://aihero.dev/skills-domain-modeling) 之后填充领域文档布局；只在解决术语或决策时创建 `GLOSSARY.md` 和 ADR，所以设置后没有领域文档很正常。不确定下一技能时，[ask-matt](https://aihero.dev/skills-ask-matt) 路由整套。，相关标识为 [原文链接](https://www.aihero.dev/ai-coding-dictionary/ticket)。

<!-- zh-CN:end 544f9c15a881b7f2 -->
