# 来源操作手册

why 技能为每个可用证据类别启动一名调查者，每人只阅读下面一份来源专用操作手册。它们是常见 MCP 的具体示例。对同类其他 MCP 做相应适配。

| 类别 | 操作手册 | 文档中的 MCP 示例 |
|---|---|---|
| 源代码管理历史 | [`code-archaeology.md`](./sources/code-archaeology.md) | git、`gh` |
| 问题／工单跟踪器 | [`linear.md`](./sources/linear.md) | Linear（可适配 Jira、GitHub Issues、Plane、Shortcut） |
| 长篇文档 | [`notion.md`](./sources/notion.md) | Notion（可适配 Confluence、Google Docs、Coda） |
| 实时团队聊天 | [`slack.md`](./sources/slack.md) | Slack（可适配 Discord、Microsoft Teams、Mattermost） |
| 基础设施可观测性 | [`datadog.md`](./sources/datadog.md) | Datadog（可适配 New Relic、Honeycomb、Grafana、Splunk） |
| 错误／异常跟踪 | [`sentry.md`](./sources/sentry.md) | Sentry（可适配 Rollbar、Bugsnag、Airbrake） |
| 产品分析仓库 | [`databricks.md`](./sources/databricks.md) | Databricks SQL（可适配 Snowflake、BigQuery、ClickHouse、dbt） |

跨领域来源：

- [`incident-postmortem.md`](./sources/incident-postmortem.md)。如果目标代码呈防御性（空值检查、重试、超时、限流、功能开关、出站防护、OOM 处理器），加入此项。
