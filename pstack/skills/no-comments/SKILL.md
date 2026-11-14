---
name: no-comments
description: "启动 Comment Sicko，修复接受的发现，并为声称存在的约束提供编码落实方案。"
disable-model-invocation: true
---

# 不留注释

启动 Comment Sicko。处理接受的发现。

尊重 Comment Sicko 的新鲜视角。

## 范围

使用调用者给定的文件或 diff。否则使用当前相对于基准分支的 diff，默认 `main`，包括工作树。

## 步骤

1. 启动 `Task`，设置 `subagent_type: "comment-sicko"`。传入范围。按照 **poteto-mode** 技能的 Subagents 部分，为每个子代理选择推理级别及 fast 或 standard 速度。不要重述其规则。

2. 检查其报告和 diff。拒绝应用代码编辑、越界操作、受例外保护的删除、错误陈述的 `MUST KILL` 理由，以及把有意保留代码当成有错的标记。针对我们自己代码中意外行为的结构重塑标记仍可执行，不要恢复那些注释。保留项只有在证明其涉及我们无法改变的事物时才成立。审计遗漏的范围内 lint 和 TypeScript 抑制。正确性或安全性抑制仍属于可执行的 `MUST KILL`。恢复删除时必须有精确例外和范围内证明。接受依据薄弱的 `IMPORTANT` 或 `do not remove` 删除或保留项前，对其符号运行 `/how` 或 `/why`。若删除项有歧义，不恢复；若保留项被反驳或仍有歧义，删除。对一份被拒报告，回退并重跑一次，明确指出失败。第二次仍被拒，则报告为未解决，并使 `/no-comments` 失败。

3. 对琐碎的已接受标记，直接通过删除无用路径、去掉参数或使用真实 API 修复。如果任何修复需要确定结构，对已接受集合及周边代码运行一次 `/architect`。停在草图。Architect 负责结构，步骤 4 负责实现。

4. 在范围内实现最小的根因修复。移除每个被点名的变通方案。如果根因在范围外，落地最小的范围内修复，其余报告为未解决。**principle-fix-root-causes** 和 **principle-redesign-from-first-principles** 技能仅指导意图。两者都不授权扩大边界或修复边界外实例。绝不拼接症状守卫。

5. 约束注释会说 `do not remove`、`do not change wording` 或 `talk to X before changing`。涉及我们无法改变事物的保留项留着。提供范围内成本最低的类型、运行时、测试或 CI lint 方案。等待交互式批准。无人值守和评估要求调用者预先批准。批准后先编码落实，再删除。否则删除注释、将约束报告为未解决，并勾勒范围外工作。

6. 报告删除数量、恢复的注释、重跑、architect 草图、修复、提出的编码方案、已落实编码、未强制执行的约束及其他未解决工作。
