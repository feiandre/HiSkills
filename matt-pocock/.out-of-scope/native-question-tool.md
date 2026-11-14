# Grilling through the harness's native question tool

<!-- zh-CN:begin 455930046668c14b -->

# 通过宿主原生命题工具进行 grilling

<!-- zh-CN:end 455930046668c14b -->

Grilling sessions (`/grilling`, `/grill-me`, `/grill-with-docs`, and grilling inside other skills) ask their questions as plain chat text. Requests to route them through a harness's built-in question UI (Claude Code's `AskUserQuestion`, a host "question tool", a structured or batched questionnaire mode) are out of scope.

<!-- zh-CN:begin 9894500ab66609b1 -->

Grilling 会话（`/grilling`、`/grill-me`、`/grill-with-docs` 及其他技能内部的 grilling）以普通聊天文字提问。将这些请求路由到宿主内置提问 UI（Claude Code 的 `AskUserQuestion`、宿主的“question tool”、结构化或批量问卷模式）不在范围内。

<!-- zh-CN:end 9894500ab66609b1 -->

## Why this is out of scope

<!-- zh-CN:begin 36ee667e68c604f1 -->

## 为何不在范围内

<!-- zh-CN:end 36ee667e68c604f1 -->

The skills are harness-neutral text. They run in Claude Code, Codex, Copilot, Cursor and anything else skills.sh installs into, and each harness has a different question tool, or none. Naming one harness's tool in the skill means either a harness-specific branch in every grilling skill, or a skill that only works properly in one place.

<!-- zh-CN:begin e6c75599904568b3 -->

这些技能是与宿主无关的文本。它们运行在 Claude Code、Codex、Copilot、Cursor 以及 skills.sh 可安装的任何环境中，而各宿主有不同的提问工具，或完全没有。在技能中点名某宿主的工具，会让每个 grilling 技能都有宿主专用分支，或使技能只在一个地方正常。

<!-- zh-CN:end e6c75599904568b3 -->

The question UI also changes the grilling itself. Structured pickers push the model towards multiple-choice questions with pre-baked answers, which is the opposite of what grilling is for: open questions you answer in your own words, one branch of the decision tree at a time. I've tried the `AskUserQuestion` UI and don't want it in these skills.

<!-- zh-CN:begin 75883c7869088803 -->

提问 UI 也会改变 grilling 本身。结构化选择器会推动模型使用预置答案的多选题，这与 grilling 的目的相反：你用自己的话回答开放问题，一次一个决策树分支。我试过 `AskUserQuestion` UI，不想在技能中使用它。

<!-- zh-CN:end 75883c7869088803 -->

If you prefer your harness's question tool, say so in your own `CLAUDE.md` / `AGENTS.md` ("when grilling, ask via AskUserQuestion"). That's a one-line, per-user preference, and it doesn't need the shared skill to know about it.

<!-- zh-CN:begin 3037eba2c5fea136 -->

若偏好宿主的提问工具，在你自己的 `CLAUDE.md` / `AGENTS.md` 中说明（“grilling 时通过 AskUserQuestion 提问”）。这只是一行逐用户偏好，不需要共享技能知道。

<!-- zh-CN:end 3037eba2c5fea136 -->

## Prior requests

<!-- zh-CN:begin 010d1f015d238fa8 -->

## 先前请求

<!-- zh-CN:end 010d1f015d238fa8 -->

- #19: "grill-me: not always using the question tool"

<!-- zh-CN:begin c64d1d1bf7bd251f -->

- #19：“grill-me：并非始终使用提问工具”

<!-- zh-CN:end c64d1d1bf7bd251f -->
- #643: "Proposal: Use AskQuestion for structured input during grilling sessions"

<!-- zh-CN:begin 6a246a745175504a -->

- #643：“提案：在 grilling 会话中使用 AskQuestion 接收结构化输入”

<!-- zh-CN:end 6a246a745175504a -->
- #840: "Use host's question tool for grilling sessions"

<!-- zh-CN:begin 25559ce17f0b65af -->

- #840：“在 grilling 会话中使用宿主的提问工具”

<!-- zh-CN:end 25559ce17f0b65af -->
- #1107: "Grilling doesn't use Agent's native QA tool OOTB"

<!-- zh-CN:begin 8208d8710627d430 -->

- #1107：“Grilling 默认不使用 Agent 原生 QA 工具”

<!-- zh-CN:end 8208d8710627d430 -->
- #1152: "Proposal: experimental HTML questionnaire mode for batch grilling"

<!-- zh-CN:begin 17c87ce42fb9ecac -->

- #1152：“提案：用于批量 grilling 的实验性 HTML 问卷模式”

<!-- zh-CN:end 17c87ce42fb9ecac -->
