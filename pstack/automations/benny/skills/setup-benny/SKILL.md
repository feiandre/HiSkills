---
name: setup-benny
description: Configure Benny and prepare its triage and repro automations. Use when installing Benny or changing its Slack, tracker, repository, routing, control, model, or budget settings.
disable-model-invocation: true

# zh-CN:begin b4bd525c89662645
# name: setup-benny
# description: "配置 Benny，并准备它的分诊和复现自动化。安装 Benny 或更改其 Slack、跟踪器、仓库、路由、控制、模型或预算设置时使用。"
# disable-model-invocation: true
# zh-CN:end b4bd525c89662645
---

# Set up Benny

<!-- zh-CN:begin fb9c72cca9e020a7 -->

# 设置 Benny

<!-- zh-CN:end fb9c72cca9e020a7 -->

Benny ships as a dormant automation pack inside pstack. The plugin manifest exposes only pstack's normal skill root; this file and the two operational files are not slash skills.

<!-- zh-CN:begin ff0336c448a04ef2 -->

Benny 作为一个休眠自动化包随 pstack 提供。插件清单仅公开 pstack 常规的技能根目录；本文件和两个操作文件都不是斜杠技能。

<!-- zh-CN:end ff0336c448a04ef2 -->

The human enters setup by pointing Cursor at the pack's `FOR_AGENTS.md`. The bootstrap flow copies the whole pack into the target repository, then reads this file directly at `.cursor/automations/benny/skills/setup-benny/SKILL.md`.

<!-- zh-CN:begin 9771ac80005b849d -->

人类通过让 Cursor 指向包内的 `FOR_AGENTS.md` 进入设置流程。引导流程把整个包复制进目标仓库，然后在 `.cursor/automations/benny/skills/setup-benny/SKILL.md` 直接读取本文件。

<!-- zh-CN:end 9771ac80005b849d -->

Benny needs external configuration and two live Cursor automations.

<!-- zh-CN:begin 6fde38065e3c4ff8 -->

Benny 需要外部配置，以及两个实际运行的 Cursor 自动化。

<!-- zh-CN:end 6fde38065e3c4ff8 -->

Do not create or update an automation until the user explicitly asks. Never put a secret value in plugin files, prompts, or committed configuration.

<!-- zh-CN:begin e2f9a504e13cf5af -->

用户未明确要求前，不要创建或更新自动化。绝不要将秘密值放入插件文件、提示词或已提交的配置。

<!-- zh-CN:end e2f9a504e13cf5af -->

## 1. Copy the pack and enable shared pstack skills

<!-- zh-CN:begin 82b5b78abb828b0f -->

## 1. 复制包并启用共享 pstack 技能

<!-- zh-CN:end 82b5b78abb828b0f -->

Do this before asking for Benny configuration and before invoking the built-in `/automate` skill.

<!-- zh-CN:begin 4061837c07da5a48 -->

在询问 Benny 配置、调用内置 `/automate` 技能之前，先完成这一步。

<!-- zh-CN:end 4061837c07da5a48 -->

Ask which repository will run the automations. The source pack is the directory containing `FOR_AGENTS.md`. The destination is `<target-repository>/.cursor/automations/benny/`.

<!-- zh-CN:begin 91447eabb0c4cb92 -->

询问哪个仓库将运行这些自动化。源包是包含 `FOR_AGENTS.md` 的目录。目标位置是 `<target-repository>/.cursor/automations/benny/`。

<!-- zh-CN:end 91447eabb0c4cb92 -->

Merge the entire source pack into the destination:

<!-- zh-CN:begin 8bedf7e4f09e60f6 -->

将整个源包合并进目标位置：

<!-- zh-CN:end 8bedf7e4f09e60f6 -->

1. Create the destination when it is absent.

<!-- zh-CN:begin da2d64391f8297fe -->

1. 目标不存在时创建它。

<!-- zh-CN:end da2d64391f8297fe -->
2. Copy every source file to the same relative path.

<!-- zh-CN:begin daad7b90d404204a -->

2. 将每个源文件复制到相同的相对路径。

<!-- zh-CN:end daad7b90d404204a -->
3. Preserve destination-only files. Never delete unrelated files during install or refresh.

<!-- zh-CN:begin 9b822b33b3404202 -->

3. 保留仅存在于目标中的文件。安装或刷新时，绝不删除无关文件。

<!-- zh-CN:end 9b822b33b3404202 -->
4. Keep user-owned configuration, feature maps, and routing maps outside the destination. Never overwrite them.

<!-- zh-CN:begin fea88d93c8f49aa6 -->

4. 将用户拥有的配置、功能地图和路由地图放在目标目录之外。绝不覆盖它们。

<!-- zh-CN:end fea88d93c8f49aa6 -->
5. When an existing source-managed file differs, inspect the diff and merge without discarding local edits. If ownership is ambiguous, stop and ask before replacing it.

<!-- zh-CN:begin 489532a2c21de523 -->

5. 现有的源管理文件存在差异时，检查差异并合并，不丢弃本地编辑。所有权有歧义时，在替换前停止并询问。

<!-- zh-CN:end 489532a2c21de523 -->
6. Verify that the destination contains `FOR_AGENTS.md`, this setup file, both operational files, their references, and the templates.

<!-- zh-CN:begin 4218e5f2931def6e -->

6. 验证目标包含 `FOR_AGENTS.md`、本设置文件、两个操作文件、它们的参考资料以及模板。

<!-- zh-CN:end 4218e5f2931def6e -->

If this file is already being read from the target destination, treat the copy as complete and run the same verification before continuing.

<!-- zh-CN:begin 0ad0fc7836f652b3 -->

