技能按主题桶放在 `skills/` 目录下：

- `engineering/`：日常代码工作

- `productivity/`：日常非代码工作流工具

- `misc/`：保留但少用，不推广

- `in-progress/`：测试版；有意公开，欢迎反馈，不随插件发布

- `deprecated/`：不再使用

`engineering/` 或 `productivity/`（**推广桶**）中的每个技能都必须在顶层 `README.md` 中引用，并列入 `.claude-plugin/plugin.json` 的 `skills` 数组（Claude Code 插件只发布推广集合）。`misc/`、`in-progress/`、`deprecated/` 技能不得出现在这两处。

安装命令从 [.agents/install-block.md](./.agents/install-block.md) 逐字复制。`.claude-plugin/marketplace.json` 是仓库自己的市场；除 Claude Code 外的代理通过它获得自动更新，Claude Code 使用 `claude-plugins-official`。修改任一清单后运行 `claude plugin validate . --strict`。[ADR 0002](./.agents/adr/0002-ship-as-a-claude-code-plugin.md) 记录原因。

顶层 `README.md` 中每个技能条目都必须把技能名链接到其 `SKILL.md`。

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`. The promoted buckets' `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked**; non-promoted bucket `README.md`s (`misc/`, `in-progress/`) use a flat list.

每个主题桶的 `README.md` 列出桶内所有技能及一行描述，并把名称链接到 `SKILL.md`。推广桶的 `README.md` 及顶层 `README.md` 将条目分为**用户调用**和**模型调用**；未推广桶的 `README.md`s（`misc/`、`in-progress/`）使用平铺列表。

Skills in `engineering/` and `productivity/` also have a human-facing docs page at `docs/<bucket>/<skill-name>.md` (the docs tree mirrors those two bucket folders under `skills/`). The published URL is `https://aihero.dev/skills-<skill-name>` regardless of bucket: the docs path is repo organisation only. When you add, rename, or change the behaviour of a skill in `engineering/` or `productivity/`, create or re-sync its docs page following [.agents/writing-docs.md](./.agents/writing-docs.md). A finished page carries four sections: **What it does**, **When to reach for it**, **Common questions**, and **It's working if**. `writing-docs.md` holds the template, the section order, and where to hunt for the questions. Skills in the non-promoted buckets (`misc/`, `in-progress/`, `deprecated/`) get **no** docs page. The one exception is a promoted skill removed outright: its page stays, marked archived (see `writing-docs.md`).

`engineering/` 与 `productivity/` 技能还有面向人的文档页 `docs/<bucket>/<skill-name>.md`（文档树在 `skills/` 下镜像 `engineering/` 与 `productivity/` 两个桶）。发布 URL 始终为 `https://aihero.dev/skills-<skill-name>`，与桶无关；文档路径仅用于仓库组织。新增、重命名或改变这两个桶技能行为时，按 [.agents/writing-docs.md](./.agents/writing-docs.md) 创建或同步文档页。完成页面包含四节：**它做什么**、**何时使用**、**常见问题**、**怎样算正常工作**。`writing-docs.md` 含模板、节顺序及问题查找位置。未推广桶（`misc/`、`in-progress/`、`deprecated/`）**不**生成文档页；唯一例外是完全移除的推广技能，其页面保留并标为归档（见 `writing-docs.md`）。

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, reachable only by the human) or model-invoked (model- or user-reachable). See [.agents/invocation.md](./.agents/invocation.md).

每个 `SKILL.md` 要么是用户调用（前置元数据 `disable-model-invocation: true`，且 `agents/openai.yaml` 中 `policy.allow_implicit_invocation: false`，只能由人到达），要么是模型调用（模型或用户可到达）。见 [.agents/invocation.md](./.agents/invocation.md)。

[`ask-matt`](./skills/engineering/ask-matt/SKILL.md) is the router that maps every user-reachable skill and how they relate. The same trigger that re-syncs a docs page applies to it: whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read `ask-matt`'s `SKILL.md` and update it so the map stays accurate: a new skill it never mentions, or a stale one it still routes to, is a router that lies.

[`ask-matt`](./skills/engineering/ask-matt/SKILL.md) 是映射所有用户可到达技能及其关系的路由器。同样，当你使用 `ask-matt` 时，新增、重命名、移除或改变用户可到达技能如何进入流程时，重新阅读并更新其 `SKILL.md`，保持地图准确；遗漏新技能或仍路由过时技能，都是错误路由。

To (re)link every skill outside `deprecated/` and `misc/` into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`), run `scripts/link-skills.sh`. Each entry is a symlink into this repo, so a `git pull` keeps installed skills current; re-run the script after adding, removing, or renaming a skill.

要将 `deprecated/` 和 `misc/` 外的技能重新链接到本地代理技能目录（`~/.claude/skills`、`~/.agents/skills`），运行 `scripts/link-skills.sh`。每个条目是指向仓库的符号链接，`git pull` 可保持已安装技能最新；新增、删除或重命名技能后重跑脚本。

No em-dashes anywhere in this repo's prose (`SKILL.md` files, docs, `README.md`, `CHANGELOG.md`, ADRs, changesets, code comments). Where a sentence reaches for one, rewrite it instead with a comma, colon, period, parentheses, or a conjunction, whichever the sentence actually wants; never do a blind character substitution.

本仓库所有说明文字（`SKILL.md`、文档、`README.md`、`CHANGELOG.md`、ADR、changeset、代码注释）不得使用长破折号。需要时按句子实际需要改成逗号、冒号、句号、括号或连词，绝不机械替换字符。

Every skill that dispatches a subagent says to start it with a fresh context window. Some harnesses (Codex, for one) fork the parent conversation by default, and a fork inherits the parent's context, which is what the subagent was meant to escape.

每个派发子代理的技能都应说明以全新上下文窗口启动它。某些平台（例如 Codex）默认 fork 父对话，fork 会继承父上下文，而子代理本应摆脱它。

## Agent skills

## 代理技能

### Triage labels

### 分诊标签

Canonical names, unchanged. See `docs/agents/triage-labels.md`. Issues are judged against [`SCOPE.md`](./SCOPE.md).

规范名称不变。见 `docs/agents/triage-labels.md`。议题按 [`SCOPE.md`](./SCOPE.md) 判断。

