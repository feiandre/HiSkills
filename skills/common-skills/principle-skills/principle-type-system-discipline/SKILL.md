---
name: principle-type-system-discipline
description: "在设计类型、审查函数签名或编写静态类型语言代码时使用。让非法状态无法表示，为语义基本类型添加品牌，在边界解析外部数据，穷尽处理变体，并从权威模式派生类型。"
disable-model-invocation: true
---

# 类型系统纪律

让编译器拒绝不可能状态、错配的基本类型和未处理变体。优先让错误和特例根本不存在，而非堆叠处理器。TypeScript 语法见 `typescript-best-practices` 技能。

- **给语义基本类型加品牌。** `UserId` 与 `OrderId` 底层都是字符串，但不可互换。为各自建类型，例如 TypeScript 的品牌交叉类型或其他语言 newtype。创建时验证一次，下游信任类型。两个参数同为基本类型但含义不同时必须加品牌。

- **外部数据在解析前不带类型。** RPC 载荷、JSON、IPC 消息、CLI 参数、配置文件、环境变量、数据库行都是如此。每个边界应有解析函数，将非结构化输入转为带类型模型；**boundary-discipline** 原则技能说明验证位置。

- **从权威模式派生类型。** protocol buffer、OpenAPI、GraphQL schema、数据库迁移、设计 token 文件等拥有形状时，从它们派生，不手工维护平行类型。见 **encode-lessons-in-structure** 原则技能。
