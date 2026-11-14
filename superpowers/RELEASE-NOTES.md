# Superpowers 发布说明

本版本在 v7.0.0 重建后重新调整了头脑风暴。很多用户指出，新版默认问题很快就令人厌烦，感觉公式化，这些意见是对的。头脑风暴现在先深入查找上下文，再提出问题，并尝试问得更好。我们预计会继续调整，但认为它已经有所改善。

本版本还精简了三个长技能，使其在 Claude Code 的上下文压缩后保留得更完整，并修改 issue 和 PR 模板，要求提供由人类撰写的摘要。

### 头脑风暴

- **先深入查找上下文。**在现有项目中，或你提供规范、计划、文件时，它会在第一条消息前先阅读，不再询问其中已回答的问题。（#2560）

- **尝试提出更好的问题。**v7.0.0 每次会话都用相同方式开场：先提议跳过提问，再泛泛询问“你希望它存在的那一刻”。现在，如果你已经说明想要什么，它会结合项目中找到的信息复述请求，再询问唯一尚未明确之处。后续问题基于你的回答与它找到的信息，并说明答案会改变什么。（#2560、#2571）

- **仅在自行启动时才提供跳过提问的选项。**若你明确点名头脑风暴或使用 `/brainstorming`，它不再提议跳过。（#2560）

- **构建前列出方案并撰写设计文档。**它会提出两三种构建方式、推荐一种，并请你选择。然后撰写设计文档，小改动则写短文档，获准前不构建任何内容。有些用户遇到过它跳过文档直接构建；在我们的一个测试场景中，修改前 24 次运行全部未经询问就跳过文档，修改后为 24 次中 3 次。（#2571）

感谢 @mbcrawfo 发起 #2530，也感谢 @katyatitkova、@ertra、@blorenz、@Biomaj、@fsalum、@technicalpickles、@orochi235、@alexxburg、@fcavalieri、@CelesteCunha 及 @zzzzz9999 在其中提供报告、记录和测试。

如果 7.0.1 的头脑风暴问题仍不合适，请在 #2530 评论。示例最有帮助：你问了什么，它反问了什么，以及你希望它问什么。

### 技能在 Claude Code 压缩后保留得更完整

压缩后，Claude Code 会重新附加每项技能，但在 20,000 个字符处截断，所以后面的内容在会话剩余时间里都会丢失。在一份报告的会话中，子代理驱动开发丢失了五轮上限，对一个任务执行了 18 轮修复。感谢 @dan-1492 的报告。（#2481）

- **`subagent-driven-development`** 将修复循环、最终审查、报告处理、恢复、预检、批处理及无法验证的指导移入 `references/`。在需要的步骤从磁盘读取对应文件。（#2565）

- **`writing-skills`** 将配套文档、SKILL.md 模板与发现指导、加固指导及流程图约定移入 `references/`。（#2564）

- **`executing-plans`** 删除了重复上文规则的示例工作流。（#2563）

- `tests/skill-size/test-skill-size.sh` 在任何 `SKILL.md` 达到 20,000 字节时失败。（#2565）

### 贡献

- **issue 与 PR 模板现在要求说明提交者是谁、人类伙伴要求了什么，以及由人类撰写的少于 200 词的摘要。**缺陷报告还要求说明如何确认未使用 Superpowers 时问题不会出现。（#2569）

- **除非维护者要求，否则不接受代理编写、用于修复他人 issue 的 PR。**若你的人类伙伴遇到相同问题，请将其报告补充到现有 issue。PR 模板、`AGENTS.md` 和 README 均已说明。（#2569）

- **`diagnosing-superpowers` 在草拟的 issue 中添加相同的两部分**，且摘要仍为占位符时不会提交。其预填链接现在打开缺陷报告模板；我们删除了会话诊断报告模板。（#2569）

我们从头重建了头脑风暴，让它更好地履行一贯目的：在构建任何内容前，帮助你弄清真正想要什么并表达出来。新技能请你描述目标与原因，复述理解以便你纠正，并不断提出好问题，直到图景清晰。随后根据工作调整流程，从直接执行到撰写完整设计。

本版本还为 Antigravity Marketplace 添加原生插件清单，并修复 Windows 钩子发现、Git Bash 路径、Hermes 技能描述及若干小缺陷。

### 头脑风暴

- **头脑风暴会在提出任何方案前引导你说明需求。**首条消息提供跳过提问的选项，并提出一个关于真实时刻或具体图景的开放问题。只有你卡住时才提供菜单。过程中，它会提议查看既有方案、你的项目或网络。理解每部分后，会用几百字复述，并将猜测明确标为猜测。（#2463）

- **理解需求后评估工作规模，并用简单语言说明。**对快速、明确的任务立即执行；小改动在聊天中与你达成一致；项目则写设计文档。你可覆盖它的判断，工作扩大时它会提高规模级别。（#2463）

- **构建者检查取代规范文档审查者。**全新子代理以实施者身份阅读设计，列出仍需询问的事项。头脑风暴回答能回答的，独立决定小问题并注明由其决定，将会改变构建内容的问题一次性提交给你。（#2463）

- **找出哪些制作方式的选择需要由你掌控。**平台、语言、库、媒介：若你有明确意见，它会充分讨论；若你授权决定，它会选择合理默认值并告知。即使跳过提问也会这样做。此改动源于某次会话：设计了 iOS 应用，却从未询问平台，最后构建了 Web 应用。（#2482、#2483）

- **只要观看比阅读更有帮助，就提供可视化伴侣：**屏幕、布局、流程、外观不同的选项、图表。提议中删除了 token 成本警告。（#2463）

- **可视化伴侣现在能完整显示含 `$'`、`$&` 等序列的屏幕。**服务器此前用 `String.replace` 插入内容，会将这些序列视为替换模式。现在按字面插入内容。感谢 @andrew-yian 的报告和 @luochen211 的修复。（#2362、#2364）

### Antigravity 平台

- **`agy plugin install https://github.com/obra/superpowers` 现在将 Superpowers 安装为原生 Antigravity 插件。**我们添加了 `.antigravity-plugin/plugin.json`，包含 Marketplace 显示名称、标志及建议提示词。此前 agy 回退为将仓库导入 Gemini CLI 扩展，然后每次会话都拒绝复制来的 Claude 格式钩子文件，报错 `invalid hook "hooks": command hook must specify 'command'`（无效的 hooks 钩子：命令钩子必须指定 command）。安装命令不变。（#2479）

- **Superpowers 在 Antigravity 上通过技能发现进行引导。**Antigravity 没有会话启动钩子事件，但会向模型展示每项已安装技能的描述，而 `using-superpowers` 的“开始任何会话时使用”会提示模型加载它。我们在 agy 1.3.1 上进行了 12 次运行验证：“来做一个 react 待办列表”和“添加设置页面”都会在写代码前触发头脑风暴，失败测试会在编辑前触发 systematic-debugging。我们还纠正了 README 与移植指南，它们曾描述从未存在的会话启动钩子与安装脚本。（#2479）

### 钩子

- **宿主以损坏的 `PATH` 启动时，SessionStart 现在也能工作。**钩子不再通过 `PATH` 查找 `dirname`、`cat` 或 `bash`，所以启动 `PATH` 无法解析这些命令（anthropics/claude-code#43127）不再导致引导丢失。感谢 @kannan983 的报告和 Ada Sen 的修复。（#2310、#2349）

- **Windows：`run-hook.cmd` 能找到按用户安装的 Git for Windows，并跳过 WSL 启动器。**现在会检查 `%LOCALAPPDATA%\Programs\Git`，搜索 `PATH` 时跳过没有 Linux 发行版就会失败的 WSL `bash.exe` 启动器。感谢 @jp5247 的报告，以及 @citizen204（#1864）和 @KaiyiQuan（#2365）的修复，我们在此合并了这些方案。（#1863、#2393）

- **Windows：`run-hook.cmd` 忽略当前目录中的 `bash` 和 `where`。**此前仓库可放置 `bash.cmd` 或 `where.bat`，使其在会话开始时执行。（#2393）

- **Windows：`run-hook.cmd` 现在将钩子退出码传给宿主。**此前即使钩子失败也会报告成功。（#2393）

### 子代理驱动开发

- **`sdd-workspace` 不再改动仓库自身的 `.superpowers/sdd/.gitignore`。**此前每次运行都用 `*` 覆盖文件，撤销仓库提交的任何版本（例如为跟踪 `progress.md` 账本而设的版本）。现在仅在文件不存在时写入默认值。感谢 @aruizcu1989 的修复。（#2161、#2399）

- **Windows 上的计划标记保持仓库相对路径。**在 Git Bash 中，`sdd-workspace` 将 `git rev-parse` 的 `C:/…` 根目录与计划的 `/c/…` 路径比较，导致每个工作区标记记录机器专属绝对路径。现在以与计划路径相同的方式解析根目录。我们在合入 @t0domanh 的 Windows 测试修复时发现此问题（#2149）。

### 执行计划

- **`task-done` 现在会记录测试命令静默通过的任务。**通过命令不输出任何内容时，`task-done` 会以 1 退出且不写账本行，导致已完成任务看似未完成。现在记录 `→ (no output)`（无输出）。感谢 @KenM-BT 的报告和 Ada Sen 的修复。（#2385、#2388）

### 请求代码审查

- **示例中的 base-SHA 命令在技能带参数时仍有效。**Claude Code 将技能正文中的 `$1` 替换为第二个参数词，所以带参数调用技能会将 `awk '{print $1}'` 变成 `awk '{print <word>}'`。示例现在使用不含 `$` 的 `cut -d' ' -f1`。感谢 @errmakov 的报告和 @klemens-floege 的修复。（#2311、#2361）

### 系统化调试

- **多层诊断示例不再打印被检查的秘密值。**`${IDENTITY:+SET}${IDENTITY:-UNSET}` 和 `env | grep IDENTITY` 都会将签名身份的值回显到日志。现在示例只报告变量是否已设置。感谢 @kennyg-g 的报告和 @m2dumpling 的修复。（#2375、#2380）

### Hermes 代理

- **Hermes 技能列表现在显示 Superpowers 技能描述。**Hermes 使用传给 `register_skill` 的描述列出每项插件技能，描述默认空。此前插件只传名称和路径，所以每项技能都显示空白，模型无从选择。现在插件传入各技能的 frontmatter 描述。感谢 @pepijn-blom 的修复。（#2284）

`writing-plans` 能更快生成更精简的计划。计划现在记录实现者所需决策（签名、测试断言、规范值），而非写出代码。某些前沿模型，包括 Opus 5.5，在编写计划时可能过度积极，在某些提示下甚至一边设计计划一边试图实现整个项目。新技能让规划专注于计划。我们复现原始报告后，临时构建消失，计划耗时降至四分之一，token 约为三分之一。感谢 Harper Reed 提供报告与会话包。（#2333）

### 编写计划

- **计划记录决策，不是代码的逐字稿。**“步骤包含什么”取代“无占位符”部分。测试步骤给出测试名称与断言；代码步骤给出精确签名、文件及规范值，只有这些信息无法确定算法时才附函数体；验证步骤给出命令及通过时输出；引用其他任务时通过该任务的 Interfaces 块。占位符仍被指出为相反方向的失败。（#2333）

- **自审检查篇幅比例。**计划比较自身与规范的长度。比规范长数倍的计划是逐字稿；代码块占主导时，将函数体替换为签名与测试断言。（#2333）

- **计划读者被描述为有能力的工程师：**知道精确接口与测试后就能写出符合惯用法的代码。这取代“零上下文、品味存疑”的描述。步骤大小现在是“一个具有可检查结果的动作”，而非“2-5 分钟”。（#2333）

