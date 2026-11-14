---
name: setup-pstack
description: 配置 pstack 按角色使用的模型及推理预算。检测可用模型并写入始终应用的规则，覆盖技能默认值。用于 /setup-pstack、“配置 pstack 模型”“pstack 预算”或修改模型选择。
---

# 设置 pstack

写入 `~/.cursor/rules/pstack-models.mdc`，一条始终应用的规则，按角色设置 pstack 模型。

## 步骤

### 1. 检测可用模型

枚举本会话可传给 `Task` 子智能体的模型 slug，这是可靠来源。Cursor 也提供列出用户可用模型的 API／CLI 时优先使用以求完整。无法检测时请用户粘贴可用 slug。绝不写入未确认可用的真实 slug。别名 `inherit-parent` 和 `auto` 始终有效，即使无法检测。

### 2. 加载当前状态

默认角色到模型映射见步骤 5。`~/.cursor/rules/pstack-models.mdc` 已存在时读取，把 `# budget` 行和角色值视为当前选择；否则从默认开始。步骤 5 没有的角色（如 `how critics`）已退役，删除。

### 3. 预算、映射和确认

**(a) 询问预算。** 优先 AskQuestion。提供四个准确标签，规则记录当前预算时说明。没有规则时说明 `large` 匹配技能默认。

- `unlimited — max reasoning`（无限制，最高推理）

- `large — xhigh reasoning`（大，超高推理）

- `medium — high reasoning`（中，高推理）

- `small — medium reasoning`（小，中推理）

**(b) 应用。** 从默认构建表格，重跑时保留按家族、列表或别名修改的角色。四个预算将每个真实 slug（含面板项）的努力 token 设为 `max`、`xhigh`、`high`、`medium`。努力 token 是阶梯 `max` > `xhigh` > `high` > `medium` > `low` 的最后一个，或尾随 `fast` 前那个。结果不是已检测 slug 时，用同家族检测到且不高于目标的最高努力；否则标记为需选择。`inherit-parent` 和 `auto` 不变。`unlimited` 将 `claude-opus-5-5-xhigh` 变成 `claude-opus-5-5-max`；Grok 最高 `xhigh`，所以保留 `grok-4.7-xhigh-fast`。`large` 保持两者。`small` 变成 `claude-opus-5-5-medium` 和 `grok-4.7-medium-fast`。，相关标识为 `inherit-parent` `auto` `unlimited` `unlimited` `large` `medium` `small` `xhigh`。

**(c) 展示角色并确认。** 列出每个角色及模型，未检测真实 slug 标为需选择；列出删除行。询问接受或修改角色，选项为检测模型加 `inherit-parent`、`auto`（均在父聊天模型运行）。面板角色值为列表，每项一个子智能体，列表长度决定并发数。`arena cross-judge pool` 是列表但 Arena 只运行一个裁判，按顺序尝试父模型外的家族；别名值不作裁判。`swarm workers` 是每个工作者默认模型，除非竞赛按分支指定。，相关标识为 `inherit-parent` `auto`。

### 4. 验证

每个真实 slug 必须已检测。`inherit-parent` 和 `auto` 始终通过。不可用则停止重问。

### 5. 写规则

写入 `~/.cursor/rules/pstack-models.mdc`，`alwaysApply: true`，含预算和目标的 `# budget` 行及每角色一行，使用 poteto-mode 标签。覆盖整个文件以保持幂等。

```
+---
+description: pstack 分角色模型选择（覆盖技能默认值）
+alwaysApply: true
+---
+# pstack 模型配置。每角色一行，删除行恢复技能默认。
+# `inherit-parent` 或 `auto`：角色在父聊天模型运行（省略 Task model）。
+# budget: large (xhigh)
+feature, refactoring: grok-4.7-xhigh-fast
+bug-fix: grok-4.7-xhigh-fast
+perf-issue: grok-4.7-xhigh-fast
+hillclimb: grok-4.7-xhigh-fast
+judgment and prose: claude-opus-5-5-xhigh
+hardest tasks: claude-opus-5-5-xhigh
+how explorer: grok-4.7-xhigh-fast
+how explainer: claude-opus-5-5-xhigh
+why investigators: grok-4.7-xhigh-fast
+why synthesizer: claude-opus-5-5-xhigh
+reflect tooling: grok-4.7-xhigh-fast
+reflect judgment, divergent, synthesizer: claude-opus-5-5-xhigh
+arena runners: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
+arena cross-judge pool: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
+swarm workers: grok-4.7-xhigh-fast
+architect runners: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
+interrogate reviewers: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
+

# 角色配置使用字段：`model`
```

### 6. 确认

告诉用户规则已写，适用于新会话；重跑会更新。

### 7. 提供验证技能（可选）

检查项目是否可驱动真实应用取证。没有时询问一次是否用 `/create-verification-skill` 生成。同意则调用；不同意则继续。，相关标识为 `verify-*`。

### 8. 提供形式验证技能（可选）

检查项目是否有形式验证技能（模型检查器、证明或验证器）。没有时询问一次是否用 `/create-formal-verification-skill` 生成。同意则调用；不同意则继续。
