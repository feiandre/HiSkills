# Issue tracker integrations: GitHub, GitLab and local markdown only

<!-- zh-CN:begin 1cbb17b065b7c127 -->

# 问题跟踪器集成：仅 GitHub、GitLab 和本地 Markdown

<!-- zh-CN:end 1cbb17b065b7c127 -->

`setup-matt-pocock-skills` offers first-class support for exactly three issue trackers, one per seed template in `skills/engineering/setup-matt-pocock-skills/`:

<!-- zh-CN:begin fdf43944270bfa40 -->

`setup-matt-pocock-skills` 为一等支持恰好三种问题跟踪器，对应 `skills/engineering/setup-matt-pocock-skills/` 中的三个种子模板：

<!-- zh-CN:end fdf43944270bfa40 -->

- **GitHub** (`issue-tracker-github.md`, via `gh`)

<!-- zh-CN:begin 4d6129b9d9e9ad2c -->

- **GitHub**（`issue-tracker-github.md`，通过 `gh`）

<!-- zh-CN:end 4d6129b9d9e9ad2c -->
- **GitLab** (`issue-tracker-gitlab.md`, via `glab`)

<!-- zh-CN:begin 8209ba256700d18a -->

- **GitLab**（`issue-tracker-gitlab.md`，通过 `glab`）

<!-- zh-CN:end 8209ba256700d18a -->
- **Local markdown** (`issue-tracker-local.md`, files under `.scratch/`)

<!-- zh-CN:begin 1f7d829dd556693c -->

- **本地 Markdown**（`issue-tracker-local.md`，文件位于 `.scratch/` 下）

<!-- zh-CN:end 1f7d829dd556693c -->

Requests to add a first-class backend for any other tracker are out of scope. That includes Jira, Linear, Azure DevOps, Trello, YouTrack, and new agent-focused trackers.

<!-- zh-CN:begin 7b0c9ed7f0d65aba -->

为其他跟踪器增加一等后端的请求不在范围内，包括 Jira、Linear、Azure DevOps、Trello、YouTrack 和新的智能体专用跟踪器。

<!-- zh-CN:end 7b0c9ed7f0d65aba -->

## Why this is out of scope

<!-- zh-CN:begin d1db540e1177720c -->

## 为什么不在范围内

<!-- zh-CN:end d1db540e1177720c -->

Every issue-tracker backend hard-codes a CLI shape into the skills (commands, flags, output parsing). Each new backend is permanent maintenance surface, because it has to keep working as the tool's CLI evolves, and it has to keep being tested against `/to-spec`, `/to-tickets`, `/triage`, and friends. I use GitHub, so that's the backend I can actually keep correct. GitLab is close enough in shape to ride along, and local markdown needs no CLI at all.

<!-- zh-CN:begin 2f8a049f5a31a62b -->

每个问题跟踪器后端都会把 CLI 形状硬编码进技能（命令、标志、输出解析）。每个新后端都是长期维护面，因为工具 CLI 演进时它必须继续工作，也必须持续针对 `/to-spec`、`/to-tickets`、`/triage` 等技能测试。我使用 GitHub，因此这是我能真正保持正确的后端。GitLab 形状接近，可以并行支持；本地 Markdown 根本不需要 CLI。

<!-- zh-CN:end 2f8a049f5a31a62b -->

Popularity doesn't change this. Jira is widely used and has an official CLI (`acli`), and it still isn't getting a template: it's a backend I don't run, with its own link semantics, workflow states and CLI quirks to keep tested. The cost lands on me whether or not the tool is mainstream.

<!-- zh-CN:begin 57deef726dee39a1 -->

流行度不改变这一点。Jira 使用广泛且有官方 CLI `acli`，仍不会得到模板：它是我不会运行的后端，需要持续测试其链接语义、工作流状态和 CLI 特性。无论工具是否主流，成本都由我承担。

<!-- zh-CN:end 57deef726dee39a1 -->

Every other tracker goes through the **Other** option in `/setup-matt-pocock-skills`: you describe your workflow in a paragraph and the skill records it as prose in `docs/agents/issue-tracker.md`. That file is yours. If you've refined a Jira or Linear workflow that works, keep it in your own repo or publish it, and point the setup at it.

<!-- zh-CN:begin 6764ca01eace59c0 -->

其他跟踪器都通过 `/setup-matt-pocock-skills` 的 **Other** 选项：你用一段话描述工作流，技能把它记录为 `docs/agents/issue-tracker.md` 中的文字。该文件属于你。若你完善了可用的 Jira 或 Linear 工作流，可在自己仓库保留或发布，并让设置指向它。

<!-- zh-CN:end 6764ca01eace59c0 -->

## Prior requests

<!-- zh-CN:begin f8b01aa3c22a73c3 -->

## 先前请求

<!-- zh-CN:end f8b01aa3c22a73c3 -->

- #99: "Add dex as an issue tracker backend" (dex was ~3 months old and ~300 stars at the time of the request)

<!-- zh-CN:begin a70e0b365303f936 -->

- #99：“添加 dex 作为问题跟踪器后端”（请求时 dex 约 3 个月大、约 300 stars）

<!-- zh-CN:end a70e0b365303f936 -->
- #258: "Add Jira as first-class issue tracker via Rovo MCP"

<!-- zh-CN:begin 176a613eb849c1c6 -->

- #258：“通过 Rovo MCP 将 Jira 添加为一等问题跟踪器”

<!-- zh-CN:end 176a613eb849c1c6 -->
- #1137: "Add Jira as a first-class issue tracker, via Atlassian's official CLI (`acli`)"

<!-- zh-CN:begin 6a633aefe53e03af -->

- #1137：“通过 Atlassian 官方 CLI（`acli`）将 Jira 添加为一等问题跟踪器”

<!-- zh-CN:end 6a633aefe53e03af -->
