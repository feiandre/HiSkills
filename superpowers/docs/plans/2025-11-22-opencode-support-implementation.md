# OpenCode 支持实现计划

> **面向代理工作者：**必需的子技能：使用 superpowers:executing-plans 逐项任务实施此计划。

**目标：**通过原生 JavaScript 插件为 OpenCode.ai 添加完整的 superpowers 支持，并与现有 Codex 实现共享核心功能。

**架构：**将通用的技能发现和解析逻辑提取到 `lib/skills-core.js`，重构 Codex 以使用它，然后利用 OpenCode 原生插件 API、自定义工具和会话钩子构建 OpenCode 插件。

**技术栈：**Node.js、JavaScript、OpenCode Plugin API、Git 工作树

## 阶段 1：创建共享核心模块

### 任务 1：提取 frontmatter 解析

**文件：**

- 创建：`lib/skills-core.js`

- 参考：`.codex/superpowers-codex`（第 40-74 行）

**步骤 1：创建包含 extractFrontmatter 函数的 lib/skills-core.js**

```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');


function extractFrontmatter(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        const lines = content.split('\n');

        let inFrontmatter = false;
        let name = '';
        let description = '';

        for (const line of lines) {
            if (line.trim() === '---') {
                if (inFrontmatter) break;
                inFrontmatter = true;
                continue;
            }

            if (inFrontmatter) {
                const match = line.match(/^(\w+):\s*(.*)$/);
                if (match) {
                    const [, key, value] = match;
                    switch (key) {
                        case 'name':
                            name = value.trim();
                            break;
                        case 'description':
                            description = value.trim();
                            break;
                    }
                }
            }
        }

        return { name, description };
    } catch (error) {
        return { name: '', description: '' };
    }
}

module.exports = {
    extractFrontmatter
};
```

**步骤 2：验证文件已创建**

运行：`ls -l lib/skills-core.js`
预期：文件存在

**步骤 3：提交**

```bash
git add lib/skills-core.js
git commit -m "feat: 创建包含 frontmatter 解析器的共享技能核心模块"
```

### 任务 2：提取技能发现逻辑

**文件：**

- 修改：`lib/skills-core.js`

- 参考：`.codex/superpowers-codex`（第 97-136 行）

**步骤 1：向 skills-core.js 添加 findSkillsInDir 函数**

在 `module.exports` 前添加：

```javascript

function findSkillsInDir(dir, sourceType, maxDepth = 3) {
    const skills = [];

    if (!fs.existsSync(dir)) return skills;

    function recurse(currentDir, depth) {
        if (depth > maxDepth) return;

        const entries = fs.readdirSync(currentDir, { withFileTypes: true });

        for (const entry of entries) {
            const fullPath = path.join(currentDir, entry.name);

            if (entry.isDirectory()) {
                const skillFile = path.join(fullPath, 'SKILL.md');
                if (fs.existsSync(skillFile)) {
                    const { name, description } = extractFrontmatter(skillFile);
                    skills.push({
                        path: fullPath,
                        skillFile: skillFile,
                        name: name || entry.name,
                        description: description || '',
                        sourceType: sourceType
                    });
                }
                recurse(fullPath, depth + 1);
            }
        }
    }

    recurse(dir, 0);
    return skills;
}
```

**步骤 2：更新 module.exports**

将导出行替换为：

```javascript
module.exports = {
    extractFrontmatter,
    findSkillsInDir
};
```

**步骤 3：验证语法**

运行：`node -c lib/skills-core.js`
预期：无输出（成功）

**步骤 4：提交**

```bash
git add lib/skills-core.js
git commit -m "feat: 为核心模块添加技能发现函数"
```

### 任务 3：提取技能解析逻辑

**文件：**

- 修改：`lib/skills-core.js`

- 参考：`.codex/superpowers-codex`（第 212-280 行）

**步骤 1：添加 resolveSkillPath 函数**

在 `module.exports` 前添加：

