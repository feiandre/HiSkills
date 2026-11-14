# 将 drill 迁入 superpowers 的 `evals/`——设计

## 背景

Drill 是一个 Python 技能遵循性基准测试，独立存放于 `obra/drill` 仓库。它驱动真实 tmux 会话，让一个 LLM 扮演模拟用户，再让一个 LLM 验证器检查生成的转录记录，并报告各场景通过或失败。它支持 Claude Code、Codex、Gemini CLI，以及（根据近期提交）OpenCode 和 Copilot CLI。

Drill 已经是 superpowers *事实上的*评估框架。drill 仓库的 PRI-1397 系列提交将约 22 个 superpowers bash 测试迁为 drill 场景，superpowers 最近的提交（`a2292c5`）还明确删除了一个冗余 bash 测试，提交信息为*“已由 drill 行为覆盖取代”*。迁移已经启动；本规格将其完成。

本工作把 drill 移到 superpowers 的 `evals/` 下，逐文件验证 drill 场景的覆盖情况后删除冗余 bash 测试，并更新文档，让贡献者找到新结构。

## 目标

1. `evals/` 成为 superpowers 的规范评估框架——包含 drill 的全部源码、场景、夹具、提示词、后端配置和测试。

2. 删除 `superpowers/tests/` 中经逐个验证、被 drill 场景 100% 覆盖的 bash 测试；其余保留。

3. `tests/`（插件基础设施：bash + node + python 集成测试）与 `evals/`（使用扮演者和验证器评估 LLM 行为）之间有明确且有文档说明的分工。

4. 顶层文档（`README.md`、`CLAUDE.md`、`docs/testing.md`）引导贡献者前往正确位置。

5. 独立的 `obra/drill` 仓库继续存在（此 PR 不改它），在此 PR 合并后另行手动归档。

## 非目标

- **CI 集成。** 此处仅手动运行。自然的后续工作是“分层”：每个 PR 运行快速子集，每晚及按需运行完整扫描。这需要决定 API 预算、配置 GitHub Actions 密钥，并准备安装有 `tmux` + `node` + `python` + `claude` / `codex` / `gemini` CLI 的运行器镜像。不在本次范围内。

- **场景与技能放在一起。** 场景仍集中在 `evals/scenarios/`。如果以后决定各技能源码旁应存放自己的场景，只需查找路径并重命名；YAML 格式不变。

- **重命名内部 Python 包**（`drill` → `evals`）。目录名使用面向用户的 `evals/`；Python 包保留 `drill` 名称，以缩小差异。`evals/README.md` 中会简短说明。

- **归档 Drill 仓库。** 此 PR 不改 `obra/drill`。合并后手动归档 drill 仓库（在 GitHub 上只读，README 指向 `obra/superpowers/evals/`）。

- **将 `tests/claude-code/analyze-token-usage.py` 移到 `evals/bin/`。** 它是有用的工具，并非测试代码。以后可以移动；此 PR 不要求。

## 分支

从 `dev` 创建 `f/evals-lift` 分支。此工作独立于尚未合并的 `f/cross-platform` PR——除可能涉及 `README.md` 外，没有共享的文件修改；即便它冲突，也足够小，可以在合并时解决。

## 迁移后的架构

```
superpowers/
  evals/                              ← 新增（完整复制 drill）
    pyproject.toml                    （Python 3.11，由 uv 管理）
    uv.lock
    .gitignore                        （drill 自带；results/、.venv/、.env）
    README.md                         （原 drill 的 README；更新安装说明）
    CLAUDE.md                         （原 drill 的 CLAUDE.md；更新路径）
    docs/
      design.md                       （drill 的设计——原样保留，从本规格交叉链接）
      manual-testing.md
      pressure-and-red-testing.md
    drill/                            （Python 包；保留名称；cli、engine、actor、verifier 等）
    backends/                         （claude-*.yaml、codex.yaml、gemini.yaml）
    scenarios/                        （32 个以上 YAML 场景）
    setup_helpers/                    （15 个 Python 辅助程序；create_base_repo、sdd_*、spec_*、worktree 等）
    fixtures/                         （template-repo、sdd-go-fractals、sdd-svelte-todo）
    prompts/                          （actor.md、verifier.md）
    bin/                              （断言辅助脚本：tool-called、tool-count 等）
    tests/                            （drill 自身的 pytest 套件）

  tests/                              ← 默认保留 bash 测试
    brainstorm-server/                ← 保留（brainstorm-server JS 代码的 node 测试）
    opencode/                         ← 保留（插件加载测试）
    codex-plugin-sync/                ← 保留（同步验证）
    claude-code/                      ← 大部分保留——参见删除关卡
    explicit-skill-requests/          ← 保留，除非已验证被替代
    skill-triggering/                 ← 保留，除非已验证被替代
    subagent-driven-dev/              ← 保留，除非已验证被替代

  docs/
    testing.md                        ← 更新（分成“插件测试”和“技能行为评估”）
    superpowers/
      specs/
        2026-05-06-lift-drill-into-evals-design.md   ← 本规格

  README.md                           ← 在贡献部分简短指向 evals/
  CLAUDE.md                           ← 一行提示“评估框架位于 evals/”
```

