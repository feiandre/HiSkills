## 子代理派发需要多代理支持

在 Codex 配置（`~/.codex/config.toml`）中加入：

```toml
[features]
multi_agent = true
```

这会启用`dispatching-parallel-agents`和`subagent-driven-development`等技能使用的多代理工具。具体工具取决于模型预设选择的版本（当前预设为V2，旧预设为V1）。工具列表与本表冲突时，以实际工具列表为准。

- **派生：**用`spawn_agent {fork_turns: "none"}`给子代理干净上下文；默认`"all"`会复制整个转录。Codex 0.145+中`~/.codex/agents/`角色文件通过`agent_type`附加到隔离分叉。全历史分叉接受`model`和`reasoning_effort`覆盖（仅拒绝`agent_type`）；隔离分叉是SDD默认，因为上下文卫生，不是因为覆盖才需要。

- **修复轮：**用`followup_task`恢复实现者；它发送消息、触发轮次并透明重载被宿主淘汰的子代理。绝不要以为派生代理无法再收消息就另派新实现者；V2总能继续。

- **生命周期：**V2没有`close_agent`；需要槽位时会自动淘汰已完成子代理，不关闭无成本。只有V1有`close_agent`：审查返回后关闭审查者，任务审查通过后关闭实现者。

- **模型名：**未经当前派生允许列表核对，绝不从技能、表格或旧会话复制模型名到`spawn_agent`；V2只接受支持V2的预设，其余直接报错。

## 等待子代理

`wait_agent`是事件订阅，不是轮询：长等待在子代理产生邮箱活动时立即唤醒，延迟与短等待相同。短超时轮询无收益，每次还消耗工具调用和上下文重复计费。实测约三分之二等待调用短超时。

- 仍有本地工作时不要等待；完成子代理的最终回答会推入邮箱，在下一轮到达。

- 确实空闲且有未完成子代理时，分有界时段等待：`wait_agent`的`timeout_ms`为300000–600000（5–10分钟）。每段唤醒或超时后输出一行状态，运行`list_agents`，追踪未报告就完成的子代理。绝不叠加小于5分钟的轮询；事件订阅同样快速。

- 完成邮件不会唤醒空闲控制器（不触发轮次）；覆盖这个空闲窗口是`wait_agent`唯一职责。超时无活动意味着需核对，不意味着缩短下一段。

## 派生时的模型路由

你发出的每次`spawn_agent`（包括自己作为子代理并行分派）都按当前技能规则明确设置`model`和`reasoning_effort`。只设`model`会落入陷阱：子代理effort静默重置为模型默认，而非父级。

请人类搭档在`~/.codex/config.toml`设置机器级兜底，让遗漏的派生仍进入审慎层级，而不继承会话最贵模型：

```toml
[agents]
default_subagent_model = "<a mid-tier model from your spawn allowlist>"
default_subagent_reasoning_effort = "medium"
```

## 环境检测

创建工作树或收尾分支的技能应先以只读git命令检测环境：

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

- `GIT_DIR != GIT_COMMON`→已在关联工作树（跳过创建）

- `BRANCH`为空→分离HEAD（沙箱内不能建分支、推送或开PR）

具体用法见`using-git-worktrees`第0步和`finishing-a-development-branch`第1步。

## Codex App 收尾

沙箱阻止分支/推送（外部管理工作树中的分离HEAD）时，代理提交全部工作并告知用户使用App原生控件：

- **“Create branch”**——命名分支，然后通过App UI提交、推送、开PR

- **“Hand off to local”**——把工作交给用户本地检出

代理仍可运行测试、暂存文件，并输出建议分支名、提交信息和PR描述供用户复制。