```javascript

function resolveSkillPath(skillName, superpowersDir, personalDir) {
    const forceSuperpowers = skillName.startsWith('superpowers:');
    const actualSkillName = forceSuperpowers ? skillName.replace(/^superpowers:/, '') : skillName;
    if (!forceSuperpowers && personalDir) {
        const personalPath = path.join(personalDir, actualSkillName);
        const personalSkillFile = path.join(personalPath, 'SKILL.md');
        if (fs.existsSync(personalSkillFile)) {
            return {
                skillFile: personalSkillFile,
                sourceType: 'personal',
                skillPath: actualSkillName
            };
        }
    }
    if (superpowersDir) {
        const superpowersPath = path.join(superpowersDir, actualSkillName);
        const superpowersSkillFile = path.join(superpowersPath, 'SKILL.md');
        if (fs.existsSync(superpowersSkillFile)) {
            return {
                skillFile: superpowersSkillFile,
                sourceType: 'superpowers',
                skillPath: actualSkillName
            };
        }
    }

    return null;
}
```

**步骤 2：更新 module.exports**

```javascript
module.exports = {
    extractFrontmatter,
    findSkillsInDir,
    resolveSkillPath
};
```

**步骤 3：验证语法**

运行：`node -c lib/skills-core.js`
预期：无输出

**步骤 4：提交**

```bash
git add lib/skills-core.js
git commit -m "feat: 添加支持遮蔽的技能路径解析"
```

### 任务 4：提取更新检查逻辑

**文件：**

- 修改：`lib/skills-core.js`

- 参考：`.codex/superpowers-codex`（第 16-38 行）

**步骤 1：添加 checkForUpdates 函数**

在顶部的 require 语句之后添加：

```javascript
const { execSync } = require('child_process');
```

在 `module.exports` 前添加：

```javascript

function checkForUpdates(repoDir) {
    try {
        const output = execSync('git fetch origin && git status --porcelain=v1 --branch', {
            cwd: repoDir,
            timeout: 3000,
            encoding: 'utf8',
            stdio: 'pipe'
        });
        const statusLines = output.split('\n');
        for (const line of statusLines) {
            if (line.startsWith('## ') && line.includes('[behind ')) {
                return true;
            }
        }
        return false;
    } catch (error) {
        return false;
    }
}
```

**步骤 2：更新 module.exports**

```javascript
module.exports = {
    extractFrontmatter,
    findSkillsInDir,
    resolveSkillPath,
    checkForUpdates
};
```

**步骤 3：验证语法**

运行：`node -c lib/skills-core.js`
预期：无输出

**步骤 4：提交**

```bash
git add lib/skills-core.js
git commit -m "feat: 为核心模块添加 git 更新检查"
```

## 阶段 2：重构 Codex 以使用共享核心

### 任务 5：更新 Codex 以导入共享核心

**文件：**

- 修改：`.codex/superpowers-codex`（在顶部添加导入）

**步骤 1：添加导入语句**

在文件顶部现有的 require 语句之后（约第 6 行）添加：

```javascript
const skillsCore = require('../lib/skills-core');
```

**步骤 2：验证语法**

运行：`node -c .codex/superpowers-codex`
预期：无输出

**步骤 3：提交**

```bash
git add .codex/superpowers-codex
git commit -m "refactor: 在 codex 中导入共享技能核心"
```

### 任务 6：用核心版本替换 extractFrontmatter

**文件：**

- 修改：`.codex/superpowers-codex`（第 40-74 行）

**步骤 1：删除本地 extractFrontmatter 函数**

删除第 40-74 行（整个 extractFrontmatter 函数定义）。

**步骤 2：更新所有 extractFrontmatter 调用**

查找并将所有调用从 `extractFrontmatter(` 替换为 `skillsCore.extractFrontmatter(`

受影响行大约为：90、310

**步骤 3：验证脚本仍正常工作**

运行：`.codex/superpowers-codex find-skills | head -20`
预期：显示技能列表

**步骤 4：提交**

```bash
git add .codex/superpowers-codex
git commit -m "refactor: 在 codex 中使用共享 extractFrontmatter"
```

### 任务 7：用核心版本替换 findSkillsInDir

**文件：**

- 修改：`.codex/superpowers-codex`（约第 97-136 行）

**步骤 1：删除本地 findSkillsInDir 函数**

删除整个 `findSkillsInDir` 函数定义（约第 97-136 行）。

**步骤 2：更新所有 findSkillsInDir 调用**

将调用从 `findSkillsInDir(` 替换为 `skillsCore.findSkillsInDir(`

