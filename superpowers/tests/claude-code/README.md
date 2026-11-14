# Claude Code 技能测试

使用 Claude Code CLI 对 superpowers 技能进行自动化测试。

## 概述

此测试套件验证技能正确加载，且 Claude 按要求遵循它们。测试以无头模式（`claude -p`）调用 Claude Code 并验证行为。

## 要求

- 已安装 Claude Code CLI 且位于 PATH（`claude --version` 应可运行）

- 已安装本地 superpowers 插件（安装见主 README）

## 运行测试

### 运行全部快速测试（推荐）：

```bash
./run-skill-tests.sh
```

### 运行集成测试（较慢，10—30 分钟）：

```bash
./run-skill-tests.sh --integration
```

### 运行指定测试：

```bash
./run-skill-tests.sh --test test-subagent-driven-development.sh
```

### 以详细输出运行：

```bash
./run-skill-tests.sh --verbose
```

### 设置自定义超时：

```bash
./run-skill-tests.sh --timeout 1800  # 集成测试 30 分钟
```

## 测试结构

### test-helpers.sh 测试辅助脚本

技能测试常用函数：

- `run_claude "prompt" [timeout]`——用提示词运行 Claude

- `assert_contains output pattern name`——验证模式存在

- `assert_not_contains output pattern name`——验证模式不存在

- `assert_count output pattern count name`——验证确切次数

- `assert_order output pattern_a pattern_b name`——验证顺序

- `create_test_project`——创建临时测试目录

- `create_test_plan project_dir`——创建示例计划文件

### 测试文件

每个测试文件：

1. 引入 `test-helpers.sh`

2. 以特定提示词运行 Claude Code

3. 使用断言验证预期行为

4. 成功返回 0，失败返回非零

## 示例测试

```bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/test-helpers.sh"

echo "=== 测试：我的技能 ==="
output=$(run_claude "What does the my-skill skill do?" 30)
assert_contains "$output" "expected behavior" "技能描述行为"

echo "=== 全部测试通过 ==="
```

## 当前测试

### 快速测试（默认运行）

#### test-subagent-driven-development.sh 测试文件

测试技能内容与要求（约 2 分钟）：

- 技能加载与可访问性

- 工作流顺序（代码质量前先作规格符合性审查）

- 记录自审要求

- 记录计划读取效率

- 记录规格符合性审查者应保持怀疑

- 记录审查循环

- 记录任务上下文提供方式

### 集成测试（使用 `--integration` 标志）

#### test-subagent-driven-development-integration.sh 测试文件

完整工作流执行测试（约 10—30 分钟）：

- 创建带 Node.js 设置的真实测试项目

- 创建含 2 个任务的实施计划

- 使用 subagent-driven-development 执行计划

- 验证实际行为：

- 开始读取一次计划（不是每任务读取）

- 子代理提示词提供完整任务文本

- 子代理报告前执行自审

- 规格符合性审查先于代码质量

- 规格审查者独立阅读代码

- 产出了可工作实现

- 测试通过

- 创建了正确的 git 提交

**它测试什么：**

- 工作流确实可端到端运行

- 我们的改进确实生效

- 子代理正确遵循技能

- 最终代码可运行且经过测试

#### test-worktree-native-preference.sh 测试文件

针对 using-git-worktrees 技能的红绿重构验证（约 5 分钟）：

- 红：技能没有步骤 1a——代理应使用 `git worktree add`

- 绿：技能有步骤 1a——代理应使用原生 EnterWorktree 工具

- 压力：与绿色相同，但以紧急措辞且已有 `.worktrees/`

- 演练场景 `worktree-creation-under-pressure.yaml` 只覆盖压力阶段

## 添加新测试

1. 创建 `test-<skill-name>.sh`

2. 引入 test-helpers.sh

3. 用 `run_claude` 与断言编写测试

4. 加入 `run-skill-tests.sh` 测试列表

5. 使其可执行：`chmod +x test-<skill-name>.sh`

## 超时注意事项

- 默认每项测试 5 分钟

- Claude Code 可能耗时响应

- 需要时用 `--timeout` 调整

- 测试应聚焦，避免长时间运行

## 调试失败测试

使用 `--verbose` 可查看完整 Claude 输出：

```bash
./run-skill-tests.sh --verbose --test test-subagent-driven-development.sh
```

非详细模式下只显示失败输出。

## CI/CD 集成

在 CI 中运行：

```bash
./run-skill-tests.sh --timeout 900
```

## 说明

- 测试验证技能*指令*，不验证完整执行

- 完整工作流测试会非常慢

- 重点验证关键技能要求

- 测试应具有确定性

- 避免测试实现细节
