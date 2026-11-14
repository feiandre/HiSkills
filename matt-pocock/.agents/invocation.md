# Model-invoked vs user-invoked

<!-- zh-CN:begin 4a5959ce487f95de -->

# 模型调用与用户调用

<!-- zh-CN:end 4a5959ce487f95de -->

Every `SKILL.md` in this repo is a skill. The one axis that splits them is **invocation**, who can reach it:

<!-- zh-CN:begin dbdb55ff46ce0b8a -->

本仓库每个 `SKILL.md` 都是技能。划分它们的唯一轴是**调用方式**，即谁能到达它：

<!-- zh-CN:end dbdb55ff46ce0b8a -->

- **User-invoked**: reachable **only by the human typing its name**. Set `disable-model-invocation: true` in the frontmatter (Claude Code) and `policy.allow_implicit_invocation: false` in `agents/openai.yaml` (Codex). The `description` is **human-facing**: a one-line summary read by a person browsing slash-commands. Strip trigger lists ("Use when the user says…").

<!-- zh-CN:begin 89f388d798471e8b -->

- **用户调用**：**只能由人输入名称到达**。在 Claude Code 前置元数据设置 `disable-model-invocation: true`，在 Codex 的 `agents/openai.yaml` 设置 `policy.allow_implicit_invocation: false`。`description` **面向人**：供浏览斜杠命令的人阅读的一行摘要，移除触发条件列表（“当用户说……时使用”）。

<!-- zh-CN:end 89f388d798471e8b -->
- **Model-invoked**: reachable by **model or user**. The default: omit `disable-model-invocation` and the `policy` block from `agents/openai.yaml`. The `description` is **model-facing** and keeps rich trigger phrasing ("Use when the user wants…, mentions…, asks for…") so auto-invocation fires. The test for whether a skill should stay model-invoked: _could the model usefully reach for this autonomously?_ (Reuse is the reason to extract a skill, not the test.)

<!-- zh-CN:begin 6fd10558eb6d1b54 -->

- **模型调用**：**模型或用户**均可到达。这是默认值：省略 `disable-model-invocation`，并省略 `agents/openai.yaml` 的 `policy` 块。`description` **面向模型**，保留丰富触发措辞（“当用户想……、提到……、请求……”），以便自动调用。判断技能是否保持模型调用：_模型能否有用地自主使用它？_（复用是提取技能的理由，不是判断标准。）

<!-- zh-CN:end 6fd10558eb6d1b54 -->

Each harness excludes a user-invoked skill from the model's reach in its own way, so nothing but the human can fire it: no other skill can. A user-invoked skill may invoke model-invoked skills, but it can never reach another user-invoked skill.

<!-- zh-CN:begin 84beea2d6dca5d03 -->

各平台以自己的方式把用户调用技能排除在模型可及范围外，因此只有人能触发，其他技能也不能。用户调用技能可调用模型调用技能，但绝不能到达另一用户调用技能。

<!-- zh-CN:end 84beea2d6dca5d03 -->

Every skill also carries an `agents/openai.yaml` beside its `SKILL.md`. It holds Codex UI metadata: `interface.display_name` and `interface.short_description` for the skill picker, and, for user-invoked skills, the `policy.allow_implicit_invocation: false` that pairs with `disable-model-invocation`. Keep the two in sync: a skill is user-invoked in both harnesses or neither.

<!-- zh-CN:begin c715616e7af009d3 -->

每个技能的 `SKILL.md` 旁还有 `agents/openai.yaml`，保存 Codex UI 元数据：技能选择器的 `interface.display_name` 和 `interface.short_description`；用户调用技能还含与 `disable-model-invocation` 配套的 `policy.allow_implicit_invocation: false`。两边保持同步：技能在两个平台中要么都是用户调用，要么都不是。

<!-- zh-CN:end c715616e7af009d3 -->

