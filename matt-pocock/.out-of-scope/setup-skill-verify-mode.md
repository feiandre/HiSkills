# Verify/Check Mode for `setup-matt-pocock-skills`

<!-- zh-CN:begin 8ffb3e11ecefffe3 -->

# `setup-matt-pocock-skills` 的验证／检查模式

<!-- zh-CN:end 8ffb3e11ecefffe3 -->

This project will not add a dedicated verify/check mode (or a separate verify skill) for `setup-matt-pocock-skills`.

<!-- zh-CN:begin 81041a01bd6f0cbb -->

本项目不会为 `setup-matt-pocock-skills` 添加专门的验证／检查模式或独立验证技能。

<!-- zh-CN:end 81041a01bd6f0cbb -->

## Why this is out of scope

<!-- zh-CN:begin ecea9d70cb658a97 -->

## 为什么不在范围内

<!-- zh-CN:end ecea9d70cb658a97 -->

A second skill (or a `--verify` flag) for checking whether `docs/agents/*.md` artifacts still match the seed-template schema would duplicate work the existing setup skill already handles in conversation.

<!-- zh-CN:begin 7608c15f84d60931 -->

再做一个技能（或 `--verify` 标志）检查 `docs/agents/*.md` 产物是否仍匹配种子模板模式，会重复现有设置技能已经在对话中处理的工作。

<!-- zh-CN:end 7608c15f84d60931 -->

The intended workflow is: **run `/setup-matt-pocock-skills` and tell it to verify your current setup.** The skill is prompt-driven, so the maintainer can scope it to a verification pass ("don't rewrite anything, just check my existing files against the current seed templates and report drift") without needing a separate code path. Adding a flag or a sibling skill would split the surface area of a feature that's already expressible through the natural-language entry point.

<!-- zh-CN:begin 65ac4b87986a906f -->

预期工作流是：**运行 `/setup-matt-pocock-skills`，并告诉它验证当前设置。** 技能由提示驱动，维护者可以把范围限定为一次验证（“不要重写任何内容，只用当前种子模板检查现有文件并报告漂移”），无需单独代码路径。添加标志或同级技能会分裂这个已经能通过自然语言入口表达的功能表面。

<!-- zh-CN:end 65ac4b87986a906f -->

Keeping configuration management to a single skill also avoids the maintenance cost of two skills drifting from each other when seed templates evolve.

<!-- zh-CN:begin b27dc505420de7ac -->

把配置管理保留在单一技能中，也避免种子模板演进时两个技能相互漂移的维护成本。

<!-- zh-CN:end b27dc505420de7ac -->

## Prior requests

<!-- zh-CN:begin acb586e1ea8e2b98 -->

## 此前请求

<!-- zh-CN:end acb586e1ea8e2b98 -->

- #106: Feature request: verify/check mode for setup-matt-pocock-skills

<!-- zh-CN:begin a4484fc6282238b0 -->

- #106：功能请求：为 setup-matt-pocock-skills 添加验证／检查模式

<!-- zh-CN:end a4484fc6282238b0 -->
