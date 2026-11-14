---
name: typescript-best-practices
description: TypeScript 最佳实践。阅读或编辑任何 .ts 或 .tsx 文件时使用。
paths: ["**/*.ts", "**/*.tsx"]
disable-model-invocation: true
---

# TypeScript 最佳实践

先应用 **type-system-discipline** 原则技能。

| 规则 | 摘要 |
|------|---------|
| 可辨识联合 | 使用 `kind` 字面判别值建模变体，使不可能状态无法表示。不要使用可选字段袋。 |
| 品牌类型 | 用 `& { readonly __brand: "X" }` 标记原始类型以免混淆。在边界验证一次。品牌来自可验证类型守卫（`input is AgentId`），绝不来自 `as`。 |
| 构造式建模 | 构建形态，使非法值无法构造。`[T, ...T[]]` 用于非空，`[T, T][]` 用于偶数长度，`start` 加 `duration` 表示范围。不要运行时代码守卫，也不要寄望细化类型。 |
| 最简单的全域类型 | 保持 `T[]`，只要其上每个操作都保持全域。仅当宽松类型迫使使用 `!`、类型断言或“永远不应发生”的抛出时，才强化为 `NonEmpty<T>`。 |
| `unknown` 优于 `any` | 外部数据为 `unknown`。 |
| 先模式后守卫 | 手写逐属性类型守卫之前，使用仓库的运行时模式库并从模式推断类型，例如 `z.infer`。 |
| 不要 `as` 类型断言 | 每次 `as` 都潜藏运行时崩溃。只在验证后断言。 |
| 收窄层级 | 判别字段 switch > `in` 运算符 > `typeof`/`instanceof` > 用户定义类型守卫 > `as`。 |
| 类型守卫 | 必须验证断言。撒谎的守卫比 `as` 更糟，因为缺陷藏在一个声称安全的名称后面。命名为 `isX` 或 `hasX`。 |
| 穷尽性 | 在 default 分支中内联 `const _exhaustive: never = x;`，使新增变体时编译器报错。 |
| `satisfies` 优于 `as` | 验证值而不会拓宽字面量类型。 |
| 边界验证 | 在数据进入时解析为具名领域类型。`Record<string, unknown>`（无论怎样拼写）止于该解析。内部信任类型。参见 **boundary-discipline** 原则技能。 |
| 从模式派生类型 | 声明新接口之前优先使用 `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof`。 |
| 对象参数 | 传递对象而非位置参数，使参数顺序自解释。热路径（逐帧渲染、分词器、解析器）可跳过。 |
| 真实测试 | 能运行的不要模拟。优先使用框架的真实测试原语并检查泄漏／可释放对象，在运行构建中验证 UI。只模拟本地无法运行的内容。 |
| 结构化遥测 | 优先使用包含足够上下文、可从 id 调试的结构化日志诊断。不要在发布代码中使用 `console.log`。 |

示例见 `references/patterns.md`。