如果已经从目标位置读取本文件，将复制视为完成，并在继续前执行相同验证。

<!-- zh-CN:end 0ad0fc7836f652b3 -->

Add pstack to the target repository's `.cursor/settings.json`. If the file or `.cursor` directory does not exist, create it.

<!-- zh-CN:begin c40ce9b0fb9a8d3d -->

将 pstack 添加到目标仓库的 `.cursor/settings.json`。如果文件或 `.cursor` 目录不存在，创建它。

<!-- zh-CN:end c40ce9b0fb9a8d3d -->

Merge this entry into the existing JSON or JSONC:

<!-- zh-CN:begin f8b616dcc8a5d906 -->

将此条目合并进现有 JSON 或 JSONC：

<!-- zh-CN:end f8b616dcc8a5d906 -->

```json
{
	"plugins": {
		"pstack": { "enabled": true }
	}
}
```

Preserve every unrelated top-level setting and every other plugin entry. If `plugins.pstack` already exists, change only its `enabled` value. Preserve comments and valid JSONC syntax when the file uses JSONC. Validate the file after editing it.

<!-- zh-CN:begin 48044c9c1fc116e3 -->

保留每个无关顶层设置和所有其他插件条目。如果 `plugins.pstack` 已存在，只改变其 `enabled` 值。如果文件使用 JSONC，保留注释及有效 JSONC 语法。编辑后验证文件。

<!-- zh-CN:end 48044c9c1fc116e3 -->

Reload the target project or start a fresh agent rooted there. Verify that these shared pstack skills resolve from project scope:

<!-- zh-CN:begin 4818048cb28caa55 -->

重新加载目标项目，或启动以该项目为根的新代理。验证下列共享 pstack 技能能从项目作用域解析：

<!-- zh-CN:end 4818048cb28caa55 -->

- `how`
- `why`
- `tdd`
- `unslop`
- `principle-separate-before-serializing-shared-state`
- `principle-minimize-reader-load`
- `principle-guard-the-context-window`
- `principle-sequence-verifiable-units`
- `principle-fix-root-causes`
- `principle-prove-it-works`

Do not count a skill loaded from the current session or a user-scoped plugin. The check must show that a fresh agent in the target repository receives pstack through project settings.

<!-- zh-CN:begin b4e1dbcff5f73380 -->

不要把当前会话或用户作用域插件加载的技能算作通过。检查必须表明，目标仓库中的新代理通过项目设置获得 pstack。

<!-- zh-CN:end b4e1dbcff5f73380 -->

If project-scoped plugin installation is unavailable or any shared dependency does not resolve, stop and explain the failure.

<!-- zh-CN:begin 3037360e30dad6fe -->

如果项目作用域插件安装不可用，或任何共享依赖无法解析，停止并解释失败。

<!-- zh-CN:end 3037360e30dad6fe -->

The Benny files are read directly from `.cursor/automations/benny/`. Do not add that directory to a plugin manifest or expect its `SKILL.md` files to appear in the slash-skill list.

<!-- zh-CN:begin d1bdc1a75406ec6d -->

Benny 文件直接从 `.cursor/automations/benny/` 读取。不要把这个目录添加到插件清单，也不要期待其中的 `SKILL.md` 文件出现在斜杠技能列表中。

<!-- zh-CN:end d1bdc1a75406ec6d -->

Tell the user that `.cursor/settings.json`, `.cursor/automations/benny/`, and any referenced secret-free configuration must be committed before either automation is enabled. Do not commit them unless the user asks.

<!-- zh-CN:begin 2e50376c1846507b -->

告诉用户，启用任一自动化前，必须提交 `.cursor/settings.json`、`.cursor/automations/benny/`，以及任何被引用且不含秘密的配置。除非用户要求，否则不要代为提交。

<!-- zh-CN:end 2e50376c1846507b -->

Once this check passes, live automation prompts may read the committed operational files by their stable repository-relative paths. They must not embed a plugin cache path or copy the file contents.

<!-- zh-CN:begin 80fc035996231195 -->

此检查通过后，实际自动化提示词可以通过稳定的仓库相对路径读取已提交操作文件。它们不得嵌入插件缓存路径，也不得复制文件内容。

<!-- zh-CN:end 80fc035996231195 -->

## 2. Adapt the configuration

<!-- zh-CN:begin 10ccf56bc0ebe7e9 -->

## 2. 调整配置

<!-- zh-CN:end 10ccf56bc0ebe7e9 -->

Open these copied examples:

<!-- zh-CN:begin ae52c3e67dfcdf5e -->

打开以下已复制示例：

<!-- zh-CN:end ae52c3e67dfcdf5e -->

- `../../templates/configuration.example.yaml`
- `../reproduce-and-fix-issues/references/feature-map.example.md`

Create user-owned copies outside `.cursor/automations/benny/`. These are configuration files, not pack files. Example locations:

<!-- zh-CN:begin d86a9ac13448a1ab -->

在 `.cursor/automations/benny/` 之外创建用户拥有的副本。这些是配置文件，不是包文件。示例位置：

<!-- zh-CN:end d86a9ac13448a1ab -->

- Project config, such as `.cursor/benny/configuration.yaml`

<!-- zh-CN:begin 0c317b9d5446e6c1 -->

- 项目配置，例如 `.cursor/benny/configuration.yaml`

<!-- zh-CN:end 0c317b9d5446e6c1 -->
- Project feature map, such as `.cursor/benny/feature-map.md`

<!-- zh-CN:begin 03290c8f6c2ec6ac -->

- 项目功能地图，例如 `.cursor/benny/feature-map.md`

