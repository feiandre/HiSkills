---
name: requesting-code-review
description: "完成任务、实现重要功能，或合并前验证工作是否符合要求时使用"
---

# 请求代码审查

派发代码审查子代理，在问题连锁扩散之前捕捉它们。审查者应获得为评估精心组织的上下文，绝不能获得你的会话历史。

**核心原则：** 尽早审查，经常审查。

## 何时请求审查

**强制：**

- 子代理驱动开发中的每个任务之后。

- 完成重要功能之后。

- 合并到 main 之前。

**可选，但有价值：**

- 遇到困难时，获得全新视角。

- 重构之前，进行基线检查。

- 修复复杂缺陷之后。

## 如何请求

**1. 获取 git SHA：**

```bash
BASE_SHA=$(git rev-parse HEAD~1)  # 或：git merge-base origin/main HEAD
HEAD_SHA=$(git rev-parse HEAD)
```

**2. 派发代码审查子代理：**

填写 [code-reviewer.md](code-reviewer.md) 中的模板，派发一个 `general-purpose` 子代理。

**占位符：**

- `{DESCRIPTION}`：简要概括你构建了什么。

- `{PLAN_OR_REQUIREMENTS}`：它应当完成什么。

- `{BASE_SHA}`：起始提交。

- `{HEAD_SHA}`：结束提交。

**3. 处理反馈：**

- 立即修复 Critical 问题。

- 继续之前修复 Important 问题。

- 记录 Minor 问题，留待之后处理。

- 如果审查者有误，提出异议并说明理由。

## 示例

```
[刚完成任务 2：添加验证函数]

你：继续之前，我先请求代码审查。

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | cut -d' ' -f1)
HEAD_SHA=$(git rev-parse HEAD)

[派发代码审查子代理]
  DESCRIPTION: 添加了 verifyIndex() 和 repairIndex()，涵盖 4 类问题
  PLAN_OR_REQUIREMENTS: docs/superpowers/plans/deployment-plan.md 中的任务 2
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661

[子代理返回]：
  优点：架构清晰，使用真实测试
  问题：
    Important: 缺少进度指示
    Minor: 报告间隔使用魔法数字（100）
  评估：可以继续

你：[修复进度指示]
[继续任务 3]
```

## 常见的自我辩解

| 借口 | 实际情况 |
|--------|---------|
| “我自己审查差异就行，不用派发审查者” | 你是协调者，在当前上下文里审查差异，会消耗继续推进工作所需的上下文窗口。派发审查子代理：差异和评估保留在它的上下文中，只有发现会返回给你。 |
| “审查者需要我的整个会话历史才能理解改动” | 提供精心组织的上下文，绝不要提供会话历史。这样审查者就会关注工作成果，而非你的思考过程。 |

## 危险信号

**绝不要：**

- 因为“很简单”而跳过审查。

- 忽略 Critical 问题。

- Important 问题尚未修复就继续。

- 对有效的技术反馈争辩。

**如果审查者有误：**

- 使用技术推理提出异议。

- 展示证明其有效的代码或测试。

- 请求澄清。

模板见：[code-reviewer.md](code-reviewer.md)。
