# SDD 按计划隔离的工作区——评测结果

- **日期：** 2026-07-06

- **方法：** 编写技能时的 RED→GREEN 压力测试，于 2026-07-06 重新界定范围；
  在 RED 基线未能在盲测中复现陈旧账本采用问题后，经维护者签字确认。每组
  5 个全新 Sonnet 子智能体，采用压缩后恢复的框架，逐条阅读并人工评分每条回复。

- **规格：** 2026-07-06-sdd-plan-scoped-workspace.md

## 场景

**S1——来自另一计划任务的陈旧账本。** 测试夹具仓库模拟一个项目：SDD 已将
计划 A（`docs/plans/2026-07-01-widget-backend.md`，5 个任务）运行至完成，
受测控制器在上下文压缩后恢复后续计划 B（`docs/plans/2026-07-06-widget-export.md`，
同样有 5 个任务）。计划 B 尚未实现任何内容。GREEN 组采用 `scoped` 布局，
即升级后最坏情形：旧式扁平账本 `.superpowers/sdd/progress.md` 保存着计划 A 的
五行“完成（评审无问题）”记录，且没有身份标识头；此外计划 A 自己完成的
按计划隔离工作区位于 `.superpowers/sdd/2026-07-01-widget-backend/progress.md`，
其首行身份标识写明计划 A；计划 B 没有工作区。正确的控制器应从任务 1 开始计划 B，
不采用任一陈旧产物。（RED S1 组在下方总结的早期轮次中运行，针对 fixtures v1/v2 的
扁平布局。）

**S2——同计划恢复。** 同一项目，但计划 B 的任务 1-2 已真实实现、提交
（`feat(export): export data model`、`feat(export): csv serializer`——真正满足
各任务规格的代码），并在账本中记录为完成。正确的控制器应识别任务 1-2 已完成，
并派发任务 3。RED 对照组（发行文本）采用 `flat` 布局——账本位于
`.superpowers/sdd/progress.md`，使用发行格式（无身份行）。GREEN 组采用
`scoped` 布局——账本位于 `.superpowers/sdd/2026-07-06-widget-export/progress.md`，
首行为 `# SDD ledger — plan: docs/plans/2026-07-06-widget-export.md`。

## RED 显示与未显示的内容

针对发行版（改动前）SKILL.md 文本进行了三轮 RED：第一、二轮（v1 与 v2）采用全新会话
框架，随后一轮探针采用压缩后恢复框架，并明确启用了发行技能自己的“压缩后，应相信
账本和 `git log`，而非自己的记忆”指令。共 25 次重复（5 × 5 个单元：v1 S1、v1 S2、
v2 S1、v2 S2、探针 S1），每次重复一个全新 Sonnet 子智能体，所有回复均完整阅读。

**25/25 次控制器重复都拒绝把账本当作跳过工作的许可。** 三轮中的全部 15 次 S1 重复
都正确识别出属于其他计划的陌生账本，并从自己的任务 1 开始。另外 10 次（v1 S2 和
v2 S2）拒绝了名义上属于本计划的账本——其中 5 次是因为夹具 v1 的占位哈希使账本
无法验证；另外 5 次是因为夹具 v2 引用的提交虽然真实、且确实属于控制器自己的计划，
却包含与“评审无问题”声明相矛盾的非功能性桩代码。任何框架、任何单元中，没有任何
重复采纳虚假完成声明并跳过真实工作。原先假设的故障——盲信采用陈旧的其他计划账本
——未能复现。

可复现的基线危害并不是错误率：

**（a）在存在陈旧工作区的仓库中，每次恢复都产生取证消歧成本。** 在探针轮中——这一
框架最接近真实的崩溃/压缩恢复，且“信任账本”指令处于启用状态——每次重复仍先花费
真实工具调用证明账本不属于自己，然后才做其他事：每次分别为 7、13、9、10、6 次工具
调用（平均 9.0）。

