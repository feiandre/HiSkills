# benny automation intent

<!-- zh-CN:begin 2c62f4f08454da98 -->

# Benny 自动化意图

<!-- zh-CN:end 2c62f4f08454da98 -->

## what i want to automate

<!-- zh-CN:begin 568f66dec399801a -->

## 我想自动化什么

<!-- zh-CN:end 568f66dec399801a -->

i want two cursor automations that work together in one slack issue channel.

<!-- zh-CN:begin f317480c16e9ce6f -->

我希望两个 Cursor 自动化在同一个 Slack 问题频道内协作。

<!-- zh-CN:end f317480c16e9ce6f -->

### automation 1: triage issue reports

<!-- zh-CN:begin 2b4c13ed2c5a8e1c -->

### 自动化 1：分诊问题报告

<!-- zh-CN:end 2b4c13ed2c5a8e1c -->

- trigger: when someone posts a new top-level report in my configured source slack channel, i want this automation to start on that report and keep its original thread coordinates.

<!-- zh-CN:begin d172c541d81ef8e3 -->

- 触发器：有人在配置的来源 Slack 频道发布新的顶层报告时，我希望自动化从该报告开始，并保留原始线程坐标。

<!-- zh-CN:end d172c541d81ef8e3 -->
- behavior: i want it to read the thread and attachments, classify the report as a bug or performance issue, feature request, question or feedback, or reroute, and trace the likely owning layer before routing.

<!-- zh-CN:begin 02f0877f6230d40e -->

- 行为：读取线程和附件，将报告分类为缺陷或性能问题、功能请求、问题或反馈，或重新路由，并在路由前追踪可能的所属层。

<!-- zh-CN:end 02f0877f6230d40e -->
- tracker: i want it to search my configured tracker for duplicates, update a confident duplicate, and create a ticket only for a clear net-new bug.

<!-- zh-CN:begin 5d6faca1e0014760 -->

- 跟踪器：在配置的跟踪器中搜索重复项，更新有把握的重复项，仅为明确全新的缺陷创建工单。

<!-- zh-CN:end 5d6faca1e0014760 -->
- tools: i want slack thread read and reply access, my configured tracker integration, and my optional routing map.

<!-- zh-CN:begin c199103ee25b21a0 -->

- 工具：我需要 Slack 线程读取与回复权限、配置的跟踪器集成，以及可选的路由地图。

<!-- zh-CN:end c199103ee25b21a0 -->
- outcome: i want exactly one reply in the source thread with a short verdict and `[benny:bug]`, `[benny:performance]`, or `[benny:other]`. a bug or performance marker may include the tracker url.

<!-- zh-CN:begin 8a4f1ee649bb1444 -->

- 结果：来源线程中恰好一条回答，包含简短裁决及 `[benny:bug]`、`[benny:performance]` 或 `[benny:other]`。缺陷或性能标记可包含跟踪器 URL。

<!-- zh-CN:end 8a4f1ee649bb1444 -->
- boundary: i never want this automation to post a root message in the source channel.

<!-- zh-CN:begin 1e0cc94aba236ce9 -->

- 边界：绝不允许自动化在来源频道发布根消息。

<!-- zh-CN:end 1e0cc94aba236ce9 -->

### automation 2: reproduce and fix confirmed bugs

<!-- zh-CN:begin fcda4e07034389c1 -->

### 自动化 2：复现并修复已确认缺陷

<!-- zh-CN:end fcda4e07034389c1 -->

- trigger: i want this automation to start from the same new top-level report, or another supported trigger chosen during setup, then wait for the trusted triage marker in the original thread.

<!-- zh-CN:begin 99ea564c908e5263 -->

- 触发器：从相同的新顶层报告开始，或从设置期间选定的其他支持触发器开始，然后在原始线程等待可信分诊标记。

<!-- zh-CN:end 99ea564c908e5263 -->
- gates: i want it to stop when someone clearly owns the fix. if an existing pull request or merged commit may fix the report, i want verification instead of a competing change.

<!-- zh-CN:begin a28129eed9e397df -->

