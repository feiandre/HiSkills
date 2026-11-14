---
name: principle-migrate-callers-then-delete-legacy-apis
description: "在引入新内部 API 且旧调用者仍存在时应用。在同一波次迁移调用者并删除旧 API，而非保留兼容层。”
disable-model-invocation: true
---

# 先迁移调用者再删除旧 API

- 更新测试以断言新契约，删除只保护重构前实现细节的测试

**适用情形：**

- 没有外部用户依赖向后兼容

- 项目能吸收协调一致的破坏性改动

- 新 API 属于简化或重构计划
