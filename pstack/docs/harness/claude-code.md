# pstack in Claude Code

<!-- zh-CN:begin cfca79a004716b21 -->

# Claude Code 中的 pstack

<!-- zh-CN:end cfca79a004716b21 -->

pstack skills use Cursor names. In Claude Code, read this file once per session, then map each Cursor name in a skill with the tables below. `<pstack>` means the folder that holds `skills/` and `docs/`. If a Cursor field has no row, drop it and say so. Never pass a field or value the tool schema rejects.

<!-- zh-CN:begin fc0eb636f567e8e7 -->

pstack技能使用Cursor名称。Claude Code中每会话读取一次本文件，并按表格把技能中的Cursor名称映射到Claude Code。`<pstack>`指包含`skills/`和`docs/`的目录。Cursor字段无对应项就删除并说明；绝不传入schema拒绝的字段或值。

<!-- zh-CN:end fc0eb636f567e8e7 -->

## Tools

<!-- zh-CN:begin efd53932375594fe -->

## 工具

<!-- zh-CN:end efd53932375594fe -->

| Cursor | Claude Code |
| --- | --- |
| `Task` | `Agent` |
| `AskQuestion` | `AskUserQuestion`. In `-p` mode it is absent, so ask in plain text. |
| Open a todolist | Use `TodoWrite` if the session offers it. Otherwise keep the list in your reply and update it at each phase. |
| Run another pstack skill (`/name` or "the **name** skill") | `Read` `<pstack>/skills/<name>/SKILL.md` and follow it. The `Skill` tool refuses most pstack skills. When you tell the user to type it, write `/pstack:<name>`. |
| `Grep`, `Glob` | `Bash` with `rg` when the session has no `Grep` or `Glob`. |

<!-- zh-CN:begin 5b3adce91962dd2f -->

| Cursor | Claude Code |
| --- | --- |
| `Task` | `Agent` |
| `AskQuestion` | `AskUserQuestion`；`-p`模式没有此工具，改用纯文本提问。 |
| 打开待办列表 | 有`TodoWrite`就用，否则在回复中维护并在每阶段更新。 |
| 运行另一pstack技能（`/name`或“**name**技能”） | 用`Read`读取`<pstack>/skills/<name>/SKILL.md`并遵循；`Skill`工具拒绝多数pstack技能。让用户输入`/pstack:<name>`。 |
| `Grep`、`Glob` | 用`Bash`执行`rg`。 | 本节涉及的标识包括 `Grep`、`Glob`。

<!-- zh-CN:end 5b3adce91962dd2f -->

## Subagent fields

<!-- zh-CN:begin 8df08fbb585b7780 -->

## 子代理字段

<!-- zh-CN:end 8df08fbb585b7780 -->

| Cursor | Claude Code |
| --- | --- |
| `subagent_type: generalPurpose` | `subagent_type: "general-purpose"` |
| `poteto-agent`, `comment-sicko` | `pstack:poteto-agent`, `pstack:comment-sicko` |
| `readonly: true` | `subagent_type: "Explore"`. It keeps `Bash`, so the brief also says "do not edit files", and you check `git status` afterward. |
| `readonly: false` | `general-purpose`. It keeps the session's MCP servers. |
| `environment: "cloud"` | `isolation: "worktree"`. Name the branch or commit the worker checks out. |
| `environment: "local"` | Omit. |
| `cloud_base_branch: <b>` | Tell the worker to check out `<b>` first. |
| `run_in_background: true` | Omit. Subagents run in the background by default and notify you when they finish. |
| `resume` | Spawn a new agent and paste the earlier result into its brief. |
| `file_attachments` | List the paths in the brief. |

<!-- zh-CN:begin bfd381aa2b4d3689 -->

| Cursor | Claude Code |
| --- | --- |
| `subagent_type: generalPurpose` | `subagent_type: "general-purpose"` |
| `poteto-agent`、`comment-sicko` | 加`pstack:`前缀。 |
| `readonly: true` | 用`subagent_type: "Explore"`；简报要求不编辑，事后检查`git status`。 |
| `readonly: false` | 用`general-purpose`，保留MCP服务器。 |
| `environment: "cloud"` | 用`isolation: "worktree"`并写明分支或提交。 |
| `environment: "local"` | 省略。 |
| `cloud_base_branch: <b>` | 要求先检出`<b>`。 |
| `run_in_background: true` | 省略；默认后台运行并通知。 |
| `resume` | 派生新代理并在简报粘贴旧结果。 |
| `file_attachments` | 简报列出路径。 | 本节涉及的标识包括 `pstack:poteto-agent`、`pstack:comment-sicko`、`Bash`。

