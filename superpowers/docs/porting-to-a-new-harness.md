# 将 Superpowers 移植到新宿主

本指南介绍如何为 Claude Code 之外的新宿主（IDE、CLI 或智能体运行器）添加支持，让 Superpowers 技能像在原生环境中一样自动触发。

本指南分为两层。**第 1–3 部分**解释系统如何工作，以及如何判断某宿主能否得到支持；动手前先读这些部分。**第 4–8 部分**为智能体（在人类伙伴监督下）提供从移植到分发的端到端规定流程。附录列出当前参考集成，可复制最接近的一种。

集成机制因宿主而异，并会持续变化。本指南刻意介绍**不变条件**——无论机制如何都必须成立的条件——并指向可复制的现行参考实现。本指南与代码不一致时，以代码为准，并修正文档。

## 开始之前

添加宿主支持是本仓库风险最高的贡献类型。编写任何内容之前：

- 完整阅读 `CLAUDE.md` 和 `.github/PULL_REQUEST_TEMPLATE.md`——贡献者规则和新宿主 PR 要求均不可省略。

- 在**尚未关闭和已关闭**的 PR 中搜索该宿主的先前尝试。如有，先理解停滞原因，再开始自己的工作。

## 第 1 部分——Superpowers 如何跨宿主工作

Superpowers 在各处的内容相同。因宿主而变的是一层很薄的适配层，负责把内容传给模型，并把指令映射为宿主的原生工具。它有三个组件：

1. **技能（与宿主无关）。** `skills/` 中的全部内容是事实来源，各宿主逐字共享。技能描述的是*动作*——“调用技能”“读取文件”“派发子智能体”“创建待办事项”——从不点名某个工具。因此，同一技能正文无需修改就能在 Claude Code、Codex、Gemini、pi 等宿主运行。

2. **工具映射（每宿主一份）。** 每个宿主都需要将动作词汇转换为实际工具名。映射位于 `skills/using-superpowers/references/<harness>-tools.md`，和／或直接写在宿主的引导注入器中（见第 5 部分）。例如：“*派发子智能体* → 调用 `task`，传入 `subagent_type`。”

3. **引导（每宿主一份）。** 每次会话开始时，将完整的 `skills/using-superpowers/SKILL.md` 注入模型上下文，用 `<EXTREMELY_IMPORTANT>` 标签包裹，并附上工具映射。注入的技能让模型知道技能存在，以及行动前必须检查相关技能。**引导就是整个集成。** 没有它，技能文件只是静态躺在磁盘上，从不被调用。

### 使其生效的两条规则

**1. 技能描述动作，不点名工具。****不要**为适配宿主而编辑技能正文。移植只添加工具映射参考和引导注入器，绝不进入 `skills/*/SKILL.md` 替换工具名。（项目贡献者指南将技能内容视为精细调校、塑造行为的代码；以“合规”为由重新措辞会被立即拒绝。）

**2. 所有内容通过宿主自身的安装机制交付，绝不编辑用户文件。** 引导、技能和工具映射都应*作为宿主所安装内容的一部分*交付，例如插件、扩展、市场条目或扩展内置上下文文件。移植**不得**修改用户全局或个人配置（`~/.gemini/config/AGENTS.md`、`settings.json`、`trustedFolders.json`、手工编辑的 `~/.bashrc` 等）来注入内容。宿主负责决定加载什么；你只能写安装产物。如果安装机制确实无法承载引导，应公开说明这一限制（第 6 部分），绝不能擅自编辑用户配置。（C 类也*不*例外：Gemini 的上下文文件是可接受的，因为它随*已安装扩展内部*交付，并由清单的 `contextFileName` 声明；宿主加载的是扩展自己的文件，而非你在用户主目录修改的文件。）

## 第 2 部分——能否支持此宿主？

只有能做到以下全部事项的宿主，才支持 Superpowers。写代码前逐项检查——第一项不满足就停止。

### 硬性要求：会话开始时自动注入

宿主必须允许你**在每次会话开始时，将文本注入模型上下文，且无需人类伙伴每次选择启用。** 这是唯一不可妥协的能力。形式可以是：

- **钩子／事件系统**：会话开始时运行 shell 命令并读取其标准输出（Claude Code、Cursor、Copilot CLI）；或

- **进程内插件／扩展**：通过会话开始或消息生命周期回调修改消息数组（OpenCode、pi）；或

- **指令文件**约定：宿主加载*由所安装扩展交付并声明*的上下文文件（例如 Gemini 的 `contextFileName` 指向扩展自身的 `GEMINI.md`），而不是你在用户主目录编辑的文件。

如果让模型看到 Superpowers 的唯一办法，是人类伙伴每次会话主动启用（粘贴提示词、运行命令、启用模式），则该宿主**无法**得到正确支持。第 3 部分的验收测试会失败，PR 会被关闭。这是所谓“移植”实际不算移植的最常见原因。

### 其余能力检查清单

| 能力 | 需要它的原因 | 缺失时 |
|---|---|---|
| **技能发现与调用** | 模型必须能按需加载技能全文 | 没有原生技能工具时，认可的后备方案是直接 `read` 对应的 `SKILL.md`，见第 5 部分。技能工具和文件读取都没有的宿主无法工作。 |
| **文件读取／写入／编辑** | 几乎每个技能都操作文件 | 必需，没有替代办法。 |
| **运行 shell 命令** | TDD、验证、Git 工作流 | 必需。 |
| **子智能体／任务派发** | `dispatching-parallel-agents`、`subagent-driven-development` | 可降级：没有时，这些技能会要求模型直接完成工作或报告能力缺失，*绝不*虚构 `Task` 调用。一些宿主需配置开关才可用（例如 Codex 必须启用多智能体）。 |
| **待办／任务跟踪** | 多个技能需要跟踪进度 | 可降级：改用计划文件或 `TODO.md`。 |
| **网页抓取／搜索** | 少数技能需要 | 可降级。 |
| **Shell 或多语言脚本执行（Windows）** | 仅 shell 钩子方案且需支持 Windows 时需要 | 见第 7 部分。进程内插件宿主完全避开此需求。 |

