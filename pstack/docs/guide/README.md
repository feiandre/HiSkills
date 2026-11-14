# The pstack guide

<!-- zh-CN:begin 0436f9eb8fe51af5 -->

# pstack 指南

<!-- zh-CN:end 0436f9eb8fe51af5 -->

pstack works best when you stop micromanaging the agent. You describe what you want and how you'll know it's done. `/poteto-mode` picks the playbook, runs the other skills as the steps need them, and shows you the evidence. This guide teaches that habit with realistic prompts.

<!-- zh-CN:begin 1efa552a37541408 -->

当你不再微观管理智能体时，pstack 效果最好。你说明想要什么，以及怎样知道完成。`/poteto-mode` 选择操作手册，在步骤需要时运行其他技能，并向你展示证据。本指南用真实提示词训练这种习惯。

<!-- zh-CN:end 1efa552a37541408 -->

Here's what you'll learn:

<!-- zh-CN:begin f28153a86f189da4 -->

你将学到：

<!-- zh-CN:end f28153a86f189da4 -->

1. [Set up pstack](./01-setup.md). Install the plugin and pick your models.

<!-- zh-CN:begin 58f08999cc462b58 -->

1. [设置 pstack](./01-setup.md)。安装插件并选择模型。

<!-- zh-CN:end 58f08999cc462b58 -->
2. [Route work through `/poteto-mode`](./02-poteto-mode.md). Give it a goal and watch it pick a playbook.

<!-- zh-CN:begin 0bdc15373ffdd1cf -->

2. [通过 `/poteto-mode` 路由工作](./02-poteto-mode.md)。给它目标，看它选择手册。

<!-- zh-CN:end 0bdc15373ffdd1cf -->
3. [Understand the code](./03-understand.md). A read-only investigation, then `/how`, `/why`, `/teach`, and `/recall` before you edit anything.

<!-- zh-CN:begin 308b505e4e650f7d -->

3. [理解代码](./03-understand.md)。先进行只读调查，编辑前使用 `/how`、`/why`、`/teach` 和 `/recall`。

<!-- zh-CN:end 308b505e4e650f7d -->
4. [Design the change](./04-design.md). `/architect`, `/arena`, `/swarm`, `/interrogate`, prototypes, and plans before code locks in a shape.

<!-- zh-CN:begin 91a8433a843f02ba -->

4. [设计改动](./04-design.md)。代码锁定形式前，使用 `/architect`、`/arena`、`/swarm`、`/interrogate`、原型和计划。

<!-- zh-CN:end 91a8433a843f02ba -->
5. [Build and clean the change](./05-build-and-clean.md). The build playbooks, `/tdd`, `/unslop`, and `/no-comments`.

<!-- zh-CN:begin fb4ff787b3c7840b -->

5. [构建并清理改动](./05-build-and-clean.md)。构建手册、`/tdd`、`/unslop` 和 `/no-comments`。

<!-- zh-CN:end fb4ff787b3c7840b -->
6. [Verify and ship](./06-verify-and-ship.md). Prove behavior on the real app, formally verify what tests rarely reach, vet numbers with `/benchmark-checklist`, then open a focused PR and drive it to merged.

<!-- zh-CN:begin 0d12c89565c42b67 -->

6. [验证并交付](./06-verify-and-ship.md)。在真实应用证明行为，形式化验证测试少触及的部分，用 `/benchmark-checklist` 审查数字，再创建聚焦 PR 并推动合并。

<!-- zh-CN:end 0d12c89565c42b67 -->
7. [Run work while you sleep](./07-overnight.md). Trust before loops, an overnight contract, a decision log you can audit, and Projects and automations that scale past one agent.

<!-- zh-CN:begin 1d0979443ea2958b -->

7. [睡眠时运行工作](./07-overnight.md)。先建立信任再循环，使用通宵契约、可审计决策日志，以及能扩展到多个智能体的 Projects 和自动化。

<!-- zh-CN:end 1d0979443ea2958b -->
8. [Steer with principle names](./08-principles.md). The 24 names that redirect an agent mid-task.