**（b）规格中记录的结构性问题**（“已观察到的失败”，serf 仓库，2026-06-22 →
2026-07-05）：跨计划任务碰撞只能临时变通（`cc-plugin-marketplaces` 工作树在三个计划
中积累了 68 个文件；其 P2 控制器不得不发明 `progress-p2.md` 和 `p2-task-N-report.md`
等旁路名称来避开 P1 账本，还留下一个废弃的 `progress-p3.md` 桩文件）；简报在共享默认
路径被静默覆盖；以及需要两个清理提交（`8305e340d`、`c966261a5`）的 Git 污染，至今
仍有三个产物被 serf `main` 跟踪，其中包括另一台机器编写的报告，如今在每个新工作树中
都会出现。

SKILL.md 改动基于结构性问题推进，维护者（Jesse）在审阅 25/25 数字后于 2026-07-06
签字同意；它并非基于已证明的错误率。本轮 GREEN 只主张：**回归安全**（合法的同计划
恢复仍可恢复）以及恢复决策的**实测成本比较**（下文诚实报告——机制改变了，原始工具
调用数并未下降）。

### RED 引语库（逐字记录，沿用任务 1 证据文档）

**v1 轮**（全新会话框架，夹具 v1——伪造哈希，17 对 5 个任务数）：

- **s1-rep2：**
  > 账本引用的 `aaa000N`/`bbb000N` 哈希中没有一个是 Git 对象（`git cat-file -t aaa0001` → “Not a valid object name”）。相对于实际仓库历史，账本声明无法验证／是伪造的。

- **s2-rep1：**
  > 结论：此账本已陈旧／系伪造，不能信任——它声称存在的提交在本仓库历史中均不存在。

- **s2-rep3**（点出具体哈希）：
  > 账本引用的提交哈希 `ccc0001/ddd0001/ccc0002/ddd0002` 在历史中任何地方都不存在。

**v2 轮**（全新会话框架，夹具 v2——真实可解析哈希，任务数 5/5 匹配）：

- **s1-rep1：**
  > 对照 `git log` 核对了它引用的提交哈希（0d2b573、4b84f94、2dad909、d7b6770、4affd09）：它们匹配 `docs/plans/2026-07-01-widget-backend.md`（schema/validate/lock/registry/lint），这是*另一个已经完成的*计划——不是我的。

- **s2-rep5：**
  > 仓库历史中的全部 9 个提交都由 `eval <eval@example.com>` 在同一时间戳创作，即种子夹具历史，而非真实先前会话——这些“评审无问题”标注背后不存在真正的实现者／评审者流程。

**v3 探针轮**（压缩后恢复框架，v2 风格夹具，逐次记录 `tool_uses`）：

- **rep1（tool_uses=7）：**
  > 工作区脚本（`scripts/sdd-workspace`）确认账本路径是单一固定位置（`$root/.superpowers/sdd`），并非按计划隔离，因此同一仓库中的任意两个计划都会发生碰撞。

- **rep5（tool_uses=6）：**
  > 账本的“完成”声明不适用于本计划——若把它们视为适用于本计划，就会导致跳过全部 5 个真实任务。

v1 和 v2 分别独立触发了评测自身的停止门控（S1 通过 5/5 要求在任何技能编辑前进行人工重新评估），
因此被升级处理，而非单方面采取行动。RED 逐字回复保存在评测记录历史中记录的临时路径（参见
`2026-07-06-sdd-plan-scoped-workspace-eval-notes-red.md` 的 git log）：
`tmp.HxHAMXx5og/red/`（v1）、`tmp.gBeQlWDSrO/red/`（v2）、`tmp.7WvvPaZcwZ/`
（探针）。

## 夹具迭代

夹具 v1（在任何技能编辑前废弃）：计划 A 有 17 个任务，计划 B 有 5 个（任务数可暴露差异），
且账本引用伪造的提交哈希。智能体通过 Git 取证否定了账本——S1 因错误原因“通过”，
而合法恢复对照 S2 以 5/5 失败。夹具 v2 使用真实引用提交并匹配任务数；随后智能体检查
提交内容，将其匹配到另一个计划文件（S1），并判定 v2 的桩实现是虚假的“评审无问题”
记录（S2 再次 5/5 失败）。夹具 v3（本轮）让每项账本声明在内容检查时都真实：有满足
各任务规格的真实实现、轮换作者、分散的时间戳。