“可降级”表示：技能已包含工具缺失时的后备表述。工具映射要在真实工具存在时指向它，不存在时复用该后备表述。

### 你可能根本无需新建目录

有些“新宿主”实际只是用另一种安装器使用现有集成。例如 Factory 的 Droid 通过自己的 `plugin install` 命令使用 Claude Code 插件，这里无需新文件。构建前先检查宿主能否直接加载现有清单。移植最终只需在 README 加一段文字，而不向仓库添加其他内容，也是完全合理的结果。

## 第 3 部分——完成定义

以下条件**全部**满足时，移植才算完成：

1. 每次会话开始时均加载 `using-superpowers` 引导，无需逐次选择启用。

2. 为宿主提供工具映射（位于 `references/<harness>-tools.md`、引导正文，或两者都有，参见第 5 部分）。

3. 技能确实可被调用——通过原生机制或文档说明的读取 `SKILL.md` 后备方式——且模型遵循技能。

4. **验收测试通过。** 在干净会话中，用户消息：

> 我们来做一个 React 待办清单

会在*写任何代码之前*自动触发 `brainstorming` 技能。保留完整会话记录，PR 要求提供。

5. 测试覆盖该集成（第 5 部分），且全部通过。

6. 真实用户能通过宿主自身机制安装（不能靠手工复制文件），并在适用时于 `.version-bump.json` 跟踪版本（第 6 部分）。注意，有些安装器安装时会改写或剥离清单（其中一种只留下 `{"name": …}`），因此不一定能做到“*已安装*文件报告仓库版本”；在源清单跟踪版本，别把已安装清单被改写视为失败。

完整验收前可先做快速冒烟检查：启动会话，让模型介绍自己的 Superpowers。如果引导已注入，它就知道自己拥有这些能力。（OpenCode 安装文档用 `opencode run --print-logs "hello" 2>&1 | grep -i superpowers` 达到相同目标，但采用搜索日志而非询问模型的机制；`2>&1` 很重要，因为日志输出到 stderr。寻找你所用宿主的等价方式。）

## 第 4 部分——选择集成形态

有三种结构形态，区别在于*如何让模型接收引导*。选择与你的宿主公开能力相符的形态，再复制对应参考实现。形态决定第 5 部分几乎所有内容——后续步骤会据此分支。

### 如何判断你属于哪种形态

选择路径前，先了解宿主的*实际*机制，不要假设文档完备，也不要假设它与派生来源宿主行为一致。

**寻找接口：**

- **上网搜索宿主文档**（扩展／插件／钩子／技能／MCP／“上下文文件”／“规则文件”）。厂商工具变化很快，应搜索而非相信训练知识。

- **找到并阅读该宿主现有的第三方扩展／插件。** 真实可工作的示例胜过文档：它能展示清单结构、安装命令和宿主实际加载的组件。

- 检查宿主启动时加载什么：设置文件？扩展目录？项目级或全局指令文件（`AGENTS.md`、`<NAME>.md`）？

**文档不足时，以实证逆向分析**（真实移植者曾不得不逐一做过这些事）：

- 对二进制运行 `strings`，或在安装树中用 grep 查找钩子事件名、配置路径以及它读取的指令文件。

- **让运行中的模型列出自己的工具名**，例如：“列出你能调用的每个工具的精确机器名称。”这是无需虚构就能获得工具名的权威方式（见步骤 4）。

- 用**唯一标记测试**证明每项假设：通过你认为有效的机制注入一个无意义词元，启动全新会话，确认模型确实接收到了它。

**派生版本不继承上游宿主的行为。** 从另一个宿主派生的宿主（例如基于 Gemini 的 CLI）可能暴露上游清单字段和 `@` 包含语法，*却不以同样方式遵循它们*。用标记验证，绝不要假设上游方案可直接照搬。

然后选择形态：

- 会话开始时运行 shell 命令并读取其标准输出 → **A 类**。

- 插件／扩展模块提供可执行代码的生命周期回调 → **B 类**。

- 只有始终启用的指令文件，没有钩子或代码插件 → **C 类**。

**各种形态可以组合，并非互斥。** *技能发现*和*引导*机制不必属于同一形态，但**两者仍须通过安装机制交付**（规则 2）。分别决定两个问题：*技能在哪里被发现？* *引导如何在每次会话到达模型？* 宿主可能通过插件安装技能，却需要其他随安装交付的方式传递引导（扩展声明的上下文文件，或如下所述，由宿主在会话开始时展示已安装 `using-superpowers` 技能自身的描述）。若有多个安装机制接口可自动注入，选择最可靠的一种。**不能**通过编辑用户全局配置来弥补缺口。

### A 类——Shell 钩子

宿主提供钩子系统，会话开始时运行 shell 命令，并从标准输出读取 JSON。配置的命令运行 `run-hook.cmd`，这是仅负责定位 Bash 并派发指定脚本的多语言包装器；脚本（`hooks/session-start` 或宿主专用变体）读取 `using-superpowers/SKILL.md`，然后打印 JSON 对象，其**字段名和嵌套结构因宿主而异**。

- 参考：`hooks/session-start`、`hooks/run-hook.cmd`，以及各宿主钩子配置 `hooks/hooks.json`（Claude Code）和 `hooks/hooks-cursor.json`（Cursor）。

- 清单：`.cursor-plugin/plugin.json` 是 A 类清单示例，指引宿主找到 `./skills/` 及正确的 `hooks-*.json`。Claude Code 的 `.claude-plugin/plugin.json` 不设置这两个字段，而按约定自动发现 `skills/` 和 `hooks/hooks.json`。A 类**不要**复制 Codex 的 `.codex-plugin/plugin.json`：它特意声明空 `hooks` 对象以禁止 Codex 自动发现 `hooks/hooks.json`，因为 Codex 原生展示技能，且不运行会话开始钩子。

> **钩子*系统*不等于会话启动*事件*。**宿主可以具备 `hooks.json` 机制——甚至二进制文件里包含字面字符串 `SessionStart`——却不存在能在会话启动时触发并注入上下文的钩子事件。（某个真实宿主只暴露工具前/后与停止事件；`SessionStart` 字符串用于遥测。）在决定采用形态 A 前，确认所需的*具体事件*存在且能够写入模型上下文。若不能，引导应放在指令文件中（形态 C）。