- 关卡：有人明确负责修复时停止。现有拉取请求或已合并提交可能修复报告时，执行验证，不制造竞争性变更。

<!-- zh-CN:end a28129eed9e397df -->
- behavior: i want it to use my configured control adapter and feature map, reproduce the exact symptom twice through the real ui, and capture screenshots, video, and a read-only state cross-check.

<!-- zh-CN:begin e214adb617c16e28 -->

- 行为：使用配置的控制适配器和功能地图，通过真实 UI 将确切症状复现两次，捕获截图、视频及只读状态交叉检查。

<!-- zh-CN:end e214adb617c16e28 -->
- fix: i want it to verify existing pull requests without authoring over them. after a confirmed repro, it may attempt one bounded root-cause fix, use tdd when the test is cheap, smoke the blast radius, and open a draft pull request only when before-and-after proof passes.

<!-- zh-CN:begin 823a2bba195dc2e7 -->

- 修复：验证现有拉取请求，不覆盖编写。确认复现后，可尝试一次有界根因修复；测试成本低时使用 TDD，快速检查影响范围，仅在前后证明通过时打开草稿拉取请求。

<!-- zh-CN:end 823a2bba195dc2e7 -->
- tools: i want slack thread read and reply access, repository and history access, draft pull request creation, my configured tracker, and my control adapter.

<!-- zh-CN:begin c04bbdab486fa0df -->

- 工具：Slack 线程读取与回复权限、仓库和历史访问、草稿拉取请求创建、配置的跟踪器及控制适配器。

<!-- zh-CN:end c04bbdab486fa0df -->
- outcome: i want evidence and a verified result in the source or optional operations threads, plus an optional draft pull request. updates should be concise.

<!-- zh-CN:begin b5e071ac1201f104 -->

- 结果：在来源线程或可选运维线程中提供证据和已验证结果，以及可选草稿 PR。更新应简洁。

<!-- zh-CN:end b5e071ac1201f104 -->
- boundary: i never want this automation to post a root message in the source channel.

<!-- zh-CN:begin 12de5617a4bc9a0f -->

- 边界：绝不允许自动化在来源频道发布根消息。

<!-- zh-CN:end 12de5617a4bc9a0f -->

### shared rules

<!-- zh-CN:begin 27bc2fe663df76a6 -->

### 共同规则

<!-- zh-CN:end 27bc2fe663df76a6 -->

- i want the source channel and root thread coordinates to stay immutable for the whole run.

<!-- zh-CN:begin e4b79bb371ccfc00 -->

- 整个运行期间，来源频道和根线程坐标保持不变。

<!-- zh-CN:end e4b79bb371ccfc00 -->
- i treat utility and debug bots as evidence, not delegation or fix ownership.

<!-- zh-CN:begin 54e81400ec5f56f7 -->

- 将工具机器人和调试机器人视为证据来源，而非委派或修复责任持有者。

<!-- zh-CN:end 54e81400ec5f56f7 -->
- i allow subagents to help, but they cannot post to slack or receive slack credentials.

<!-- zh-CN:begin 3e434ee0bcf951d7 -->

- 允许子代理协助，但它们不能向 Slack 发帖，也不能获得 Slack 凭据。

<!-- zh-CN:end 3e434ee0bcf951d7 -->
- i want this entire pack committed at `.cursor/automations/benny/` in the target repository. its `SKILL.md` files are direct automation instructions, not registered plugin skills.

<!-- zh-CN:begin b801fa0c7da17f7f -->

- 整个包提交到目标仓库的 `.cursor/automations/benny/`。其中 `SKILL.md` 是直接自动化指令，不是注册插件技能。

<!-- zh-CN:end b801fa0c7da17f7f -->
- i want pstack enabled through the target repository's committed `.cursor/settings.json` only for shared dependencies such as `how`, `why`, `tdd`, `unslop`, and the required principle skills.

<!-- zh-CN:begin dfc2f588949f6778 -->

