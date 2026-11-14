# 面向发现的 SKILL.md 编写

属于 superpowers:writing-skills：介绍 SKILL.md 模板，以及如何命名、描述和确定技能规模，让智能体找到并阅读它。

## SKILL.md 结构

**前置元数据（YAML）：**

- 两个必需字段：`name` 和 `description`（所有支持字段见 [agentskills.io/specification](https://agentskills.io/specification)）

- 总计最多 1024 个字符

- `name`：只使用字母、数字和连字符（不含括号或特殊字符）

- `description`：第三人称，只说明何时使用（不说明它做什么）

- 以“Use when...”开头，聚焦触发条件

- 包括具体症状、情况和背景

- **绝不要概括技能流程或工作流**（原因见下文技能发现优化）

- 尽可能控制在 500 字符以内

```markdown
---
name: Skill-Name-With-Hyphens
description: 在[具体触发条件和症状]时使用
---

# 技能名称

## 概述
这是什么？用 1-2 句话说明核心原则。

## 何时使用
[决策不明显时，加入小型内联流程图]

以列表列出症状和用例
不应使用的时机

## 核心模式（适用于技术／模式）
修改前后代码对比

## 快速参考
用于浏览常用操作的表格或列表

## 实现
简单模式使用内联代码
大量参考或可复用工具链接到文件

## 常见错误
出错原因与修复

## 现实影响（可选）
具体结果
```

## 技能发现优化（SDO）

**对发现至关重要：** 未来智能体需要找到你的技能

### 1. 丰富的 Description 字段

**目的：** 智能体读取 description 决定为任务加载哪些技能。让它回答：“我现在应该读这个技能吗？”

**格式：** 以“Use when...”开头，聚焦触发条件

**关键：description = 何时使用，而不是技能做什么**

description 只应描述触发条件。不要在 description 中概括技能流程或工作流。

**为什么重要：** 测试发现，description 概括工作流时，智能体可能照它执行而不读技能全文。一个写明“任务之间进行代码审查”的 description 让智能体只做一次审查，即使技能流程图清楚显示两次审查（规格符合性，然后代码质量）。

把 description 改成仅“在当前会话执行含独立任务的实现计划时使用”（不再概括工作流）后，智能体正确阅读流程图并执行两阶段审查。

**陷阱：** 概括工作流的 description 提供了智能体会走的捷径。技能正文反而变成被跳过的文档。

```yaml
description: 执行计划时使用——每个任务派发子智能体，任务之间进行代码审查
description: 用于 TDD——先写测试、看它失败、写最少代码、重构
description: 在当前会话执行含独立任务的实现计划时使用
description: 实现任何功能或修复缺陷时，在编写实现代码之前使用
```

**内容：**

- 使用具体触发点、症状和表明技能适用的情境

- 描述*问题*（竞争条件、行为不一致），而不是*语言专属症状*（setTimeout、sleep）

- 除非技能本身针对特定技术，否则触发条件保持技术无关

- 若技能针对特定技术，请在触发条件中明确

- 使用第三人称（会注入系统提示词）

- **绝不要概括技能的流程或工作流**

```yaml
description: 用于异步测试
description: 异步测试不稳定时，我可以帮你
description: 测试使用 setTimeout/sleep 且不稳定时使用
description: 测试存在竞争条件、时序依赖或通过／失败结果不一致时使用
description: 使用 React Router 并处理身份认证重定向时使用
```

### 2. 关键词覆盖

使用智能体会搜索的词：

- 错误消息：“Hook timed out”、“ENOTEMPTY”、“race condition”

- 症状：“flaky”、“hanging”、“zombie”、“pollution”

- 同义词：“timeout/hang/freeze”、“cleanup/teardown/afterEach”

- 工具：实际命令、库名、文件类型

### 3. 描述性命名

**使用主动语态、动词优先：**

- ✅ `creating-skills`，而非 `skill-creation`

- ✅ `condition-based-waiting`，而非 `async-test-helpers`

### 4. 词元效率（关键）

**问题：** 入门和频繁引用的技能会加载到每个对话中。每个词元都算数。

**目标字数：**

- 入门工作流：每个少于 150 词

- 频繁加载的技能：总计少于 200 词

- 其他技能：少于 500 词（仍应简洁）

**技巧：**

**把细节移到工具帮助：**

```bash
search-conversations 支持 --text、--both、--after DATE、--before DATE、--limit N
search-conversations 支持多种模式和过滤器。运行 --help 查看详情。
```

**使用交叉引用：**

```markdown
# ❌ 错误：重复工作流细节
搜索时，使用模板派发子智能体……
[20 行重复说明]

# ✅ 正确：引用其他技能
始终使用子智能体（节省 50-100 倍上下文）。必需：工作流使用 [other-skill-name]。
```

**压缩示例：**

```markdown
# ❌ 错误：冗长示例（42 词）
你的人类伙伴：“以前我们如何处理 React Router 的认证错误？”
你：我会搜索过去的对话，寻找 React Router 认证模式。
[派发子智能体，搜索：“React Router authentication error handling 401”]

# ✅ 正确：最小示例（20 词）
伙伴：“我们如何处理 React Router 的认证错误？”
你：正在搜索……
[派发子智能体 → 综合]
```

**消除冗余：**

- 不要重复交叉引用技能中的内容

- 不要解释命令本身已显而易见的内容

- 不要为同一模式加入多个示例

**验证：**

```bash
wc -w skills/path/SKILL.md
```

**按你做的事或核心洞见命名：**

- ✅ `condition-based-waiting` 优于 `async-test-helpers`

- ✅ `using-skills`，而非 `skill-usage`

- ✅ `flatten-with-flags` 优于 `data-structure-refactoring`

- ✅ `root-cause-tracing` 优于 `debugging-techniques`

**动名词（-ing）适合流程：**

- 主动表达你正在执行的动作

### 5. 交叉引用其他技能

**编写引用其他技能的文档时：**

只使用技能名称，并配明确要求标记：

- ✅ 正确：`**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development`（必需子技能：使用 test-driven-development）

- ✅ 正确：`**REQUIRED BACKGROUND:** You MUST understand superpowers:systematic-debugging`（必需背景：你必须理解 systematic-debugging）

- ❌ 错误：`See skills/testing/test-driven-development`（是否必需不清楚）

- ❌ 错误：`@skills/testing/test-driven-development/SKILL.md`（强制加载，消耗上下文）

**为什么不用 @ 链接：** `@` 语法会立即强制加载文件，在你需要前就消耗 20 万以上上下文。
