---
name: reflect
description: 对活动记录并行启动三名审查子智能体，提炼经验并路由为现有技能的具体编辑。用户说 reflect 时使用。
disable-model-invocation: true
---

# 反思

从当前对话挖掘持久经验，再路由为技能编辑。

用户说“reflect”或“/reflect”时调用。对话平凡、偏题或已被正确技能覆盖时跳过；一次性事项不是经验。

## 1. 定位活动记录

在系统提示指定的 `agent-transcripts/` 查找本对话，不跨 `~/.cursor/projects/*/` 读取无关项目。

```bash
ls -t <agent-transcripts>/*.jsonl <agent-transcripts>/*/*.jsonl <agent-transcripts>/*/subagents/*.jsonl 2>/dev/null | head -10
```

这涵盖旧扁平布局 `<id>.jsonl`、当前嵌套布局 `<id>/<id>.jsonl` 和子代理布局 `<parent>/subagents/<child>.jsonl`。对每个候选读取首行 JSONL，选择 `message.content[0].text` 包含会话开场用户提示的文件；若都不匹配，则改为传入会话的精简摘要。

## 2. 并行启动三名审查员

一条消息、三个 `Task` 调用，`subagent_type: generalPurpose`，代理模式（`readonly: false`）。审查员需要 MCP 查票、聊天和可观测性 trace。

每个审查者和合成器使用 `pstack-models.mdc` 规则中的角色行及默认值；将 `model` 设为该行的值，规则或行缺失时则用默认值。若值为 `auto` 或 `inherit-parent`，保持 `model` 未设置。Task 工具拒绝某个 slug 时使用默认值并说明；连默认值也被拒绝时，从其错误信息中选择同系列最接近的有效 slug。按 **poteto-mode** 技能的子代理一节，为每个子代理选择推理级别及快速或标准速度。

| 视角 | 角色行 | 默认模型 | 提示模板 |
|---|---|---|---|
| 判断 | `reflect judgment, divergent, synthesizer` | `claude-opus-5-5-xhigh` | `references/judgment-reviewer.md` |
| 工具 | `reflect tooling` | `grok-4.7-xhigh-fast` | `references/tooling-reviewer.md` |
| 发散 | `reflect judgment, divergent, synthesizer` | `claude-opus-5-5-xhigh` | `references/divergent-reviewer.md` `model` |

逐字传入每个模板，并在标记处替换记录路径或摘要；审查者在 `Task` 响应正文中返回发现。

## 3. 合成

发起一次 `Task` 调用，设置 `subagent_type: generalPurpose`，`model` 取自 `reflect judgment, divergent, synthesizer` 行（默认 `claude-opus-5-5-xhigh`），代理模式为 `readonly: false`。它通过 MCP 抽查引用，而只读模式会移除 MCP。逐字传入 `references/synthesizer.md`，并在标记处内联每个审查者的完整输出；它返回接受、拒绝或待办列表。

## 4. 结构性执行检查

接受项若能由 lint、脚本、元数据标志或运行时检查更可靠执行，移到待办（**encode-lessons-in-structure** 技能）。

## 5. 应用

展示完整接受／拒绝／待办输出，应用接受编辑前等待明确批准。用户选择子集并可改路由。绝不自动应用。

立即把每个待办项提交团队 devex 或 backlog 跟踪器；只有接受项等待批准。

绝不编辑 `plugins/cache/` 下技能。批准前显示目标 `.cursor/skills/<skill>/` 或 `~/.cursor/skills/<skill>/`；批准后复制到该处编辑副本。绝不创建 PR 或推送。

严格遵循每行路由：

- 平凡现有技能编辑（一行条目、收紧句子、修过时事实）由父代理直接做。

- 实质编辑（新章节、新模式表、超过约 10 行）交给内建 `create-skill` 的草稿／测试／迭代循环。

- `tune description: <skill path>` 交给 `create-skill` 运行描述优化循环。

- `new skill via create-skill: <kebab-name>` 交给 `create-skill`，不要临时发明形态。

环境有 SKILL.md 验证器时，对所有触碰技能运行后再宣布完成。

## 6. 向用户总结

无前言短清单：

- 已应用编辑：`<skill path>`，每项一行变化。

- 新建技能：`<skill path>`，每项一行（少见）。

- 已提交待办：`<issue title>`（`<tags>`），每项一行。

- 丢弃项：每个拒绝发现一行并附合成器理由。