**步骤 3：验证脚本仍正常工作**

运行：`.codex/superpowers-codex find-skills | head -20`
预期：显示技能列表

**步骤 4：提交**

```bash
git add .codex/superpowers-codex
git commit -m "refactor: 在 codex 中使用共享 findSkillsInDir"
```

### 任务 8：用核心版本替换 checkForUpdates

**文件：**

- 修改：`.codex/superpowers-codex`（约第 16-38 行）

**步骤 1：删除本地 checkForUpdates 函数**

删除整个 `checkForUpdates` 函数定义。

**步骤 2：更新所有 checkForUpdates 调用**

将调用从 `checkForUpdates(` 替换为 `skillsCore.checkForUpdates(`

**步骤 3：验证脚本仍正常工作**

运行：`.codex/superpowers-codex bootstrap | head -50`
预期：显示引导内容

**步骤 4：提交**

```bash
git add .codex/superpowers-codex
git commit -m "refactor: 在 codex 中使用共享 checkForUpdates"
```

## 阶段 3：构建 OpenCode 插件

### 任务 9：创建 OpenCode 插件目录结构

**文件：**

- 创建：`.opencode/plugin/superpowers.js`

**步骤 1：创建目录**

运行：`mkdir -p .opencode/plugin`

**步骤 2：创建基础插件文件**

```javascript
#!/usr/bin/env node



const skillsCore = require('../../lib/skills-core');
const path = require('path');
const fs = require('fs');
const os = require('os');

const homeDir = os.homedir();
const superpowersSkillsDir = path.join(homeDir, '.config/opencode/superpowers/skills');
const personalSkillsDir = path.join(homeDir, '.config/opencode/skills');


export const SuperpowersPlugin = async ({ project, client, $, directory, worktree }) => {
  return {
  };
};
```

**步骤 3：验证文件已创建**

运行：`ls -l .opencode/plugin/superpowers.js`
预期：文件存在

**步骤 4：提交**

```bash
git add .opencode/plugin/superpowers.js
git commit -m "feat: 创建 opencode 插件骨架"
```

### 任务 10：实现 use_skill 工具

**文件：**

- 修改：`.opencode/plugin/superpowers.js`

**步骤 1：添加 use_skill 工具实现**

将插件的 return 语句替换为：

```javascript
export const SuperpowersPlugin = async ({ project, client, $, directory, worktree }) => {
  const { z } = await import('zod');

  return {
    tools: [
      {
        name: 'use_skill',
        description: '加载并读取指定技能来指导工作。技能包含经过验证的工作流、强制流程和专家技巧。',
        schema: z.object({
          skill_name: z.string().describe('要加载的技能名称（例如 "superpowers:brainstorming" 或 "my-custom-skill"）')
        }),
        execute: async ({ skill_name }) => {
          const resolved = skillsCore.resolveSkillPath(
            skill_name,
            superpowersSkillsDir,
            personalSkillsDir
          );

          if (!resolved) {
            return `Error: Skill "${skill_name}" not found.\n\nRun find_skills to see available skills.`;
          }
          const fullContent = fs.readFileSync(resolved.skillFile, 'utf8');
          const { name, description } = skillsCore.extractFrontmatter(resolved.skillFile);
          const lines = fullContent.split('\n');
          let inFrontmatter = false;
          let frontmatterEnded = false;
          const contentLines = [];

          for (const line of lines) {
            if (line.trim() === '---') {
              if (inFrontmatter) {
                frontmatterEnded = true;
                continue;
              }
              inFrontmatter = true;
              continue;
            }

            if (frontmatterEnded || !inFrontmatter) {
              contentLines.push(line);
            }
          }

          const content = contentLines.join('\n').trim();
          const skillDirectory = path.dirname(resolved.skillFile);
          return `# ${name || skill_name}
# ${description || ''}
# 配套工具和文档位于 ${skillDirectory}
# ============================================

${content}`;
        }
      }
    ]
  };
};
```

**步骤 2：验证语法**

运行：`node -c .opencode/plugin/superpowers.js`
预期：无输出

**步骤 3：提交**

```bash
git add .opencode/plugin/superpowers.js
git commit -m "feat: implement use_skill tool for opencode"
```

### 任务 11：实现 find_skills 工具

