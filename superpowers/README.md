# Superpowers 超能力

Superpowers 是供编码代理使用的完整软件开发方法论，建立在一套可组合技能及确保代理使用这些技能的初始指令之上。

## 目录

- [工作原理](#how-it-works)
- [商业服务](#commercial-services)
- [开始使用](#installation)
- [基本工作流程](#the-basic-workflow)
- [出现问题时](#when-something-goes-wrong)
- [社区](#community)
- [包含内容](#whats-inside)
- [理念](#philosophy)
- [贡献](#contributing)
- [更新](#updating)
- [许可证](#license)
- [可视化辅助遥测](#visual-companion-telemetry)

## 工作原理

从启动编码代理的那一刻开始，一旦发现你在构建某样东西，它*不会*立刻开始尝试写代码，而是退一步问你真正想做什么。

从对话中梳理出规格后，它会分成足够短、便于实际阅读和理解的部分展示给你。

设计获你批准后，代理制定实施计划，清楚到一个充满热情、品位欠佳、缺乏判断和项目上下文、又不爱测试的初级工程师也能照着做。它强调真正的红/绿 TDD、YAGNI（你不会需要它）和 DRY（不要重复自己）。

接着，你一声“开始”，它便启动*子代理驱动开发*流程，让代理逐个处理工程任务，检查和审查成果，持续推进。代理一次自主工作数小时而不偏离共同制定的计划，并不罕见。

还有许多其他内容，但这就是系统的核心。技能自动触发，你无需特殊操作。你的编码代理就这样拥有了 Superpowers。

## 商业服务

如果你在企业中使用 Superpowers，需要商业支持、额外工具或支出管理，请随时联系 sales@primeradiant.com。

## 基本工作流程

1. **brainstorming** - 在构建任何东西之前激活。通过提问让你描述真实需求与原因，再复述理解供你纠正。小改动在聊天中达成一致；项目会形成构建者可据此规划的书面设计文档。
2. **using-git-worktrees** - 设计批准后激活。在新分支创建隔离工作区，运行项目设置，验证干净的测试基线。
3. **writing-plans** - 有获批准设计时激活。拆成小任务（各 2–5 分钟）。每项都有准确文件路径、完整代码和验证步骤。
4. **subagent-driven-development** 或 **executing-plans** - 有计划时激活。可以每任务派一个全新子代理并逐个审查（最彻底），也可以在当前会话直接实现全部任务，最后对整个分支进行一次全新审查（最省）。
5. **test-driven-development** - 实施期间激活。强制 RED-GREEN-REFACTOR：编写失败测试，观察失败，写最小代码，观察通过，提交。删除测试之前编写的代码。
6. **requesting-code-review** - 任务之间激活。对照计划审查，按严重程度报告问题。严重问题阻止继续。
7. **finishing-a-development-branch** - 任务完成时激活。验证测试，提供选项（合并/PR/保留/丢弃），清理 worktree。

**任何任务前，代理都检查相关技能。** 这些是强制工作流，不是建议。

## 出现问题时

会话有时行为异常：技能不该触发时触发、该触发时沉默，或代理忽略计划、重复工作、消耗超出预期的 token。让编码代理“查明这个会话中 superpowers 哪里出了问题”，便会调用 **diagnosing-superpowers** 技能。要检查先前会话，请指定它：“查明会话 `<id>` 中 superpowers 哪里出了问题”。

技能读取会话转录，用行级证据报告发生了什么；如果你需要，还会打包脱敏资料包供 bug 报告使用。

## 包含内容

### 技能库

**测试**

- **test-driven-development** - RED-GREEN-REFACTOR 循环（含测试反模式参考）

**调试**

- **systematic-debugging** - 四阶段根因流程（含根因追踪、纵深防御、基于条件等待技术）
- **verification-before-completion** - 确保确实修复
- **diagnosing-superpowers** - 用证据查明会话的问题；导出脱敏资料包或提交 issue

**协作**

- **brainstorming** - 构建前引出意图
- **writing-plans** - 详细实施计划
- **executing-plans** - 当前会话直接执行计划：一个上下文，一次最终审查
- **dispatching-parallel-agents** - 并行子代理工作流
- **requesting-code-review** - 审查前检查清单
- **receiving-code-review** - 回应反馈
- **using-git-worktrees** - 并行开发分支
- **finishing-a-development-branch** - 合并/PR 决策流程
- **subagent-driven-development** - 两阶段审查的快速迭代（先规格符合性，再代码质量）

**元技能**

- **writing-skills** - 依照最佳实践创建新技能（含测试方法论）
- **using-superpowers** - 技能系统入门

## 理念

- **测试驱动开发** - 始终先写测试
- **系统化优于临时处理** - 流程优先于猜测
- **降低复杂度** - 以简单为首要目标
- **证据优于断言** - 宣布成功前先验证

阅读[最初的发布公告](https://blog.fsck.com/2025/10/09/superpowers/)。

## 贡献

Superpowers 的一般贡献流程如下。请注意，我们通常不接受新增技能贡献，任何技能更新都必须能在我们支持的所有编码代理上运行。除非维护者要求，即便你遇到同样问题，我们也不接受代理编写的、修复他人所提 issue 的 PR；请把你的报告添加到现有 issue。

1. Fork 仓库
2. 切换到 'dev' 分支
3. 为你的工作创建分支
4. 遵循 `writing-skills` 技能创建和测试新增及修改技能
5. 提交 PR，填写拉取请求模板每个部分，包括由人类用自己的话撰写的摘要。

技能行为测试使用 [superpowers-evals](https://github.com/prime-radiant-inc/superpowers-evals/) 的 drill 评估宿主，克隆到 `evals/`——设置见 `evals/README.md`。插件基础设施测试位于 `tests/`，通过相关 `run-*.sh` 或 `npm test` 运行。

完整指南见 `skills/writing-skills/SKILL.md`。

## 更新

Superpowers 更新在一定程度上取决于编码代理，但通常自动进行。

## 许可证

MIT 许可证——详情见 LICENSE 文件

## 可视化伴侣遥测

由于技能和插件不向创作者提供反馈，我们不知道有多少人在使用 Superpowers。默认情况下，头脑风暴可选可视化伴侣功能上的 Prime Radiant 标志从我们的网站加载。它包含所用 Superpowers 版本，不包含项目、提示词或编码代理的任何详情。我们看不到你的点击或正在构建的内容。这帮助我们粗略了解多少人使用 Superpowers 及所用版本。它 100% 可选。要禁用，将环境变量 `SUPERPOWERS_DISABLE_TELEMETRY` 设为任意真值。Superpowers 也遵循 Claude Code 的 `DISABLE_TELEMETRY` 和 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` 退出选项。
