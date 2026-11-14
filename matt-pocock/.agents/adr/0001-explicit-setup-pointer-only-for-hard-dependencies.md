# Explicit `/setup-matt-pocock-skills` pointer only for hard dependencies

<!-- zh-CN:begin c477355d59035705 -->

# 仅为硬依赖提供明确的 `/setup-matt-pocock-skills` 指针

<!-- zh-CN:end c477355d59035705 -->

Engineering skills depend on per-repo config (issue tracker, triage label vocabulary, domain doc layout) seeded by `/setup-matt-pocock-skills`. Some skills cannot meaningfully function without that config: they have to publish to a specific issue tracker or apply a specific label string. Others only use it to sharpen output (vocabulary, ADR awareness) and degrade gracefully without it.

<!-- zh-CN:begin ae5d9f7fe53cffd6 -->

工程技能依赖由 `/setup-matt-pocock-skills` 播种的逐仓库配置（issue 跟踪器、分诊标签词汇、领域文档布局）。有些技能没有该配置便无法有意义工作：必须发布到特定 issue 跟踪器或应用特定标签字符串。其他技能只用它改善输出（词汇、ADR 意识），缺少时能平稳降级。

<!-- zh-CN:end ae5d9f7fe53cffd6 -->

We split these into **hard-dependency** and **soft-dependency** skills:

<!-- zh-CN:begin 4c314638c3b91e8f -->

我们将它们分为**硬依赖**与**软依赖**技能：

<!-- zh-CN:end 4c314638c3b91e8f -->

- **Hard dependency** (`to-tickets`, `to-spec`, `triage`): include an explicit one-liner: _"… should have been provided to you; run `/setup-matt-pocock-skills` if not."_ Without the mapping, output is wrong, not just fuzzy.

<!-- zh-CN:begin 55feebcea2866c58 -->

- **硬依赖**（`to-tickets`、`to-spec`、`triage`）：包含明确一行：_“……本应已提供给你；若没有，请运行 `/setup-matt-pocock-skills`。”_ 没有映射时输出是错误，而不只是模糊。

<!-- zh-CN:end 55feebcea2866c58 -->
- **Soft dependency** (`diagnose`, `tdd`, `improve-codebase-architecture`): reference "the project's domain glossary" and "ADRs in the area you're touching" in vague prose only. If the docs aren't there, the skill still works; output is just less sharp.

<!-- zh-CN:begin 9f0863fd97e0636a -->

- **软依赖**（`diagnose`、`tdd`、`improve-codebase-architecture`）：只在模糊正文中提及“项目领域术语表”和“你触及区域的 ADR”。文档不存在时技能仍工作，只是输出稍不敏锐。

<!-- zh-CN:end 9f0863fd97e0636a -->

The split keeps soft-dependency skills token-light and avoids cargo-culting the setup pointer into places where it isn't load-bearing.

<!-- zh-CN:begin 00b78c88ff338346 -->

这种拆分让软依赖技能保持轻 token，并避免把设置指针照搬到并不承重的地方。

<!-- zh-CN:end 00b78c88ff338346 -->