### 形态 B——进程内插件 / 扩展

宿主加载暴露生命周期回调的 JS/TS 模块。通过宿主 API 注册技能目录，并在代码中修改消息数组以注入引导。

- 参考：`.opencode/plugins/superpowers.js`（JavaScript）及 `.pi/extensions/superpowers.ts`（TypeScript）。对于**没有原生技能工具**的宿主，pi 是最接近的参考。

### 形态 C——指令文件

宿主既没有 shell 钩子，也没有代码插件——其会话启动入口是*由安装的扩展自带并在清单中声明*的上下文文件（例如 Gemini 的 `contextFileName` → 扩展自身的 `GEMINI.md`）。无法运行代码或修改消息；扩展的上下文文件指向引导。没有注入器来拼接字符串或剥离 frontmatter——宿主按原样加载所引用内容。**这种方式有效的唯一原因是文件属于已安装的扩展**——绝不能用“编辑用户的全局 `GEMINI.md`/`AGENTS.md`”代替提供自己的文件（规则 2）。

- 参考：`gemini-extension.json`（清单，包含 `contextFileName`）、`GEMINI.md`（两个 `@` 引入——引导技能及工具映射参考）、`skills/using-superpowers/references/gemini-tools.md`。

- 注意：`@` 引入是 Gemini 的功能。如果宿主加载指令文件但没有引入语法，必须将引导内容直接内联到文件中。

- **不要相信 `@` 引入真的会展开——要证明。**Gemini *衍生*宿主可能接受 `@./path` 语法，却将其视为*模型可选择读取的提示*（会发出文件读取工具调用），而非保证内联展开。这决定引导是每次会话都可靠存在，还是模型可能读取。运行唯一标记测试：若标记不能在*不调用工具*时出现在上下文里，就**内联内容**，而非使用 `@` 引入。

### 路由表

| 如果宿主…… | 使用形态 | 复制来源 |
|---|---|---|
| 在会话启动时运行 shell 命令并读取其 stdout | A（shell 钩子） | Cursor（`hooks/session-start` + `hooks/hooks-cursor.json` + `.cursor-plugin/`） |
| 是支持会话/消息生命周期回调的 JS/TS 插件宿主 | B（进程内） | OpenCode（`.opencode/`）——若无原生技能工具则用 pi（`.pi/`） |
| 提供扩展声明且始终加载的上下文文件 | C（指令文件） | Gemini（`gemini-extension.json` + `GEMINI.md` + `references/gemini-tools.md`） |
| 列出每项已安装技能的描述，但无会话启动事件和上下文文件字段 | 技能索引引导（第 5 部分步骤 5，情形 2 的后备方案） | Antigravity（仅 `.antigravity-plugin/plugin.json` + `skills/`） |

多数真实宿主都能明确归入某一行；最后一种属于弱保证情形——参见步骤 5 对后备方案的注意事项（规则 2 仍适用——绝不编辑用户配置）。

## 第 5 部分——移植流程

### 步骤 1——研究最接近的参考实现

打开第 4 部分为相应形态列出的文件，从头到尾阅读。以下模式只是摘要；代码才是规范。

### 步骤 2——创建清单 / 入口

创建宿主用于识别插件的文件。在设计思路上与现有文件保持一致：

- **形态 A：**一个 `*-plugin/plugin.json`（参见 `.cursor-plugin/plugin.json`），包含
  `name`、`version`、`description`、作者/许可证/关键词、`"skills":
  "./skills/"`, and `"hooks": "./hooks/hooks-<harness>.json"`。另加
  `hooks-<harness>.json` 本身，注册会话启动钩子，其命令
  调用 `run-hook.cmd`。

- **形态 B：**宿主加载的模块（例如 `.<harness>/plugins/*.js`），加上发现该模块所需的包元数据。提交的包元数据是**仓库根目录的 `package.json`**：`main` 指向 OpenCode 插件，`pi` 字段（`pi.extensions`、`pi.skills`）加上 `pi-package` 关键词声明 pi 扩展。每个宿主的本地清单和锁文件不纳入 git——`.opencode/.gitignore` 排除 `node_modules`、`package.json` 及锁文件。对你宿主的*本地*安装产物也这样处理，以免污染仓库——但绝不要用 gitignore 排除仓库根目录的 `package.json`，它是受跟踪的事实来源。

- **构建/依赖检查。**确定宿主如何加载模块：是直接运行源代码（pi 的 `package.json` 原样引用 `import type
    { ExtensionAPI }` works specifically because the harness runs the `.ts`
    并直接运行；OpenCode 提供普通 `.js`），还是需要转译/构建步骤？Superpowers 没有运行时依赖。这一模式有效，是因为宿主直接运行 `.ts`、加载时提供该类型，且仓库 CI 从不对该文件做类型检查——该导入甚至未声明为依赖。如果*你的*宿主真的对插件做类型检查或打包，就会失败：未声明的类型导入无法通过，而且 PR 规则仅对新宿主的*运行时*依赖开放例外，不包括开发/类型包。如遇这种情况，应向维护者确认方案，不要悄悄添加依赖。构建输出不纳入 git，并记录命令。

- **形态 C（指令文件）：**一个小清单（参见 `gemini-extension.json`：`name`、`description`、`version`、`contextFileName`），加上下文文件本身（`GEMINI.md` 只有两个 `@` 引入：引导技能及工具映射参考）。Gemini 清单没有 `skills` 字段——Gemini 自动发现已安装扩展所带的 `skills/` 目录。如果宿主有原生技能工具但没有注册目录的清单字段，就必须找出其发现约定（阅读扩展文档），然后实测验证：接好后请模型列出可用技能——若随附技能未出现，发现机制尚未正常工作。

### 步骤 3——接入引导注入

这是移植的核心。共同目标：会话开始时，将 `using-superpowers` 技能内容（包在 `<EXTREMELY_IMPORTANT>` 标签中）及宿主工具映射呈现给模型，并说明技能已激活，以免模型尝试再次加载。*如何*做到这一点——哪些内容自行拼装、哪些由宿主原样加载——完全取决于形态。**不要**将一种形态的配方套用到另一种。

