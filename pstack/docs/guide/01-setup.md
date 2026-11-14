# Set up pstack

<!-- zh-CN:begin a84584d076e1880c -->

# 设置 pstack

<!-- zh-CN:end a84584d076e1880c -->

In this page you install the plugin, pick which models pstack uses, and run your first task. Setup is one command plus a short conversation.

<!-- zh-CN:begin 2ee84505a986ce29 -->

本页安装插件、选择 pstack 使用的模型并运行首个任务。设置只需一条命令和简短对话。

<!-- zh-CN:end 2ee84505a986ce29 -->

## Install the plugin

<!-- zh-CN:begin 759af82198fffe07 -->

## 安装插件

<!-- zh-CN:end 759af82198fffe07 -->

In a Cursor chat, run:

<!-- zh-CN:begin a3cfe870698b2fef -->

在 Cursor 对话中运行：

<!-- zh-CN:end a3cfe870698b2fef -->

```text
/add-plugin pstack
```

Cursor confirms the plugin is installed.

<!-- zh-CN:begin 0f126e1002236352 -->

Cursor 会确认插件安装。

<!-- zh-CN:end 0f126e1002236352 -->

In Claude Code, run `/plugin marketplace add cursor/plugins`, then `/plugin install pstack@cursor-plugins`. Claude Code prefixes plugin commands, so each command in this guide takes a `pstack:` prefix there, such as `/pstack:setup-pstack`, which writes its model rule to `~/.claude/rules/pstack-models.md`. The [Claude Code adapter](../harness/claude-code.md) covers the other differences.

<!-- zh-CN:begin 7e38bc6b08e8e13f -->

在 Claude Code 中运行 `/plugin marketplace add cursor/plugins`，然后 `/plugin install pstack@cursor-plugins`。Claude Code 给插件命令加前缀，因此本指南命令在此处加 `pstack:`，如 `/pstack:setup-pstack`，其模型规则写入 `~/.claude/rules/pstack-models.md`。[Claude Code 适配器](../harness/claude-code.md)说明其他差异。

<!-- zh-CN:end 7e38bc6b08e8e13f -->

## Pick your models

<!-- zh-CN:begin 572d5623187fa935 -->

## 选择模型

<!-- zh-CN:end 572d5623187fa935 -->

Run:

<!-- zh-CN:begin 26c1ea465de90718 -->

运行：

<!-- zh-CN:end 26c1ea465de90718 -->

```text
/setup-pstack
```

[`/setup-pstack`](../../skills/setup-pstack/SKILL.md) detects the models you have access to, asks for a reasoning budget, shows you each role (code delegates, judgment, the review panels), and asks what you want. Answer the questions. It writes `~/.cursor/rules/pstack-models.mdc`, a small rule every pstack skill reads.

<!-- zh-CN:begin e2366967c6b2a086 -->

[`/setup-pstack`](../../skills/setup-pstack/SKILL.md) 检测可访问模型，询问推理预算，展示各角色（代码委派、判断、审查面板）并询问选择。回答后它写入 `~/.cursor/rules/pstack-models.mdc`，所有 pstack 技能读取。

<!-- zh-CN:end e2366967c6b2a086 -->

The defaults run at `xhigh` reasoning, the same as the `large` budget. `unlimited` lifts each model to its highest tier, up to `max`. Opus goes to `max`. Grok tops out at `xhigh`, so it stays there. `medium` and `small` lower the reasoning and spend fewer tokens.

<!-- zh-CN:begin a31e849a2598d337 -->

默认使用 `xhigh` 推理，等同 `large` 预算。`unlimited` 将各模型提升到最高层级，至多 `max`；Opus 到 `max`，Grok 最高 `xhigh`。`medium` 与 `small` 降低推理并减少 token。

<!-- zh-CN:end a31e849a2598d337 -->

You only override what you care about. A role with no line in the rule keeps the skill's default. To restore a default, delete that role's line. A rerun of `/setup-pstack` keeps any role whose model differs from the default. When a default changes, a rule written before the change still pins the old default, so delete those role lines, or delete the file, then run `/setup-pstack` again.

<!-- zh-CN:begin 765e142225bdccfe -->

