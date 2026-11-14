# Claude Code 工具说明

Claude Code 是参考平台：技能使用其词汇（子代理派发用 `Agent`、待办、`Skill`）。本说明介绍 Claude Code 能让计划比技能默认形态更便宜运行的一处。它由人类搭档选择启用，不改变技能要求。

## 子代理驱动开发的低成本编排

控制器会话是 superpowers:subagent-driven-development 最昂贵的位置：它读取每个派发结果和报告，且通常运行会话最强模型。Claude Code 支持嵌套子代理（默认主对话下三层；`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` 可调整），整个循环可下沉一层。

人类搭档要求这样做，或表示会话模型用于协调太贵时，将计划和端到端使用 superpowers:subagent-driven-development 的指令交给一个中层模型编排器子代理。编排器按技能模型选择自行派发实现者和审查者；工作区与台账在磁盘，额外层不丢信息。最终消息须逐字携带“我作出的裁定”列表，该列表将决定传达给人类搭档，你只转交，不概括。

只对整个计划使用。为单个任务嵌套派发没有收益，还多占一席。
