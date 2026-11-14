# OpenCode 支持设计

**日期：** 2025-11-22
**作者：** Bot 与 Jesse
**状态：** 设计完成，等待实现

## 概述

使用原生 OpenCode 插件架构，为 OpenCode.ai 添加完整的 Superpowers 支持，并与现有 Codex 实现共享核心功能。

## 背景

OpenCode.ai 是类似 Claude Code 和 Codex 的编码智能体。此前移植 Superpowers 到 OpenCode 的尝试（PR #93、PR #116）采用复制文件的方式。本设计采用不同方案：通过其 JavaScript/TypeScript 插件系统构建原生 OpenCode 插件，同时与 Codex 实现共享代码。

### 平台之间的主要差异

- **Claude Code**：原生 Anthropic 插件系统 + 基于文件的技能

- **Codex**：没有插件系统 → 引导 Markdown + CLI 脚本

- **OpenCode**：带事件钩子和自定义工具 API 的 JavaScript/TypeScript 插件

### OpenCode 的智能体系统

- **主智能体**：Build（默认、完整访问）和 Plan（受限、只读）

- **子智能体**：General（研究、搜索、多步骤任务）

- **调用方式**：由主智能体自动派发，或使用手动 `@mention` 语法

- **配置**：在 `opencode.json` 或 `~/.config/opencode/agent/` 中配置自定义智能体

## 架构

### 高层结构

1. **共享核心模块**（`lib/skills-core.js`）

- 通用技能发现和解析逻辑

- 由 Codex 和 OpenCode 实现共同使用

2. **平台专用包装器**

- Codex：CLI 脚本（`.codex/superpowers-codex`）

- OpenCode：插件模块（`.opencode/plugin/superpowers.js`）

3. **技能目录**

- 核心：`~/.config/opencode/superpowers/skills/`（或安装位置）

- 个人：`~/.config/opencode/skills/`（覆盖核心技能）

### 代码复用策略

从 `.codex/superpowers-codex` 提取通用功能到共享模块：

```javascript
module.exports = {
  extractFrontmatter(filePath),
  findSkillsInDir(dir, maxDepth),
  findAllSkills(dirs),
  resolveSkillPath(skillName, dirs),
  checkForUpdates(repoDir)
};
```

### 技能前置元数据格式

当前格式（没有 `when_to_use` 字段）：

```yaml
---
name: skill-name
description: 在[条件]时使用 - [它做什么]；[补充背景]
---
```

## OpenCode 插件实现

### 自定义工具

**工具 1：`use_skill`**

把指定技能内容加载到对话中（相当于 Claude 的 Skill 工具）。

```javascript
{
  name: 'use_skill',
  description: '加载并阅读指定技能以指导工作',
  schema: z.object({
    skill_name: z.string().describe('技能名称（例如 "superpowers:brainstorming"）')
  }),
  execute: async ({ skill_name }) => {
    const { skillPath, content, frontmatter } = resolveAndReadSkill(skill_name);
    const skillDir = path.dirname(skillPath);

    return `# ${frontmatter.name}
# ${frontmatter.description}
# 支持工具和文档位于 ${skillDir}
# ============================================

${content}`;
  }
}
```

**工具 2：`find_skills`**

列出所有可用技能及其元数据。

```javascript
{
  name: 'find_skills',
  description: '列出所有可用技能',
  schema: z.object({}),
  execute: async () => {
    const skills = discoverAllSkills();
    return skills.map(s =>
      `${s.namespace}:${s.name}
  ${s.description}
  目录：${s.directory}
`).join('\n');
  }
}
```

### 会话启动钩子

新会话开始时（`session.started` 事件）：

1. **注入 using-superpowers 内容**

- using-superpowers 技能的完整内容

- 建立强制工作流

2. **自动运行 find_skills**

- 预先显示全部可用技能列表

- 为每项包含技能目录

3. **注入工具映射说明**

```markdown
   **OpenCode 的工具映射：**
   技能引用你没有的工具时，替换为：
   - `TodoWrite` → `update_plan`
   - 带子智能体的 `Task` → 使用 OpenCode 子智能体系统（@mention）
   - `Skill` 工具 → `use_skill` 自定义工具
   - Read、Write、Edit、Bash → 你的原生等价工具

   **技能目录包含：**
   - 支持脚本（用 bash 运行）
   - 补充文档（用 read 工具读取）
   - 该技能专用工具
   ```