只覆盖你在意项。规则未列出的角色沿用技能默认；删除角色行即恢复。重跑 `/setup-pstack` 会保留模型不同于默认的角色。默认变化后，旧规则仍固定旧默认；删除那些角色行或文件后重跑 `/setup-pstack`。

<!-- zh-CN:end 765e142225bdccfe -->

You might be wondering what happens if you use Auto. Set a role to `inherit-parent` or `auto` and pstack omits the subagent `model` field, so the subagent inherits your parent chat model. Both values mean the same thing, and neither is a model slug. For a panel role the value is a list, and one subagent runs per entry, so the list length sets the panel size. Setup also configures `swarm workers`, the default model for every `/swarm` worker unless a race names a model for each arm.

<!-- zh-CN:begin faed2a0b4c7b8cf4 -->

使用 Auto 时：将角色设为 `inherit-parent` 或 `auto`，pstack 省略子代理 `model` 字段，子代理继承父对话模型。两值含义相同，均非模型 slug。面板角色值是列表，每项运行一个子代理，列表长度决定面板大小。设置还配置 `swarm workers`，即 `/swarm` 每个工作者的默认模型，除非竞速为各分支指定模型。

<!-- zh-CN:end faed2a0b4c7b8cf4 -->

## Accept the verification offers, or don't

<!-- zh-CN:begin 041c68cd7bd6ce24 -->

## 接受或拒绝验证提议

<!-- zh-CN:end 041c68cd7bd6ce24 -->

At the end of setup, `/setup-pstack` looks for a way to prove app behavior in your project, either a `verify-*` skill or an existing harness. If it finds neither, it offers once to generate one with [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md).

<!-- zh-CN:begin de36591d7b8548ce -->

设置末尾，`/setup-pstack` 寻找证明应用行为的方式：`verify-*` 技能或现有 harness。都没有时，只在这次询问是否用 [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) 生成。

<!-- zh-CN:end de36591d7b8548ce -->

Say yes and it writes `.cursor/skills/verify-<app>/`, a project-local skill that teaches agents to drive your app the way a user does. It proves the skill works once before handing it over. Say no and setup moves on. You can run `/create-verification-skill` yourself any time. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers it in depth.

<!-- zh-CN:begin 4c5f91cbb4cfab6e -->