- 仅通过目标仓库已提交的 `.cursor/settings.json` 启用 pstack，用于 `how`、`why`、`tdd`、`unslop` 和所需原则技能等共享依赖。

<!-- zh-CN:end dfc2f588949f6778 -->
- i want each live automation prompt to read its committed operational file directly. i do not want plugin cache paths, copied excerpts, or slash-skill discovery.

<!-- zh-CN:begin c6311b339d0ec930 -->

- 每个实际自动化提示词直接读取已提交操作文件。不要插件缓存路径、复制摘录或斜杠技能发现。

<!-- zh-CN:end c6311b339d0ec930 -->
- i keep user-owned configuration, feature maps, routing maps, and secrets outside `.cursor/automations/benny/` so pack refreshes cannot overwrite them.

<!-- zh-CN:begin f8ced28737f3387b -->

- 用户拥有的配置、功能地图、路由地图和秘密保留在 `.cursor/automations/benny/` 之外，使包刷新不会覆盖它们。

<!-- zh-CN:end f8ced28737f3387b -->
- i want both automations to fail closed when channel coordinates, tracker access, the control adapter, or the feature map are missing or uncertain.

<!-- zh-CN:begin 89ad70b0f4943bfc -->

- 频道坐标、跟踪器访问、控制适配器或功能地图缺失或不确定时，两个自动化都失败关闭。

<!-- zh-CN:end 89ad70b0f4943bfc -->
- i want draft pull requests only. do not merge or deploy.

<!-- zh-CN:begin f5b48b103a4c75d4 -->

- 只创建草稿拉取请求。不要合并或部署。

<!-- zh-CN:end f5b48b103a4c75d4 -->

### my configuration

<!-- zh-CN:begin 15773e90883d1249 -->

### 我的配置

<!-- zh-CN:end 15773e90883d1249 -->

- source slack channel: `<channel>`

<!-- zh-CN:begin bd39e5049de791da -->

- 来源 Slack 频道：`<channel>`

<!-- zh-CN:end bd39e5049de791da -->
- optional operations channel: `<channel or none>`

<!-- zh-CN:begin 13e4a978392afad6 -->

- 可选运维频道：`<channel or none>`

<!-- zh-CN:end 13e4a978392afad6 -->
- repository and default branch: `<repo>`, `<branch>`

<!-- zh-CN:begin 05fc8cbbd964bf6b -->

- 仓库与默认分支：`<repo>`、`<branch>`

<!-- zh-CN:end 05fc8cbbd964bf6b -->
- tracker: `<type, team, project, labels, intake status>`

<!-- zh-CN:begin 46053ee765a47364 -->

- 跟踪器：`<type, team, project, labels, intake status>`

<!-- zh-CN:end 46053ee765a47364 -->
- routing map: `<path or none>`

<!-- zh-CN:begin 99896111292d6bd9 -->

- 路由地图：`<path or none>`

<!-- zh-CN:end 99896111292d6bd9 -->
- triage identity: `<slack identity>`

<!-- zh-CN:begin 12ebc26a6111cb15 -->

- 分诊身份：`<slack identity>`

<!-- zh-CN:end 12ebc26a6111cb15 -->
- control skill: `<configured skill or adapter>`

<!-- zh-CN:begin 67e848548f8e297d -->

- 控制技能：`<configured skill or adapter>`

<!-- zh-CN:end 67e848548f8e297d -->
- feature map: `<committed same-repo path outside the copied pack, or behavior to paraphrase>`

<!-- zh-CN:begin 31576f7094b7d763 -->

- 功能地图：`<committed same-repo path outside the copied pack, or behavior to paraphrase>`

<!-- zh-CN:end 31576f7094b7d763 -->
- models: `<triage, reproduce, code, media review>`

<!-- zh-CN:begin 55cfab131b0e4593 -->

- 模型：`<triage, reproduce, code, media review>`

<!-- zh-CN:end 55cfab131b0e4593 -->
- status emoji strings: `<seen, reproducing, reproduced, blocked, fixing, failed, pull request opened>`

<!-- zh-CN:begin 34041d263935ce7d -->