此 PR 完成后，`tests/` 和 `evals/` 目录的职责明确区分：

- **`tests/`**——插件的非 LLM 代码能否工作？包含 brainstorm-server JS 代码、OpenCode 插件加载、codex-plugin-sync 同步验证的单元和集成测试。使用 bash + node + python。

- **`evals/`**——代理在真实 LLM 会话中的行为是否正确？使用扮演者和验证器的 Drill 场景。仅使用 Python，运行真实 tmux 会话。

## 删除关卡（逐个 bash 测试）

*仅当*能验证某个 drill 场景覆盖了 bash 测试的每项断言，才删除该测试。实施计划逐文件记录验证：阅读 bash 测试，列出检查项，找到 drill 场景，确认每项检查都有对应的 `verify.assertions` 或 `verify.criteria` 条目。只要缺一项，就选择扩展 drill 场景或保留 bash 测试。默认保留。

**暂定覆盖对应表**（基于提交信息；任何删除前都需要逐文件验证）：

| Bash 测试 | 声称对应的 drill 替代项 | 覆盖状态 |
|-----------|---------------------------|-----------------|
| `tests/skill-triggering/prompts/*`（6 个提示词文件） | `triggering-*.yaml`（6 个场景） | 候选——删除前逐提示词验证 |
| `tests/skill-triggering/run-test.sh`、`run-all.sh` | 不适用（运行器，并非测试） | **保留**——运行器脚本 |
| `tests/explicit-skill-requests/prompts/please-use-brainstorming.txt` | 需要验证——drill 尚无明显对应项 | 很可能**保留**，除非增加 drill 场景 |
| `tests/explicit-skill-requests/prompts/use-systematic-debugging.txt` | 需要验证——drill 无明显对应项 | 很可能**保留**，除非增加 drill 场景 |
| `tests/explicit-skill-requests/run-claude-describes-sdd.sh` | 部分对应 → `mid-conversation-skill-invocation.yaml` | 候选——逐脚本验证 |
| `tests/explicit-skill-requests/run-haiku-test.sh` | 没有 drill 场景覆盖 Haiku 专属行为 | **保留** |
| `tests/explicit-skill-requests/run-multiturn-test.sh`、`run-extended-multiturn-test.sh` | 没有 drill 场景覆盖多轮铺垫 | **保留**，除非增加 drill 场景 |
| `tests/explicit-skill-requests/run-test.sh`、`run-all.sh` | 不适用（运行器） | **保留** |
| `tests/subagent-driven-dev/go-fractals/`、`tests/subagent-driven-dev/svelte-todo/` | `sdd-go-fractals.yaml`、`sdd-svelte-todo.yaml` | 候选——删除前验证（其中包含测试套件通过的真实断言） |
| `tests/claude-code/test-document-review-system.sh` | `spec-reviewer-catches-planted-flaws.yaml` | 候选——删除前验证 |
| `tests/claude-code/test-requesting-code-review.sh` | `code-review-catches-planted-bugs.yaml` | 候选——删除前验证 |
| `tests/claude-code/test-subagent-driven-development-integration.sh` | `sdd-rejects-extra-features.yaml`（YAGNI 子集） | **部分**——bash 测试还断言至少 3 次提交、`npm test` 通过，并运行 `analyze-token-usage.py`。Drill 场景断言禁止的导出及审查者关卡。两者大多不重叠——几乎肯定应**保留并扩展 drill 场景**。 |
| `tests/claude-code/test-subagent-driven-development.sh` | 元/文档测试（让代理*描述* SDD）；没有 drill 场景覆盖描述测试 | **保留**，除非增加 drill 场景 |
| `tests/claude-code/test-worktree-native-preference.sh` | `worktree-creation-under-pressure.yaml` | 候选——删除前验证 |
| `tests/claude-code/test-helpers.sh`、`run-skill-tests.sh`、`analyze-token-usage.py` | 不适用（工具，并非测试） | **保留**——库/工具 |