Bucket `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked**.

<!-- zh-CN:begin cdf249aa8b646c28 -->

主题桶 `README.md` 与顶层 `README.md` 将条目分为**用户调用**和**模型调用**。

<!-- zh-CN:end cdf249aa8b646c28 -->

## Dependencies between them

<!-- zh-CN:begin 5a773f93ca4ad114 -->

## 它们之间的依赖

<!-- zh-CN:end 5a773f93ca4ad114 -->

Dependencies are expressed as an explicit instruction to **call the Skill tool** with the named skill (`Call the Skill tool with "grilling"`), not deep `../other-skill/FILE.md` cross-references, and not a bare `/skill`-style mention left for the model to interpret. Naming the tool is what gets it fired: most harnesses expose skill invocation as a tool the model calls, and spelling that out gets a higher hit rate than dropping a `/name` into prose and hoping it's read as a command. Dropping the leading `/` also keeps this harness-neutral rather than less: a skill name on its own carries no assumption about which harness's trigger syntax it belongs to. Shared reference docs live inside the skill that owns them; other skills reach that material by calling the Skill tool with it, not by linking across folders.

<!-- zh-CN:begin a20390f5d7dfadb0 -->

依赖应写成明确指令，**调用 Skill 工具**并指定技能名（`Call the Skill tool with "grilling"`），不用深层 `../other-skill/FILE.md` 交叉引用，也不留下裸 `/skill` 提及让模型解释。明确工具名更容易触发：多数平台将技能调用暴露为工具，说清楚比在正文放 `/name` 并指望它被读成命令命中率更高。去掉前导 `/` 也保持平台中立：单独技能名不预设某平台触发语法。共享参考文档位于拥有它的技能内；其他技能通过调用该技能获取，不跨文件夹链接。

<!-- zh-CN:end a20390f5d7dfadb0 -->

This is about **operative** instructions: a skill's own steps telling the agent to go run another skill right now. Router prose that just names skills for a human to pick from (`ask-matt`, bucket `README.md`s) isn't invoking anything, so it keeps `/skill`-style names as plain labels.

<!-- zh-CN:begin a6c0da87a4353de1 -->

这里针对**操作指令**：技能步骤要求代理立即运行另一技能。只为供人挑选而列出名称的路由文字（`ask-matt`、桶 `README.md`）不调用任何东西，因此保留 `/skill` 形式作为普通标签。

<!-- zh-CN:end a6c0da87a4353de1 -->

The Skill tool takes one skill per call. A step that needs two skills is two calls, not one call with two names: say so (`Call the Skill tool twice, for "grilling" and "domain-modeling"`), not "call it with X and Y," which reads as a single call taking both.

<!-- zh-CN:begin 2227b1d1c207dc47 -->

Skill 工具每次只接受一个技能。需要两个技能的步骤要调用两次，不能说成一次调用含两个名称；应写（`Call the Skill tool twice, for "grilling" and "domain-modeling"`），不要写“用它调用 X 和 Y”。

<!-- zh-CN:end 2227b1d1c207dc47 -->

This whole convention only holds when the named skill is **model-invoked**. A user-invoked skill can never be reached this way, full stop: per the invariant above, no other skill can call it, including by naming it to the Skill tool. When a step's precondition is a user-invoked skill (e.g. `setup-matt-pocock-skills`), phrase it as an instruction for the human to act on: "tell the user to run `/setup-matt-pocock-skills`", never as a Skill tool call.

<!-- zh-CN:begin f695432d653bfe07 -->

整个约定只在被点名技能是**模型调用**时成立。用户调用技能绝不能用此方式到达：其他技能不能调用它，包括把它交给 Skill 工具。步骤前置条件为用户调用技能（如 `setup-matt-pocock-skills`）时，写成让人执行的指令：“告诉用户运行 `/setup-matt-pocock-skills`”，绝不写成 Skill 工具调用。

<!-- zh-CN:end f695432d653bfe07 -->

## Passive vs active domain work

<!-- zh-CN:begin 4d6bb33b53f4a85d -->

## 被动与主动领域工作

<!-- zh-CN:end 4d6bb33b53f4a85d -->

Merely _reading_ `GLOSSARY.md` for vocabulary is a one-line prose pointer, not the `domain-modeling` skill. Only the active build/sharpen discipline (challenge terms, edge-case scenarios, write ADRs, update `GLOSSARY.md` inline) is `domain-modeling`.

<!-- zh-CN:begin 367f7a3bd503683e -->

仅为词汇而_阅读_ `GLOSSARY.md` 是单行文字指针，不是 `domain-modeling` 技能。只有主动构建/完善纪律（挑战术语、边界情形、写 ADR、同步更新 `GLOSSARY.md`）才属于 `domain-modeling`。

<!-- zh-CN:end 367f7a3bd503683e -->