- 状态 emoji 字符串：`<seen, reproducing, reproduced, blocked, fixing, failed, pull request opened>`

<!-- zh-CN:end 34041d263935ce7d -->
- budgets: `<polling, verdict wait, follow-up, repro, rejection, fix>`

<!-- zh-CN:begin e82e2b204d093587 -->

- 预算：`<polling, verdict wait, follow-up, repro, rejection, fix>`

<!-- zh-CN:end e82e2b204d093587 -->
- optional bot token capability: `<none, file download, or editable operations status>`

<!-- zh-CN:begin b1b895ada798d426 -->

- 可选机器人令牌能力：`<none, file download, or editable operations status>`

<!-- zh-CN:end b1b895ada798d426 -->

start from [`configuration.example.yaml`](./templates/configuration.example.yaml) and [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md). copy and fill them outside this pack, for example under `.cursor/benny/`. keep secret values in a secret manager or environment.

<!-- zh-CN:begin ba6eed918c02a035 -->

从 [`configuration.example.yaml`](./templates/configuration.example.yaml) 和 [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md) 开始。在包外复制并填写，例如 `.cursor/benny/`。秘密值放在秘密管理器或环境变量中。

<!-- zh-CN:end ba6eed918c02a035 -->

## for the agent

<!-- zh-CN:begin b1cb34a2747c3d48 -->

## 给代理的说明

<!-- zh-CN:end b1cb34a2747c3d48 -->

the human enters setup by pointing cursor at this file. do not look for or invoke a discovered benny slash skill.

<!-- zh-CN:begin 264b613c40e0d166 -->

人类将 Cursor 指向本文件以进入设置。不要寻找或调用已发现的 Benny 斜杠技能。

<!-- zh-CN:end 264b613c40e0d166 -->

1. ask which repository will run the automations.

<!-- zh-CN:begin 0d6bed61a5c1644b -->

1. 询问哪个仓库运行这些自动化。

<!-- zh-CN:end 0d6bed61a5c1644b -->
2. treat the directory containing this `FOR_AGENTS.md` as the source pack.

<!-- zh-CN:begin 31d726bcdf5dbf6c -->

2. 将包含本 `FOR_AGENTS.md` 的目录视为源包。

<!-- zh-CN:end 31d726bcdf5dbf6c -->
3. merge the entire source pack into `<target-repository>/.cursor/automations/benny/`.

<!-- zh-CN:begin c6cfc1e4e40663fd -->

3. 将整个源包合并到 `<target-repository>/.cursor/automations/benny/`。

<!-- zh-CN:end c6cfc1e4e40663fd -->
4. preserve every destination-only file. never delete unrelated files or overwrite user-owned configuration, feature maps, or routing maps.

<!-- zh-CN:begin f7df8c081dd54875 -->

4. 保留目标中独立存在的每个文件。绝不删除无关文件，也不覆盖用户拥有的配置、功能地图或路由地图。

<!-- zh-CN:end f7df8c081dd54875 -->
5. when an existing destination file at a source-managed path differs, review the diff and merge without discarding local edits. if ownership is ambiguous, stop and ask before replacing it.

<!-- zh-CN:begin 6025286e3911a939 -->

5. 源管理路径在目标中已有不同文件时，审查差异并合并且不丢弃本地编辑。所有权不清时停下，替换前询问。

<!-- zh-CN:end 6025286e3911a939 -->
6. verify that the copied `FOR_AGENTS.md` and `skills/setup-benny/SKILL.md` exist in the target repository.

<!-- zh-CN:begin f93b708bbe7bb45b -->

6. 验证复制后的 `FOR_AGENTS.md` 和 `skills/setup-benny/SKILL.md` 存在于目标仓库。

<!-- zh-CN:end f93b708bbe7bb45b -->
7. read and follow `.cursor/automations/benny/skills/setup-benny/SKILL.md` directly from the target repository.

<!-- zh-CN:begin b5d6e905c6c17316 -->

7. 直接从目标仓库读取并遵循 `.cursor/automations/benny/skills/setup-benny/SKILL.md`。