- 新技能编写的每份计划在 Sonnet 5 上对植入缺陷探针均取得 9/9 的执行结果，与完整代码计划相同。（#2333）

- 删除 `plan-document-reviewer-prompt.md`。没有内容引用它。（#2333）

### 文档

- 删除 `CLAUDE.md`。Claude Code 现在直接读取 `AGENTS.md`，但仅在不存在 `CLAUDE.md` 时，因此保留那一行指针会隐藏真正的指导。

v6.4.0 从未发布。v6.4.1 是首个包含这些改动的版本。它暂缓发布新的 `proving-it-works-with-a-movie` 技能，该技能正进行清理与稳健性改进，将在后续版本回归。

新的 `diagnosing-superpowers` 技能找出会话中出了什么问题。`executing-plans` 重建为原生执行，即比子代理驱动更便宜的替代。此次还支持三个新平台：OpenCode 2.0、Muse 和 Qwen Code。

### 新技能

- **`diagnosing-superpowers`**：会话出问题时（重复工作、忽略计划、技能未触发、意外账单），让代理“查明本会话 superpowers 哪里出错。” 它与你确定问题，读取磁盘转录，并用 `path:line` 证据报告每项发现。经要求可生成清洗包或起草 GitHub 议题供批准，保留引用证据。当前或过去会话均可。（#2236、#2287）

### 执行计划

**注意：** `executing-plans` 不再每几任务停下确认；它运行整个计划，末尾做一次审查。

- **原生（内联）执行现为真实模式。** 过去 64 行存根与无插件运行效果相同；现已重建：会话在同一工作区、台账和停止规则下自行实现每项任务，再由最强模型对整分支审查。`task-start`、`task-done` 保持台账与测试日志真实。这是最便宜的计划执行方式，适合中档会话模型。（#2318）；其中相关的字段或标识包括 `executing-plans`。

- **计划交接提供子代理驱动和原生两种方式**，说明成本，并按计划推荐一种；已有选择会保留。（#2258、#2318）

### 编写计划

- **运行前审查已保存计划。** 批准想法或范围不等于批准未见的计划。（#2258）

- **计划带审查重点节**：列出规格暗示但无任务测试覆盖的最多五个输入/失败模式，每项由拥有代码的任务测试固定。评估中所有实现者都在未命名输入上遇到相同崩溃；该节用于捕获它。（#2319）

### 头脑风暴

- **先弄清为何想要，再提功能**，复述意图供纠正，并把批准绑定到实际设计与计划阶段。有会话把“范围可以”误认为搭架许可。（#2258）

### 代码审查

- **审查者按合理用户预期判断规格未提行为**，未命名输入崩溃不再被列为次要。另列“拒绝判断”清单，由运行计划的会话逐项决定。（#2319）

- 多提交 `BASE_SHA` 备选现为 `git merge-base origin/main HEAD`；裸 `origin/main` 会在主线推进后把新文件伪装成删除。（#2133、#2118）

### 测试驱动开发

- **项目套件才能定义绿色，不只是测试文件。** 任务只点名一个文件时，12 次探测有 11 次只跑该文件，旁边坏测试未被发现。技能现在要求运行项目测试命令并逐个报告失败，包括非你造成者。（#2110）

### 子代理驱动开发

- **同名计划不再共用工作区。** `docs/alpha/plan.md` 与 `docs/beta/plan.md` 曾解析到同一目录，简报互相覆盖。现在记录所属计划，冲突用独立目录，旧工作区原地接管。（#2138、#2045）；其中相关的字段或标识包括 `task-brief`。

- **`review-package` 拒绝空或非后代 `BASE..HEAD` 范围**（退出 3），错误分支提交无法生成“干净”的零内容审查。（#2136、#2050）

- **Claude Code 控制器可下沉一层**，作为中层模型嵌套子代理；成本与墙钟约减半。需主动选择，适合协调模型太贵的会话。（#2320）

### 新平台支持

- **OpenCode 2.0.4+** 与 V1 并存，技能经 V2 原生 API 注册；bootstrap 在续接、重启、fork、压缩后保留，委派子会话不继承控制器 bootstrap。（#2106、#2306）

- **Muse**：原生插件清单和 SessionStart 钩子。依次运行 `muse plugins install ./`、`muse plugins approve superpowers`。（#2317）

- **Qwen Code** 加入安装文档：`qwen extensions install obra/superpowers`。（#2132）

### 修复

- **打包器移除执行位时技能仍可用。** Codex 市场和 MiniMax Code 重打包让脚本不可执行，文档命令报 `Permission denied`。技能现通过解释器调用：`bash scripts/foo.sh`、`node render-graphs.js`，SDD 辅助脚本也如此。（#2301、#2134、#2040）

- 平台支持议题模板使用存在的 `new-harness` 标签。（#2250）

### 文档

- `docs/testing.md` 描述 Quorum 评估实验室，替代过时 Drill 引用和命令。（#2135）

- README 增加“出问题时”节，指向 `diagnosing-superpowers`。

- **`AGENTS.md` 成为规范贡献指南**，`CLAUDE.md` 只一行引用。旧 `AGENTS.md` 是符号链接，Muse 安装器拒绝。（#2317）；其中相关的字段或标识包括 `CLAUDE.md`。

- 采用 Prime Radiant 社区行为准则。（#2122）

### 平台支持

- **Devin CLI**：`devin plugins install obra/superpowers` 现可用，技能在会话开始时自动触发。（#1995）

- **Hermes Agent**：从 git clone 安装；技能经原生加载器注册，bootstrap 首轮加载。（#1922、#2025）

- **Grok Build CLI** 加入安装文档。（#1919）

### 头脑风暴

- **仪式随任务规模变化。** 请求分为 spike、有界、架构级；小任务跳过双文档。所有路径仍在实施前等批准。（#2063）

### 子代理驱动开发

- **控制器不再因计划冲突停滞。** 非灾难冲突和含糊处记录裁定继续；仅破坏性或不可逆动作停下。曾有会话在控制器可决定的问题上空等近九小时。（#2077）

- **派发前冲突扫描把检查写入台账**，而非只声称计划干净。（#2080）

- **小型同形任务合并为一次派发**，显著降低微任务成本；批审查验证简报每个文件都进入差异。（#2078）

- **实现者和审查者不得自行生成子代理**，避免重复审查。（#2059）

- **计划带 `Spec:` 指针**，SDD 在准备时读取规格，冲突按设计解决而非猜测。（#2086）

- 审查者重读看不清楚的证据而非重跑测试（#2089），断路器裁定出现在完成报告。

### Codex 平台

- 子代理等待改为事件驱动而非轮询；生成时明确模型和推理强度，并按 Codex 源码修正多代理参考。（#2060、#2061、#2062）

### 完成开发分支

- **删除工作树不再销毁未跟踪文件。** `git worktree remove` 因未提交工作拒绝时，技能停下列出文件并询问，不用 `--force`。（#2016、#1223、#2024）

### 修复

- writing-skills 的 `render-graphs.js` 支持 Windows。

- 修正 Windows 上 Copilot CLI 后台运行指导。（#1929、#2006）

- `bump-version.sh` 覆盖 Hermes 清单。

### 文档

- README 增加目录并重组入门。

### 子代理驱动开发

SDD 跟踪进度和关闭审查发现有两项结构调整，均由实时评估活动开发。

- **工作区按计划限定。** `.superpowers/sdd/` 无计划身份和生命周期，同树后续计划会把前计划台账当进度；观察到多轮污染和临时补丁。`sdd-workspace` 现要求计划文件并解析 `.superpowers/sdd/<plan-basename>/`；`task-brief`、`review-package` 写入本计划目录（后者首参数为计划文件）；台账首行命名计划；最终审查干净后删除工作区，git 历史是持久记录。基线中控制器原本拒绝外来台账，但每次恢复花 6—13 次跨计划取证；限定后结构解决。25/25 基线与绿色运行记录在 `docs/specs/`、`docs/plans/`；其中相关的字段或标识包括 `review-package`。

- **审查修复循环恢复实现者。** 修复轮采用恢复语义而非新派发，增加范围化复审提示 `re-review-prompt.md`，复审者检查修复而非重读全任务；五轮断路器，触发时控制器裁定。SKILL.md 按生命周期重组，红标转为规范合理化表。

### 技能

分支范围压缩活动：移除面向已调用读者的小结、社会证明和推销文字，承载论点折叠为合理化表或使用处。每处删减用子代理探测；一处有害删减经改写才发布。

- **`testing-anti-patterns.md` 改名 `writing-good-tests.md`**，重建为正向目录（六条先给正确示例），加入可证伪纪律：指出会失败的产线改动、独立推导预期、末尾变异检查。点名两个漏洞：字符串存在陷阱（脚本/技能/提示 grep 假证伪）和变化检测陷阱（常量断言失败却未防错）；触发范围扩到所有测试写作。平凡代码和人类文字无需测试。

- **TDD 的“为何顺序重要”保留为合理化行。** 整节删除在“先写后测”压力下降低行为（控制 8/10 → 处理 5/10，Claude/Codex 一致），因此每个反驳放入常见合理化行，代理产生念头时可见。

- **`finishing-a-development-branch` 不再提议丢弃工作。** 过去“Discard this work”紧邻“Merge”，会销毁已通过工作；现仅明确请求加输入确认可用。PR 创建改为平台无关（使用 CLI 或推送 URL），并修复清理后工作树路径重算导致来源检查失效。

- **全库移除小结与说服文字。** `brainstorming`、`systematic-debugging`、`dispatching-parallel-agents`、`verification-before-completion`、`executing-plans`、`subagent-driven-development`、`requesting-code-review`、`receiving-code-review`、`using-git-worktrees`、`writing-plans`、`writing-skills` 删除 Bottom Line/Key Principles/Real-World Impact/Advantages；两个工作树技能把防护节改为借口/现实表；其中相关的字段或标识包括 `using-git-worktrees`、`finishing-a-development-branch`。

### Windows 平台

- **SessionStart 钩子现经 Git Bash。** 命令以带引号路径开头，PowerShell 解析失败（#1751），cmd.exe 在含 `(` 时截断（#1918），bootstrap 静默不加载。钩子声明 `shell: "bash"`，Claude Code ≥2.1.81 直接解析 Git for Windows，缺失时给出安装提示；旧版本忽略键。已在 Linux、含恶意路径的 Windows 11 Git Bash 和无 Git Bash Windows 11 端到端验证。

### 平台支持

- **恢复 Gemini CLI 支持。** v6.1.0 因 Google 宣布 EOL 而过早移除；正式评估永久移除前，安装文档与 `gemini-tools.md` 工具映射恢复。（#1959）

### 修复

- **`find-polluter.sh` 现在真正找到测试文件。** `find .` 输出 `./` 前缀，文档化 `-path "src/**/*.test.ts"` 零命中，空输入 `wc -l` 却报“Found 1”。现已修正（#2008、#2011）；调用方自带 `./` 不会双前缀，`**/` 也可折叠匹配，避免漏掉 `src/top.test.ts`。新增确定性测试套件；其中相关的字段或标识包括 `src/**/*.test.ts`。

- **Codex 打包脚本支持 macOS 之外。** 修正 GNU tar 等价确定性元数据参数、固定规范文件模式，并用 `tarfile` 断言 mtime。

- **SDD 技能测试不再抖动。** 单文件超时上限升至 900 秒；断言辅助函数不区分大小写，`assert_order` 失败时输出内容便于诊断。

- **v6.1.0 参考清理后的文档与测试整理。** 替换已删除 `claude-code-tools.md`/`copilot-tools.md` 的失效链接，删除悬空锚点，Antigravity/Pi 映射测试只断言现存的平台专属表格；其中相关的字段或标识包括 `#subagent-support`。

### Codex 平台