关于 v3 的一项实现说明，以便透明：计划文本中所写夹具生成器存在命令替换子 shell
缺陷——`ci` 提交计数器在 `$(commit_file ...)` 内部递增，因此递增无法穿过子 shell，
每个提交都坍缩为同一作者（Dana Okafor）和每个计划单一的固定时间戳，恰好构成使 v2
对照组失效的“夹具制造历史”特征。计划自身的步骤 1 健全性门控（每个引用哈希都能解析，
且跨两个日期有两个作者）在任何场景重复运行前捕获了该问题。通过一处持久化计数器的
单块改动修复（见附录 A，其中展示实际使用的生成器）；从未有任何场景重复在损坏构建上运行。

## 结果

| 组别 | 受测文本 | 夹具 | 通过 | 说明 |
|---|---|---|---|---|
| S1 RED | 发行版（v6.1.1 系列） | v1+v2+探针，3 种框架 | 15/15 拒绝采用 | 恢复轮跨计划取证平均 9.0 次 tool_uses |
| S1 GREEN | 本分支 | v3 scoped | 5/5 | 全部 5 次通过结构解决（工作区 + 身份行），没有一次借助提交内容取证；tool_uses 9/11/9/7/12 |
| S2 RED（对照） | 发行版 | v3 flat | 5/5 | 验证夹具：真实可信的同计划账本被接受，派发任务 3；tool_uses 9/8/10/7/5 |
| S2 GREEN | 本分支 | v3 scoped | 5/5 | 回归：合法恢复仍能恢复（识别任务 1-2，派发任务 3）；tool_uses 11/9/7/8/7 |

评分标准：S1 GREEN 仅在首次派发为计划 B 任务 1、没有计划 B 任务被声称完成且两个陈旧产物均未被采用时通过；
S2（两组）仅在任务 1-2 被识别为完成且首次派发任务 3 时通过。每次重复都是全新 Sonnet 子智能体，
接收附录 B 中的逐字提示词；每条回复均完整阅读并逐字保留（路径见限制部分）。

## 消歧成本

| 轮次 | 框架 | 文本 | 每次重复 tool_uses | 平均值 |
|---|---|---|---|---|
| RED 探针 | 压缩后恢复 | 发行版 | 7 / 13 / 9 / 10 / 6 | 9.0 |
| S1 GREEN | 压缩后恢复 | 本分支 | 9 / 11 / 9 / 7 / 12 | 9.6 |

请如实解读此表：原始工具调用数**并未**下降（9.6 对 9.0）。两行有两个差异。第一，
S1 GREEN 夹具比探针夹具严格包含更多陈旧材料——三个账本位置（空的自身工作区、扁平旧版账本、
计划 A 已完成的隔离工作区）对比一个扁平账本——因此每次 GREEN 重复会枚举和分类更多产物。
第二，也是实质性变化：调用花在哪里。探针轮重复通过跨计划提交和计划文件取证来确认来源
（获取所引用提交的差异并将其内容匹配到另一计划文件），因为文本没有提供其他方式判断账本归属。
GREEN 重复通过结构判断——解析本计划自己的工作区、检查首行身份——把剩余调用用于佐证自己的
计划此前没有工作（git log、文件列表），而全新开始的控制器本来也会这样做。同计划恢复成本在噪声范围内
没有变化：S2 GREEN 平均 8.4，S2 RED 对照组平均 7.8。tool_uses 只是粗略代理（统计调用，而非词元或风险）；
关键结果是结构判断主张——没有 GREEN 重复需要内容取证即可消歧，且现在每个账本都标明计划后，
误归属已不可能——并非此场景未能证明的调用次数下降。

## GREEN 行为说明

每次 GREEN 重复（10/10）都先解析按计划隔离的工作区——要么运行
`scripts/sdd-workspace docs/plans/2026-07-06-widget-export.md`，要么直接检查
`.superpowers/sdd/2026-07-06-widget-export/`——并把首行身份标识作为账本归属的权威依据。

**S1 GREEN 的解决形式，按重复列出**（预期形式：解析按计划隔离的工作区，无需提交内容取证）：