<!-- zh-CN:end bfd381aa2b4d3689 -->

## Models

<!-- zh-CN:begin 4ac95bba70f47960 -->

## 模型

<!-- zh-CN:end 4ac95bba70f47960 -->

| Cursor | Claude Code |
| --- | --- |
| `claude-<family>-<version>-<effort>[-fast]`, such as `claude-opus-5-5-xhigh` | `model: "opus"` and `effort: "xhigh"`. `model` takes only `opus`, `sonnet`, `haiku`, `fable`. Drop `-fast`. |
| A `grok-*`, `gpt-*`, or other non-Claude slug | Omit `model` so the agent runs on the session model, and say so. |
| `auto` or `inherit-parent` | Omit `model`. |
| The `pstack-models.mdc` rule, `~/.cursor/rules/pstack-models.mdc` | `~/.claude/rules/pstack-models.md`. Claude Code loads it into every new session, so its role lines are already in context. If they are not, read the file. If the file or the role's line is missing, use the skill's default slug. |
| A role value `<model> <effort>`, such as `opus high` | `model: "opus"` and `effort: "high"`. |

<!-- zh-CN:begin 35ec97b993aa559a -->

| Cursor | Claude Code |
| --- | --- |
| `claude-<family>-<version>-<effort>[-fast]` | 拆为`model: "opus"`等和独立`effort`；删除`-fast`。 |
| `grok-*`、`gpt-*`或其他非Claude标识 | 省略`model`并说明使用会话模型。 |
| `auto`、`inherit-parent` | 省略`model`。 |
| `pstack-models.mdc`、`~/.cursor/rules/pstack-models.mdc` | 用`~/.claude/rules/pstack-models.md`；角色行缺失时读取文件，仍缺失则用技能默认值。 |
| 角色值`<model> <effort>` | 拆成`model`和`effort`。 | 本节涉及的标识包括 `claude-opus-5-5-xhigh`、`model: "opus"`、`effort: "xhigh"`、`opus`、`sonnet`、`haiku`、`fable`、`opus high`、`effort: "high"`。

<!-- zh-CN:end 35ec97b993aa559a -->

## setup-pstack

<!-- zh-CN:begin 72e33ed55735a277 -->

## setup-pstack 设置

<!-- zh-CN:end 72e33ed55735a277 -->

Claude Code loads every `.md` file in `~/.claude/rules/` into each new session, so `setup-pstack` writes its rule there. Follow its steps with these changes:

<!-- zh-CN:begin ca3b3b0cf8f14dc2 -->

Claude Code加载`~/.claude/rules/`中的所有`.md`，因此`setup-pstack`把规则写在那里：

<!-- zh-CN:end ca3b3b0cf8f14dc2 -->

- Detect. The detected models are the `model` values that the `Agent` tool schema lists, each with an effort from its `effort` values. Write a real model as `<model> <effort>`, such as `opus xhigh`. The effort is the last token, so the budget step works as written.

<!-- zh-CN:begin a337c43075c46c44 -->

- 检测：模型的`model`与`effort`来自`Agent` schema；写成`<model> <effort>`，如`opus xhigh`，最后一个token是effort。

<!-- zh-CN:end a337c43075c46c44 -->
- Defaults. Map each default slug with the rows above: `claude-opus-5-5-xhigh` is `opus xhigh`, and `grok-4.7-xhigh-fast` is `inherit-parent`.

<!-- zh-CN:begin 9456668635ce3bcd -->

- 默认映射：`claude-opus-5-5-xhigh`为`opus xhigh`，`grok-4.7-xhigh-fast`为`inherit-parent`。

<!-- zh-CN:end 9456668635ce3bcd -->
- Write. Write `~/.claude/rules/pstack-models.md` with no frontmatter, then the comment lines, the `# budget` line, and one line per role from step 5. Overwrite the whole file. Never put the role lines in `CLAUDE.md` or `AGENTS.md`.

<!-- zh-CN:begin 92cc5698f3a40009 -->

- 写入：创建`~/.claude/rules/pstack-models.md`，无frontmatter，随后注释、`# budget`和每角色一行；覆盖整文件，绝不放`CLAUDE.md`/`AGENTS.md`。

<!-- zh-CN:end 92cc5698f3a40009 -->

## Paths

<!-- zh-CN:begin 97525e0888b6478c -->

## 路径

<!-- zh-CN:end 97525e0888b6478c -->

