# Ship the skill set as a native Claude Code plugin; defer a native Codex plugin

<!-- zh-CN:begin 7f44beec09d155fb -->

# 将技能集作为原生 Claude Code 插件发布；暂缓原生 Codex 插件

<!-- zh-CN:end 7f44beec09d155fb -->

These skills have always been installable via [skills.sh](https://skills.sh/mattpocock/skills) (`npx skills add mattpocock/skills`), which copies editable skill files into a user's project across Claude Code, Codex, and other Agent-Skills-standard harnesses. A recurring request is a **plug-and-play** distribution: subscribe to the set as a read-only, always-current bundle you don't edit, rather than a fork you own. That is exactly what native plugin systems provide.

<!-- zh-CN:begin aeb9d0a37e0e7989 -->

这些技能一直可通过 [skills.sh](https://skills.sh/mattpocock/skills)（`npx skills add mattpocock/skills`）安装，它会把可编辑技能复制到 Claude Code、Codex 及其他 Agent-Skills 标准宿主的项目。常见请求是**即插即用**分发：订阅只读且始终最新、无需编辑的包，而非自己拥有的分叉。原生插件系统正好提供这一点。

<!-- zh-CN:end aeb9d0a37e0e7989 -->

We ship a native **Claude Code plugin** and, for now, **defer** a native **Codex plugin**. The split is forced by how each ecosystem's plugin manifest selects skills, against this repo's bucketed layout.

<!-- zh-CN:begin 02e8906754770668 -->

我们发布原生 **Claude Code 插件**，目前**暂缓**原生 **Codex 插件**。原因是两个生态的插件清单选择技能方式不同，与本仓库的分桶布局冲突。

<!-- zh-CN:end 02e8906754770668 -->

## The constraint: bucketed skills vs. single-path selection

<!-- zh-CN:begin 07dfbffbb4917caf -->

## 约束：分桶技能与单路径选择

<!-- zh-CN:end 07dfbffbb4917caf -->

Skills live in bucket folders under `skills/`: `engineering/` and `productivity/` are **promoted** (shipped); `misc/`, `personal/`, `in-progress/`, and `deprecated/` are **not**. A plugin must expose only the promoted set, which spans two of those bucket folders.

<!-- zh-CN:begin fc00b4128614317e -->

技能位于 `skills/` 的分桶目录：`engineering/` 和 `productivity/` 是**已晋升**（发布）的；`misc/`、`personal/`、`in-progress/` 和 `deprecated/` 不发布。插件只能暴露已晋升集，而它们跨两个分桶。

<!-- zh-CN:end fc00b4128614317e -->

- **Claude Code**: `.claude-plugin/plugin.json` accepts `skills` as an **array of explicit skill-directory paths**. We list the promoted skills one by one, exclude everything else with zero ambiguity, and add `.claude-plugin/marketplace.json` so the repo is its own single-plugin marketplace. Verified end to end: `claude plugin validate . --strict` passes, and `marketplace add` → `install` resolves all promoted skills.

<!-- zh-CN:begin ce400cc4e3e5e894 -->

- **Claude Code**：`.claude-plugin/plugin.json` 的 `skills` 接受**显式技能目录路径数组**。逐项列出已晋升技能，明确排除其他内容，并添加 `.claude-plugin/marketplace.json` 让仓库成为单插件市场。端到端验证：`claude plugin validate . --strict` 通过，`marketplace add`→`install` 解析全部已晋升技能。

<!-- zh-CN:end ce400cc4e3e5e894 -->

- **Codex**: `.codex-plugin/plugin.json` accepts `skills` only as a **single path string** (arrays are rejected with `missing or invalid plugin.json`), and Codex discovers `SKILL.md` files recursively under it. There is no way to name two bucket folders, or to curate a subset, from one path. Two escape hatches were tested and rejected:

<!-- zh-CN:begin bdae52f6f6eb7ca8 -->

- **Codex**：`.codex-plugin/plugin.json` 只接受**单个路径字符串**作为 `skills`（数组会被拒绝并报 `missing or invalid plugin.json`），Codex 在该路径下递归发现 `SKILL.md`。一个路径无法指定两个桶或精选子集。测试后拒绝两条绕路：

<!-- zh-CN:end bdae52f6f6eb7ca8 -->
  - Pointing at `./skills/` would also ship `deprecated/`, `in-progress/`, `personal/`, and `misc/`: retired, draft, and personal skills we deliberately don't promote.

  <!-- zh-CN:begin 1a9cbc2fa4e3767c -->

  - 指向 `./skills/` 会连同 `deprecated/`、`in-progress/`、`personal/` 和 `misc/` 一起发布（已退役、草稿和私人技能）。

  <!-- zh-CN:end 1a9cbc2fa4e3767c -->
  - A curated flat directory of **symlinks** into the buckets does not survive install: Codex copies the plugin tree into its cache and **drops symlinks**, so the skills arrive empty.

  <!-- zh-CN:begin b3f698086cfd204f -->

  - 用**符号链接**构建精选扁平目录也无法通过安装：Codex 把插件树复制到缓存并**丢弃符号链接**，技能成为空目录。

  <!-- zh-CN:end b3f698086cfd204f -->

The only robust ways to give Codex a single promoted-only path are (a) **restructure** so `skills/` contains only promoted skills (moving the non-promoted buckets out, a large blast radius across `CLAUDE.md`, `scripts/link-skills.sh`, the bucket READMEs, and the local dev workflow that relies on `in-progress/` and `personal/`), or (b) **commit duplicate copies** of promoted skills into a flat directory (a sync burden and a second source of truth). Both are structural decisions, not something to bundle into shipping the Claude plugin. This is very likely the original, half-remembered reason a plugin wasn't shipped earlier: the manifest formats didn't cleanly express a curated subset of a bucketed repo.

<!-- zh-CN:begin c04bb05ad549f271 -->

给 Codex 单一路径且仅含已晋升技能的稳妥方案：(a) **重构**，让 `skills/` 只含已晋升技能（移走其他分桶，会影响 `CLAUDE.md`、`scripts/link-skills.sh`、各 README 和依赖 `in-progress/`、`personal/` 的本地开发流程），或 (b) **提交重复副本**到扁平目录（增加同步负担和第二个真相来源）。两者都是结构决策，不宜夹带进 Claude 插件发布。这很可能正是早先未发布插件的原始原因：清单格式无法清楚表达分桶仓库的精选子集。

<!-- zh-CN:end c04bb05ad549f271 -->

## Decision

<!-- zh-CN:begin 55d447eda979f8ac -->

## 决定

<!-- zh-CN:end 55d447eda979f8ac -->

- Ship the **Claude Code plugin** now (`.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`), curated to the promoted set, as the headline v1.2 deliverable.

<!-- zh-CN:begin 067f1a8bee429d9c -->

- 立即发布**Claude Code 插件**（`.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`），精选已晋升集，作为 v1.2 主要交付。

<!-- zh-CN:end 067f1a8bee429d9c -->
- Keep **skills.sh** as the universal installer: it already serves Codex and other harnesses today, so no Codex user is left without an install path.

<!-- zh-CN:begin 26368672ceb59fd1 -->

- 保留 **skills.sh** 作为通用安装器：它已服务 Codex 和其他宿主，Codex 用户仍有安装途径。

<!-- zh-CN:end 26368672ceb59fd1 -->
- **Defer** the native Codex plugin until we decide between restructuring `skills/` to promoted-only vs. committing a generated flat copy. Revisit when Codex either supports a `skills` array / include-list or preserves symlinks on install.

<!-- zh-CN:begin 6ac86c92bf95c692 -->

- **暂缓**原生 Codex 插件，先决定重构 `skills/` 仅含晋升技能，还是提交生成的扁平副本。等 Codex 支持 `skills` 数组/包含清单，或安装时保留符号链接，再重审。

<!-- zh-CN:end 6ac86c92bf95c692 -->

## Invariants this creates

<!-- zh-CN:begin eaaaaa52dd1535d3 -->

## 由此建立的不变量

<!-- zh-CN:end eaaaaa52dd1535d3 -->

- Every promoted skill has an entry in `.claude-plugin/plugin.json`'s `skills` array (this already stood as a `CLAUDE.md` rule; it now also gates the plugin's contents).

<!-- zh-CN:begin 830f9cf62996ca34 -->

- 每个已晋升技能在 `.claude-plugin/plugin.json` 的 `skills` 数组有入口；这已是 `CLAUDE.md` 规则，现在也控制插件内容。

<!-- zh-CN:end 830f9cf62996ca34 -->
- `.claude-plugin/plugin.json`'s `version` tracks `package.json`'s version: bump both together on release. Claude uses the plugin `version` to decide when installed users see an update.

<!-- zh-CN:begin 4a972fb602ffe4a4 -->

- `.claude-plugin/plugin.json` 的 `version` 跟随 `package.json` 版本，发布时一起提升。Claude 用插件 `version` 判断已安装用户何时看到更新。

<!-- zh-CN:end 4a972fb602ffe4a4 -->

## Update, 2026-08-05

<!-- zh-CN:begin 6a9bb86c838e8a3d -->

## 更新，2026-08-05

<!-- zh-CN:end 6a9bb86c838e8a3d -->

`mattpocock-skills` was accepted into **Claude Code's official marketplace** (configured name `claude-plugins-official`, source repo `anthropics/claude-plugins-official`), which every Claude Code install has by default. `claude plugins install mattpocock-skills` is now the documented route, and the `marketplace add` → `install` path above is superseded. The install wording lives in [.agents/install-block.md](../install-block.md).

<!-- zh-CN:begin b2bcefde3de4d532 -->

`mattpocock-skills` 已进入 **Claude Code 官方市场**（名 `claude-plugins-official`，源仓库 `anthropics/claude-plugins-official`），所有 Claude Code 安装默认带有。现在文档路径为 `claude plugins install mattpocock-skills`，上述 `marketplace add`→`install` 已被取代；安装文案位于 [.agents/install-block.md](../install-block.md)。

<!-- zh-CN:end b2bcefde3de4d532 -->

The official listing points at this repo's git URL and reads `.claude-plugin/plugin.json` directly, so it does not depend on `.claude-plugin/marketplace.json`. That file is retained only as a fallback for installing the repo directly (an unreleased commit, or a fork).

<!-- zh-CN:begin 870c817d0c0c4443 -->

官方条目指向本仓库 git URL 并直接读取 `.claude-plugin/plugin.json`，不依赖 `.claude-plugin/marketplace.json`。该文件仅作为直接安装仓库（未发布提交或分叉）时的回退。

<!-- zh-CN:end 870c817d0c0c4443 -->

Verified 2026-08-05, on Claude Code 2.1.222, against the live listing:

<!-- zh-CN:begin e7be45c923c25db1 -->

2026-08-05 在 Claude Code 2.1.222 对线上条目验证：

<!-- zh-CN:end e7be45c923c25db1 -->

- `claude plugins install mattpocock-skills` resolves with no marketplace added first, and reports `mattpocock-skills@claude-plugins-official`.

<!-- zh-CN:begin 19988ebe93e963ac -->

- 未先添加市场，`claude plugins install mattpocock-skills` 即解析，并报告 `mattpocock-skills@claude-plugins-official`。

<!-- zh-CN:end 19988ebe93e963ac -->
- `claude plugin details mattpocock-skills` then reports version 1.2.0 and loads the promoted skills.

<!-- zh-CN:begin eaceb270b3e8e16a -->

- `claude plugin details mattpocock-skills` 显示 1.2.0 并加载已晋升技能。

<!-- zh-CN:end eaceb270b3e8e16a -->
- The listing's `source` is `{"source": "url", "url": "https://github.com/mattpocock/skills.git", "sha": …}`: the **sha is pinned**, so a release reaches installed users when that pin moves, not the moment we tag. At the time of writing the pin sits two commits behind `main`, which is why it lists 22 skills rather than the 24 in `plugin.json`.

<!-- zh-CN:begin 1dfcf32089848474 -->

- 条目的 `source` 为 `{"source": "url", "url": "https://github.com/mattpocock/skills.git", "sha": …}`；**sha 被固定**，只有 pin 移动时已安装用户才收到版本，打 tag 不会立即生效。写作时 pin 落后 `main` 两个提交，因此列出 22 个技能，而 `plugin.json` 中有 24 个。

<!-- zh-CN:end 1dfcf32089848474 -->
- The in-session `/plugin install mattpocock-skills` was **not** exercised: `/plugin` is unavailable in headless (`claude -p`) sessions. It runs the same resolver as the CLI, and the documented example form is `/plugin install <name>@claude-plugins-official`.

<!-- zh-CN:begin f09e0154eb811718 -->

- 未测试会话中的 `/plugin install mattpocock-skills`：无头（`claude -p`）会话无 `/plugin`。它运行与 CLI 相同的解析器，文档示例为 `/plugin install <name>@claude-plugins-official`。

<!-- zh-CN:end f09e0154eb811718 -->

## Update, 2026-10-07

<!-- zh-CN:begin 8a52fedab801bbd4 -->

## 更新，2026-10-07

<!-- zh-CN:end 8a52fedab801bbd4 -->

The Codex constraint above no longer holds. Codex `main` accepts a `skills` string array and falls back to `.claude-plugin/` when there is no `.codex-plugin/` ([manifest.rs](https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/manifest.rs)). Codex still drops symlinks.

<!-- zh-CN:begin bbd43350eb2d8cfe -->

上述 Codex 限制已消失。Codex `main` 接受 `skills` 字符串数组，无 `.codex-plugin/` 时回退 `.claude-plugin/`（[manifest.rs](https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/manifest.rs)）。Codex 仍丢弃符号链接。

<!-- zh-CN:end bbd43350eb2d8cfe -->

On Codex 0.161.0, the `@mattpocock` marketplace install loads the promoted model-invoked skills and nothing from `misc/` or `in-progress/`. Copilot CLI reads the same manifests and reports "Installed 27 skills".

<!-- zh-CN:begin a5009bf825cca448 -->

在 Codex 0.161.0 上，`@mattpocock` 市场安装会加载已晋升的模型调用技能，不加载 `misc/` 或 `in-progress/`。Copilot CLI 读取同一清单并报告“Installed 27 skills”（安装 27 个技能）。

<!-- zh-CN:end a5009bf825cca448 -->

## Update, 2026-10-08: managed installs first

<!-- zh-CN:begin ff962d6e8d80d6bd -->

## 更新，2026-10-08：托管安装优先

<!-- zh-CN:end ff962d6e8d80d6bd -->

`@mattpocock` is now the lead route on Codex, Copilot and VS Code, at the cost of a one-time opt-in on Copilot. Claude Code stays on `claude-plugins-official`, as in the 2026-08-05 update, because it auto-updates by default and needs no `marketplace add`.

<!-- zh-CN:begin 4b6b5f83258af162 -->

`@mattpocock` 已成为 Codex、Copilot 和 VS Code 的首选路线，代价是 Copilot 需一次性选择加入。Claude Code 仍用 `claude-plugins-official`（如 2026-08-05 更新），因为它默认自动更新，无需执行 `marketplace add`。

<!-- zh-CN:end 4b6b5f83258af162 -->

The version invariant above now applies to every managed route. `npm run version` already keeps it by running `scripts/sync-plugin-version.mjs`. `marketplace.json` has no `version` field, so it can't drift.

<!-- zh-CN:begin 609062360fb03624 -->

上述版本不变量现在适用于各托管路线。`npm run version` 已通过 `scripts/sync-plugin-version.mjs` 保持同步。`marketplace.json` 没有 `version` 字段，因此不会漂移。

<!-- zh-CN:end 609062360fb03624 -->