- **Codex 不再重新注册 Claude SessionStart 钩子。** 旧清单缺 `hooks` 时回退发现仓库根 `hooks/hooks.json`，导致安装信任提示。现显式 `hooks: {}` 表示无钩子；缺失、`[]`、空内联列表仍会回退，值必须精确 `{}`；其中相关的字段或标识包括 `hooks`。

- **移除孤立 Codex 会话开始死代码。** 删除 `hooks/session-start-codex` 及其测试；shell 钩子示例移至 Cursor，修正 `docs/windows/polyglot-hooks.md` 旧指针，Codex 插件类别改为“Developer Tools”；其中相关的字段或标识包括 `docs/porting-to-a-new-harness.md`、`hooks-codex.json`。

### 打包

- **新增 `package-codex-plugin.sh`。** 生成确定性 `.zip` 或 `tar.gz`，规范时间戳、保留执行位、核验每个技能 OpenAI 元数据、包含图标、拒绝脏工作区；保留 `hooks: {}`，可从元数据重建逐字节相同归档。新增测试套件。

### 降低每会话 token 成本

`using-superpowers` bootstrap 注入每个会话，体积持续计费。此版本精简它及平台参考，同时保留影响行为的内容。

- **压缩 `using-superpowers` bootstrap。** graphviz 流程图改为文字；Instruction-Priority 并入 User Instructions；删除逐平台访问技能步骤；平台适配只保留仍有参考文件的平台。完整红标合理化表和用户指令优先规则不变。

- **精简平台工具映射。** 删除现代代理已知的动作到工具表，只保留子代理派发、任务跟踪、指令文件路径等平台专属说明；无专属内容的 `claude-code-tools.md` 与 `copilot-tools.md` 删除。

### Codex 平台

- **Codex 可从市场安装。** 新增 `.agents/plugins/marketplace.json`，指向同一根，使 Codex 找到可安装插件。

- **Codex 不再带 SessionStart 钩子。** Codex 可靠自行触发技能，钩子反而使体验变差；移除 `hooks-codex.json` 和清单注册。

### 平台支持

- **移除 Gemini CLI。** Google 于 2026-06-18 EOL；扩展无法安装更新。移除安装文档、子代理平台列表、评估描述及工具映射参考。

### 子代理驱动开发

- **SDD 临时文件移出 `.git/`。** Claude Code 保护 `.git/`，实现者写报告会被阻止。简报、报告、审查差异和台账现放入自忽略 `.superpowers/sdd/`，不进 `git status` 或提交，并按工作树解析。注意事项：`git clean -fdx` 会删台账，可凭 `git log` 恢复。（#1780）；其中相关的字段或标识包括 `.git/sdd/`、`sdd-workspace`。

### 安装修复

- **不再发布 `evals` 子模块。** 它破坏部分安装；评估 harness 移至独立仓库。（#1778、#1774）

### Codex 修复

- **头脑风暴伴侣版本显示**：打包插件无根 `package.json` 时回退 `.codex-plugin/plugin.json`；其中相关的字段或标识包括 `package.json`、`readSuperpowersVersion()`。

- **更干净的 Codex 插件同步**：排除 `.gitmodules` 和 `.pre-commit-config.yaml`。

Superpowers 6.0 是大版本。重点是重写 `subagent-driven-development` 的任务审查方式：更便宜、更严格、更难钻空子。

数字并非适用所有平台和工作量，但评估中 Claude Code 与 Codex 质量控制相近，速度约快一倍，token 约少 50%。

还新增 Kimi Code、Pi、Antigravity，改进头脑风暴可视化安全模型，并让多项技能工具调用更厂商中立。

### 可见变化

- **两个逐任务审查提示合并。** `spec-reviewer-prompt.md` 和 `code-quality-reviewer-prompt.md` 改为 `task-reviewer-prompt.md`，直接派发旧文件者应切换。

- **旧全局工作树目录移除。** 技能不再使用 `~/.config/superpowers/worktrees/`，工作树默认进入项目已有 `.worktrees/`/`worktrees/`，否则新建 `.worktrees/`；其中相关的字段或标识包括 `using-git-worktrees`、`finishing-a-development-branch`。

### 新平台支持

新增三平台，各带 bootstrap、工具映射和测试，README 各有安装节。

- **Kimi Code**：插件清单、文档和测试；从市场或仓库安装。（初始清单 @qer）

- **Pi**：会话开始扩展注册技能并注入 `using-superpowers`；Pi 原生技能无需兼容层。

- **Antigravity（`agy`）**：直接安装并在首条消息 bootstrap；用标准 React todo 验收。

### 子代理驱动开发

真实项目成本质量实验重塑控制器审查：旧流程每任务两个审查者，且控制器判模型/严重度，昂贵易被钻空；新流程一审查者、文件交接、减少控制器判断。

- **每任务一个审查者、两种结论。** `task-reviewer-prompt.md` 读差异一次，返回规格符合和质量结论，一轮修复清两项；新“无法从差异验证”标记未触及代码要求，交控制器核查。（#1538、#1543）

- **末尾一次全局审查。** 用最强模型审整分支，不再逐任务重审所有内容。

- **计划预检。** 首任务前检查内部冲突及审查会判缺陷的要求，一次提出。

- **差异和任务文本走文件。** 避免粘贴差异常驻昂贵上下文，也避免审查者重建；`task-brief`、`review-package` 写文件。

- **每次派发说明模型。** 未命名模型会继承最昂贵模型，曾把 26 个审查者都放顶级；模板现要求模型并鼓励适当选择便宜层级。

- **控制器不得要求审查者忽略。** 禁止压制发现和预评严重度；计划强制的缺陷也上报由你决定。

- **审查者只读且怀疑理由。** 不碰工作树/分支；实现者“故意不抽象”不能打消真实问题；其中相关的字段或标识包括 `git checkout`。

- **更强证据和报告。** 每结论附文件行号；报告写文件，TDD 时附红绿证据；台账支持丢上下文后恢复。（#994）

### 编写计划

计划现在携带控制器和审查者过去每次重推的结构。

- **全局约束块**逐字列出所有任务规则（版本下限、依赖限制、命名文案、确切值），确保下游可见。

- **逐任务接口块**说明输入输出，使实现者知道邻接契约。

- **规模指导**让任务足以拥有测试周期和审查，将设置、配置、文档融入需要它的任务。测试中此类计划一轮修复，对照需二至四轮并交付真实缺陷。

### 头脑风暴可视化伴侣

可视化伴侣是代理随对话打开的网页服务器。原无认证，共享/远程机器上能访问端口者可读取或注入事件。此版本加入真实安全模型，并支持重启和断线。

- **现在用每会话密钥保护一切。** 代理 URL 携带一次性密钥，浏览器存入仅标签页作用域的 cookie，每个请求和 WebSocket 连接都必须提供它。这阻止了无关本地标签页和可路由远程主机接入，也覆盖来源白名单无法捕获的 DNS 重绑定。关闭 #1014。

- **文件服务器仍限制在沙箱内。** 拒绝符号链接、点文件和任何越出内容目录的路径，忽略 macOS 资源叉文件，并发送常规 no-store 与拒绝框架头。保存会话密钥的文件仅所有者可写。

- **伴随界面只在有帮助时提供。** 某个问题用展示比用文字说更清楚时，技能首次提出，作为独立消息出现，并允许用户拒绝。接受后浏览器打开首屏。关闭 #755。

- **能在重启和连接不稳定后恢复。** 给定项目目录后，服务器在重启间保留端口和密钥，打开的标签页可直接重连。页面自行重连，显示实时状态药丸，服务器停机时显示“已暂停”覆盖层。

- **更长空闲寿命，更安全关闭。** 空闲超时由 30 分钟改为 4 小时；`stop-server.sh` 发信号前确认拥有正确进程，避免重启后误杀无关 `node`。修复 #1703。

- **Windows 启动加固**——统一 shell 检测；Node 无法在 MSYS2 间跟踪 POSIX 进程所有权，因此 Windows 改用空闲超时关闭。

### 现有运行环境更新

- **Codex** 通过自身 SessionStart hook 引导，不再使用共享接线；Codex App 增加安装章节及更完整工具文档（网页搜索、`AGENTS.md`、个人技能）。#1540

- **OpenCode** 在其插件、安装文档和 README 中获得基于动作的工具映射，并增加引导缓存测试。

- **Cursor** 清单删除 `agents` 与 `commands` 条目，因为目录已不存在。

### 一套技能，所有运行环境

技能过去使用 Claude Code 方言，如“使用 Task 工具”“放进 CLAUDE.md”。本次发布按实际动作重写词汇（“分派子代理”“你的指令文件”），并增加逐运行环境参考，将动作映射到对应工具且在各自运行时核对。原先写“Claude”的正文现在写“你的代理”。

- **各运行环境工具参考**位于 `skills/using-superpowers/references/`，覆盖 Claude Code、Codex、Copilot、Gemini、Pi、Antigravity。

- **`finishing-a-development-branch` 中立化代码托管平台**——不再硬编码 `gh pr create`，代理使用现有平台工具推送。#1609

- **一处更名：**“Claude Search Optimization”改为“Skill Discovery Optimization”，该技术不只用于 Claude。

### 编写技能

为技能作者增加两项能力。

- **让形式匹配失败**——短表帮助选择正确指导类型。单纯“不要做 X”适用于纪律失误，但输出*形态*有问题时会适得其反，示例更有效。该表和更严格的合理化章节范围引导作者选用真正有用的形式。

- **微测试措辞**——提交措辞前低成本检查：相对无指导对照采样数次并手工阅读所有结果，把逐次波动视为警告。

### 测试

技能行为测试从 `tests/` 移到基于“drill”的 `evals/` 子模块；drill 运行真实 Claude Code、Codex、Gemini 会话并用 LLM 评判。更严格场景覆盖后退役多个仓库内 bash 套件，无等价替代者保留。今后 `tests/` 放插件代码测试，`evals/` 放技能行为测试，`docs/testing.md` 说明划分。新后端覆盖 Antigravity、Pi 和更多模型，新增 shell lint 与 pre-commit 检查。#1541

### 缺陷修复

- **systematic-debugging 不再迫使每个会话进入扩展思考。** 一个条目含有 Claude Code 扫描的关键词，每次加载技能都悄悄打开开关。插入连字符可打断关键词且正文仍可读。#1283，@Nick Galatis。

- **Windows SessionStart hook 不再每次会话打印写入错误**——每个 `printf` 经 `cat` 吸收断管，输出其他部分不变。#1612，@silvertakana 报告。

- **Windows 前台模式**跟踪正确进程，并在 MSYS2 清除所属 PID。@nestorluiscamachopaz。

- **`using-superpowers` 引导**不再把“debugging”列为不存在的技能。@mhat 报告。

- **TDD 技能**链接测试反模式参考。#1532、#1529；链接修复 #1474，@Stable Genius。

- **`using-git-worktrees`** 修复步骤编号并移除陈旧 Cursor 引用。#1522，@fuleinist。

- **Codex 审查技能**用普通指导替代内部玩笑。#1531。

### 文档与贡献者指南

- **新运行环境移植指南**（`docs/porting-to-a-new-harness.md`）说明每个集成所需三部分及成败关键规则：会话开始时加载引导。

- **每个 PR 和问题现在披露制作方式**——模型、运行环境、版本和已安装插件，或注明手工编写。贡献来源会影响评估。PR 也指向 `dev`，不指向 `main`。PR 模板、三个问题模板和新平台支持模板均包含。

### 贡献者

感谢 @mattvanhorn、@nawfal、@Nick Galatis、@silvertakana、@nestorluiscamachopaz、@qer、@mhat、@Stable Genius、@fuleinist、@dev_Hakaze、@robotsnh、Rahul 和 @arittr。

