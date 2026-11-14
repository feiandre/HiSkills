# Reproduce automation prompt

<!-- zh-CN:begin a8d0335847aa4481 -->

# 复现自动化提示词

<!-- zh-CN:end a8d0335847aa4481 -->

> Source material for the copied setup workflow. Paraphrase this intent into a built-in `automate` draft after `automate` confirms that the copied pack is committed in the repository where the automation will run.

<!-- zh-CN:begin 9f1c348307354e9b -->

> 供复制后的设置工作流使用的来源材料。内置 `automate` 确认已复制包提交到自动化运行的仓库后，将此意图转述为 `automate` 草稿。

<!-- zh-CN:end 9f1c348307354e9b -->

Read and follow `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` for this run.

<!-- zh-CN:begin af93538a1089f025 -->

本次运行读取并遵循 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`。

<!-- zh-CN:end af93538a1089f025 -->

Configuration source. Include this repository-relative path only when it is committed in the same target repository. Otherwise paraphrase the configured values. Never use a plugin source or cache path:

<!-- zh-CN:begin 3af2e9baae4b826d -->

配置来源。只有提交到同一目标仓库时，才包含此仓库相对路径。否则转述配置值。绝不使用插件源路径或缓存路径：

<!-- zh-CN:end 3af2e9baae4b826d -->

```text
{{BENNY_CONFIG_PATH}}
```

Trigger:

<!-- zh-CN:begin e25eb59121578792 -->

触发器：

<!-- zh-CN:end e25eb59121578792 -->

```json
{
	"source_channel_id": "{{SLACK_CHANNEL_ID}}",
	"message_ts": "{{SLACK_MESSAGE_TS}}",
	"thread_ts": "{{SLACK_THREAD_TS_OR_EMPTY}}"
}
```

The creation intent should describe this as a new top-level report in the configured source Slack channel. It should include the configured repository, default branch, issue tracker, control adapter, feature map, and draft pull request capability.

<!-- zh-CN:begin f93f956e860aa0c9 -->

创建意图应描述为配置来源 Slack 频道中的新顶层报告。应包含配置的仓库、默认分支、问题跟踪器、控制适配器、功能地图及草稿拉取请求能力。

<!-- zh-CN:end f93f956e860aa0c9 -->

Treat the source channel and root thread timestamp as immutable. If either is missing or does not match configuration, stop without posting.

<!-- zh-CN:begin 340552cd96da1d50 -->

将来源频道和根线程时间戳视为不可变。任一缺失或与配置不匹配，停止且不发帖。

<!-- zh-CN:end 340552cd96da1d50 -->

Wait for a configured triage marker from the configured triage identity in this exact thread. Proceed only for `[benny:bug]` or `[benny:performance]`.

<!-- zh-CN:begin 6160710da729542f -->

等待配置的分诊身份在此确切线程发出配置的分诊标记。仅对 `[benny:bug]` 或 `[benny:performance]` 继续。

<!-- zh-CN:end 6160710da729542f -->

Require the configured control-adapter skill before attempting a repro. Reproduce the exact discriminating symptom twice through the real UI. Verify existing pull requests or commits without authoring over them. Attempt a bounded fix only after a confirmed repro and the operational file's fix gate.

<!-- zh-CN:begin 42e5d1f231acd38e -->

尝试复现前必须具备配置的控制适配器技能。通过真实 UI 将可明确区分的确切症状复现两次。验证现有拉取请求或提交，不另行编写覆盖它们。只有确认复现并通过操作文件的修复关卡后，才尝试范围受限的修复。

<!-- zh-CN:end 42e5d1f231acd38e -->

The coordinator is the only Slack poster. Every child prompt must forbid `SendSlackMessage`, `PostToSlack`, `chat.postMessage`, and all other Slack writes. Children return findings only.

<!-- zh-CN:begin 0f85794588841a1a -->

协调者是唯一能在 Slack 发帖的人。每份子提示词必须禁止 `SendSlackMessage`、`PostToSlack`、`chat.postMessage` 及全部其他 Slack 写入。子代理只返回发现。

<!-- zh-CN:end 0f85794588841a1a -->

Never post a root message in the source channel.

<!-- zh-CN:begin f9980671f81bfe16 -->

绝不在来源频道发布根消息。

<!-- zh-CN:end f9980671f81bfe16 -->
