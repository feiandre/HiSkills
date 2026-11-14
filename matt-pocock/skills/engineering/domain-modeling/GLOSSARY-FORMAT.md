# GLOSSARY.md 格式

## 结构

```md
# {上下文名称}

{用一两句话说明该上下文是什么以及为何存在。}

## 语言

**Order（订单）**：
{用一两句话说明术语。}
_避免_：Purchase、transaction

**Invoice（发票）**：
交付后向客户发送的付款请求。
_避免_：Bill、payment request

**Customer（客户）**：
下订单的人或组织。
_避免_：Client、buyer、account
```

## 规则

- **要有主张。**同一概念有多个词时选最佳词，其余列入 `_Avoid_`。

- **定义紧凑。**最多一两句；说明它是什么，而非做什么。

- **只收录本项目上下文特有的术语。**通用编程概念（超时、错误类型、工具模式）即使大量使用也不收录。添加前问：这是本上下文独有概念，还是通用编程概念？只收前者。

- **自然分组时按小标题归类。**若全部术语属于同一整体，扁平列表即可。

## 单上下文和多上下文仓库

**单上下文（多数仓库）：**根目录一个 `GLOSSARY.md`。

**多上下文：**根目录 `GLOSSARY-MAP.md` 列出上下文、位置和关系：

```md
# 术语表地图

## 上下文

- [Ordering（下单）](./src/ordering/GLOSSARY.md)：接收并跟踪客户订单
- [Billing（计费）](./src/billing/GLOSSARY.md)：生成发票并处理付款
- [Fulfillment（履约）](./src/fulfillment/GLOSSARY.md)：管理仓库拣货和发货

## 关系

- **Ordering → Fulfillment**：Ordering 发出 `OrderPlaced` 事件，Fulfillment 消费并开始拣货
- **Fulfillment → Billing**：Fulfillment 发出 `ShipmentDispatched`，Billing 消费并生成发票
- **Ordering ↔ Billing**：共享 `CustomerId` 和 `Money` 类型
```

技能据此推断结构：

- 存在 `GLOSSARY-MAP.md` 时读取并定位上下文

- 只有根 `GLOSSARY.md` 时视为单上下文

- 两者都不存在时，在首次确定术语时才创建根 `GLOSSARY.md`

存在多个上下文时，推断当前主题属于哪个；不清楚就问。