**文件：**

- 修改：`.opencode/plugin/superpowers.js`

**步骤 1：将 find_skills 工具加入 tools 数组**

在 use_skill 工具定义之后、关闭 tools 数组之前加入：

```javascript
      {
        name: 'find_skills',
        description: '列出 superpowers 与个人技能库中的全部可用技能。',
        schema: z.object({}),
        execute: async () => {
          const superpowersSkills = skillsCore.findSkillsInDir(
            superpowersSkillsDir,
            'superpowers',
            3
          );
          const personalSkills = skillsCore.findSkillsInDir(
            personalSkillsDir,
            'personal',
            3
          );
          const allSkills = [...personalSkills, ...superpowersSkills];

          if (allSkills.length === 0) {
            return '未找到技能。请将 superpowers 技能安装到 ~/.config/opencode/superpowers/skills/';
          }

          let output = 'Available skills:\n\n';

          for (const skill of allSkills) {
            const namespace = skill.sourceType === 'personal' ? '' : 'superpowers:';
            const skillName = skill.name || path.basename(skill.path);

            output += `${namespace}${skillName}\n`;
            if (skill.description) {
              output += `  ${skill.description}\n`;
            }
            output += `  Directory: ${skill.path}\n\n`;
          }

          return output;
        }
      }
```

**步骤 2：验证语法**

运行：`node -c .opencode/plugin/superpowers.js`
预期：无输出

**步骤 3：提交**

```bash
git add .opencode/plugin/superpowers.js
git commit -m "feat: implement find_skills tool for opencode"
```

### 任务 12：实现会话开始 hook

**文件：**

- 修改：`.opencode/plugin/superpowers.js`

**步骤 1：加入 session.started hook**

在 tools 数组之后加入：

```javascript
    'session.started': async () => {
      const usingSuperpowersPath = skillsCore.resolveSkillPath(
        'using-superpowers',
        superpowersSkillsDir,
        personalSkillsDir
      );

      let usingSuperpowersContent = '';
      if (usingSuperpowersPath) {
        const fullContent = fs.readFileSync(usingSuperpowersPath.skillFile, 'utf8');
        const lines = fullContent.split('
');
        let inFrontmatter = false;
        let frontmatterEnded = false;
        const contentLines = [];

        for (const line of lines) {
          if (line.trim() === '---') {
            if (inFrontmatter) {
              frontmatterEnded = true;
              continue;
            }
            inFrontmatter = true;
            continue;
          }

          if (frontmatterEnded || !inFrontmatter) {
            contentLines.push(line);
          }
        }

        usingSuperpowersContent = contentLines.join('
').trim();
      }
      const toolMapping = `
**OpenCode 工具映射：**
技能引用你未拥有的工具时，使用 OpenCode 等价工具：
- \`TodoWrite\` → \`update_plan\`（你的规划／任务跟踪工具）
- 带子代理的 \`Task\` 工具 → 使用 OpenCode 子代理系统（@mention 语法或自动分派）
- \`Skill\` 工具 → \`use_skill\` 自定义工具（已可用）
- \`Read\`、\`Write\`、\`Edit\`、\`Bash\` → 使用你的原生工具

**技能目录包含支持文件：**
- 可用 bash 工具运行的脚本
- 可读取的附加文档
- 该技能专用工具与辅助程序

**技能命名：**
- Superpowers 技能：\`superpowers:skill-name\`（来自 ~/.config/opencode/superpowers/skills/）
- 个人技能：\`skill-name\`（来自 ~/.config/opencode/skills/）
- 名称相同时个人技能覆盖 superpowers 技能
`;
      const hasUpdates = skillsCore.checkForUpdates(
        path.join(homeDir, '.config/opencode/superpowers')
      );

      const updateNotice = hasUpdates ?
        '

⚠️ **有可用更新！** 运行 `cd ~/.config/opencode/superpowers && git pull` 更新 superpowers。' :
        '';
      return {
        context: `<EXTREMELY_IMPORTANT>
你拥有 superpowers。

**以下是你的 'superpowers:using-superpowers' 技能完整内容——使用技能的入门说明。其他技能请使用 'use_skill' 工具：**

${usingSuperpowersContent}

${toolMapping}${updateNotice}
</EXTREMELY_IMPORTANT>`
      };
    }
