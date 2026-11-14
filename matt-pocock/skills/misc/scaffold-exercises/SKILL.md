---
name: scaffold-exercises
description: 创建章节、题目、答案和讲解，并能通过项目 lint 的练习目录结构，包含完整骨架。
---

# 搭建练习骨架

创建能通过 `pnpm ai-hero-cli internal lint` 的练习目录结构，然后使用 `git commit` 提交。

## 目录命名

- **章节**：位于 `exercises/` 内的 `XX-section-name/`（例如 `01-retrieval-skill-building`）。

- **练习**：位于章节内的 `XX.YY-exercise-name/`（例如 `01.03-retrieval-with-bm25`）。

- 章节编号 = `XX`，练习编号 = `XX.YY`。

- 名称使用短横线命名法（小写字母，以连字符分隔）。

## 练习变体

每个练习至少需要以下一个子文件夹：

- `problem/`：带 TODO 的学生工作区。

- `solution/`：参考实现。

- `explainer/`：概念资料，没有 TODO。

创建桩时，除非计划另有指定，默认使用 `explainer/`。

## 必需文件

每个子文件夹（`problem/`、`solution/`、`explainer/`）都需要一个 `readme.md`，要求：

- **非空**（必须有实际内容，即使只有一行标题也可以）。

- 没有失效链接。

创建桩时，创建包含标题和描述的最小 readme：

```md
# 练习标题

在此填写描述
```

如果子文件夹包含代码，还需要至少一行 `main.ts`；但仅创建练习桩时，只包含 `readme.md` 也可以。

## 工作流程

1. **解析计划**：提取章节名、练习名和变体类型。

2. **创建目录**：对每个路径执行 `mkdir -p`。

3. **创建 readme 桩**：每个变体文件夹一个 `readme.md`，包含标题。

4. **运行 lint**：用 `pnpm ai-hero-cli internal lint` 验证。

5. **修正所有错误**：迭代到 lint 通过。

## Lint 规则摘要

检查器（`pnpm ai-hero-cli internal lint`）检查：

- 每个练习具有子文件夹（`problem/`、`solution/`、`explainer/`）。

- `problem/`、`explainer/` 或 `explainer.1/` 至少存在一个。

- 主要子文件夹中存在非空的 `readme.md`。

- 没有 `.gitkeep` 文件。

- 没有 `speaker-notes.md` 文件。

- `readme.md` 中没有失效链接。

- `readme.md` 中没有 `pnpm run exercise` 命令。

- 每个子文件夹都需要 `main.ts`，除非它只有 readme。

## 移动 / 重命名练习

重新编号或移动练习时：

1. 使用 `git mv`（不是 `mv`）重命名目录——保留 git 历史。

2. 更新数字前缀以维持顺序。

3. 移动后重新运行 lint。

例如：

```bash
git mv exercises/01-retrieval/01.03-embeddings exercises/01-retrieval/01.04-embeddings
```

## 示例：根据计划创建桩

假设计划如下：

```
第 05 章：记忆技能构建
- 05.01 记忆简介
- 05.02 短期记忆（讲解 + 题目 + 答案）
- 05.03 长期记忆
```

```bash
mkdir -p exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer
mkdir -p exercises/05-memory-skill-building/05.02-short-term-memory/{explainer,problem,solution}
mkdir -p exercises/05-memory-skill-building/05.03-long-term-memory/explainer
```

然后创建 readme 桩：

```
exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer/readme.md -> "# 记忆简介"
exercises/05-memory-skill-building/05.02-short-term-memory/explainer/readme.md -> "# 短期记忆"
exercises/05-memory-skill-building/05.02-short-term-memory/problem/readme.md -> "# 短期记忆"
exercises/05-memory-skill-building/05.02-short-term-memory/solution/readme.md -> "# 短期记忆"
exercises/05-memory-skill-building/05.03-long-term-memory/explainer/readme.md -> "# 长期记忆"
```