<!-- zh-CN:end 03290c8f6c2ec6ac -->
- Project routing map, such as `.cursor/benny/routing.md`

<!-- zh-CN:begin 329e6b0acb67b559 -->

- 项目路由地图，例如 `.cursor/benny/routing.md`

<!-- zh-CN:end 329e6b0acb67b559 -->
- User config, such as `~/.config/benny/configuration.yaml`

<!-- zh-CN:begin 27539d1a7e6c29cb -->

- 用户配置，例如 `~/.config/benny/configuration.yaml`

<!-- zh-CN:end 27539d1a7e6c29cb -->
- User feature map, such as `~/.config/benny/feature-map.md`

<!-- zh-CN:begin edb89bb4e798fb3e -->

- 用户功能地图，例如 `~/.config/benny/feature-map.md`

<!-- zh-CN:end edb89bb4e798fb3e -->

Fill one feature-map section for every user-facing feature the automation may reproduce. Keep it at the user point of view. Do not freeze implementation details or current code paths in the map.

<!-- zh-CN:begin b5b2b6ef1d4e7a87 -->

为自动化可能复现的每个面向用户功能填写一个功能地图章节。始终保持用户视角。不要把实现细节或当前代码路径固定在地图中。

<!-- zh-CN:end b5b2b6ef1d4e7a87 -->

Do not edit the copied examples. Pack refreshes may update source-managed files after conflict review, but they must never touch the user-owned copies.

<!-- zh-CN:begin bc77eb2ad06e306a -->

不要编辑已复制的示例。包刷新可在冲突审查后更新源管理文件，但绝不能触及用户拥有的副本。

<!-- zh-CN:end bc77eb2ad06e306a -->

Prefer committed, secret-free files in the target repository when a fresh automation checkout must read them. Otherwise paraphrase the required values into the live prompt. Reference a repository file only after the built-in `/automate` skill confirms that the file is committed in the repository where the automation runs.

<!-- zh-CN:begin eaf921a3b044bbac -->

全新自动化检出必须读取文件时，优先使用目标仓库中已提交且不含秘密的文件。否则，将所需值转述进实际提示词。只有内置 `/automate` 技能确认文件已提交到自动化运行所在仓库后，才引用该仓库文件。

<!-- zh-CN:end eaf921a3b044bbac -->

Use stable repository-relative paths for committed pack and configuration files. Never reference the plugin source directory or a plugin cache path from a live automation.

<!-- zh-CN:begin 47098d119bd86e5c -->

对已提交的包和配置文件使用稳定的仓库相对路径。实际自动化中绝不引用插件源目录或插件缓存路径。

<!-- zh-CN:end 47098d119bd86e5c -->

## 3. Fill the required choices

<!-- zh-CN:begin 5af7b3ed07682645 -->

## 3. 填写必需选择

<!-- zh-CN:end 5af7b3ed07682645 -->

Ask for or confirm:

<!-- zh-CN:begin 17e1636b07310ff1 -->

询问或确认：

<!-- zh-CN:end 17e1636b07310ff1 -->

- Source Slack channel ID

<!-- zh-CN:begin fb11b7cdb26ebfa7 -->

- 来源 Slack 频道 ID

<!-- zh-CN:end fb11b7cdb26ebfa7 -->
- Optional operations or status channel ID

<!-- zh-CN:begin 78f79f850b791fbd -->

- 可选的运维或状态频道 ID

<!-- zh-CN:end 78f79f850b791fbd -->
- Repository URL and default branch

<!-- zh-CN:begin 68dc4959266079e4 -->

- 仓库 URL 和默认分支

<!-- zh-CN:end 68dc4959266079e4 -->
- Triage identity or Slack user ID

<!-- zh-CN:begin a159bbbd55854ddb -->

- 分诊身份或 Slack 用户 ID

<!-- zh-CN:end a159bbbd55854ddb -->
- Issue tracker type, team, project, labels, and intake status

<!-- zh-CN:begin ee7c631f9330a8f4 -->

- 问题跟踪器类型、团队、项目、标签和接收状态

<!-- zh-CN:end ee7c631f9330a8f4 -->
- Tracker adapter skill or MCP actions

<!-- zh-CN:begin 82df574f2ac82f11 -->

- 跟踪器适配技能或 MCP 操作

<!-- zh-CN:end 82df574f2ac82f11 -->
- Optional routing map path

<!-- zh-CN:begin e1c0b2136b5d40f5 -->

- 可选的路由地图路径

<!-- zh-CN:end e1c0b2136b5d40f5 -->
- Required control skill name

<!-- zh-CN:begin bf248378bd7a420c -->

- 必需的控制技能名称

<!-- zh-CN:end bf248378bd7a420c -->
- Required user-facing feature-map path

<!-- zh-CN:begin 551887bea2d04871 -->

- 必需的面向用户功能地图路径

<!-- zh-CN:end 551887bea2d04871 -->
- Status emoji strings

<!-- zh-CN:begin 8a7403681f6821fc -->

- 状态 emoji 字符串

<!-- zh-CN:end 8a7403681f6821fc -->
- Pull request URL format

<!-- zh-CN:begin 6179dc7b5de60ff8 -->

- pull request URL 格式

<!-- zh-CN:end 6179dc7b5de60ff8 -->
- Polling and effort budgets

<!-- zh-CN:begin 38d75d1c60bb27db -->

- 轮询和工作量预算

<!-- zh-CN:end 38d75d1c60bb27db -->
- Model slug for triage, repro, code work, and media review

<!-- zh-CN:begin 2a26aaea44ede476 -->

- 分诊、复现、代码工作和媒体审查所用模型 slug

<!-- zh-CN:end 2a26aaea44ede476 -->