```

**步骤 2：验证语法**

运行：`node -c .opencode/plugin/superpowers.js`
预期：无输出

**步骤 3：提交**

```bash
git add .opencode/plugin/superpowers.js
git commit -m "feat: implement session.started hook for opencode"
```

## 阶段 4：文档

### 任务 13：创建 OpenCode 安装指南

**文件：**

- 创建：`.opencode/INSTALL.md`

**步骤 1：创建安装指南**

```markdown
# 为 OpenCode 安装 Superpowers

## 前置条件

- 已安装 [OpenCode.ai](https://opencode.ai)
- 已安装 Node.js
- 已安装 Git

## 安装步骤

### 1. 安装 Superpowers 技能

```bash
mkdir -p ~/.config/opencode/superpowers
git clone https://github.com/obra/superpowers.git ~/.config/opencode/superpowers
```

### 2. 安装插件

插件包含在刚克隆的 superpowers 仓库中。

OpenCode 会自动从此位置发现它：

也可链接到项目本地插件目录：

```bash
mkdir -p .opencode/plugin
ln -s ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js .opencode/plugin/superpowers.js
```

### 3. 重启 OpenCode

重启 OpenCode 以加载插件。下一会话应显示：

```
你已拥有 superpowers。
```

## 用法

### 查找技能

用 `find_skills` 工具列出全部可用技能：

```
使用 find_skills 工具
```

### 加载技能

用 `use_skill` 工具加载指定技能：

```
使用 use_skill 工具，skill_name: "superpowers:brainstorming"
```

### 个人技能

在 `~/.config/opencode/skills/` 创建自己的技能：

```bash
mkdir -p ~/.config/opencode/skills/my-skill
```

创建 `~/.config/opencode/skills/my-skill/SKILL.md`：

```markdown
---
name: my-skill
description: 当 [条件] 时使用 - [它做什么]
---

# 我的技能

[在这里写你的技能内容]
```

同名个人技能覆盖 superpowers 技能。

## 故障排查

```bash
cd ~/.config/opencode/superpowers
git pull
```

## 故障排查

### 插件未加载

1. 检查插件文件存在：`ls ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js`

2. 检查 OpenCode 日志错误

3. 验证 Node.js：`node --version`

### 未找到技能

1. 验证目录存在：`ls ~/.config/opencode/superpowers/skills`

2. 用 `find_skills` 查看发现结果

3. 检查每个技能都有 `SKILL.md`

### 工具映射问题

技能引用不存在的 Claude Code 工具时：

- `TodoWrite` → 使用 `update_plan`

- 带子代理的 `Task` → 用 `@mention` 调用 OpenCode 子代理

- `Skill` → 使用 `use_skill` 工具

- 文件操作 → 使用原生工具

## 获取帮助

- 报告问题：https://github.com/obra/superpowers/issues

- 文档：https://github.com/obra/superpowers

```

**步骤 2：验证文件创建**

运行：`ls -l .opencode/INSTALL.md`
预期：文件存在

**步骤 3：提交**

```bash
git add .opencode/INSTALL.md
git commit -m "docs: add opencode installation guide"
```

### 任务 14：更新主 README

**文件：**

- 修改：`README.md`

找到支持平台章节（搜索“Codex”），在其后加入：

**步骤 2：验证格式**

```markdown
### OpenCode

Superpowers 通过原生 JavaScript 插件与 [OpenCode.ai](https://opencode.ai) 配合工作。

**安装：** 参见 [.opencode/INSTALL.md](.opencode/INSTALL.md)

**功能：**
- 自定义工具：`use_skill` 和 `find_skills`
- 自动会话引导
- 支持覆盖同名技能的个人技能
- 可访问支持文件与脚本
```

运行：`grep -A 10 "### OpenCode" README.md`
预期：显示新增章节

运行：`grep -A 10 "### OpenCode" README.md`
预期：显示新增章节

**步骤 1：增加 OpenCode 支持条目**

```bash
git add README.md
git commit -m "docs: add opencode support to readme"
```

### 任务 15：更新发布说明

**文件：**

- 修改：`RELEASE-NOTES.md`

在文件顶部标题后加入：

**步骤 2：验证格式**

```markdown
## [未发布]

### 新增

- **OpenCode 支持**：OpenCode.ai 原生 JavaScript 插件
  - 自定义工具：`use_skill` 和 `find_skills`
  - 含工具映射说明的自动会话引导
  - 复用共享核心模块（`lib/skills-core.js`）
  - 安装指南位于 `.opencode/INSTALL.md`

### 变更

- **重构 Codex 实现**：现使用共享 `lib/skills-core.js` 模块
  - 消除 Codex 与 OpenCode 间重复代码
  - 技能发现与解析的单一事实来源

---
```

运行：`head -30 RELEASE-NOTES.md`
预期：显示新章节

运行：`head -30 RELEASE-NOTES.md`
预期：显示新章节

- 测试：`.codex/superpowers-codex`

```bash
git add RELEASE-NOTES.md
git commit -m "docs: add opencode support to release notes"
```

## 阶段 5：最终验证

### 任务 16：测试 Codex 仍正常

**文件：**

- 测试：`.codex/superpowers-codex`

运行：`.codex/superpowers-codex find-skills | head -20`
预期：显示技能名和描述列表

运行：`.codex/superpowers-codex find-skills | head -20`
预期：显示技能名与描述列表

运行：`.codex/superpowers-codex use-skill superpowers:brainstorming | head -20`
预期：显示 brainstorming 内容

运行：`.codex/superpowers-codex use-skill superpowers:brainstorming | head -20`
预期：显示 brainstorming 内容

运行：`.codex/superpowers-codex bootstrap | head -30`
预期：显示含指令的引导内容

运行：`.codex/superpowers-codex bootstrap | head -30`
预期：显示含指令的引导内容

无需提交——仅验证。

运行：

### 任务 17：验证文件结构

**文件：**

- 检查：所有新文件存在

预期：所有文件存在

**步骤 2：验证目录结构**

```bash
ls -l lib/skills-core.js
ls -l .opencode/plugin/superpowers.js
ls -l .opencode/INSTALL.md
```

预期：所有文件存在

- 检查：`git status`

运行：`tree -L 2 .opencode/`（没有 tree 时用 `find .opencode -type f`）
预期：

```
.opencode/
├── INSTALL.md
└── plugin/
    └── superpowers.js
```

**步骤 3：结构正确后继续**

无需提交——仅验证。

### 任务 18：最终提交与总结

**文件：**

- 检查：`git status`

**步骤 1：检查 git 状态**

运行：`git status`
预期：工作树干净，全部变更已提交

**步骤 2：审查提交日志**

运行：`git log --oneline -20`
预期：显示本次实施的全部提交

**步骤 3：创建总结文档**

完成总结应展示：

- 提交总数

- 创建文件：`lib/skills-core.js`、`.opencode/plugin/superpowers.js`、`.opencode/INSTALL.md`

- 修改文件：`.codex/superpowers-codex`、`README.md`、`RELEASE-NOTES.md`

- 已测试：验证 Codex 命令

- 可进入：使用真实 OpenCode 安装测试

**步骤 4：报告完成**

向用户展示总结，并提供：

1. 推送到远程

2. 创建拉取请求

3. 用真实 OpenCode 安装测试（要求已安装 OpenCode）

## 测试指南（手动——需要 OpenCode）

这些步骤要求已安装 OpenCode，不属于自动实施：

1. **安装技能**：遵循 `.opencode/INSTALL.md`

2. **启动 OpenCode 会话**：确认引导出现

3. **测试 find_skills**：应列出所有可用技能

4. **测试 use_skill**：加载技能并确认内容出现

5. **测试支持文件**：确认技能目录路径可访问

6. **测试个人技能**：创建个人技能并确认覆盖核心技能

7. **测试工具映射**：确认 TodoWrite → update_plan 有效

## 成功标准

- [ ] 已创建含全部核心函数的 `lib/skills-core.js`

- [ ] `.codex/superpowers-codex` 已重构为共享核心

- [ ] Codex 命令仍可用（find-skills、use-skill、bootstrap）

- [ ] 已创建含工具与 hooks 的 `.opencode/plugin/superpowers.js`

- [ ] 已创建安装指南

- [ ] 已更新 README 与 RELEASE-NOTES

- [ ] 全部变更已提交

- [ ] 工作树干净