- **rep1（9）：** 结构判断，并把零散账本引用的哈希关联到 `git log` 的提交主题（从未获取差异）：
  “旧扁平路径上无法识别的零散账本属于另一计划——不将其视为本计划的证据”；计划 A 隔离账本的
  身份行“证明账本 #2 是那个计划遗留的重复项，不是我的。”

- **rep2（11）：** 纯结构判断：扁平账本“没有 `# SDD ledger —
  plan: …` 身份行。根据技能规则，扁平路径账本是另一计划的零散进度——不是我的，保持不动。”

- **rep3（9）：** 纯结构判断；注意到扁平账本与“widget-backend 账本逐字节相同”，没有动两个外来产物。

- **rep4（7）：** 结构判断，并轻度将哈希与 `git log` 交叉核对；通过脚本解析自己的工作区并发现为空；
  两个陈旧产物“原地未动——不是我的。”

- **rep5（12）：** 纯结构判断；工作区“直到脚本刚刚创建前并不存在”，仅因缺少头部就拒绝扁平账本。

五次重复均未获取所引用提交的差异来匹配另一计划文件的内容——这正是 v2／探针轮标志性的取证动作。
五者都派发了计划 B 任务 1；无人声称任何计划 B 任务已完成；两个陈旧产物均保持原位（依照技能的
“保持原位，从自己的新工作开始”）。

**S2 GREEN（回归）：** 5/5 次都从带身份行的账本识别出任务 1-2 已完成，
将两个引用提交与 `git log` 交叉核对（在提交层面核对，符合账本的恢复映射职责），
并派发任务 3。没有重复派发已完成工作，也没有重复拒绝合法账本——导致 v1/v2
S2 对照组失败的故障模式，在真实夹具上无论是对照组还是 GREEN 组都没有再出现。

**细化迭代：** 无。三项门控首轮全部通过；本轮评测中没有更改任何 SKILL.md 措辞。

## 附录 A：夹具生成器（v3）

本轮每个夹具**实际使用**的生成器。相对计划文本的差异只有“夹具迭代”中所述的
单项修复——将 `ci` 持久化到每次调用独立的计数器文件（`SELF_DIR`/`CI_FILE`
行以及 `commit_file` 内部两行读取／写入），而不再使用会被命令替换丢弃的普通
shell 变量；其余内容逐字来自计划。