Use only model slugs shown as available in the user's Cursor model picker or supported model list. Do not guess a slug and do not carry over a private default.

<!-- zh-CN:begin 0bc4662dfd99186e -->

只使用用户 Cursor 模型选择器或受支持模型列表中显示为可用的模型 slug。不要猜测 slug，也不要沿用私有默认值。

<!-- zh-CN:end 0bc4662dfd99186e -->

The source channel, triage identity, repository, tracker adapter, control skill, and feature map must be explicit. Fail setup if any required value stays ambiguous.

<!-- zh-CN:begin 3072a15191de6158 -->

来源频道、分诊身份、仓库、跟踪器适配器、控制技能和功能地图都必须明确。任何必需值仍有歧义时，设置失败。

<!-- zh-CN:end 3072a15191de6158 -->

Use pstack's `unslop` skill on the final automation names, descriptions, and prompt shims before saving them.

<!-- zh-CN:begin e086d6615125b3d2 -->

保存之前，对最终自动化名称、描述和提示词薄封装使用 pstack 的 `unslop` 技能。

<!-- zh-CN:end e086d6615125b3d2 -->

## 4. Check integration capabilities

<!-- zh-CN:begin f184ec3376c8a0da -->

## 4. 检查集成能力

<!-- zh-CN:end f184ec3376c8a0da -->

The triage automation needs:

<!-- zh-CN:begin 85f08e48bd696348 -->

分诊自动化需要：

<!-- zh-CN:end 85f08e48bd696348 -->

- Read access to the configured source Slack channel and its threads

<!-- zh-CN:begin a379f615a1b8e6df -->

- 对配置来源 Slack 频道及其线程的读取权限

<!-- zh-CN:end a379f615a1b8e6df -->
- Thread-reply access in that channel

<!-- zh-CN:begin 7852f5da7f6dd864 -->

- 在该频道中回复线程的权限

<!-- zh-CN:end 7852f5da7f6dd864 -->
- Attachment metadata and file download access when reports include media

<!-- zh-CN:begin 7b3335eead9fe817 -->

- 报告含媒体时，访问附件元数据和下载文件的权限

<!-- zh-CN:end 7b3335eead9fe817 -->
- Search, read, create, and update access through the configured issue-tracker adapter

<!-- zh-CN:begin fe7e9f86efda09f6 -->

- 通过已配置问题跟踪器适配器进行搜索、读取、创建和更新的权限

<!-- zh-CN:end fe7e9f86efda09f6 -->

The repro automation needs:

<!-- zh-CN:begin 12e40ac224a6bfb0 -->

复现自动化需要：

<!-- zh-CN:end 12e40ac224a6bfb0 -->

- Read access to the source thread

<!-- zh-CN:begin e51742de31b53978 -->

- 来源线程读取权限

<!-- zh-CN:end e51742de31b53978 -->
- Thread-reply access in the source channel

<!-- zh-CN:begin 482087957feb9fdd -->

- 来源频道内线程回复权限

<!-- zh-CN:end 482087957feb9fdd -->
- Optional post and edit access in the configured operations channel

<!-- zh-CN:begin 09747011d6e0c0d5 -->

- 可选的、在已配置运维频道中发帖和编辑的权限

<!-- zh-CN:end 09747011d6e0c0d5 -->
- Repository read and history access

<!-- zh-CN:begin 81a2821e1c9550d6 -->

- 仓库读取及历史访问权限

<!-- zh-CN:end 81a2821e1c9550d6 -->
- A pull request action that can open a draft pull request

<!-- zh-CN:begin 785b23ce625583a2 -->

- 可打开草稿 pull request 的操作

<!-- zh-CN:end 785b23ce625583a2 -->
- The configured control-adapter skill

<!-- zh-CN:begin 2adb846c9defae18 -->

- 已配置的控制适配技能

<!-- zh-CN:end 2adb846c9defae18 -->

Prefer configured Cursor Slack actions for reads and posts. The optional `BENNY_SLACK_BOT_TOKEN` may fill a narrow gap such as editing one operations status message or downloading an attachment. Store the value in a secret manager or environment, not in YAML.

<!-- zh-CN:begin d7c37967ed2df357 -->

读取与发帖优先使用已配置 Cursor Slack 操作。可选的 `BENNY_SLACK_BOT_TOKEN` 可填补狭窄缺口，例如编辑一条运维状态消息或下载附件。将其值存入秘密管理器或环境，而不是 YAML。

<!-- zh-CN:end d7c37967ed2df357 -->

Do not use undocumented integration endpoints.

<!-- zh-CN:begin 9e5e88319fd1526a -->

不要使用未记录的集成端点。

<!-- zh-CN:end 9e5e88319fd1526a -->

## 5. Prepare the routing map

<!-- zh-CN:begin b10f76f9e1a9c80c -->

## 5. 准备路由地图

<!-- zh-CN:end b10f76f9e1a9c80c -->

If the user wants reroutes or owner pings:

<!-- zh-CN:begin 15cd372c8dfe7b1a -->

如果用户需要重新路由或 @ 负责人：

<!-- zh-CN:end 15cd372c8dfe7b1a -->

1. Copy `../triage-issue-reports/references/routing.example.md` outside `.cursor/automations/benny/`.

<!-- zh-CN:begin d8742acf0cc02d9b -->

1. 将 `../triage-issue-reports/references/routing.example.md` 复制到 `.cursor/automations/benny/` 之外。

<!-- zh-CN:end d8742acf0cc02d9b -->
2. Replace every placeholder with public or organization-local values.

<!-- zh-CN:begin 6ed3abba6c852223 -->

2. 用公开或组织本地值替换所有占位符。