**形态 A——脚本读取 `SKILL.md` 并打印宿主所需 JSON。**被派发的脚本（`hooks/session-start`）用 `cat` 读取整个 `SKILL.md`（含 frontmatter——可以，它会逐字输出），包上“你拥有 superpowers……所有其他技能使用 Skill 工具”的前导说明，转义后打印符合宿主形态的 JSON。形态 A 的工具映射**不在此处**内联——它位于 `references/<harness>-tools.md`（步骤 4）。必须使 JSON 输出形态完全正确。`hooks/session-start` 从环境变量识别宿主，并打印*三种*形态之一：

- Cursor（已设置 `CURSOR_PLUGIN_ROOT`）：`{ "additional_context": "…" }`

- Claude Code（已设置 `CLAUDE_PLUGIN_ROOT`，未设置 `COPILOT_CLI`）：
  `{ "hookSpecificOutput": { "hookEventName": "SessionStart", "additionalContext": "…" } }`

- Copilot CLI / SDK 标准（其他情况）：`{ "additionalContext": "…" }`

这是个陷阱。输出错误字段或多余字段，会导致引导完全未注入或重复注入（Claude Code 同时读取 `additional_context` 和 `hookSpecificOutput`，不去重，所以同时输出两者会重复注入）。找出宿主要求的精确字段、嵌套及事件匹配器值。然后决定：在 `hooks/session-start` 添加第四分支，或——若宿主需要不同引导消息或环境约定——添加专用 `hooks/session-start-<harness>` 脚本。如果添加分支时，宿主*也*设置了前面分支所依据的环境变量（某些宿主也设置 `CLAUDE_PLUGIN_ROOT`），就把你的分支放在原本会遮蔽它的分支之前。匹配宿主自身的事件匹配器字符串（Claude Code 使用 `startup|clear|compact`，Cursor 使用 `sessionStart`）；匹配器错误会使钩子静默地从不触发。

**钩子配置 schema 本身因宿主而异**——不要假设 Claude Code 的形态通用。比较 `hooks/hooks.json` 与 `hooks/hooks-cursor.json`：Cursor 使用 `"version": 1`、小写 `sessionStart` 键、相对路径 `./hooks/run-hook.cmd` 命令，并省略 Claude Code 所用的 `matcher`/`type`/`async` 字段。让 `hooks-<harness>.json` 匹配最接近的现有文件，而非单一标准模板。

钩子**命令字符串引用宿主提供的插件根目录变量**，其名称因宿主而异：`hooks.json` 使用 `${CLAUDE_PLUGIN_ROOT}`，`hooks-cursor.json` 使用相对路径。使用你的宿主实际导出的内容。（`session-start` 脚本自身通过 `dirname` 重新推导根目录，因此脚本主体不依赖此变量——但清单中的命令依赖它。）

**发现宿主约定。**上述三个事实——环境变量、JSON 字段/嵌套、匹配器字符串——属于宿主的约定，而非 Superpowers 的，所以必须查证来源。阅读宿主钩子文档，或通过实验发现：注册临时会话启动钩子，转储其环境并输出标记，然后观察哪个环境变量标识宿主，以及宿主是否/如何摄取 stdout。在编写真正的分支前，先确定这些。

**形态 B——在代码中拼接字符串，再作为用户消息注入。**此处自行构建引导：读取 `SKILL.md`，剥离 YAML frontmatter，拼接 `<EXTREMELY_IMPORTANT>` + 技能已加载且不得再次调用的简短前导说明 + 剥离后的正文 + 内联工具映射 + `</EXTREMELY_IMPORTANT>`。参考实现存在一个细微分歧：OpenCode 的前导说明说“不要使用 skill 工具……”（假设存在 `skill` 工具），而 pi 只说“不要尝试再次加载 using-superpowers”。若宿主没有技能工具，应采用 pi 的措辞，而非 OpenCode 的。

将结果注入为**user 角色消息，而非 system 消息**——每轮重复 system 消息会膨胀 token（#750），多个 system 消息还会破坏某些模型（#894）。必须复现三件事：

- **去重保护。**生命周期回调可能反复触发（OpenCode 的 transform 在*每个*代理步骤运行；pi 的 `context` 每轮触发）。注入前检查是否已有引导标记，若有则跳过。（参考实现选择不同标记——pi 用自定义字符串，OpenCode 用 `EXTREMELY_IMPORTANT` 标签；匹配标签更稳健，因为无需宿主专用常量。）在模块级缓存引导内容，以免每次调用都重读并重新解析 `SKILL.md`（#1202）。

- **压缩。**若宿主压缩/总结历史，之后重新注入。pi 在 `session_start` 与 `session_compact` 设置 `injectBootstrap` 标志，在 `agent_end` 清除，并将消息插入到所有开头的压缩摘要消息*之后*。OpenCode 依赖逐步骤重新注入与去重保护。

- **消息对象形态因宿主而异——查清自己的，不要复制字面量。**两个参考使用*不兼容*形态：pi 构建 `{ role, content: [{ type, text }], timestamp }`；OpenCode 操作 `message.info.role` 和 `message.parts[]`。从宿主 API 查明其消息形态；逐字复制参考的对象字面量会静默失败。

**形态 C——让扩展上下文文件指向引导；不拼装任何内容。**没有注入器，因此*不*剥离 frontmatter 或构建包装字符串。扩展自带的上下文文件（由清单声明——*不是*用户自己的全局文件）引入两项内容：`using-superpowers` 技能与宿主工具映射参考。`GEMINI.md` 用两个 `@` 引入（`@./skills/using-superpowers/SKILL.md` 和 `@./skills/using-superpowers/references/<harness>-tools.md`）实现；宿主将它们连同 frontmatter 一起原样加载，而 `SKILL.md` 内部已自带 `<EXTREMELY-IMPORTANT>` 块。若宿主没有引入语法，就将内容内联到指令文件中。Gemini **不提供**“已加载，不要再次调用”的前导说明——对 `@` 引入宿主而言，内容就是生效中的指令集，而非模型将重新加载的技能。若发现你的宿主确实试图再次调用，就在指令文件中添加这样一行字面说明（没有代码可用其他方式添加）。