## 验证协议（子代理关卡）

实施计划中的每项变更，提交前都由独立子代理交叉检查。

| 变更类别 | 子代理验证 |
|----------------|----------------------|
| 每次删除 bash 测试 | 派发子代理，提供：(a) bash 测试文件内容，(b) 候选 drill 场景 YAML，(c) 提示词：*“列出 bash 测试的每项断言。列出 drill 场景中的每个 verify 条目。为每项 bash 断言找到匹配的 drill 检查，否则报告为未匹配。输出逐断言表格。”* 子代理输出就是关卡——只有每项 bash 断言均有匹配才能删除。 |
| 初次复制 `evals/` | 子代理验证：(a) 迁移提交信息记录所复制 drill 的 SHA，保证来源可审计；(b) 每个文件的**逐文件 SHA-256 校验和**与 drill 仓库一致（不只比较文件数量）；(c) `evals/` 中不存在排除路径（`.git/`、`.venv/`、`results/`、`.env`、`__pycache__/`、`*.egg-info/`、任何 `.private-journal/`）；(d) 全部后端 YAML 引用的路径在迁移后存在；(e) `pyproject.toml`、`uv.lock`、`.gitignore` 完整。 |
| Drill 自身 pytest 套件 | 路径默认值修改后，子代理运行 `cd evals && uv run pytest`。Drill 在 `evals/tests/` 自带 pytest 套件，其中 `test_backend.py` 测试 `SUPERPOWERS_ROOT` 环境变量行为——这些测试必须更新为与辅助函数一致并继续通过。 |
| 删除后清理引用 | 子代理在整个 superpowers 目录树（排除 `node_modules/`、`.venv/` 和 `evals/`）搜索已删除 bash 测试路径的引用。搜索目标：`docs/`、`docs/superpowers/plans/`、`RELEASE-NOTES.md`、`CLAUDE.md`、`GEMINI.md`、`AGENTS.md`、`README.md`、`.github/`、`scripts/`、`.opencode/INSTALL.md`、`.codex-plugin/INSTALL.md`、`lefthook.yml`。每个命中要么更新，要么揭示遗漏的依赖。 |
| 修改路径默认值（`SUPERPOWERS_ROOT` 默认值） | 子代理在路径修改后至少运行一个成本低的 drill 场景（例如 `triggering-test-driven-development`），确认仍通过。是真实验证，不只是代码审查。 |
| 最终 PR 前对抗审查 | 并行运行两个子代理，使用“找到最多真实问题者得 5 分”的框架——与跨平台 PR 使用的协议相同。验证源码和行为。 |

每项子代理任务在实施计划中各有一个条目，明确输入和通过标准。相关提交信息概述子代理输出（“子代理验证：……”），使过程可审计。

## 具体路径/配置修改

**撰写本规格前已验证。** `drill/cli.py` 定义 `PROJECT_ROOT = Path(__file__).parent.parent`。迁移后，`cli.py` 位于 `evals/drill/cli.py`，因此 `PROJECT_ROOT` 解析为 `evals/`，`PROJECT_ROOT.parent` 解析为 superpowers 仓库根目录。这就是 `SUPERPOWERS_ROOT` 应采用的默认值。

**YAML 替换审计。** 只有四个 `claude*.yaml` 后端配置会将 `${SUPERPOWERS_ROOT}` 插入 `args`（用于 `--plugin-dir` 标志）；`codex.yaml` 与 `gemini.yaml` 只在 `required_env` 中列出 `SUPERPOWERS_ROOT`（由运行前/后钩子中 `engine.py:233` / `setup.py:25` 的 `os.environ["SUPERPOWERS_ROOT"]` 查找使用）。辅助函数修改 `os.environ` 能覆盖这两条代码路径。

