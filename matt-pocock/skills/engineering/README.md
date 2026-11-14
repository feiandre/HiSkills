# 工程

我日常编码使用的技能。

## 用户调用

仅在你输入时可调用（Claude Code：`disable-model-invocation: true`；Codex：`agents/openai.yaml` 中 `policy.allow_implicit_invocation: false`）。

- **[ask-matt](./ask-matt/SKILL.md)**：询问哪项技能或流程适合当前情况。为本仓库用户调用技能提供路由。

- **[grill-with-docs](./grill-with-docs/SKILL.md)**：深入追问会话，同时构建项目领域模型，厘清术语并即时更新 `GLOSSARY.md` 与 ADR。

- **[triage](./triage/SKILL.md)**：通过分诊角色状态机推进问题。

- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)**：扫描代码库中的深化机会，以可视化 HTML 报告展示，再针对你选择的机会深入追问。

- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)**：为工程技能配置本仓库（问题跟踪器、分诊标签、领域文档布局）。每仓库运行一次。

- **[to-spec](./to-spec/SKILL.md)**：将当前对话转成规格，发布到问题跟踪器。

- **[to-tickets](./to-tickets/SKILL.md)**：将任何计划、规格或对话拆为一组曳光弹工单，各自声明阻塞边；可写成本地文件文本，也可用真实跟踪器中的原生阻塞链接。

- **[implement](./implement/SKILL.md)**：实现规格或工单集合描述的工作，在预先约定的接缝处驱动 `/tdd`，提交前以 `/code-review` 收尾。

- **[implement-spec](./implement-spec/SKILL.md)**：在一个集成分支实现整份规格。将工单作为任务图，沿就绪前沿运行实现者子代理以最大并发，再以 `/code-review` 收尾。

- **[wayfinder](./wayfinder/SKILL.md)**：把超过一次代理会话容量的大块工作规划成问题跟踪器上的共享决策工单地图，逐一解决，直到通往目的地的路线清晰。

- **[retro](./retro/SKILL.md)**：会话结束后建议改进编码代理环境（导航、自动检查、编码标准、引导文件、工具），严重程度最高的优先。

## 模型调用

模型或用户均可调用（丰富触发措辞，使模型能主动使用）。

- **[prototype](./prototype/SKILL.md)**：构建一次性原型回答设计问题：状态／逻辑用一个可分享 HTML 文件，或提供几种可切换的 UI 变体。

- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)**：针对疑难缺陷和性能回归的严谨诊断循环：建立会因该缺陷失败的反馈循环 → 最小化 → 假设 → 插桩 → 修复 → 回归测试。

- **[research](./research/SKILL.md)**：以高可信一手来源调查问题，将附引用的发现写成仓库内 Markdown 文件，以后台代理运行。

- **[tdd](./tdd/SKILL.md)**：以红绿重构循环实施测试驱动开发。一次一个纵向切片构建功能或修复缺陷。

- **[domain-modeling](./domain-modeling/SKILL.md)**：通过质疑术语、用场景压力测试、即时更新 `GLOSSARY.md` 与 ADR，主动构建并完善项目领域模型。

- **[codebase-design](./codebase-design/SKILL.md)**：设计深模块的共同规范与词汇：小接口、清楚的接缝、可通过接口测试。

- **[code-review](./code-review/SKILL.md)**：对固定点以来的差异作双轴审查：**标准**（是否遵循仓库编码标准及 Fowler 坏味道基线）与**规格**（是否忠实实现原问题／规格），以并行子代理运行。

- **[pr](./pr/SKILL.md)**：拉取请求正文的形态：摘要用能清楚说明变更的最小可视化、前后对照证明有效、合并风险判断（单向门或双向门，以及影响范围）。

- **[wizard](./wizard/SKILL.md)**：生成交互式 bash 向导，逐步引导人类执行只有其本人能做的事：配置基础设施、凭据或 CI 秘密、浏览陌生第三方后台、执行一次性迁移或切换。