| Cursor | Claude Code |
| --- | --- |
| `.cursor/skills/`, `~/.cursor/skills/` | `.claude/skills/`, `~/.claude/skills/` |
| `~/.cursor/plugins/`, `.cursor-plugin/plugin.json` | `~/.claude/plugins/`, `.claude-plugin/plugin.json` |
| `.cursor/rules/*.mdc`, always-applied rules | `CLAUDE.md`, or `AGENTS.md` when no `CLAUDE.md` exists. Claude Code never reads `.mdc` files. The model rule is the exception. See Models. |
| `https://github.com/cursor/plugins/blob/main/pstack/<path>` | `<pstack>/<path>` when that file exists. The plugin ships the skills, `docs/guide/`, and `README.md`. Read the local copy and never fetch it. Give the user the URL when they need a link. |
| Transcripts in `~/.cursor/projects/<slug>/agent-transcripts/` | `~/.claude/projects/<slug>/<session>.jsonl`. The slug is the workspace path with each `/` and `.` changed to `-`, so `/Users/you/proj` is `-Users-you-proj`. The newest `.jsonl` directly in that folder is the current session. Its `<session>/subagents/` folder holds subagent transcripts. Read only this workspace's folder. |

<!-- zh-CN:begin c1cbd1346ea28f74 -->

| Cursor | Claude Code |
| --- | --- |
| `.cursor/skills/`、`~/.cursor/skills/` | `.claude/skills/`、`~/.claude/skills/` |
| `~/.cursor/plugins/`、`.cursor-plugin/plugin.json` | `.claude-plugin/plugin.json`等Claude路径。 |
| `.cursor/rules/*.mdc`、始终应用规则 | `CLAUDE.md`或`AGENTS.md`；除模型规则外Claude不读`.mdc`。 |
| `https://github.com/cursor/plugins/blob/main/pstack/<path>` | 文件存在时用`<pstack>/<path>`；读本地副本，不抓取。 |
| `~/.cursor/projects/<slug>/agent-transcripts/` | `~/.claude/projects/<slug>/<session>.jsonl`；最新文件为当前会话，子代理在`<session>/subagents/`；只读本工作区。 | 本节涉及的标识包括 `~/.claude/plugins/`、`CLAUDE.md`、`docs/guide/`、`README.md`、`/`、`.`、`-`、`/Users/you/proj`、`-Users-you-proj`、`.jsonl`。

<!-- zh-CN:end c1cbd1346ea28f74 -->

## Cursor-only features

<!-- zh-CN:begin d87a6d80e7c4b552 -->

## 仅 Cursor 的功能

<!-- zh-CN:end d87a6d80e7c4b552 -->

Claude Code has no Cursor Automations, Bugbot, Cursor cloud agents, or built-in PR tool. When a step needs one, put one line in your reply, `Skipped in Claude Code: <step>. <reason>.`, then go on to the next step. Do not stop, ask, or retry. When a later step needs what the skipped step made, such as a URL or a key, leave a placeholder and name it in the line.

<!-- zh-CN:begin 350fbc8bc2f6ba5f -->

Claude Code没有Cursor Automations、Bugbot、Cursor云代理或内置PR工具。需要时回复`Skipped in Claude Code: <step>. <reason>.`并继续，不停止、询问或重试；后续依赖其产物时留下并命名占位符。

<!-- zh-CN:end 350fbc8bc2f6ba5f -->

| Cursor | Claude Code |
| --- | --- |
| Cursor Automations: routines, `update_state` routine calls, `api2.cursor.sh/automations` webhooks, routine wakes, and `SendToUser` secret requests | Skip with the line. |
| Bugbot | Bugbot comments on a GitHub PR are ordinary review threads, so triage them with the forge command that the step gives. Skip a step that starts, waits for, or configures Bugbot when the PR has no Bugbot check or comment. |
| Cursor cloud agents | `environment: "cloud"` maps to a worktree, as in Subagent fields. Skip a step that needs the cloud agent itself, such as its dashboard status or its own machine. |
| A built-in PR tool | Use the forge command that the step gives, such as `gh pr create`. That is not a skip, so write no line. |

<!-- zh-CN:begin 8277fd5d810c00c7 -->

| Cursor | Claude Code |
| --- | --- |
| Automations、routines、`update_state`、webhook、`SendToUser`密钥 | 说明后跳过。 |
| Bugbot | GitHub PR评论按普通审查线程处理；没有检查或评论时跳过相关配置步骤。 |
| 云代理 | `environment: "cloud"`映射工作树；依赖代理自身的步骤跳过。 |
| 内置PR工具 | 使用`gh pr create`等forge命令，不算跳过。 | 本节涉及的标识包括 `api2.cursor.sh/automations`。

<!-- zh-CN:end 8277fd5d810c00c7 -->
