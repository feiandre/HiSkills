## What it does

<!-- zh-CN:begin 2696ee09cf9b8f0c -->

## 它的作用

<!-- zh-CN:end 2696ee09cf9b8f0c -->

`wizard` generates an interactive bash script that walks a human, step by step, through a manual procedure: wiring up third-party services, running a one-off migration, moving a project from state A to state B. It opens each URL, says what to click and copy, captures what comes back, and writes it into `.env` files and GitHub Actions secrets.

<!-- zh-CN:begin 0234e5431861622f -->

`wizard` 生成交互式 bash 脚本，逐步引导人类完成手动流程：接入第三方服务、运行一次性迁移、把项目从状态 A 移到状态 B。它打开每个 URL，说明点击和复制什么，记录返回内容，并写入 `.env` 文件及 GitHub Actions 秘密。

<!-- zh-CN:end 0234e5431861622f -->

The [agent](https://www.aihero.dev/ai-coding-dictionary/agent) writes the script; it never runs it. You do, on your own machine. A wizard is a program, not a list of instructions. The script runs each step in order and keeps the values you enter. Your part is to click, paste, and press Enter.

<!-- zh-CN:begin 006162697235000c -->

[代理](https://www.aihero.dev/ai-coding-dictionary/agent)编写脚本，绝不运行它。你会在自己的机器上运行。向导是程序，不是指令列表。脚本按顺序运行每一步并保留输入值。你负责点击、粘贴并按下 Enter。

<!-- zh-CN:end 006162697235000c -->

## When to reach for it

<!-- zh-CN:begin 85ef371664c36d32 -->

## 何时使用

<!-- zh-CN:end 85ef371664c36d32 -->

You can type `/wizard`, and the agent can also reach for it on its own. When it hits a step you have to take (a key it can't mint, a dashboard it can't click), it builds you a wizard instead of writing the instructions into the chat, where they scroll away.

<!-- zh-CN:begin 7a5b3a43c59d4d6c -->

你可以输入 `/wizard`，代理也能自行使用。遇到必须由你执行的步骤（它无法生成的密钥、无法点击的后台）时，它会为你构建向导，而不是把指令写进会滚走的聊天。

<!-- zh-CN:end 7a5b3a43c59d4d6c -->

Reach for it when the next thing blocking you is a trip through a dashboard:

<!-- zh-CN:begin fa1225feec03cf94 -->

下一阻碍是一次后台操作时使用它：

<!-- zh-CN:end fa1225feec03cf94 -->

| Situation | What the wizard does |
| --- | --- |
| A new dev needs six services configured before the app boots | Opens each dashboard in order, captures the keys, writes them to `.env` and CI |
| A one-off migration needs switches flipped in a specific order | Sequences the irreversible steps behind confirmation gates |
| A project has to move from state A to state B once | Walks the transition and reports what it could not do |
| You are about to write those steps into a README | Writes an executable version instead, which fails visibly when a step goes stale |

<!-- zh-CN:begin a3a68cc9ae51a54a -->

| 情形 | 向导做什么 |
| --- | --- |
| 新开发者启动应用前要配置六项服务 | 按顺序打开各后台，捕获密钥，写入 `.env` 和 CI |
| 一次性迁移必须按特定顺序打开开关 | 将不可逆步骤排在确认关卡之后 |
| 项目只需从状态 A 移到状态 B 一次 | 走完转换并报告做不到的事 |
| 你准备把这些步骤写进 README | 改写为可执行版本，步骤过期时会明显失败 |

<!-- zh-CN:end a3a68cc9ae51a54a -->

Don't reach for it to *decide* what to build; for that, [grill-with-docs](https://aihero.dev/skills-grill-with-docs) and [to-spec](https://aihero.dev/skills-to-spec) are the tools.

<!-- zh-CN:begin 31e78402bdfcdf57 -->

不要用它*决定*构建什么；那应由 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 和 [to-spec](https://aihero.dev/skills-to-spec) 完成。

<!-- zh-CN:end 31e78402bdfcdf57 -->

## Prerequisites

<!-- zh-CN:begin edf9fb1494ddd8fd -->

## 前置条件

<!-- zh-CN:end edf9fb1494ddd8fd -->

None to generate one. The wizard it writes runs on bash, and uses `gh` when a stage sets a GitHub secret or variable. If `gh` is missing or not authenticated, the run does not fail. That stage shows a warning, and the closing summary tells you what to set by hand.

<!-- zh-CN:begin 31208e66fe7ab076 -->

生成无需前置条件。生成的向导运行于 bash，并在某阶段设置 GitHub 秘密或变量时使用 `gh`。`gh` 缺失或未认证不会导致失败；该阶段显示警告，结束摘要告诉你要手动设置什么。

<!-- zh-CN:end 31208e66fe7ab076 -->

## Stages

<!-- zh-CN:begin 242f7f783888d703 -->

## 阶段

<!-- zh-CN:end 242f7f783888d703 -->

A **stage** is one focused task on one screen. The script clears the terminal between stages, so a stage that overflows the screen loses the part that scrolled away. You author stages in dependency order and set `TOTAL_STAGES`, which drives the progress display.

<!-- zh-CN:begin 2921d3403078ca42 -->

**阶段**是一屏上的一项集中任务。脚本在阶段间清屏，因此溢出屏幕的阶段会丢失滚出部分。按依赖顺序编写阶段，并设置 `TOTAL_STAGES` 控制进度显示。

<!-- zh-CN:end 2921d3403078ca42 -->

The [skill](https://www.aihero.dev/ai-coding-dictionary/skill) scopes the procedure before it writes any script. It reads the repo instead of asking cold: `.env*`, `docker-compose*`, framework config, and every `secrets.*` / `vars.*` reference in `.github/workflows/`. Each of those references is a value the wizard has to produce. It then shows you the ordered stage list to confirm. Only after you confirm does it map each stage to the exact path a human follows ("Dashboard → Developers → API keys → Reveal test key → copy"). Where it doesn't know the current UI, it asks you or checks the docs rather than inventing clicks.

<!-- zh-CN:begin d417041f573d0779 -->

[技能](https://www.aihero.dev/ai-coding-dictionary/skill)先界定流程，再写脚本。它读取仓库而不是冷启动提问：`.env*`、`docker-compose*`、框架配置，以及 `.github/workflows/` 中每个 `secrets.*` / `vars.*` 引用。每个引用都是向导必须产生的值。随后显示有序阶段列表供确认。确认后才把各阶段映射到人的确切操作路径（“Dashboard → Developers → API keys → Reveal test key → copy”）。不知道当前 UI 时，它询问你或查看文档，不臆造点击步骤。

<!-- zh-CN:end d417041f573d0779 -->

For each captured value, scoping decides where it goes:

<!-- zh-CN:begin 6d2ba6c331ba0e09 -->

每个捕获值由界定过程决定去向：

<!-- zh-CN:end 6d2ba6c331ba0e09 -->

| Destination | When |
| --- | --- |
| `.env` only | Local dev needs it, CI doesn't |
| GitHub secret | CI reads it, and it's sensitive |
| GitHub variable | CI reads it, and it's public |
| Both `.env` and a secret | Local dev and CI both need it |
| Nowhere | The stage is a pure action: a switch flipped, a plan upgraded |

<!-- zh-CN:begin 1e34ee5b78cebae4 -->

| 目的地 | 条件 |
| --- | --- |
| 仅 `.env` | 本地开发需要，CI 不需要 |
| GitHub 秘密 | CI 读取且内容敏感 |
| GitHub 变量 | CI 读取且内容公开 |
| `.env` 与秘密 | 本地和 CI 都需要 |
| 不写入 | 阶段是纯动作：打开开关、升级计划 |

<!-- zh-CN:end 1e34ee5b78cebae4 -->

## The template already solves the UX

<!-- zh-CN:begin ee07f80c1918a012 -->

## 模板已解决用户体验

<!-- zh-CN:end ee07f80c1918a012 -->

The [template](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/template.sh) ships the whole experience: progress with time remaining, confirmation gates, cross-platform URL opening including WSL, hidden entry for secrets, idempotent `.env` upserts, `gh secret` / `gh variable` writes, and a closing summary of everything it had to skip. Everything above the `STAGES` marker is a fixed library, identical in every wizard and never hand-edited. Because the library never changes, every wizard behaves the same way. The only work per wizard is to scope the procedure and author its stages.

<!-- zh-CN:begin 207fa57ee5eac3ce -->

[模板](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/template.sh) 提供完整体验：进度与剩余时间、确认关卡、包括 WSL 的跨平台 URL 打开、秘密隐藏输入、幂等 `.env` 更新、`gh secret` / `gh variable` 写入，以及最后汇总被迫跳过的一切。`STAGES` 标记以上部分是固定库，每个向导都相同，绝不手工修改。因为库不变，所有向导行为一致。每个向导只需界定流程和编写阶段。

<!-- zh-CN:end 207fa57ee5eac3ce -->

The agent that writes a wizard never runs it end to end, because the script opens browsers and waits for human input. The agent checks it statically instead: `bash -n`, `shellcheck` where available, and a trace that every value lands where scoping said it would, with every `set_secret` name matching a real `secrets.*` reference in CI. So the first run is yours, and that run is the test.

<!-- zh-CN:begin d0da54071bb0bde5 -->

编写向导的代理从不端到端运行它，因为脚本打开浏览器并等待人工输入。代理改为静态检查：`bash -n`、可用时 `shellcheck`，并追踪每个值都到达界定阶段指定位置，每个 `set_secret` 名称都匹配 CI 中真实 `secrets.*` 引用。因此第一次运行由你完成，那次运行就是测试。

<!-- zh-CN:end d0da54071bb0bde5 -->

## Ephemeral by default

<!-- zh-CN:begin 1bb04870e67fa8aa -->

## 默认是临时的

<!-- zh-CN:end 1bb04870e67fa8aa -->

| What you have | What to do with the script |
| --- | --- |
| A one-off migration, a personal setup, a transition you'll never repeat | Save it to a scratch or `scripts/` path, run it, delete it |
| A setup path the next person on the repo will also need | Commit it and link it from the README, so they run the script instead of re-asking an agent |

<!-- zh-CN:begin 23b86502fffb5d50 -->

| 你拥有的条件 | 如何处理脚本 |
| --- | --- |
| 一次性迁移、个人设置、永不再重复的转换 | 保存到临时或 `scripts/` 路径，运行后删除 |
| 仓库下一位使用者也会用到的设置路径 | 提交并从 README 链接，使其运行脚本而不必再问代理 |

<!-- zh-CN:end 23b86502fffb5d50 -->

## Common questions

<!-- zh-CN:begin f92b0566a77c2fb8 -->

## 常见问题

<!-- zh-CN:end f92b0566a77c2fb8 -->

**Do my API keys end up in the model's context?**

<!-- zh-CN:begin 9d189cf3acd92ebb -->

**API 密钥会进入模型上下文吗？**

<!-- zh-CN:end 9d189cf3acd92ebb -->

No. The agent writes a script; it doesn't run it. You run the script yourself, and it captures the key with hidden terminal entry and writes it straight to `.env` or `gh secret`. The wizard is a CLI, and the model is not connected to it. This holds only for values the wizard captures at runtime. If you paste a key into the chat while scoping the procedure, it's in the [context](https://www.aihero.dev/ai-coding-dictionary/context) like any other pasted text.

<!-- zh-CN:begin e52ba7757793879d -->

不会。代理编写脚本但不运行。你亲自运行，脚本通过隐藏终端输入捕获密钥，直接写入 `.env` 或 `gh secret`。向导是 CLI，模型没有连接它。这仅适用于向导运行时捕获的值。若界定流程时把密钥粘贴到聊天，它就会像任何粘贴文本一样进入[上下文](https://www.aihero.dev/ai-coding-dictionary/context)。

<!-- zh-CN:end e52ba7757793879d -->

**Can I go back and fix a value I mistyped?**

<!-- zh-CN:begin a05cfab7069153cd -->

**我能返回修正输错的值吗？**

<!-- zh-CN:end a05cfab7069153cd -->

Not mid-run. There is no back button. The stages run forward, and a wrong answer on stage 3 means Ctrl-C and re-run. Re-running is cheap, because any value already written to `.env` is offered back as a default, so you press Enter through the stages you got right and retype only the wrong one. Users asked for this in launch week, and it is still open: "loved it! One thing though, is there a way to go back and correct what you've entered?"

<!-- zh-CN:begin 4da53d0d6e40555d -->

运行中不能。没有返回按钮。阶段单向前进，第 3 阶段输错就意味着 Ctrl-C 后重跑。重跑成本低，因为已写入 `.env` 的值会作为默认值提供，你可一路 Enter 跳过正确阶段，只重输错误值。发布周用户已提出这需求，仍未解决：“很喜欢！但能不能返回修正已输入内容？”

<!-- zh-CN:end 4da53d0d6e40555d -->

**Does it know what I've already set up?**

<!-- zh-CN:begin 8b333a50c34d780b -->

**它知道我已完成哪些设置吗？**

<!-- zh-CN:end 8b333a50c34d780b -->

Partly, and less than the launch reactions assumed. It reads the repo before it asks (your `.env` files, `docker-compose`, framework config, the `secrets.*` references in CI), so it scopes to values that are missing rather than starting from zero the way a README does. What it doesn't do is check the third-party service. If a key exists in your `.env` the wizard offers it back and Enter keeps it; if you already created the Stripe account but never saved the key, the wizard still sends you to the dashboard for it.

<!-- zh-CN:begin 89a185bd95bc396c -->

部分知道，但少于发布时反应所假设的程度。提问前读取仓库（`.env` 文件、`docker-compose`、框架配置、CI 中 `secrets.*` 引用），因此只界定缺失值，不像 README 从零开始。它不检查第三方服务。`.env` 已有密钥时会提供并可由 Enter 保留；若已创建 Stripe 账户却从未保存密钥，向导仍会让你去后台获取。

<!-- zh-CN:end 89a185bd95bc396c -->

**Where does it sit in the workflow, after grilling and the spec?**

<!-- zh-CN:begin b2e4c63825944891 -->

**它在工作流中位于追问与规格之后吗？**

<!-- zh-CN:end b2e4c63825944891 -->

Nowhere in particular. It's a standalone, not a chain step. The common guess is `/grill-with-docs → /to-spec → /wizard`, and that sequence is fine, but the trigger is a manual procedure showing up, which can happen at any point: before you start, mid-build, or long after ship. It also works as a discovery tool. Scoping finds the hidden prerequisites of a task, like the three API keys you hadn't thought about, before you commit to the work.

<!-- zh-CN:begin a90ce09ba2b05ccb -->

没有固定位置。它是独立工具，不是链步骤。常见猜测是 `/grill-with-docs → /to-spec → /wizard`，这个顺序可行，但触发器是出现手动流程，可能在任何时点发生：开始前、构建中或发布后很久。它也适合发现：正式投入前，界定过程会发现隐藏前提，例如你没想到的三个 API 密钥。

<!-- zh-CN:end a90ce09ba2b05ccb -->

**Does it work outside Claude Code?**

<!-- zh-CN:begin 077144aa77cc8c5c -->

**它能在 Claude Code 之外工作吗？**

<!-- zh-CN:end 077144aa77cc8c5c -->

The script does. It's plain bash, and it runs the same whatever [harness](https://www.aihero.dev/ai-coding-dictionary/harness) generated it. The skill itself is model-invoked, so it's listed everywhere: type `/wizard` in Claude Code or `$wizard` in Codex, or just describe the setup you're stuck on. Being model-invoked also keeps it clear of [#693](https://github.com/mattpocock/skills/issues/693), where Claude's desktop and web apps drop *user-invoked* skills from the [model](https://www.aihero.dev/ai-coding-dictionary/model)'s listing and report them as not installed.

<!-- zh-CN:begin 32e33cf3f7fd2e1c -->

脚本可以。它是普通 bash，不依赖哪个[运行环境](https://www.aihero.dev/ai-coding-dictionary/harness)生成。技能本身由模型调用，因此各处可见：在 Claude Code 输入 `/wizard`，在 Codex 输入 `$wizard`，或直接描述卡住的设置。模型调用也避开 [#693](https://github.com/mattpocock/skills/issues/693)：Claude 桌面和网页应用会从[模型](https://www.aihero.dev/ai-coding-dictionary/model)列表移除*用户调用*技能并报告未安装。

<!-- zh-CN:end 32e33cf3f7fd2e1c -->

**Didn't this used to be user-invoked?**

<!-- zh-CN:begin cf09c36448105f6d -->

**它以前是用户调用吗？**

<!-- zh-CN:end cf09c36448105f6d -->

It did. It's now model-invoked, so the agent reaches for it unprompted when it hits a step you have to take. Nothing you could do before stopped working. Model invocation lets the agent call the skill as well as you, so `/wizard` behaves as it did. The change fixes one failure. Before, an agent that hit a credentials wall mid-build dumped six numbered steps into the chat for you to follow by hand. Now it writes a wizard.

<!-- zh-CN:begin 22db6ba86af3dc92 -->

是。现在由模型调用，因此代理遇到你必须执行的步骤时可主动使用。以前可做的一切仍可用。模型调用让代理和你都能调用，`/wizard` 行为不变。变更修复了一种失败：以前代理构建中遇到凭据障碍，会把六个编号步骤丢进聊天供手工操作；现在会编写向导。

<!-- zh-CN:end 22db6ba86af3dc92 -->

**It used to be in `in-progress/`. Where is it now?**

<!-- zh-CN:begin c8a92a386c42a8db -->

**它以前在 `in-progress/`，现在在哪？**

<!-- zh-CN:end c8a92a386c42a8db -->

`engineering/`, as of v1.2. It graduated out of the beta bucket and now ships in the plugin, so it arrives with the rest of the promoted set rather than needing an individual install. Its behaviour didn't change on graduation.

<!-- zh-CN:begin caaf4b944e171d84 -->

自 v1.2 起位于 `engineering/`。它从 beta 分类毕业，随插件发布，因此和其他晋升技能一起到达，无需单独安装。毕业时行为未变。

<!-- zh-CN:end caaf4b944e171d84 -->

## It's working if

<!-- zh-CN:begin 61a2ca557f6f2a3c -->

## 正常工作的表现

<!-- zh-CN:end 61a2ca557f6f2a3c -->

- You're shown an ordered list of stages, and the values each one produces, and asked to confirm, before any script exists.

<!-- zh-CN:begin 365c5f68d6ec1652 -->

- 创建任何脚本前，向你展示有序阶段及其产生的值，并请求确认。

<!-- zh-CN:end 365c5f68d6ec1652 -->
- Every URL is opened before the value from that page is asked for. You're never asked to paste something you haven't been sent to fetch.

<!-- zh-CN:begin b4ecd1588dc14f0f -->

- 请求该页面值之前先打开每个 URL。绝不会要求粘贴你尚未被引导获取的内容。

<!-- zh-CN:end b4ecd1588dc14f0f -->
- Secrets are typed blind. Nothing sensitive echoes into your scrollback.

<!-- zh-CN:begin 987644cf69e6de65 -->

- 秘密采用盲输入，敏感内容不会回显到滚动记录。

<!-- zh-CN:end 987644cf69e6de65 -->
- Each stage fits one screen. Nothing you still need has scrolled away.

<!-- zh-CN:begin a0d0084c9e2dec5f -->

- 每个阶段适配一屏，需要的内容不会滚出视野。

<!-- zh-CN:end a0d0084c9e2dec5f -->
- Ctrl-C and re-run picks up where you left off, offering the values already saved as defaults.

<!-- zh-CN:begin 010648df5096c6c7 -->

- Ctrl-C 后重跑可从停点继续，已保存值作为默认值。

<!-- zh-CN:end 010648df5096c6c7 -->
- The final screen lists what it wrote, and separately lists what it couldn't do and you have to finish by hand.

<!-- zh-CN:begin e5e75ae2274d1acd -->

- 最后一屏列出已写入内容，并单独列出无法完成、需手工收尾的事项。

<!-- zh-CN:end e5e75ae2274d1acd -->

## Where it fits

<!-- zh-CN:begin a2b5345adec39215 -->

## 所处位置

<!-- zh-CN:end a2b5345adec39215 -->

`wizard` is a reach-for-it-anytime standalone, sitting at the line where automation stops and a human has to click. Its nearest neighbour is [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills), because both exist to get a repo into a working state. That one configures this skill set, and `wizard` generates a setup path for everything else. It also pairs with [implement](https://aihero.dev/skills-implement): when a build lands a feature that needs credentials or a manual cutover, a wizard covers the steps only a human can do. When you're unsure which skill fits the moment, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin 6ae144fa72909fc1 -->

`wizard` 是随时可用的独立工具，位于自动化停止、人类必须点击之处。最邻近的是 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills)，二者都让仓库进入可用状态；后者配置此技能集，`wizard` 为其他一切生成设置路径。它与 [implement](https://aihero.dev/skills-implement) 搭配：构建交付需要凭据或手动切换的功能时，向导覆盖只能由人完成的步骤。不确定当下适用哪个技能时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。

<!-- zh-CN:end 6ae144fa72909fc1 -->
