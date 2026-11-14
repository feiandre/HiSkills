# Hermes 版本递增接线设计

**日期：** 2026-08-05
**修订：** 2026-08-06
**状态：** 已批准

## 目标

将 `.hermes-plugin/plugin.yaml` 注册到 `.version-bump.json`，让 `scripts/bump-version.sh` 处理 YAML，且不在 Bash 实现 YAML 解析器，使 Hermes 清单与仓库版本同步。

## 设计

- 在 `.version-bump.json` 添加 `{ "path": ".hermes-plugin/plugin.yaml", "field": "version" }`。

- `.json` 走现有 `jq` 辅助函数，`.yaml` 走 Mike Farah `yq` v4；键和值作为数据传入，不插入表达式。

- 只支持存在的顶层 YAML 字符串字段；嵌套字段及 `.yml` 不在范围。

- `--check`、`--audit` 与版本更新均经同一个小型读写分派器。

- 任何版本递增写清单前，先运行一次只读预检：验证所需工具，并经由分派器读取所有存在的已声明清单。这防止旧 JSON 已更新后 YAML 才确定性失败。缺失文件行为不变，无 `jq` 或 `yq` 时 `--help` 仍工作。

预检是唯一可靠性增强，不使脚本具备事务性，也不重设计现有审计与错误状态行为。

## 测试

三个聚焦行为测试在隔离临时夹具上运行真实脚本，证明：

- 对齐的 JSON 和 YAML 通过 `--check`、`--audit`，递增会更新两种格式；

- 实际递增中，JSON 先声明，后一个 YAML 清单顶层 `version` 非字符串时，以非零退出，所有清单逐字节不变；以及

- 真实 `.version-bump.json` 注册 Hermes 清单。

验证还运行 shell lint 和仓库上的 `scripts/bump-version.sh --check`。

## 非目标

- 不手写 YAML 解析器。

- 不支持 `.yml` 或嵌套 YAML。

- 不改变 Hermes 运行时。

- 不增加回滚框架、通用配置模式层、审计/状态重构或穷尽失败矩阵。

- 不修复评审中发现的独立版本验证与 JSON 表达式问题。
