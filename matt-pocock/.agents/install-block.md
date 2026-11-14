# The canonical install block

<!-- zh-CN:begin d593ccd92a4e5789 -->

# 规范安装区块

<!-- zh-CN:end d593ccd92a4e5789 -->

One install story, one wording. `README.md`, `.changeset/*`, and every page under `docs/` must say **this** and nothing else. Change it here first, then propagate.

<!-- zh-CN:begin 0cbbd4ff15d49901 -->

一个安装故事，一种措辞。`README.md`、`.changeset/*` 和 `docs/` 每页必须只说**这里**的内容。先修改此处再传播。

<!-- zh-CN:end 0cbbd4ff15d49901 -->

## Managed installs first

<!-- zh-CN:begin de1303d5e53eee4c -->

## 托管安装优先

<!-- zh-CN:end de1303d5e53eee4c -->

Lead with installs that update themselves. Fall back to skills.sh, labelled "manual updates", only for agents that have no such install. Call a route managed only if it updates without the user running a command. Put any one-time opt-in beside its install command. Never promise "instant".

<!-- zh-CN:begin 3a27918091fb8aa4 -->

优先写自行更新的安装；只有代理没有托管方式时，“手动更新”才回退到 skills.sh。只有无需用户运行命令就能更新，才称托管。一次性选择加入说明放在其安装命令旁。绝不承诺“即时”。

<!-- zh-CN:end 3a27918091fb8aa4 -->

Claude Code installs from its official marketplace, `claude-plugins-official`. Every other managed route installs from this repo's own marketplace, `.claude-plugin/marketplace.json` and `plugin.json`. Those routes reinstall only when the `version` in `plugin.json` changes. The Release workflow runs `npm run version`, which copies that field from `package.json`, so users get a release when the "chore: version skills" PR merges.

<!-- zh-CN:begin 51681110bbf49950 -->

Claude Code从官方市场`claude-plugins-official`安装；其他托管路线从本仓库市场`.claude-plugin/marketplace.json`和`plugin.json`安装。只有`plugin.json`的`version`变化时才重装。Release工作流运行`npm run version`，从`package.json`复制版本，因此“chore: version skills”PR合并后用户得到发布。

<!-- zh-CN:end 51681110bbf49950 -->

| Agent         | Route                            | Updates itself?                                                  |
| ------------- | -------------------------------- | ---------------------------------------------------------------- |
| Claude Code   | `@claude-plugins-official`       | Yes, by default                                                  |
| Codex         | `@mattpocock` marketplace        | Yes, at startup, by default                                      |
| Copilot CLI   | `@mattpocock` marketplace        | Yes, after a one-time `autoUpdate: true`                         |
| VS Code       | Chat: Install Plugin From Source | Yes, daily, by default                                           |
| Gemini CLI    | `gemini skills install` (copies) | No. A Gemini extension would need a flat `skills/<name>/` layout |
| Everyone else | skills.sh                        | No. Run `npx skills update`, and re-run `add` for new skills     |

<!-- zh-CN:begin bc478b4eeacc3bf0 -->

| 代理 | 路线 | 自动更新？ |
| ------------- | -------------------------------- | ---------------------------------------------------------------- |
| Claude Code | `@claude-plugins-official` | 默认是 |
| Codex | `@mattpocock`市场 | 默认启动时是 |
| Copilot CLI | `@mattpocock`市场 | 一次性设置`autoUpdate: true`后是 |
| VS Code | Chat: Install Plugin From Source | 默认每日是 |
| Gemini CLI | `gemini skills install`（复制） | 否；需要扁平`skills/<name>/`布局 |
| 其他 | skills.sh | 否；运行`npx skills update`，新技能再运行`add` |

<!-- zh-CN:end bc478b4eeacc3bf0 -->

Sources (2026-10-08): Codex `core-plugins/src/manager.rs`; Copilot [cli-config-dir-reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference); VS Code `pluginAutoUpdate.ts`; Gemini `skillLoader.ts`.

<!-- zh-CN:begin 7d06c91134b7fab1 -->

来源（2026-10-08）：Codex `core-plugins/src/manager.rs`；Copilot [cli-config-dir-reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference)；VS Code `pluginAutoUpdate.ts`；Gemini `skillLoader.ts`。

<!-- zh-CN:end 7d06c91134b7fab1 -->

Nobody has run Auggie, Droid, Qwen or Goose against this repo, so they stay on skills.sh until someone does.

<!-- zh-CN:begin 6d65f32e6afb0ffd -->

尚未用Auggie、Droid、Qwen或Goose测试本仓库，因此它们继续用skills.sh，直到有人验证。

<!-- zh-CN:end 6d65f32e6afb0ffd -->

## Claude Code

