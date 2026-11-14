# 最终审查与收尾

属于 superpowers:subagent-driven-development。计划中的每个任务都已完成。

最终全分支审查也获得审查包：运行 `bash scripts/review-package PLAN_FILE MERGE_BASE HEAD`（MERGE_BASE＝分支起始提交，例如 `git merge-base main HEAD`），将打印路径加入最终审查派发，使最终审查员读取一个文件而不是用 git 命令重新推导分支差异。派发到可用的最强模型（见 SKILL.md 的模型选择），使用 superpowers:requesting-code-review 的 [code-reviewer.md](../../requesting-code-review/code-reviewer.md)。让它查看账本中延后处理的轻微问题和暂存行，以判断合并前必须修复什么。

如果最终全分支审查返回问题，派发**一个**修复子智能体并提供完整问题清单，不要为每个问题派一个修复者。逐问题修复者会各自重建上下文并重跑套件；一个真实会话的最终审查修复波次比所有任务总和还贵。随后对修复波次精确运行一次限定范围复审（`bash scripts/review-package PLAN_FILE FIX_BASE HEAD` 覆盖修复范围，[re-review-prompt.md](../re-review-prompt.md)）。按修复循环的断路器裁定遗留问题（references/fix-loop.md）：用裁决暂存，或裁定关键问题并在账本记录决定。只有阻止运行计划的四件事（SKILL.md 顶部）在此阻止你。没有第二轮修复波次——finishing-a-development-branch 提供选项时，遗留关键问题会呈现给人类伙伴。

### 收尾

删除任何内容前，将所有包含 `Ruling:` 的账本行——预检裁决、暂存问题、断路器裁定，全部——按作出顺序收入最终消息的“我作出的裁决”下，并说明每项若错误会造成什么代价。该列表必须完整：账本有裁决，列表就必须有。人类伙伴只能从这个列表了解你代表他们作出的决定；他们阅读并返工你弄错的地方。随工作区一起消失的裁决是秘密决定。

最终全分支审查干净且修复已合并后，删除本计划工作区（`rm -rf <workspace>`）——现在 git 历史就是记录。同级目录属于其他计划，不要动。

使用 superpowers:finishing-a-development-branch。
