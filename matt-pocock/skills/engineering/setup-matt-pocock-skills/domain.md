# 领域文档

探索代码库时，工程技能应如何使用本仓库的领域文档。

## 探索前阅读

- 仓库根目录的 **`GLOSSARY.md`**，或

- 若存在根目录 **`GLOSSARY-MAP.md`**：每个上下文一个 `GLOSSARY.md`，阅读相关文件。

- **`docs/adr/`**：阅读涉及即将改动区域的 ADR；多上下文仓库也检查 `src/<context>/docs/adr/`。

不存在时**静默继续**，不指出缺失或建议提前创建。`/domain-modeling`（经 `/grill-with-docs` 与 `/improve-codebase-architecture` 到达）会在术语或决策实际确定时按需创建。

## 文件结构

单上下文仓库（多数仓库）：

```
/
├── GLOSSARY.md                ← 领域术语表
├── docs/adr/                  ← 架构决策记录
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

多上下文仓库（根目录存在 `GLOSSARY-MAP.md`）：

```
/
├── GLOSSARY-MAP.md            ← 多上下文地图
├── docs/adr/                  ← 系统级决策
└── src/
    ├── ordering/
    │   ├── GLOSSARY.md
    │   └── docs/adr/          ← 上下文专属决策
    └── billing/
        ├── GLOSSARY.md
        └── docs/adr/
```

## 使用术语表词汇

输出提及领域概念时，使用 `GLOSSARY.md` 定义词，不漂移到明确避免的同义词。

概念尚不在术语表中：要么你发明了项目不使用的语言（重新考虑），要么存在真实缺口（记录给 `/domain-modeling`）。

## 标出 ADR 冲突

与现有 ADR 矛盾时明确呈现，不静默覆盖：

> _与 ADR-0007（事件溯源订单）矛盾，但值得重新讨论，因为……_