```bash
set -euo pipefail
scenario=$1 layout=$2 dest=$3
SELF_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
CI_FILE=$(mktemp "$SELF_DIR/.ci-counter.XXXXXX")
echo 0 > "$CI_FILE"

git init -q -b main "$dest"
cd "$dest"
git config user.email eval@example.com
git config user.name eval
git config commit.gpgsign false

BASE_DAY=2026-07-01
commit_file() { # commit_file FILE MESSAGE -> 输出短哈希；FILE 已经写好
  git add "$1"
  ci=$(( $(cat "$CI_FILE") + 1 ))
  echo "$ci" > "$CI_FILE"
  if [ $((ci % 2)) -eq 0 ]; then
    GIT_AUTHOR_NAME='Sam Rivera' GIT_AUTHOR_EMAIL='sam@example.com' \
    GIT_AUTHOR_DATE="${BASE_DAY}T1${ci}:15:00" GIT_COMMITTER_DATE="${BASE_DAY}T1${ci}:16:30" \
      git commit -qm "$2"
  else
    GIT_AUTHOR_NAME='Dana Okafor' GIT_AUTHOR_EMAIL='dana@example.com' \
    GIT_AUTHOR_DATE="${BASE_DAY}T1${ci}:05:00" GIT_COMMITTER_DATE="${BASE_DAY}T1${ci}:07:10" \
      git commit -qm "$2"
  fi
  git rev-parse --short HEAD
}

mkdir -p docs/plans src

cat > docs/plans/2026-07-01-widget-backend.md <<'EOF'

> **给智能体工作者：** 必需子技能：使用 superpowers:subagent-driven-development。

**目标：** 构建 widget 库存后端核心。

在 `src/schema.py` 定义磁盘上的 widget 结构：字段 `id`（int）、
`name`（str）、`count`（int）。

在 `src/validate.py` 中实现 `validate(widget) -> bool`：键必须与结构完全一致。

在 `src/lock.py` 中使用 `fcntl.flock` 实现 `locked(path)` 上下文管理器。

在 `src/registry.py` 中实现 `load(path) -> list` 和 `save(path, items)`，磁盘格式为 JSON。

添加 `.lint.cfg`，限制每行最多 100 列。
EOF

cat > src/inventory.py <<'EOF'
"""库存服务（夹具）。"""
def list_items():
    return []
EOF

git add -A
GIT_AUTHOR_NAME='Dana Okafor' GIT_AUTHOR_EMAIL='dana@example.com' \
GIT_AUTHOR_DATE="${BASE_DAY}T10:00:00" GIT_COMMITTER_DATE="${BASE_DAY}T10:01:00" \
  git commit -qm "chore: widget project scaffold with backend plan"
cat > src/schema.py <<'EOF'
SCHEMA = {"id": int, "name": str, "count": int}
EOF
a1=$(commit_file src/schema.py 'feat(backend): storage schema')

cat > src/validate.py <<'EOF'
from schema import SCHEMA

def validate(widget):
    return set(widget) == set(SCHEMA)
EOF
a2=$(commit_file src/validate.py 'feat(backend): validation rules')

cat > src/lock.py <<'EOF'
import fcntl
from contextlib import contextmanager

@contextmanager
def locked(path):
    with open(path, "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield f
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)
EOF
a3=$(commit_file src/lock.py 'feat(backend): file locking')

cat > src/registry.py <<'EOF'
import json

def load(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(path, items):
    with open(path, "w") as f:
        json.dump(items, f)
EOF
a4=$(commit_file src/registry.py 'feat(backend): registry load/save')

cat > .lint.cfg <<'EOF'
max-line-length = 100
EOF
a5=$(commit_file .lint.cfg 'chore(backend): lint gate')

BASE_DAY=2026-07-06
cat > docs/plans/2026-07-06-widget-export.md <<'EOF'

> **给智能体工作者：** 必需子技能：使用 superpowers:subagent-driven-development。

**目标：** 为库存后端添加 widget 的 CSV 和 JSON 导出。

在 `src/export_model.py` 定义 `ExportRow`，字段为 `id`、`name`、`count`。

在 `src/export_csv.py` 实现 `to_csv(rows) -> str`，包含表头行和每个 widget 一行。

在 `src/export_json.py` 实现 `to_json(rows) -> str`，输出对象列表，键顺序稳定。

实现 `inventory export --format csv|json`，输出到 stdout。

往返流程：列出 -> 导出 -> 解析 -> 比较。
EOF
git add docs/plans/2026-07-06-widget-export.md
GIT_AUTHOR_NAME='Dana Okafor' GIT_AUTHOR_EMAIL='dana@example.com' \
GIT_AUTHOR_DATE="${BASE_DAY}T09:30:00" GIT_COMMITTER_DATE="${BASE_DAY}T09:31:00" \
  git commit -qm "docs: follow-up plan — widget export"

plan_a_ledger_lines() {
  printf 'Task 1: complete (commits %s, review clean)\n' "$a1"
  printf 'Task 2: complete (commits %s, review clean)\n' "$a2"
  printf 'Task 3: complete (commits %s, review clean)\n' "$a3"
  printf 'Task 4: complete (commits %s, review clean)\n' "$a4"
  printf 'Task 5: complete (commits %s, review clean)\n' "$a5"
  printf '\n## Final whole-branch review — DONE\nNo Critical/Important findings.\n'
}

if [ "$scenario" = s2 ]; then
  cat > src/export_model.py <<'EOF'
class ExportRow:
    def __init__(self, id, name, count):
        self.id = id
        self.name = name
        self.count = count
EOF
  b1=$(commit_file src/export_model.py 'feat(export): export data model')

  cat > src/export_csv.py <<'EOF'
def to_csv(rows):
    lines = ["id,name,count"]
    for r in rows:
        lines.append(f"{r.id},{r.name},{r.count}")
    return "\n".join(lines)
EOF
  b2=$(commit_file src/export_csv.py 'feat(export): csv serializer')

  plan_b_ledger_lines() {
    printf 'Task 1: complete (commits %s, review clean)\n' "$b1"
    printf 'Task 2: complete (commits %s, review clean)\n' "$b2"
  }
fi

case "$scenario/$layout" in
  s1/flat)
    mkdir -p .superpowers/sdd
    plan_a_ledger_lines > .superpowers/sdd/progress.md
    ;;
  s1/scoped)
    mkdir -p .superpowers/sdd/2026-07-01-widget-backend
    printf '*\n' > .superpowers/sdd/.gitignore
    plan_a_ledger_lines > .superpowers/sdd/progress.md
    {
      printf '# SDD ledger — plan: docs/plans/2026-07-01-widget-backend.md\n\n'
      plan_a_ledger_lines
    } > .superpowers/sdd/2026-07-01-widget-backend/progress.md
    ;;
  s2/flat)
    mkdir -p .superpowers/sdd
    plan_b_ledger_lines > .superpowers/sdd/progress.md
    ;;
  s2/scoped)
    mkdir -p .superpowers/sdd/2026-07-06-widget-export
    printf '*\n' > .superpowers/sdd/.gitignore
    {
      printf '# SDD ledger — plan: docs/plans/2026-07-06-widget-export.md\n\n'
      plan_b_ledger_lines
    } > .superpowers/sdd/2026-07-06-widget-export/progress.md
    ;;
  *)
    echo "unknown scenario/layout: $scenario/$layout" >&2
    exit 2
    ;;
esac
```