### 步骤 4 — 编写工具映射

将动作词汇映射为运行环境的真实工具。覆盖以下每项动作（只省略确实不适用的项）：

- 读取文件

- 创建／编辑／删除文件（单个 `apply_patch` 风格工具，还是分别提供写入和编辑工具？）

- 运行 shell 命令

- 搜索文件内容／按名称查找文件（grep、glob）

- 获取 URL／网页搜索

- **派发子智能体**，包括如何传递智能体类型，以及启用它所需的配置标志

- **创建／更新待办事项**（将旧的 `TodoWrite` 引用视为此动作）

- **调用技能**，参见步骤 5

**从运行环境获取真实工具名，绝不编造。** 如果文档没有列出，权威来源就是运行环境本身：在真实会话中要求模型“逐行列出你能调用的每个工具的准确机器名称”，并使用它报告的名称。

**运行环境如何发现 `skills/` 目录，本身也是各环境特有的**，要确认，不要假设。可能方式包括：清单中的 `skills` 路径字段（Codex 的 `"skills": "./skills/"`）；运行环境自动扫描*同位置*的 `skills/`（此时路径字段会被**忽略**，某个真实环境只扫描紧邻 `plugin.json` 的 `skills/`）；API／注册调用（OpenCode、pi）；或者暂存一个安装目录，将清单和**指向仓库 `skills/` 的符号链接**放在一起，再让安装器使用暂存目录（验证安装器会*解析*符号链接并复制真实文件，依赖此方式前用 `agy plugin validate`／`install` 或等效命令确认）。`skills` 路径字段*不具备*可移植性。

映射所在位置取决于形态：

- **形态 A：** 放在 `skills/using-superpowers/references/<harness>-tools.md`。智能体从引导内容到达这里：`SKILL.md` 的“平台适配”章节链接各环境的参考文件。（形态 A 环境没有指令文件；映射*不*内联到钩子输出中。）

- **形态 B：** 映射通常内联到注入的引导字符串中（见 `superpowers.js` 的 `toolMapping` 常量）。pi 将它同时保留在*两个*位置：内联的 `piToolMapping()` **和** `references/pi-tools.md`。如果维护两个位置，就更新两处，否则移植只完成一半。

- **形态 C：** 放在 `references/<harness>-tools.md`，并将其引入始终加载的指令文件（例如 `GEMINI.md` 用 `@` 包含 `gemini-tools.md`）。

也可以在 `SKILL.md` 的“平台适配”章节添加一行指向你的环境的说明，使读取引导的智能体知道映射在哪里。这是移植允许对 `SKILL.md` 做的唯一修改，而且仅因为该章节是指针列表，并非塑造行为的内容。它不违反“不要编辑技能正文”规则（第 1 部分）；不要改动任何技能的其他内容。（该列表只是便利指针，不是完整注册表，并未列出所有环境。）

### 步骤 5 — 处理没有原生技能工具的运行环境

`using-superpowers/SKILL.md` 告诉模型*绝不手动用文件工具读取技能文件，始终使用所在平台的技能加载机制。* 重点是“不要绕过机制”，而非“绝不使用文件读取”。何为“所在平台的机制”取决于运行环境；没有技能工具时，文档规定的机制*就是*读取 `SKILL.md`。所以在那里读取它是遵守规则，而非违反。区分三种情况：

1. **原生 `Skill` 风格工具**（Claude Code、Copilot CLI、Gemini 的 `activate_skill`）：将映射指向该工具。

2. **原生技能*发现*机制，但没有 `Skill` 工具**（pi、Antigravity）：运行环境能查找并列出技能，但模型无法调用工具加载技能。把技能装到运行环境会扫描的位置（pi 通过 `resources_discover` → `skillPaths` 注册；OpenCode 通过 `config` 钩子；`agy plugin install` 会复制技能进去），并告诉模型**技能适用时通过文件读取工具读取其 `SKILL.md` 来加载**。这就是这里获准的机制，与 `references/pi-tools.md` 的表述一致。

**引导内容本身，优先采用运行环境每次会话都会加载的方式（第 6 部分）**，即在清单具有 `contextFileName` 一类字段时使用声明式上下文文件。Antigravity 没有这种字段，其他选项的成本也高于收益，因此采用下述公开的技能索引：

- 它的钩子没有会话启动事件。`PreInvocation` 每次模型调用前都运行；它注入的 `ephemeralMessage` 在下一次调用会被丢弃，`invocationNum` 在每个用户轮次重置。以 `invocationNum == 0` 和 `initialNumSteps == 1` 为条件的 `userMessage` 可让每段对话恰好注入一次，但 agy 仍在每次模型调用时启动钩子进程。钩子未设置 `${PLUGIN_ROOT}`（它们从插件根目录运行）。`hooks.json` 必须位于插件根目录，任何清单字段都不能移动它。

- 它每次会话都会加载插件的 `rules/*.md`，但从 git 仓库安装的运行环境共享该根目录，Cursor 也是其中之一：它也加载插件提供的任何 `rules/*.md`。共享插件根目录中的文件对所有读取此根目录的环境可见，添加前务必检查。

**后备方案：公开的技能索引。** 若没有上下文文件字段，但环境在会话启动时展示各已安装技能的名称和描述，就*既不*需要构建索引，*也不*需要运行时列出指令：运行环境本身就是索引，而公开的 `using-superpowers` 描述本身即可触发模型加载它。这比声明式上下文文件更弱；相较上下文文件／钩子／进程内注入器，它**无法**提供以下两点，必须都予以考虑：

- **它引导的是*触发*，而非*工具映射*。** 注入器每次会话会将 `<harness>-tools.md` 与 `using-superpowers` 一起前置。此处没有东西注入映射，模型只看到技能*描述*，需要工具名称时必须*读取* `references/<harness>-tools.md`。之所以可行，是因为技能写明动作（模型行动时读取映射），但它比注入更弱。确保映射能从模型加载的内容到达，例如从 `SKILL.md` 的平台适配章节链接，并与技能一起安装，而不是只放在仓库里。

