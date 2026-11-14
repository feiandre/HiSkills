# SDD 计划作用域工作区——设计

- **日期：**2026-07-06

- **状态：**方向已由Jesse在2026-07-06批准；本规格记录调查建议

- **问题负责人：**subagent-driven-development技能（`skills/subagent-driven-development/`）

## 问题

SDD的持久进度工作区（`.superpowers/sdd/`，v6.0.0/v6.0.3引入）没有计划身份和生命周期终点。所有产物以裸任务号命名（`progress.md`、`task-N-brief.md`、`task-N-report.md`），SKILL.md要求启动控制器把找到的台账都当自己的进度：

> 技能开始时检查台账：
> `cat "$(git rev-parse --show-toplevel)/.superpowers/sdd/progress.md"`。标为完成的任务就是DONE，不重新派发；从第一个未完成任务继续。

同一工作树中执行**后续计划**的新会话会把前计划台账当作自己的，按技能字面会跳过任务。工作区从不删除，陈旧状态永久累积。

### 已观察失败（serf仓库，2026-06-22→2026-07-05）

- **跨计划冲突，临时绕过：**`cc-plugin-marketplaces`工作树三个计划累积68个文件。P2控制器自造`progress-p2.md`和`p2-task-N-report.md`避开P1；P2简报静默覆盖默认路径下P1简报；遗留`progress-p3.md`桩。

- **三次污染git：**SDD临时文件被提交，需两次清理提交（`8305e340d`、`c966261a5`）；今天serf main仍有三个跟踪产物，包括另一台机器撰写的报告，会在每个新工作树出现。后续计划任务1报告覆盖无关跟踪文件，永久制造`git status`噪声。

- 自忽略`.gitignore`只在脚本运行时写；手工追加台账的控制器从不创建它，文件一旦跟踪，gitignore无效。

### 根因

身份不在数据中；正确性依赖无触发器的清理。只靠计划结束清理，会在台账本应拯救的崩溃/压缩情形失败。身份必须结构化。

## 设计

### 1. 每计划工作区目录（结构身份）

工作区变为`.superpowers/sdd/<plan-slug>/`，slug是计划文件名去`.md`（文件名已日期化kebab-case，如`2026-07-04-plugin-marketplaces-p1-backend-core`）。不同计划产物不再冲突；陈旧兄弟目录无人引用而惰性。 （保留标识：`<plan-slug>`）

脚本接口（均在`skills/subagent-driven-development/scripts/`）：

- `sdd-workspace PLAN_FILE`——解析并创建`<repo-root>/.superpowers/sdd/<plan-slug>/`；维护`.superpowers/sdd/.gitignore`（父级，内容`*`）；打印绝对路径；缺参数或文件不存在退出2；slug去扩展后不得为空。 （保留标识：`.gitignore`）

- `task-brief PLAN_FILE N [OUTFILE]`——签名不变；默认输出经`sdd-workspace PLAN_FILE`移到`<workspace>/task-N-brief.md`。

- `review-package PLAN_FILE BASE HEAD [OUTFILE]`——首参新增PLAN_FILE；默认输出`<workspace>/review-<base7>..<head7>.diff`。

旧扁平布局无兼容路径：脚本和SKILL.md同一插件版本发布，且无其他调用者（已明确确认）。

### 2. 台账写明计划（手工台账保护）

台账仍为`<workspace>/progress.md`；创建时首行必须为：

```
# SDD台账——计划：docs/superpowers/plans/<plan-file>.md
```

SKILL.md启动检查改为计划作用域，以该可观察行作条件护栏，采用正向配方：用`sdd-workspace PLAN_FILE`解析本计划工作区，读取其中`progress.md`；计划行指向其他文件的台账属于其他计划，保持不动并使用自己的工作区。覆盖手工写台账和旧扁平路径遗留。

护栏措辞服从评估结果；只对RED基线实际观察失败增加反制。