| 文件 | 当前 | 修改后 |
|------|---------|-------|
| `drill/cli.py` | 模块导入时执行 `load_dotenv(PROJECT_ROOT / ".env")`；未处理 `SUPERPOWERS_ROOT` | `load_dotenv` 后调用新辅助函数 `_set_superpowers_root_default()`，仅在变量尚未设置时把 `os.environ["SUPERPOWERS_ROOT"]` 设为 `str(PROJECT_ROOT.parent)`。顺序：`load_dotenv` → 设置默认值 → click 组定义。 |
| `drill/engine.py:233`、`drill/setup.py:25` | 直接访问 `os.environ["SUPERPOWERS_ROOT"]`（未设置时出现 KeyError） | 不变。CLI 启动钩子保证 engine/setup 执行时环境变量已设置。 |
| `backends/claude*.yaml`（5 个文件） | 在 `args` 中为 `--plugin-dir` 替换 `${SUPERPOWERS_ROOT}` | 不变。YAML 替换在后端加载时读取 `os.environ`，发生在 CLI 启动之后。 |
| `backends/codex.yaml`、`backends/gemini.yaml` | 仅在 `required_env` 中列出 `SUPERPOWERS_ROOT` | 从 `required_env` 删除（辅助函数负责提供）。`claude*.yaml` 保留 `required_env` 以向后兼容（环境变量可用于覆盖）。 |
| `evals/tests/test_backend.py` | 测试断言 `SUPERPOWERS_ROOT` 存在于 `required_env` 列表，并测试路径解析 | 更新测试以符合新契约：辅助函数提供默认值、环境覆盖仍有效、codex/gemini 不再要求 `required_env`。 |
| `evals/README.md` | “export SUPERPOWERS_ROOT=/path/to/superpowers” | 删除 export 行；说明该环境变量自动默认为 `evals/` 的父目录；说明唯一必需的设置是 `ANTHROPIC_API_KEY`（或 `OPENAI_API_KEY` / Gemini 身份验证）。 |
| `evals/CLAUDE.md` | 相同 | 相同 |
| `evals/.gitignore` | drill 现有模式（`results/`、`.venv/`、`__pycache__/`、`.env`、`*.pyc`、`*.egg-info/`、`dist/`、`build/`、`.claude/`） | 原样复制。模式相对于文件位置，因此在 `evals/` 下正确生效。 |
| `evals/lefthook.yml` | drill 自带的 `lefthook.yml` 定义 `pre-commit: uv run ruff check && uv run ty check` | 移至 `evals/lefthook.yml`。可以 (a) 在 superpowers 根目录安装 lefthook 并转交给 `evals/lefthook.yml`，或 (b) 记录贡献者应手动运行 `cd evals && lefthook run pre-commit`。**实施决定：为简单起见选择 (b)**——不改变 superpowers 顶层工作流程。 |

`.env` 位置：保留 `evals/.env`（已 gitignore）。贡献者从此处 source，或在 shell 环境设置 `ANTHROPIC_API_KEY`。

**需小幅增加的顶层 superpowers 文件：**

- `superpowers/.gitignore`：添加 `evals/results/`、`evals/.venv/`、`evals/.env`（双保险；evals/.gitignore 已本地覆盖）。

- `superpowers/CLAUDE.md`：增加一行指针“评估 harness 位于 `evals/`，见 `evals/README.md`”，便于代理发现。

- `superpowers/docs/testing.md`：拆成“## 插件测试”（现有 tests/ 内容，删除测试引用已裁剪）和“## 技能行为评估”（一段摘要及指向 `evals/`）。

- `superpowers/README.md`：在贡献节增加一行，指向 `evals/` 进行技能行为测试。

## 迁移顺序

每步独立提交（或少量提交）。第 2 步是最大提交（逐字复制 drill）；后续小而原子。

