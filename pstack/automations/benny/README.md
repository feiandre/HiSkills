# benny

<!-- zh-CN:begin a2c2ca8964b71c4f -->

# benny（Benny 自动化）

<!-- zh-CN:end a2c2ca8964b71c4f -->

benny gives you two cursor automations for slack issue reports. one triages each report. the other reproduces confirmed bugs and may prepare a small draft fix.

<!-- zh-CN:begin a40073d6b7f90ad8 -->

benny 为 Slack issue 报告提供两个 Cursor 自动化。一个分诊每份报告，另一个复现已确认缺陷并可能准备小型草稿修复。

<!-- zh-CN:end a40073d6b7f90ad8 -->

the files in this directory are dormant setup and automation sources. they do not appear as slash skills.

<!-- zh-CN:begin b36eaeb98ee47f91 -->

本目录文件是休眠的设置和自动化源。它们不作为斜杠技能出现。

<!-- zh-CN:end b36eaeb98ee47f91 -->

## set it up

<!-- zh-CN:begin f7254af5f7eccf38 -->

## 设置

<!-- zh-CN:end f7254af5f7eccf38 -->

1. point cursor at [`FOR_AGENTS.md`](./FOR_AGENTS.md) and name the target repository.

<!-- zh-CN:begin 53b076812d2a7350 -->

1. 将 Cursor 指向 [`FOR_AGENTS.md`](./FOR_AGENTS.md) 并命名目标仓库。

<!-- zh-CN:end 53b076812d2a7350 -->
2. let setup merge this whole directory into the target at `.cursor/automations/benny/`. it must preserve destination-only files and review conflicts instead of overwriting local edits.

<!-- zh-CN:begin 4bb0a99558956bec -->

2. 让设置将整个目录合并到目标的 `.cursor/automations/benny/`。它必须保留目标独有文件并审查冲突，而非覆盖本地编辑。

<!-- zh-CN:end 4bb0a99558956bec -->
3. let setup enable pstack in the target repository's `.cursor/settings.json` for shared dependencies:

<!-- zh-CN:begin f171444884d89327 -->

3. 让设置在目标仓库的 `.cursor/settings.json` 中为共享依赖启用 pstack：

<!-- zh-CN:end f171444884d89327 -->

```json
{
	"plugins": {
		"pstack": { "enabled": true }
	}
}
```

4. keep user-owned configuration outside the copied pack, for example in `.cursor/benny/`. adapt [`configuration.example.yaml`](./templates/configuration.example.yaml) and [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md).

<!-- zh-CN:begin 6129481cd8d8ab51 -->

4. 将用户拥有的配置保留在复制的包之外，例如 `.cursor/benny/`。调整 [`configuration.example.yaml`](./templates/configuration.example.yaml) 和 [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md)。

<!-- zh-CN:end 6129481cd8d8ab51 -->
5. commit `.cursor/settings.json`, `.cursor/automations/benny/`, and any secret-free configuration before enabling either automation.

<!-- zh-CN:begin 24606d42df9e29d4 -->

5. 启用任一自动化前，提交 `.cursor/settings.json`、`.cursor/automations/benny/` 及任何无秘密配置。

<!-- zh-CN:end 24606d42df9e29d4 -->
6. review each new automation draft or update existing automations in their editors. then send a harmless test report and verify every source-channel post stays in the original thread.

<!-- zh-CN:begin be441c5f56225983 -->

6. 在编辑器中审查每个新自动化草稿或更新现有自动化。然后发送一份无害测试报告，并验证每个 source-channel 帖子都留在原线程。

<!-- zh-CN:end be441c5f56225983 -->