<!-- zh-CN:begin cb6fac0abca41bc6 -->

## Claude Code（中文说明）

<!-- zh-CN:end cb6fac0abca41bc6 -->

<canonical-block name="claude-code">

<!-- zh-CN:begin 5b817db51c829342 -->

<canonical-block name="claude-code"> <!-- 中文结构说明 -->

<!-- zh-CN:end 5b817db51c829342 -->

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```

Updates itself by default.

<!-- zh-CN:begin 08069ce4190843bf -->

默认自动更新。

<!-- zh-CN:end 08069ce4190843bf -->

</canonical-block>

<!-- zh-CN:begin 43e20131c6de2468 -->

</canonical-block> <!-- 中文结构说明 -->

<!-- zh-CN:end 43e20131c6de2468 -->

## Codex

<!-- zh-CN:begin fb0cc0778903acfb -->

## Codex（中文说明）

<!-- zh-CN:end fb0cc0778903acfb -->

<canonical-block name="codex">

<!-- zh-CN:begin b68e689a204811aa -->

<canonical-block name="codex"> <!-- 中文结构说明 -->

<!-- zh-CN:end b68e689a204811aa -->

```bash
codex plugin marketplace add mattpocock/skills
codex plugin add mattpocock-skills@mattpocock
```

Updates itself at startup.

<!-- zh-CN:begin a9febaf03706ffe2 -->

启动时自动更新。

<!-- zh-CN:end a9febaf03706ffe2 -->

</canonical-block>

<!-- zh-CN:begin 130ba454b90a6b4f -->

</canonical-block> <!-- 中文结构说明 -->

<!-- zh-CN:end 130ba454b90a6b4f -->

## GitHub Copilot (CLI and VS Code)

<!-- zh-CN:begin d3eda1380d2d8858 -->

## GitHub Copilot（CLI与VS Code）

<!-- zh-CN:end d3eda1380d2d8858 -->

Use the marketplace, not `copilot plugin install mattpocock/skills`. Copilot has deprecated direct repo installs, and they can't auto-update. The `extraKnownMarketplaces` entry follows the documented schema, but nobody has run it yet.

<!-- zh-CN:begin c5ddb22736f6897e -->

使用市场，不要用`copilot plugin install mattpocock/skills`。Copilot已弃用直接仓库安装且不能自动更新。`extraKnownMarketplaces`按文档schema设置，但尚未实际运行验证。

<!-- zh-CN:end c5ddb22736f6897e -->

<canonical-block name="copilot">

<!-- zh-CN:begin ef6099a60f36b6b2 -->

<canonical-block name="copilot"> <!-- 中文结构说明 -->

<!-- zh-CN:end ef6099a60f36b6b2 -->

```bash
copilot plugin marketplace add mattpocock/skills
copilot plugin install mattpocock-skills@mattpocock
```

Then, once, add to `~/.copilot/settings.json`:

<!-- zh-CN:begin 202f327f02827032 -->

然后一次性把以下内容加入`~/.copilot/settings.json`：

<!-- zh-CN:end 202f327f02827032 -->

```json
{
  "extraKnownMarketplaces": {
    "mattpocock": { "source": { "source": "github", "repo": "mattpocock/skills" }, "autoUpdate": true }
  }
}
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/mattpocock/skills`. It updates daily.

<!-- zh-CN:begin ac261cb91a42504f -->

VS Code中运行**Chat: Install Plugin From Source**并输入`https://github.com/mattpocock/skills`；每日更新。

<!-- zh-CN:end ac261cb91a42504f -->

</canonical-block>

<!-- zh-CN:begin bd261482e0ddf9f9 -->

</canonical-block> <!-- 中文结构说明 -->

<!-- zh-CN:end bd261482e0ddf9f9 -->

## Gemini CLI

<!-- zh-CN:begin 7701d6d35a07b691 -->

## Gemini CLI（中文说明）

<!-- zh-CN:end 7701d6d35a07b691 -->

Gemini doesn't read `.claude-plugin`, and `--path` takes one bucket. One install per promoted bucket gives exactly the promoted set (27 skills, verified 2026-10-07).

<!-- zh-CN:begin c3b5878b4e613fa1 -->

Gemini不读`.claude-plugin`，`--path`每次只接受一个桶。每个已晋升桶安装一次正好得到已晋升集（27个技能，2026-10-07验证）。

<!-- zh-CN:end c3b5878b4e613fa1 -->

<canonical-block name="gemini">

<!-- zh-CN:begin dbac7ea9ee6c65d6 -->

<canonical-block name="gemini"> <!-- 中文结构说明 -->

<!-- zh-CN:end dbac7ea9ee6c65d6 -->

