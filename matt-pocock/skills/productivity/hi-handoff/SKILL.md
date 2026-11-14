---
name: hi-handoff
description: 将当前对话压缩成交接文档，供另一个智能体接手
argument-hint: 下一次会话将用于什?
disable-model-invocation: true
---


编写一份总结当前对话的交接文档，使全新智能体能继续工作。保存到用户操作系统的用户指定的目录或者项目根目录下的`docs/session-docs/` 目录下或者临时目录（`$TMPDIR`，否则 `/tmp`；Windows 用 `%TEMP%`），不是当前工作区。

文档中包括“建议技能”章节，列出下一智能体应使用 Skill 工具调用的技能。

不要重复其他产物（规格文档、计划、ADR、issue、提交、差异）已经包含的内容。通过路径或 URL 引用它们。

如果用户传入参数，将其视为下一次会话重点说明，据此定制文档。

删除 API key、密码或个人身份信息PII等敏感信息。