### 移除内容

- **移除旧斜杠命令**——`/brainstorm`、`/execute-plan`、`/write-plan` 已删除。它们只是提示用户调用对应技能的弃用桩；现直接调用 `superpowers:brainstorming`、`superpowers:executing-plans`、`superpowers:writing-plans`。#1188

- **移除 `superpowers:code-reviewer` 命名代理**——它是插件唯一命名代理，仅两个技能使用，而其他审查／实现子代理都通过提示模板分派 `general-purpose`。代理角色和检查清单已并入 `skills/requesting-code-review/code-reviewer.md`，成为自包含 Task 分派模板。原分派 `Task (superpowers:code-reviewer)` 者改用带模板的 `Task (general-purpose)`。PR #1299。

- **从技能移除集成章节**——它们是代理原生技能系统出现前的遗留内容，对引导无帮助。

### 工作树技能重写

`using-git-worktrees` 与 `finishing-a-development-branch` 现在检测代理是否已在隔离工作树中，优先运行环境原生工作树控制，再回退到 `git worktree`。行为经 TDD 验证，并在五种运行环境跨平台检查。PRI-974，PR #1121。

- **环境检测**——两技能先检查 `GIT_DIR != GIT_COMMON`；已在链接工作树则完全跳过创建。子模块防护避免误判。

- **创建工作树前征得同意**——`using-git-worktrees` 不再隐式创建，先询问。修复 #991（subagent-driven-development 曾未经同意自动创建）。

- **优先原生工具（步骤 1a）**——运行环境提供自身工作树工具（如 Codex）时优先使用；用户明确偏好时遵守。

- **按来源清理**——`finishing-a-development-branch` 只清理 `.worktrees/` 内、由 superpowers 创建的工作树，外部不动。修复 #940、#999、#238；其中 #238 要求先执行 `cd` 到仓库根目录，再执行 `git worktree remove`。

- **分离 HEAD 处理**——无分支可合并时，收尾菜单缩为两项。

- **硬编码 `/Users/jesse` 路径**替换为通用占位符。#858，PR #1122。

### 面向 AI 代理的贡献者指南

`CLAUDE.md`（符号链接到 `AGENTS.md`）顶部新增两节，直接面向 AI 代理。对最近 100 个关闭 PR 的审计显示 94% 拒绝率，主要因 AI 生成垃圾：未读模板、重复项、捏造问题、把 fork／领域特定变更推到上游。

- **提交前检查清单**——阅读 PR 模板、搜索现有 PR、确认真实问题、确认变更属于核心、提交前向人类展示完整差异。

- **不接受的内容**——第三方依赖、“合规”式技能正文重写、项目特定配置、批量 PR、推测性修复、领域特定技能、fork 特定变更、捏造内容和捆绑无关变更。

- **新运行环境 PR 需会话记录**——过去多数集成只复制技能或用 `npx skills` 包装，而没在会话开始加载 `using-superpowers` 引导。现在要求通过验收（干净会话中“Let's make a react todo list”自动触发 `brainstorming`）并提供完整记录。

### Codex 插件镜像工具

新脚本 `sync-to-codex-plugin` 将 superpowers 镜像到 OpenAI Codex 插件市场 `prime-radiant-inc/openai-codex-plugins`，与路径／用户无关，任何团队成员均可运行。PR #1165。

- 每次将 fork 新建克隆到临时目录，就地生成覆盖层并打开 PR；从脚本位置自动检测上游，并预检 `rsync`/`git`/`gh auth`/`python3`。

- `--bootstrap` 首次设置；`EXCLUDES` 锚定源根；排除 `assets/`。

- 镜像 `CODE_OF_CONDUCT.md`，移除 `agents/openai.yaml` 覆盖层。

- 在镜像 `plugin.json` 填入 `interface.defaultPrompt`。PR #1180，@arittr。

- Codex 插件文件提交到源仓库以使同步使用规范版本，保留 Codex 市场元数据。

### OpenCode 测试文件

- **引导内容在模块级缓存**——`getBootstrapContent()` 曾在每个代理步骤调用 `fs.existsSync`、`fs.readFileSync` 和 frontmatter 正则（`experimental.chat.messages.transform` hook 每步触发）。现在会话生命周期只读一次，缺文件用 null 哨兵；15 项回归测试覆盖缓存、fs 次数、注入保护、缺文件与重置。修复 #1202。

- **集成测试现代化。**

- **README 明确安装注意事项。**

### 代码审查整合

`requesting-code-review` 现在自包含：角色、清单和分派模板位于 `skills/requesting-code-review/code-reviewer.md`，技能直接分派 `Task (general-purpose)`。PR #1299。

- **单一事实来源**——原分散在 `agents/code-reviewer.md` 和技能占位模板并各自漂移的角色／清单现合为一个文件。

- **`subagent-driven-development` 同步调整**——`code-quality-reviewer-prompt.md` 改为分派 `Task (general-purpose)`。

- **新增行为测试**——`tests/claude-code/test-requesting-code-review.sh` 向小项目植入真实缺陷（SQL 注入、明文密码、凭据日志），断言审查者把每项标为 Critical/Important 并拒绝批准。

> 注意：`tests/claude-code/test-requesting-code-review.sh` 与 `tests/claude-code/test-document-review-system.sh` 于 2026-05-06 移入 drill 场景并从 `tests/` 删除。参见 `evals/scenarios/code-review-catches-planted-bugs.yaml` 与 `evals/scenarios/spec-reviewer-catches-planted-flaws.yaml`。文中引用作为带日期的历史记录保留。

- **精简 Codex 与 Copilot 变通文档**——`references/codex-tools.md` 和 `references/copilot-tools.md` 的“Named agent dispatch”章节说明如何把命名代理扁平化为通用分派。现已无命名代理，变通无用，两节删除。

### 子代理驱动开发

- **不再每 3 个任务暂停**——`requesting-code-review` 中“每批（3 任务）后审查”（原用于 `executing-plans`）的节奏曾泄漏到 `subagent-driven-development`。现改为“每项任务或自然检查点”，并加入明确持续执行指令。

- **SDD 集成测试现在会执行其断言**——三个独立缺陷导致测试在打印任何验证结果前静默退出：工作目录路径中有未解析的 `..` 段；`set -euo pipefail` 与 `find | sort | head -1` 相互作用（生产端收到 SIGPIPE，导致脚本终止）；以及 `claude -p` 调用缺少 `--plugin-dir`，使测试加载已安装插件而非工作树。三项均已修复；六项验证测试现在会针对真实端到端的 SDD 运行实际执行。

### Cursor 平台

- **Windows SessionStart 钩子**改为通过 `run-hook.cmd` 路由，而非直接调用无扩展名的 `session-start` 脚本。这修复了 Windows 在编辑器中打开文件而不执行的问题。另删除了 `hooks-cursor.json` 中误加的 UTF-8 BOM。

### Gemini CLI 平台

- **子代理派发映射**——Gemini 的 `Task` 派发现在映射到 `@agent-name` / `@generalist`，并记录了对独立任务并行派发子代理的方式。

### 技能

- **术语清理**，涉及技能内容。

### 文档与安装

- 在 README 中添加 **Factory Droid 安装说明**。

- README 中添加 **快速开始安装链接**。（@arittr 的 PR #1293）

- 更新 **Codex 插件安装指南**。（@arittr 的 PR #1288）

- 在工具参考中将 **Codex 的 `wait` 映射修正**为 `wait_agent`。

- **重新整理安装顺序**；清理 Codex 安装说明。

- **删除遗留的 `CHANGELOG.md`**，以 `RELEASE-NOTES.md` 作为唯一来源。（@shaanmajid 的 PR #1163）

- 修复 **Discord 邀请链接**；在社区部分添加发布公告链接及详细 Discord 说明。

### 社区

- @shaanmajid——删除遗留的 `CHANGELOG.md`（PR #1163）

- @arittr——README 快速开始安装链接（#1293）、Codex 插件安装指南（#1288）、`sync-to-codex-plugin` 的 `interface.defaultPrompt` 种子内容（#1180）

### GitHub Copilot CLI 支持

- **SessionStart 上下文注入**——Copilot CLI v1.0.11 添加了对 sessionStart 钩子输出中 `additionalContext` 的支持。会话启动钩子现在检测 `COPILOT_CLI` 环境变量，并输出 SDK 标准格式 `{ "additionalContext": "..." }`，使 Copilot CLI 用户能在会话开始时获得完整的 superpowers 引导。（@culinablaz 在 PR #910 中的原始修复）

- **工具映射**——添加 `references/copilot-tools.md`，包含完整的 Claude Code 到 Copilot CLI 工具对应表

- **技能与 README 更新**——将 Copilot CLI 添加到 `using-superpowers` 技能的平台说明及 README 安装部分

### OpenCode 修复

- **技能路径一致性**——引导文本不再宣传与实际运行时路径不符、容易误导的 `configDir/skills/superpowers/` 路径。代理应使用原生 `skill` 工具，不按路径导航文件。测试现在使用来自单一事实来源的一致路径。（#847、#916）

- **将引导作为用户消息**——将引导注入从 `experimental.chat.system.transform` 移到 `experimental.chat.messages.transform`，前置到首条用户消息，而非添加系统消息。这避免了系统消息每轮重复造成的 token 膨胀（#750），并修复了与 Qwen 及其他因多个系统消息而出错的模型的兼容性（#894）。

### 内联自审取代子代理审查循环

子代理审查循环（派发全新代理审查计划/规范）使执行时间翻倍（约 25 分钟开销），却未带来可测量的计划质量提升。跨 5 个版本、每个 5 次试验的回归测试显示，无论是否运行审查循环，质量得分都相同。

- **brainstorming**——以内联规范自审清单取代规范审查循环（派发子代理 + 最多 3 次迭代）：扫描占位符、内部一致性、范围检查、歧义检查

- **writing-plans**——以内联自审清单取代计划审查循环（派发子代理 + 最多 3 次迭代）：规范覆盖、占位符扫描、类型一致性

- **writing-plans**——添加明确的“无占位符”部分，定义计划失败情形（TBD、含糊描述、未定义引用、“类似于任务 N”）

- 自审每次约 30 秒可发现 3-5 个真实缺陷，而非约 25 分钟，缺陷率与子代理方式相当

### 头脑风暴服务器

- **重组会话目录**——头脑风暴服务器会话目录现在包含两个同级子目录：`content/`（提供给浏览器的 HTML 文件）和 `state/`（事件、服务器信息、pid、日志）。此前服务器状态和用户交互数据与提供的内容一同存储，使其可通过 HTTP 访问。服务器启动 JSON 现同时包含 `screen_dir` 与 `state_dir` 路径。（吉田仁报告）

### 缺陷修复

- **所有者 PID 生命周期修复**——头脑风暴服务器的所有者 PID 监控有两个缺陷，会导致 60 秒内误关闭：(1) 将跨用户 PID（Tailscale SSH 等）的 EPERM 视为“进程已死”；(2) 在 WSL 上，祖父 PID 解析为短暂子进程，在首次生命周期检查前已退出。修复方式是将 EPERM 视为“存活”，并在启动时验证所有者 PID——如果它已经死亡，就禁用监控，服务器依赖 30 分钟空闲超时。由于服务器现在通用处理此问题，也从 `start-server.sh` 移除了 Windows/MSYS2 专用特例。（#879）

- **writing-skills**——纠正“SKILL.md frontmatter 仅支持两个字段”的错误说法；现在表述为“两个必需字段”，并链接到 agentskills.io 规范以查看所有支持字段（@arittr 的 PR #882）

### Codex 应用兼容性

