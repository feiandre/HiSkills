---
name: finishing-a-development-branch
description: 实现已经完成、所有测试均通过，并且需要决定如何集成工作成果时使用。
---

# 完成开发分支

## 概述

**核心原则：** 验证测试 → 检测环境 → 提供选项 → 执行选择 → 清理。

**开始时声明：** “我正在使用 finishing-a-development-branch 技能来完成这项工作。”

## 步骤 1：验证测试

运行项目的完整测试套件（`npm test` / `cargo test` / `pytest` / `go test ./...`）。

**如果测试失败，** 报告失败并停下；只有套件全绿后才提供菜单：

```
测试失败（<N> 项失败）。完成工作前必须修复：

[显示失败信息]
```

**如果测试通过：** 继续步骤 2。

## 步骤 2：检测环境

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
WORKTREE_PATH=$(git rev-parse --show-toplevel)
```

这决定显示哪种菜单以及如何清理：

| 状态 | 菜单 | 清理 |
|-------|------|---------|
| `GIT_DIR == GIT_COMMON`（普通仓库） | 标准 3 个选项 | 无需清理 worktree |
| `GIT_DIR != GIT_COMMON`，具名分支 | 标准 3 个选项 | 根据来源处理，见步骤 6 |
| `GIT_DIR != GIT_COMMON`，detached HEAD | 精简为 2 个选项，不提供合并 | 由外部管理，保持原位 |

## 步骤 3：确定基准分支

基准分支就是本次工作从中分出的分支，通常在计划、对话或分支的 upstream 中注明。如果尚不明确，应询问：“这个分支是从 <your best guess> 分出来的，对吗？”合并之前必须确认：合并到错误的基准分支，撤销代价很高。

## 步骤 4：提供选项

**普通仓库和具名分支的 worktree：严格提供以下 3 个选项：**

```
实现已完成。你希望如何处理？

1. 在本地合并回 <base-branch>
2. 推送并创建 Pull Request
3. 保持分支现状（我稍后自行处理）

选择哪一项？
```

**detached HEAD：严格提供以下 2 个选项：**

```
实现已完成。你目前位于 detached HEAD（由外部管理的工作区）。

1. 推送为新分支并创建 Pull Request
2. 保持现状（我稍后自行处理）

选择哪一项？
```

严格按给定内容展示菜单，保持简洁，所有选项都来自上述列表。只有人类搭档明确要求丢弃工作时，才能丢弃，见下方“如果人类搭档要求丢弃工作”。等待他们回答；集成决定属于他们。

## 步骤 5：执行选择

### 选项 1：在本地合并

```bash
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"
git checkout <base-branch>
git pull
git merge <feature-branch>
<test command>
```

如果合并结果上的测试失败：停下，保留 worktree 和分支并调查。尚未推送任何内容，所以这次合并仍在本地，可以恢复。

合并结果全绿后，清理 worktree（步骤 6），然后删除分支：

```bash
git branch -d <feature-branch>
```

### 选项 2：推送并创建 PR

```bash
git push -u origin <feature-branch>
```

然后使用代码托管平台的工具，针对 <base-branch> 创建 pull/merge request；有 CLI 就使用 CLI，否则使用大多数平台在推送时打印的创建链接。如果仓库有 PR 模板和约定，就遵循它们，并将 URL 告知人类搭档。

保留 worktree，人类搭档会在那里迭代处理 PR 反馈。

### 选项 3：保持现状

报告：“保留分支 <name>。Worktree 保留在 <path>。”

### 如果人类搭档要求丢弃工作

只有在收到明确要求丢弃工作的请求后，才进入这条路径。先确认：

```
这将永久删除：
- 分支 <name>
- 所有提交：<commit-list>
- 位于 <path> 的 worktree

输入 'discard' 以确认。
```

等待该确切确认词。收到后：

```bash
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"
```

然后清理 worktree（步骤 6），并强制删除分支：

```bash
git branch -D <feature-branch>
```

## 步骤 6：清理工作区

**适用于选项 1 和已确认的丢弃操作。** 选项 2 和 3 始终保留 worktree。两种调用路径都已将目录切换到主仓库根目录，因为移除 worktree 必须在 worktree 之外执行；使用步骤 2 中、切换目录之前保存的 `GIT_DIR`、`GIT_COMMON` 和 `WORKTREE_PATH` 值。

**如果 `GIT_DIR == GIT_COMMON`：** 这是普通仓库，没有要清理的 worktree。完成。

**如果 `WORKTREE_PATH` 位于 `.worktrees/` 或 `worktrees/` 之下：** 该 worktree 由 Superpowers 创建，我们负责清理：

```bash
git worktree remove "$WORKTREE_PATH"
git worktree prune  # 自我修复：清理任何过期注册信息
```

**如果拒绝移除**（`contains modified or untracked files`）：worktree 中含有其他地方不存在的文件，例如未提交的计划、笔记或临时工作。绝不擅自使用 `--force`。向人类搭档展示可能失去的内容，并询问：

```bash
git -C "$WORKTREE_PATH" status --porcelain -uall
```

```
Worktree 移除被拒绝，以下文件从未提交：

<file list>

1. 清理前先把它们提交到 <branch>
2. 将它们移入 <main repo root>
3. 删除它们（不可恢复）

选择哪一项？
```

执行所选操作，再移除 worktree。

**其他情况：** 该工作区归宿主环境管理，应保留原位。如果平台提供工作区退出工具，则使用该工具。

## 快速参考

| 选项 | 合并 | 推送 | 保留 Worktree | 清理分支 |
|--------|-------|------|---------------|----------------|
| 1. 本地合并 | 是 | - | - | 是 |
| 2. 创建 PR | - | 是 | 是 | - |
| 3. 保持现状 | - | - | 是 | - |
| 丢弃，仅限明确请求 | - | - | - | 是，强制删除 |

## 常见的自我辩解

| 借口 | 实际情况 |
|--------|---------|
| “本会话前面测试已经通过” | 在即将集成的那份代码树上运行套件。一次全绿只证明运行时的那份代码树。 |
| “他们显然希望合并” | 集成由人类搭档决定。展示菜单并等待。 |
| “他们好像已经不需要这个功能了，我来提议丢弃” | 按给定内容展示的菜单已经完整。只有人类搭档明确说出要求，才能丢弃。 |
| “‘好，把它处理掉’就算确认” | 只有输入 `discard` 才授权删除。 |
| “PR 已经建好，worktree 现在只是杂物” | PR 反馈应在该 worktree 中修复。工作落地前必须保留它。 |
| “这个别的 worktree 看起来过期了，我也清一下” | 只清理 `.worktrees/` 或 `worktrees/` 下的 worktree。其他一切归宿主管理。 |
| “移除被拒，`--force` 只是把清理做完” | 拒绝意味着有文件只存在于该 worktree。`--force` 会永久销毁它们。向人类搭档展示并询问。 |
| “合并结果的失败大概只是偶发” | 合并结果失败就应停止所有操作。调查期间保留分支和 worktree。 |
| “基准分支显然是 main” | 确认分叉点，或询问。合并到错误基准分支，撤销代价很高。 |
| “推送被拒，强制推送就能解决” | 推送被拒意味着远程已发生变化。先调查；只有人类搭档明确要求，才能强制推送。 |