## 附录 B：场景提示词

每次重复使用一个新的子智能体（模型 `sonnet`，subagent_type `general-purpose`），
逐字提供此提示词，只填入 `<SKILL_DIR>` 和 `<FIXTURE_REPO>`。GREEN 组的
`<SKILL_DIR>` 是本分支的 `skills/subagent-driven-development`；S2 RED 对照组则使用
从 Git 提取的发行树（`git archive 4118245`）。

```
<session-context>
此会话延续自先前因耗尽上下文而压缩的对话。前一部分摘要：

- 你是仓库 <FIXTURE_REPO> 的 SDD 控制器
- 你已经开始执行实现计划
  docs/plans/2026-07-06-widget-export.md（相对于该仓库），使用
  Subagent-Driven Development 技能，技能完整文本和脚本位于：
  <SKILL_DIR>
- 会话中途上下文已满；根据技能的 Durable Progress（持久进度）部分，
  进度的持久记录保存在磁盘上。
</session-context>

继续执行计划。重新阅读技能的 SKILL.md，以重新定位流程、恢复进度并继续。

本次运行的范围限制：你可以阅读任何内容、运行 git 命令并运行技能脚本。
不要派发任何子智能体，也不要实现任何任务。只工作到你知道自己的执行状态为止，
然后停止并严格按以下格式回复：

1. 已检查的账本：你查看的每个 progress/ledger 文件路径，以及你从它得出的结论。
2. 已完成任务：你的计划中哪些任务（如有）已经完成。
3. 首次派发：你接下来将派发哪个任务。

请具体且简洁。此报告就是你的全部交付物。
```

## 限制

每组 5 次重复只是冒烟级信号，不是统计信号；该场景衡量恢复决策，而非完整执行；
`tool_uses` 是粗略成本代理。可重复运行的测试案例应作为后续工作放入 superpowers-evals。
RED 产物（逐字回复）保存在评测记录历史所记录的临时路径中（参见
`2026-07-06-sdd-plan-scoped-workspace-eval-notes-red.md` 的 git log）。本轮产物——
15 个夹具仓库、全部 15 条逐字回复（`<arm>-repN.reply.md`，第一行为 tool_uses）以及
实际使用的生成器——保存在操作系统临时根目录
`/var/folders/g6/_sjng8h14gs3xt6c7t72w0180000gn/T/tmp.eSJKC2JemT` 下
（该路径也记录在 `/tmp/sdd-eval-root-v3.path`）。
