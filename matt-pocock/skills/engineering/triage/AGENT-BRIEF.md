# 编写代理简报

代理简报是在 GitHub issue 或 PR 移入 `ready-for-agent` 时发布的结构化评论。它是离线（AFK）代理工作的权威规范。原始正文和讨论是上下文；代理简报才是契约。

简报说明**代理应该做什么**，适用范围涵盖两种对象：对 issue 而言，是从零构建改动；对 PR 而言，是*针对现有差异*剩下要做什么：完成它、补足缺口、处理审查意见。原则相同；下方 PR 示例展示区别。

## 原则

### 持久性优先于精确性

issue 可能在 `ready-for-agent` 中停留数天或数周。期间代码库会变化。简报应保持有用，即使文件被重命名、移动或重构。

- **应**描述接口、类型和行为契约

- **应**点名代理应查找或修改的具体类型、函数签名或配置形状

- **不要**引用文件路径：它们会过期

- **不要**引用行号

- **不要**假定当前实现结构保持不变

### 行为化，而非过程化

描述系统**应该做什么**，而非**如何**实现。代理会重新探索代码库并自行作实现决策。

- **好：**“`SkillConfig` 类型应接受类型为 `CronExpression` 的可选 `schedule` 字段”

- **差：**“打开 src/types/skill.ts，在第 42 行添加 schedule 字段”

- **好：**“用户不带参数运行 `/triage` 时，应看到需要关注的 issue 摘要”

- **差：**“在主处理函数中添加 switch 语句”

### 完整验收标准

代理需要知道何时完成。每份代理简报都必须有具体、可测试的验收标准。每项标准应可独立验证。

- **好：**“运行 `gh issue list --label needs-triage` 返回已通过初步分类的 issue”

- **差：**“分诊应正确工作”

### 明确范围边界

说明哪些内容不在范围内。这防止代理镀金或对相邻功能作假定。

## 模板

```markdown
## Agent Brief

**Category:** bug / enhancement
**Summary:** 一句话说明需要发生什么

**Current behavior:**
描述当前发生什么。对缺陷而言，这是损坏行为。
对增强而言，这是功能所基于的现状。

**Desired behavior:**
描述代理完成后应发生什么。
具体说明边界情况和错误条件。

**Key interfaces:**
- `TypeName`：需要改变什么以及为何
- `functionName()` 返回类型：当前返回什么，与应返回什么
- 配置形状：需要的新配置选项

**Acceptance criteria:**
- [ ] 具体、可测试的标准 1
- [ ] 具体、可测试的标准 2
- [ ] 具体、可测试的标准 3

**Out of scope:**
- 不应在本 issue 中改变或处理的事项
- 看似相关但实际独立的相邻功能
```

## 示例

### 好的代理简报（缺陷）

```markdown
## Agent Brief

**Category:** bug
**Summary:** 技能描述截断发生在词中间，产生损坏输出

**Current behavior:**
技能描述超过 1024 个字符时，会在恰好 1024 个字符处截断，
不考虑词边界。这会产生在词中间结束的描述
（例如 “Use when the user wants to confi”）。

**Desired behavior:**
截断应在 1024 个字符前的最后一个词边界处断开，
并追加 “...” 表示已截断。

**Key interfaces:**
- `SkillMetadata` 类型的 `description` 字段：无需改变类型，
  但填充它的验证/处理逻辑必须尊重词边界
- 任何读取 SKILL.md frontmatter 并提取 description 的函数

**Acceptance criteria:**
- [ ] 少于 1024 字符的描述保持不变
- [ ] 超过 1024 字符的描述在 1024 字符前的最后一个词边界截断
- [ ] 截断描述以 “...” 结尾
- [ ] 包含 “...” 的总长度不超过 1024 字符

**Out of scope:**
- 改变 1024 字符限制本身
- 多行描述支持
```

### 好的代理简报（增强）

```markdown
## Agent Brief

**Category:** enhancement
**Summary:** 添加 `.out-of-scope/` 目录支持，用于跟踪被拒绝的功能请求

**Current behavior:**
功能请求被拒绝时，issue 会附加 `wontfix` 标签并通过评论关闭。
决定或理由没有持久记录。未来类似请求要求维护者回忆或搜索
先前讨论。

**Desired behavior:**
被拒绝的功能请求应记录在 `.out-of-scope/<concept>.md` 文件中，
捕获决定、理由及所有请求该功能的 issue 链接。分诊新 issue 时，
应检查这些文件是否有匹配。

**Key interfaces:**
- `.out-of-scope/` 中的 Markdown 文件格式：每个文件应有
  `# Concept Name` 标题、`**Decision:**` 行、`**Reason:**` 行，
  以及带 issue 链接的 `**Prior requests:**` 列表
- 分诊工作流应尽早读取所有 `.out-of-scope/*.md` 文件，
  并按概念相似度为传入 issue 匹配它们

**Acceptance criteria:**
- [ ] 将功能以 wontfix 关闭时，在 `.out-of-scope/` 中创建/更新文件
- [ ] 文件包含决定、理由及已关闭 issue 的链接
- [ ] 若匹配的 `.out-of-scope/` 文件已存在，将新 issue 追加到
      “Prior requests” 列表，而不是创建重复文件
- [ ] 分诊期间检查现有 `.out-of-scope/` 文件，并在新 issue
      匹配先前拒绝时展示

**Out of scope:**
- 自动匹配（由人类确认匹配）
- 重新打开此前拒绝的功能
- 缺陷报告（只有增强拒绝进入 `.out-of-scope/`）
```

### 好的代理简报（PR）

对 PR 而言，“Current behavior”描述差异的状态，简报要求代理完成或修复它，而不是从头构建。

```markdown
## Agent Brief

**Category:** enhancement
**Summary:** 完成贡献者为 `triage list` 添加的 `--json` 输出标志

**Current behavior:**
PR 添加 `--json` 标志，将 issue 列表序列化为 JSON。正常路径可用，
差异符合项目命令结构。仍有两个缺口：错误仍以人类可读文本打印，
而非 JSON；新标志没有测试覆盖。

**Desired behavior:**
使用 `--json` 时，所有输出（包括错误）都是 stdout 上的格式良好 JSON，
且命令退出码不变。未使用该标志时，现有人类可读输出保持不变。

**Key interfaces:**
- 命令错误路径在 `--json` 下应输出 `{ "error": string }`，
  而非纯文本错误
- 复用 PR 已添加的现有序列化器；不要引入第二个

**Acceptance criteria:**
- [ ] `triage list --json` 在成功和错误情形都输出有效 JSON
- [ ] 退出码与非 JSON 命令相同
- [ ] 测试覆盖 `--json` 成功输出及一个错误情形
- [ ] 默认（非 JSON）输出逐字节不变

**Out of scope:**
- 为任何其他命令添加 `--json`
- 改变 PR 已定义的 JSON 成功载荷形状
```

### 差的代理简报

```markdown
## Agent Brief

**Summary:** 修复分诊缺陷

**What to do:**
分诊功能坏了。查看主文件并修复。
大约第 150 行的函数有问题。

**Files to change:**
- src/triage/handler.ts（第 150 行）
- src/types.ts（第 42 行）
```

这很差，因为：

- 没有类别

- 描述含糊（“分诊功能坏了”）

- 引用了会过期的文件路径和行号

- 没有验收标准

- 没有范围边界

- 没有描述当前行为与期望行为