4. **检查更新**（非阻塞）

- 带超时的快速 git fetch

- 有更新时通知

### 插件结构

```javascript
const skillsCore = require('../../lib/skills-core');
const path = require('path');
const fs = require('fs');
const { z } = require('zod');

export const SuperpowersPlugin = async ({ client, directory, $ }) => {
  const superpowersDir = path.join(process.env.HOME, '.config/opencode/superpowers');
  const personalDir = path.join(process.env.HOME, '.config/opencode/skills');

  return {
    'session.started': async () => {
      const usingSuperpowers = await readSkill('using-superpowers');
      const skillsList = await findAllSkills();
      const toolMapping = getToolMappingInstructions();

      return {
        context: `${usingSuperpowers}\n\n${skillsList}\n\n${toolMapping}`
      };
    },

    tools: [
      {
        name: 'use_skill',
        description: '加载并阅读指定技能',
        schema: z.object({
          skill_name: z.string()
        }),
        execute: async ({ skill_name }) => {
        }
      },
      {
        name: 'find_skills',
        description: '列出所有可用技能',
        schema: z.object({}),
        execute: async () => {
        }
      }
    ]
  };
};
```

## 文件结构

```
superpowers/
├── lib/
│   └── skills-core.js           # 新增：共享技能逻辑
├── .codex/
│   ├── superpowers-codex        # 更新：使用 skills-core
│   ├── superpowers-bootstrap.md
│   └── INSTALL.md
├── .opencode/
│   ├── plugin/
│   │   └── superpowers.js       # 新增：OpenCode 插件
│   └── INSTALL.md               # 新增：安装指南
└── skills/                       # 不变
```

## 实现计划

### 阶段 1：重构共享核心

1. 创建 `lib/skills-core.js`

- 从 `.codex/superpowers-codex` 提取前置元数据解析

- 提取技能发现逻辑

- 提取路径解析（含覆盖关系）

- 只使用 `name` 和 `description`（不用 `when_to_use`）

2. 更新 `.codex/superpowers-codex` 使用共享核心

- 从 `../lib/skills-core.js` 导入

- 移除重复代码

- 保留 CLI 包装逻辑

3. 测试 Codex 实现仍然有效

- 验证引导命令

- 验证 use-skill 命令

- 验证 find-skills 命令

### 阶段 2：构建 OpenCode 插件

1. 创建 `.opencode/plugin/superpowers.js`

- 从 `../../lib/skills-core.js` 导入共享核心

- 实现插件函数

- 定义自定义工具（use_skill、find_skills）

- 实现 session.started 钩子

2. 创建 `.opencode/INSTALL.md`

- 安装说明

- 目录设置

- 配置指导

3. 测试 OpenCode 实现

- 验证会话启动引导

- 验证 use_skill 工具有效

- 验证 find_skills 工具有效

- 验证技能目录可访问

### 阶段 3：文档与收尾

1. 更新 README，加入 OpenCode 支持

2. 在主文档中添加 OpenCode 安装说明

3. 更新 RELEASE-NOTES

4. 测试 Codex 和 OpenCode 都正常工作

## 后续步骤

1. **创建隔离工作区**（使用 Git 工作树）

- 分支：`feature/opencode-support`

2. **在适用处遵循 TDD**

- 测试共享核心函数

- 测试技能发现和解析

- 两个平台的集成测试

3. **增量实现**

- 阶段 1：重构共享核心并更新 Codex

- 继续前验证 Codex 仍有效

- 阶段 2：构建 OpenCode 插件

- 阶段 3：文档和收尾

4. **测试策略**

- 使用真实 OpenCode 安装进行人工测试

- 验证技能加载、目录和脚本有效

- 并排测试 Codex 和 OpenCode

- 验证工具映射正确

5. **PR 与合并**

- 用完整实现创建 PR

- 在干净环境测试

- 合并到 main

## 收益

- **代码复用**：技能发现／解析只有一个事实来源

- **可维护性**：缺陷修复同时适用于两个平台

- **可扩展性**：便于添加未来平台（Cursor、Windsurf 等）

- **原生集成**：正确使用 OpenCode 插件系统

- **一致性**：所有平台提供相同技能体验