<!-- zh-CN:begin 0e6ad6f56e20609b -->

8. [用原则名称掌舵](./08-principles.md)。24 个可在任务中途重定向智能体的名称。

<!-- zh-CN:end 0e6ad6f56e20609b -->
9. [Make it yours](./09-make-it-yours.md). Your own mode, `/correct` for repeated mistakes, and how to test a skill change.

<!-- zh-CN:begin 7c6a454711ee9649 -->

9. [让它成为你的](./09-make-it-yours.md)。自己的模式、用 `/correct` 纠正重复错误，以及如何测试技能改动。

<!-- zh-CN:end 7c6a454711ee9649 -->
10. [Recipes and pitfalls](./10-recipes-and-pitfalls.md). Prompts to copy and mistakes to skip.

<!-- zh-CN:begin 5007d833932b47e1 -->

10. [配方与陷阱](./10-recipes-and-pitfalls.md)。可复制提示词和应避开的错误。

<!-- zh-CN:end 5007d833932b47e1 -->

Read the pages in order the first time. After that, each page stands alone.

<!-- zh-CN:begin cb7d9011c61192ed -->

第一次按顺序阅读，之后每页可独立参考。

<!-- zh-CN:end cb7d9011c61192ed -->

When you're stuck, or can't tell which skill fits, type [`/poteto-help`](../../skills/poteto-help/SKILL.md) with your question:

<!-- zh-CN:begin 837d64177cb68b59 -->

遇到困难或不确定哪个技能合适时，用问题输入 [`/poteto-help`](../../skills/poteto-help/SKILL.md)：

<!-- zh-CN:end 837d64177cb68b59 -->

```text
/poteto-help which skill should i use to review this branch?
```

<!-- zh-CN:begin bceebbeedd92aa60 -->

```text
/poteto-help 审查这个分支应该用哪个技能？
```

<!-- zh-CN:end bceebbeedd92aa60 -->

It answers, hands you a prompt to send, and links the skill or guide page the answer came from. It doesn't start the work, because a pstack run spends real tokens, so you send the prompt when you're ready. It runs only when you type it.

<!-- zh-CN:begin 839326ece2642c86 -->

它回答，交给你一条可发送的提示词，并链接答案来源的技能或指南页。它不会开始工作，因为 pstack 运行会消耗真实词元；准备好后由你发送提示词。仅在你输入时运行。

<!-- zh-CN:end 839326ece2642c86 -->

## If you only remember one thing

<!-- zh-CN:begin 628ca5f6fd1c8460 -->

## 只记住一件事

<!-- zh-CN:end 628ca5f6fd1c8460 -->

Give the agent a goal and a way to check it, in your own words:

<!-- zh-CN:begin bae6dd3d8cede222 -->

用自己的话给智能体目标和检查方式：

<!-- zh-CN:end bae6dd3d8cede222 -->

```text
/poteto-mode the export writes duplicate rows when a retry lands mid-run. repro first, then fix and verify.
```

<!-- zh-CN:begin 301b36608797f802 -->

```text
/poteto-mode 重试在运行中途发生时，导出会写入重复行。先复现，再修复并验证。
```

<!-- zh-CN:end 301b36608797f802 -->

You don't need to name a playbook or list skills. "repro first" and a checkable outcome are all the routing signal `/poteto-mode` needs. It matches the Bug fix playbook, copies the steps into a todo list, and calls the right skills as each step fires.

<!-- zh-CN:begin 314682fc3f975e04 -->

无需命名手册或列出技能。“先复现”和可检查结果就是 `/poteto-mode` 所需的路由信号。它匹配缺陷修复手册，将步骤复制到待办列表，并在每步触发时调用正确技能。

<!-- zh-CN:end 314682fc3f975e04 -->

Next: [Set up pstack](./01-setup.md).

<!-- zh-CN:begin 53c891e2159fef1c -->

下一步：[设置 pstack](./01-setup.md)。

<!-- zh-CN:end 53c891e2159fef1c -->