```
1. 从 `dev` 建分支（f/evals-lift）

2. 将 drill 仓库复制到 evals/（单次提交，便于回退）
   ├─ 复制时记录 drill SHA → 提交消息
   ├─ 使用 `rsync -a --exclude=.git --exclude=.venv --exclude=results
   │  --exclude=.env --exclude=__pycache__ --exclude='*.egg-info'
   │  --exclude=.private-journal /path/to/drill/ evals/`
   │  （选用 rsync 而非 `cp -r` 以明确排除；用
   │  `find evals -name '.git' -type d` 确认无返回）
   ├─ 子代理关卡：每个未排除文件的 SHA-256 与 drill 一致；排除路径不在 evals/
   └─ 冒烟检查：`cd evals && uv sync` 成功（只证明安装，不是行为测试）

3. 更新默认路径
   ├─ 在 drill/cli.py 添加 _set_superpowers_root_default() 辅助函数
   ├─ 在 load_dotenv 后、click 组定义前接入
   ├─ 更新 evals/README.md 和 evals/CLAUDE.md（删除 SUPERPOWERS_ROOT 安装步骤）
   ├─ 从 codex.yaml/gemini.yaml 的 required_env 删除 SUPERPOWERS_ROOT
   │  （claude*.yaml 保留作为覆盖）
   └─ 更新 evals/tests/test_backend.py 匹配新契约

4. 从新位置验证（两项检查）
   ├─ 运行 drill pytest：`cd evals && uv run pytest`，必须通过
   └─ 运行低成本场景：`cd evals && uv run drill run
      triggering-test-driven-development -b claude`，必须通过。
      这是真实行为验证，不只是代码审查。

5. Bash 测试删除阶段：逐文件并设子代理关卡
   对候选删除列表每文件：
   a. 子代理比较 bash 断言与 drill 场景验证块
   b. 通过标准：每条 bash 断言有对应 drill 检查
   c. 通过则删文件（每文件或连贯组一次提交）
   d. 失败则扩展 drill 场景（独立提交并验证），或保留测试（不提交）

6. 清理旧引用
   ├─ 子代理在 superpowers 树中（排除 node_modules/、.venv/、evals/）grep 被删路径
   ├─ 搜索 docs/、docs/superpowers/plans/、RELEASE-NOTES.md、CLAUDE.md、
   │  GEMINI.md、AGENTS.md、README.md、.github/、scripts/、.opencode/INSTALL.md、
   │  .codex-plugin/INSTALL.md、lefthook.yml
   ├─ 更新活跃引用（如 docs/testing.md、README 安装说明）
   └─ 历史文档中的引用保留，并简短注明“测试已移除；行为由 drill 场景 X 覆盖”，不重写

7. 顶层文档
   ├─ 拆分 docs/testing.md
   ├─ CLAUDE.md 指针
   └─ README.md 贡献节

8. 重跑冒烟检查（回归关卡）
   ├─ `cd evals && uv run pytest`
   └─ `cd evals && uv run drill run triggering-test-driven-development -b claude`

9. 最终对抗审查
   └─ 两个并行子代理查看完整差异，采用“找到最多合理问题者得 5 分”框架

10. 推送分支并向 dev 开 PR
    └─ PR 描述包含固定 drill SHA、合并后归档 action item、每个删除文件的覆盖凭据
```

## 验证（实施后）

实施计划必须显示：

- 第 2 步后 `evals/` 包含全部未排除 drill 源文件（子代理对 `obra/drill@<recorded-sha>` 做**逐文件 SHA-256 差异检查**）。

- `evals/` 不包含排除路径（`.git/`、`.venv/`、`results/`、`.env`、`__pycache__/`、`*.egg-info/`、`.private-journal/`）。

- 第 2 步提交消息记录 drill 源 SHA。

- 未设置 `SUPERPOWERS_ROOT` 时 `cd evals && uv sync` 成功。

- `cd evals && uv run pytest`（drill 自身测试）通过。

- `cd evals && uv run drill list` 的场景数与记录 SHA 的独立 drill 仓库相同。

- `cd evals && uv run drill run triggering-test-driven-development -b claude` 通过（证明路径默认端到端有效）。

- 每个删除的 bash 测试在提交消息中有验证表，每条断言映射到 drill 检查。

- 活跃 superpowers 文档中搜索被删路径零命中（第 6 步后）；`docs/superpowers/plans/*.md` 和 `RELEASE-NOTES.md` 历史引用只注明不重写。

- `docs/testing.md` 同时含“插件测试”和“技能行为评估”。

- drill 仓库历史不变；`obra/drill` 不受本 PR 影响。

- PR 描述列出合并后归档 `obra/drill` 的 action item。

## 未决问题

无。澄清决定均已作出：

| 问题 | 决定 |
|----------|----------|
| drill 在 superpowers 中位于何处？ | `evals/`（改名自 drill）；独立仓库另步归档 |
| 冗余 bash 测试如何处理？ | 逐文件删除，子代理验证覆盖；默认保留 |
| 场景布局？ | 集中于 `evals/scenarios/` |
| Python 工具链位置？ | 自含于 `evals/` |
| CI 集成？ | 本 PR 仅手动；记录未来路径 |
| 迁移机制？ | 普通复制；drill 历史保留在归档仓库 |
| 内部 Python 包名？ | 保留 `drill`（目录为 `evals/`） |
| 分支策略？ | 从 `dev` 独立建分支（不叠在 `f/cross-platform`） |