<!-- zh-CN:end b5d6e905c6c17316 -->

i want you to merge this entry into the target repository's `.cursor/settings.json`:

<!-- zh-CN:begin 132fefb24b1212ad -->

将此项合并到目标仓库的 `.cursor/settings.json`：

<!-- zh-CN:end 132fefb24b1212ad -->

```json
{
	"plugins": {
		"pstack": { "enabled": true }
	}
}
```

preserve every unrelated setting and plugin. preserve comments and valid jsonc syntax when the existing file uses jsonc.

<!-- zh-CN:begin f1e9fcd981b0945a -->

保留每个无关设置和插件。现有文件使用 JSONC 时，保留注释和合法 JSONC 语法。

<!-- zh-CN:end f1e9fcd981b0945a -->

i want verification from a fresh agent rooted in the target repository. confirm that pstack's `how`, `why`, `tdd`, `unslop`, and the principle skills used by benny resolve in project scope. do not count skills loaded from the current session or a user-scoped install.

<!-- zh-CN:begin 3b9f68eafd21232e -->

我希望由以目标仓库为根的全新代理验证。确认 pstack 的 `how`、`why`、`tdd`、`unslop` 及 Benny 使用的原则技能在项目作用域可解析。不要把当前会话或用户作用域安装加载的技能算作通过。

<!-- zh-CN:end 3b9f68eafd21232e -->

if project-scoped plugins are unavailable or any shared dependency does not resolve, stop and explain what failed. do not add `.cursor/automations/benny/skills/` to a plugin manifest or expect its files to appear in the slash-skill list.

<!-- zh-CN:begin 3d46b94537c6c45a -->

项目作用域插件不可用或任何共享依赖无法解析时，停止并解释失败。不要把 `.cursor/automations/benny/skills/` 添加到插件清单，也不要期待其文件出现在斜杠技能列表。

<!-- zh-CN:end 3d46b94537c6c45a -->

tell me that `.cursor/settings.json`, `.cursor/automations/benny/`, and any referenced secret-free configuration must be committed before either automation is enabled. do not create or update an automation until i explicitly ask.

<!-- zh-CN:begin 09a9a84af8d3e26f -->

告诉我在启用任一自动化前，必须提交 `.cursor/settings.json`、`.cursor/automations/benny/` 以及任何引用的无秘密配置。用户明确要求前，不要创建或更新自动化。

<!-- zh-CN:end 09a9a84af8d3e26f -->

for first-time creation, use built-in `/automate` once for triage and once for repro and fix. complete the draft review, approval, readiness check, and Automations editor handoff for the first automation before starting the second.

<!-- zh-CN:begin a3189294a82b3aad -->

首次创建时，分别运行一次内置 `/automate` 进行分诊，再进行复现与修复。完成第一个自动化的草稿审查、批准、就绪检查和 Automations 编辑器交接后，再开始第二个。

<!-- zh-CN:end a3189294a82b3aad -->

paraphrase this intent and the finished configuration into each draft. the triage prompt must read and follow `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`. the repro prompt must read and follow `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`. use these repo-relative paths only after `/automate` confirms they are committed in the repository where the automation will run.

<!-- zh-CN:begin a365fa6d8cf3987c -->

将本意图和完成后的配置转述进每份草稿。分诊提示词必须读取并遵循 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`。复现提示词必须读取并遵循 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`。只有 `/automate` 确认它们在自动化运行的仓库中提交后，才使用这些仓库相对路径。

<!-- zh-CN:end a365fa6d8cf3987c -->

for existing automations, do not use `/automate` to inspect or update them. validate the configuration, then use the concise field checklist in the copied setup file so i can edit each automation directly in its editor. do not create duplicates.

<!-- zh-CN:begin dd0b154e1f67c857 -->

对于现有自动化，不要用 `/automate` 检查或更新。验证配置后，使用已复制设置文件中的简洁字段清单，让用户在各自编辑器直接修改。不要创建重复项。

<!-- zh-CN:end dd0b154e1f67c857 -->
