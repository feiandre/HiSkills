# Renaming skills to dodge harness built-in commands

<!-- zh-CN:begin 290abc366aadb9d6 -->

# 为避免运行环境内建命令而重命名技能

<!-- zh-CN:end 290abc366aadb9d6 -->

Skill names are not changed because a harness ships a built-in command or skill with the same name (`/prototype`, `/research`, `/code-review`, and so on). Requests to rename a skill, or add an alias, to avoid a collision are out of scope.

<!-- zh-CN:begin 53588e5c5c71e35b -->

不因运行环境自带同名命令或技能（`/prototype`、`/research`、`/code-review` 等）而改变技能名称。为避免冲突而重命名技能或添加别名的请求不在范围内。

<!-- zh-CN:end 53588e5c5c71e35b -->

## Why this is out of scope

<!-- zh-CN:begin c89cc777ac26283f -->

## 为什么不在范围内

<!-- zh-CN:end c89cc777ac26283f -->

Harnesses add built-ins all the time, and each harness picks its own names. Renaming every time one of them lands on a name we already use would mean chasing a moving target across Claude Code, Copilot, Devin and the rest, and breaking every user's muscle memory and every cross-reference between skills each time.

<!-- zh-CN:begin 1186540d78cde79e -->

运行环境不断添加内建功能，每个环境又使用自己的名称。每次某个环境碰到我们已用的名称就改名，就会在 Claude Code、Copilot、Devin 等环境间追逐移动目标，并破坏每个用户的操作记忆和技能之间的所有交叉引用。

<!-- zh-CN:end 1186540d78cde79e -->

How a harness resolves two things with the same name is the harness's behaviour, not the skill's. The skill text is correct either way.

<!-- zh-CN:begin 6f9b1f994e3a0846 -->

运行环境如何解析两个同名内容属于运行环境的行为，不属于技能。技能文本在两种情况下都正确。

<!-- zh-CN:end 6f9b1f994e3a0846 -->

The way through is namespaced invocation. The Claude Code plugin exposes every skill under its plugin name, so you can always reach ours explicitly:

<!-- zh-CN:begin fdfa920c13a56ae7 -->

解决办法是命名空间调用。Claude Code 插件在插件名下公开所有技能，因此始终可显式访问我们的技能：

<!-- zh-CN:end fdfa920c13a56ae7 -->

```
/mattpocock-skills:research
/mattpocock-skills:code-review
```

<!-- zh-CN:begin f8c6eed6df0dc8d7 -->

```
# 通过插件命名空间显式调用技能
/mattpocock-skills:research
/mattpocock-skills:code-review
```

<!-- zh-CN:end f8c6eed6df0dc8d7 -->

If you installed with skills.sh, the files are yours: rename the folder and the `name:` field in your copy.

<!-- zh-CN:begin f59c430ce2533f3d -->

如果通过 skills.sh 安装，文件属于你：在你的副本中重命名文件夹及 `name:` 字段。

<!-- zh-CN:end f59c430ce2533f3d -->

If a harness gives you no way to reach a namespaced or renamed skill at all, report that to the harness.

<!-- zh-CN:begin 467f33c4ab444c46 -->

如果运行环境完全无法访问命名空间或重命名后的技能，请向该运行环境的项目报告。

<!-- zh-CN:end 467f33c4ab444c46 -->

## Prior requests

<!-- zh-CN:begin 8c0edb768fd08e76 -->

## 此前请求

<!-- zh-CN:end 8c0edb768fd08e76 -->

- #423: "/code-review shadows Claude Code own review skill"

<!-- zh-CN:begin 48882ed6860c13a7 -->

- #423：“/code-review 遮蔽 Claude Code 自带审查技能”

<!-- zh-CN:end 48882ed6860c13a7 -->
- #483: "/code-review name clash with Claude Code built-in"

<!-- zh-CN:begin 116cf22263e64538 -->

- #483：“/code-review 名称与 Claude Code 内建功能冲突”

<!-- zh-CN:end 116cf22263e64538 -->
- #857: "Rename the research skill to avoid conflict with Copilot's built-in /research command"

<!-- zh-CN:begin 5d26acd9f4bbe011 -->

- #857：“重命名 research 技能，避免与 Copilot 内建 /research 命令冲突”

<!-- zh-CN:end 5d26acd9f4bbe011 -->
- #1019: "Shorthand `/prototype` conflicts with hidden new Claude Code built-in skill `/prototype`"

<!-- zh-CN:begin e7db6305d3dad6a1 -->

- #1019：“简写 `/prototype` 与隐藏的新 Claude Code 内建技能 `/prototype` 冲突”

<!-- zh-CN:end e7db6305d3dad6a1 -->
- #1037: "Skill name overlap with devin cli inbuilt commands"

<!-- zh-CN:begin 89655d2185bbe519 -->

- #1037：“技能名称与 devin cli 内建命令重叠”

<!-- zh-CN:end 89655d2185bbe519 -->