### 3. 工作区生命周期（卫生，不是正确性）

最终整分支审查干净且修复波（若有）合并后——交给`superpowers:finishing-a-development-branch`前——控制器删除本计划目录（`rm -rf "$WORKSPACE"`）。记录由git历史承担，台账的中途压缩恢复职责结束。绝不碰兄弟目录；崩溃/并行计划各有目录，刻意停放的跨计划产物（如`WAVE1-HANDOFF.md`）直接放在`.superpowers/sdd/`，不归任何计划清理。

### 4. SKILL.md触点

- **持久进度**：计划工作区解析、计划作用域台账、含计划行的台账格式、不匹配护栏、完成删除、更新`git clean -fdx`路径风险。

- **实现者状态/审查提示/文件交接/危险信号/示例流程**：更新脚本签名（`review-package PLAN_FILE BASE HEAD`）和路径；`implementer-prompt.md` 与 `task-reviewer-prompt.md` 不含路径，无需改。

- 只有RED基线显示结构修复+护栏仍失败时才增加危险信号。

## 明确不在范围

- 不改`finishing-a-development-branch`或其他技能。

- 除现有父`.gitignore`外，不加git级提交防护。 路径为 `.superpowers/`。

- 不追溯清理serf仓库（另行跟进）。

- 无旧布局迁移或回退读取。

## 测试

### 确定性shell测试（扩展`tests/claude-code/test-sdd-workspace.sh`）

- `sdd-workspace PLAN`打印并创建`<root>/.superpowers/sdd/<slug>`；缺参数/文件报错。

- 两个计划解析到不同目录，`task-brief`产物各归其目录。

- `review-package PLAN BASE HEAD`写计划目录。

- 父`.gitignore`自忽略：工作区不出现在`git status`/`git add -A`。

- 关联工作树区分保持。

- 检查现有套件旧路径预期（初始grep无命中，审计仍是任务关卡）。 现有测试包括 `test-subagent-driven-development.sh`。 另含 `test-subagent-driven-development-integration.sh`。 集成测试文件的后缀为 `-integration.sh`。

### 评估（writing-skills RED→GREEN，2026-07-06重划范围）

压力场景用全新Sonnet子代理对临时目录夹具运行（不在本工作树），采用压缩恢复框架，逐次人工评分；测的是控制器恢复决策，不派真实实现者。

**迫使重划范围的RED结果：**原假设“盲目采用外来台账”**未复现**：三种框架25/25次都对照git日志和计划文件核实提交，拒绝外来台账并从计划B任务1开始，每次花6–13次工具调用。两次夹具迭代诚实证明（伪造哈希立即识破；桩实现被识破为虚假“审查干净”），S2对照两次失败。完整记录在已提交评估文档。

**重划范围和关卡：**

- 修改依据结构记录（冲突、临时旁路名、覆盖简报、git污染——serf仓库）加实测歧义成本，维护者签字替代SKILL.md写作技能的失败基线要求。

- **S1 GREEN（需5/5）：**新作用域布局中放计划A陈旧工作区和旧扁平垃圾；计划B恢复控制器直接解析自身工作区并从任务1开始；相对RED基线的`tool_uses`成本差为7/13/9/10/6。

- **S2 RED对照（≥4/5）和GREEN（5/5）**使用真实v3夹具：合法同计划恢复识别任务1–2并派任务3。保护台账原本目的，不能破坏。

结果写入`docs/superpowers/specs/2026-07-06-sdd-plan-scoped-workspace-eval-results.md`并在PR总结。

## 风险

- **不同目录同名计划slug冲突：**接受；文件名按惯例有日期，同basename通常同计划，恢复是期望行为。

- **控制器完全跳过脚本：**以台账计划行为护栏，S1测量文字是否有效。

- **工作区崩溃后重跑完成计划：**台账合法属于同计划，恢复而非重启是设计行为，现有`git log`核查覆盖分歧。
