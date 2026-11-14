---
name: pr
description: "撰写 PR 正文时使用。"
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

使用以下模板撰写 PR 正文：

```markdown
## 摘要

<图表、差异草图或树形图>

## 证据

- **之前：** <截图、输出或失败的测试运行结果>
  **之后：** <截图、输出或通过的测试运行结果>

## 合并风险

**门：** <单向门或双向门>

<可选：描述>

**影响范围：** <用一个词概述>

<可选：合并的潜在影响>
```

## 章节

跳过所有开场白，文字保持简短。使用 `GLOSSARY.md` 中用户的领域语言。

### 摘要

选择能说明关键点的最小视图。

- 用伪代码展示逻辑或算法：

- 用调用树展示运行时控制流：

- 用组件树展示 UI 结构，包括重要状态和模块边界：

- 用浅层文件树展示文件职责或大范围重构：

```text
src/
├── commands/       # 解析用户操作
├── sessions/       # 拥有会话状态
└── transport/      # 发送 API 请求
```

- 用 Mermaid 展示组件交互、控制流或数据流：

- 重点是“改变了什么”且周边结构已存在时，使用 `diff`。让差异形式与主题匹配。

对于组件变更：

对于文件布局变更：

```diff
 src/
 ├── commands/
+│   └── show-me.ts       # 展开斜杠命令
 ├── sessions/
-└── transport.ts
+└── transport/
+    ├── client.ts
+    └── stream.ts
```

对于调用树或调用栈变更：

对于状态或控制流变更：

- 大部分内容新增、删除上下文会掩盖归属或顺序，或用户需要可复制目标结构时，展示完整代码块：

```ts
function expandSkill(command: string): string {
  const skillName = command.slice(1);
  // 返回一条发送给智能体的技能调用提示
  return `use the ${skillName} skill`;
}
```

#### 指导

每项可视化都放在其所支持的简短文字旁。只保留回答当前问题或解释选项所需的调用、文件、props、状态和边界。

可以只用一种或多种，但不太可能全用。自行判断，不要淹没用户。

### 证据

展示变更有效的具体证据，给出前后对比。

环境具备且变更具有视觉效果时，截图是 S 级证据。

基于执行的证据是 A 级：测试结果、控制台输出。展示确切测试在变更前失败、变更后通过。

### 合并风险

描述这是单向门还是双向门。双向门可以返回，单向门不能。回滚成本低的 PR 风险较小。涉及破坏性操作或难以逆转的决策属于单向门。

影响范围是本 PR 改动可能产生的影响或作用范围，例如布局偏移、消费者功能损坏、移动端响应式表现。