<!-- zh-CN:end 6ed3abba6c852223 -->
3. Keep owner pings off by default.

<!-- zh-CN:begin c8e6e3212513ee99 -->

3. 默认关闭 @ 负责人。

<!-- zh-CN:end c8e6e3212513ee99 -->
4. Allow a ping only for a configured feature owner or a confirmed likely regression author.

<!-- zh-CN:begin f4d4588f415c912b -->

4. 只有针对已配置的功能负责人，或经确认很可能是回归引入者的人，才允许 @。

<!-- zh-CN:end f4d4588f415c912b -->

If no routing map is configured, triage may classify a report but must not guess a destination or owner.

<!-- zh-CN:begin 0b34437c0d907fbe -->

如果没有配置路由地图，分诊可以给报告分类，但不得猜测目的地或负责人。

<!-- zh-CN:end 0b34437c0d907fbe -->

## 6. Verify the control adapter

<!-- zh-CN:begin ab56150aad78823b -->

## 6. 验证控制适配器

<!-- zh-CN:end ab56150aad78823b -->

Read `../reproduce-and-fix-issues/references/control-adapter.md` and the user's completed feature map.

<!-- zh-CN:begin b1c26745fcab5d41 -->

阅读 `../reproduce-and-fix-issues/references/control-adapter.md` 和用户填好的功能地图。

<!-- zh-CN:end b1c26745fcab5d41 -->

Confirm that the named skill can:

<!-- zh-CN:begin fad98c1e3bcdccbe -->

确认指定技能能够：

<!-- zh-CN:end fad98c1e3bcdccbe -->

- Bring up the target app

<!-- zh-CN:begin 69ff31b89dc19872 -->

- 启动目标应用

<!-- zh-CN:end 69ff31b89dc19872 -->
- Navigate every mapped feature through the real UI

<!-- zh-CN:begin 272ab90afd4f8e7a -->

- 通过真实 UI 导航到每个映射功能

<!-- zh-CN:end 272ab90afd4f8e7a -->
- Exercise mapped states through declared adapter actions

<!-- zh-CN:begin d82a1a82b4892daf -->

- 通过声明的适配器动作执行映射状态

<!-- zh-CN:end d82a1a82b4892daf -->
- Inspect state without forcing the result

<!-- zh-CN:begin f8b4ed3ebef2d42b -->

- 检查状态而不强行设定结果

<!-- zh-CN:end f8b4ed3ebef2d42b -->
- Capture screenshots

<!-- zh-CN:begin 386a1d9857a0fd0c -->

- 捕获截图

<!-- zh-CN:end 386a1d9857a0fd0c -->
- Start and stop a recording

<!-- zh-CN:begin d104cc6c6fdeff41 -->

- 开始和停止录制

<!-- zh-CN:end d104cc6c6fdeff41 -->
- Clean up its processes and temporary data

<!-- zh-CN:begin 5c2b76645da18e44 -->

- 清理自己的进程和临时数据

<!-- zh-CN:end 5c2b76645da18e44 -->

If any capability is missing, leave the repro automation disabled. It must fail closed rather than claim a reproduction it did not perform.

<!-- zh-CN:begin bcd1cfafdf54664c -->

只要缺少任一能力，就保持复现自动化禁用。它必须在失败时默认关闭，而不是声称完成了实际上没做过的复现。

<!-- zh-CN:end bcd1cfafdf54664c -->

## 7. Prepare the live automations

<!-- zh-CN:begin fd752f8009a12e56 -->

## 7. 准备实际自动化

<!-- zh-CN:end fd752f8009a12e56 -->

Ask whether this is first-time creation or configuration of existing automations.

<!-- zh-CN:begin caad308b4a947f7e -->

询问这是首次创建，还是配置已有自动化。

<!-- zh-CN:end caad308b4a947f7e -->

Read `../../FOR_AGENTS.md` from the copied pack as the primary user-intent source for either path. Use it to understand the two triggers, tools, instructions, outcomes, and shared rules.

<!-- zh-CN:begin 950509975f5f4e7c -->

无论哪条路径，都从已复制的包中读取 `../../FOR_AGENTS.md`，作为首要用户意图来源。用它理解两个触发器、工具、指令、结果和共享规则。

<!-- zh-CN:end 950509975f5f4e7c -->

### First-time creation

<!-- zh-CN:begin 869fd4746e23020d -->

### 首次创建

<!-- zh-CN:end 869fd4746e23020d -->

Create one automation at a time.

<!-- zh-CN:begin c253f17c2126015a -->

一次创建一个自动化。

<!-- zh-CN:end c253f17c2126015a -->

For each automation:

<!-- zh-CN:begin 2a3d1b20f012d556 -->

对于每个自动化：

<!-- zh-CN:end 2a3d1b20f012d556 -->

1. Read the matching copied prompt template as secondary internal source material.

<!-- zh-CN:begin 7c9fdafbb3242a9d -->

1. 阅读匹配的已复制提示词模板，作为次要内部来源材料。

<!-- zh-CN:end 7c9fdafbb3242a9d -->
2. Turn `FOR_AGENTS.md`, the finished Benny configuration, and the template intent into a complete natural-language request.

<!-- zh-CN:begin 0c9bbde8db0bb193 -->

2. 将 `FOR_AGENTS.md`、已完成的 Benny 配置和模板意图转为一个完整的自然语言请求。

<!-- zh-CN:end 0c9bbde8db0bb193 -->
3. Tell the live prompt to read and follow its exact committed operational file under `.cursor/automations/benny/`.

<!-- zh-CN:begin 712d0db095cdf5bc -->