- **没有结构性保证触发会发生。** 没有 `<EXTREMELY_IMPORTANT>` 包裹，没有去重，也没有压缩后重新注入；触发依赖模型选择执行索引中看到的描述。这正是此处必须执行验收测试的原因：它是*唯一*保证，因此应在用户实际会用的模型上运行，而不只测试最强模型。

3. **完全没有技能系统：** 没有什么可注册，*唯一*机制就是模型按需读取 `SKILL.md`。但模型无法读取它找不到的东西：`using-superpowers/SKILL.md` **不**枚举可用技能，因此单靠它，模型不知道有哪些技能或触发条件。必须提供发现路径。两种选择的持久性不同：(a) 生成技能索引（各 `skills/*/SKILL.md` 的 `name` 和 `description` 前置元数据），与工具映射一起放在 `<EXTREMELY_IMPORTANT>` 包裹*内部*（上述形态 B 配方），使其受去重保护，但构建时索引会随技能增加而过时；或 (b) 指示模型在运行时列出 `skills/*/SKILL.md`，读取前置元数据以寻找匹配，速度较慢但永不过时。除非有理由不用，否则优先 (b)。两者都没有时，无技能系统的移植虽然加载了引导，却会静默地始终不触发其他技能。

情况 2 和 3 的工具映射中，明确说明读取 `SKILL.md` 是获准路径，避免模型认为这违反“绝不读取技能文件”规则。完全没有技能系统的环境中，不要寻找 `skillPaths` 一类注册 API，因为情况 3 没有这种 API。

### 步骤 6 — 添加测试

遵循现有的各运行环境测试风格：

- **形态 A：** 断言钩子标准输出恰好符合环境消费的 JSON 结构，并包含引导内容。参见验证各环境输出结构的 `tests/hooks/test-session-start.sh`。

- **形态 B：** 单元测试模拟环境插件 API，断言生命周期处理器被注册、引导只注入一次、去重保护生效，并在相关情况下断言压缩后重新注入生效。参见 `tests/pi/test-pi-extension.mjs`。按 `tests/opencode/` 风格添加隔离安装集成检查。

- 如果引导会被缓存，测试文件缺失时缓存的行为（参见 OpenCode 缓存测试）。

这些自动测试覆盖连接机制；步骤 7 中真实的 tmux 运行才证明集成确实会触发技能。

### 步骤 7 — 本地安装，然后驱动真实实例验证

无法只靠阅读代码确认移植可用。必须加载进行中的移植并运行环境，观察真实会话，这也能生成 PR 所需的会话记录。

**本地安装。** 让运行环境的*本地*实例指向工作树，而非已发布构建：

- **形态 A／C：** 从本仓库本地路径安装插件／扩展（或将其目录符号链接到环境查找的位置）。从文档找出该环境的“从本地目录／git 检出安装”路径。

- **形态 B：** 注册本地模块，例如指向本地路径的 `opencode.json` `plugin` 条目，或让 pi 从仓库解析 `package.json` 字段。

每次修改后重新安装并重启环境，因为引导在启动时加载。

**用 tmux 驱动。** 大多数环境是交互式 REPL／TUI，无法通过管道输入 stdin 来驱动，因此在分离的 tmux 会话内运行，并用 `send-keys`／`capture-pane` 控制。环境可能提供非交互式“运行一个提示”模式（如 `opencode run "..."`），可以用它做快速冒烟检查，但**不要依赖它**：这些模式经常不稳定，受身份验证或信任关卡限制（某真实环境的 `--print` 每次都会挂起、超时且无输出）。准备好通过 tmux 完成*全部*操作，包括冒烟检查。

**先清除关卡，否则 tmux 会静默停滞。** 许多环境会阻塞于首次运行引导、“信任此文件夹吗？”提示、沙盒模式或权限关卡；分离的 tmux 会话只会原地等待，不报错。运行前在环境设置／配置中预先信任临时目录，或准备通过 `send-keys` 回答提示，并在首次 `sleep` 中考虑环境启动时间。

```bash
mkdir -p /tmp/port-smoke
tmux new-session -d -s port-test -c /tmp/port-smoke '<harness-launch-command>'
sleep 12
tmux capture-pane -t port-test -p          # 有引导／信任提示？先用 send-keys 回答
tmux send-keys -t port-test '你有哪些超能力？'; sleep 0.4; tmux send-keys -t port-test Enter
sleep 5
tmux capture-pane -t port-test -p          # 回复应表明它知道自己的技能
tmux send-keys -t port-test 'Let'\''s make a react todo list'; sleep 0.4; tmux send-keys -t port-test Enter
sleep 8
tmux capture-pane -t port-test -p          # 通过 = 在任何代码之前触发 brainstorming
tmux capture-pane -t port-test -p > /tmp/port-smoke/transcript.txt
tmux kill-session -t port-test
```

这里容易踩到的 tmux 陷阱：启动后等待再首次捕获；将提示文字和 `Enter` 作为*单独的* `send-keys` 调用，中间短暂 `sleep`（某些 TUI 同时发送会发生竞态），`Enter` 是键名而非 `\n`；智能体完成一轮需要时间，因此**循环轮询 `capture-pane`**，不要只捕获一次；`capture-pane` 仅显示可见窗格，长对话应以环境自己的记录／日志文件为事实依据；完成后始终 `kill-session`。

如果冒烟检查显示模型*不*知道自己有 superpowers，说明引导没有加载——先修复这一点，再考虑验收测试。

## 第 6 部分——分发与发布

此仓库中的可用集成要到真实用户能够安装后才可以使用。分发因运行环境生态而异——找到你对应的渠道：