```bash
gemini skills install https://github.com/mattpocock/skills.git --path skills/engineering
gemini skills install https://github.com/mattpocock/skills.git --path skills/productivity
```

Re-run both commands to update.

<!-- zh-CN:begin 9733792ba2eae3bb -->

重跑两条命令更新。

<!-- zh-CN:end 9733792ba2eae3bb -->

</canonical-block>

<!-- zh-CN:begin efbd73a759a8a6f2 -->

</canonical-block> <!-- 中文结构说明 -->

<!-- zh-CN:end efbd73a759a8a6f2 -->

## Every other agent, or editable files (skills.sh)

<!-- zh-CN:begin 5ac22e94df949b05 -->

## 其他代理或可编辑文件（skills.sh）

<!-- zh-CN:end 5ac22e94df949b05 -->

`-a` preselects the agent. Each agent in the comment was run on 2026-10-07. Prefer skills.sh to an agent's own repo installer, such as `amp skill add` or `pi install git:…`, because those also pull in `misc/` and `in-progress/`. `npx skills update` skips skills added upstream since `add`, so the block tells users to re-run `add`.

<!-- zh-CN:begin b29cd757597405bd -->

`-a`预选代理；注释中每个代理均在2026-10-07运行验证。优先skills.sh而非代理自带仓库安装器（如`amp skill add`或`pi install git:…`），后者还会拉入`misc/`和`in-progress/`。`npx skills update`不会添加上游新增而`add`之后出现的技能，因此需重跑`add`。

<!-- zh-CN:end b29cd757597405bd -->

<canonical-block name="other-agents">

<!-- zh-CN:begin 3d07deb26553848e -->

<canonical-block name="other-agents"> <!-- 中文结构说明 -->

<!-- zh-CN:end 3d07deb26553848e -->

```bash
npx skills@latest add mattpocock/skills -a <agent>  # cursor, opencode, devin, windsurf, amp, pi; omit -a to choose
```

<!-- zh-CN:begin ee8fc3838c2cdb25 -->

```bash
npx skills@latest add mattpocock/skills -a <agent>  # cursor、opencode、devin、windsurf、amp、pi；省略 -a 可交互选择
```

<!-- zh-CN:end ee8fc3838c2cdb25 -->

When the installer asks which skills to take, include `setup-matt-pocock-skills`. To update, run `npx skills@latest update`, and re-run `add` to pick up new skills.

<!-- zh-CN:begin e7b43b9514f1284a -->

安装器询问选择哪些技能时包含`setup-matt-pocock-skills`。更新运行`npx skills@latest update`，再运行`add`获取新技能。

<!-- zh-CN:end e7b43b9514f1284a -->

</canonical-block>

<!-- zh-CN:begin 7580302beeaa36cd -->

</canonical-block> <!-- 中文结构说明 -->

<!-- zh-CN:end 7580302beeaa36cd -->

Use the single-skill form wherever one skill is named on its own. `docs/` pages don't use this block, because ai-hero renders the install widget above the page body. See [writing-docs.md](./writing-docs.md).

<!-- zh-CN:begin b47a9a816b0e57ed -->

单独提到一个技能时使用单技能形式。`docs/`页面不用此安装区块，因为ai-hero把安装控件渲染在正文上方；参见[writing-docs.md](./writing-docs.md)。

<!-- zh-CN:end b47a9a816b0e57ed -->

<canonical-block name="skills-sh-one-skill">

<!-- zh-CN:begin 51226efbbbceeccf -->

<canonical-block name="skills-sh-one-skill"> <!-- 中文结构说明 -->

<!-- zh-CN:end 51226efbbbceeccf -->

```bash
npx skills@latest add mattpocock/skills --skill=<name>
```

```bash
npx skills@latest update <name>
```

</canonical-block>

<!-- zh-CN:begin d91aa3aa71e443e7 -->

</canonical-block> <!-- 中文结构说明 -->

<!-- zh-CN:end d91aa3aa71e443e7 -->

`skills@latest` is the pinned spelling everywhere.

<!-- zh-CN:begin c606a871a34f4ab5 -->

各处固定写作`skills@latest`。

<!-- zh-CN:end c606a871a34f4ab5 -->

## The two routes are exclusive

<!-- zh-CN:begin 53f8efa344b71006 -->

## 两条路线互斥

<!-- zh-CN:end 53f8efa344b71006 -->

The plugin is a managed, read-only bundle you subscribe to. skills.sh writes files you own and edit. Installing both leaves the user with every skill twice: always say "pick one".

<!-- zh-CN:begin 9bea72c9d6da660a -->

插件是托管的只读订阅包；skills.sh写入你拥有并编辑的文件。同时安装会让每个技能出现两次，因此始终说“选一种”。

<!-- zh-CN:end 9bea72c9d6da660a -->