3. 告诉实际提示词读取并遵循它在 `.cursor/automations/benny/` 下确切的已提交操作文件。

<!-- zh-CN:end 712d0db095cdf5bc -->
4. Use the stable repository-relative path, not a plugin source or cache path. Do not copy the operational file contents into the live prompt.

<!-- zh-CN:begin 149f28d091f0145e -->

4. 使用稳定的仓库相对路径，而不是插件源路径或缓存路径。不要把操作文件内容复制进实际提示词。

<!-- zh-CN:end 149f28d091f0145e -->
5. Read and follow the built-in `automate` skill.

<!-- zh-CN:begin 8c84d9479ffcde91 -->

5. 阅读并遵循内置 `automate` 技能。

<!-- zh-CN:end 8c84d9479ffcde91 -->
6. Let `automate` discover Slack channels, the repository, and connected integrations.

<!-- zh-CN:begin eef746f7b51a2991 -->

6. 让 `automate` 发现 Slack 频道、仓库和已连接集成。

<!-- zh-CN:end eef746f7b51a2991 -->
7. Let `automate` confirm that the copied pack and any referenced configuration files are committed in the same repository where the automation will run.

<!-- zh-CN:begin 5ba067a04966bf66 -->

7. 让 `automate` 确认已复制的包和任何引用的配置文件已提交到自动化将运行的同一仓库。

<!-- zh-CN:end 5ba067a04966bf66 -->
8. Let `automate` show its draft table, obtain approval, ask readiness, and open the Automations editor.

<!-- zh-CN:begin ad185ef15fae7217 -->

8. 让 `automate` 展示草稿表、取得批准、询问是否就绪，并打开 Automations 编辑器。

<!-- zh-CN:end ad185ef15fae7217 -->
9. Finish the editor handoff for this automation before starting the next one.

<!-- zh-CN:begin 96905d37695bec32 -->

9. 开始下一个自动化之前，完成当前自动化的编辑器交接。

<!-- zh-CN:end 96905d37695bec32 -->

Give `automate` this complete triage intent, filled from configuration:

<!-- zh-CN:begin 21e1edb7307aacea -->

将以下完整分诊意图交给 `automate`，使用配置填入内容：

<!-- zh-CN:end 21e1edb7307aacea -->

- Name `benny-triage`.

<!-- zh-CN:begin 3fb7ce6d5b0b45a0 -->

- 名称为 `benny-triage`。

<!-- zh-CN:end 3fb7ce6d5b0b45a0 -->
- Read and follow `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md` for every run.

<!-- zh-CN:begin 7802a014a908cf52 -->

- 每次运行都读取并遵循 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`。

<!-- zh-CN:end 7802a014a908cf52 -->
- Trigger on each new top-level report in the configured source Slack channel.

<!-- zh-CN:begin cc03f235ae7dd336 -->

- 对配置来源 Slack 频道中的每个新顶层报告触发。

<!-- zh-CN:end cc03f235ae7dd336 -->
- Read the triggering thread and reply only inside it.

<!-- zh-CN:begin 74a0c9f367df0c55 -->

- 读取触发线程，并且只在其中回复。

<!-- zh-CN:end 74a0c9f367df0c55 -->
- Use the configured issue-tracker integration.

<!-- zh-CN:begin a395fe93e7f79b8a -->

- 使用已配置的问题跟踪器集成。

<!-- zh-CN:end a395fe93e7f79b8a -->
- Classify, inspect evidence, trace cause, dedupe, and create only clear new bugs.

<!-- zh-CN:begin 62a3908675596c86 -->

- 分类、检查证据、追踪原因、去重，并且只为明确的新 bug 创建问题。

<!-- zh-CN:end 62a3908675596c86 -->
- End one thread-only verdict with the configured `[benny:bug]`, `[benny:performance]`, or `[benny:other]` marker and optional tracker URL.

<!-- zh-CN:begin c281ee43a87c2d39 -->

- 以一条仅在线程内的裁决结束，包含配置的 `[benny:bug]`、`[benny:performance]` 或 `[benny:other]` 标记，以及可选的跟踪器 URL。

<!-- zh-CN:end c281ee43a87c2d39 -->
- Never post a source-channel root message.

<!-- zh-CN:begin 0b287f060384bb7f -->

- 绝不在来源频道发布根消息。

<!-- zh-CN:end 0b287f060384bb7f -->

After the triage editor handoff is complete, give `automate` this complete repro and fix intent:

<!-- zh-CN:begin b7a6ddc54c1dacf8 -->

分诊编辑器交接完成后，将以下完整复现和修复意图交给 `automate`：

<!-- zh-CN:end b7a6ddc54c1dacf8 -->

- Name `benny-reproduce`.

<!-- zh-CN:begin 1c452d0616b71cc7 -->

- 名称为 `benny-reproduce`。

<!-- zh-CN:end 1c452d0616b71cc7 -->
- Read and follow `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` for every run.

<!-- zh-CN:begin 979cf87395997548 -->

- 每次运行都读取并遵循 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`。

<!-- zh-CN:end 979cf87395997548 -->
- Trigger on the same new top-level reports in the configured source Slack channel.

<!-- zh-CN:begin 5f498c0bb4a31554 -->

- 对配置来源 Slack 频道中相同的新顶层报告触发。

<!-- zh-CN:end 5f498c0bb4a31554 -->
- Use the configured repository and default branch.

<!-- zh-CN:begin 0a9c962d2da99044 -->

- 使用已配置仓库和默认分支。

<!-- zh-CN:end 0a9c962d2da99044 -->
- Read the source thread and reply only inside it.

<!-- zh-CN:begin 0b33ef94e80cad8f -->

