# 技能编写最佳实践

> 学习如何编写代理能够发现并成功使用的有效技能。

优秀技能应当简洁、结构清晰，并通过实际使用进行测试。本指南提供实用的编写决策，帮助代理可靠地发现和有效使用技能。

技能工作方式的背景说明见[技能概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)。

## 核心原则

### 简洁至上

[上下文窗口](https://platform.claude.com/docs/en/build-with-claude/context-windows)是共享资源。技能与其他代理所需信息共同占用上下文，包括：

* 系统提示词

* 对话历史

* 其他技能的元数据

* 实际请求

并非技能中的每个 token 都会立即产生成本。启动时只预加载所有技能的元数据（名称和描述）。代理仅在技能相关时读取 SKILL.md，并只在需要时读取附加文件。但保持 SKILL.md 简洁仍很重要：一旦加载，其中每个 token 都会与对话历史及其他上下文竞争。

**默认假设：**代理本身已经非常聪明。

只补充代理尚未拥有的上下文。逐项质疑信息：

* “代理真的需要这条解释吗？”

* “能否假定代理已经知道？”

* “这一段是否值得其 token 成本？”

**好示例：简洁**（约 50 个 token）：

````markdown  theme={null}
## 提取 PDF 文本

使用 pdfplumber 提取文本：

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
````

**坏示例：过于冗长**（约 150 个 token）：

```markdown  theme={null}
## 提取 PDF 文本

PDF（便携式文档格式）是一种常见文件格式，包含文本、图像和其他内容。要从 PDF 提取文本，需要用库。PDF 处理库很多，但推荐 pdfplumber，因为易用且能处理大多数情况。首先用 pip 安装，然后使用下面的代码……
```

简洁版本假定代理知道 PDF 是什么以及库如何工作。

### 设置合适的自由度

让说明的具体程度与任务的脆弱性和可变性相匹配。

**高自由度**（文字说明）：

适用于：

* 有多种有效方法

* 决策取决于上下文

* 用启发式原则引导

示例：

```markdown  theme={null}
## 代码审查流程

1. 分析代码结构和组织
2. 检查潜在缺陷或边界情况
3. 提出可读性和可维护性改进建议
4. 验证是否符合项目约定
```

**中等自由度**（伪代码或带参数的脚本）：

适用于：

* 已有首选模式

* 允许一定变化

* 配置会影响行为

示例：

````markdown  theme={null}
## 生成报告

使用此模板并按需定制：

```python
def generate_report(data, format="markdown", include_charts=True):
    pass
```
````

**低自由度**（特定脚本，参数很少或没有）：

适用于：

* 操作脆弱且容易出错

* 一致性至关重要

* 必须严格执行特定顺序

示例：

````markdown  theme={null}
## 数据库迁移

严格运行以下脚本：

```bash
python scripts/migrate.py --verify --backup
```

不要修改命令或添加其他标志。
````

**类比：**把代理看作探索路径的机器人：

* **两侧悬崖的窄桥**：只有一条安全前进路线。提供具体护栏和准确指令（低自由度）。例如：必须按准确顺序执行的数据库迁移。

* **没有危险的旷野**：多条路径都能成功。给出总体方向，信任代理寻找最佳路线（高自由度）。例如：由上下文决定最佳方法的代码审查。

### 用所有计划使用的模型测试

技能是模型能力的补充，效果取决于底层模型。请用所有计划配套使用的模型测试技能。

**按模型测试时的考虑：**

* **Claude Haiku**（快速、经济）：技能是否提供足够指引？

* **Claude Sonnet**（均衡）：技能是否清楚高效？

* **Claude Opus**（推理强）：技能是否避免过度解释？

适合 Opus 的内容可能需要为 Haiku 增加细节。若计划跨多个模型使用，应让说明适用于全部模型。

## 技能结构

<Note>
  **YAML 前置元数据**：SKILL.md 的 frontmatter 需要两个字段：

* `name`——技能的人类可读名称（最多 64 个字符）

* `description`——用一行说明技能做什么及何时使用（最多 1024 个字符）

完整技能结构见[技能概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#skill-structure)。
</Note>

### 命名约定

使用一致的命名模式，便于引用和讨论技能。建议技能名称采用**动名词形式**（动词加 -ing），清楚描述技能提供的活动或能力。

**好的命名示例（动名词形式）：**

* “Processing PDFs”（处理 PDF）

* “Analyzing spreadsheets”（分析电子表格）

* “Managing databases”（管理数据库）

* “Testing code”（测试代码）

* “Writing documentation”（编写文档）

**可接受的替代形式：**

* 名词短语：“PDF Processing”“Spreadsheet Analysis”

* 动作导向：“Process PDFs”“Analyze Spreadsheets”

**避免：**

* 含糊名称：“Helper”“Utils”“Tools”

* 过于宽泛：“Documents”“Data”“Files”

* 技能集合内部命名模式不一致

一致命名便于：

* 在文档和对话中引用技能

* 一眼理解技能用途

* 组织和搜索多个技能

* 维护专业、统一的技能库

### 编写有效的描述

`description` 字段用于发现技能，应同时说明技能做什么及何时使用。

<Warning>
  **始终使用第三人称**。描述会注入系统提示词，视角不一致会造成发现困难。

* **好：**“处理 Excel 文件并生成报告”

* **避免：**“我可以帮你处理 Excel 文件”

* **避免：**“你可以用它处理 Excel 文件”
</Warning>

**要具体并包含关键词**。同时写出技能功能及使用该技能的具体触发条件或上下文。

每个技能只有一个 description 字段。该字段对技能选择至关重要：代理可能要从 100 多个技能中选出正确者。描述必须足够详细，使代理知道何时选择该技能，SKILL.md 其余部分提供实施细节。

有效示例：

**PDF 处理技能：**

```yaml  theme={null}
description: 从 PDF 文件提取文本和表格、填写表单、合并文档。处理 PDF 文件，或用户提到 PDF、表单、文档提取时使用。
```

**Excel 分析技能：**

```yaml  theme={null}
description: 分析 Excel 电子表格、创建数据透视表、生成图表。分析 Excel 文件、电子表格、表格数据或 .xlsx 文件时使用。
```

**Git 提交辅助技能：**

```yaml  theme={null}
description: 通过分析 git diff 生成描述性提交信息。用户请求帮助编写提交信息或审查已暂存变更时使用。
```

避免如下含糊描述：

```yaml  theme={null}
description: 帮助处理文档
```

```yaml  theme={null}
description: 处理数据
```

```yaml  theme={null}
description: 对文件做些事情
```

### 渐进式披露模式

SKILL.md 是概览，像入门指南的目录一样在需要时指向详细信息。渐进式披露的工作原理见概览中的[技能如何工作](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work)。

**实用建议：**

* 为获得最佳性能，将 SKILL.md 正文保持在 500 行以内

* 接近该限制时，把内容拆到独立文件

* 用下列模式有效组织说明、代码和资源

#### 可视化概览：由简到繁

基本技能只从包含元数据和说明的 SKILL.md 文件开始：

<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=87782ff239b297d9a9e8e1b72ed72db9" alt="Simple SKILL.md file showing YAML frontmatter and markdown body" data-og-width="2048" width="2048" data-og-height="1153" height="1153" data-path="images/agent-skills-simple-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=c61cc33b6f5855809907f7fda94cd80e 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=90d2c0c1c76b36e8d485f49e0810dbfd 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=ad17d231ac7b0bea7e5b4d58fb4aeabb 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=f5d0a7a3c668435bb0aee9a3a8f8c329 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=0e927c1af9de5799cfe557d12249f6e6 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=46bbb1a51dd4c8202a470ac8c80a893d 2500w" />

技能增长后，可以打包额外内容，只让代理在需要时加载：

<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=a5e0aa41e3d53985a7e3e43668a33ea3" alt="Bundling additional reference files like reference.md and forms.md." data-og-width="2048" width="2048" data-og-height="1327" height="1327" data-path="images/agent-skills-bundling-content.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=f8a0e73783e99b4a643d79eac86b70a2 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=dc510a2a9d3f14359416b706f067904a 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=82cd6286c966303f7dd914c28170e385 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=56f3be36c77e4fe4b523df209a6824c6 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=d22b5161b2075656417d56f41a74f3dd 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=3dd4bdd6850ffcc96c6c45fcb0acd6eb 2500w" />

完整技能目录结构可能如下：

```
pdf/
├── SKILL.md              # 主说明（触发时加载）
├── FORMS.md              # 表单填写指南（按需加载）
├── reference.md          # API 参考（按需加载）
├── examples.md           # 使用示例（按需加载）
└── scripts/
    ├── analyze_form.py   # 辅助脚本（执行而不加载）
    ├── fill_form.py      # 表单填写脚本
    └── validate.py       # 验证脚本
```

#### 模式 1：带引用资料的高层指南

````markdown  theme={null}
---
name: PDF Processing
description: 从 PDF 文件提取文本和表格、填写表单、合并文档。处理 PDF 文件，或用户提到 PDF、表单、文档提取时使用。
---

# PDF 处理

## 快速开始

使用 pdfplumber 提取文本：
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## 高级功能

**表单填写**：完整指南见 [FORMS.md](FORMS.md)
**API 参考**：所有方法见 [REFERENCE.md](REFERENCE.md)
**示例**：常见模式见 [EXAMPLES.md](EXAMPLES.md)
````

智能体仅在需要时加载 FORMS.md、REFERENCE.md 或 EXAMPLES.md。

#### 模式 2：按领域组织

对于覆盖多个领域的技能，按领域组织内容，避免加载无关上下文。用户询问销售指标时，智能体只需阅读与销售有关的模式，无需财务或营销数据。这样可以降低 token 用量并让上下文保持聚焦。

```
bigquery-skill/
├── SKILL.md (概览与导航)
└── reference/
    ├── finance.md (收入、账单指标)
    ├── sales.md (商机、销售管道)
    ├── product.md (API 使用、功能)
    └── marketing.md (营销活动、归因)
```

````markdown SKILL.md theme={null}
# BigQuery 数据分析

## 可用数据集

**财务**：收入、ARR、账单 → 参见 [reference/finance.md](reference/finance.md)
**销售**：商机、销售管道、客户 → 参见 [reference/sales.md](reference/sales.md)
**产品**：API 使用、功能、采用情况 → 参见 [reference/product.md](reference/product.md)
**营销**：营销活动、归因、邮件 → 参见 [reference/marketing.md](reference/marketing.md)

## 快速搜索

使用 grep 查找特定指标：

```bash
grep -i "revenue" reference/finance.md
grep -i "pipeline" reference/sales.md
grep -i "api usage" reference/product.md
```
````

#### 模式 3：按条件提供细节

展示基础内容，通过链接指向高级内容：

```markdown  theme={null}
# DOCX 处理

## 创建文档

创建新文档使用 docx-js。参见 [DOCX-JS.md](DOCX-JS.md).

## 编辑文档

简单编辑可直接修改 XML。

**修订跟踪**：参见 [REDLINING.md](REDLINING.md)
**OOXML 细节**：参见 [OOXML.md](OOXML.md)
```

只有用户需要这些功能时，智能体才读取 REDLINING.md 或 OOXML.md。

### 避免深度嵌套引用

文件被其他已引用文件引用时，智能体可能只读其中一部分。遇到嵌套引用时，智能体可能用 `head -100` 等命令预览内容而不是阅读全文，导致信息不完整。

**让引用与 SKILL.md 之间只有一层深度**。所有参考文件都应从 SKILL.md 直接链接，确保智能体需要时读取完整文件。

**反例：嵌套太深**：

```markdown  theme={null}
# SKILL.md
参见 [advanced.md](advanced.md)...

# advanced.md
参见 [details.md](details.md)...

# details.md
这里才是实际信息……
```

**正例：只有一层**：

```markdown  theme={null}
# SKILL.md

**基本用法**：[SKILL.md 中的指令]
**高级功能**：参见 [advanced.md](advanced.md)
**API 参考**：参见 [reference.md](reference.md)
**示例**：参见 [examples.md](examples.md)
```

### 用目录组织较长的参考文件

超过 100 行的参考文件，应在顶部包含目录。这样即使智能体通过局部读取进行预览，也能看到可用信息的完整范围。

**示例**：

```markdown  theme={null}
# API 参考

## 目录
- 身份验证与设置
- 核心方法（创建、读取、更新、删除）
- 高级功能（批处理操作、webhook）
- 错误处理模式
- 代码示例

## 身份验证与设置
...

## 核心方法
...
```

随后，智能体可以按需读取完整文件或跳到具体章节。

关于这种基于文件系统的架构如何实现渐进式披露，详见下方高级部分的[运行环境](#runtime-environment)章节。

## 工作流和反馈循环

### 为复杂任务使用工作流

将复杂操作拆分为清晰、有先后顺序的步骤。特别复杂的工作流应提供检查清单，供智能体复制到回复中，并随进度逐项勾选。

**示例 1：研究综合工作流**（适用于不含代码的技能）：

````markdown  theme={null}
## 研究综合工作流

复制此检查清单并跟踪进度：

```
研究进度：
- [ ] 步骤 1：阅读所有来源文档
- [ ] 步骤 2：识别关键主题
- [ ] 步骤 3：交叉核查论点
- [ ] 步骤 4：创建结构化摘要
- [ ] 步骤 5：验证引用
```

**步骤 1：阅读所有来源文档**

审阅 `sources/` 目录中的每份文档。记录主要论点和支持证据。

**步骤 2：识别关键主题**

寻找来源之间的模式。哪些主题反复出现？各来源在哪些方面一致或存在分歧？

**步骤 3：交叉核查论点**

对每项主要论点，确认它出现在来源材料中。记录支持每一点的来源。

**步骤 4：创建结构化摘要**

按主题组织发现。包括：
- 主要论点
- 来自来源的支持证据
- 冲突观点（如有）

**步骤 5：验证引用**

检查每项论点是否引用正确的来源文档。引用不完整则返回步骤 3。
````

此示例展示工作流如何应用于无需代码的分析任务。检查清单模式适用于任何复杂的多步骤过程。

**示例 2：PDF 表单填写工作流**（适用于包含代码的技能）：

````markdown  theme={null}
## PDF 表单填写工作流

复制此检查清单，完成后逐项勾选：

```
任务进度：
- [ ] 步骤 1：分析表单 （运行 analyze_form.py）
- [ ] 步骤 2：创建字段映射 （编辑 fields.json）
- [ ] 步骤 3：验证映射 （运行 validate_fields.py）
- [ ] 步骤 4：填写表单 （运行 fill_form.py）
- [ ] 步骤 5：验证输出 （运行 verify_output.py）
```

**步骤 1：分析表单**

运行： `python scripts/analyze_form.py input.pdf`

这会提取表单字段及其位置，并保存到 `fields.json`。

**步骤 2：创建字段映射**

编辑 `fields.json`，为每个字段添加值。

**步骤 3：验证映射**

运行： `python scripts/validate_fields.py fields.json`

继续前修复所有验证错误。

**步骤 4：填写表单**

运行： `python scripts/fill_form.py input.pdf fields.json output.pdf`

**步骤 5：验证输出**

运行： `python scripts/verify_output.py output.pdf`

验证失败则返回步骤 2。
````

清晰的步骤可以防止智能体跳过关键验证。检查清单帮助你和智能体共同跟踪多步骤工作流的进度。

### 实现反馈循环

**常见模式**：运行验证器 → 修复错误 → 重复

此模式能显著提升输出质量。

**示例 1：遵循风格指南**（适用于不含代码的技能）：

```markdown  theme={null}
## 内容审阅过程

1. 遵循 STYLE_GUIDE.md 的指导起草内容
2. 对照检查清单审阅：
   - 检查术语一致性
   - 验证示例遵循标准格式
   - 确认包含所有必需章节
3. 如果发现问题：
   - 记录每个问题，注明具体章节引用
   - 修订内容
   - 再次审阅检查清单
4. 只有满足所有要求才继续
5. 定稿并保存文档
```

此示例展示使用参考文档而非脚本的验证循环模式。“验证器”是 STYLE\_GUIDE.md，智能体通过阅读和比较执行检查。

**示例 2：文档编辑过程**（适用于包含代码的技能）：

```markdown  theme={null}
## 文档编辑过程

1. 编辑 `word/document.xml`
2. **立即验证**: `python ooxml/scripts/validate.py unpacked_dir/`
3. 如果验证失败：
   - 仔细阅读错误消息
   - 修复 XML 中的问题
   - 再次运行验证
4. **只有验证通过才继续**
5. 重新构建： `python ooxml/scripts/pack.py unpacked_dir/ output.docx`
6. 测试输出文档
```

验证循环可以尽早发现错误。

## 内容指导

### 避免时效性信息

不要包含将会过时的信息：

**反例：具有时效性**（将来会出错）：

```markdown  theme={null}
如果在 2025 年 8 月之前操作，使用旧 API。
2025 年 8 月之后使用新 API。
```

**正例**（使用“旧模式”章节）：

```markdown  theme={null}
## 当前方法

使用 v2 API 端点： `api.example.com/v2/messages`

## 旧模式

<details>
<summary>旧版 v1 API（2025-08 弃用）</summary>

v1 API 使用： `api.example.com/v1/messages`

此端点不再受支持。
</details>
```

旧模式章节提供历史背景，同时避免使主要内容杂乱。

### 使用一致术语

选定一个术语并在整个技能中始终使用：

**正例：保持一致**：

* 始终使用“API 端点”

* 始终使用“字段”

* 始终使用“提取”

**反例：不一致**：

* 混用“API 端点”“URL”“API 路由”“路径”

* 混用“字段”“框”“元素”“控件”

* 混用“提取”“拉取”“获取”“检索”

一致性有助于智能体理解并遵循指令。

## 常见模式

### 模板模式

为输出格式提供模板。严格程度应与你的需求匹配。

**适用于严格要求**（例如 API 响应或数据格式）：

````markdown  theme={null}
## 报告结构

始终严格使用此模板结构：

```markdown
# [分析标题]

## 执行摘要
[用一段话概述关键发现]

## 关键发现
- 发现 1 及支持数据
- 发现 2 及支持数据
- 发现 3 及支持数据

## 建议
1. 具体可执行的建议
2. 具体可执行的建议
```
````

**适用于灵活指导**（适合调整时）：

````markdown  theme={null}
## 报告结构

以下是合理的默认格式，但请根据分析自行做出最佳判断：

```markdown
# [分析标题]

## 执行摘要
[概览]

## 关键发现
[根据发现调整章节]

## 建议
[针对具体上下文定制]
```

根据具体分析类型按需调整章节。
````

### 示例模式

对于输出质量依赖示例的技能，像普通提示一样提供输入／输出对：

````markdown  theme={null}
## 提交消息格式

参照以下示例生成提交消息：

**示例 1:**
输入：添加使用 JWT 令牌的用户身份验证
输出：
```
feat(auth): 实现基于 JWT 的身份验证

添加登录端点和令牌验证中间件
```

**示例 2:**
输入：修复报告中日期显示不正确的问题
输出：
```
fix(reports): 修正时区转换中的日期格式

在报告生成的全过程一致使用 UTC 时间戳
```

**示例 3:**
输入：更新依赖并重构错误处理
输出：
```
chore: 更新依赖并重构错误处理

- 将 lodash 升级到 4.17.21
- 统一各端点的错误响应格式
```

遵循此风格：type(scope): 简短描述，随后给出详细说明。
````

与单纯描述相比，示例能帮助智能体更清晰地理解期望的风格和细节程度。

### 条件工作流模式

引导智能体通过决策点：

```markdown  theme={null}
## 文档修改工作流

1. 确定修改类型：

   **创建新内容？** → 遵循下方“创建工作流”
   **编辑现有内容？** → 遵循下方“编辑工作流”

2. 创建工作流：
   - 使用 docx-js 库
   - 从零构建文档
   - 导出为 .docx 格式

3. 编辑工作流：
   - 解包现有文档
   - 直接修改 XML
   - 每次变更后验证
   - 完成后重新打包
```

<Tip>
  如果工作流变得庞大或复杂、包含许多步骤，考虑将其移入独立文件，并告诉智能体根据当前任务读取相应文件。
</Tip>

## 评估与迭代

### 先构建评估

**先创建评估，再编写大量文档。** 这样可以确保技能解决真实问题，而不是为想象中的问题编写文档。

**评估驱动开发：**

1. **识别缺口**：在不使用技能的情况下，让智能体执行代表性任务。记录具体失败或缺失上下文

2. **创建评估**：构建三个场景来测试这些缺口

3. **建立基线**：衡量不使用该技能时智能体的表现

4. **编写最少指令**：创建足以弥补缺口并通过评估的内容即可

5. **迭代**：执行评估，对比基线，进一步改进

此方法确保你解决实际问题，而不是预先应对可能永远不会出现的需求。

**评估结构**：

```json  theme={null}
{
  "skills": ["pdf-processing"],
  "query": "从此 PDF 文件提取全部文本并保存到 output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "使用合适的 PDF 处理库或命令行工具成功读取 PDF 文件",
    "提取文档所有页面的文本内容，不遗漏任何页面",
    "以清晰易读的格式将提取的文本保存到名为 output.txt 的文件"
  ]
}
```

<Note>
  此示例展示带有简单测试评分规则的数据驱动评估。我们目前不提供运行这些评估的内置方式。用户可以创建自己的评估系统。评估是衡量技能有效性的事实依据。
</Note>

### 借助智能体迭代开发技能

最有效的技能开发过程会把智能体本身纳入其中。你与一个实例（“智能体 A”）协作创建另一批实例（“智能体 B”）要使用的技能。智能体 A 帮助你设计和提炼指令，智能体 B 在真实任务中测试它们。这样做之所以有效，是因为底层模型既理解如何编写有效的智能体指令，也理解智能体需要哪些信息。

**创建新技能：**

1. **先不使用技能完成任务**：用常规提示词与智能体 A 一起解决问题。工作过程中，你会自然地补充背景、解释偏好并分享流程知识。留意自己反复提供了哪些信息。

2. **找出可复用的模式**：任务完成后，找出你所提供的信息中，哪些对今后的类似任务有用。

**示例**：如果你完成了一次 BigQuery 分析，可能提供过表名、字段定义、筛选规则（例如“始终排除测试账号”）以及常用查询模式。

3. **要求智能体 A 创建技能**：“创建一个技能，记录我们刚使用的 BigQuery 分析模式。包括表结构、命名约定，以及排除测试账号的规则。”

<Tip>
     现代智能体原生理解技能格式和结构。你无需特殊系统提示词或“编写技能”技能就能获得创建帮助。只要要求智能体创建技能，它就会生成具有合适前置元数据和正文内容的规范 SKILL.md。
   </Tip>

4. **检查是否简洁**：确认智能体 A 没有添加不必要的解释。可以问：“删除关于胜率含义的解释，智能体已经知道这一点。”

5. **改善信息架构**：要求智能体 A 更有效地组织内容。例如：“把表结构整理到单独的参考文件。我们以后可能添加更多表。”

6. **在类似任务上测试**：让已加载该技能的全新实例智能体 B 处理相关用例。观察它能否找到正确信息、正确应用规则并成功完成任务。

7. **根据观察结果迭代**：若智能体 B 遇到困难或遗漏内容，带着具体细节回到智能体 A：“这个智能体使用技能时，忘了按第四季度日期过滤。要不要增加一节说明日期筛选模式？”

**迭代现有技能：**

改进技能时沿用同样的分工模式。你轮流：

* **与智能体 A 协作**（帮助提炼技能的专家）

* **用智能体 B 测试**（使用技能完成真实工作的智能体）

* **观察智能体 B 的行为**，再把认识带回给智能体 A

1. **在真实工作流中使用技能**：给已加载技能的智能体 B 实际任务，而非测试场景

2. **观察智能体 B 的行为**：记录它在哪里受阻、成功或作出意外选择

**示例观察**：“我要智能体 B 生成区域销售报告时，它写出了查询，却忘了排除测试账号，即使技能提到了这条规则。”

3. **回到智能体 A 改进**：分享当前 SKILL.md 并描述观察结果。问：“我发现智能体 B 在我要求区域报告时忘记过滤测试账号。技能提到了过滤，但可能不够醒目？”

4. **审阅智能体 A 的建议**：智能体 A 可能建议重新组织内容，让规则更醒目；使用更强的措辞，例如用“必须过滤”替代“始终过滤”；或重新组织工作流部分。

5. **应用并测试改动**：用智能体 A 的改进更新技能，再让智能体 B 在类似请求上测试

6. **根据使用情况重复**：遇到新场景时继续这种观察—改进—测试循环。每次迭代都依据真实智能体行为而非假设改进技能。

**收集团队反馈：**

1. 与队友分享技能，观察他们如何使用

2. 询问：技能会在预期时激活吗？指令清楚吗？缺少什么？

3. 吸收反馈，修正自身使用模式中的盲点

**这种方法为何有效**：智能体 A 理解智能体需求；你提供领域专业知识；智能体 B 通过真实使用暴露缺口；迭代改进依据观察到的行为而非假设完善技能。

### 观察智能体如何使用技能

迭代技能时，要关注智能体实际如何使用它们。留意：

* **意外的浏览路径**：智能体读取文件的顺序是否出乎你的预料？这可能表明你的结构没有想象中直观

* **错过的关联**：智能体是否没有跟随指向重要文件的引用？你的链接可能需要更明确或更醒目

* **过度依赖某些部分**：如果智能体反复读取同一文件，考虑这些内容是否应放在主 SKILL.md 中

* **被忽略的内容**：如果智能体从不访问随附文件，它可能没有必要存在，或在主指令中的提示不够清楚

请依据这些观察迭代，而不是依据假设。技能元数据中的 `name` 和 `description` 尤其关键。智能体会在判断是否因当前任务触发技能时使用它们。务必清楚描述技能做什么以及何时使用。

## 应避免的反模式

### 避免 Windows 风格路径

即使在 Windows 上，文件路径也始终使用正斜杠：

* ✓ **正确**：`scripts/helper.py`、`reference/guide.md`

* ✗ **避免**：`scripts\helper.py`、`reference\guide.md`

Unix 风格路径可在所有平台使用，Windows 风格路径在 Unix 系统上会导致错误。

### 避免提供过多选项

除非必要，不要给出多种方案：

````markdown  theme={null}
**错误示例：选择过多**（令人困惑）：
“你可以用 pypdf，或用 pdfplumber，或用 PyMuPDF，或用 pdf2image，或者……”

**正确示例：提供默认方案**（并留出备用路径）：
“使用 pdfplumber 提取文本：
```python
import pdfplumber
```

对于需要 OCR 的扫描版 PDF，改用 pdf2image 配合 pytesseract。”
````

## 进阶：包含可执行代码的技能

下面各节重点讨论包含可执行脚本的技能。若技能只使用 Markdown 指令，请跳至[有效技能检查清单](#checklist-for-effective-skills)。

### 解决问题，而不是推回给智能体

为技能编写脚本时，应处理错误情况，而不是把问题推给智能体。

**正确示例：明确处理错误**：

```python  theme={null}
def process_file(path):
    """处理文件；文件不存在时创建一个。"""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"未找到文件 {path}，正在创建默认文件")
        with open(path, 'w') as f:
            f.write('')
        return ''
    except PermissionError:
        print(f"无法访问 {path}，改用默认值")
        return ''
```

**错误示例：推给智能体**：

```python  theme={null}
def process_file(path):
    return open(path).read()
```

配置参数也应说明理由并写成文档，避免“巫术常量”（Ousterhout 定律）。如果你都不知道正确值，智能体又如何确定它？

**正确示例：自我说明**：

```python  theme={null}
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
```

**错误示例：魔数**：

```python  theme={null}
TIMEOUT = 47  # 为什么是 47？
RETRIES = 5   # 为什么是 5？
```

### 提供实用脚本

即使智能体能编写脚本，预制脚本也有优势：

**实用脚本的好处**：

* 比生成的代码更可靠

* 节省词元（无需将代码放入上下文）

* 节省时间（无需生成代码）

* 确保不同次使用保持一致

<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=4bbc45f2c2e0bee9f2f0d5da669bad00" alt="将可执行脚本与指令文件一并打包" data-og-width="2048" width="2048" data-og-height="1154" height="1154" data-path="images/agent-skills-executable-scripts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=9a04e6535a8467bfeea492e517de389f 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=e49333ad90141af17c0d7651cca7216b 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=954265a5df52223d6572b6214168c428 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=2ff7a2d8f2a83ee8af132b29f10150fd 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=48ab96245e04077f4d15e9170e081cfb 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=0301a6c8b3ee879497cc5b5483177c90 2500w" />

上图展示可执行脚本如何与指令文件配合。指令文件（forms.md）引用脚本，智能体可执行脚本而无需把其内容加载到上下文中。

**重要区别**：请在指令中明确智能体应该：

* **执行脚本**（最常见）：“运行 `analyze_form.py` 提取字段”

* **将其作为参考阅读**（适用于复杂逻辑）：“字段提取算法见 `analyze_form.py`”

对大多数实用脚本而言，优先执行，因为它更可靠、更高效。脚本执行细节见下文[运行环境](#runtime-environment)部分。

**示例**：

````markdown  theme={null}
## 实用脚本

**analyze_form.py**：从 PDF 提取所有表单字段

```bash
python scripts/analyze_form.py input.pdf > fields.json
```

输出格式：
```json
{
  "field_name": {"type": "text", "x": 100, "y": 200},
  "signature": {"type": "sig", "x": 150, "y": 500}
}
```

**validate_boxes.py**：检查边界框是否重叠

```bash
python scripts/validate_boxes.py fields.json
```

**fill_form.py**：把字段值填入 PDF

```bash
python scripts/fill_form.py input.pdf fields.json output.pdf
```
````

### 使用视觉分析

输入可渲染为图像时，可让智能体分析：

````markdown  theme={null}
## 表单布局分析

1. 将 PDF 转换为图像：
   ```bash
   python scripts/pdf_to_images.py form.pdf
   ```

2. 分析每页图像以识别表单字段
3. 智能体可以从视觉上看到字段位置和类型
````

<Note>
  在此示例中，你需要编写 `pdf_to_images.py` 脚本。
</Note>

智能体的视觉能力有助于理解布局和结构。

### 创建可验证的中间输出

智能体执行复杂开放式任务时可能出错。“规划—验证—执行”模式要求智能体先以结构化格式创建计划，再用脚本验证，最后执行，从而及早捕获错误。

**示例**：假设要求智能体根据电子表格更新 PDF 中的 50 个表单字段。没有验证时，它可能引用不存在的字段、产生冲突值、漏掉必填字段或错误地应用更新。

**解决方案**：沿用上述工作流（填写 PDF 表单），但加入一个中间 `changes.json` 文件，在应用变更前先验证。工作流变为：分析 → **创建计划文件** → **验证计划** → 执行 → 验证。

**这种模式为何有效：**

* **及早捕获错误**：验证在应用变更前发现问题

* **可由机器验证**：脚本提供客观验证

* **规划可逆**：智能体可反复修改计划而无需触碰原始文件

* **调试清楚**：错误消息指出具体问题

**适用时机**：批量操作、破坏性变更、复杂验证规则、高风险操作。

**实现提示**：让验证脚本提供详细且具体的错误消息，例如“未找到字段 'signature\_date'。可用字段：customer\_name、order\_total、signature\_date\_signed”，帮助智能体修复问题。

### 包依赖

技能在代码执行环境中运行，平台限制不同：

* **claude.ai**：可从 npm/PyPI 安装包，并从 GitHub 仓库拉取

* **Anthropic API**：无网络访问，也无运行时包安装

在 SKILL.md 列出所需包，并用[代码执行工具文档](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)确认可用。

### 运行环境

技能在具有文件系统、bash 命令和代码执行能力的代码环境中运行。架构见总览中的[技能架构](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#the-skills-architecture)。

**这对编写有什么影响：**

**代理如何访问技能：**

1. **元数据预加载**：启动时，所有技能 YAML 的名称和描述进入系统提示。

2. **按需读文件**：代理需要时用文件工具访问 SKILL.md 及其他文件。

3. **高效执行脚本**：bash 执行实用脚本，只需输出进入上下文，不载入全文。

4. **大文件无上下文成本**：参考、数据、文档实际读取前不消耗 token。

* **文件路径重要**：代理按文件系统导航，使用正斜杠 `reference/guide.md`。

* **描述性文件名**：如 `form_validation_rules.md`，不用 `doc2.md`。

* **按发现组织**：目录按领域或能力组织。

* 好：`reference/finance.md`、`reference/sales.md`

* 差：`docs/file1.md`、`docs/file2.md`

* **打包完整资源**：完整 API 文档、大量示例、大数据集在访问前不占上下文。

* **确定性操作优先脚本**：写 `validate_form.py`，而非让代理生成验证代码。

* **明确执行意图**：

* “运行 `analyze_form.py` 提取字段”（执行）

* “参考 `analyze_form.py` 的提取算法”（阅读）

* **测试文件访问模式**：用真实请求验证代理能否导航目录。

**示例：**

```
bigquery-skill/
├── SKILL.md（概览，指向参考文件）
└── reference/
    ├── finance.md（收入指标）
    ├── sales.md（管道数据）
    └── product.md（使用分析）
```

用户问收入时，代理阅读 SKILL.md，看到 `reference/finance.md`，再用 bash 只读该文件。其他文件留在磁盘，直到需要才占用 token。这正是渐进披露。

完整架构见技能总览的[技能如何工作](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work)。

### MCP 工具引用

技能使用 MCP（Model Context Protocol）工具时，始终用完全限定名，避免“工具找不到”。

**格式**：`ServerName:tool_name`

**示例**：

```markdown  theme={null}
使用 BigQuery:bigquery_schema 工具查询表模式。
使用 GitHub:create_issue 工具创建议题。
```

其中：

* `BigQuery`、`GitHub` 是 MCP 服务器名

* `bigquery_schema`、`create_issue` 是工具名

无服务器前缀时，多 MCP 环境中代理可能找不到工具。

### 不要假定工具已安装

不要假定包可用：

````markdown  theme={null}
**错误示例：假定已安装**：
“用 pdf 库处理文件。”

**正确示例：明确依赖**：
“安装所需包：`pip install pypdf`

然后使用：
```python
from pypdf import PdfReader
reader = PdfReader("file.pdf")
```
”
````

## 技术说明

### YAML 前置元数据要求

SKILL.md 要求 `name`（最多 64 字符）和 `description`（最多 1024 字符）。完整结构见[技能总览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#skill-structure)。

### Token 预算

SKILL.md 正文建议低于 500 行；过长时用前述渐进披露拆文件。架构见[技能总览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work)。

## 有效技能检查清单

分享前检查：

### 核心质量

* [ ] 描述具体且含关键术语

* [ ] 描述包含做什么和何时使用

* [ ] SKILL.md 少于 500 行

* [ ] 额外细节在独立文件（需要时）

* [ ] 无时间敏感信息（或位于“旧模式”节）

* [ ] 全文术语一致

* [ ] 示例具体不抽象

* [ ] 文件引用只有一层深度

* [ ] 渐进披露使用适当

* [ ] 工作流步骤清楚

### 代码与脚本

* [ ] 脚本解决问题而不推给代理

* [ ] 错误处理明确有帮助

* [ ] 无“巫术常量”，所有值有理由

* [ ] 指令列出所需包且确认可用

* [ ] 脚本有清楚文档

* [ ] 无 Windows 风格路径（全用正斜杠）

* [ ] 关键操作有验证步骤

* [ ] 质量关键任务有反馈循环

### 测试

* [ ] 至少三次评估

* [ ] 用 Haiku、Sonnet、Opus 测试

* [ ] 用真实场景测试

* [ ] 纳入团队反馈（适用时）

## 下一步

<CardGroup cols={2}>
  <Card title="开始使用 Agent Skills" icon="rocket" href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart">
    创建第一个技能
  </Card>

<Card title="在 Claude Code 中使用技能" icon="terminal" href="https://code.claude.com/docs/en/skills">
    在 Claude Code 中创建管理技能
  </Card>

<Card title="通过 API 使用技能" icon="code" href="https://platform.claude.com/docs/en/build-with-claude/skills-guide">
    以程序方式上传使用技能
  </Card>
</CardGroup>