- **codex-tools**——添加具名代理派发映射，说明如何将 Claude Code 的具名代理类型转换为 Codex 的 `spawn_agent` 与工作者角色（@arittr 的 PR #647）

- **codex-tools**——为感知工作树的技能添加环境检测和 Codex 应用收尾部分（由 @arittr 提供）

- **设计规范**——添加 Codex 应用兼容性设计规范（PRI-823），涵盖只读环境检测、工作树安全技能行为及沙箱回退模式（由 @arittr 提供）

### 缺陷修复

- **头脑风暴服务器 ESM 修复**——将 `server.js` 重命名为 `server.cjs`，使头脑风暴服务器能在 Node.js 22+ 上正常启动；该环境中根目录 `package.json` 的 `"type": "module"` 会导致 `require()` 失败。（@sarbojitrana 的 PR #784，修复 #774、#780、#783）

- **Windows 上的头脑风暴服务器所有者 PID**——在 Windows/MSYS2 上跳过 PID 生命周期监控，因为 Node.js 看不到其 PID 命名空间，从而防止服务器在 60 秒后自行终止。（#770，@lucasyhzlu-debug 的 PR #768 中文档）

- **stop-server.sh 可靠性**——报告成功前验证服务器进程确实已终止。SIGTERM + 等待 2 秒 + 回退 SIGKILL。（#723）

### 变更

- **执行交接**——恢复用户写完计划后在子代理驱动与内联执行之间的选择。推荐子代理驱动，但不再强制。

### 审查循环改进

通过去除不必要的审查轮次并收紧审查者关注点，大幅减少 token 使用并加快规范与计划审查。

- **一次性审查完整计划**——计划审查者现在一次审查完整计划，而非逐块审查。删除全部与块有关的概念（`## Chunk N:` 标题、1000 行分块限制、逐块派发）。

- **提高阻塞问题门槛**——规范和计划审查者提示词现在均包含“校准”部分：仅标记会在实施期间造成真实问题的事项。细枝末节的措辞、风格偏好和格式争议不应阻塞批准。

- **减少最大审查迭代次数**——规范与计划审查循环均从 5 次减至 3 次。若审查者校准正确，3 轮已足够。

- **精简审查者清单**——规范审查者从 7 类减至 5 类；计划审查者从 7 类减至 4 类。移除聚焦格式的检查（任务语法、分块大小），转而关注实质（可构建性、与规范一致性）。

### OpenCode 平台

- **单行插件安装**——OpenCode 插件现在通过 `config` 钩子自动注册技能目录。无需符号链接或 `skills.paths` 配置。安装只需在 `opencode.json` 添加一行。（PR #753）

- **添加 `package.json`**，使 OpenCode 能从 git 安装 superpowers 为 npm 包。

### 缺陷修复

- **验证服务器确实已停止**——`stop-server.sh` 现在报告成功前确认进程已死亡。SIGTERM + 等待 2 秒 + 回退 SIGKILL。进程仍存活时报告失败。（PR #751）

- **通用代理用语**——头脑风暴伴侣等待页现在说“the agent”（代理），不再说“Claude”。

### Cursor 支持

- **Cursor 钩子**——添加 `hooks/hooks-cursor.json`，采用 Cursor 的驼峰格式（`sessionStart`、`version: 1`），并更新 `.cursor-plugin/plugin.json` 引用它。修复 `session-start` 中的平台检测，优先检查 `CURSOR_PLUGIN_ROOT`（Cursor 也可能设置 `CLAUDE_PLUGIN_ROOT`）。（基于 PR #709）

### 缺陷修复

- **在 `--resume` 时停止触发 SessionStart 钩子**——启动钩子此前在恢复会话时重新注入上下文，而恢复会话的历史记录中已有上下文。钩子现在仅在 `startup`、`clear` 和 `compact` 时触发。

- **Bash 5.3+ 钩子挂起**——在 `hooks/session-start` 中以 `printf` 替换 heredoc（`cat <<EOF`）。修复 macOS 上 Homebrew bash 5.3+ 因 heredoc 中大型变量展开的 bash 回归导致的无限挂起。（#572、#571）

- **POSIX 安全钩子脚本**——在 `hooks/session-start` 中将 `${BASH_SOURCE[0]:-$0}` 替换为 `$0`。修复 Ubuntu/Debian 上 `/bin/sh` 为 dash 时的“Bad substitution”（错误替换）错误。（#553）

- **可移植 shebang**——将所有 shell 脚本中的 `#!/bin/bash` 替换为 `#!/usr/bin/env bash`。修复 NixOS、FreeBSD 及使用过时或缺少 `/bin/bash` 的 Homebrew bash 的 macOS 上的执行问题。（#700）

- **Windows 上的头脑风暴服务器**——自动检测 Windows/Git Bash（`OSTYPE=msys*`、`MSYSTEM`）并切换为前台模式，修复 `nohup`/`disown` 进程回收导致的服务器静默失败。（#737）

- **Codex 文档修复**——在 Codex 文档中将弃用的 `collab` 标志替换为 `multi_agent`。（PR #749）

### 零依赖头脑风暴服务器

**删除所有随附 node_modules——server.js 现在完全自包含**

- 用基于内置 `http`、`fs` 和 `crypto` 模块的零依赖 Node.js 服务器，替换 Express/Chokidar/WebSocket 依赖

- 删除约 1,200 行随附的 `node_modules/`、`package.json` 和 `package-lock.json`

- 自定义 WebSocket 协议实现（RFC 6455 帧格式、ping/pong、正确的关闭握手）

- 用原生 `fs.watch()` 文件监控替代 Chokidar

- 完整测试套件：HTTP 服务、WebSocket 协议、文件监控及集成测试

### 头脑风暴服务器可靠性

- **空闲 30 分钟后自动退出**——无客户端连接时服务器关闭，防止产生孤立进程

- **所有者进程跟踪**——服务器监控父宿主 PID，并在所属会话终止时退出

- **存活检查**——技能在复用现有实例前验证服务器是否响应

- **编码修复**——提供的 HTML 页面使用正确的 `<meta charset="utf-8">`

### 子代理上下文隔离

- 所有委派技能（brainstorming、dispatching-parallel-agents、requesting-code-review、subagent-driven-development、writing-plans）现在都包含上下文隔离原则

- 子代理只接收所需上下文，防止上下文窗口污染

### Agentskills 符合性

**头脑风暴服务器移入技能目录**