- 读取来源线程，并且只在其中回复。

<!-- zh-CN:end 0b33ef94e80cad8f -->
- Include pull request creation and the configured tracker, control-adapter, and feature-map requirements. Paraphrase mapped user paths and states unless `automate` confirms an eligible committed file in the same repository.

<!-- zh-CN:begin 9be694f69cb71a58 -->

- 包含 pull request 创建，以及已配置的跟踪器、控制适配器和功能地图要求。除非 `automate` 确认同一仓库中存在合格的已提交文件，否则转述映射的用户路径和状态。

<!-- zh-CN:end 9be694f69cb71a58 -->
- Wait for a trusted triage marker before acting.

<!-- zh-CN:begin 2077bb1716237b8a -->

- 行动前等待可信的分诊标记。

<!-- zh-CN:end 2077bb1716237b8a -->
- Reproduce the exact symptom twice through the mapped real UI and capture evidence.

<!-- zh-CN:begin 36cf9b4c1ee6f6cc -->

- 通过映射的真实 UI 将确切症状复现两次，并捕获证据。

<!-- zh-CN:end 36cf9b4c1ee6f6cc -->
- Verify an existing fix without authoring over it.

<!-- zh-CN:begin 5e99e22e8e0cac60 -->

- 验证已有修复，不要另行编写覆盖它。

<!-- zh-CN:end 5e99e22e8e0cac60 -->
- Attempt an optional bounded fix only after confirmed repro, then open a draft pull request when proof and checks pass.

<!-- zh-CN:begin 00b03689baaa4419 -->

- 仅在确认复现后，才尝试可选的有界修复；证明和检查通过时，再打开草稿 pull request。

<!-- zh-CN:end 00b03689baaa4419 -->
- Never post a source-channel root message.

<!-- zh-CN:begin 81ec24789b05f767 -->

- 绝不在来源频道发布根消息。

<!-- zh-CN:end 81ec24789b05f767 -->

Do not duplicate `automate`'s Slack, repository, integration, completeness, authentication, draft-review, approval, readiness, or editor-handoff work.

<!-- zh-CN:begin 5b9de0dfdc0840c6 -->

不要重复 `automate` 在 Slack、仓库、集成、完整性、认证、草稿审查、批准、就绪确认或编辑器交接方面的工作。

<!-- zh-CN:end 5b9de0dfdc0840c6 -->

### Existing automations

<!-- zh-CN:begin 41d09639b4d2ff69 -->

### 已有自动化

<!-- zh-CN:end 41d09639b4d2ff69 -->

The built-in `automate` skill is creation-only. Do not use it to search for, inspect, or update existing automations.

<!-- zh-CN:begin 0dd7bd3768040682 -->

内置 `automate` 技能仅用于创建。不要用它搜索、检查或更新已有自动化。

<!-- zh-CN:end 0dd7bd3768040682 -->

Finish configuration, routing, control-adapter, and feature-map validation. Then give the user this concise editor checklist.

<!-- zh-CN:begin 8c0bba7f2062bbd9 -->

完成配置、路由、控制适配器和功能地图验证。然后给用户这份简洁编辑器检查清单。

<!-- zh-CN:end 8c0bba7f2062bbd9 -->

For the existing triage automation, update:

<!-- zh-CN:begin 36dcbc7ffd0e7189 -->

对于已有分诊自动化，更新：

<!-- zh-CN:end 36dcbc7ffd0e7189 -->

- Name and description

<!-- zh-CN:begin 914150fe2b233e3d -->

- 名称和描述

<!-- zh-CN:end 914150fe2b233e3d -->
- Direct instruction to read `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`

<!-- zh-CN:begin 6f4e9d6dd32f611c -->

- 直接要求读取 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md` 的指令

<!-- zh-CN:end 6f4e9d6dd32f611c -->
- New top-level Slack report trigger and source channel

<!-- zh-CN:begin d9926b5d53b7f8ff -->

- 新顶层 Slack 报告触发器和来源频道

<!-- zh-CN:end d9926b5d53b7f8ff -->
- Slack thread read and reply capabilities

<!-- zh-CN:begin 4b013bcfedd15575 -->

- Slack 线程读取与回复能力

<!-- zh-CN:end 4b013bcfedd15575 -->
- Issue-tracker integration

<!-- zh-CN:begin c3d1cf6d9ec47ecf -->

- 问题跟踪器集成

<!-- zh-CN:end c3d1cf6d9ec47ecf -->
- Paraphrased triage instructions, thread-only rule, and Benny verdict markers

<!-- zh-CN:begin 71e67b64e6e35077 -->

- 转述的分诊指令、仅限线程规则和 Benny 裁决标记

<!-- zh-CN:end 71e67b64e6e35077 -->

For the existing repro automation, update:

<!-- zh-CN:begin a5f44972fa27723b -->

对于已有复现自动化，更新：

<!-- zh-CN:end a5f44972fa27723b -->

- Name and description

<!-- zh-CN:begin af2068ca01ec730a -->

- 名称和描述

<!-- zh-CN:end af2068ca01ec730a -->
- Direct instruction to read `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`

<!-- zh-CN:begin 1190f4febd12452e -->

- 直接要求读取 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` 的指令

<!-- zh-CN:end 1190f4febd12452e -->
- Matching Slack trigger and source channel

<!-- zh-CN:begin ff0d643ff5c7c396 -->

- 匹配的 Slack 触发器和来源频道

<!-- zh-CN:end ff0d643ff5c7c396 -->
- Repository and default branch

<!-- zh-CN:begin 269b5fea70ff7430 -->

- 仓库和默认分支

<!-- zh-CN:end 269b5fea70ff7430 -->
- Slack thread read and reply capabilities

