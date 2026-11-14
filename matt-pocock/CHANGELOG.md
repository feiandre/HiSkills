# mattpocock-skills

<!-- zh-CN:begin 09ca8d5d3600e89e -->

# mattpocock-skills 技能集

<!-- zh-CN:end 09ca8d5d3600e89e -->

## 1.3.2

### Patch Changes

<!-- zh-CN:begin bc9e5040c439e63c -->

### 补丁变更

<!-- zh-CN:end bc9e5040c439e63c -->

- [#1194](https://github.com/mattpocock/skills/pull/1194) [`b645f47`](https://github.com/mattpocock/skills/commit/b645f47de3e17ed3bf60586c9bebb8092e0f79fd) Thanks [@mattpocock](https://github.com/mattpocock)! - `ask-matt` now reads a skill's `SKILL.md` before stating what it does or recommending a step be skipped, instead of trusting its own one-line summaries ([#614](https://github.com/mattpocock/skills/issues/614)).

<!-- zh-CN:begin a966aa461df2a5bd -->

- [#1194](https://github.com/mattpocock/skills/pull/1194) [`b645f47`](https://github.com/mattpocock/skills/commit/b645f47de3e17ed3bf60586c9bebb8092e0f79fd) 感谢 [@mattpocock](https://github.com/mattpocock)！- `ask-matt` 现在会先阅读技能的 `SKILL.md`，再说明其作用或建议跳过某个步骤，不再依赖自己的一行摘要（[#614](https://github.com/mattpocock/skills/issues/614)）。

<!-- zh-CN:end a966aa461df2a5bd -->

- [#1304](https://github.com/mattpocock/skills/pull/1304) [`5beb35b`](https://github.com/mattpocock/skills/commit/5beb35b040e3de97e54fa9e386d7e42d15c295c2) Thanks [@mattpocock](https://github.com/mattpocock)! - `chief-of-staff` now keeps its memory in an LLM wiki (an `index.md` plus one page per topic, maintained through ingest, query and lint) and writes it as a historical record: every claim is dated, and every claim about code cites the commit it was true at.

<!-- zh-CN:begin 0f8c2fe37304b30d -->

- [#1304](https://github.com/mattpocock/skills/pull/1304) [`5beb35b`](https://github.com/mattpocock/skills/commit/5beb35b040e3de97e54fa9e386d7e42d15c295c2) 感谢 [@mattpocock](https://github.com/mattpocock)！- `chief-of-staff` 现在把记忆保存在 LLM wiki 中（一个 `index.md` 加上每主题一页，通过摄取、查询和 lint 维护），并将其写为历史记录：每项陈述都有日期，每项关于代码的陈述都引用其成立时的提交。

<!-- zh-CN:end 0f8c2fe37304b30d -->

- [#1208](https://github.com/mattpocock/skills/pull/1208) [`3da8c01`](https://github.com/mattpocock/skills/commit/3da8c01116264675eeefbd6e9d59c734de9095cc) Thanks [@mattpocock](https://github.com/mattpocock)! - `code-review` now searches the repo for standards files and always hands `CODING_STANDARDS.md` / `CONTRIBUTING.md` to the Standards sub-agent ([#1065](https://github.com/mattpocock/skills/issues/1065)), runs both sub-agents in the foreground and uses their returned reports ([#1073](https://github.com/mattpocock/skills/issues/1073)), and resolves the issue tracker through the provided tracker doc instead of a hard-coded path ([#937](https://github.com/mattpocock/skills/issues/937)).

<!-- zh-CN:begin 14c8d4ca955443d1 -->

- [#1208](https://github.com/mattpocock/skills/pull/1208) [`3da8c01`](https://github.com/mattpocock/skills/commit/3da8c01116264675eeefbd6e9d59c734de9095cc) 感谢 [@mattpocock](https://github.com/mattpocock)！- `code-review` 现在会搜索仓库中的标准文件，并始终把 `CODING_STANDARDS.md` / `CONTRIBUTING.md` 交给标准子智能体（[#1065](https://github.com/mattpocock/skills/issues/1065)），在前台运行两个子智能体并使用返回的报告（[#1073](https://github.com/mattpocock/skills/issues/1073)），并通过提供的跟踪器文档解析问题跟踪器，而不再使用硬编码路径（[#937](https://github.com/mattpocock/skills/issues/937)）。

<!-- zh-CN:end 14c8d4ca955443d1 -->

- [#1209](https://github.com/mattpocock/skills/pull/1209) [`f3fc563`](https://github.com/mattpocock/skills/commit/f3fc5632f401156837ee3872f14fe33ccf1024ea) Thanks [@mattpocock](https://github.com/mattpocock)! - `diagnosing-bugs` Phase 5 now has the agent `diff` a forced mutation against a pristine copy before trusting the red, so an edit that silently changed nothing can't pass as a failing test ([#955](https://github.com/mattpocock/skills/issues/955)).

<!-- zh-CN:begin 802e2f4f83316a78 -->

- [#1209](https://github.com/mattpocock/skills/pull/1209) [`f3fc563`](https://github.com/mattpocock/skills/commit/f3fc5632f401156837ee3872f14fe33ccf1024ea) 感谢 [@mattpocock](https://github.com/mattpocock)！- `diagnosing-bugs` 的第 5 阶段现在要求智能体在相信红色结果之前，将强制变异与原始副本进行 `diff`，以免悄悄没有改变任何内容的编辑被当作失败测试（[#955](https://github.com/mattpocock/skills/issues/955)）。

<!-- zh-CN:end 802e2f4f83316a78 -->

- [#1187](https://github.com/mattpocock/skills/pull/1187) [`e0efb6e`](https://github.com/mattpocock/skills/commit/e0efb6e7435ebb420d8a25d6816ed1ebaa2d23d2) Thanks [@mattpocock](https://github.com/mattpocock)! - Fixed the GitHub tracker template's external-PR listing, which failed on `authorAssociation` ([#468](https://github.com/mattpocock/skills/issues/468), thanks @lofi-coding). Re-run `/setup-matt-pocock-skills` to refresh `docs/agents/issue-tracker.md`.

<!-- zh-CN:begin 060bcc4785764734 -->

- [#1187](https://github.com/mattpocock/skills/pull/1187) [`e0efb6e`](https://github.com/mattpocock/skills/commit/e0efb6e7435ebb420d8a25d6816ed1ebaa2d23d2) 感谢 [@mattpocock](https://github.com/mattpocock)！- 修复了 GitHub 跟踪器模板的外部 PR 列表，该功能此前会因 `authorAssociation` 失败（[#468](https://github.com/mattpocock/skills/issues/468)，感谢 @lofi-coding）。重新运行 `/setup-matt-pocock-skills` 以刷新 `docs/agents/issue-tracker.md`。

<!-- zh-CN:end 060bcc4785764734 -->

- [#1169](https://github.com/mattpocock/skills/pull/1169) [`59db609`](https://github.com/mattpocock/skills/commit/59db609eb1e18aaf59b63284d0e52255aff0c63c) Thanks [@mattpocock](https://github.com/mattpocock)! - The GitHub issue tracker template that `setup-matt-pocock-skills` writes now tells agents to file issues only into the user's own repo, never into `mattpocock/skills`, and to check the target repo before the first `gh issue create`. Agents working in a clone or fork of this repo had filed their specs and tickets here ([#541](https://github.com/mattpocock/skills/issues/541) to [#550](https://github.com/mattpocock/skills/issues/550)).

<!-- zh-CN:begin bee22cf68d26e86c -->

- [#1169](https://github.com/mattpocock/skills/pull/1169) [`59db609`](https://github.com/mattpocock/skills/commit/59db609eb1e18aaf59b63284d0e52255aff0c63c) 感谢 [@mattpocock](https://github.com/mattpocock)！- `setup-matt-pocock-skills` 写出的 GitHub 问题跟踪器模板现在要求智能体只把问题提交到用户自己的仓库，绝不提交到 `mattpocock/skills`，并在第一次 `gh issue create` 之前检查目标仓库。此前，在本仓库的克隆或分支中工作的智能体会将规格和工单提交到这里（[#541](https://github.com/mattpocock/skills/issues/541) 至 [#550](https://github.com/mattpocock/skills/issues/550)）。

<!-- zh-CN:end bee22cf68d26e86c -->

- [#1193](https://github.com/mattpocock/skills/pull/1193) [`95249b0`](https://github.com/mattpocock/skills/commit/95249b0b49782349740fd9b8c6ce32b4e59e497a) Thanks [@mattpocock](https://github.com/mattpocock)! - `grilling` words each question so "yes" accepts the recommended answer, so agreeing never means answering "no" ([#706](https://github.com/mattpocock/skills/issues/706)).

<!-- zh-CN:begin 0b4a2195b42074a6 -->

- [#1193](https://github.com/mattpocock/skills/pull/1193) [`95249b0`](https://github.com/mattpocock/skills/commit/95249b0b49782349740fd9b8c6ce32b4e59e497a) 感谢 [@mattpocock](https://github.com/mattpocock)！- `grilling` 调整每个问题的措辞，使“是”接受推荐答案，因此同意永远不会意味着回答“否”（[#706](https://github.com/mattpocock/skills/issues/706)）。

<!-- zh-CN:end 0b4a2195b42074a6 -->

- [#1184](https://github.com/mattpocock/skills/pull/1184) [`4f4e943`](https://github.com/mattpocock/skills/commit/4f4e9433bbb7c4957ef33b1ea26686fb7c2a4cf4) Thanks [@mattpocock](https://github.com/mattpocock)! - `handoff` now names where the OS temp directory is (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows), so agents stop guessing ([#272](https://github.com/mattpocock/skills/issues/272)).

<!-- zh-CN:begin fd1b9e6a9c7d22dc -->

- [#1184](https://github.com/mattpocock/skills/pull/1184) [`4f4e943`](https://github.com/mattpocock/skills/commit/4f4e9433bbb7c4957ef33b1ea26686fb7c2a4cf4) 感谢 [@mattpocock](https://github.com/mattpocock)！- `handoff` 现在会说明操作系统临时目录在哪里（`$TMPDIR`，否则为 `/tmp`；Windows 上为 `%TEMP%`），让智能体不再猜测（[#272](https://github.com/mattpocock/skills/issues/272)）。

<!-- zh-CN:end fd1b9e6a9c7d22dc -->

- [#1189](https://github.com/mattpocock/skills/pull/1189) [`e48341a`](https://github.com/mattpocock/skills/commit/e48341a3d412cfeba4b9a79d3fd0331fc376ba82) Thanks [@mattpocock](https://github.com/mattpocock)! - `implement` now calls the Skill tool for `tdd` and `code-review` instead of bare `/skill` prose, matching [#878](https://github.com/mattpocock/skills/issues/878).

<!-- zh-CN:begin 63efe7b040c97a85 -->

- [#1189](https://github.com/mattpocock/skills/pull/1189) [`e48341a`](https://github.com/mattpocock/skills/commit/e48341a3d412cfeba4b9a79d3fd0331fc376ba82) 感谢 [@mattpocock](https://github.com/mattpocock)！- `implement` 现在为 `tdd` 和 `code-review` 调用 Skill 工具，而不再使用裸 `/skill` 文字说明，符合 [#878](https://github.com/mattpocock/skills/issues/878)。

<!-- zh-CN:end 63efe7b040c97a85 -->

- [#1196](https://github.com/mattpocock/skills/pull/1196) [`6d6a5b9`](https://github.com/mattpocock/skills/commit/6d6a5b9072f47ee7ba1d972d8ce0ee98b7ed4394) Thanks [@mattpocock](https://github.com/mattpocock)! - `implement` fetches a passed ticket reference from the issue tracker and states its title before starting, asking when the reference is ambiguous ([#700](https://github.com/mattpocock/skills/issues/700)).

<!-- zh-CN:begin c9b1f46cb5f75492 -->

- [#1196](https://github.com/mattpocock/skills/pull/1196) [`6d6a5b9`](https://github.com/mattpocock/skills/commit/6d6a5b9072f47ee7ba1d972d8ce0ee98b7ed4394) 感谢 [@mattpocock](https://github.com/mattpocock)！- `implement` 会从问题跟踪器获取传入的工单引用，并在开始前说明其标题；引用不明确时会询问（[#700](https://github.com/mattpocock/skills/issues/700)）。

<!-- zh-CN:end c9b1f46cb5f75492 -->

- [#1228](https://github.com/mattpocock/skills/pull/1228) [`ed0de59`](https://github.com/mattpocock/skills/commit/ed0de59eb5de8c2730a650cc69f588ffa64c1040) Thanks [@mattpocock](https://github.com/mattpocock)! - `setup-matt-pocock-skills` now wires up a git remote before writing a GitHub/GitLab tracker that nothing can reach ([#1201](https://github.com/mattpocock/skills/issues/1201)), and offers to `git mv` a legacy `CONTEXT.md` / `CONTEXT-MAP.md` to its `GLOSSARY` name ([#1176](https://github.com/mattpocock/skills/issues/1176)). The GitHub template comments before closing ([#873](https://github.com/mattpocock/skills/issues/873)), reads a PR's body as well as its comments ([#1138](https://github.com/mattpocock/skills/issues/1138)), moves **Blocking** into Conventions with the native `gh` flags ([#855](https://github.com/mattpocock/skills/issues/855)), and names the command that counts open blockers ([#1118](https://github.com/mattpocock/skills/issues/1118)). The GitLab template lists MRs with `-O json` and names the frontier query's command ([#1143](https://github.com/mattpocock/skills/issues/1143)). Re-run `/setup-matt-pocock-skills` to refresh `docs/agents/`.

<!-- zh-CN:begin ee77e4ecdd314d94 -->

- [#1228](https://github.com/mattpocock/skills/pull/1228) [`ed0de59`](https://github.com/mattpocock/skills/commit/ed0de59eb5de8c2730a650cc69f588ffa64c1040) 感谢 [@mattpocock](https://github.com/mattpocock)！- `setup-matt-pocock-skills` 现在会先配置 Git 远程仓库，再写入无法连接任何内容的 GitHub/GitLab 跟踪器（[#1201](https://github.com/mattpocock/skills/issues/1201)），并主动提出用 `git mv` 将旧版 `CONTEXT.md` / `CONTEXT-MAP.md` 改名成其 `GLOSSARY` 名称（[#1176](https://github.com/mattpocock/skills/issues/1176)）。GitHub 模板会在结束时评论（[#873](https://github.com/mattpocock/skills/issues/873)），同时读取 PR 正文及其评论（[#1138](https://github.com/mattpocock/skills/issues/1138)），使用原生 `gh` 标志把 **Blocking** 移至 Conventions（[#855](https://github.com/mattpocock/skills/issues/855)），并说明统计未关闭阻塞项的命令（[#1118](https://github.com/mattpocock/skills/issues/1118)）。GitLab 模板用 `-O json` 列出 MR，并说明前沿查询的命令（[#1143](https://github.com/mattpocock/skills/issues/1143)）。重新运行 `/setup-matt-pocock-skills` 以刷新 `docs/agents/`。

<!-- zh-CN:end ee77e4ecdd314d94 -->

- [#1197](https://github.com/mattpocock/skills/pull/1197) [`5b7cade`](https://github.com/mattpocock/skills/commit/5b7cade4d68947f34dae71326a0ce89f09e22c9c) Thanks [@mattpocock](https://github.com/mattpocock)! - `setup-matt-pocock-skills` now creates missing triage labels on GitHub/GitLab ([#616](https://github.com/mattpocock/skills/issues/616)), fixes the GitLab template's `glab` commands ([#635](https://github.com/mattpocock/skills/issues/635)), reads GitHub issues with `--json` so labels and body come through ([#733](https://github.com/mattpocock/skills/issues/733)), and names the "Label in our tracker" column in `triage-labels.md` ([#801](https://github.com/mattpocock/skills/issues/801)). Re-run `/setup-matt-pocock-skills` to refresh `docs/agents/`.

<!-- zh-CN:begin 753c92ca6185605a -->

- [#1197](https://github.com/mattpocock/skills/pull/1197) [`5b7cade`](https://github.com/mattpocock/skills/commit/5b7cade4d68947f34dae71326a0ce89f09e22c9c) 感谢 [@mattpocock](https://github.com/mattpocock)！- `setup-matt-pocock-skills` 现在会在 GitHub/GitLab 上创建缺失的分诊标签（[#616](https://github.com/mattpocock/skills/issues/616)），修复 GitLab 模板中的 `glab` 命令（[#635](https://github.com/mattpocock/skills/issues/635)），用 `--json` 读取 GitHub 问题，以便获取标签和正文（[#733](https://github.com/mattpocock/skills/issues/733)），并在 `triage-labels.md` 中说明“我们跟踪器中的标签”列（[#801](https://github.com/mattpocock/skills/issues/801)）。重新运行 `/setup-matt-pocock-skills` 以刷新 `docs/agents/`。

<!-- zh-CN:end 753c92ca6185605a -->

- [#1341](https://github.com/mattpocock/skills/pull/1341) [`7739eae`](https://github.com/mattpocock/skills/commit/7739eaed7f8f3915437a8def198a6d0d7206dbc7) Thanks [@mattpocock](https://github.com/mattpocock)! - Skills that dispatch subagents (`implement-spec`, `code-review`, `codebase-design`, `improve-codebase-architecture`, `wayfinder`, `research`, `grilling`, `chief-of-staff`) now say to start each one with a fresh context window rather than forking the current conversation, which some harnesses (Codex) do by default and which throws away the clean context a subagent exists for.

<!-- zh-CN:begin c6324b3ad08d28dc -->

- [#1341](https://github.com/mattpocock/skills/pull/1341) [`7739eae`](https://github.com/mattpocock/skills/commit/7739eaed7f8f3915437a8def198a6d0d7206dbc7) 感谢 [@mattpocock](https://github.com/mattpocock)！- 会派发子智能体的技能（`implement-spec`、`code-review`、`codebase-design`、`improve-codebase-architecture`、`wayfinder`、`research`、`grilling`、`chief-of-staff`）现在要求每个子智能体都使用全新上下文窗口启动，而不分叉当前对话；有些宿主（Codex）默认采用分叉，这会丢弃子智能体本应拥有的干净上下文。

<!-- zh-CN:end c6324b3ad08d28dc -->

- [#1192](https://github.com/mattpocock/skills/pull/1192) [`3f59913`](https://github.com/mattpocock/skills/commit/3f599139104dfceabc7754eeb91319802f85e042) Thanks [@mattpocock](https://github.com/mattpocock)! - `tdd` now gives each proposed seam a one-line note on what it catches and what it misses, so choosing between seams is no longer a guess ([#607](https://github.com/mattpocock/skills/issues/607)).

<!-- zh-CN:begin 71ba6cc02727b723 -->

- [#1192](https://github.com/mattpocock/skills/pull/1192) [`3f59913`](https://github.com/mattpocock/skills/commit/3f599139104dfceabc7754eeb91319802f85e042) 感谢 [@mattpocock](https://github.com/mattpocock)！- `tdd` 现在会为每个建议的接缝写一行说明，指出它能捕获和遗漏什么，因此在接缝之间选择不再靠猜（[#607](https://github.com/mattpocock/skills/issues/607)）。

<!-- zh-CN:end 71ba6cc02727b723 -->

- [#1183](https://github.com/mattpocock/skills/pull/1183) [`ad5400b`](https://github.com/mattpocock/skills/commit/ad5400b930b297b0c0cb231ff1ffe42a7da666aa) Thanks [@mattpocock](https://github.com/mattpocock)! - `teach` quizzes vary which position holds the correct answer ([#611](https://github.com/mattpocock/skills/issues/611)).

<!-- zh-CN:begin 5a42a989c642cd0b -->

- [#1183](https://github.com/mattpocock/skills/pull/1183) [`ad5400b`](https://github.com/mattpocock/skills/commit/ad5400b930b297b0c0cb231ff1ffe42a7da666aa) 感谢 [@mattpocock](https://github.com/mattpocock)！- `teach` 测验会变化正确答案所在的位置（[#611](https://github.com/mattpocock/skills/issues/611)）。

<!-- zh-CN:end 5a42a989c642cd0b -->

- [#1183](https://github.com/mattpocock/skills/pull/1183) [`ad5400b`](https://github.com/mattpocock/skills/commit/ad5400b930b297b0c0cb231ff1ffe42a7da666aa) Thanks [@mattpocock](https://github.com/mattpocock)! - `teach` writes its workspace to the directory you ran it in, not the skill folder ([#377](https://github.com/mattpocock/skills/issues/377)).

<!-- zh-CN:begin f6af41db94adae8e -->

- [#1183](https://github.com/mattpocock/skills/pull/1183) [`ad5400b`](https://github.com/mattpocock/skills/commit/ad5400b930b297b0c0cb231ff1ffe42a7da666aa) 感谢 [@mattpocock](https://github.com/mattpocock)！- `teach` 会把工作区写入你运行它的目录，而不是技能文件夹（[#377](https://github.com/mattpocock/skills/issues/377)）。

<!-- zh-CN:end f6af41db94adae8e -->

- [#1188](https://github.com/mattpocock/skills/pull/1188) [`cffab50`](https://github.com/mattpocock/skills/commit/cffab50350e3d96688f63f890f4d7ca0e6007cfe) Thanks [@mattpocock](https://github.com/mattpocock)! - `to-tickets` makes each ticket a sub-issue of its source issue (the GitHub tracker template now gives the command), and omits `## Blocked by` when blockers are native edges. Re-run `/setup-matt-pocock-skills` to refresh `docs/agents/issue-tracker.md`. Thanks @richardwhatever ([#554](https://github.com/mattpocock/skills/issues/554)) and @adamslowe ([#262](https://github.com/mattpocock/skills/issues/262)).

<!-- zh-CN:begin 157d5a494eb1afd8 -->

- [#1188](https://github.com/mattpocock/skills/pull/1188) [`cffab50`](https://github.com/mattpocock/skills/commit/cffab50350e3d96688f63f890f4d7ca0e6007cfe) 感谢 [@mattpocock](https://github.com/mattpocock)！- `to-tickets` 会把每个工单设为其源问题的子问题（GitHub 跟踪器模板现在提供命令），并在阻塞项为原生边时省略 `## Blocked by`。重新运行 `/setup-matt-pocock-skills` 以刷新 `docs/agents/issue-tracker.md`。感谢 @richardwhatever（[#554](https://github.com/mattpocock/skills/issues/554)）和 @adamslowe（[#262](https://github.com/mattpocock/skills/issues/262)）。

<!-- zh-CN:end 157d5a494eb1afd8 -->

- [#1181](https://github.com/mattpocock/skills/pull/1181) [`8295b8e`](https://github.com/mattpocock/skills/commit/8295b8e10d4cdb6cce772a56dda7b7c37075074d) Thanks [@mattpocock](https://github.com/mattpocock)! - `wayfinder` no longer labels maps or tickets `ready-for-agent` ([#518](https://github.com/mattpocock/skills/issues/518)), writes cross-references only with real issue ids ([#507](https://github.com/mattpocock/skills/issues/507)), opens no PR from research branches ([#576](https://github.com/mattpocock/skills/issues/576)), and resolves each ticket as the type its label names ([#625](https://github.com/mattpocock/skills/issues/625)). Thanks @jcwayne, @baob, @rynz and @sponge-b0b.

<!-- zh-CN:begin 1fb321d1ffe19adb -->

- [#1181](https://github.com/mattpocock/skills/pull/1181) [`8295b8e`](https://github.com/mattpocock/skills/commit/8295b8e10d4cdb6cce772a56dda7b7c37075074d) 感谢 [@mattpocock](https://github.com/mattpocock)！- `wayfinder` 不再把地图或工单标为 `ready-for-agent`（[#518](https://github.com/mattpocock/skills/issues/518)），只使用真实问题 ID 编写交叉引用（[#507](https://github.com/mattpocock/skills/issues/507)），不从研究分支创建 PR（[#576](https://github.com/mattpocock/skills/issues/576)），并按标签所命名的类型解决每个工单（[#625](https://github.com/mattpocock/skills/issues/625)）。感谢 @jcwayne、@baob、@rynz 和 @sponge-b0b。

<!-- zh-CN:end 1fb321d1ffe19adb -->

- [#1237](https://github.com/mattpocock/skills/pull/1237) [`49dd158`](https://github.com/mattpocock/skills/commit/49dd158d1076134a641b33efb035946536778336) Thanks [@mattpocock](https://github.com/mattpocock)! - `wizard` template fixes: `_existing` decodes a double-quoted `.env` value, so Enter-keeps-current no longer stores the quotes ([#1220](https://github.com/mattpocock/skills/issues/1220)); stages run inside `run_wizard`, so editing the script mid-run can't kill it ([#1142](https://github.com/mattpocock/skills/issues/1142)); `_clear` falls back to ANSI when `tput clear` fails ([#1081](https://github.com/mattpocock/skills/issues/1081)); `write_env` sets the shell variable too ([#1041](https://github.com/mattpocock/skills/issues/1041)); drop the unused `RED` ([#1003](https://github.com/mattpocock/skills/issues/1003)).

<!-- zh-CN:begin a841b0a63b204880 -->

- [#1237](https://github.com/mattpocock/skills/pull/1237) [`49dd158`](https://github.com/mattpocock/skills/commit/49dd158d1076134a641b33efb035946536778336) 感谢 [@mattpocock](https://github.com/mattpocock)！- `wizard` 模板修复：`_existing` 会解码双引号包裹的 `.env` 值，因此按 Enter 保留当前值不再存储引号（[#1220](https://github.com/mattpocock/skills/issues/1220)）；各阶段在 `run_wizard` 内运行，因此运行期间编辑脚本不会杀死进程（[#1142](https://github.com/mattpocock/skills/issues/1142)）；`_clear` 在 `tput clear` 失败时回退到 ANSI（[#1081](https://github.com/mattpocock/skills/issues/1081)）；`write_env` 也会设置 shell 变量（[#1041](https://github.com/mattpocock/skills/issues/1041)）；移除未使用的 `RED`（[#1003](https://github.com/mattpocock/skills/issues/1003)）。

<!-- zh-CN:end a841b0a63b204880 -->

- [#1198](https://github.com/mattpocock/skills/pull/1198) [`868c4cf`](https://github.com/mattpocock/skills/commit/868c4cf20cb7e08bc805c388ff1f305dbedd261a) Thanks [@mattpocock](https://github.com/mattpocock)! - `wizard` template fixes: `ask` uses Readline so arrow keys move the cursor ([#741](https://github.com/mattpocock/skills/issues/741)); `write_env` single-quotes values so spaces, `#`, `$` and quotes survive `source` and dotenv ([#770](https://github.com/mattpocock/skills/issues/770)); `open_url` prints the open-it-yourself warning when no browser opener exists ([#774](https://github.com/mattpocock/skills/issues/774)); `write_env` writes through a symlinked `.env` and keeps an existing file's mode ([#811](https://github.com/mattpocock/skills/issues/811)); `ask` and `ask_secret` fail at EOF instead of looping ([#852](https://github.com/mattpocock/skills/issues/852)).

<!-- zh-CN:begin feecce67c6616cfe -->

- [#1198](https://github.com/mattpocock/skills/pull/1198) [`868c4cf`](https://github.com/mattpocock/skills/commit/868c4cf20cb7e08bc805c388ff1f305dbedd261a) 感谢 [@mattpocock](https://github.com/mattpocock)！- `wizard` 模板修复：`ask` 使用 Readline，因此方向键可移动光标（[#741](https://github.com/mattpocock/skills/issues/741)）；`write_env` 用单引号包裹值，使空格、`#`、`$` 和引号能通过 `source` 与 dotenv（[#770](https://github.com/mattpocock/skills/issues/770)）；`open_url` 在没有浏览器打开器时打印自行打开的警告（[#774](https://github.com/mattpocock/skills/issues/774)）；`write_env` 会经由符号链接的 `.env` 写入，并保留现有文件模式（[#811](https://github.com/mattpocock/skills/issues/811)）；`ask` 和 `ask_secret` 在 EOF 时失败，而不是循环（[#852](https://github.com/mattpocock/skills/issues/852)）。

<!-- zh-CN:end feecce67c6616cfe -->

## 1.3.1

### Patch Changes

<!-- zh-CN:begin 59f0e6fadc6eddb8 -->

### 补丁变更

<!-- zh-CN:end 59f0e6fadc6eddb8 -->

- [#1121](https://github.com/mattpocock/skills/pull/1121) [`c5b9869`](https://github.com/mattpocock/skills/commit/c5b98691982c4f0d3a5e40ab09566b3b84721e00) Thanks [@mattpocock](https://github.com/mattpocock)! - `ask-matt` no longer says `diagnosing-bugs` hands off to `improve-codebase-architecture` from a post-mortem; that step was removed. It now points you at `/retro` once the fix is in, to ask what would have prevented the bug, and at `/improve-codebase-architecture` where the finding is a missing seam. The `diagnosing-bugs` docs page drops the same stale hand-off. Thanks @Ygilany for spotting it ([#1117](https://github.com/mattpocock/skills/issues/1117)).

<!-- zh-CN:begin d999f61b18252ba1 -->

- [#1121](https://github.com/mattpocock/skills/pull/1121) [`c5b9869`](https://github.com/mattpocock/skills/commit/c5b98691982c4f0d3a5e40ab09566b3b84721e00) 感谢 [@mattpocock](https://github.com/mattpocock)！- `ask-matt` 不再说 `diagnosing-bugs` 会在事后复盘中移交给 `improve-codebase-architecture`；该步骤已移除。修复落地后，它现在会指向 `/retro`，询问什么本可以防止该缺陷；若发现缺少接缝，则指向 `/improve-codebase-architecture`。`diagnosing-bugs` 文档页也移除了同样过时的移交说明。感谢 @Ygilany 发现此问题（[#1117](https://github.com/mattpocock/skills/issues/1117)）。

<!-- zh-CN:end d999f61b18252ba1 -->

## 1.3.0

### Minor Changes

<!-- zh-CN:begin f120d46628bbdd2d -->

### 次要变更

<!-- zh-CN:end f120d46628bbdd2d -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate **`implement-spec`** into the **Engineering** bucket, so it ships in the Claude Code plugin, gets a docs page, and is routed by `ask-matt` as the parallel alternative to per-ticket `implement`.

<!-- zh-CN:begin a86bfd33cdc39284 -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) 感谢 [@mattpocock](https://github.com/mattpocock)！- 将 **`implement-spec`** 提升到 **工程** 类别，因此它随 Claude Code 插件发布、获得文档页，并由 `ask-matt` 作为逐工单 `implement` 的并行替代方案进行路由。

<!-- zh-CN:end a86bfd33cdc39284 -->

  `implement-spec` (user-invoked) implements a whole spec in one run. It reads the tickets as a **task graph**, runs implementer subagents in their own worktrees across the ready **frontier**, and lands everything on one **integration branch**, closing out with `code-review`. Ahead of graduating:

  <!-- zh-CN:begin 9ed6bf61424f5f2e -->

  `implement-spec`（由用户调用）在一次运行中实现整个规格。它把工单读取为**任务图**，在就绪**前沿**中让实现子智能体各自在自己的工作树中运行，并将所有内容落到一个**集成分支**，最后以 `code-review` 收尾。提升前：

  <!-- zh-CN:end 9ed6bf61424f5f2e -->

  - The goal is now the integration branch, not a PR. A draft PR opens only when the issue tracker closes work through PRs or you ask for one, and only after the first merge (a branch with no commits ahead of main can't open one). Without a PR, the tickets are resolved the way the tracker closes work.

  <!-- zh-CN:begin 82101c2619543493 -->

  - 目标现在是集成分支，而不是 PR。只有当问题跟踪器以 PR 结束工作，或你主动要求时，才创建草稿 PR，而且必须在首次合并后创建（相对 main 没有新增提交的分支无法创建 PR）。没有 PR 时，工单按跟踪器结束工作的方式解决。

  <!-- zh-CN:end 82101c2619543493 -->
  - It points at the issue tracker like its siblings, telling you to run `/setup-matt-pocock-skills` when none has been provided, rather than silently defaulting to `gh`.

  <!-- zh-CN:begin 4e353a3c8a185ebf -->

  - 像其他同类技能一样指向问题跟踪器；未提供跟踪器时要求运行 `/setup-matt-pocock-skills`，而不是静默默认使用 `gh`。

  <!-- zh-CN:end 4e353a3c8a185ebf -->
  - Each implementer confirms its worktree is based on the integration branch, builds its ticket with `tdd`, and merges the integration tip into its own branch before reporting done, so each merge is a fast-forward.

  <!-- zh-CN:begin cb17595190c4c6e8 -->

  - 每位实现者确认工作树基于集成分支，用 `tdd` 构建自己的工单，并在报告完成前把集成分支最新提交合并到自身分支，使每次合并都是快进。

  <!-- zh-CN:end cb17595190c4c6e8 -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate **`pr`** into the **Engineering** bucket, so it ships in the Claude Code plugin, gets a docs page, and is routed by `ask-matt` as the PR-body close-out.

<!-- zh-CN:begin fccc4b999ae05478 -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) 感谢 [@mattpocock](https://github.com/mattpocock)！——将 **`pr`** 晋升到 **Engineering** 分类，使其随 Claude Code 插件发布、拥有文档页，并由 `ask-matt` 作为 PR 正文收尾流程路由。

<!-- zh-CN:end fccc4b999ae05478 -->

  `pr` (model-invoked) is the shape a pull request body should take: a summary as the smallest visual that makes the change clear (pseudocode, a call tree, a file tree, Mermaid, a diff), before/after evidence that it works, and a merge-danger call (one-way or two-way door, plus blast radius). The Summary visuals are adapted from Dex Horthy's `show-me`, credited in the skill's `CREDITS.md`.

  <!-- zh-CN:begin f1a41ac2fbe871c1 -->

`pr`（模型调用）规定拉取请求正文的形态：用能清楚说明变更的最小可视化作摘要（伪代码、调用树、文件树、Mermaid、差异），提供前后对照证明，并判断合并风险（单向门或双向门，以及影响半径）。摘要可视化改编自 Dex Horthy 的 `show-me`，署名见技能的 `CREDITS.md`。

  <!-- zh-CN:end f1a41ac2fbe871c1 -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate **`retro`** into the **Engineering** bucket, so it ships in the Claude Code plugin, gets a docs page, and is routed by `ask-matt` as the last step of the main flow, after `code-review`.

<!-- zh-CN:begin 07369e00ae464aed -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) 感谢 [@mattpocock](https://github.com/mattpocock)！——将 **`retro`** 晋升到 **Engineering** 分类，使其随 Claude Code 插件发布、拥有文档页，并由 `ask-matt` 作为 `code-review` 之后主流程最后一步路由。

<!-- zh-CN:end 07369e00ae464aed -->

  `retro` (user-invoked) looks back at a coding session and suggests changes to the agent's environment rather than the code: navigation pointers, automated checks, coding standards, steering files, tool economy, information access. It classifies each coding-standards finding first: a mechanical violation gets a deterministic check (a linter rule, a pre-commit hook, or a CI job), and `CODING_STANDARDS.md` is kept for genuine judgement calls. A repo with no guardrail at all is a finding in its own right.

  <!-- zh-CN:begin ee20031cf50358ec -->

`retro`（用户调用）回顾编码会话，建议改变代理环境而非代码：导航指针、自动检查、编码标准、引导文件、工具经济性、信息访问。它先分类每条编码标准发现：机械违规使用确定性检查（linter 规则、pre-commit hook 或 CI 作业），`CODING_STANDARDS.md` 留给真正需要判断的情况。完全没有任何护栏的仓库本身就是一条发现。

  <!-- zh-CN:end ee20031cf50358ec -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`daa01d8`](https://github.com/mattpocock/skills/commit/daa01d8aa68ad5c61b68970ec2018d0ce9567be6) Thanks [@mattpocock](https://github.com/mattpocock)! - Remove the **`resolving-merge-conflicts`** skill. It's no longer needed, and nothing replaces it: the agent works through an in-progress merge or rebase conflict without a dedicated skill. It leaves the Claude Code plugin, the README and the `ask-matt` router. Its docs page at `https://aihero.dev/skills-resolving-merge-conflicts` stays up, marked archived.

<!-- zh-CN:begin 6ee0d1f2b8257745 -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`daa01d8`](https://github.com/mattpocock/skills/commit/daa01d8aa68ad5c61b68970ec2018d0ce9567be6) 感谢 [@mattpocock](https://github.com/mattpocock)！——移除 **`resolving-merge-conflicts`** 技能。它已不再需要，也没有替代品：代理不使用专用技能即可处理进行中的合并或变基冲突。它退出 Claude Code 插件、README 和 `ask-matt` 路由。位于 `https://aihero.dev/skills-resolving-merge-conflicts` 的文档页保留并标为已归档。

<!-- zh-CN:end 6ee0d1f2b8257745 -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`006a52b`](https://github.com/mattpocock/skills/commit/006a52be23e0178375e083e30535fa8224471f3e) Thanks [@mattpocock](https://github.com/mattpocock)! - Rename the `CONTEXT.md`/`CONTEXT-MAP.md` domain-doc convention to `GLOSSARY.md`/`GLOSSARY-MAP.md` everywhere the skills read and write it (`domain-modeling`, `grill-with-docs`, `improve-codebase-architecture`, `setup-matt-pocock-skills`, `triage`, `tdd`, `diagnosing-bugs`, `ask-matt`, `codebase-design`, `wait-what`, `pr`), plus the docs pages and this repo's own root glossary.

<!-- zh-CN:begin ec7798177908e373 -->

- [#1120](https://github.com/mattpocock/skills/pull/1120) [`006a52b`](https://github.com/mattpocock/skills/commit/006a52be23e0178375e083e30535fa8224471f3e) 感谢 [@mattpocock](https://github.com/mattpocock)！——在所有技能读写领域文档的位置，将 `CONTEXT.md`／`CONTEXT-MAP.md` 约定更名为 `GLOSSARY.md`／`GLOSSARY-MAP.md`（涉及 `domain-modeling`、`grill-with-docs`、`improve-codebase-architecture`、`setup-matt-pocock-skills`、`triage`、`tdd`、`diagnosing-bugs`、`ask-matt`、`codebase-design`、`wait-what`、`pr`），并更新文档页及本仓库根词汇表。

<!-- zh-CN:end ec7798177908e373 -->

  If you have an existing `CONTEXT.md` (or `CONTEXT-MAP.md`) from before this change, `git mv` it to the new name: the skills only look for `GLOSSARY.md`/`GLOSSARY-MAP.md` going forward.

  <!-- zh-CN:begin f2e71d934862d928 -->

如果已有此变更之前创建的 `CONTEXT.md`（或 `CONTEXT-MAP.md`），用 `git mv` 改为新名称：技能以后只查找 `GLOSSARY.md`／`GLOSSARY-MAP.md`。

  <!-- zh-CN:end f2e71d934862d928 -->

### Patch Changes

<!-- zh-CN:begin b4453054bd31c796 -->

### 补丁变更

<!-- zh-CN:end b4453054bd31c796 -->

- [#848](https://github.com/mattpocock/skills/pull/848) [`f02e2ed`](https://github.com/mattpocock/skills/commit/f02e2ed3624d031272f8547742d23bf6bca8b072) Thanks [@mattpocock](https://github.com/mattpocock)! - domain-modeling: trigger on discussing codebase terminology and on writing or editing a GLOSSARY.md or an ADR directly, replacing the narrower "pin down domain terminology or a ubiquitous language" / "record an architectural decision" phrasing. Also drops the "another skill needs to maintain the domain model" caveat, since that's the invoking skill's job to state explicitly, not this description's.

<!-- zh-CN:begin 8152a6579cd92558 -->

- [#848](https://github.com/mattpocock/skills/pull/848) [`f02e2ed`](https://github.com/mattpocock/skills/commit/f02e2ed3624d031272f8547742d23bf6bca8b072) 感谢 [@mattpocock](https://github.com/mattpocock)！——domain-modeling：在讨论代码库术语，或直接编写、编辑 GLOSSARY.md 或 ADR 时触发，替换较窄的“确定领域术语或无歧义语言”／“记录架构决定”表述。同时删除“另一个技能需要维护领域模型”的附注，因为说明这一点是调用技能的责任，不应放在此描述里。

<!-- zh-CN:end 8152a6579cd92558 -->

- [#911](https://github.com/mattpocock/skills/pull/911) [`4f28947`](https://github.com/mattpocock/skills/commit/4f289474bad013fe2be8f8769d733f59d9103d6b) Thanks [@mattpocock](https://github.com/mattpocock)! - Quote the `description` front matter in `to-spec`, `code-review`, `setup-matt-pocock-skills`, `writing-fragments`, `writing-shape`, and `wait-what`. An unquoted colon-space left over from the em-dash sweep in [#905](https://github.com/mattpocock/skills/issues/905) made each block invalid YAML, so `skills.sh` skipped all six during discovery and they couldn't be listed or installed via `npx skills`.

<!-- zh-CN:begin 8ad7320b3b06b8ef -->

- [#911](https://github.com/mattpocock/skills/pull/911) [`4f28947`](https://github.com/mattpocock/skills/commit/4f289474bad013fe2be8f8769d733f59d9103d6b) 感谢 [@mattpocock](https://github.com/mattpocock)！——为 `to-spec`、`code-review`、`setup-matt-pocock-skills`、`writing-fragments`、`writing-shape` 和 `wait-what` 的 frontmatter `description` 加引号。[#905](https://github.com/mattpocock/skills/issues/905) 破折号清理遗留的未加引号冒号加空格使这些块成为无效 YAML，导致 `skills.sh` 在发现时跳过六项，无法通过 `npx skills` 列出或安装。

<!-- zh-CN:end 8ad7320b3b06b8ef -->

- [#917](https://github.com/mattpocock/skills/pull/917) [`85f83d3`](https://github.com/mattpocock/skills/commit/85f83d3fde1d3a90d5c9a657f6998c79a6c37308) Thanks [@mattpocock](https://github.com/mattpocock)! - grilling: update the round template so consecutive questions are separated by a horizontal rule (`---`) instead of running together.

<!-- zh-CN:begin 9fe58a262c7fc897 -->

- [#917](https://github.com/mattpocock/skills/pull/917) [`85f83d3`](https://github.com/mattpocock/skills/commit/85f83d3fde1d3a90d5c9a657f6998c79a6c37308) 感谢 [@mattpocock](https://github.com/mattpocock)！——grilling：更新轮次模板，使连续问题用水平分隔线（`---`）隔开，不再挤在一起。

<!-- zh-CN:end 9fe58a262c7fc897 -->

- [#879](https://github.com/mattpocock/skills/pull/879) [`d419977`](https://github.com/mattpocock/skills/commit/d419977fe07d9e1607d3523f3579310bbb076b93) Thanks [@mattpocock](https://github.com/mattpocock)! - grilling: remove em-dashes from `SKILL.md`, replacing them with colons and semicolons so the instructions read as plain text.

<!-- zh-CN:begin 4106b27cac33db4e -->

- [#879](https://github.com/mattpocock/skills/pull/879) [`d419977`](https://github.com/mattpocock/skills/commit/d419977fe07d9e1607d3523f3579310bbb076b93) 感谢 [@mattpocock](https://github.com/mattpocock)！——grilling：从 `SKILL.md` 删除破折号，用冒号和分号替代，使指令读作普通文本。

<!-- zh-CN:end 4106b27cac33db4e -->

- [#905](https://github.com/mattpocock/skills/pull/905) [`e6e9577`](https://github.com/mattpocock/skills/commit/e6e957797d8cceb5b351c0dc840369523f9fb8fb) Thanks [@mattpocock](https://github.com/mattpocock)! - Remove every em-dash from the repo's prose (docs, `SKILL.md` files, ADRs, `README.md`, scripts, JSON/YAML metadata), hand-rewriting each sentence with a comma, colon, period, parentheses, or conjunction rather than mechanically substituting the character. `CLAUDE.md`/`AGENTS.md` now says not to reintroduce them.

<!-- zh-CN:begin 133c4c79a9879cd3 -->

- [#905](https://github.com/mattpocock/skills/pull/905) [`e6e9577`](https://github.com/mattpocock/skills/commit/e6e957797d8cceb5b351c0dc840369523f9fb8fb) 感谢 [@mattpocock](https://github.com/mattpocock)！——从仓库正文（文档、`SKILL.md`、ADR、`README.md`、脚本、JSON/YAML 元数据）删除所有破折号，手工用逗号、冒号、句号、括号或连接词重写每句，而非机械替换字符。`CLAUDE.md`／`AGENTS.md` 现在禁止重新引入。

<!-- zh-CN:end 133c4c79a9879cd3 -->

- [#878](https://github.com/mattpocock/skills/pull/878) [`e3e547b`](https://github.com/mattpocock/skills/commit/e3e547b57d549110a0aa6ff40fd7b871c01c76c9) Thanks [@mattpocock](https://github.com/mattpocock)! - Standardize cross-skill invocation on an explicit "call the Skill tool" instruction instead of bare `/skill`-style prose, across `code-review`, `diagnosing-bugs`, `grill-with-docs`, `grill-me`, `improve-codebase-architecture`, `tdd`, `to-spec`, `to-tickets`, `triage`, and `wayfinder`.

<!-- zh-CN:begin b5bf4ebf5b657549 -->

- [#878](https://github.com/mattpocock/skills/pull/878) [`e3e547b`](https://github.com/mattpocock/skills/commit/e3e547b57d549110a0aa6ff40fd7b871c01c76c9) 感谢 [@mattpocock](https://github.com/mattpocock)！——将 `code-review`、`diagnosing-bugs`、`grill-with-docs`、`grill-me`、`improve-codebase-architecture`、`tdd`、`to-spec`、`to-tickets`、`triage` 和 `wayfinder` 中的跨技能调用统一为明确的“call the Skill tool”指令，替代裸 `/skill` 风格正文。

<!-- zh-CN:end b5bf4ebf5b657549 -->

  - A skill that names another skill in prose ("run the `/grilling` skill") does not reliably cause it to load. This is the documented rough edge behind `grill-with-docs`'s most-reported problem. Naming the tool directly (`Call the Skill tool with "grilling"`) is intended to raise the hit rate. Dropping the leading `/` also makes the instruction harness-neutral rather than less: it no longer assumes Claude Code's trigger syntax.

  <!-- zh-CN:begin 03d178c4c85fd6c5 -->

  - 在正文中点名另一技能（“运行 `/grilling` 技能”）并不能可靠加载它。这是 `grill-with-docs` 报告最多问题背后的已知粗糙边缘。直接点名工具（`Call the Skill tool with "grilling"`）意在提高命中率。去掉前导 `/` 也使指令在运行环境间中立，不再假定 Claude Code 触发语法。

  <!-- zh-CN:end 03d178c4c85fd6c5 -->
  - A step needing more than one skill now says so as multiple calls ("Call the Skill tool twice, for `grilling` and `domain-modeling`"), not one call carrying two names.

  <!-- zh-CN:begin 8ffe72feed21c110 -->

  - 需要多个技能的步骤现在写成多次调用（“Call the Skill tool twice, for `grilling` and `domain-modeling`”），而不是一次调用携带两个名字。

  <!-- zh-CN:end 8ffe72feed21c110 -->
  - Documents the convention in `.agents/invocation.md` for future skills to follow.

  <!-- zh-CN:begin da1be9b989eaab4d -->

  - 在 `.agents/invocation.md` 中记录约定，供未来技能遵循。

  <!-- zh-CN:end da1be9b989eaab4d -->

- [#880](https://github.com/mattpocock/skills/pull/880) [`1dab982`](https://github.com/mattpocock/skills/commit/1dab98299c3b81f560026c01b7ebf55ed5d91373) Thanks [@mattpocock](https://github.com/mattpocock)! - Stop skills from trying to reach user-invoked skills through the Skill tool: fix cross-skill references that violated the "no other skill can call it" invariant in `.agents/invocation.md`, in `to-spec`, `wayfinder`, `to-tickets`, `triage`, `code-review`, and `diagnosing-bugs`.

<!-- zh-CN:begin dbbe0c923a32ca3d -->

- [#880](https://github.com/mattpocock/skills/pull/880) [`1dab982`](https://github.com/mattpocock/skills/commit/1dab98299c3b81f560026c01b7ebf55ed5d91373) 感谢 [@mattpocock](https://github.com/mattpocock)！——阻止技能通过 Skill 工具访问用户调用技能：修复 `to-spec`、`wayfinder`、`to-tickets`、`triage`、`code-review` 和 `diagnosing-bugs` 中违反 `.agents/invocation.md` “其他技能不能调用它”不变量的跨技能引用。

<!-- zh-CN:end dbbe0c923a32ca3d -->

  - `to-spec`, `wayfinder`, `to-tickets`, `triage`, and `code-review` each carried a precondition ("...run `/setup-matt-pocock-skills` if not") that PR [#878](https://github.com/mattpocock/skills/issues/878) rewrote into a literal `Call the Skill tool with "setup-matt-pocock-skills"` instruction. `setup-matt-pocock-skills` is user-invoked, so none of these skills (user-invoked or model-invoked) can call it. Reworded all five as instructions for the agent to tell the human to run it instead.

  <!-- zh-CN:begin 22046866c0c5a958 -->

  - `to-spec`、`wayfinder`、`to-tickets`、`triage` 和 `code-review` 都带有前提条件（“……未运行时 `/setup-matt-pocock-skills`”），PR [#878](https://github.com/mattpocock/skills/issues/878) 将其改写成字面指令 `Call the Skill tool with "setup-matt-pocock-skills"`。`setup-matt-pocock-skills` 由用户调用，因此这些技能（无论用户还是模型调用）都不能调用它。五项都改写为让代理告诉人类运行它。

  <!-- zh-CN:end 22046866c0c5a958 -->
  - `diagnosing-bugs`'s Phase 6 post-mortem hand off to `improve-codebase-architecture` (also user-invoked) the same way, from an autonomous, often-unattended bug-fixing flow with no human in the loop to catch the failed call. Removed the hand-off outright rather than softening it, since it rarely fired in practice. Phase 6 is now "Cleanup" only; the mechanical checklist is untouched.

  <!-- zh-CN:begin 41e85b28809ff151 -->

  - `diagnosing-bugs` 的阶段 6 复盘向 `improve-codebase-architecture`（同为用户调用）的交接也如此；它发生在自主、常无人值守的缺陷修复流程中，没有人在环内发现失败调用。直接移除该交接而非弱化，因为实际很少触发。阶段 6 现仅剩“清理”；机械检查清单未变。

  <!-- zh-CN:end 41e85b28809ff151 -->
  - Added a carve-out paragraph to `.agents/invocation.md`'s "Dependencies between them" section: the `Call the Skill tool with "name"` convention only applies when the named skill is model-invoked. This is the section PR [#878](https://github.com/mattpocock/skills/issues/878) introduced without reconciling it against the user-invoked/model-invoked invariant stated eight lines above it; the gap is most of why this bug reached six call sites instead of one.

  <!-- zh-CN:begin 2283054315f03487 -->

  - 在 `.agents/invocation.md` 的“Dependencies between them”一节增加例外：`Call the Skill tool with "name"` 约定仅在命名技能由模型调用时适用。该节由 PR [#878](https://github.com/mattpocock/skills/issues/878) 引入，却未与上方八行处用户调用／模型调用不变量统一；这个缺口是缺陷扩散到六个调用点而非一个的主要原因。

  <!-- zh-CN:end 2283054315f03487 -->

  Fixes [#453](https://github.com/mattpocock/skills/issues/453).

  <!-- zh-CN:begin da5d85b6cd405bca -->

修复 [#453](https://github.com/mattpocock/skills/issues/453)。

  <!-- zh-CN:end da5d85b6cd405bca -->

- [#904](https://github.com/mattpocock/skills/pull/904) [`594f0f8`](https://github.com/mattpocock/skills/commit/594f0f83188921a60d45d63d6cdac509de20df2c) Thanks [@mattpocock](https://github.com/mattpocock)! - wait-what: follow `GLOSSARY-MAP.md` to the right `GLOSSARY.md` when a repo indexes multiple contexts that way instead of keeping a single root `GLOSSARY.md`.

<!-- zh-CN:begin 87dbe7cca7305128 -->

- [#904](https://github.com/mattpocock/skills/pull/904) [`594f0f8`](https://github.com/mattpocock/skills/commit/594f0f83188921a60d45d63d6cdac509de20df2c) 感谢 [@mattpocock](https://github.com/mattpocock)！——wait-what：仓库通过该方式索引多个上下文时，遵循 `GLOSSARY-MAP.md` 找到正确的 `GLOSSARY.md`，不再固定使用单一根 `GLOSSARY.md`。

<!-- zh-CN:end 87dbe7cca7305128 -->

## 1.2.3

### Patch Changes

<!-- zh-CN:begin 898478dab35207a0 -->

### 补丁变更

<!-- zh-CN:end 898478dab35207a0 -->

- [#779](https://github.com/mattpocock/skills/pull/779) [`efce423`](https://github.com/mattpocock/skills/commit/efce423018fc6468a3239621f1c1bcaacc723801) Thanks [@mattpocock](https://github.com/mattpocock)! - Make `diagnosing-bugs` redact secrets.

<!-- zh-CN:begin 8400857e9648f922 -->

- [#779](https://github.com/mattpocock/skills/pull/779) [`efce423`](https://github.com/mattpocock/skills/commit/efce423018fc6468a3239621f1c1bcaacc723801) 感谢 [@mattpocock](https://github.com/mattpocock)！——让 `diagnosing-bugs` 脱敏秘密。

<!-- zh-CN:end 8400857e9648f922 -->

  - Add a **Redact** section to `SKILL.md`. The skill has the agent show commands, outputs and captured artifacts; the section makes redaction the first move on each — write `<REDACTED>`, build loops against env vars so the credential stays in the environment, and quote only the signal-carrying lines of a captured artifact.

  <!-- zh-CN:begin 8daac9c6305f87d5 -->

  - 在 `SKILL.md` 增加**脱敏**章节。技能让代理展示命令、输出和捕获产物；该章节要求每次首先脱敏：写 `<REDACTED>`，围绕环境变量构建循环使凭据留在环境中，并只引用捕获产物中承载信号的行。

  <!-- zh-CN:end 8daac9c6305f87d5 -->
  - The Phase 1 completion criterion said "paste the invocation and its output". It now says show it redacted, and Phase 1 asks the user for a **redacted** captured artifact.

  <!-- zh-CN:begin ad67be87a32df380 -->

  - 阶段 1 的完成标准原为“粘贴调用及输出”，现要求展示脱敏版；阶段 1 请求用户提供**脱敏**的捕获产物。

  <!-- zh-CN:end ad67be87a32df380 -->
  - Note in `scripts/hitl-loop.template.sh` that `capture` prints its value back to the terminal, so it takes observations while signing in stays a `step`.

  <!-- zh-CN:begin 00e6280c24f62d71 -->

  - 在 `scripts/hitl-loop.template.sh` 注明 `capture` 会把值打印回终端，因此登录期间采集观察仍用 `step`。

  <!-- zh-CN:end 00e6280c24f62d71 -->

- [#781](https://github.com/mattpocock/skills/pull/781) [`14bfbbd`](https://github.com/mattpocock/skills/commit/14bfbbd8654a8d2910299e1a004c19c1979687d8) Thanks [@mattpocock](https://github.com/mattpocock)! - Drop Claude Code's tool and agent-type names from the subagent-dispatch instructions in `code-review`, `codebase-design`, and `improve-codebase-architecture`, so the step is followable on Codex and other harnesses.

<!-- zh-CN:begin 85f3de2aa82c4c4f -->

- [#781](https://github.com/mattpocock/skills/pull/781) [`14bfbbd`](https://github.com/mattpocock/skills/commit/14bfbbd8654a8d2910299e1a004c19c1979687d8) 感谢 [@mattpocock](https://github.com/mattpocock)！——从 `code-review`、`codebase-design` 和 `improve-codebase-architecture` 的子代理分派说明中删除 Claude Code 工具和代理类型名，使步骤在 Codex 及其他运行环境可执行。

<!-- zh-CN:end 85f3de2aa82c4c4f -->

- [#783](https://github.com/mattpocock/skills/pull/783) [`c0fd1e9`](https://github.com/mattpocock/skills/commit/c0fd1e973e040347d424e09934099f1bd6c2dee0) Thanks [@mattpocock](https://github.com/mattpocock)! - wizard: remove the time estimate. The template drops `TOTAL_MINUTES` and the time-remaining display, `stage` takes a name only, and progress is counted in stages.

<!-- zh-CN:begin c20db23c0cfbd6ac -->

- [#783](https://github.com/mattpocock/skills/pull/783) [`c0fd1e9`](https://github.com/mattpocock/skills/commit/c0fd1e973e040347d424e09934099f1bd6c2dee0) 感谢 [@mattpocock](https://github.com/mattpocock)！——wizard：移除时间估计。模板删除 `TOTAL_MINUTES` 和剩余时间显示，`stage` 只接受名称，进度按阶段计数。

<!-- zh-CN:end c20db23c0cfbd6ac -->

## 1.2.2

### Patch Changes

<!-- zh-CN:begin ebc41894c63e0721 -->

### 补丁变更

<!-- zh-CN:end ebc41894c63e0721 -->

- [#766](https://github.com/mattpocock/skills/pull/766) [`4aaccb5`](https://github.com/mattpocock/skills/commit/4aaccb58d40559d7e3c59a029b2290ae5ba538de) Thanks [@mattpocock](https://github.com/mattpocock)! - Make `writing-for-agents` model-invokable in Codex again.

<!-- zh-CN:begin 570075280d351174 -->

- [#766](https://github.com/mattpocock/skills/pull/766) [`4aaccb5`](https://github.com/mattpocock/skills/commit/4aaccb58d40559d7e3c59a029b2290ae5ba538de) 感谢 [@mattpocock](https://github.com/mattpocock)！——让 `writing-for-agents` 在 Codex 中重新可由模型调用。

<!-- zh-CN:end 570075280d351174 -->

  - Drop `policy.allow_implicit_invocation: false` from `agents/openai.yaml`. Codex filtered the skill out of the model-visible skills list, so its description could not trigger it — only an explicit `$writing-for-agents` mention worked.

  <!-- zh-CN:begin b71c52f267d41f99 -->

  - 从 `agents/openai.yaml` 删除 `policy.allow_implicit_invocation: false`。Codex 曾把技能过滤出模型可见技能列表，描述无法触发，只有明确 `$writing-for-agents` 才可用。

  <!-- zh-CN:end b71c52f267d41f99 -->
  - Update the stale `interface.display_name` and `interface.short_description`, which still named the old `writing-great-skills` skill.

  <!-- zh-CN:begin 6008c1438bf4f235 -->

  - 更新仍指向旧 `writing-great-skills` 的 `interface.display_name` 和 `interface.short_description`。

  <!-- zh-CN:end 6008c1438bf4f235 -->
  - Move the skill from the **User-invoked** list to the **Model-invoked** list in `README.md` and `skills/productivity/README.md`.

  <!-- zh-CN:begin 38baf204d241c325 -->

  - 在 `README.md` 和 `skills/productivity/README.md` 中将技能从**用户调用**列表移至**模型调用**列表。

  <!-- zh-CN:end 38baf204d241c325 -->

## 1.2.0

### Minor Changes

<!-- zh-CN:begin a976098623401c59 -->

### 次要变更

<!-- zh-CN:end a976098623401c59 -->

- [#551](https://github.com/mattpocock/skills/pull/551) [`697d4ce`](https://github.com/mattpocock/skills/commit/697d4ce9742da558fd1ba6697c8e9775e2e302dd) Thanks [@mattpocock](https://github.com/mattpocock)! - Add Codex metadata alongside each skill's Claude Code frontmatter so the set works in both harnesses without generated copies.

<!-- zh-CN:begin 3bb7aa0474cf0cc9 -->

- [#551](https://github.com/mattpocock/skills/pull/551) [`697d4ce`](https://github.com/mattpocock/skills/commit/697d4ce9742da558fd1ba6697c8e9775e2e302dd) 感谢 [@mattpocock](https://github.com/mattpocock)！——在每个技能的 Claude Code frontmatter 旁添加 Codex 元数据，使整套技能无需生成副本即可在两个运行环境工作。

<!-- zh-CN:end 3bb7aa0474cf0cc9 -->

  - Add an `agents/openai.yaml` beside every `SKILL.md` with Codex UI metadata (`interface.display_name`, `interface.short_description`).

  <!-- zh-CN:begin 0c4224a12315c8cf -->

  - 在每个 `SKILL.md` 旁添加 `agents/openai.yaml`，包含 Codex UI 元数据（`interface.display_name`、`interface.short_description`）。

  <!-- zh-CN:end 0c4224a12315c8cf -->
  - Mark every user-invoked skill with `policy.allow_implicit_invocation: false`, the Codex analog of `disable-model-invocation: true`, so Codex excludes it from implicit invocation while explicit `$skill` invocation still works.

  <!-- zh-CN:begin bed1458d87540266 -->

  - 用 `policy.allow_implicit_invocation: false` 标记每个用户调用技能，它相当于 `disable-model-invocation: true`，使 Codex 排除隐式调用，同时明确 `$skill` 仍可用。

  <!-- zh-CN:end bed1458d87540266 -->
  - Document the dual-harness invocation model in `.agents/invocation.md`, `CLAUDE.md`, and the promoted-bucket READMEs.

  <!-- zh-CN:begin 86d97a3e0a1e96b4 -->

  - 在 `.agents/invocation.md`、`CLAUDE.md` 和晋升分类 README 中记录双运行环境调用模型。

  <!-- zh-CN:end 86d97a3e0a1e96b4 -->
  - Add `AGENTS.md` as a symlink to `CLAUDE.md` so Codex reads the same repo instructions.

  <!-- zh-CN:begin d803778fc8273d98 -->

  - 添加指向 `CLAUDE.md` 的符号链接 `AGENTS.md`，使 Codex 读取相同仓库指令。

  <!-- zh-CN:end d803778fc8273d98 -->

- [#593](https://github.com/mattpocock/skills/pull/593) [`0f2bdbd`](https://github.com/mattpocock/skills/commit/0f2bdbdb06220d2df3718b8f0483157c6c8a8600) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate **`to-questionnaire`** out of `in-progress/` into the **Productivity** bucket, so it ships in the plugin. It turns a decision you can't answer alone into a Markdown questionnaire for the one person who can — filled in async, or worked through together in a meeting.

<!-- zh-CN:begin 8b6abfed784ea408 -->

- [#593](https://github.com/mattpocock/skills/pull/593) [`0f2bdbd`](https://github.com/mattpocock/skills/commit/0f2bdbdb06220d2df3718b8f0483157c6c8a8600) 感谢 [@mattpocock](https://github.com/mattpocock)！——将 **`to-questionnaire`** 从 `in-progress/` 晋升到 **Productivity** 分类，随插件发布。它把无法独自回答的决定转成给唯一能回答者的 Markdown 问卷：异步填写，或在会议中共同完成。

<!-- zh-CN:end 8b6abfed784ea408 -->

  Its defining move is that it grills you about the **send**, not the subject: a normal grilling session interrogates the topic, which is exactly what you can't answer here, so the interview asks only who the questionnaire is going to and what you need back, then aims every question at the gap between the two.

  <!-- zh-CN:begin 9670ea417369c762 -->

其决定性做法是围绕**发送**而非主题向你追问：普通追问会审问主题，而这里恰恰是你无法回答的部分，因此访谈只询问问卷要发给谁、你需要收回什么，再把每个问题都对准两者之间的差距。

  <!-- zh-CN:end 9670ea417369c762 -->

  Now wired as a promoted skill — plugin entry, top-level + Productivity READMEs under **User-invoked**, a docs page at `docs/productivity/to-questionnaire.md`, and a Standalone route in `ask-matt` framing it as the inverse of `/grill-me` (mine someone else, not yourself).

  <!-- zh-CN:begin 443e839997eae42f -->

现在它已作为晋升技能接入：插件入口、顶层及 Productivity README 中位于 **User-invoked** 下的条目、`docs/productivity/to-questionnaire.md` 文档页面，以及 `ask-matt` 中以 `/grill-me` 的反向形式呈现的独立入口（挖掘别人，而非你自己）。

  <!-- zh-CN:end 443e839997eae42f -->

- [#680](https://github.com/mattpocock/skills/pull/680) [`b3376f8`](https://github.com/mattpocock/skills/commit/b3376f8d39848dd08572ec2667da4739a67c8c04) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate **`wizard`** out of `in-progress/` into the **Engineering** bucket, so it ships in the plugin — and make it model-invoked. It generates an interactive bash script that walks a human through a manual procedure — third-party setup, a one-off migration, an A→B state transition — opening each URL, saying what to click, capturing the values, and writing them into `.env` files and GitHub Actions secrets.

<!-- zh-CN:begin 1007a41d164eb84d -->

- [#680](https://github.com/mattpocock/skills/pull/680) [`b3376f8`](https://github.com/mattpocock/skills/commit/b3376f8d39848dd08572ec2667da4739a67c8c04) 感谢 [@mattpocock](https://github.com/mattpocock)！– 将 **`wizard`** 从 `in-progress/` 晋升到 **Engineering** 分类，从而随插件发布，并改为模型调用。它生成交互式 bash 脚本，引导人完成手动流程，例如第三方设置、一次性迁移或 A→B 状态转换；脚本会打开每个 URL、说明点击什么、捕获值，并写入 `.env` 文件和 GitHub Actions secret。

<!-- zh-CN:end 1007a41d164eb84d -->

  The delightful UX is pre-solved by the bundled `template.sh` (progress with time-remaining, confirmation gates, cross-platform URL opening including WSL, hidden secret entry, idempotent `.env` upserts, `gh secret`/`gh variable` writes with graceful degradation, closing skip summary). Everything above the `STAGES` marker is a fixed library that's never hand-edited — the skill's job is only to scope the procedure and author its **stages**.

  <!-- zh-CN:begin 0f695b73d691f581 -->

令人愉快的用户体验由内置 `template.sh` 预先解决（显示剩余时间的进度、确认关卡、跨平台打开 URL 包括 WSL、隐藏密钥输入、幂等 `.env` 更新插入、优雅降级地写入 `gh secret`／`gh variable`、结束时跳过摘要）。`STAGES` 标记之上的内容都是固定库，从不手工编辑；该技能只负责界定流程范围并编写其中的**阶段**。

  <!-- zh-CN:end 0f695b73d691f581 -->

  Engineering rather than Productivity: it reads `.env*`, `docker-compose*`, framework config and every `secrets.*`/`vars.*` reference in `.github/workflows/` to scope itself, writes CI secrets, and verifies its output with `bash -n` and `shellcheck`.

  <!-- zh-CN:begin cea830559e6d2a1b -->

它属于 Engineering 而非 Productivity：它会读取 `.env*`、`docker-compose*`、框架配置以及 `.github/workflows/` 中每一处 `secrets.*`／`vars.*` 引用，以界定自身范围，写入 CI secret，并用 `bash -n` 和 `shellcheck` 验证输出。

  <!-- zh-CN:end cea830559e6d2a1b -->

  Because it is model-invoked, the agent can reach for it the moment it hits a step only a human can perform, instead of dumping numbered instructions into the chat and hoping you follow them. Typing `/wizard` works exactly as before — model-invocation only ever _adds_ the agent's reach. The description is written as the pointer that decides when it fires: what it produces, four trigger branches (provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, a one-off migration or cutover), and an explicit non-trigger — don't invoke it for steps the agent can perform itself. Work an agent can do, an agent should do; the wizard is for the clicks, approvals and dashboard trips you would not hand to one. The stage-list confirmation before a line is written now doubles as the proposal when the agent fires it mid-build.

  <!-- zh-CN:begin de86bfaa82b10c48 -->

由于采用模型调用，智能体遇到只有人才能执行的步骤时可以立即调用它，无需把编号说明倾倒进聊天并指望你照做。输入 `/wizard` 仍与以前完全一样；模型调用只是*扩展*智能体的触及范围。描述被写成决定何时触发的指针：它产出什么、四个触发分支（配置基础设施、设置凭据或 CI secret、走过陌生的第三方仪表板、一次性迁移或切换），以及明确的非触发条件：不要为智能体自己能完成的步骤调用它。智能体能做的工作就应由智能体完成；向导面向不会交给智能体的点击、审批和仪表板操作。现在，写入任何一行前的阶段列表确认，也充当智能体构建中途触发它时的提案。

  <!-- zh-CN:end de86bfaa82b10c48 -->

  Now wired as a promoted skill — plugin entry, top-level + Engineering READMEs under **Model-invoked**, a docs page at `docs/engineering/wizard.md`, and a Standalone route in `ask-matt` for the steps only a human can take. Model-invocation also puts it out of the reach of [#693](https://github.com/mattpocock/skills/issues/693), which drops user-invoked skills from the listing on Claude's desktop and web surfaces.

  <!-- zh-CN:begin 4b7f8eb6ed9d9389 -->

现在它已作为晋升技能接入：插件入口、顶层及 Engineering README 中位于 **Model-invoked** 下的条目、`docs/engineering/wizard.md` 文档页面，以及 `ask-matt` 中面向只能由人执行步骤的独立入口。模型调用还让它不受 [#693](https://github.com/mattpocock/skills/issues/693) 影响，该问题会从 Claude 桌面端和网页界面的列表中移除用户调用技能。

  <!-- zh-CN:end 4b7f8eb6ed9d9389 -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) Thanks [@mattpocock](https://github.com/mattpocock)! - Reshape the **`prototype`** skill around two ideas: the demo is **a single shareable HTML file**, and the prototype is **a primary source**.

<!-- zh-CN:begin d2e1eb2bec121269 -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！– 围绕两个理念重塑 **`prototype`** 技能：演示是**一个可分享的 HTML 文件**，原型是**一手来源**。

<!-- zh-CN:end d2e1eb2bec121269 -->

  The logic branch now produces one self-contained file (plain HTML/CSS/JS, no build, no server) instead of a terminal app — a non-developer can open it by double-click and drive it in their own domain language: a labelled state panel, always-available free-play buttons, and a set of tabbed **guided walkthroughs**, each a scenario with the ordered buttons to press underneath it. The portable pure-logic module still lifts into the real code; the HTML shell is the throwaway.

  <!-- zh-CN:begin 3f4168dec05bcf0d -->

逻辑分支现在生成一个自包含文件（纯 HTML/CSS/JS，无构建、无服务器），而非终端应用。非开发者可以双击打开，并用本领域语言操作：带标签的状态面板、始终可用的自由操作按钮，以及一组分页的**引导式演练**；每个演练都展示一个场景，下方列出依次按下的按钮。可移植的纯逻辑模块仍会提取到真实代码中；HTML 外壳则是用后即弃的部分。

  <!-- zh-CN:end 3f4168dec05bcf0d -->

  Throwaway no longer means deleted. Rather than being removed once it has answered its question, the prototype is captured as runnable evidence on a throwaway branch (`prototype/<name>`) out of main, with a context pointer to it left on the implementation issue — so the main branch keeps only the validated decision while the exploration stays findable. The answer (verdict + question) is still captured durably in an issue/ADR/commit.

  <!-- zh-CN:begin 2ec4dd5b0ca896bb -->

“用后即弃”不再意味着删除。原型回答完问题后不会直接移除，而是作为可运行证据保存在从 `main` 分出的临时分支（`prototype/<name>`）上，并在实现 issue 中留下上下文指针。这样主分支只保留已验证的决策，探索仍然可查。答案（结论和问题）仍持久记录在 issue／ADR／提交中。

  <!-- zh-CN:end 2ec4dd5b0ca896bb -->

- [#536](https://github.com/mattpocock/skills/pull/536) [`42a5b70`](https://github.com/mattpocock/skills/commit/42a5b70fcacc7baff1977b13f3919fb2f63af14e) Thanks [@mattpocock](https://github.com/mattpocock)! - Ship the skill set as a native **Claude Code plugin**, listed in Claude Code's official marketplace. You can now subscribe to the promoted skills as a managed, read-only bundle instead of copying editable files:

<!-- zh-CN:begin f1d9964d8358eded -->

- [#536](https://github.com/mattpocock/skills/pull/536) [`42a5b70`](https://github.com/mattpocock/skills/commit/42a5b70fcacc7baff1977b13f3919fb2f63af14e) 感谢 [@mattpocock](https://github.com/mattpocock)！– 将整套技能作为原生 **Claude Code 插件**发布，并列入 Claude Code 官方市场。现在可以订阅晋升技能托管、只读的套装，无需复制可编辑文件：

<!-- zh-CN:end f1d9964d8358eded -->

  ```bash
  claude plugins install mattpocock-skills
  ```

  Or, from inside a session:

  <!-- zh-CN:begin de1789f50ccd80ca -->

或在会话内执行：

  <!-- zh-CN:end de1789f50ccd80ca -->

  ```
  /plugin install mattpocock-skills
  ```

  There is no marketplace to add first — the official marketplace is configured by default.

  <!-- zh-CN:begin d7c1eb2a5ea19eff -->

无需先添加市场：官方市场默认已配置。

  <!-- zh-CN:end d7c1eb2a5ea19eff -->

  `.claude-plugin/plugin.json` carries the full plugin metadata (version, description, author, license, keywords) and the explicit list of promoted skills. `skills.sh` remains the universal installer (and the path for Codex and other harnesses today); a native Codex plugin is deferred — see `.agents/adr/0002-ship-as-a-claude-code-plugin.md` for why.

  <!-- zh-CN:begin 7e04bc9d29b61ca0 -->

`.claude-plugin/plugin.json` 携带完整插件元数据（版本、描述、作者、许可证、关键词）以及明确的晋升技能列表。`skills.sh` 仍是通用安装器（也是目前 Codex 和其他运行环境的路径）；原生 Codex 插件暂缓发布，原因见 `.agents/adr/0002-ship-as-a-claude-code-plugin.md`。

  <!-- zh-CN:end 7e04bc9d29b61ca0 -->

- [#751](https://github.com/mattpocock/skills/pull/751) [`355fa74`](https://github.com/mattpocock/skills/commit/355fa7420b418af838998f7ec4365ceda1c8dfcc) Thanks [@mattpocock](https://github.com/mattpocock)! - Add **`wait-what`** — a one-word corrective for model verbosity. Type it the moment a message doesn't land, and the agent re-pitches it: a little context, ASD-STE100 Simplified Technical English, and the ubiquitous language from your `CONTEXT.md`. User-invoked, three lines long.

<!-- zh-CN:begin 4a749e274d60c187 -->

- [#751](https://github.com/mattpocock/skills/pull/751) [`355fa74`](https://github.com/mattpocock/skills/commit/355fa7420b418af838998f7ec4365ceda1c8dfcc) 感谢 [@mattpocock](https://github.com/mattpocock)！– 添加 **`wait-what`**，用一个词纠正模型冗长。消息没让人听懂时立即输入它，智能体就会重新讲一遍：补一点上下文，使用 ASD-STE100 简化技术英语，并采用 `CONTEXT.md` 中的通用语言。该技能由用户调用，只有三行。

<!-- zh-CN:end 4a749e274d60c187 -->

  The mechanism is the name. Concision skills fail by growing — a 400-line skill still leaves the model verbose — so this one is a single precise leading word and nothing else. Names that describe the _output_ (`/tldr`, `/no-fluff`) make the model clip words and lose you further; naming the _listener's_ state asks for both halves at once, fewer words **and** the context you were missing. It also reuses the leading words already in your global `CLAUDE.md`, so the skill, `CLAUDE.md` and every `CONTEXT.md` reach for the same tokens.

  <!-- zh-CN:begin ec28b08607418ee6 -->

机制就在名称本身。简洁技能常因不断膨胀而失效：写 400 行的技能，模型仍可能啰嗦；所以这个技能只有一个精准的引导词，别无他物。描述*输出*的名称（`/tldr`、`/no-fluff`）会让模型删减词语，反而使你更听不懂；命名*听者*的状态则同时要求两者：更少的词，**以及**你缺失的上下文。它还复用全局 `CLAUDE.md` 中已有的引导词，使技能、`CLAUDE.md` 和每个 `CONTEXT.md` 都指向同一组词。

  <!-- zh-CN:end ec28b08607418ee6 -->

  It repairs one message; it doesn't prevent the next one. The cure for jargon is a shared language built upfront with `/grill-with-docs`; this is what you reach for when you don't have one yet.

  <!-- zh-CN:begin ad8cd24b66f91184 -->

它修复一条消息，不能预防下一条。术语问题的根治办法是事先用 `/grill-with-docs` 建立共同语言；尚未建立共同语言时，才使用本技能。

  <!-- zh-CN:end ad8cd24b66f91184 -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) Thanks [@mattpocock](https://github.com/mattpocock)! - Name the `/wayfinder` unit a **decision ticket**, and burn research tickets down with subagents.

<!-- zh-CN:begin 55fa647d37fc0e41 -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！– 将 `/wayfinder` 的工作单元命名为**决策票**，并用子智能体并行消化研究票。

<!-- zh-CN:end 55fa647d37fc0e41 -->

  People kept reading a wayfinder ticket as an ordinary _implementation_ ticket — a slice of a build to execute — when wayfinder uses them as **decision tickets**: questions whose resolution is a decision. The skill description and its opening line now introduce the term (and say what makes it one), with the `ask-matt` / engineering README blurbs and the docs page matching — while "ticket" stays the everyday word once the term is established. `CONTEXT.md` records **Decision ticket** as a domain term, so the "avoid: ticket" guidance no longer contradicts wayfinder's deliberate use of the word.

  <!-- zh-CN:begin f6a44d1c6b80a32e -->

人们一直把 wayfinder 的票理解为普通的*实现*票，即待执行构建的一部分；wayfinder 实际将其用作**决策票**：答案本身就是一个决策的问题。技能描述和开头句现在引入该术语（并说明判定标准），`ask-matt`／工程 README 简介和文档页面也保持一致；“票”在术语确立后仍作为日常用词。`CONTEXT.md` 将 **Decision ticket** 记为领域术语，因此“避免：票”的指导不再与 wayfinder 有意使用该词相冲突。

  <!-- zh-CN:end f6a44d1c6b80a32e -->

  Research tickets are no longer parked for a separately-launched session. Research stays a real ticket type — it's a genuine shared blocker that downstream decisions hang on, and that dependency is exactly what the frontier's blocking edges exist to render. What changes is how it's resolved: because research is AFK, charting doesn't stop and read it. After creating the tickets, the charting session fires a `/research` subagent for each research ticket to burn it down in parallel, capturing the findings on a throwaway `research/<name>` branch with a context pointer. Research tickets are the one exception to _one ticket per session_.

  <!-- zh-CN:begin 8ef46c2e227bd320 -->

研究票不再留待另开会话处理。研究仍是真实的票类型：它是下游决策确实依赖的共享阻塞项，这种依赖正是前沿图中的阻塞边要呈现的内容。变化的是解决方式：研究可以离线进行，所以绘图不会停下来读取它。创建票之后，绘图会话会为每张研究票触发一个 `/research` 子智能体并行消化，并将发现保存在临时 `research/<name>` 分支上，同时留下上下文指针。研究票是*每个会话一张票*的唯一例外。

  <!-- zh-CN:end 8ef46c2e227bd320 -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) Thanks [@mattpocock](https://github.com/mattpocock)! - **Breaking:** rename **`writing-great-skills`** → **`writing-for-agents`**, restructure it, and add a new leading word.

<!-- zh-CN:begin 606e2dc19e4c2b4a -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！– **破坏性变更：** 将 **`writing-great-skills`** 更名为 **`writing-for-agents`**，调整其结构，并添加新的引导词。

<!-- zh-CN:end 606e2dc19e4c2b4a -->

  The reference now covers any document an agent consumes — skills, `AGENTS.md` / `CLAUDE.md`, docs reached by a pointer — not just skills. `GLOSSARY.md` is merged into `SKILL.md` (one authoritative treatment per term; the `_Avoid_` synonym lists and the standalone Predictability definition are gone); the skill-only mechanics (frontmatter, model- vs user-invoked, router skills, the invocation cut of splitting) are disclosed to a new `SKILL-MECHANICS.md`. The skill is now **model-invoked**: it fires when creating or editing skills or modifying `AGENTS.md`/`CLAUDE.md`. `ask-matt`'s pointer updated. Reinstall under the new name; the old name is gone (no alias).

  <!-- zh-CN:begin ca4402509b1561de -->

参考资料现在覆盖智能体消费的任何文档，包括技能、`AGENTS.md`／`CLAUDE.md`，以及通过指针到达的文档，而不只是技能。`GLOSSARY.md` 已合并进 `SKILL.md`（每个术语只有一处权威说明；`_Avoid_` 同义词列表和独立的 Predictability 定义已删除）；技能专属机制（前置元数据、模型调用与用户调用、路由技能、拆分中的调用切分）移入新的 `SKILL-MECHANICS.md`。该技能现在由**模型调用**：创建或编辑技能，或修改 `AGENTS.md`／`CLAUDE.md` 时触发。`ask-matt` 的指针已更新。请用新名称重新安装；旧名称已移除（没有别名）。

  <!-- zh-CN:end ca4402509b1561de -->

  The pruning section gains **cache**. Single source of truth now reaches past the document into the environment — `package.json` scripts, config files, directory layout, `--help` output are themselves authoritative, so a doc that restates them is a cache of a lookup, earning its load only when the lookup is expensive. The positive target: cache what the agent cannot find by looking (unwritten conventions, the reason behind a choice, gotchas no config confesses), and leave one-file, one-command lookups to the environment, where they cannot go stale.

  <!-- zh-CN:begin 7f04076eeaf5e081 -->

精简章节新增**缓存**概念。单一事实来源现在延伸到文档之外的环境：`package.json` 脚本、配置文件、目录布局、`--help` 输出本身就是权威来源，因此重述这些内容的文档只是查询缓存，只有查询成本高时才值得加载。正向目标：缓存智能体查看不到的内容（未写明的约定、选择背后的原因、配置未透露的陷阱），把单文件、单命令即可完成的查询留给环境，使其不会过时。

  <!-- zh-CN:end 7f04076eeaf5e081 -->

- [#533](https://github.com/mattpocock/skills/pull/533) [`45afd80`](https://github.com/mattpocock/skills/commit/45afd8074a8b7de5fe073845d080fa9dd6c429fa) Thanks [@mattpocock](https://github.com/mattpocock)! - Add a YAGNI scoping filter to the **`improve-codebase-architecture`** skill's Explore step. Instead of scanning the whole repo evenly, it now scopes to where change is actually landing: if you name a direction it takes it, otherwise it reads the last ~20 commit messages to bias exploration toward actively-developed paths. A deepening opportunity in code nobody touches is a refactor you'll never cash in — the leverage only pays off where you keep editing — so the report stops tidying dormant corners of the repo.

<!-- zh-CN:begin a70cd8b0888772fb -->

- [#533](https://github.com/mattpocock/skills/pull/533) [`45afd80`](https://github.com/mattpocock/skills/commit/45afd8074a8b7de5fe073845d080fa9dd6c429fa) 感谢 [@mattpocock](https://github.com/mattpocock)！– 为 **`improve-codebase-architecture`** 技能的探索步骤添加 YAGNI 范围过滤器。它不再均匀扫描整个仓库，而是限定在实际发生变更的区域：如果指定方向就按方向执行，否则读取最近约 20 条提交消息，把探索偏向正在活跃开发的路径。无人触碰的代码里即使有深化机会，也是永远无法兑现的重构；收益只在持续编辑之处实现，因此报告不再整理仓库中沉寂的角落。

<!-- zh-CN:end a70cd8b0888772fb -->

### Patch Changes

<!-- zh-CN:begin e38303113548a81b -->

### 补丁变更

<!-- zh-CN:end e38303113548a81b -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) Thanks [@mattpocock](https://github.com/mattpocock)! - Sharpen `/ask-matt` — the router now covers phase boundaries, the two wayfinder mistakes, and two skills it never mentioned.

<!-- zh-CN:begin 6fd67c9dc3567e10 -->

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！– 打磨 `/ask-matt`：路由器现在覆盖阶段边界、wayfinder 的两种常见错误，以及此前从未提及的两个技能。

<!-- zh-CN:end 6fd67c9dc3567e10 -->

  **Phase boundaries.** A **phase** is a chunk of work inside a session — the grilling, the implementation, the QA — and the boundary between two of them is where you decide what to do with the context you've built. The two-bullet `Crossing sessions` section is replaced by a decision tree carrying all five options in order (**continue**, `/clear`, `/handoff`, **subagent**, `/compact`), with the reasoning disclosed in a new `PHASE-BOUNDARIES.md`. Three fixes come with it:

  <!-- zh-CN:begin 99aa967be167570e -->

**阶段边界。** **阶段**是会话内的一块工作，例如追问、实现、QA；两个阶段的边界是你决定如何处理已有上下文的地方。原先只有两条的 `Crossing sessions` 章节替换为按顺序包含全部五个选项的决策树（**继续**、`/clear`、`/handoff`、**子智能体**、`/compact`），理由公开在新的 `PHASE-BOUNDARIES.md` 中。随之带来三项修正：

  <!-- zh-CN:end 99aa967be167570e -->

  - **`/handoff` was oversold.** It read as the general bridge between context windows. It's narrow: you need it only when something has to _travel_ — a new harness, a new directory, a colleague, or a side task forked mid-phase. What it buys is portability.

  <!-- zh-CN:begin c90f4efa3b5a70a0 -->

  - **`/handoff` 被过度宣传了。** 它读起来像上下文窗口之间的通用桥梁。其实范围很窄：只有某些内容必须*传递*时才需要它，例如新的运行环境、新目录、同事，或阶段中途分叉出的旁支任务。它提供的是可移植性。

  <!-- zh-CN:end c90f4efa3b5a70a0 -->
  - **`/compact` is the default, not the first reach.** It sits at the bottom of the tree, after the four cheaper or more precise questions above it. Starting there produces a session that's confidently wrong about whatever the summary flattened.

  <!-- zh-CN:begin eee42a84a35fd14a -->

  - **`/compact` 是默认选择，而不应首先采用。** 它位于决策树底部，排在上方四项更便宜或更精确的问题之后。一上来就用它，会让会话对摘要抹平的内容产生自信的错误判断。

  <!-- zh-CN:end eee42a84a35fd14a -->
  - **Two branches were missing entirely.** **Continue** is the one to rule out first — it's the only move that keeps the conversation as a primary source rather than a summary of one — and a **subagent** handles anything scoped tightly enough to run AFK.

  <!-- zh-CN:begin cb980af7ab787366 -->

  - **此前完全缺少两个分支。** 应首先排除**继续**的可能性，它是唯一让对话本身而非对话摘要持续作为一手来源的做法；任务范围足够紧凑、可以离线运行的工作，则交给**子智能体**。

  <!-- zh-CN:end cb980af7ab787366 -->

  Context hygiene's escape hatch now says `/compact` rather than `/handoff` (same harness, same directory, at a boundary — the handoff clause doesn't apply), and the smart zone figure is updated from ~120k to ~150k tokens.

  <!-- zh-CN:begin 98b5b51ec8f09a27 -->

上下文卫生的逃生口现在写 `/compact` 而非 `/handoff`（同一运行环境、同一目录、处在边界，交接条款不适用），智能区间数值从约 120k token 更新为约 150k token。

  <!-- zh-CN:end 98b5b51ec8f09a27 -->

  **Wayfinder routing.** The two mistakes people most often make with the heaviest, most cognitively demanding flow:

  <!-- zh-CN:begin 39a33155b5ef2bb3 -->

**Wayfinder 路由。** 人们使用这个最重、认知要求最高的流程时最常犯的两个错误：

  <!-- zh-CN:end 39a33155b5ef2bb3 -->

  - **Over-reaching for it.** It's slower and denser than a single grill, so it's flagged as the heaviest flow and reserved for the idea that genuinely won't fit one session — a well-scoped feature belongs on `/grill-with-docs`, not here.

  <!-- zh-CN:begin f64ae286f7429a3a -->

  - **过早伸手去用。** 它比单次追问更慢、更密集，因此被标记为最重的流程，只留给确实无法在单个会话中容纳的想法；范围明确的功能应使用 `/grill-with-docs`，而不是这里。

  <!-- zh-CN:end f64ae286f7429a3a -->
  - **Losing the way at the handoff.** When the map clears, wayfinder hands off, it doesn't build: merge onto the main flow at `/to-spec` (which collapses the map's linked decisions into a buildable plan) rather than looping the map straight into `/implement`. Straight-to-`/implement` is only for efforts that turned out genuinely small.

  <!-- zh-CN:begin 40d085880a7d6937 -->

  - **交接时弄丢方向。** 地图清晰后，wayfinder 只交接而不构建：在 `/to-spec` 汇入主流程（将地图关联的决策折叠成可构建计划），不要直接把地图循环进 `/implement`。只有最终发现确实很小的努力才直接进入 `/implement`。

  <!-- zh-CN:end 40d085880a7d6937 -->

  **Missing routes.** `/grilling` and `/resolving-merge-conflicts` were absent from the router altogether and are now in it, and `grill-me` splits from `grill-with-docs` on whether you are in a working directory.

  <!-- zh-CN:begin a6b212679b80df3b -->

  **缺失路由。** 路由器此前完全没有 `/grilling` 和 `/resolving-merge-conflicts`，现已加入；`grill-me` 与 `grill-with-docs` 根据是否位于工作目录中分流。

  <!-- zh-CN:end a6b212679b80df3b -->

- [#502](https://github.com/mattpocock/skills/pull/502) [`44eed54`](https://github.com/mattpocock/skills/commit/44eed545186ffd0263e8004867750b80cfddd215) Thanks [@mattpocock](https://github.com/mattpocock)! - Make `/setup-matt-pocock-skills` friendlier and align the local-markdown tracker with the current spec.

<!-- zh-CN:begin 2213cbe381636713 -->

- [#502](https://github.com/mattpocock/skills/pull/502) [`44eed54`](https://github.com/mattpocock/skills/commit/44eed545186ffd0263e8004867750b80cfddd215) 感谢 [@mattpocock](https://github.com/mattpocock)！— 让 `/setup-matt-pocock-skills` 更友好，并让本地 Markdown 跟踪器符合当前规格。

<!-- zh-CN:end 2213cbe381636713 -->

  - **Triage labels** are now asked about only when the `triage` skill is installed, and then as a single recommended-yes question ("keep the default triage labels?") instead of an override interrogation. When `triage` isn't installed, the section — and `docs/agents/triage-labels.md` — are skipped.

  <!-- zh-CN:begin 41b762a6869e4cdc -->

  - **分诊标签**现在只在安装 `triage` 技能时询问，而且只问一个建议答“是”的问题（“保留默认分诊标签吗？”），不再盘问覆盖设置。未安装 `triage` 时，跳过此部分与 `docs/agents/triage-labels.md`。

  <!-- zh-CN:end 41b762a6869e4cdc -->
  - **External PRs as a request surface** is no longer a setup question. The GitHub/GitLab templates still carry the flag, defaulted off; a user can flip it in `docs/agents/issue-tracker.md` later.

  <!-- zh-CN:begin 4b37cf144e180b01 -->

  - **将外部 PR 作为请求入口**不再是设置问题。GitHub/GitLab 模板仍保留此标志，默认关闭；以后可在 `docs/agents/issue-tracker.md` 中开启。

  <!-- zh-CN:end 4b37cf144e180b01 -->
  - **Domain docs** default to single-context without asking; multi-context is only offered when the repo shows monorepo signals.

  <!-- zh-CN:begin cade9c4551e536a8 -->

  - **领域文档**默认使用单上下文，不再询问；仅当仓库显示 monorepo 特征时提供多上下文。

  <!-- zh-CN:end cade9c4551e536a8 -->
  - **Local-markdown tickets** are now one file per ticket under `.scratch/<feature>/issues/<NN>-<slug>.md` — never a single combined `tickets.md`. `/to-tickets` and the local issue-tracker template now agree, and the spec file is `spec.md` (not `PRD.md`) to match `/to-spec`.

  <!-- zh-CN:begin 058540d5adf692ea -->

  - **本地 Markdown 工单**每张单独放在 `.scratch/<feature>/issues/<NN>-<slug>.md`，绝不合并成一个 `tickets.md`。`/to-tickets` 与本地跟踪器模板现已一致，规格文件为 `spec.md`（而非 `PRD.md`），与 `/to-spec` 一致。

  <!-- zh-CN:end 058540d5adf692ea -->

  Docs pages for `setup-matt-pocock-skills` and `to-tickets` re-synced.

  <!-- zh-CN:begin 38d42e884ac8da07 -->

  已重新同步 `setup-matt-pocock-skills` 和 `to-tickets` 文档页。

  <!-- zh-CN:end 38d42e884ac8da07 -->

- [#532](https://github.com/mattpocock/skills/pull/532) [`170ad48`](https://github.com/mattpocock/skills/commit/170ad48655825783d0193e850e31a9aac957bb95) Thanks [@mattpocock](https://github.com/mattpocock)! - Reword **`grilling`** for general use. Its description and body no longer scope the interview to a software plan: "this plan" → "this", "enact the plan" → "act on it", and "exploring the codebase" → "exploring the environment". The technique is unchanged; it now reads as a stress-test of any plan, decision, or idea.

<!-- zh-CN:begin c561ac76feefe452 -->

- [#532](https://github.com/mattpocock/skills/pull/532) [`170ad48`](https://github.com/mattpocock/skills/commit/170ad48655825783d0193e850e31a9aac957bb95) 感谢 [@mattpocock](https://github.com/mattpocock)！— 为通用用途重写 **`grilling`**。描述与正文不再把访谈局限于软件计划：“此计划”→“此事”，“实施计划”→“采取行动”，“探索代码库”→“探索环境”。方法不变，现在可对任何计划、决策或想法进行压力检验。

<!-- zh-CN:end c561ac76feefe452 -->

- [#593](https://github.com/mattpocock/skills/pull/593) [`a4b2009`](https://github.com/mattpocock/skills/commit/a4b2009a1a3ac9575506c10b4c84f08f9bba7a38) Thanks [@mattpocock](https://github.com/mattpocock)! - Rework **`grilling`** from one-question-at-a-time to round-by-round. It now maps the decision tree and asks the whole **frontier** — every question whose prerequisites are already settled — in a single numbered round, then recomputes the frontier from the user's answers and asks the next round. Same 13 questions land in ~3 rounds instead of 13. Facts the environment can answer are dispatched to background sub-agents so research never blocks the round: only questions downstream of a running exploration wait for it. The session ends when the frontier is empty.

<!-- zh-CN:begin aaf0d037c6e74f44 -->

- [#593](https://github.com/mattpocock/skills/pull/593) [`a4b2009`](https://github.com/mattpocock/skills/commit/a4b2009a1a3ac9575506c10b4c84f08f9bba7a38) 感谢 [@mattpocock](https://github.com/mattpocock)！— 将 **`grilling`** 从一次一问改为逐轮提问。先绘制决策树，一轮以编号提出整个**前沿**，即所有前置条件已确定的问题；根据用户回答重新计算前沿，再提下一轮。同样 13 个问题约 3 轮完成，而非 13 轮。环境可回答的事实交后台子代理，研究不阻塞整轮；只有依赖正在进行的探索的问题需要等待。前沿为空时结束会话。

<!-- zh-CN:end aaf0d037c6e74f44 -->

  Every question in a round is emitted in one fixed shape — `❓ **Q1** - **<title>**`, then the body (prose or multiple choices), then the recommendation on its own `➡️` line. A round reads as a scannable numbered list with each recommendation visually separated from the question, so you can answer by number instead of quoting questions back.

  <!-- zh-CN:begin 67fd1937f44bd198 -->

  每轮每问采用固定形式 `❓ **Q1** - **<标题>**`，接着是正文（叙述或多选），然后建议独占 `➡️` 行。整轮形成易浏览的编号列表，建议与问题视觉分离，可按编号回答，无需引用问题。 对应结构：`❓ **Q1** - **<title>**`。

  <!-- zh-CN:end 67fd1937f44bd198 -->

  `grill-me`, `grill-with-docs` and `triage` run the frontier a round at a time as well — `triage`'s grill step and `grilling`'s Codex `short_description` now say so instead of describing the old rhythm. The opt-out for one-question-at-a-time (a line in your global `CLAUDE.md`) is unchanged.

  <!-- zh-CN:begin 5f8b147b81809665 -->

  `grill-me`、`grill-with-docs`、`triage` 也逐轮推进前沿；`triage` 的追问步骤与 `grilling` 的 Codex `short_description` 现已这样说明，不再描述旧节奏。在全局 `CLAUDE.md` 加一行以选择一次一问的退出方式不变。

  <!-- zh-CN:end 5f8b147b81809665 -->

- [#752](https://github.com/mattpocock/skills/pull/752) [`c66bdee`](https://github.com/mattpocock/skills/commit/c66bdeeee002d81e3f8b21403c07f9a0d7bea6da) Thanks [@mattpocock](https://github.com/mattpocock)! - Remove six skills from the repo. None of them was in the Claude Code plugin, but all six were installable through [skills.sh](https://skills.sh/mattpocock/skills), which serves every skill in the repo — so this is what leaves that listing, and where each one went.

<!-- zh-CN:begin 085544f46c0511e1 -->

- [#752](https://github.com/mattpocock/skills/pull/752) [`c66bdee`](https://github.com/mattpocock/skills/commit/c66bdeeee002d81e3f8b21403c07f9a0d7bea6da) 感谢 [@mattpocock](https://github.com/mattpocock)！— 从仓库删除六个技能。它们均不在 Claude Code 插件中，但此前都可通过提供仓库所有技能的 [skills.sh](https://skills.sh/mattpocock/skills) 安装；下文说明退出列表的条目及其去向。

<!-- zh-CN:end 085544f46c0511e1 -->

  Four retired skills, each already absorbed by a skill that does the job better:

  <!-- zh-CN:begin 67cc2086f6699f0a -->

  四个退役技能都已被更适合完成其任务的技能吸收：

  <!-- zh-CN:end 67cc2086f6699f0a -->

  - **`ubiquitous-language`** → **`/domain-modeling`**, which builds and maintains the whole domain model rather than dumping a glossary from one conversation.

  <!-- zh-CN:begin f1922821c3de855f -->

  - **`ubiquitous-language`** → **`/domain-modeling`**；后者构建维护整个领域模型，而非从单次对话倾倒术语表。

  <!-- zh-CN:end f1922821c3de855f -->
  - **`design-an-interface`** → **`/codebase-design`**. Nothing is lost: the "design it twice" technique — parallel sub-agents generating radically different designs, from Ousterhout — ships inside that skill as `DESIGN-IT-TWICE.md`.

  <!-- zh-CN:begin 5ced77d7fe2d72cf -->

  - **`design-an-interface`** → **`/codebase-design`**。内容没有丢失：源自 Ousterhout 的“设计两次”技术，由并行子代理产生截然不同的设计，作为 `DESIGN-IT-TWICE.md` 随技能提供。

  <!-- zh-CN:end 5ced77d7fe2d72cf -->
  - **`qa`** → **`/triage`** and **`/to-tickets`**.

  <!-- zh-CN:begin faaa6a5234fc8a6e -->

  - **`qa`** → **`/triage`** 和 **`/to-tickets`**（替代技能）。

  <!-- zh-CN:end faaa6a5234fc8a6e -->
  - **`request-refactor-plan`** → **`/to-spec`** and **`/improve-codebase-architecture`**.

  <!-- zh-CN:begin 141841b0eb5f02f6 -->

  - **`request-refactor-plan`** → **`/to-spec`** 和 **`/improve-codebase-architecture`**（替代技能）。

  <!-- zh-CN:end 141841b0eb5f02f6 -->

  And two that were only ever mine — tied to my own machine and never meant for anyone else. The `personal/` bucket goes with them:

  <!-- zh-CN:begin 7259b0c5cd781003 -->

  另外两个一直只供我自己使用，绑定我的机器，从未打算供其他人使用。`personal/` 分类也随之移除：

  <!-- zh-CN:end 7259b0c5cd781003 -->

  - **`edit-article`**
  - **`obsidian-vault`**, which hardcoded a path to my own Obsidian vault.

  <!-- zh-CN:begin 83e286a9a0680b63 -->

  - **`obsidian-vault`**，硬编码了我自己的 Obsidian 笔记库路径。

  <!-- zh-CN:end 83e286a9a0680b63 -->

  `skills/deprecated/` stays as a bucket, now empty. `skills/in-progress/` is unchanged and is now described for what it actually is: a beta channel, published on purpose, installable one skill at a time through skills.sh.

  <!-- zh-CN:begin 1ea93ef605e17cd9 -->

  保留 `skills/deprecated/` 分类，目前为空。`skills/in-progress/` 不变，现如实描述为有意发布的测试版渠道，可通过 skills.sh 逐个安装技能。

  <!-- zh-CN:end 1ea93ef605e17cd9 -->

- [#734](https://github.com/mattpocock/skills/pull/734) [`a2f9333`](https://github.com/mattpocock/skills/commit/a2f9333669ff53db762c87ecda5a15442060a3be) Thanks [@mattpocock](https://github.com/mattpocock)! - Finish the `to-prd` → `to-spec` rename: "spec" is now the only term in the shipped text.

<!-- zh-CN:begin 9f2965124d99fd60 -->

- [#734](https://github.com/mattpocock/skills/pull/734) [`a2f9333`](https://github.com/mattpocock/skills/commit/a2f9333669ff53db762c87ecda5a15442060a3be) 感谢 [@mattpocock](https://github.com/mattpocock)！— 完成 `to-prd` → `to-spec` 重命名：“规格”现为发布文本中的唯一术语。

<!-- zh-CN:end 9f2965124d99fd60 -->

  - **`to-spec`** no longer opens with "you may know this document as a PRD" — the parenthetical is dropped from the skill and its docs page. The local-markdown tracker template drops the same hedge.

  <!-- zh-CN:begin 36c6e140621cfc63 -->

  - **`to-spec`** 不再以“你可能知道此文档叫 PRD”开头，技能及文档页均删除此括注。本地 Markdown 跟踪器模板也删除相同保留说法。

  <!-- zh-CN:end 36c6e140621cfc63 -->
  - **`code-review`** talks about the originating issue/spec rather than issue/PRD, in its frontmatter description, its two-axis summary, and the spec-source search order. Both READMEs re-synced.

  <!-- zh-CN:begin 9bdceb142b80715c -->

  - **`code-review`** 在前置元数据描述、双轴概述和规格来源搜索顺序中，改说原始议题/规格，而非议题/PRD。两个 README 已重新同步。

  <!-- zh-CN:end 9bdceb142b80715c -->
  - **The GitHub and GitLab tracker templates** now say "Issues and specs for this repo live as GitHub/GitLab issues" — they had been left on "PRDs" when the local template was updated, so the stale term propagated into every repo they were written into.

  <!-- zh-CN:begin ee4bbcd422ddc0cd -->

  - **GitHub 和 GitLab 跟踪器模板**现写“此仓库的议题与规格以 GitHub/GitLab 议题形式保存”；更新本地模板时，它们遗留的“PRD”使过时术语传播到了写入模板的每个仓库。

  <!-- zh-CN:end ee4bbcd422ddc0cd -->
  - **`docs/engineering/research.md`** pointed at `https://aihero.dev/skills-to-prd`, a dead slug for the renamed skill; it now links `to-spec` like the other nineteen docs pages do.

  <!-- zh-CN:begin ebf5b593b6d4a2a3 -->

  - **`docs/engineering/research.md`** 曾指向已重命名技能的失效地址 `https://aihero.dev/skills-to-prd`，现与其他十九个文档页一样链接 `to-spec`。

  <!-- zh-CN:end ebf5b593b6d4a2a3 -->

  The CHANGELOG and existing changesets still name PRDs where they document the rename itself, which is correct.

  <!-- zh-CN:begin 38b5429cca9bc855 -->

  CHANGELOG 与现有 changeset 在记录重命名本身时仍提 PRD，这是正确的。

  <!-- zh-CN:end 38b5429cca9bc855 -->

## 1.1.0

### Minor Changes

<!-- zh-CN:begin 4b7f23cae5894733 -->

### 次要变更

<!-- zh-CN:end 4b7f23cae5894733 -->

- [#406](https://github.com/mattpocock/skills/pull/406) [`930a450`](https://github.com/mattpocock/skills/commit/930a450089f77a49af09001d955db8452a4b867d) Thanks [@mattpocock](https://github.com/mattpocock)! - Bring the **`ask-matt`** router up to date with the full skill set. It now maps five skills it was missing: **`tdd`** (woven into the main flow as the red-green engine `implement` drives), **`diagnosing-bugs`** (a new "Something's broken" on-ramp — there was previously no route for a bug), **`domain-modeling`** and **`codebase-design`** (a new "Vocabulary underneath" section), and **`grilling`** (the shared interview primitive). `prototype` is fleshed out as a standalone and the description broadens from "user-invoked skills" to "the skills". A maintenance rule is added to `CLAUDE.md` so any future skill add/rename/remove or flow change triggers an `ask-matt` re-check, beside the existing docs-page re-sync rule.

<!-- zh-CN:begin 2a51f88c59213dd1 -->

- [#406](https://github.com/mattpocock/skills/pull/406) [`930a450`](https://github.com/mattpocock/skills/commit/930a450089f77a49af09001d955db8452a4b867d) 感谢 [@mattpocock](https://github.com/mattpocock)！— 更新 **`ask-matt`** 路由器以覆盖完整技能集。补映射五个遗漏技能：**`tdd`**（融入主流程，作为 `implement` 驱动的红绿引擎）、**`diagnosing-bugs`**（新增“有东西坏了”入口，此前无缺陷路由）、**`domain-modeling`** 和 **`codebase-design`**（新增“底层词汇”部分），以及 **`grilling`**（共享访谈基本单元）。`prototype` 完善为独立技能，描述从“用户调用技能”扩大为“所有技能”。在 `CLAUDE.md` 中，现有文档页同步规则旁新增维护规则：未来新增、重命名、删除技能或流程变更，都触发重查 `ask-matt`。

<!-- zh-CN:end 2a51f88c59213dd1 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) Thanks [@mattpocock](https://github.com/mattpocock)! - Promote and harden **`code-review`**. The in-progress **`review`** skill is renamed to **`code-review`** and moved from `in-progress/` into `engineering/`: it now ships in the plugin, is listed in the top-level and Engineering READMEs (Model-invoked), and has a docs page at `docs/engineering/code-review.md`. The `/implement` skill and docs point at `/code-review`.

<!-- zh-CN:begin 39edb0ce003ca3b5 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！— 将 **`code-review`** 转正并加强它。开发中的 **`review`** 重命名为 **`code-review`**，从 `in-progress/` 移至 `engineering/`，随插件发布，列入顶层与 Engineering README（模型调用），并提供 `docs/engineering/code-review.md` 文档页。`/implement` 技能与文档指向 `/code-review`。

<!-- zh-CN:end 39edb0ce003ca3b5 -->

  It also gains an always-on **Fowler smell baseline** on its Standards axis — a curated ~12 high-signal "Bad Smells in Code" (Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest) inlined into `SKILL.md` as a fixed baseline alongside whatever the repo documents, not a new third axis. Two binding rules keep it safe: a documented repo standard overrides the baseline, and every smell is reported as a judgement call, never a hard violation.

  <!-- zh-CN:begin 901f947f4d307516 -->

  标准轴增加始终启用的 **Fowler 坏味道基线**：精选约 12 个高信号“代码坏味道”（神秘命名、重复代码、依恋情结、数据泥团、基本类型偏执、重复 switch、霰弹式修改、发散式变化、夸夸其谈的通用性、消息链、中间人、被拒绝的遗赠），内联到 `SKILL.md`，与仓库文档标准并列作为固定基线，不是第三条轴。两条约束确保安全：有文档的仓库标准覆盖基线；每个坏味道均以判断意见报告，绝不作为硬性违规。

  <!-- zh-CN:end 901f947f4d307516 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) Thanks [@mattpocock](https://github.com/mattpocock)! - Sharpen **`grilling`** on two fronts.

<!-- zh-CN:begin a252a42ff286f3bf -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！— 从两方面加强 **`grilling`**。

<!-- zh-CN:end a252a42ff286f3bf -->

  **A confirmation gate.** The agent won't enact the plan until you confirm the shared understanding has been reached — turning the skill's existing "shared understanding" completion criterion into an explicit stop-gate. The `description` also recruits the pretrained **`grill`** leading word ("Grill the user relentlessly") to sharpen invocation, and the docs page is re-synced.

  <!-- zh-CN:begin 6eee7a5e0ea043cc -->

  **确认关卡。** 你确认达成共同理解之前，代理不会实施计划，将原有“共同理解”完成标准变成明确停止关卡。`description` 也采用预训练中的 **`grill`** 引导词（“持续深入追问用户”）以提高调用准确性，并同步文档页。

  <!-- zh-CN:end 6eee7a5e0ea043cc -->

  **Facts vs. decisions.** Grilling now splits _facts_ (look them up — explore the codebase) from _decisions_ (put each one to the human and wait for their answer). The old blanket line — "if a question can be answered by exploring the codebase, explore the codebase instead" — was written for the live-human case, but once another skill runs grilling inside a resolve-the-ticket frame it read as license to answer _decisions_ autonomously too. Separating the two keeps a grilling agent from racing ahead and answering its own questions.

  <!-- zh-CN:begin 7dbb139d6a658127 -->

  **事实与决策。** 追问现区分_事实_（查找，探索代码库）和_决策_（逐个交给人类并等回答）。旧的笼统句子“探索代码库能回答的问题，就改为探索代码库”适合真人实时参与的情形；但其他技能在解决工单框架内运行追问时，它被读成也可自主回答_决策_。分开两者可防止追问代理抢先回答自己的问题。

  <!-- zh-CN:end 7dbb139d6a658127 -->

- [#463](https://github.com/mattpocock/skills/pull/463) [`af6d692`](https://github.com/mattpocock/skills/commit/af6d6922c3e2b5288eef155346cbe319e4ed3bd0) Thanks [@mattpocock](https://github.com/mattpocock)! - Add two adjacent Steering failure modes to **`writing-great-skills`**, both about how language you think of as "off" still steers the agent. **Negation** — the _elephant_ — is steering by prohibition: naming what _not_ to do drags the forbidden behaviour into context and makes it _more_ available, not less (_don't think of an elephant_), so the cure is to prompt the **positive**. **Negative Space** — the void — is blindness to the steering done by what you leave _out_: every decision a skill declines is delegated to the agent's priors rather than left neutral, so the cure is to read a draft for its silences and decide each omission deliberately (fill it, or leave it open as a real **branch**). Kept as two entries, not one — they carry different diagnostics and different cures — each a full `GLOSSARY.md` entry plus a `SKILL.md` failure-mode bullet, matching how every other failure mode is carried.

<!-- zh-CN:begin d26293a8fa127744 -->

- [#463](https://github.com/mattpocock/skills/pull/463) [`af6d692`](https://github.com/mattpocock/skills/commit/af6d6922c3e2b5288eef155346cbe319e4ed3bd0) 感谢 [@mattpocock](https://github.com/mattpocock)！— 为 **`writing-great-skills`** 增加两个相邻的引导失败模式，说明你以为“关闭”的语言如何仍引导代理。**否定**——_大象_——通过禁止引导：说出_不要_做什么，将被禁止行为带入上下文，使其_更_容易出现而非更少（_不要想大象_），因此应给出**正面**提示。**负空间**——空白——是看不到_省略_产生的引导：技能拒绝决定的每件事都交给代理先验，并非中立，因此应检查草稿的沉默，对每处省略刻意决定，补全或作为真正**分支**开放。两条保持独立，因诊断和补救不同；各自都有完整 `GLOSSARY.md` 条目和 `SKILL.md` 失败模式项目，与其他条目一致。

<!-- zh-CN:end d26293a8fa127744 -->

- [`850873c`](https://github.com/mattpocock/skills/commit/850873cd73d5f81826ebf512ad35d2b1e113001f) Thanks [@mattpocock](https://github.com/mattpocock)! - Make the **`prototype`** skill model-invoked, so the agent can reach for it autonomously (and other skills can too). Its description is rewritten around the leading word _prototype_ — throwaway code that answers a design question — with one trigger per branch (state/logic sanity-check, or UI exploration).

<!-- zh-CN:begin e717252031e84afa -->

- [`850873c`](https://github.com/mattpocock/skills/commit/850873cd73d5f81826ebf512ad35d2b1e113001f) 感谢 [@mattpocock](https://github.com/mattpocock)！— 让 **`prototype`** 技能可由模型调用，供代理与其他技能自主使用。描述围绕引导词_原型_重写：用完即弃、回答设计问题的代码；每条分支各一个触发条件（状态/逻辑合理性检查，或 UI 探索）。

<!-- zh-CN:end e717252031e84afa -->

- [#409](https://github.com/mattpocock/skills/pull/409) [`0d74d01`](https://github.com/mattpocock/skills/commit/0d74d01cbc64ca27778a49b38599f70c534e76a0) Thanks [@mattpocock](https://github.com/mattpocock)! - Add the **`research`** skill — a small, model-invoked skill that spins up a **background agent** to investigate a question against **primary sources** (official docs, source code, specs, first-party APIs), then leaves a single cited Markdown file wherever the repo keeps such notes. It's delegable reading legwork: you keep working while it reads, and get back a document to grill, plan, or design against. Listed in the top-level and Engineering READMEs (Model-invoked), added to `.claude-plugin/plugin.json`, given a docs page at `docs/engineering/research.md`, and routed as a Standalone in `ask-matt`.

<!-- zh-CN:begin 6f56d1efd582a7de -->

- [#409](https://github.com/mattpocock/skills/pull/409) [`0d74d01`](https://github.com/mattpocock/skills/commit/0d74d01cbc64ca27778a49b38599f70c534e76a0) 感谢 [@mattpocock](https://github.com/mattpocock)！— 新增 **`research`** 技能：由模型调用的小技能，启动**后台代理**，据**一手来源**（官方文档、源码、规格、一方 API）调查问题，在仓库存放此类笔记处留下一个带引用的 Markdown 文件。这是可委派的阅读工作：它阅读时你继续工作，最后得到可用于追问、计划或设计的文档。已列入顶层与 Engineering README（模型调用），加入 `.claude-plugin/plugin.json`，提供 `docs/engineering/research.md` 文档页，并在 `ask-matt` 中作为独立入口路由。

<!-- zh-CN:end 6f56d1efd582a7de -->

- [#469](https://github.com/mattpocock/skills/pull/469) [`a0329ba`](https://github.com/mattpocock/skills/commit/a0329ba95751f58566ed7ab484475917a68f1629) Thanks [@mattpocock](https://github.com/mattpocock)! - Split the **`to-issues`** skill into a lean **Process** and a **Reference** section, and teach it to handle a **wide refactor** — a single mechanical change (like renaming a column) whose **blast radius** fans across the whole codebase, breaking thousands of call sites at once so no vertical slice can land green. The drafting step now points at two co-located reference blocks: the **Vertical slice rules** for ordinary tracer bullets, and **Wide refactors**, which slices the change by **expand–contract** (expand the new form beside the old, migrate call sites in batches sized by blast radius, then contract the old form away) so CI stays green batch to batch — or, when it can't, only at a final integrate-and-verify issue. The issue body template moves into Reference too.

<!-- zh-CN:begin 9ed1e35826532649 -->

- [#469](https://github.com/mattpocock/skills/pull/469) [`a0329ba`](https://github.com/mattpocock/skills/commit/a0329ba95751f58566ed7ab484475917a68f1629) 感谢 [@mattpocock](https://github.com/mattpocock)！— 将 **`to-issues`** 拆成精简**流程**与**参考**部分，新增**广泛重构**支持：单一机械改动（如重命名列）的**影响范围**扩散全库，一次破坏数千调用点，使任何纵向切片均不能独立通过。起草步骤指向同处的两个参考块：普通曳光弹任务的**纵向切片规则**与**广泛重构**；后者按**扩展—收缩**切片（在旧形式旁扩展新形式，按影响范围确定批量迁移调用点的规模，最后收缩移除旧形式），使批次间 CI 通过；无法做到时，则只在最终集成验证议题通过。议题正文模板也移到参考部分。

<!-- zh-CN:end 9ed1e35826532649 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`386d4ff`](https://github.com/mattpocock/skills/commit/386d4ff719a7c420ad1454232d0436b01f1b8c17) Thanks [@mattpocock](https://github.com/mattpocock)! - Unify the planning skills. **`to-prd` is renamed to `to-spec`** — "spec" is now the single through-line term (it still opens with "you may know this document as a PRD" for discoverability). **`to-plan` and `to-issues` are merged into one `to-tickets` skill, and `to-issues` is deleted.**

<!-- zh-CN:begin 8c84fc1afc0c3714 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`386d4ff`](https://github.com/mattpocock/skills/commit/386d4ff719a7c420ad1454232d0436b01f1b8c17) 感谢 [@mattpocock](https://github.com/mattpocock)！— 统一规划技能。**`to-prd` 重命名为 `to-spec`**，“规格”成为贯穿全文的唯一术语（为便于发现，仍以“你可能知道此文档叫 PRD”开头）。**`to-plan` 与 `to-issues` 合并为 `to-tickets`，并删除 `to-issues`。

<!-- zh-CN:end 8c84fc1afc0c3714 -->

  `to-tickets` breaks a plan, spec, or conversation into a set of **tickets** — tracer-bullet vertical slices, each declaring its **blocking edges**. That one artifact reads two ways depending on the tracker `/setup-matt-pocock-skills` configured: a **local file** (`tickets.md`) writes the edges as text and you work it top-to-bottom by hand; a **real tracker** writes them as native blocking links, so any ticket whose blockers are done is on the frontier and several agents can run at once. The edges live in the ticket either way — the medium only decides whether anything acts on them in parallel.

  <!-- zh-CN:begin 7f954c8058956ebb -->

  `to-tickets` 把计划、规格或对话拆成一组**工单**：曳光弹式纵向切片，每张声明**阻塞依赖边**。同一产物按 `/setup-matt-pocock-skills` 配置的跟踪器有两种用法：**本地文件**（`tickets.md`）以文本写依赖，人手从上到下处理；**真实跟踪器**用原生阻塞链接，阻塞项已完成的工单进入前沿，可由多个代理同时执行。两者依赖都存在工单里，媒介只决定是否有机制并行处理它们。

  <!-- zh-CN:end 7f954c8058956ebb -->

  Publishing prefers the tracker's **native sub-issues** for parent → slice and **native blocking edges** for `Blocked by` where the tracker supports them, keeping the `## Parent` / `## Blocked by` body sections as the fallback. The "What to build" template points at where a `/prototype`'s code lives rather than inlining a snippet from it.

  <!-- zh-CN:begin c763f7cb5538d7e4 -->

  发布时，在跟踪器支持的情况下，父项 → 切片优先使用**原生子议题**，`Blocked by` 优先使用**原生阻塞依赖边**，正文中的 `## Parent` / `## Blocked by` 部分作为回退。“构建什么”模板指向 `/prototype` 代码所在位置，而不内联片段。

  <!-- zh-CN:end c763f7cb5538d7e4 -->

  `ask-matt`'s main flow now routes `idea → /to-spec → /to-tickets → /implement`, and there are human-facing docs pages at `docs/engineering/to-spec.md` and `docs/engineering/to-tickets.md`.

  <!-- zh-CN:begin e733a982a01e6690 -->

  `ask-matt` 主流程现为：想法 → `/to-spec` → `/to-tickets` → `/implement`，并提供面向人的 `docs/engineering/to-spec.md` 和 `docs/engineering/to-tickets.md` 文档页。 对应结构：`idea → /to-spec → /to-tickets → /implement`。

  <!-- zh-CN:end e733a982a01e6690 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`0557d57`](https://github.com/mattpocock/skills/commit/0557d57579d9b3d39839fdaf8d4a6542b17539ce) Thanks [@mattpocock](https://github.com/mattpocock)! - Settle wayfinder's place in the docs as a **situational on-ramp**, not the new main entry flow — the grill-led _idea → ship_ chain stays the front door (crowning wayfinder as the default spine is a v2-sized move, not a 1.1). The **`ask-matt`** router now names wayfinder's concrete triggers — a greenfield project or a huge feature build, too big for one session — and the two grill front doors (**`grill-me`**, **`grill-with-docs`**) signpost _up_ to wayfinder for the effort that's too big to hold in one session, so the on-ramp is discoverable from where a reader actually starts.

<!-- zh-CN:begin ae33d514d0b73dc8 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`0557d57`](https://github.com/mattpocock/skills/commit/0557d57579d9b3d39839fdaf8d4a6542b17539ce) 感谢 [@mattpocock](https://github.com/mattpocock)！— 确定 wayfinder 在文档中是**特定情境入口**，而非新的主入口流程；以追问主导的_想法 → 发布_链仍是正门（将 wayfinder 定为默认主线属于 v2 级变化，而非 1.1）。**`ask-matt`** 路由器明确其触发条件：全新项目或巨大功能构建，大到单次会话容不下。两个追问入口 **`grill-me`**、**`grill-with-docs`** 对单次会话无法容纳的工作_向上_指引到 wayfinder，使读者从实际起点就能发现该入口。

<!-- zh-CN:end ae33d514d0b73dc8 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate and reframe **`wayfinder`** — the skill for planning a huge chunk of work, more than one agent session can hold. It moves out of `in-progress/` into `engineering/` (plugin entry, top-level + Engineering READMEs under **User-invoked**, a docs page at `docs/engineering/wayfinder.md`, and a route in `ask-matt`), landing as a mature skill. The rename and reframe that got it there:

<!-- zh-CN:begin a34b2e742243fb81 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！— 将 **`wayfinder`** 转正并重新定位：用于规划单次代理会话无法容纳的大量工作。它从 `in-progress/` 移至 `engineering/`（插件入口、顶层及 Engineering README 的**用户调用**区、`docs/engineering/wayfinder.md` 文档页，以及 `ask-matt` 路由），成为成熟技能。促成转正的重命名与调整如下：

<!-- zh-CN:end a34b2e742243fb81 -->

  - **`decision-mapping` is renamed to `wayfinder`**, invoked as `/wayfinder`. "Decision map" was jargony and inaccurate — only one ticket type is actually a decision. The reframe charts a route through a foggy problem instead, giving one coherent leading-word frame — **fog of war**, **frontier**, **the map** — rather than an invented term layered on top.

  <!-- zh-CN:begin 9b8cc34f2ac40c32 -->

  - **`decision-mapping` 重命名为 `wayfinder`**，通过 `/wayfinder` 调用。“决策地图”术语生硬且不准确，实际只有一种工单类型是决策。新定位是在迷雾问题中绘制路线，以**战争迷雾**、**前沿**、**地图**形成一致引导词框架，而非再叠加自造术语。

  <!-- zh-CN:end 9b8cc34f2ac40c32 -->
  - **Destination as the leading word.** Wayfinding finds the _way_ to a destination; it doesn't charge at building it. Naming the destination is the first act of charting — it fixes the scope and shapes every ticket — so the map gains a `## Destination` field every session orients to, and triage pins it before any ticket exists.

  <!-- zh-CN:begin ced2ca19009b829c -->

  - **目的地作为引导词。** 寻路寻找通往目的地的_路线_，而非直接冲去构建。确定目的地是绘图第一步，界定范围并塑造每张工单，因此地图新增每次会话都遵循的 `## Destination` 字段；分诊在任何工单产生前先确定它。

  <!-- zh-CN:end ced2ca19009b829c -->
  - **Plan, don't do.** The map produces **decisions, not deliverables**; it's done when nothing is left to decide before someone builds the thing. An effort can override this in its Notes.

  <!-- zh-CN:begin b9ed102419d8323d -->

  - **规划，而非执行。** 地图产出**决策而非交付物**；在有人开始构建前，已无待决事项即完成。工作可在 Notes 中覆盖此规定。

  <!-- zh-CN:end b9ed102419d8323d -->
  - **The map is an index, not a store.** A decision lives in exactly one place — its ticket — so the map only gists and links, never restates; graduating fog into a ticket clears the graduated patch so nothing lingers in two places.

  <!-- zh-CN:begin 2f084e18a8f5735b -->

  - **地图是索引而非存储。** 决策只存在一处，即其工单；地图只概述并链接，不复述。迷雾转为工单时清除已转正区域，避免同一内容留在两处。

  <!-- zh-CN:end 2f084e18a8f5735b -->
  - **Collaborative by default.** The map moves off a local Markdown file onto the repo's issue tracker: a single `wayfinder:map` issue whose tickets are its child issues — one shared URL the team can watch. Sessions load the map at low resolution and zoom into tickets on demand. Wayfinder stays tracker-agnostic (GitHub, GitLab, local-markdown) behind a pointer in `docs/agents/issue-tracker.md`, and `setup-matt-pocock-skills` seeds the "Wayfinding operations" section.

  <!-- zh-CN:begin 13085f361d10ddcd -->

  - **默认协作。** 地图从本地 Markdown 移至仓库议题跟踪器：单个 `wayfinder:map` 议题，工单作为其子议题，团队共享关注一个 URL。会话先低分辨率加载地图，按需放大工单。`docs/agents/issue-tracker.md` 中的指针让 wayfinder 保持跟踪器无关（GitHub、GitLab、本地 Markdown），`setup-matt-pocock-skills` 初始化“寻路操作”部分。

  <!-- zh-CN:end 13085f361d10ddcd -->
  - **Claim by assignment, not a label.** A session claims a ticket by assigning it to the driving dev — the assignee _is_ the claim — freeing the label vocabulary to `wayfinder:<type>` alone.

  <!-- zh-CN:begin d42e3b0a6c907f99 -->

  - **通过分配认领，不靠标签。** 会话将工单分配给主持开发者即认领，受理人_就是_认领，从而标签词汇仅需 `wayfinder:<type>`。

  <!-- zh-CN:end d42e3b0a6c907f99 -->
  - **Native blocking.** Blocking prefers the tracker's native dependency relationship, which renders the frontier visually in the tracker's own UI so the human sees what's takeable without opening the map. GitHub and GitLab templates spell out the native recipe, with a body-convention fallback.

  <!-- zh-CN:begin 8a511b7d94dcee35 -->

  - **原生阻塞。** 优先用跟踪器原生依赖关系，在其 UI 中可视化前沿，人无需打开地图即可看出可接任务。GitHub/GitLab 模板明确原生方法，并提供正文约定回退。

  <!-- zh-CN:end 8a511b7d94dcee35 -->
  - **Fog vs. out of scope, split.** Two plainly-named map sections — `## Not yet specified` (in-scope fog that graduates as the frontier advances) and `## Out of scope` (work ruled beyond the destination, closed, never graduating) — so beyond-destination work no longer reads as takeable frontier.

  <!-- zh-CN:begin 6cc97763ece7a24d -->

  - **分开迷雾与范围外。** 两个直白命名的地图区：`## Not yet specified`（范围内迷雾，随前沿推进转为工单）与 `## Out of scope`（超出目的地的工作，已关闭，永不转正），使目的地外的工作不再像可接前沿任务。

  <!-- zh-CN:end 6cc97763ece7a24d -->
  - **A fourth `task` ticket type.** For literal manual work that blocks a decision (provisioning access, moving data, signing up for a service) — the one type that _does_ rather than decides, earning its place by unblocking a decision.

  <!-- zh-CN:begin 0f1f595aa071a664 -->

  - **第四种工单类型 `task`。** 用于阻塞决策的实际人工工作（开通访问、迁移数据、注册服务），是唯一以_执行_而非决策为目标的类型，其存在价值在于解除决策阻塞。

  <!-- zh-CN:end 0f1f595aa071a664 -->
  - **HITL / AFK ticket classification.** Every ticket type is **HITL** (human in the loop — grilling, prototype) or **AFK** (agent alone — research; task is either). A HITL ticket only resolves through the live exchange, so "wait for the human" falls out of the label — a grilling agent that answers its own questions has, by definition, broken HITL. (This fixes students' reports of `/wayfinder` grilling _itself_ instead of the human.)

  <!-- zh-CN:begin 54e936868951cfc9 -->

  - **HITL / AFK 工单分类。** 每种工单属于 **HITL**（人参与：追问、原型）或 **AFK**（代理独立：研究；task 两者皆可）。HITL 只能通过实时交流解决，因此标签本身就意味着“等待人类”；追问代理自问自答按定义已违反 HITL。（修复学员反映 `/wayfinder` 追问_自己_而非人类的问题。）

  <!-- zh-CN:end 54e936868951cfc9 -->
  - **No-fog early exit restored.** If the opening breadth-first grilling surfaces no fog, the journey is small enough for one session — so it stops and asks how you'd like to proceed rather than building a map nobody needs.

  <!-- zh-CN:begin 183ab36ee657be96 -->

  - **恢复无迷雾提前退出。** 开场广度优先追问未发现迷雾，说明单次会话足以容纳，便停止并询问如何继续，而非建立无人需要的地图。

  <!-- zh-CN:end 183ab36ee657be96 -->

### Patch Changes

<!-- zh-CN:begin 32b1ebe22dacc00a -->

### 补丁变更

<!-- zh-CN:end 32b1ebe22dacc00a -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) Thanks [@mattpocock](https://github.com/mattpocock)! - Reshape **`tdd`** into a reference-only skill and add a missing anti-pattern.

<!-- zh-CN:begin db417c419cb92f01 -->

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！— 将 **`tdd`** 调整为纯参考技能，并补上缺失的反模式。

<!-- zh-CN:end db417c419cb92f01 -->

  **Reference-only.** The red → green → refactor loop is anchored by leading words the model already holds, so the step-by-step Workflow was largely restating the loop. Dropped the Workflow and per-cycle checklist; folded their one durable idea — vertical slices / tracer bullets — into the Anti-patterns section and a short Rules-of-the-loop list. Introduced **seam** as the leading word for where tests go: test only at pre-agreed seams, confirmed with the user before any test is written. Also dropped the refactor stage — TDD is now red → green; refactoring belongs to the review stage, so the refactor rule and `refactoring.md` moved out (its home is `code-review`).

  <!-- zh-CN:begin 782089e78e7ce66a -->

  **纯参考。** 红 → 绿 → 重构循环已有模型熟悉的引导词，逐步工作流大体只在复述。删除工作流及每轮检查表，将唯一持久理念（纵向切片/曳光弹）融入反模式与简短循环规则。用**接缝**作为测试位置引导词：只在预先约定且写测试前获用户确认的接缝处测试。还删除重构阶段，TDD 现为红 → 绿；重构属于审查，因此重构规则与 `refactoring.md` 移出，归于 `code-review`。

  <!-- zh-CN:end 782089e78e7ce66a -->

  **Tautological tests.** Added the tautological-test anti-pattern: a test whose assertion is recomputed the way the code computes it passes by construction and gives zero confidence — distinct from the implementation-coupling anti-pattern already covered. Added as a peer at the same sites: a Philosophy principle (expected values must come from an independent source of truth), a checklist gate, and a BAD/GOOD example pair in `tests.md`.

  <!-- zh-CN:begin 2b866819669d3f66 -->

  **同义反复测试。** 新增反模式：以代码自身相同算法重算断言的测试，天然通过，完全不增加信心；不同于已有的实现耦合反模式。在相同位置增加并列条目：理念原则（预期值必须源自独立事实来源）、检查表关卡，以及 `tests.md` 中的错误/正确示例对。

  <!-- zh-CN:end 2b866819669d3f66 -->

- [`e00eadb`](https://github.com/mattpocock/skills/commit/e00eadb4bb32c3d5a631ead1a5ed5d6a7c5f74e2) Thanks [@mattpocock](https://github.com/mattpocock)! - Extend the **`triage`** skill to triage external pull requests, treating a PR as an issue with attached code that runs through the same roles and state machine. PRs flow inline alongside issues (gated by a per-repo setup toggle), discovery surfaces only external PRs, the bug-only "reproduce" step is generalized into a single "verify the claim" step, and a redundancy check resolves already-implemented requests to `wontfix` without polluting the out-of-scope knowledge base. `setup-matt-pocock-skills` gains the PRs-as-a-request-surface toggle for GitHub/GitLab.

<!-- zh-CN:begin d5f020948e1682a4 -->

- [`e00eadb`](https://github.com/mattpocock/skills/commit/e00eadb4bb32c3d5a631ead1a5ed5d6a7c5f74e2) 感谢 [@mattpocock](https://github.com/mattpocock)！— 扩展 **`triage`**，支持外部 PR 分诊：视作附带代码的议题，经过相同角色和状态机。PR 与议题同列流转，由每仓库设置开关控制；发现阶段只展示外部 PR；仅用于缺陷的“复现”推广为统一“验证主张”；冗余检查将已实现请求归为 `wontfix`，不污染范围外知识库。`setup-matt-pocock-skills` 新增 GitHub/GitLab 的 PR 请求入口开关。

<!-- zh-CN:end d5f020948e1682a4 -->

- [#472](https://github.com/mattpocock/skills/pull/472) [`d869d45`](https://github.com/mattpocock/skills/commit/d869d45afc32beab1c2d1350f8de5e81589512cd) Thanks [@mattpocock](https://github.com/mattpocock)! - Fix **`wayfinder`** hardcoding the issue-tracker doc path, which broke the indirection the rest of the suite relies on.

<!-- zh-CN:begin cf56a69259ba81f7 -->

- [#472](https://github.com/mattpocock/skills/pull/472) [`d869d45`](https://github.com/mattpocock/skills/commit/d869d45afc32beab1c2d1350f8de5e81589512cd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 修复 **`wayfinder`** 硬编码议题跟踪器文档路径，破坏其余技能套件依赖的间接寻址问题。

<!-- zh-CN:end cf56a69259ba81f7 -->

  `to-issues`, `to-prd`, and `triage` never name a path — they resolve the tracker through the `### Issue tracker` block that `setup-matt-pocock-skills` writes into `CLAUDE.md` / `AGENTS.md`, which points at the tracker doc wherever it lives. Wayfinder instead pinned the literal `docs/agents/issue-tracker.md`, so in a repo that keeps its agent docs elsewhere it silently fell back to the local-markdown tracker — even one whose `CLAUDE.md` clearly declares GitHub issues. It now resolves the doc via that same pointer and reads its "Wayfinding operations" section by name, keeping the indirection consistent across the suite.

  <!-- zh-CN:begin 16751fc371c4ad72 -->

  `to-issues`、`to-prd`、`triage` 不指定路径，而通过 `setup-matt-pocock-skills` 写入 `CLAUDE.md` / `AGENTS.md` 的 `### Issue tracker` 块解析跟踪器，该块指向任意位置的跟踪器文档。wayfinder 却固定 `docs/agents/issue-tracker.md`，使代理文档存放他处的仓库静默回退到本地 Markdown，即使 `CLAUDE.md` 明确声明 GitHub 议题。现在也经同一指针解析文档，再按名称读取“寻路操作”部分，使套件间接寻址一致。

  <!-- zh-CN:end 16751fc371c4ad72 -->

## 1.0.1

### Patch Changes

<!-- zh-CN:begin c01ecbcfc701cec5 -->

### 补丁变更

<!-- zh-CN:end c01ecbcfc701cec5 -->

- [`d20ee26`](https://github.com/mattpocock/skills/commit/d20ee2684e2a9442698ac3c1e0f2c5b68c4cf296) Thanks [@mattpocock](https://github.com/mattpocock)! - Make the **`teach`** skill reuse-first. Lessons are now built from reusable **components** in `./assets/` — stylesheets, quiz widgets, simulators, diagram helpers. Reuse is the default: the agent reads `./assets/` before authoring a lesson, builds from what's there, and extracts anything new and reusable into a component rather than inlining it.

<!-- zh-CN:begin 65b423c1dea76f94 -->

- [`d20ee26`](https://github.com/mattpocock/skills/commit/d20ee2684e2a9442698ac3c1e0f2c5b68c4cf296) 感谢 [@mattpocock](https://github.com/mattpocock)！— 让 **`teach`** 优先复用。课程现在使用 `./assets/` 中可复用**组件**：样式表、测验控件、模拟器、图示辅助。代理编写课程前先读取 `./assets/`，用现有内容构建，任何新增可复用内容提取为组件，而不内联。

<!-- zh-CN:end 65b423c1dea76f94 -->

## 1.0.0

### Major Changes

<!-- zh-CN:begin f3708fd3cc85a1bb -->

### 重大变更

<!-- zh-CN:end f3708fd3cc85a1bb -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Add the **`ask-matt`** skill — a user-invoked router that points you at the right skill or flow for your situation.

<!-- zh-CN:begin 46e9b33edc7b976d -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 新增 **`ask-matt`**：用户调用的路由器，按情境指向正确技能或流程。

<!-- zh-CN:end 46e9b33edc7b976d -->

  **Breaking:** `ask-matt` routes over the other user-invoked skills in this repo, so it expects them to be installed.

  <!-- zh-CN:begin 41419161401cfc87 -->

  **破坏性变化：** `ask-matt` 为仓库其他用户调用技能提供路由，因此要求已安装它们。

  <!-- zh-CN:end 41419161401cfc87 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Add the shared design skills and rewire existing skills onto them.

<!-- zh-CN:begin 33bd93ac6c4d41a6 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 新增共享设计技能，并将现有技能改接到它们。

<!-- zh-CN:end 33bd93ac6c4d41a6 -->

  - New **`codebase-design`** skill — the deep-module vocabulary (module, interface, depth, seam, adapter) and the principles for putting a lot of behaviour behind a small interface. The language that previously lived in `improve-codebase-architecture/LANGUAGE.md` now lives here, generalized for reuse across skills.

  <!-- zh-CN:begin a8fc207655c177a1 -->

  - 新增 **`codebase-design`**：深模块词汇（模块、接口、深度、接缝、适配器），以及用小接口封装大量行为的原则。原在 `improve-codebase-architecture/LANGUAGE.md` 的语言现移至此处，泛化供技能间复用。

  <!-- zh-CN:end a8fc207655c177a1 -->
  - New **`domain-modeling`** skill — actively build and sharpen a project's domain model, stress-testing terms against the glossary and keeping `CONTEXT.md` and ADRs current.

  <!-- zh-CN:begin 3b6e62765be1477a -->

  - 新增 **`domain-modeling`**：主动构建完善项目领域模型，对照术语表压力检验术语，使 `CONTEXT.md` 和 ADR 保持最新。

  <!-- zh-CN:end 3b6e62765be1477a -->
  - `improve-codebase-architecture` now draws its architecture vocabulary from `/codebase-design` and its domain model from `/domain-modeling`.

  <!-- zh-CN:begin 1f7ff3f559f76cb7 -->

  - `improve-codebase-architecture` 现从 `/codebase-design` 获取架构词汇，从 `/domain-modeling` 获取领域模型。

  <!-- zh-CN:end 1f7ff3f559f76cb7 -->
  - `tdd` now leans on `/codebase-design` for interface-design guidance — its inline `deep-modules.md` / `interface-design.md` notes were removed in favour of the shared skill.

  <!-- zh-CN:begin 5022798c140daa6e -->

  - `tdd` 现依赖 `/codebase-design` 的接口设计指导；内联 `deep-modules.md` / `interface-design.md` 笔记已删除，改用共享技能。

  <!-- zh-CN:end 5022798c140daa6e -->
  - `grill-with-docs` now builds the domain model inline via `/domain-modeling`.

  <!-- zh-CN:begin f03ce0e9275810bb -->

  - `grill-with-docs` 现通过 `/domain-modeling` 在流程中构建领域模型。

  <!-- zh-CN:end f03ce0e9275810bb -->

  **Breaking:** these skills now depend on the new `codebase-design` / `domain-modeling` skills, so you must install them too.

  <!-- zh-CN:begin 1b413865770f3127 -->

  **破坏性变化：** 这些技能依赖新增的 `codebase-design` / `domain-modeling`，必须同时安装。

  <!-- zh-CN:end 1b413865770f3127 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Remove the **`caveman`** and **`zoom-out`** skills.

<!-- zh-CN:begin 5e4a897584c299b3 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 移除 **`caveman`** 与 **`zoom-out`** 技能。

<!-- zh-CN:end 5e4a897584c299b3 -->

  - `caveman` was a duplicate of another skill I was testing and was never meant to be public.

  <!-- zh-CN:begin 5d1ca025d741d4a3 -->

  - `caveman` 是我测试另一技能时的重复项，从未打算公开。

  <!-- zh-CN:end 5d1ca025d741d4a3 -->
  - `zoom-out` went unused in practice, so it's been removed from the repo.

  <!-- zh-CN:begin 403b3200d907b3b3 -->

  - `zoom-out` 实际无人使用，因此从仓库移除。

  <!-- zh-CN:end 403b3200d907b3b3 -->

  **Breaking:** both skills have been removed.

  <!-- zh-CN:begin ae102d05fb580f8c -->

  **破坏性变化：** 两技能均已移除。

  <!-- zh-CN:end ae102d05fb580f8c -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Rename the **`diagnose`** skill to **`diagnosing-bugs`**.

<!-- zh-CN:begin 2af1a2bce8874837 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 将 **`diagnose`** 重命名为 **`diagnosing-bugs`**。

<!-- zh-CN:end 2af1a2bce8874837 -->

  **Breaking:** invoke it as `/diagnosing-bugs` — the old `/diagnose` name no longer exists.

  <!-- zh-CN:begin 42b24dc20d024aa5 -->

  **破坏性变化：** 改用 `/diagnosing-bugs`；旧 `/diagnose` 名称不再存在。

  <!-- zh-CN:end 42b24dc20d024aa5 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Replace **`write-a-skill`** with **`writing-great-skills`**.

<!-- zh-CN:begin 699c88161dbfbdba -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 以 **`writing-great-skills`** 替代 **`write-a-skill`**。

<!-- zh-CN:end 699c88161dbfbdba -->

  - Removed `write-a-skill`.

  <!-- zh-CN:begin 101d2e80ecb5b095 -->

  - 已移除 `write-a-skill`。

  <!-- zh-CN:end 101d2e80ecb5b095 -->
  - Added `writing-great-skills` (plus its `GLOSSARY.md`) — a reference for writing and editing skills well: the vocabulary and principles that make a skill predictable, hunting no-ops down to the sentence level.

  <!-- zh-CN:begin 913a00d75e232a27 -->

  - 新增 `writing-great-skills` 及其 `GLOSSARY.md`：用于良好编写编辑技能的参考，包含使技能可预测的词汇与原则，逐句找出无效指令。

  <!-- zh-CN:end 913a00d75e232a27 -->
  - Exposed `grilling` as a model-invoked skill — the reusable interview loop behind `grill-me` and `grill-with-docs`.

  <!-- zh-CN:begin dbcfec1aca2812d1 -->

  - 将 `grilling` 开放为模型调用技能，即 `grill-me` 与 `grill-with-docs` 背后可复用的访谈循环。

  <!-- zh-CN:end dbcfec1aca2812d1 -->

  **Breaking:** `write-a-skill` has been removed; use `writing-great-skills` instead.

  <!-- zh-CN:begin d01e33a8592cd5b7 -->

  **破坏性变化：** `write-a-skill` 已移除，改用 `writing-great-skills`。

  <!-- zh-CN:end d01e33a8592cd5b7 -->

### Minor Changes

<!-- zh-CN:begin eb9347e768e8df7d -->

### 次要变更

<!-- zh-CN:end eb9347e768e8df7d -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Add the **`resolving-merge-conflicts`** skill — a loop for resolving an in-progress git merge or rebase conflict. Standalone, with no dependencies on other skills.

<!-- zh-CN:begin dfb5556e6d0a4d28 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 新增 **`resolving-merge-conflicts`**，循环解决进行中的 git merge 或 rebase 冲突。独立使用，不依赖其他技能。

<!-- zh-CN:end dfb5556e6d0a4d28 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Rename the skill taxonomy from **Commands / Skills** to **User-invoked / Model-invoked** across the docs, and add `docs/invocation.md` defining the split: user-invoked skills are reachable only when you type them and exist to orchestrate; model-invoked skills can also be reached automatically when the task fits. A user-invoked skill may invoke model-invoked skills, but never another user-invoked one.

<!-- zh-CN:begin 85e1704ce6393a7b -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 在所有文档中将技能分类从**命令/技能**改为**用户调用/模型调用**，新增 `docs/invocation.md` 定义差异：用户调用技能只能通过手动输入到达，用于编排；模型调用技能也可在任务适合时自动到达。用户调用技能可调用模型调用技能，绝不可调用另一用户调用技能。

<!-- zh-CN:end 85e1704ce6393a7b -->

### Patch Changes

<!-- zh-CN:begin 7edaeb042d117ff2 -->

### 补丁变更

<!-- zh-CN:end 7edaeb042d117ff2 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) Thanks [@mattpocock](https://github.com/mattpocock)! - Tighten the **`review`** skill: fail-fast ref check, single-sourced rules, and no-op cuts.

<!-- zh-CN:begin 1c30f030f421a766 -->

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！— 收紧 **`review`**：快速失败引用检查、单一来源规则、删除无效步骤。

<!-- zh-CN:end 1c30f030f421a766 -->