同意后写入 `.cursor/skills/verify-<app>/`，项目内技能教代理按用户方式驱动应用。交付前先证明技能工作一次。拒绝则继续，可随时自行运行 `/create-verification-skill`。详见[验证与发布](./06-verify-and-ship.md#create-a-project-verification-skill)。

<!-- zh-CN:end 4c5f91cbb4cfab6e -->

If you're new to pstack, say yes. An agent that can check its own work keeps going until the check passes. An agent that can't hands every result back to you to check by hand. Of everything in this guide, the verification skill pays off the most.

<!-- zh-CN:begin ff559a06229ea69a -->

初次使用 pstack 时建议同意。能自检的代理会推进到检查通过；不能者把每个结果交人手查。整个指南中验证技能回报最高。

<!-- zh-CN:end ff559a06229ea69a -->

Then setup offers once to generate a formal verification skill with [`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md), unless the project already has one. Tests check the cases someone thought to write. A formal verification skill checks one key property of your code, such as "a job never runs twice at once", in every case within a stated scope. Say yes when your code has concurrency, retries, a state machine, or a parser, where a bug is costly and tests rarely reach the case that breaks. Otherwise say no, and run it later if that changes. [Verify and ship](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill) covers it.

<!-- zh-CN:begin 1f5d68c100f78ef2 -->

随后设置再询问一次是否用 [`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md) 生成形式验证技能，除非项目已有。测试只覆盖有人想到的情形；形式验证在限定范围检查关键性质，如“任务绝不并发运行两次”。代码有并发、重试、状态机或解析器且错误代价高、测试难覆盖时同意；否则拒绝，变化后再运行。详见[验证与发布](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill)。

<!-- zh-CN:end 1f5d68c100f78ef2 -->

After setup, start a new chat. The model rule applies to new sessions.

<!-- zh-CN:begin 121db1b478913f59 -->

设置后新建对话，模型规则只应用于新会话。

<!-- zh-CN:end 121db1b478913f59 -->

## Keep the cost in check

<!-- zh-CN:begin d4bf190517fa31b2 -->

## 控制成本

<!-- zh-CN:end d4bf190517fa31b2 -->

pstack spends extra tokens on subagents and review panels. That's the price of the rigor. To spend fewer:

<!-- zh-CN:begin 61f053f4d1c1037f -->

pstack 在子代理与审查面板上使用额外 token，这是严格性的价格。减少花费可：

<!-- zh-CN:end 61f053f4d1c1037f -->

- Rerun `/setup-pstack` and pick a smaller reasoning budget or cheaper models. A strong model in the main chat with cheaper, faster models in the code roles is a good split.

<!-- zh-CN:begin eb2a625d3ec2828a -->

- 重跑 `/setup-pstack`，选更小推理预算或更便宜模型。主对话用强模型，代码角色用便宜快速模型是好组合。

<!-- zh-CN:end eb2a625d3ec2828a -->

- Set a role to `auto` or `inherit-parent` so it runs on the chat's own model.

<!-- zh-CN:begin 77a7f4367c6ece67 -->

- 将角色设为 `auto` 或 `inherit-parent`，使用当前对话模型。

<!-- zh-CN:end 77a7f4367c6ece67 -->

- Shorten a panel list. Each entry runs one subagent.

<!-- zh-CN:begin 11b4456b7e961557 -->

- 缩短面板列表，每项一个子代理。

<!-- zh-CN:end 11b4456b7e961557 -->

- Save `/poteto-mode` for work that needs rigor. A small, obvious edit doesn't.

<!-- zh-CN:begin b7ca7581d1ef2467 -->

- 只为需要严格性的工作使用 `/poteto-mode`；小型明显改动无需。

<!-- zh-CN:end b7ca7581d1ef2467 -->

## Run your first task

<!-- zh-CN:begin 97986f82f976862a -->

## 运行首个任务

<!-- zh-CN:end 97986f82f976862a -->

Pick something real but small, and describe it the way you'd describe it to a colleague:

<!-- zh-CN:begin 4fc852ff17033cbe -->

选真实但小的任务，像对同事一样描述：

<!-- zh-CN:end 4fc852ff17033cbe -->

```text
/poteto-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

Watch the todo list. Its first items are the matched playbook's steps copied in, the Feature playbook for this prompt. If `/poteto-mode` skips a step, the step stays in the list with `skip: <reason>`, so you can see what it chose not to do.

<!-- zh-CN:begin 1797444d0274cf16 -->

观察待办列表。前几项是匹配操作手册的复制步骤，此提示对应功能手册。`/poteto-mode` 跳过步骤时仍保留并标 `skip: <reason>`（跳过原因），可看出它选择不做什么。

<!-- zh-CN:end 1797444d0274cf16 -->

From here you can type normal follow-ups. To keep `/poteto-mode` on for the whole chat, pick it from the `/` menu with Option+Enter (Mac) or Alt+Enter (Windows) instead of Enter. That makes it a [Custom Mode](https://cursor.com/docs/skills#using-a-skill-as-a-custom-mode), which stays in context on every turn until you exit it. Custom Modes are available in the Agents Window and the CLI. Plain Enter attaches the skill to one message, and it fades as the chat moves on.

<!-- zh-CN:begin f18c5579dbd15b05 -->

之后可正常追问。若整个对话保持 `/poteto-mode`，在 `/` 菜单用 Option+Enter（Mac）或 Alt+Enter（Windows）选择，而非 Enter。这成为[自定义模式](https://cursor.com/docs/skills#using-a-skill-as-a-custom-mode)，每轮保留直到退出。自定义模式适用于 Agents Window 和 CLI。普通 Enter 只附加到一条消息，随对话推移淡出。

<!-- zh-CN:end f18c5579dbd15b05 -->

Next: [Route work through `/poteto-mode`](./02-poteto-mode.md).

<!-- zh-CN:begin 6a27965d80c13671 -->

下一步：[通过 `/poteto-mode` 路由工作](./02-poteto-mode.md)。

<!-- zh-CN:end 6a27965d80c13671 -->