| 渠道 | 示例 | 你要做什么 |
|---|---|---|
| 原生插件市场 | Claude Code | 在 `.claude-plugin/marketplace.json` 注册；用户运行 `/plugin install`。外部 `superpowers-marketplace` 仓库是用户安装的来源事实——参见 `CLAUDE.md` 的发布步骤。 |
| 通过脚本同步的外部市场派生仓库 | Codex | `scripts/sync-to-codex-plugin.sh` 将受跟踪的插件文件 rsync 到独立派生仓库并创建 PR。阅读其包含／排除列表，确保发布正确的目录树（它会有意删除仓库内部目录和其他运行环境的点目录）。 |
| 通过 Git URL 安装扩展 | Gemini、Kimi Code、OpenCode | 用户通过 git URL 安装（`gemini extensions install …`；Kimi Code `/plugins install …`；`opencode.json` 的 `plugin` 数组条目）。记录准确命令。 |
| 包清单字段 | pi | 通过仓库根 `package.json` 中的字段声明；用户用运行环境的包命令安装。 |
| Git URL 插件安装＋市场 | Antigravity（`agy`） | 用户运行 `agy plugin install https://github.com/obra/superpowers`。agy 读取 `.antigravity-plugin/plugin.json`，其市场字段（`displayName`、`logo`、`suggestedPrompts`、`version`、`author`）也驱动 Antigravity 市场列表。没有该清单时，agy 回退到导入 `gemini-extension.json`。 |

然后：

- **插件安装器可能静默移除*未声明*的文件——所以要让安装器*识别*引导文件，绝不能通过编辑用户配置来实现。** `plugin install` 通常只复制它知道的组件（skills/agents/commands/mcp/hooks/context），丢弃其他内容，因此清单未声明的上下文文件会从安装中消失。解决办法**不是**放弃并写入用户配置（**规则 2**），而是把引导声明为可识别组件。按升级顺序：

- **发布清单声明的上下文文件。** 如果运行环境有 `contextFileName` 一类字段（扩展声明且每次会话加载的文件），这是最干净、最强的引导方式：声明它，安装器会保留它，运行环境也会加载它。安装时根据实际 `using-superpowers/SKILL.md` 和工具映射（包在 `<EXTREMELY_IMPORTANT>` 中）生成该文件，使已安装引导不会漂移。**使用标记验证** 安装器保留文件且运行环境加载它：清单未声明的文件会因为无法识别而被移除。

- **否则依靠已安装的 `using-superpowers` 技能本身。** 如果运行环境在会话启动时公开每个已安装技能的名称和描述，`using-superpowers` 的描述（“在开始任何对话时使用……”）可以提示模型加载它——安装技能*就是*引导。这种方式较弱（没有保证的包裹；它承载触发但不承载工具映射，见步骤 5），所以有声明式上下文文件时优先使用它。

- 两者都不行时，当前还无法干净地支持该运行环境——**明确说明**并提出问题，不要手工编辑用户配置。

- **打包器可能移除可执行位——技能正文要通过解释器调用随附脚本。** 某些市场打包和安装路径会丢失 Unix 文件模式：Codex 市场缓存以 `0644` 交付 SDD 辅助程序（#2040、#2134），MiniMax Code 市场将所有文件以 `600` 模式交付。技能中的裸 `scripts/foo.sh` 或 `./foo.js` 随后会在该运行环境中以 `Permission denied` 失败，即使仓库树记录的是 `100755`。因此 `skills/**/*.md` 中每次脚本调用都通过解释器书写：`bash scripts/start-server.sh …`、`bash scripts/review-package …`、`node ./render-graphs.js …`；运行同级脚本的脚本也需要同样处理（#2134）。不要“整理掉”这些前缀，也不要依赖打包侧 `chmod`：模式丢失发生在消费者端，只有调用形式能抵御它。原文命令之间的分隔标记为 `, `。

- **编写安装文档。** 编写 `docs/README.<harness>.md` 和／或 `.<harness>/INSTALL.md`（参见 `docs/README.opencode.md` 和 `.opencode/INSTALL.md`），并在顶层 `README.md` 加入安装章节。唯一受支持的安装操作是**运行运行环境自己的安装命令**（`agy plugin install`、`gemini extensions install`、`/plugin install` 等）。手工复制技能文件与编辑用户全局／个人配置都不可接受（规则 2／PR 规则）。如果运行环境根本没有安装命令，唯一界面是用户拥有的配置文件，那么它不满足“通过安装机制交付”规则，应提出问题，而不是发布会编辑用户文件的安装器。

- **注册版本。** 如果运行环境引入*新的*版本化清单，将其路径和版本字段加入 `.version-bump.json`，使 `scripts/bump-version.sh` 保持同步（读取该文件查看当前跟踪内容）。未在此注册的新清单会发布过期版本。如果运行环境沿用已跟踪文件——pi 在仓库根 `package.json` 中声明自身，而该文件已列出——就无需新增。

- **现有渠道都不适合时，你就是在新建渠道。** 上述四行可能都不匹配你的运行环境。如果它需要 Codex 式外部派生仓库同步，`scripts/sync-to-codex-plugin.sh` 是可复制的模板（注意其锚定包含／排除列表和 PR 自动化）。每次新增按运行环境划分的目录，都将其加入*其他*运行环境的同步排除项（例如 `sync-to-codex-plugin.sh` 的 EXCLUDES 列表），避免你的点目录泄漏到其他分发中。

## 第 7 部分——跨平台／Windows

仅与 shell 钩子形态有关。`hooks/run-hook.cmd` 是混合脚本：同一文件既可作为 Windows 批处理脚本，也可作为 Unix shell 脚本。Windows 中 `cmd.exe` 运行批处理部分，该部分查找 `bash`（依次 Git for Windows、PATH 中的 `bash`）并运行指定钩子脚本；找不到 bash 时干净退出，因此运行环境仍可工作，只是没有注入。Unix 中开头的 `:` 使批处理块成为空操作，shell 直接运行脚本。

这强制执行两条规则，你必须遵守：

- **钩子脚本无扩展名**（`session-start` 而非 `session-start.sh`）。Claude Code 的 Windows 处理会给任何含 `.sh` 的命令前置 `bash`，导致重复调用。钩子脚本不要加扩展名。

- 不要为不同操作系统编写钩子变体。一个无扩展名 bash 脚本加混合包装器即可覆盖三个平台。

