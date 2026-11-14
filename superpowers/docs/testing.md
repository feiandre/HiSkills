# 测试 Superpowers

Superpowers 有两类不同测试，各在自己的目录：

- **`tests/`**：插件的非 LLM 代码是否工作？用 Bash + Node + Python 集成测试 brainstorm-server JS、OpenCode 插件加载、codex-plugin 同步及分析工具。

- **`evals/`**：代理在真实 LLM 会话中行为是否正确？Python harness 驱动 Claude Code / Codex / Gemini CLI 的真实 tmux 会话，由 LLM 行动者与验证者判断技能合规性。

## 插件测试

位于 `tests/`。目前包括：

- `tests/brainstorm-server/`：brainstorm server JS 的 Node 测试套件。

- `tests/opencode/`：OpenCode 插件加载、bootstrap 缓存与工具注册的 Bash 测试。

- `tests/codex-plugin-sync/`：Bash 同步验证。

- `tests/kimi/`：Kimi 插件清单接线的 Bash/Python 检查。

- `tests/claude-code/test-helpers.sh`、`analyze-token-usage.py`：剩余 Bash 测试使用的工具。

- `tests/claude-code/test-subagent-driven-development.sh`：代理能否描述 SDD 的测试（无 quorum 对应项；测试描述回忆，行为不参与）。

- `tests/claude-code/test-subagent-driven-development-integration.sh`：扩展 SDD 集成与 token 分析（quorum 覆盖 YAGNI 子集；Bash 还断言提交数、Claude Code 任务跟踪与 token 遥测）。

- `tests/claude-code/test-worktree-native-preference.sh`：worktree 技能的 RED-GREEN-REFACTOR 验证（quorum 覆盖 PRESSURE 阶段；Bash 还覆盖 RED/GREEN 基线）。

- `tests/explicit-skill-requests/`：quorum 未覆盖的 Haiku 专项、多轮及技能名提示测试。

- `tests/diagnosing-superpowers/test-skill-structure.sh`：diagnosing-superpowers 的结构检查（前置元数据、引用文件、泄漏扫描、字数预算）；行为场景评估记录由维护者保存在仓库外。

通过相关目录的 `run-*.sh` 或 `npm test` 运行插件测试。

## 技能行为评估

位于 `evals/`（[superpowers-evals](https://github.com/prime-radiant-inc/superpowers-evals/) 评估实验室，曾任 Drill）。Quorum 是系统的 harness CLI：通过 Gauntlet QA 代理驱动真实编码代理 CLI，并按场景验收标准及确定性后置检查评分。场景位于 `evals/scenarios/<name>/`。安装、容器运行时和安全模型见 `evals/README.md`。快速开始（本地紧急运行）：

```bash
cd evals
bun install
export SUPERPOWERS_ROOT=/path/to/superpowers
bun run quorum run scenarios/triggering-test-driven-development --coding-agent claude
bun run quorum show <run-dir>
```

Quorum 场景很慢（每个 3—30 分钟以上），并在宽松模式下运行真实 LLM；先读 `evals/README.md` 的 Live Eval Risk 节。只有静态关卡（`bun run check`、`bun run quorum check`）适合公共 CI；后续仍应分层：PR 上跑静态关卡，每夜及按需运行实时扫描。
