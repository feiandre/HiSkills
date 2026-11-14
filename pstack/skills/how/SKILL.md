---
name: how
description: "用于‘X 如何工作’、修改代码前的代码走查，以及放置/所有权/分层问题（‘这个应该放哪’、‘哪个包拥有它’、‘这是正确层级吗’）。解释子系统架构、运行时流程和入门心智模型。动机请用 why。"
disable-model-invocation: true
---

# How（如何）

探索代码库以回答“X 如何工作？”问题。产出资深工程师了解某子系统层次的架构解释，足以建立可用心智模型，又不会冗长到像带注释的源代码。

每次生成都是带 `subagent_type: generalPurpose` 与 `readonly: true` 的 Task 子代理。探索者使用 `pstack-models.mdc` 规则中的 `how explorer` 行（默认 `grok-4.7-xhigh-fast`），每位解释者使用 `how explainer` 行（默认 `claude-opus-5-5-xhigh`）。将 `model` 设为该行值；规则或行缺失则用默认值。值为 `auto` 或 `inherit-parent` 时不要设置 `model`。若 Task 工具拒绝 slug，使用默认值并说明。若拒绝默认值，则从错误消息使用同系列最接近有效 slug。按 **poteto-mode** 技能的 Subagents 部分为工作选择每个子代理的推理级别及快速/标准速度。

## 1. 评估复杂度

若范围含糊，说明解释并探索。用户可纠正。

- **简单**（单模块、小型工具，或“函数 X 如何工作”等窄问题）：不使用探索者。生成一位一趟完成探索和解释的解释者，基于 `references/explainer-prompt.md`，不含探索者发现部分。进入步骤 4。

- **复杂**（跨多个文件或服务的子系统、横切功能、完整架构概览）：进入步骤 2。

拿不准时选择简单路径。

## 2. 探索（仅复杂情形）

将问题分解成 2 到 4 个角度，每个是子系统的独立切片。在一条消息生成所有探索者，每位携带 `references/explorer-prompt.md` 及填入的角度。

## 3. 综合（仅复杂情形）

所有探索者返回后，生成一位解释者，携带 `references/explainer-prompt.md` 并填入每位探索者的发现。

## 4. 呈现

呈现解释者输出。可为清晰稍作编辑，或从对话添加上下文。不要实质改写。

## 输出格式

解释使用 `references/explainer-prompt.md` 定义的各部分，删除不适用项：概览、关键概念、如何工作、内容所在位置、陷阱。