- 按照 [agentskills.io](https://agentskills.io) 规范，将 `lib/brainstorm-server/` → `skills/brainstorming/scripts/`

- 将所有 `${CLAUDE_PLUGIN_ROOT}/lib/brainstorm-server/` 引用替换为相对 `scripts/` 路径

- 技能现在完全可跨平台移植——定位脚本无需平台专用环境变量

- 删除 `lib/` 目录（其中曾是最后剩余的内容）

### 新功能

**Gemini CLI 扩展**

- 通过仓库根目录的 `gemini-extension.json` 和 `GEMINI.md` 提供原生 Gemini CLI 扩展支持

- `GEMINI.md` 在会话开始时通过 @ 引入 `using-superpowers` 技能和工具映射表

- Gemini CLI 工具映射参考（`skills/using-superpowers/references/gemini-tools.md`）——将 Claude Code 工具名称（Read、Write、Edit、Bash 等）转换为 Gemini CLI 对应项（read_file、write_file、replace 等）

- 记录 Gemini CLI 限制：不支持子代理，技能回退到 `executing-plans`

- 扩展根目录位于仓库根目录，以实现跨平台兼容（避免 Windows 符号链接问题）

- 在 README 中添加安装说明

### 改进

**多平台头脑风暴服务器启动**

- visual-companion.md 中的逐平台启动说明：Claude Code（默认模式）、Codex（通过 `CODEX_CI` 自动前台）、Gemini CLI（结合 `is_background` 使用 `--foreground`），及其他环境的回退方案

- 服务器现在将启动 JSON 写入 `$SCREEN_DIR/.server-info`，因此即使后台执行隐藏 stdout，代理也能找到 URL 和端口

**随附头脑风暴服务器依赖**

- 将 `node_modules` 纳入仓库，因此全新安装插件后头脑风暴服务器即可运行，无需在运行时使用 `npm`

- 从随附依赖中移除 `fsevents`（仅适用于 macOS 的原生二进制文件；没有它时 chokidar 能平稳回退）

- 如果缺少 `node_modules`，回退为通过 `npm install` 自动安装

**OpenCode 工具映射修复**

- `TodoWrite` → `todowrite`（此前错误映射为 `update_plan`）；已对照 OpenCode 源码验证

### 缺陷修复

**Windows/Linux：单引号破坏 SessionStart 钩子**（#577、#529、#644、PR #585）

- hooks.json 中 `${CLAUDE_PLUGIN_ROOT}` 周围的单引号在 Windows 上失败（cmd.exe 不将单引号识别为路径定界符），在 Linux 上也失败（单引号阻止变量展开）

- 修复：用转义双引号替换单引号——适用于 macOS bash、Windows cmd.exe、Windows Git Bash 和 Linux，无论路径是否含空格

- 已在 Windows 11（NT 10.0.26200.0）、Claude Code 2.1.72 和 Git for Windows 上验证

**头脑风暴跳过规范审查循环**（#677）

- 规范审查循环（派发 spec-document-reviewer 子代理，迭代直到批准）存在于“设计之后”正文部分，却未出现在检查清单与流程图中

- 代理比起正文更可靠地遵循图表和清单，因此规范审查步骤被完全跳过

- 向检查清单添加步骤 7（规范审查循环），并向 dot 图添加相应节点

- 使用 `claude --plugin-dir` 和 `claude-session-driver` 测试：工作者现在会正确派发审查者

**Cursor 安装命令**（PR #676）

- 修正 README 中 Cursor 安装命令：`/plugin-add` → `/add-plugin`（通过 Cursor 2.5 发布公告确认）

**头脑风暴中的用户审查门槛**（#565）

- 在规范完成与交接给 writing-plans 之间添加明确的用户审查步骤

- 实现规划开始前，用户必须批准规范

- 检查清单、流程图和正文均更新为包含新门槛

**会话启动钩子在每个平台仅输出一次上下文**

- 钩子现在检测自己是在 Claude Code 还是其他平台中运行

- 对 Claude Code 输出 `hookSpecificOutput`，其他平台输出 `additional_context`——避免重复注入上下文

**token 分析脚本的 lint 修复**

- 在 `tests/claude-code/analyze-token-usage.py` 中将 `except:` → `except Exception:`

### 维护

**删除无用代码**

- 删除 `lib/skills-core.js` 及其测试（`tests/opencode/test-skills-core.js`）——自 2026 年 2 月起已不再使用

- 从 `tests/opencode/test-plugin-loading.sh` 删除 skills-core 存在性检查

### 社区

- @karuturi——Claude Code 官方市场安装说明（PR #610）

- @mvanhorn——会话启动钩子双输出修复、OpenCode 工具映射修复

- @daniel-graham——裸 except 的 lint 修复

- PR #585 作者——Windows/Linux 钩子引号修复

### 破坏性变更

**重组规范和计划目录**

- 规范（brainstorming 输出）现在保存至 `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`

- 计划（writing-plans 输出）现在保存至 `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

- 用户对规范/计划位置的偏好覆盖这些默认值

- 更新所有技能内部引用、测试文件和示例路径以保持一致

- 迁移：如有需要，将现有文件从 `docs/plans/` 移到新位置

**在具备相应能力的宿主上强制使用子代理驱动开发**

Writing-plans 不再提供 subagent-driven 与 executing-plans 之间的选择。在支持子代理的宿主（Claude Code、Codex）上，必须使用 subagent-driven-development。Executing-plans 保留给没有子代理能力的宿主，并会告知用户 Superpowers 在支持子代理的平台上效果更好。

**Executing-plans 不再分批执行**

删除“执行 3 个任务后停止供审查”的模式。计划现在连续执行，仅遇到阻塞时停止。

**弃用斜杠命令**

`/brainstorm`、`/write-plan` 和 `/execute-plan` 现在显示弃用通知，引导用户使用对应技能。命令将在下一个大版本移除。

### 新功能

**可视化头脑风暴伴侣**

用于头脑风暴会话的可选浏览器伴侣。当主题适合可视化时，头脑风暴技能会提议在终端对话旁的浏览器窗口展示模型图、图表、比较和其他内容。

- `lib/brainstorm-server/`——WebSocket 服务器，附浏览器辅助库、会话管理脚本及深色/浅色主题框架模板（“Superpowers 头脑风暴”，带 GitHub 链接）

- `skills/brainstorming/visual-companion.md`——关于服务器工作流、屏幕编写与反馈收集的渐进披露指南

- 头脑风暴技能在流程中添加可视化伴侣决策点：探索项目上下文后，评估后续问题是否涉及视觉内容，并用单独消息提供伴侣选项

- 逐问题决策：即使用户接受，每个问题仍分别评估更适合浏览器还是终端

- 集成测试位于 `tests/brainstorm-server/`

**文档审查系统**

通过派发子代理，为规范和计划文档提供自动审查循环：

- `skills/brainstorming/spec-document-reviewer-prompt.md`——审查者检查完整性、一致性、架构及 YAGNI

- `skills/writing-plans/plan-document-reviewer-prompt.md`——审查者检查与规范一致性、任务分解、文件结构及文件大小

- Brainstorming 撰写设计文档后派发规范审查者

- Writing-plans 在每部分之后按块进行计划审查循环

- 审查循环重复至获准，或迭代 5 次后上报

- 端到端测试位于 `tests/claude-code/test-document-review-system.sh`

- 设计规范和实现计划位于 `docs/superpowers/`

**贯穿技能流水线的架构指导**

为 brainstorming、writing-plans 和 subagent-driven-development 添加面向隔离的设计与文件大小意识指导：

- **Brainstorming**——新增“为隔离与清晰度而设计”（清晰边界、定义良好的接口、可独立测试的单元）及“在现有代码库中工作”（遵循现有模式，仅做针对性改进）部分

- **Writing-plans**——新增“文件结构”部分：定义任务前梳理文件及职责。新增“范围检查”兜底：捕获本应在头脑风暴阶段分解的多子系统规范

- **SDD 实现者**——新增“代码组织”部分（遵循计划文件结构，报告文件膨胀顾虑）及“力不从心时”的上报指导

- **SDD 代码质量审查者**——现在检查架构、单元分解、计划符合性及文件增长

- **规范/计划审查者**——审查标准新增架构及文件大小

- **范围评估**——Brainstorming 现在评估项目是否过大、无法由单份规范覆盖。多子系统请求会尽早标记并分成子项目，每个子项目各有规范 → 计划 → 实现周期

**子代理驱动开发改进**

- **模型选择**——根据任务类型选择模型能力的指导：机械实现用廉价模型，集成用标准模型，架构与审查用强能力模型

- **实现者状态协议**——子代理现在报告 DONE、DONE_WITH_CONCERNS、BLOCKED 或 NEEDS_CONTEXT。控制器对各状态作适当处理：补充上下文重新派发、提升模型能力、拆分任务或向人类上报

### 改进

**指令优先级层次**

为 using-superpowers 添加明确优先顺序：

1. 用户明确指令（CLAUDE.md、AGENTS.md、直接请求）——最高优先级

2. Superpowers 技能——覆盖默认系统行为

3. 默认系统提示词——最低优先级

若 CLAUDE.md 或 AGENTS.md 说“不要使用 TDD”，而技能说“始终使用 TDD”，以用户指令为准。

**SUBAGENT-STOP 门槛**

为 using-superpowers 添加 `<SUBAGENT-STOP>` 块。为特定任务派发的子代理现在跳过该技能，而不是激活 1% 规则并调用完整技能工作流。

**多平台改进**

- Codex 工具映射移至渐进披露参考文件（`references/codex-tools.md`）

- 添加平台适配指针，使非 Claude Code 平台能找到对应工具

- 计划头部现在面向“代理工作者”，而非特指“Claude”

- 在 `docs/README.codex.md` 中记录 Collab 功能要求

**Writing-plans 模板更新**

- 计划步骤现在采用复选框语法（`- [ ] **Step N:**`）以跟踪进度

- 计划头部同时引用 subagent-driven-development 与 executing-plans，并按平台路由

### 新增

**Cursor 支持**

Superpowers 现在支持 Cursor 插件系统。包含 `.cursor-plugin/plugin.json` 清单及 README 中 Cursor 专用安装说明。SessionStart 钩子输出现在除现有 `hookSpecificOutput.additionalContext` 外，还包含 `additional_context` 字段，以兼容 Cursor 钩子。

### 修复

**Windows：恢复多语言包装器以可靠执行钩子（#518、#504、#491、#487、#466、#440）**

Windows 上 Claude Code 的 `.sh` 自动检测会给钩子命令前加 `bash`，导致执行失败。修复如下：

- 将 `session-start.sh` 重命名为无扩展名的 `session-start`，避免自动检测干扰

- 恢复 `run-hook.cmd` 多语言包装器，支持多位置 bash 发现（先搜索标准 Git for Windows 路径，再回退至 PATH）

- 找不到 bash 时静默退出，不报错

- 在 Unix 上，包装器通过 `exec bash` 直接运行脚本

- 使用 POSIX 安全的 `dirname "$0"` 路径解析（适用于 dash/sh，不仅是 bash）

这修复了 Windows 上因路径含空格、缺少 WSL、MSYS 上 `set -euo pipefail` 脆弱性及反斜杠破坏而导致的 SessionStart 失败。

此修复应能大幅改善 superpowers 技能遵循情况，并降低 Claude 意外进入原生计划模式的概率。

### 变更

**头脑风暴技能现在强制执行其工作流，而非仅描述**

模型此前会跳过设计阶段，直接进入 frontend-design 等实现技能，或将整个头脑风暴过程压缩为单个文本块。技能现在使用硬门槛、必需清单及 graphviz 流程图强制遵循：

- `<HARD-GATE>`：设计展示且用户批准前，不使用实现技能、不写代码、不搭建脚手架

- 明确的检查清单（6 项），必须创建为任务并按顺序完成

- Graphviz 流程图，`writing-plans` 为唯一有效终止状态

- 明确指出“这太简单，不需要设计”这一反模式——这正是模型用于跳过流程的合理化理由

- 设计部分的篇幅按该部分复杂度决定，而非项目复杂度

**Using-superpowers 工作流图拦截 EnterPlanMode**

为技能流程图添加 `EnterPlanMode` 拦截。模型即将进入 Claude 原生计划模式时，会检查是否已进行头脑风暴，并改为通过头脑风暴技能路由。始终不进入计划模式。

### 修复

**SessionStart 钩子现在同步运行**

将 hooks.json 中 `async: true` 改为 `async: false`。异步时钩子可能未能在模型首轮前完成，导致首条消息的上下文中没有 using-superpowers 指令。

### 破坏性变更

**Codex：以原生技能发现替代引导 CLI**

删除 `superpowers-codex` 引导 CLI、Windows `.cmd` 包装器及相关引导内容文件。Codex 现在通过 `~/.agents/skills/superpowers/` 符号链接使用原生技能发现，因此不再需要旧的 `use_skill`/`find_skills` CLI 工具。

安装现在只需克隆 + 符号链接（见 INSTALL.md）。无需 Node.js 依赖。旧的 `~/.codex/skills/` 路径已弃用。

### 修复

**Windows：修复 Claude Code 2.1.x 钩子执行（#331）**

Claude Code 2.1.x 改变了 Windows 上的钩子执行方式：现在自动检测命令中的 `.sh` 文件并前加 `bash`。这破坏了多语言包装器模式，因为 `bash "run-hook.cmd" session-start.sh` 试图将 `.cmd` 文件当作 bash 脚本执行。

修复：hooks.json 现在直接调用 session-start.sh。Claude Code 2.1.x 自动处理 bash 调用。另添加 .gitattributes，强制 shell 脚本使用 LF 换行（修复 Windows 检出时的 CRLF 问题）。

**Windows：SessionStart 钩子异步运行以防终端冻结（#404、#413、#414、#419）**

同步 SessionStart 钩子阻止 Windows 上 TUI 进入原始模式，使全部键盘输入冻结。异步运行钩子既可避免冻结，又仍能注入 superpowers 上下文。

**Windows：修复 `escape_for_json` 的 O(n²) 性能问题**

逐字符循环 `${input:$i:1}` 因 bash 子串复制开销呈 O(n²)。Windows Git Bash 上耗时超过 60 秒。现改用 bash 参数替换 `${s//old/new}`，每种模式一次 C 级遍历；macOS 快 7 倍，Windows 显著更快。

**Codex：修复 Windows/PowerShell 调用（#285、#243）**

- Windows 不遵循 shebang，直接调用无扩展名的 `superpowers-codex` 会弹出“打开方式”。所有调用现在加 `node` 前缀。

- 修复 Windows 的 `~/` 路径展开——PowerShell 传给 `node` 时不会展开 `~`。改用 `$HOME`，它在 bash 与 PowerShell 中都能正确展开。

**Codex：修复安装器路径解析**

使用 `fileURLToPath()` 而非手工解析 URL 路径，以在所有平台正确处理空格和特殊字符。

**Codex：修复 writing-skills 中陈旧技能路径**

将弃用的 `~/.codex/skills/` 引用更新为原生发现使用的 `~/.agents/skills/`。

### 改进

**实施前现在必须隔离工作树**

将 `using-git-worktrees` 加入 `subagent-driven-development` 与 `executing-plans` 的必需技能。实施流程现在明确要求先创建隔离工作树，防止意外直接改动 main。

**main 分支保护放宽为需明确同意**

不再完全禁止 main 分支工作，而是允许用户明确同意后执行。更灵活，同时让用户知道影响。

**简化安装验证**

从验证步骤移除 `/help` 检查和特定斜杠命令列表。技能主要通过描述目标来调用，不依赖运行特定命令。

**Codex：明确引导中的子代理工具映射**

改进 Codex 工具与 Claude Code 对子代理工作流等价映射的文档。

### 测试

- 为 subagent-driven-development 增加工作树要求测试

- 增加 main 分支红旗警告测试

- 修复技能识别测试断言中的大小写敏感性

### 修复

**OpenCode：按官方文档统一为 `plugins/` 目录（#343）**

OpenCode 官方文档使用 `~/.config/opencode/plugins/`（复数）。我们的文档曾用单数 `plugin/`。OpenCode 接受两者，但现统一官方约定避免混淆。

变更：

- 仓库结构中 `.opencode/plugin/` 更名 `.opencode/plugins/`

- 更新所有平台安装文档（INSTALL.md、README.opencode.md）

- 更新测试脚本以匹配

**OpenCode：修复符号链接说明（#339、#342）**

- 在 `ln -s` 前显式 `rm`，修复重装时“文件已存在”

- 补上 INSTALL.md 缺少的技能符号链接步骤

- 从弃用 `use_skill`/`find_skills` 更新为原生 `skill` 工具引用

### 破坏性变更

**OpenCode：切换到原生技能系统**

Superpowers for OpenCode 现在使用原生 `skill` 工具，不再使用自定义 `use_skill`/`find_skills`，与 OpenCode 内置发现更干净地集成。

**需要迁移：**技能必须符号链接到 `~/.config/opencode/skills/superpowers/`（见更新安装文档）。

### 修复

**OpenCode：修复会话开始时代理重置（#226）**

旧引导注入用 `session.prompt({ noReply: true })`，导致 OpenCode 在首条消息时把所选代理重置为“build”。现在用 `experimental.chat.system.transform` hook 直接修改系统提示词，无副作用。

**OpenCode：修复 Windows 安装（#232）**

- 移除 `skills-core.js` 依赖，避免文件复制而非链接时相对导入损坏

- 增加 cmd.exe、PowerShell、Git Bash 的完整 Windows 安装文档

- 记录各平台符号链接与 junction 的正确用法

**Claude Code：修复 2.1.x 的 Windows hook 执行**

Claude Code 2.1.x 改变 Windows hook 执行方式：自动检测命令中的 `.sh` 并前置 `bash `。这破坏多语言包装模式，因为 `bash "run-hook.cmd" session-start.sh` 会把 .cmd 当 bash 脚本。

修复：hooks.json 直接调用 session-start.sh，由 2.1.x 自动处理 bash。另加 .gitattributes 强制 shell 脚本 LF，修复 Windows 检出的 CRLF 问题。

### 改进

**强化 using-superpowers 对明确技能请求的处理**

修复一种失败：用户点名请求技能（如“subagent-driven-development, please”）时 Claude 仍跳过调用，认为“我知道它是什么意思”而直接工作。

变更：

- “The Rule”从“检查技能”改为“调用相关或被请求的技能”，强调主动调用

- 增加“在任何回复或行动之前”——旧措辞只说回复，Claude 有时先行动

- 说明调用错误技能可以接受，减少犹豫

- 新增红旗：“我知道它是什么意思” → 理解概念不等于使用技能

**增加明确技能请求测试**

`tests/explicit-skill-requests/` 新测试套件验证用户点名请求时 Claude 正确调用技能，含单轮与多轮场景。

### 修复

**斜杠命令现在仅限用户**

三个斜杠命令（`/brainstorm`、`/execute-plan`、`/write-plan`）都加 `disable-model-invocation: true`，Claude 不能再通过 Skill 工具调用，只能由用户手动执行。

底层技能（`superpowers:brainstorming`、`superpowers:executing-plans`、`superpowers:writing-plans`）仍可被 Claude 自主调用，避免调用一个最终只重定向的冗余命令。

### 修复

**明确 Claude Code 中技能的访问方式**

修复 Claude 用 Skill 工具调用后还另行读取技能文件的混淆。`using-superpowers` 现在明确 Skill 工具直接加载内容，无需读文件。

- `using-superpowers` 新增“How to Access Skills”章节

- 指令中的“读取技能”改为“调用技能”

- 斜杠命令使用完整技能名（如 `superpowers:brainstorming`）

**为 receiving-code-review 增加 GitHub 线程回复指导**（感谢 @ralphbean）

增加说明：在原线程回复行内审查评论，不发顶层 PR 评论。

**为 writing-skills 增加自动化优先于文档的指导**（感谢 @EthanJStark）

增加说明：机械约束应自动化，不写成文档；技能用于需要判断的事项。

### 新功能

**subagent-driven-development 两阶段代码审查**

子代理工作流现在每项任务后采用两个独立审查阶段：

1. **规格符合性审查**——怀疑型审查者验证实现完全符合规格，捕获遗漏需求与过度构建，不信任报告而读取实际代码。

2. **代码质量审查**——仅在规格审查通过后运行，检查清晰代码、测试覆盖、可维护性。

这能捕获代码写得好但不符合要求的常见失败。审查是循环而非一次：发现问题后实现者修复，审查者再检查。

其他子代理工作流改进：

- 控制器向工作者提供完整任务文本，而非文件引用

- 工作者可在开始前和工作中提出澄清问题

- 报告完成前运行自审清单

- 开始时读一次计划并提取到 TodoWrite

`skills/subagent-driven-development/` 新提示模板：

- `implementer-prompt.md`——含自审清单并鼓励提问

- `spec-reviewer-prompt.md`——对照需求进行怀疑式验证

- `code-quality-reviewer-prompt.md`——标准代码审查

**调试技术与工具合并**

`systematic-debugging` 现在随附支持技术与工具：

- `root-cause-tracing.md`——沿调用栈向后追踪缺陷

- `defense-in-depth.md`——多层添加验证

- `condition-based-waiting.md`——以条件轮询替代任意超时

- `find-polluter.sh`——二分查找污染测试的脚本

- `condition-based-waiting-example.ts`——真实调试会话的完整实现

**测试反模式参考**

`test-driven-development` 现在含 `testing-anti-patterns.md`，覆盖：

- 测试 mock 行为而非真实行为

- 向生产类添加仅测试方法

- 不理解依赖就 mock

- 隐藏结构性假设的不完整 mock

**技能测试基础设施**

三个验证技能行为的新框架：

`tests/skill-triggering/`——验证技能能从无明确命名的朴素提示触发，测试 6 个技能，确认描述本身足够。

`tests/claude-code/`——用 `claude -p` 的无头集成测试，通过会话记录（JSONL）验证技能使用；含 `analyze-token-usage.py` 跟踪成本。

`tests/subagent-driven-dev/`——两个完整测试项目的端到端验证：

- `go-fractals/`——含 Sierpinski/Mandelbrot 的 CLI（10 任务）

- `svelte-todo/`——使用 localStorage 与 Playwright 的 CRUD 应用（12 任务）

### 重大变更

**DOT 流程图作为可执行规格**

使用 DOT/GraphViz 流程图重写关键技能，将其作为权威流程定义，正文为支持内容。

**描述陷阱**（记录于 `writing-skills`）：发现描述含工作流摘要时，Claude 会遵循短描述而不读详细流程图。修复：描述只写触发条件（“Use when X”），不写过程细节。

**using-superpowers 中的技能优先级**

多个技能适用时，流程技能（头脑风暴、调试）明确先于实施技能。“构建 X”先触发头脑风暴，再触发领域技能。

**强化头脑风暴触发**

描述改为祈使句：“你必须在任何创造性工作前使用——创建功能、构建组件、增加功能或修改行为。”

### 破坏性变更

**技能合并**——六个独立技能被合并：

- `root-cause-tracing`、`defense-in-depth`、`condition-based-waiting` → 并入 `systematic-debugging/`

- `testing-skills-with-subagents` → 并入 `writing-skills/`

- `testing-anti-patterns` → 并入 `test-driven-development/`

- 删除过时 `sharing-skills`

### 其他改进

- **render-graphs.js**——从技能提取 DOT 图并渲染 SVG 的工具

- using-superpowers 中的**合理化表**——可扫描格式，新增“我需要更多上下文”“先让我探索”“这感觉有产出”等条目

- **docs/testing.md**——用 Claude Code 集成测试验证技能的指南

### 已修复

- **Linux 兼容性**：修复多语言 hook 包装器（`run-hook.cmd`）以使用 POSIX 兼容语法

- 第 16 行将 bash 专用 `${BASH_SOURCE[0]:-$0}` 改为标准 `$0`

- 解决 `/bin/sh` 为 dash 的 Ubuntu/Debian“Bad substitution”

- 修复 #141

### 变更

- **OpenCode 引导重构**：引导注入从 `chat.message` hook 改为 `session.created` 事件

- 会话创建时通过带 `noReply: true` 的 `session.prompt()` 注入

- 明确告知模型 using-superpowers 已加载，避免重复加载

- 引导内容生成合并到共享 `getBootstrapContent()`

- 清理为单一实现（移除回退模式）

### 新增

- **OpenCode 支持**：OpenCode.ai 原生 JavaScript 插件

- 自定义工具：`use_skill` 和 `find_skills`

- 消息插入模式让技能跨上下文压缩保留

- 通过 chat.message hook 自动注入上下文

- 会话压缩时自动重注入

- 三层技能优先级：项目 > 个人 > superpowers

- 支持项目本地技能（`.opencode/skills/`）

- 与 Codex 复用共享核心模块（`lib/skills-core.js`）

- 带正确隔离的自动测试套件（`tests/opencode/`）

- 平台专用文档（`docs/README.opencode.md`、`docs/README.codex.md`）

### 变更

- **重构 Codex 实现**：现使用共享 `lib/skills-core.js` ES 模块

- 消除 Codex 与 OpenCode 之间的代码重复

- 技能发现与解析使用唯一来源

- Codex 通过 Node.js 互操作成功加载 ES 模块

- **改进文档**：重写 README，清楚说明问题与方案

- 删除重复和冲突内容

- 增加完整工作流描述（头脑风暴 → 计划 → 执行 → 收尾）

- 简化平台安装说明

- 强调技能检查协议而非自动激活承诺

### 改进

- 优化 superpowers bootstrap，消除重复执行技能。`using-superpowers` 内容直接在会话上下文提供，并说明只有其他技能才用 Skill 工具；避免代理明明已有内容却手动的循环；其中相关的字段或标识包括 `using-superpowers`。

### 改进

- 简化 `brainstorming`，回归对话愿景：移除六阶段重流程和正式清单，改为自然对话，一次一问，再以 200—300 词分节展示设计并确认；保留文档与实施交接。

### 改进

- 更新 `brainstorming`：提问前自主侦察，鼓励建议驱动决定，防止把优先级推回人类。

- 按 Strunk《The Elements of Style》提升 `brainstorming` 清晰度：删除冗词、否定改正叙述、改善并列结构。

### 缺陷修复

- 明确 `writing-skills` 指向正确代理个人技能目录（Claude Code 为 `~/.claude/skills`，Codex 为 `~/.codex/skills`）。

### 新功能

**实验性 Codex 支持**

- 新增统一 `superpowers-codex` 脚本，含 bootstrap/use-skill/find-skills 命令

- 跨平台 Node.js 实现（Windows、macOS、Linux）

- 命名空间：superpowers 技能为 `superpowers:skill-name`，个人技能为 `skill-name`

- 同名时个人技能覆盖 superpowers 技能

- 干净显示名称/描述，不展示原始前置元数据

- 显示每个技能支持文件目录

- Codex 工具映射：TodoWrite→update_plan，子代理→手动回退等

- bootstrap 与最小 AGENTS.md 集成，自动启动

- Codex 专属完整安装和 bootstrap 说明

**与 Claude Code 集成的关键差异：**

- 单一统一脚本而非独立工具

- Codex 工具替代系统

- 简化子代理为手动工作

- 术语由“核心技能”改为“Superpowers 技能”

### 新增文件

- `.codex/INSTALL.md`：Codex 安装指南

- `.codex/superpowers-bootstrap.md`：Codex 适配 bootstrap

- `.codex/superpowers-codex`：统一 Node.js 可执行文件

**注意：** Codex 支持为实验性；提供核心功能，但可能需根据反馈调整。

### 改进

**更新 using-superpowers 使用 Skill 工具而非 Read 工具**

- 技能调用由 Read 改为 Skill 工具

- 描述由“使用 Read 工具”改为“使用 Skill 工具”

- 第 3 步改为“用 Skill 工具读取并运行”

- 合理化列表改为“运行当前版本”

Skill 工具是 Claude Code 调用技能的正式机制；本次纠正 bootstrap 指引。

### 变更文件

- `skills/using-superpowers/SKILL.md`：Read 引用改为 Skill

### 改进

**加强 using-superpowers 对合理化规避的防护**

- 增加 EXTREMELY-IMPORTANT 强制检查块

- “即使只有 1% 可能适用，也必须阅读”

- “你没有选择，不能合理化绕过。”

- 增加强制首次响应协议清单

- 任何回复前完成五步

- 明确未执行即失败

- 增加八种常见合理化规避模式

- “这只是简单问题” → 错

- “我可以快速查文件” → 错

- “先收集信息” → 错

- 另有五种观察到的模式

这些改动针对代理在清晰指令下仍合理化跳过技能；强措辞和预先反驳用于提高合规难度。

### 变更文件

- `skills/using-superpowers/SKILL.md`：增加三层执行约束

### 新功能

**插件包含代码审查代理**

- 在 `agents/` 增加 `superpowers:code-reviewer`

- 按计划和编码标准系统审查

- 以前用户须自行配置代理

- 所有引用改为命名空间形式；其中相关的字段或标识包括 `superpowers:code-reviewer`。

- 修复 #55

### 变更文件

- 新增 `agents/code-reviewer.md`：审查清单与输出格式

- `skills/requesting-code-review/SKILL.md`：引用命名空间代理；其中相关的字段或标识包括 `superpowers:code-reviewer`。

- `skills/subagent-driven-development/SKILL.md`：同上；其中相关的字段或标识包括 `superpowers:code-reviewer`。

### 新功能

**头脑风暴工作流中的设计文档**

- 增加第 4 阶段：设计文档

- 实施前写入 `docs/plans/YYYY-MM-DD-<topic>-design.md`

- 恢复原命令转技能时丢失的功能

- 文档在工作树设置与实施计划前完成

- 用子代理在时间压力下验证合规

### 破坏性变更

**技能引用命名空间标准化**

- 内部技能均使用 `superpowers:` 前缀

- 格式如 `superpowers:test-driven-development`（原先不带前缀）；其中相关的字段或标识包括 `test-driven-development`。

- 影响所有必需子技能、推荐子技能和必需背景引用

- 与 Skill 工具调用一致

- 更新 brainstorming、executing-plans、subagent-driven-development、systematic-debugging、testing-skills-with-subagents、writing-plans、writing-skills

### 改进

**区分设计文档与实施计划名称**

- 设计文档用 `-design.md` 防止冲突

- 实施计划仍用 `YYYY-MM-DD-<feature-name>.md`

- 两者均在 `docs/plans/`，名称清楚区分

### 缺陷修复

- **修正 README 命令语法**（#44）：使用 `/superpowers:brainstorm` 而非 `/brainstorm`；Claude Code 自动加插件命名空间。

### 破坏性变更

**技能名统一小写**

- 前置 `name:` 使用小写 kebab-case 并与目录一致

- 例如 `brainstorming`、`test-driven-development`、`using-git-worktrees`

- 公告和交叉引用同步

- 目录、前置元数据、文档命名一致

### 新功能

**增强头脑风暴技能**

- 增加阶段、活动和工具使用速查表

- 增加可复制工作流清单

- 增加回访早期阶段的决策流程图

- 增加 AskUserQuestion 具体示例

- 增加“提问模式”，说明结构化与开放问题适用处

- 将关键原则改为可扫描表格

**集成 Anthropic 最佳实践**

- 新增 `skills/writing-skills/anthropic-best-practices.md`

- writing-skills SKILL.md 引用该指南

- 提供渐进披露、工作流和评估模式

### 改进

**技能交叉引用更清晰**

- 使用明确要求标记：

- `**REQUIRED BACKGROUND:**`：必须理解的背景

- `**REQUIRED SUB-SKILL:**`：工作流必须使用的子技能

- `**Complementary skills:**`：可选有帮助技能

- 移除旧路径格式（`skills/collaboration/X` → `X`）

- 集成节按必需/互补分类

- 交叉引用文档遵循最佳实践

**对齐 Anthropic 最佳实践**

- 修正描述语法和第三人称语气

- 增加速查表

- 增加可复制工作流清单

- 仅为不明显决策使用流程图

- 改进可扫描表格

- 所有技能低于建议 500 行

### 缺陷修复

- **恢复缺失命令重定向**：还原 v3.0 误删的 `commands/brainstorm.md`、`commands/write-plan.md`

- 修正 `defense-in-depth` 名称错配（原 `Defense-in-Depth-Validation`）

- 修正 `receiving-code-review` 名称错配（原 `Code-Review-Reception`）

- 修正 `commands/brainstorm.md` 技能引用

- 删除不存在相关技能引用

### 文档

**writing-skills 改进**

- 交叉引用使用明确要求标记

- 引用 Anthropic 官方最佳实践

- 改进正确引用格式示例

### 变更

现在使用 Anthropic 一方技能系统！

### 缺陷修复

- **本地技能仓库领先上游时不再误报警告**：区分本地落后（更新）、领先（无警告）、分叉（警告）。

### 缺陷修复

- **修复插件上下文 SessionStart 钩子**（#8、PR #9）：原静默“Plugin hook error”阻止上下文加载；修复包括：

- BASH_SOURCE 未绑定时用 `${BASH_SOURCE[0]:-$0}` 回退

- grep 空结果加 `|| true` 处理

# Superpowers v2.0.0 发布说明

## 概述

Superpowers v2.0 通过重大架构转变，使技能更易访问、维护和社区驱动。

重点是**技能仓库分离**：技能、脚本、文档移至独立 [obra/superpowers-skills](https://github.com/obra/superpowers-skills) 仓库。插件变为管理本地克隆的轻量外壳，技能会话开始自动更新；用户 fork 并按 git 流程贡献。技能库独立版本。

还新增九个解决问题、研究和架构技能。重写核心 **using-skills** 文档，采用命令式语气和清晰结构；**find-skills** 直接输出可粘贴 Read 工具的路径。

插件自动处理克隆、fork 与更新；贡献者可轻松改进共享技能。此版本为社区资源快速发展奠基。

## 破坏性变更

### 技能仓库分离

**最大变化：** 技能不再在插件内，已移至 [obra/superpowers-skills](https://github.com/obra/superpowers-skills)。

**对你意味着：**

- **首次安装**：插件自动克隆到 `~/.config/superpowers/skills/`

- **Fork**：设置时可选 fork 技能仓库（装有 `gh` 时）

- **更新**：会话开始自动快进更新

- **贡献**：分支工作、本地提交、向上游 PR

- **不再遮蔽**：旧个人/核心双层系统改为单仓库分支工作流

**迁移：**

若已有安装：

1. 旧 `~/.config/superpowers/.git` 备份为 `~/.config/superpowers/.git.bak`

2. 旧技能将备份到 `~/.config/superpowers/skills.bak`

3. 将在 `~/.config/superpowers/skills/` 创建obra/superpowers-skills的全新克隆

### 已移除功能

- **个人superpowers覆盖系统**——替换为git分支工作流

- **setup-personal-superpowers钩子**——由initialize-skills.sh替代

## 新功能

### 技能仓库基础设施

**自动克隆与设置**（`lib/initialize-skills.sh`）

- 首次运行克隆obra/superpowers-skills

- 安装GitHub CLI时提供创建分叉

- 正确设置upstream/origin远程

- 处理旧安装迁移

**自动更新**

- 每次会话启动从跟踪远程抓取

- 可快进时自动合并

- 需手动同步（分支分叉）时通知

- 手动同步使用pulling-updates-from-skills-repository技能

### 新技能

**问题解决技能**（`skills/problem-solving/`）

- **collision-zone-thinking**——强制组合无关概念以产生新洞见

- **inversion-exercise**——反转假设揭示隐藏约束

- **meta-pattern-recognition**——跨领域识别普遍原则

- **scale-game**——在极端条件下测试根本真相

- **simplification-cascades**——寻找可消除多个组件的洞见

- **when-stuck**——分派到合适的问题解决技术

**研究技能**（`skills/research/`）

- **tracing-knowledge-lineages**——理解想法随时间的演变

**架构技能**（`skills/architecture/`）

- **preserving-productive-tensions**——保留多个有效方案，避免过早强制解决

### 技能改进

**using-skills（原getting-started）**

- 从getting-started改名using-skills

- 使用命令语气彻底重写（v4.0.0）

- 关键规则前置

- 所有流程增加“为什么”解释

- 引用始终带/SKILL.md后缀

- 更清楚地区分刚性规则和弹性模式

**writing-skills**

- 交叉引用指引从using-skills移入

- 增加token效率（字数目标）章节

- 改进CSO（Claude Search Optimization）指引

**sharing-skills**

- 更新为新分支和PR流程（v2.0.0）

- 删除个人/核心分裂引用

**pulling-updates-from-skills-repository**（新）

- 与上游同步的完整流程

- 替代旧updating-skills技能

### 工具改进

**find-skills**

- 现在输出带/SKILL.md后缀的完整路径

- 路径可直接交给Read工具

- 更新帮助文本

**skill-run**

- 从scripts/移到skills/using-skills/

- 改进文档

### 插件基础设施

**会话启动钩子**

- 从技能仓库位置加载

- 会话启动时显示完整技能列表

- 打印技能位置信息

- 显示更新状态（成功更新/落后上游）

- 将“技能落后”警告移到输出末尾

**环境变量**

- `SUPERPOWERS_SKILLS_ROOT`设为`~/.config/superpowers/skills`

- 所有路径一致使用

## Bug修复

- 修复分叉时重复添加上游远程

- 修复find-skills输出重复“skills/”前缀

- 从session-start移除过时的setup-personal-superpowers调用

- 修复钩子和命令中的路径引用

## 文档

### README（中文说明）

- 更新为新技能仓库架构

- 突出链接superpowers-skills仓库

- 更新自动更新说明

- 修复技能名和引用

- 更新Meta技能列表

### 测试文档

- 增加全面测试清单`docs/TESTING-CHECKLIST.md`

- 为测试创建本地市场配置

- 记录手动测试场景

## 技术细节

### 文件变更

**新增：**

- `lib/initialize-skills.sh`——技能仓库初始化和自动更新

- `docs/TESTING-CHECKLIST.md`——手动测试场景

- `.claude-plugin/marketplace.json`——本地测试配置

**删除：**

- `skills/`目录（82个文件）——现位于obra/superpowers-skills

- `scripts/`目录——现位于obra/superpowers-skills/skills/using-skills/

- `hooks/setup-personal-superpowers.sh`——过时

**修改：**

- `hooks/session-start.sh`——从~/.config/superpowers/skills加载

- `commands/brainstorm.md`——路径改为SUPERPOWERS_SKILLS_ROOT

- `commands/write-plan.md`——路径改为SUPERPOWERS_SKILLS_ROOT

- `commands/execute-plan.md`——路径改为SUPERPOWERS_SKILLS_ROOT

- `README.md`——为新架构彻底重写

### 提交历史

本版本包含：

- 20多个技能仓库分离提交

- PR #1：受Amplifier启发的问题解决和研究技能

- PR #2：个人superpowers覆盖系统（后来替换）

- 多项技能完善和文档改进

## 升级说明

### 全新安装

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

插件自动处理所有事项。

### 从v1.x升级

1. **备份个人技能**（如有）：

2. **更新插件：**

```bash
/plugin update superpowers
```

3. **下次会话启动时：**

- 旧安装自动备份

- 克隆新技能仓库

- 有GitHub CLI时提供分叉选项

4. **迁移个人技能**（如有）：

- 在本地技能仓库创建分支

- 从备份复制个人技能

- 提交并推送到分叉

- 考虑以PR回馈

## 后续

### 用户

- 探索新的问题解决技能

- 尝试基于分支的技能改进流程

- 向社区回馈技能

### 贡献者

- 技能仓库现位于https://github.com/obra/superpowers-skills

- Fork→分支→PR流程

- 文档TDD方法见skills/meta/writing-skills/SKILL.md

## 已知问题

目前没有。

## 致谢

- 问题解决技能受Amplifier模式启发

- 社区贡献与反馈

- 对技能效果的广泛测试和迭代

**完整变更日志：**https://github.com/obra/superpowers/compare/dd013f6...main
**技能仓库：**https://github.com/obra/superpowers-skills
**问题：**https://github.com/obra/superpowers/issues
