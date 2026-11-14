# Lazy-loading `writing-for-agents` in skills that judge agent-facing writing

<!-- zh-CN:begin c6a3ddafc8557288 -->

# 在判断面向代理写作的技能中延迟加载 `writing-for-agents`

<!-- zh-CN:end c6a3ddafc8557288 -->

`retro` loads `writing-for-agents` on every run, not only before it writes. Requests to defer that load until the skill edits a skill, an `AGENTS.md`/`CLAUDE.md` or a doc are out of scope.

<!-- zh-CN:begin 75c9ca07e902c513 -->

`retro` 每次运行都加载 `writing-for-agents`，不仅在写之前。要求延迟到技能编辑技能、`AGENTS.md`/`CLAUDE.md` 或文档时才加载的请求不在范围。

<!-- zh-CN:end 75c9ca07e902c513 -->

## Why this is out of scope

<!-- zh-CN:begin c30ec7fbc82b69cb -->

## 为什么不在范围

<!-- zh-CN:end c30ec7fbc82b69cb -->

`writing-for-agents` is more than a style guide. It defines what a no-op instruction is and what makes a good skill, and `retro` uses those definitions to judge the steering files it reads, before it writes anything. A retro that only reads and reports still needs it. Load it lazily and the No-ops and Skills candidates get judged with no yardstick.

<!-- zh-CN:begin b2bab1517040a060 -->

`writing-for-agents` 不只是风格指南。它定义什么是无效指令、什么构成好技能，`retro` 写入前就用这些定义判断所读指导文件。即使只读并报告，也需要它。延迟加载会让 No-ops 和 Skills 候选失去判断尺度。

<!-- zh-CN:end b2bab1517040a060 -->

## Prior requests

<!-- zh-CN:begin 6c89d4035baf02d8 -->

## 以往请求

<!-- zh-CN:end 6c89d4035baf02d8 -->

- #1238: "retro: load writing-for-agents only before writing" (closed)

<!-- zh-CN:begin 134ffcbbbcd1fe9c -->

- #1238：“retro：仅在写之前加载 writing-for-agents”（已关闭）

<!-- zh-CN:end 134ffcbbbcd1fe9c -->
