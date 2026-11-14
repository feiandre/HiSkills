# Databricks 分析与系统表

## 此来源包含什么

Databricks 是产品分析、数据管道与仓库遥测层，可补充 Datadog。Datadog 提供*基础设施/运行时*视角，Databricks 提供*产品/数据*视角：用户做了什么、运行了哪些实验、功能使用如何演变、阈值常量从何而来。

- **产品分析事件。** 原始表 `your_warehouse.events.analytics_track_event`，以及 `<your_analytics_db>.<schema>.<table>` 中按事件类型去重、带类型的 dbt 模型。用户行为包括功能调用、点击、接受/拒绝、提交、客户端上报错误。

- **用量与计费事件。** `your_warehouse.events.usage_event` / `<your_analytics_db>.<schema>.stg_usage_events`，以及 `your_warehouse.events.raw_model_event` / `<your_analytics_db>.<schema>.stg_raw_model_events`。用于成本或用量驱动的决策。

- **实验/功能开关数据。** 曝光与结果表。**模式因公司而异。** 假设表名之前先用 `SHOW TABLES` 探查。

- **系统表。** `system.query.history`、`system.compute.warehouses`、`system.billing.*`、`system.access.audit`。可回答“这个查询昂贵吗？”“有人运行过多少次？”“仓库负载何时飙升？”

- **dbt 血缘。** `<your_analytics_db>.<schema>` 中的模型揭示哪些管道依赖某表/字段。上游变更常会促使消费方代码修改。

- **Databricks notebook。** 工程师在改动代码前写的探索性分析。**无法通过 SQL MCP 查询。** 若怀疑依据在 notebook 中，应明确列为缺口。

## 如何搜索

使用 Databricks SQL MCP。主要工具为 `execute_sql_read_only`。若返回 `statement_id`，用 `poll_sql_result` 轮询，不要重跑。

**查询前先了解结构。** 模式因公司而异，信任表名之前先探查：

```sql
SHOW TABLES IN <your_analytics_db>.<schema> LIKE '*<keyword>*';
DESCRIBE TABLE <your_analytics_db>.<schema>.stg_<event>;
```

**每个查询都限定时间。** 表很大，无约束扫描会超时。按 `_timestamp`（事件）或 `start_time`（`system.query.history`）过滤，窗口覆盖发布日期前后，通常各约 30 天，只有充分理由才扩大。

**优先使用带类型的 dbt 模型。** `<your_analytics_db>.<schema>.<table>` 已去重、带类型并采用 liquid clustering。`your_warehouse.events.analytics_track_event` 有重复，且 `properties_json` 不带类型。模型名通常为 `stg_<source>_<event_name_with_underscores>`，`<source>` 是 `app`、`backend`、`website` 或 `cli`。仅凭模式无法确定时用 `SHOW TABLES` 确认；仅当尚无 dbt 模型，或需要 dbt 刷新延迟内的事件时才回到原始表。

**带类型 dbt 模型的列约定**（了解这些可少一次 `DESCRIBE`）：

- `_timestamp`、`_id`、`_auth_id`、`_request_id`、`event_name`。每个模型都有。

- `properties_<name>`。带类型、以下划线命名的事件属性（`properties_entrypoint`、`properties_size_bytes` 等）。

- `context_team_id`、`context_client_version`、`context_country`、`context_client_os`。预先提取的客户端上下文。

### 通常有回报的调查模式

按目标选表与列组合：

1. **事件使用轨迹。** 在 PR 合并前后 ±30 天内统计相关 `stg_*` 每日数量。合并后一两天内从零跳到稳定量，是有力旁证，说明 PR 发布了功能；衰减到零可能表示废弃或删除。

2. **防护/防御性检查来源。** 查看 PR 前 14 天相关 `properties_<name>` 的分布（中位数 / p99 / 最大值）。p99 与目标阈值常量吻合，可能说明数值来自数据。

3. **实验/功能开关查找。** 用 `SHOW TABLES ... LIKE '*experiment*'` 找曝光表，再按变体统计 PR 日期附近相关开关键的曝光数。

4. **迁移、回填或性能重写的查询历史证据。** 在紧凑 `start_time` 窗口内用 `statement_text ILIKE '%<table_or_symbol>%'` 筛选 `system.query.history`，找出可能促使变更的昂贵查询（按 `total_duration_ms` 排序，或聚合 `SUM(read_bytes)`、`COUNT(*)`）。

5. **dbt 血缘。** 若目标读写 `<your_analytics_db>.<schema>` 模型，该模型在本仓库的 git 历史常有依据。将此线索交回 git 调查者，不要自行追查。

## 什么样的证据好

除上述模式外：

- 防御性代码 PR 后几天内某类错误事件数降至接近零，可能说明 PR 解决了该类错误。

- 曝光表某行列出目标功能开关键，且 PR 发布日期附近有“已发布”/“已结束”决策。

## 常见陷阱

- **有埋点不等于因果。** 事件存在只说明有人特意记录，不表示目标代码*因为*它而存在。与 git 调查者给出的 PR/提交引用结合后才声称因果。

- **埋点静默变化。** 事件量阶跃可能只是开始记录新事件，并非用户行为变化。解读增长前检查同窗口是否有埋点 PR。

- **模式漂移。** 事件属性会演变，今天的 dbt 列在目标代码编写时可能不存在。旧数据也许只在原始 `properties_json` 中保存属性。

- **dbt 刷新延迟。** `<your_analytics_db>.<schema>.*` 按计划重建（常为每小时/每天）。最近数小时事件应改用 `your_warehouse.events.*`，并按 `_id` 去重。

- **公司专属表。** 实验、开关、计费与用量表各有差异。没有确认表存在便报告结果是典型失败。先用 `SHOW TABLES` / `DESCRIBE TABLE` 探查。

- **保留期断崖。** 窗口早于表保留期或 dbt 模型创建日期时，这是*缺口*，不是空结果。明确说明，避免汇总者把“无结果”读成“无活动”。

- **Notebook 不可查询。** SQL MCP 看不到 Databricks notebook；若依据可能在 notebook 中，报告缺口。

## 返回什么

对每个相关发现：

- 类型（产品事件 / 实验曝光 / 用量或计费事件 / 系统表行 / dbt 模型）

- 完整限定表名和实际查询

- 查询时间窗口

- 简洁数值摘要（计数、百分位、首次/最后出现时间）。**不要倾倒原始行。**

- 与目标发布日期的时序相关性（例如“首行 2024-08-15，PR #49074 于 2024-08-14 合并”）

- 相关性与强度：直接 / 旁证 / 弱