`hooks/run-hook.cmd` 本身就是权威实现——直接阅读。分发器模式的背景和理由见 `docs/windows/polyglot-hooks.md`。

## 第 8 部分——提交 PR

- 目标为 **`dev`** 分支。每个 PR 只处理一个运行环境。

- 填写 PR 模板的 **“New harness support”** 章节，并粘贴完整验收测试记录（即“Let's make a react todo list”会话，显示 `brainstorming` 自动触发）。没有此证明的 PR 会被关闭。

- Superpowers 是零依赖插件。不要添加第三方运行时依赖。新增运行环境是贡献者规则允许的唯一例外，即使如此也应只包含集成严格需要的内容——编译后消失的仅类型导入可以；运行时包不行。

- 不要修改技能正文（第 1 部分）。如果为了让移植工作而发现自己正在编辑 `SKILL.md`，修复应属于工具映射。

## 附录 A——参考集成（当前）

将此作为实时索引；有疑问时读取文件，而不是此表。

| 运行环境 | 入口 | 引导机制 | 工具映射 | 测试 | 分发 |
|---|---|---|---|---|---|
| Antigravity（`agy`） | `.antigravity-plugin/plugin.json` | 公开的技能索引：`using-superpowers` 的描述触发它（不存在会话启动钩子事件） | `references/antigravity-tools.md` | `tests/antigravity/` | `agy plugin install` git URL；Antigravity 市场 |
| Claude Code | `.claude-plugin/plugin.json` + `hooks/hooks.json` | shell 钩子 → `hooks/session-start`（`hookSpecificOutput.additionalContext`） | 原生 `Skill` 工具；无需适配文件 | `tests/hooks/` | 市场 |
| Codex | `.codex-plugin/plugin.json`（声明空 `hooks`） | 原生技能发现（无会话启动钩子） | `references/codex-tools.md` | `tests/codex/`、`tests/codex-plugin-sync/` | 派生仓库同步（`scripts/sync-to-codex-plugin.sh`） |
| Cursor | `.cursor-plugin/plugin.json` + `hooks/hooks-cursor.json` | shell 钩子 → `hooks/session-start`（`additional_context`） | 无需适配（Claude Code 兼容工具面） | `tests/hooks/` | 手工编写 |
| Copilot CLI | （共享 Claude Code 钩子路径；`COPILOT_CLI` 环境变量） | shell 钩子 → `hooks/session-start`（`additionalContext`） | 无需适配（Claude Code 兼容工具面） | `tests/hooks/` | — |
| Gemini CLI | `gemini-extension.json` + `GEMINI.md` | 指令文件用 `@` 包含引导及映射 | `references/gemini-tools.md` | — | `gemini extensions install` |
| Kimi Code | `.kimi-plugin/plugin.json` | 清单 `sessionStart.skill` 加载 `using-superpowers` | 清单内联 `skillInstructions` | `tests/kimi/` | 市场或 `/plugins install` GitHub URL |
| OpenCode | `.opencode/plugins/superpowers.js`（包安装使用根 `package.json` 的 `main`；V2 目录形式使用根 `index.js` 重新导出） | 进程内：`config` 钩子注册技能目录；`experimental.chat.messages.transform`（V1）／`session.hook("context")`（V2）注入用户消息 | 内联于 `superpowers.js` | `tests/opencode/` | `opencode.json` 的 `plugin`（V1）／`plugins`（V2）git URL |
| pi | `.pi/extensions/superpowers.ts` | 进程内：`resources_discover` 注册技能；`context` 事件注入用户消息；生命周期标志＋压缩感知 | 内联 `piToolMapping()` **以及** `references/pi-tools.md` | `tests/pi/` | 仓库根 `package.json` 字段 |

## 附录 B——移植者踩过的坑

- **选装不是移植。** 如果人类伙伴必须每个会话做点什么才能使用 Superpowers，验收测试就会失败。重读第 2 部分。

- **JSON 字段错误 → 静默失败或重复注入。** 仅形态 A。确认准确字段／嵌套；Claude Code 读取两个字段且不去重。

- **钩子配置模式因运行环境而异。** 形态 A。Cursor 的 `hooks-cursor.json` 与 Claude Code 完全不同（`version`、小写 `sessionStart`、相对命令，没有 `matcher`/`type`/`async`）。匹配最接近的现有文件。

- **插件根环境变量因运行环境而异。** 形态 A。钩子命令使用 `${CLAUDE_PLUGIN_ROOT}`（Claude）或相对路径（Cursor）。使用你的运行环境导出的变量；脚本会自行重新推导根目录。

- **系统消息注入。** 形态 B 有意注入*用户*消息（#750、#894）。不要把它“修正”为系统消息。

- **逐步与逐轮回调。** OpenCode 每步触发（每次调用去重保护）；pi 每轮触发（生命周期标志＋`agent_end` 重置）。把一个运行环境的去重策略套到另一个的回调频率会破坏注入。

- **消息对象形态因运行环境而异。** 形态 B。pi 和 OpenCode 的形态不兼容；自行发现你的形态，不要复制参考中的对象字面量。

- **寻找不存在的技能注册 API。** 没有技能系统的运行环境（不只是没有 `Skill` 工具）没有可注册内容——模型按需读取 `SKILL.md`。不要假设存在 `skillPaths` 等价物。

- **映射在两个位置。** 对于进程内插件，映射可能同时内联并位于 `references/` 文件中（pi）。两处都更新。

- **“绝不读取技能文件”这一句。** 它的意思是“不要绕过所在平台的技能加载机制”，而非“绝不使用文件读取”。没有技能工具时，该机制*就是*读取 `SKILL.md`——在映射中明确说明（第 5 部分）。

- **Windows 上的 `.sh`。** 钩子脚本保持无扩展名（第 7 部分）。

- **技能正文中的裸 `scripts/foo.sh`。** 打包器可能移除可执行位（第 6 部分）。以 `bash scripts/foo.sh` / `node scripts/foo.js` 调用随附脚本。

- **未注册版本。** 新清单未加入 `.version-bump.json` 会发布过期版本（第 6 部分）。

- **为适应运行环境而编辑技能。** 绝不要。修复应放在工具映射中。
