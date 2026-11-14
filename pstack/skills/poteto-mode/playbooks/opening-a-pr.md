### 创建 PR

每个其他手册结尾调用。

**工作树。** 从 `main` 的 git 工作树工作，子智能体继承它。同分支多个 `Task` 各用工作树，或之间 `git fetch && git reset --hard origin/<branch>`。分支有无关脏工作：打补丁、换新工作树、应用。工作树混乱：从 `main` 重置并最小重做。

**提交。** 可以多提交；创建 PR 前变基为小而有序提交。每次提交是未来 PR：可独立落地并讲清故事。修复属于刚做提交时 amend，独立则新提交；正文不重述标题。

**PR。** 提交前对差异运行 `cursor-team-kit` 的 `/deslop`，审查前运行 `/no-comments`。标题、描述、提交正文用 `/technical-writing`（除 Diátaxis 的全部层级，遵循 STE：每动作一词、保留冠词、可用朴素动词代替 `-ing`），再运行 `/unslop`。

**标题。** Conventional Commits `type(scope): subject`，无句号。类型如 `feat`、`fix`、`docs`、`refactor`、`test`、`chore`、`perf`。scope 是区域，如 `pstack`。subject 简短祈使，承载变更时写真实符号，例如 `fix(pstack): retarget opening-a-pr babysit trigger`。，相关标识为 `poteto-mode`。

**描述。** PR 正文是一分钟简报，面向已有差异的审阅者。说明为何存在、不包含什么、可能破坏什么、如何证明有效。短句、少标识符、无大段文字。正文成为 squash 提交正文，保持约 40 行内。使用 `##` 标题，按以下顺序，无内容章节删除：

- `## Why`：问题和办法，1 至 3 短句。无 SHA、变基族谱或“基于 main”。

- `## What changed`：1 至 3 短条目。只在承载变更时写符号或路径；重命名／重定向写出两侧。

- `## Scope`：必需。1 至 3 项说明覆盖及有意排除内容（后续、已知缺口）。不逐文件长文。

- `## Tradeoffs`：只列审查者会问的被否决选项。无真实选择时省略。

- `## Blast Radius`：1 至 2 句说明影响谁或什么及安全／风险原因。main 为红时说明继续红的成本。

- `## Verification`：1 至 3 条，每项真实运行路径和结果。性能写一个带单位的主数字、`before → after`、其余材料链接。无样本方法、集群复述或指标表。

章节后可附证明声明的视频／截图。完整 SHA、通道复述、杠杆校正长文、逐文件清单和 CLEAN 结论放链接产物，不放正文。

**平台。** 首次 PR 操作前确定并保持用于创建、编辑、查看、观察、合并。默认 GitHub CLI `gh`；`command -v origin` 成功且能解析仓库时优先 `origin pr ...`，否则 `gh` 并记录回退。不要求 Graphite `gt`。

**内建 PR 工具。** 有内建工具就通过它创建、编辑、重定向、标就绪；CLI 生成的 PR 会漏掉其跟踪内容。工具不覆盖或其他操作按已确定平台。

**大小和堆叠。** 优先五个窄 PR 而非一个大 PR。堆叠是基分支链：根指向 trunk，子分支变基到父精确尖端并指向父分支；父合并后按 `playbooks/shipping.md` 第 4 步移到 trunk。无内建工具时按平台使用 `origin pr create --status open --base <parent-branch>` 或 `gh pr create --base <parent-branch>`，重定向用对应 `edit`。独立工作从 trunk 分支；大幅堆叠前先变基 trunk。，相关标识为 <parent-branch> <parent-branch> <pr> <pr> `origin pr edit <pr> --base <parent-branch>` `gh pr edit <pr> --base <parent-branch>`。

**就绪。** 所有 PR 以就绪打开，绝不用草稿。内建工具默认草稿时设 `draft: false`；Origin 传 `--status open`；`gh` 省略 `--draft`。仍为草稿则通过工具标就绪或 `origin pr ready`／`gh pr ready`。引用状态前运行 `view`。，相关标识为 <number> <number> <number> <number> `origin pr ready <number>` `gh pr ready <number>` `origin pr view <number>` `gh pr view <number>`。

**照看。** 创建 PR 不开始照看。发布 URL 继续构建；先完成阶段或堆叠。整个堆叠存在且用户要求后另做照看。每新 PR 照看会停滞构建并浪费后续波次重启的检查。反馈偏离意图时回推。

子智能体创建 PR 时运行 `/deslop`、`/no-comments` 并发布 URL，返回父代理而不照看；Autopilot-full/stack 负责人例外，其简报指定照看循环，代码就绪后开始并报告可合并，豁免此处等待整个堆叠的规则。，相关标识为 `playbooks/babysit.md` `playbooks/babysit.md`。
