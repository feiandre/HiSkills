# Matt Pocock Skills

<!-- zh-CN:begin e2e83ed5dcff4cac -->

# Matt Pocock 技能集

<!-- zh-CN:end e2e83ed5dcff4cac -->

A collection of agent skills (slash commands and behaviors) loaded by Claude Code. Skills are organized into buckets and consumed by per-repo configuration emitted by `/setup-matt-pocock-skills`.

<!-- zh-CN:begin b887a424e534e1dc -->

由 Claude Code 加载的智能体技能集合（斜杠命令与行为）。技能按桶组织，并由 `/setup-matt-pocock-skills` 生成的逐仓库配置使用。

<!-- zh-CN:end b887a424e534e1dc -->

## Language

<!-- zh-CN:begin 1c0f6f001a30c90d -->

## 语言

<!-- zh-CN:end 1c0f6f001a30c90d -->

**Issue tracker**:
The tool that hosts a repo's issues: GitHub Issues, Linear, a local `.scratch/` markdown convention, or similar. Skills like `to-tickets`, `to-spec`, and `triage` read from and write to it.
_Avoid_: backlog manager, backlog backend, issue host

<!-- zh-CN:begin 533f11a3e444206e -->

**Issue tracker（问题跟踪器）**：
托管仓库问题的工具：GitHub Issues、Linear、本地 `.scratch/` Markdown 约定等。`to-tickets`、`to-spec`、`triage` 等技能从它读取并写入。
*避免*：backlog manager、backlog backend、issue host。

<!-- zh-CN:end 533f11a3e444206e -->

**Issue**:
A single tracked unit of work inside an **Issue tracker**: a bug, task, spec, or slice produced by `to-tickets`.
_Avoid_: ticket (use only when quoting external systems that call them tickets, or for a **Decision ticket**, see below)

<!-- zh-CN:begin f1c22aaec13a4eff -->

**Issue（问题）**：
**Issue tracker** 中单个受跟踪工作单元：`to-tickets` 生成的缺陷、任务、规格或切片。
*避免*：ticket（仅在引用称其为 ticket 的外部系统，或下方 **Decision ticket** 时使用）。

<!-- zh-CN:end f1c22aaec13a4eff -->

**Decision ticket**:
A `wayfinder` unit: a child **Issue** of a `wayfinder:map` holding a *question* whose resolution is a decision, not a slice of a build to execute. The **decision** qualifier is what keeps it distinct from an implementation ticket; `wayfinder` introduces the term, then uses "ticket".

<!-- zh-CN:begin a20e38ec11e620bd -->

**Decision ticket（决策工单）**：
`wayfinder` 单元：包含*问题*且解决结果为决定而非可执行构建切片的 `wayfinder:map` 子 **Issue**。**decision** 限定词使它区别于实现工单；`wayfinder` 引入该词，随后使用“ticket”。

<!-- zh-CN:end a20e38ec11e620bd -->

**Triage role**:
A canonical state-machine label applied to an **Issue** during triage (e.g. `needs-triage`, `ready-for-afk`). Each role maps to a real label string in the **Issue tracker** via `docs/agents/triage-labels.md`.

<!-- zh-CN:begin 78d1f13d2dca190b -->

**Triage role（分诊角色）**：
分诊期间应用于 **Issue** 的规范状态机标签（如 `needs-triage`、`ready-for-afk`）。每个角色通过 `docs/agents/triage-labels.md` 映射到 **Issue tracker** 中的真实标签字符串。

<!-- zh-CN:end 78d1f13d2dca190b -->

## Relationships

<!-- zh-CN:begin c4db4e3ad13bc6ba -->

## 关系

<!-- zh-CN:end c4db4e3ad13bc6ba -->

- An **Issue tracker** holds many **Issues**

<!-- zh-CN:begin ecde90704dae6592 -->

- 一个 **Issue tracker** 包含多个 **Issues**

<!-- zh-CN:end ecde90704dae6592 -->
- An **Issue** carries one **Triage role** at a time

<!-- zh-CN:begin 36b7ae40e692dcf9 -->

- 一个 **Issue** 同时携带一个 **Triage role**

<!-- zh-CN:end 36b7ae40e692dcf9 -->
- A **Decision ticket** is an **Issue** (a child of a `wayfinder:map`)

<!-- zh-CN:begin 21627ca0d80e2aac -->

- **Decision ticket** 是一个 **Issue**（`wayfinder:map` 的子项）

<!-- zh-CN:end 21627ca0d80e2aac -->

## Flagged ambiguities

<!-- zh-CN:begin 0c55e8b9a84e3e78 -->

## 已标记的歧义

<!-- zh-CN:end 0c55e8b9a84e3e78 -->

- "backlog" was previously used to mean both the *tool* hosting issues and the *body of work* inside it. Resolved: the tool is the **Issue tracker**; "backlog" is no longer used as a domain term.

<!-- zh-CN:begin 5d3da46a918a250d -->

- “backlog” 以前既指托管问题的*工具*，也指其中的*工作集合*。已解决：工具是 **Issue tracker**；“backlog” 不再是领域术语。

<!-- zh-CN:end 5d3da46a918a250d -->
- "backlog backend" / "backlog manager". Resolved: collapsed into **Issue tracker**.

<!-- zh-CN:begin ac20cf566bb44950 -->

- “backlog backend”／“backlog manager”。已解决：合并为 **Issue tracker**。

<!-- zh-CN:end ac20cf566bb44950 -->
