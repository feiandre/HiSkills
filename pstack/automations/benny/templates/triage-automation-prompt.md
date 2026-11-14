# Triage automation prompt

<!-- zh-CN:begin 7fe5fda2bb211aaa -->

# 分诊自动化提示词

<!-- zh-CN:end 7fe5fda2bb211aaa -->

> Source material for the copied setup workflow. Paraphrase this intent into a built-in `automate` draft after `automate` confirms that the copied pack is committed in the repository where the automation will run.

<!-- zh-CN:begin 4235e5574324ffb3 -->

> 复制后设置工作流所用的源材料。`automate` 确认复制包已提交到自动化将运行的仓库后，把此意图改写成内置 `automate` 草稿。

<!-- zh-CN:end 4235e5574324ffb3 -->

Read and follow `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md` for this run.

<!-- zh-CN:begin dad806e7a280f6ad -->

本次运行请阅读并遵循 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`。

<!-- zh-CN:end dad806e7a280f6ad -->

Configuration source. Include this repository-relative path only when it is committed in the same target repository. Otherwise paraphrase the configured values. Never use a plugin source or cache path:

<!-- zh-CN:begin c03b5100b20ec6c0 -->

配置来源。仅当该相对仓库路径已提交到同一目标仓库时才包含它；否则改写配置值。绝不要使用插件源或缓存路径：

<!-- zh-CN:end c03b5100b20ec6c0 -->

```text
{{BENNY_CONFIG_PATH}}
```

Trigger:

<!-- zh-CN:begin 168dc99b35b77bfc -->

触发器：

<!-- zh-CN:end 168dc99b35b77bfc -->

```json
{
	"source_channel_id": "{{SLACK_CHANNEL_ID}}",
	"message_ts": "{{SLACK_MESSAGE_TS}}",
	"thread_ts": "{{SLACK_THREAD_TS_OR_EMPTY}}"
}
```

The creation intent should describe this as a new top-level report in the configured source Slack channel.

<!-- zh-CN:begin 20ef2c3e660281df -->

创建意图应描述为在配置的来源 Slack 频道中新建顶层报告。

<!-- zh-CN:end 20ef2c3e660281df -->

Treat the source channel and root thread timestamp as immutable. If either is missing or does not match configuration, stop without posting or writing to the issue tracker.

<!-- zh-CN:begin 4f4ceb4e7d4b1047 -->

把来源频道和根讨论串时间戳视为不可变。任一缺失或与配置不符时，停止，不发帖也不写问题跟踪器。

<!-- zh-CN:end 4f4ceb4e7d4b1047 -->

The committed operational file owns classification, attachment review, cause tracing, routing, dedupe, tracker writes, and the final verdict. Post no progress messages. Never post a root message in the source channel.

<!-- zh-CN:begin 148b2e2116d99b9c -->

已提交的运行文件负责分类、附件审查、原因追踪、路由、去重、跟踪器写入和最终结论。不发进度消息；绝不在来源频道发布根消息。

<!-- zh-CN:end 148b2e2116d99b9c -->

The coordinator is the only Slack poster. Any delegated worker must be read-only, return findings only, and receive an explicit ban on every Slack write action.

<!-- zh-CN:begin e4aa2cdfcd75b29f -->

协调者是唯一能在 Slack 发帖的角色。任何委派工作者必须只读、只返回发现，并被明确禁止所有 Slack 写入操作。

<!-- zh-CN:end e4aa2cdfcd75b29f -->

End the single verdict with exactly one configured marker:

<!-- zh-CN:begin 1fd0f8e21e649407 -->

用恰好一个配置标记结束唯一结论：

<!-- zh-CN:end 1fd0f8e21e649407 -->

```text
[benny:bug]
[benny:performance]
[benny:other]
```

A bug or performance marker may add `tracker=<URL>`.

<!-- zh-CN:begin 91eb546244fe57da -->

bug 或 performance 标记可追加 `tracker=<URL>`。

<!-- zh-CN:end 91eb546244fe57da -->