<!-- zh-CN:begin a8502219fb7bafe1 -->

- Slack 线程读取与回复能力

<!-- zh-CN:end a8502219fb7bafe1 -->
- Pull request action

<!-- zh-CN:begin cc45257b0414facc -->

- pull request 操作

<!-- zh-CN:end cc45257b0414facc -->
- Tracker, control-adapter, and feature-map requirements

<!-- zh-CN:begin 351ec3b2a0fc2f11 -->

- 跟踪器、控制适配器和功能地图要求

<!-- zh-CN:end 351ec3b2a0fc2f11 -->
- Paraphrased marker wait, evidence, verification, and bounded-fix instructions

<!-- zh-CN:begin 26b702fd16aa9c88 -->

- 转述的等待标记、证据、验证和有界修复指令

<!-- zh-CN:end 26b702fd16aa9c88 -->

Ask the user to update each existing automation directly in its Automations editor. Do not create replacements or duplicates.

<!-- zh-CN:begin 3384a829c748bfa3 -->

请用户在各自 Automations 编辑器中直接更新每个已有自动化。不要创建替代品或重复项。

<!-- zh-CN:end 3384a829c748bfa3 -->

### Creation boundary

<!-- zh-CN:begin 6d2d8ebaabb3751a -->

### 创建边界

<!-- zh-CN:end 6d2d8ebaabb3751a -->

Never call a direct automation backend service or backend automation tool. Never use a browser URL that carries draft fields. Never build or open a Cursor protocol deep link. For new automations, the only finish path is the built-in `automate` skill's reviewed Automations editor handoff.

<!-- zh-CN:begin 6561f7024f5f6a52 -->

绝不调用直接自动化后端服务或后端自动化工具。绝不使用携带草稿字段的浏览器 URL。绝不构建或打开 Cursor 协议深层链接。对于新自动化，唯一的完成路径是内置 `automate` 技能经过审查的 Automations 编辑器交接。

<!-- zh-CN:end 6561f7024f5f6a52 -->

Do not enable either automation until the thread-safety test passes after the editor save.

<!-- zh-CN:begin 0f7ab0793dc2d60d -->

在编辑器保存后的线程安全测试通过之前，不要启用任何一个自动化。

<!-- zh-CN:end 0f7ab0793dc2d60d -->

## 8. Test thread safety

<!-- zh-CN:begin a3825756650cb5f3 -->

## 8. 测试线程安全

<!-- zh-CN:end a3825756650cb5f3 -->

Use a test channel or a harmless test report.

<!-- zh-CN:begin ac229e72d6313a72 -->

使用测试频道或无害的测试报告。

<!-- zh-CN:end ac229e72d6313a72 -->

Before testing, confirm that the target repository's `.cursor/settings.json`, `.cursor/automations/benny/`, and every referenced secret-free configuration file are committed on the branch used by the automation checkout. Confirm that both live prompts point at their exact committed operational files. If any check fails, stop. Tell the user that the automation cannot be enabled yet.

<!-- zh-CN:begin 53e95ef68d407394 -->

测试之前，确认目标仓库的 `.cursor/settings.json`、`.cursor/automations/benny/` 和每个引用的不含秘密配置文件，都已提交到自动化检出所使用的分支。确认两个实际提示词都指向各自确切的已提交操作文件。任何检查失败时，停止。告诉用户自动化还不能启用。

<!-- zh-CN:end 53e95ef68d407394 -->

Verify:

<!-- zh-CN:begin fd7d06aa77fc23b5 -->

验证：

<!-- zh-CN:end fd7d06aa77fc23b5 -->

1. Triage stores the root `thread_ts` and posts exactly one verdict as a reply.

<!-- zh-CN:begin 486efe4750487d41 -->

1. 分诊保存根 `thread_ts`，并恰好发布一条作为回复的裁决。

<!-- zh-CN:end 486efe4750487d41 -->
2. The verdict contains one configured marker.

<!-- zh-CN:begin b28000379f4f32f1 -->

2. 裁决包含一个已配置标记。

<!-- zh-CN:end b28000379f4f32f1 -->
3. Repro accepts the marker only from the configured triage identity.

<!-- zh-CN:begin 5808a0c245894fbc -->

3. 复现只接受来自已配置分诊身份的标记。

<!-- zh-CN:end 5808a0c245894fbc -->
4. Repro keeps the same immutable source coordinates.

<!-- zh-CN:begin 0bac43b4a635c8ee -->

4. 复现始终保留相同且不可变的来源坐标。

<!-- zh-CN:end 0bac43b4a635c8ee -->
5. No source-channel root message appears.

<!-- zh-CN:begin 8864a5ee58bda8b6 -->

5. 来源频道中不出现根消息。

<!-- zh-CN:end 8864a5ee58bda8b6 -->
6. A delegated worker cannot use any Slack write action.

<!-- zh-CN:begin 24d3e7c49eb6d2f1 -->

6. 委派工作者无法使用任何 Slack 写入操作。

<!-- zh-CN:end 24d3e7c49eb6d2f1 -->
7. Missing coordinates, a deleted parent, or a failed preflight produces no post and no tracker issue.

<!-- zh-CN:begin 995e9730d870c2d6 -->

7. 缺少坐标、父消息被删除或预检失败时，既不发帖，也不创建跟踪器问题。

<!-- zh-CN:end 995e9730d870c2d6 -->

Enable normal traffic only after all seven checks pass.

<!-- zh-CN:begin d22e4fcda4836093 -->

仅在全部七项检查通过后，才启用正常流量。

<!-- zh-CN:end d22e4fcda4836093 -->
