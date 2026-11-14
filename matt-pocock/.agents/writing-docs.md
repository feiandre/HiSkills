# Writing docs pages

<!-- zh-CN:begin bb2dcca4b5419990 -->

# 编写文档页面

<!-- zh-CN:end bb2dcca4b5419990 -->

Every skill in `engineering/` and `productivity/` has a human-facing **docs page** at `docs/<bucket>/<skill-name>.md`. The docs tree mirrors those two bucket folders under `skills/`. It is published at `https://aihero.dev/skills-<skill-name>`; the URL is always `skills-<skill-name>` regardless of bucket, so the docs path is repo organisation only. The page is not the skill and not a copy of `SKILL.md`. Only these two buckets are promoted; the rest (`misc/`, `in-progress/`, `deprecated/`) ship no docs page.

<!-- zh-CN:begin ea5b4a4d8bf7d836 -->

`engineering/` 与 `productivity/` 中每项技能都有面向人的**文档页面**，位于 `docs/<bucket>/<skill-name>.md`。文档树镜像 `skills/` 下这两个桶目录。页面发布在 `https://aihero.dev/skills-<skill-name>`；无论所属桶为何，URL 始终是 `skills-<skill-name>`，因此文档路径只反映仓库组织。页面不是技能，也不是 `SKILL.md` 的复制品。只有这两个桶会被推广；其余（`misc/`、`in-progress/`、`deprecated/`）不提供文档页面。

<!-- zh-CN:end ea5b4a4d8bf7d836 -->

Most of these skills are **user-invoked**: the agent will never fire them for you, so *you* are the index that has to remember they exist and when to reach for them. That memory is **cognitive load**. The job of a docs page is to relieve it: to orient one reader around one skill so they can hold it in their head, know when to reach for it, and see where it sits in the system. The pages are collectively a distributed router; each is a node.

<!-- zh-CN:begin 75d491835a711662 -->

这些技能大多由**用户调用**：代理不会替你触发，所以*你*才是必须记住它们存在、以及何时使用的索引。这种记忆构成**认知负担**。文档页面的职责就是减轻负担：围绕一项技能帮助一位读者定位，使其能记在脑中、知道何时使用，并理解它在系统中所处的位置。这些页面共同组成一个分布式路由器；每一页都是节点。

<!-- zh-CN:end 75d491835a711662 -->

Act whenever a promoted skill is added, renamed, or has its behaviour changed: create or re-sync its docs page. A rename moves the file too (`docs/<bucket>/<old>.md` → `docs/<bucket>/<new>.md`), because the published URL tracks the name; a skill that moves between `engineering/` and `productivity/` moves its docs file to the matching folder. Skills in `misc/`, `in-progress/`, and `deprecated/` get no page, because none of those buckets is promoted. A skill moving *out* of one of them into `engineering/` or `productivity/` gains a page; one moving the other way loses it. A promoted skill that is removed outright keeps its page as an **archived** page: leave the body as it was and open it with a blockquote notice (`> **Archived.** ...`) naming the version it was removed in and any replacement, so the published URL keeps resolving.

<!-- zh-CN:begin 6330e8bcdb7fa0ee -->

每当推广的技能新增、重命名或行为改变时，都应行动：创建或重新同步其文档页面。重命名时文件也移动（`docs/<bucket>/<old>.md` → `docs/<bucket>/<new>.md`），因为发布 URL 跟随名称；在 `engineering/` 与 `productivity/` 之间移动的技能，其文档文件也移到对应文件夹。`misc/`、`in-progress/`、`deprecated/` 中的技能不获得页面，因为这些桶都未推广。技能从这些桶移入 `engineering/` 或 `productivity/` 时获得页面；反向移动则失去页面。完全移除的推广技能保留其页面并标为**已归档**：保持正文原样，并以引用块通知（`> **Archived.** ...`）开头，注明移除版本及任何替代方案，使已发布 URL 继续可解析。

<!-- zh-CN:end 6330e8bcdb7fa0ee -->

Because these pages are published on `aihero.dev`, **every link is absolute**: never a repo-relative path. A link to another skill points at `https://aihero.dev/skills-<name>`; a link into the repo points at its full `https://github.com/mattpocock/skills/...` URL. A relative link that works in the repo breaks once published.

<!-- zh-CN:begin 3c5ce9b07a5c5f26 -->

由于这些页面发布在 `aihero.dev` 上，**每个链接都必须使用绝对地址**：绝不使用仓库相对路径。指向其他技能的链接使用 `https://aihero.dev/skills-<name>`；指向仓库中的内容的链接使用完整 `https://github.com/mattpocock/skills/...` URL。仓库内可用的相对链接发布后就会失效。

<!-- zh-CN:end 3c5ce9b07a5c5f26 -->

There is no H1. The published page takes its title from the slug.

<!-- zh-CN:begin aea5d3164dfe774d -->

没有 H1。已发布页面从 slug 获取标题。

<!-- zh-CN:end aea5d3164dfe774d -->

## Page structure

<!-- zh-CN:begin f753c0c3e86fbf99 -->

## 页面结构

<!-- zh-CN:end f753c0c3e86fbf99 -->

Fill the template below, keeping its order. The **fixed frame** (`## What it does`, `## When to reach for it`, `## Where it fits`) appears on every page. `## Prerequisites` and the free-form substance sections carry only what this particular skill needs; delete the rest.

<!-- zh-CN:begin b22b80095a75b943 -->

按下述模板填写，并保留其顺序。**固定框架**（`## What it does`、`## When to reach for it`、`## Where it fits`）出现在每页上。`## Prerequisites` 及自由形式的核心部分只保留该技能所需内容；其余删除。

<!-- zh-CN:end b22b80095a75b943 -->

Four sections make a page worth reading: `What it does`, `When to reach for it`, `Common questions`, `It's working if`. The first two orient the reader; the last two are where the page stops summarising the skill and starts answering the reader's own situation. Each of the last two has a bar to clear, below, but treat a page that clears neither as unfinished, not as finished-and-short.

<!-- zh-CN:begin 8a2c4bbd36e60dc1 -->

四个部分使页面值得阅读：`What it does`、`When to reach for it`、`Common questions`、`It's working if`。前两部分帮助读者定位；后两部分让页面从概括技能转向回答读者自身的情境。下面为后两部分各设定标准；两者均未达到标准的页面应视为未完成，不能当成已完成但简短的页面。

<!-- zh-CN:end 8a2c4bbd36e60dc1 -->

**A page carries no install commands.** The ai-hero page template renders the install widget itself (a copy button, the single-skill command, the whole-set command, and the update line) above the body. A page that also writes them out shows the reader the same command twice, and the two copies drift: the hand-written pair on every page went stale against the widget beside it. Install wording is a property of the site, not of the page. If it needs changing, change it in ai-hero; the canonical wording lives in [the install block](./install-block.md).

<!-- zh-CN:begin ef552da69d136189 -->

**页面不包含安装命令。**ai-hero 页面模板会在正文上方自行渲染安装组件（复制按钮、单技能命令、整套命令及更新行）。若页面再次写出命令，读者会看到同一命令两次，而且两个副本会漂移：每页手写的命令已经与旁边组件不一致。安装文案属于网站的属性，不属于页面。若需改动，请在 ai-hero 中修改；规范文案位于[安装块](./install-block.md)。

<!-- zh-CN:end ef552da69d136189 -->

<page-template>

<!-- zh-CN:begin 6b56ca762478a028 -->

<page-template>

<!-- 页面模板开始 -->

<!-- zh-CN:end 6b56ca762478a028 -->

## What it does

<!-- zh-CN:begin f35ff0de467ef465 -->

## 作用

<!-- zh-CN:end f35ff0de467ef465 -->

One or two plain-language paragraphs. Lead with the skill's one-sentence job, then state the **defining constraint**: the single fact that makes this skill behave differently from the obvious default (for `to-spec`: it does not interview the user again, it synthesises what is already known). Write it as a plain declarative sentence, never a labelled aside like "The defining constraint:" or "The key thing:"; the formula reads as filler. This line is the most valuable on the page; never omit it.

<!-- zh-CN:begin 6b5c7380ffcff7db -->

一到两段平实语言。先写技能一句话的职责，然后说明**决定性约束**：使该技能与显而易见的默认做法不同的事（对 `to-spec` 而言：它不再次访谈用户，而会综合已知内容）。用平实陈述句表达，绝不使用“决定性约束：”或“关键之处：”之类的标签式旁白；套话读起来像填充。这一行是页面最有价值的内容；绝不能省略。

<!-- zh-CN:end 6b5c7380ffcff7db -->

## When to reach for it

<!-- zh-CN:begin 607e44b22c6efb35 -->

## 何时使用

<!-- zh-CN:end 607e44b22c6efb35 -->

How and when you reach for the skill, in two beats that are both effectively always present:

<!-- zh-CN:begin 21da01999a9b09e3 -->

说明你如何以及何时使用该技能，分两个几乎总是存在的部分：

<!-- zh-CN:end 21da01999a9b09e3 -->

- **Invocation mode.** State whether you type it or the agent fires it. A user-invoked skill: "You invoke this by typing `/<name>`, and the agent won't reach for it on its own." A model-invoked skill: "Type `/<name>`, or the agent reaches for it automatically when a task fits."

<!-- zh-CN:begin 9fffcd8281cc5dac -->

- **调用模式。**说明是你键入命令，还是代理触发。用户调用型技能：“你通过键入 `/<name>` 调用，代理不会自行使用它。”模型调用型技能：“键入 `/<name>`，或代理在任务适合时自动使用它。”

<!-- zh-CN:end 9fffcd8281cc5dac -->
- **Trigger boundary.** The index entry: "reach for this when …". Where the skill is confusable with a sibling, add the other half: "for <X> instead, use [<sibling>](https://aihero.dev/skills-<sibling>)."

<!-- zh-CN:begin 1efd61dd2b540e38 -->

- **触发边界。**这就是索引条目：“在……时使用”。若该技能易与相邻技能混淆，补足另一半：“若需要 <X>，改用[<sibling>](https://aihero.dev/skills-<sibling>)。”

<!-- zh-CN:end 1efd61dd2b540e38 -->

## Prerequisites

<!-- zh-CN:begin 32c68014cd0a1ad5 -->

## 前置条件

<!-- zh-CN:end 32c68014cd0a1ad5 -->

Optional: include only when the skill needs something in place to be functional; omit the heading entirely otherwise. Covers: a **workspace it writes into** (a stateful skill like `grill-with-docs` writes `GLOSSARY.md` and ADRs; `teach` builds a whole directory, so say what it writes and where), **prior setup** (`triage`/`to-spec`/`to-tickets` need `setup-matt-pocock-skills` to have configured an issue tracker), or **repo-specific tooling**. A stateless skill that runs anywhere has no prerequisites, so drop the section.

<!-- zh-CN:begin e3e9a744c3fab680 -->

可选：仅当技能需要某项条件才能工作时保留，否则完全删去标题。涵盖：它会写入的**工作区**（有状态技能如 `grill-with-docs` 会写 `GLOSSARY.md` 和 ADR；`teach` 会建立整个目录，因此说明写什么、写到哪里）、**先前设置**（`triage`/`to-spec`/`to-tickets` 需要 `setup-matt-pocock-skills` 配置问题跟踪器），或**仓库专用工具**。可在任何地方运行的无状态技能没有前置条件，删除该部分。

<!-- zh-CN:end e3e9a744c3fab680 -->

## <free-form middle>

<!-- zh-CN:begin 831b3a44e648008a -->

## <free-form middle> 自由形式中间部分

<!-- zh-CN:end 831b3a44e648008a -->

One to three short sections, in the skill's *own vocabulary*, that make it click. Choose whatever headings fit the skill: the loop it runs, the artifact it produces, the fork it makes, the one anti-pattern it kills. There is no prescribed heading; the skills are too heterogeneous for one.

<!-- zh-CN:begin 794a43b49f27be98 -->

用该技能**自己的词汇**写一到三个短节，帮助它豁然贯通。选择适合该技能的标题：它运行的循环、产生的制品、作出的分叉、消除的反模式。没有规定标题；技能差异太大，无法统一。

<!-- zh-CN:end 794a43b49f27be98 -->

The single non-negotiable: **surface the skill's leading word / defining idea** (`tight` feedback loop, `deep module`, throwaway-code-answers-a-question, red-green). It pays off twice: the reader learns what the skill *is*, and learns the word they'll later think with to *reach for* it.

<!-- zh-CN:begin 2f038d9eeb7651a1 -->

唯一不可妥协之处：**呈现该技能的主导词/核心思想**（`tight` 反馈循环、`deep module`、一次性代码回答问题、red-green）。它有两重收益：读者既知道技能*是什么*，也学到日后思考并*使用它*时所需的词。

<!-- zh-CN:end 2f038d9eeb7651a1 -->

## Common questions

<!-- zh-CN:begin 9a8296770e154a58 -->

## 常见问题

<!-- zh-CN:end 9a8296770e154a58 -->

The questions readers really ask about this skill, each in bold with the answer in the lines beneath it. No sub-headings.

<!-- zh-CN:begin 4cad2a4955f5679c -->

读者确实会问的技能问题，每个问题加粗，回答写在下方各行。不设子标题。

<!-- zh-CN:end 4cad2a4955f5679c -->

An observed question always beats an invented one, so go and find them before you write any:

<!-- zh-CN:begin ead71753f7a51000 -->

观察到的问题始终胜过编造的问题，所以写之前先去寻找：

<!-- zh-CN:end ead71753f7a51000 -->

- **The wiki.** If `~/repos/matt/personal-wiki` exists on this machine, it is the richest source there is. Its `wiki/audience/` area is organised around what the audience wants, discusses, and **is confused by**: read `wiki/index.md` first for the registry of pages, then the pages bearing on this skill. Every page carries `sources:` linkbacks to the original X, Discord, GitHub, and email threads; the wiki is a secondary source, so quote the asker's own question rather than the wiki's summary of it. Skip this bullet where the directory does not exist.

<!-- zh-CN:begin 9138e2d3ce016b14 -->

- **Wiki。**若本机存在 `~/repos/matt/personal-wiki`，它是最丰富的来源。其 `wiki/audience/` 区域围绕受众想要什么、讨论什么以及**困惑什么**组织：先阅读 `wiki/index.md` 获取页面登记表，再阅读与该技能相关的页面。每页都有 `sources:` 回链到原 X、Discord、GitHub 和电子邮件线程；Wiki 是二手来源，因此引用提问者自己的问题，而非 Wiki 的摘要。目录不存在时跳过此条。

<!-- zh-CN:end 9138e2d3ce016b14 -->
- **This repo's issues.** `gh issue list --repo mattpocock/skills --search "<skill-name>" --state all`. A question filed twice is a question the page owes an answer to.

<!-- zh-CN:begin ec4293d44d6426c4 -->

- **本仓库的 issue。**`gh issue list --repo mattpocock/skills --search "<skill-name>" --state all`。被提交两次的问题，就是页面应回答的问题。

<!-- zh-CN:end ec4293d44d6426c4 -->
- **`CHANGELOG.md`.** Anything renamed, moved, or behaviourally changed generates a "where did it go?" that the page has to answer.

<!-- zh-CN:begin d2f753221e7a8a99 -->

- **`CHANGELOG.md`。**任何重命名、移动或行为变化都会产生“它去哪儿了？”的问题，页面必须回答。

<!-- zh-CN:end d2f753221e7a8a99 -->

Where the hunt comes up thin, the section may also carry a question a reader would plainly ask, but **the count stays honest to the evidence**. A well-discussed skill earns six; an obscure one earns one or two, or none at all. Padding a thin skill out to match a rich one is how the section fills with questions nobody has, and an invented question teaches the reader nothing.

<!-- zh-CN:begin bdd06b8f268462f5 -->

若搜索所得稀少，本节也可以包含读者显然会问的问题，但**数量必须忠实于证据**。讨论充分的技能可获得六个问题；冷门技能只获得一两个，甚至没有。为让内容单薄的技能与丰富技能篇幅相同而填充，会让本节充满无人提出的问题，编造的问题也无法教会读者任何内容。

<!-- zh-CN:end bdd06b8f268462f5 -->

Order them by how often each comes up, sharpest first, and say the unflattering thing where it is true: a very long grilling session usually means the scope was too big; a model asked to write its own skill produces something verbose. Omit the heading where there is nothing worth answering.

<!-- zh-CN:begin bf7b359e1c18b091 -->

按出现频率排序，最尖锐的在前，并在真实时说出不讨喜的话：极长的 grilling 会话通常说明范围太大；要求模型编写自己的技能会产出冗长内容。没有值得回答的内容时删除标题。

<!-- zh-CN:end bf7b359e1c18b091 -->

## It's working if

<!-- zh-CN:begin afcfbc6aad270714 -->

## 怎样算有效

<!-- zh-CN:end afcfbc6aad270714 -->

A few bullets naming what the reader sees when the skill is doing its job. The bar on each is that the reader can check it without opening `SKILL.md`: a signal in their own work, or in the trace in front of them. "The document gets shorter as it gets better" passes; "the library section is byte-identical to `template.sh`" is a compliance check on the skill's internals wearing this section's name. Include it wherever the tells are crisp; omit the heading where they stay vague.

<!-- zh-CN:begin c46693fe6c9660f6 -->

用若干条列出读者在技能起作用时能看到什么。每条的标准是读者无需打开 `SKILL.md` 即可检查：在他们自己的工作或眼前轨迹中的信号。“文档越改越好时反而更短”可以通过；而“库部分与 `template.sh` 逐字节相同”是借用本节之名检查技能内部是否符合要求。信号明确时保留；仍含糊时删除。

<!-- zh-CN:end c46693fe6c9660f6 -->

## Where it fits

<!-- zh-CN:begin 9d8eafca59a85556 -->

## 所处位置

<!-- zh-CN:end 9d8eafca59a85556 -->

Always present. Situate the skill in the system in a sentence or two:

<!-- zh-CN:begin a5508077b68a34f4 -->

始终保留。用一两句话将该技能放到系统中：

<!-- zh-CN:end a5508077b68a34f4 -->

- **Role.** Name it: a **chain step** (`grill-with-docs → to-spec → to-tickets → implement → code-review`), a **run-once setup** (`setup-matt-pocock-skills`), **periodic maintenance** (`improve-codebase-architecture`, "every few days"), or a **reach-for-it-anytime standalone** (`diagnosing-bugs`, `prototype`, `handoff`). A standalone's map is one honest sentence, which is far better than omitting the section.

<!-- zh-CN:begin 6e0612040c68eb91 -->

- **角色。**明确名称：**链式步骤**（`grill-with-docs → to-spec → to-tickets → implement → code-review`）、**一次性设置**（`setup-matt-pocock-skills`）、**周期维护**（`improve-codebase-architecture`，“每隔几天”），或**随时可用的独立技能**（`diagnosing-bugs`、`prototype`、`handoff`）。独立技能的地图用一句诚实的话，远胜于省略本节。

<!-- zh-CN:end 6e0612040c68eb91 -->
- **Neighbours.** The one or two siblings that matter, each with a because-clause, linked absolutely.

<!-- zh-CN:begin 83a44a9fb1b5bc58 -->

- **相邻技能。**一到两个重要相邻项，每个附“因为”从句，并使用绝对链接。

<!-- zh-CN:end 83a44a9fb1b5bc58 -->
- **The map.** Point to [ask-matt](https://aihero.dev/skills-ask-matt), the router over the whole set, so this page stays a node and never has to redraw the graph.

<!-- zh-CN:begin a08d47858f7d60f9 -->

- **地图。**指向 [ask-matt](https://aihero.dev/skills-ask-matt)，即覆盖整套技能的路由器，使本页继续作为节点，永远无需重绘图。

<!-- zh-CN:end a08d47858f7d60f9 -->

</page-template>

<!-- zh-CN:begin 7bd73cd22515d3d2 -->

</page-template>

<!-- 页面模板结束 -->

<!-- zh-CN:end 7bd73cd22515d3d2 -->

## Conventions

<!-- zh-CN:begin 4cc9a8f8917f8d7c -->

## 约定

<!-- zh-CN:end 4cc9a8f8917f8d7c -->

- Explain the **why**, not the process. The page orients and situates the skill; it never reproduces the `SKILL.md` steps or template dumps: a human choosing a tool does not need the runbook.

<!-- zh-CN:begin 4e4ac0fa50a3bcb0 -->

- 解释**为什么**，而非流程。页面帮助定位并说明技能所在位置；绝不复制 `SKILL.md` 的步骤或模板倾倒内容：选择工具的人不需要运行手册。

<!-- zh-CN:end 4e4ac0fa50a3bcb0 -->
- **Never name the author.** The page is a technical document, not a record of who said what. "Matt says", "Matt's own answer", "his position is", a quoted reply: all of it goes. A finding from the question hunt is worth keeping; its attribution is not. State the substance as a plain claim about the skill ("the fix is a direct instruction: …", "the split comes down to session count") and drop the frame. The reader is deciding whether to use a tool; an opinion carries the same weight either way, and an attributed one dates as soon as the position moves. Quoting a *user* stays fine: "one user reported …" is evidence about the skill in the wild, and stays anonymous.

<!-- zh-CN:begin cd0b413658f35bb1 -->

- **绝不点名作者。**页面是技术文档，不是“谁说过什么”的纪录。“Matt 说”“Matt 自己的答案”“他的观点是”、引用的回复：全部删除。问题调研中的发现值得保留，出处归属不值得。以关于技能的平实断言陈述实质（“修复方式是直接指示：……”，“划分取决于会话数量”），去掉框架。读者只是在决定是否使用工具；有无署名时观点权重相同，而且一旦立场改变，署名便会过时。引用*用户*没有问题：“一位用户报告……”是关于技能实际使用情况的证据，并保持匿名。

<!-- zh-CN:end cd0b413658f35bb1 -->
- Use the skill's **leading words** (_seam_, _deep module_, _tracer bullet_) so the page and the skill speak one language.

<!-- zh-CN:begin cde243c4c4c457dc -->

- 使用技能的**主导词**（_seam_、_deep module_、_tracer bullet_），使页面与技能使用同一种语言。

<!-- zh-CN:end cde243c4c4c457dc -->
- **Use the [AI Coding Dictionary](https://www.aihero.dev/ai-coding-dictionary)'s term where one exists, and link its first use on the page.** The dictionary is the house vocabulary for AI coding: _context window_, _subagent_, _harness_, _primary source_, _agent mode_. Prefer its word over a synonym you invent. Link the first occurrence of each term to `https://www.aihero.dev/ai-coding-dictionary/<slug>` (the slug is the term lowercased with non-alphanumerics as hyphens: _context window_ → `context-window`), and leave every later occurrence unlinked. Link only where the word carries the dictionary's sense: a domain *model*, background *context* or an auth *token* is a different word that happens to match. Never link inside a heading, a code span, or an existing link, and never link a word that names a skill in this repo rather than the concept. For the full term list, read `~/repos/ai/ai-coding-dictionary/dictionary/` if it exists on this machine (one file per term, the filename *is* the term), and otherwise [mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding), which is the source of truth either way.

<!-- zh-CN:begin 77a992ac8ff2ea94 -->

- **[AI 编程词典](https://www.aihero.dev/ai-coding-dictionary)中存在术语时使用其术语，并在页面首次使用时链接。**该词典是 AI 编程的惯用词汇：_context window_、_subagent_、_harness_、_primary source_、_agent mode_。优先采用其词语，而非自行发明同义词。将每个术语首次出现链接到 `https://www.aihero.dev/ai-coding-dictionary/<slug>`（slug 为术语转为小写，非字母数字字符变成连字符：_context window_ → `context-window`），后续出现均不链接。仅在词语表达词典含义时链接：领域*模型*、背景*上下文*或认证*token* 是恰好相同的另一个词。绝不在标题、代码段或现有链接内部链接，也绝不为本仓库中的技能名称而非概念链接。完整术语表：若本机存在 `~/repos/ai/ai-coding-dictionary/dictionary/` 则阅读它（每术语一个文件，文件名*就是*术语），否则使用 [mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)，两者均为事实来源。

<!-- zh-CN:end 77a992ac8ff2ea94 -->
- **Branches go in a table or a list, never in a paragraph.** Where the page presents a choice (two artifacts the skill can produce, four situations that trigger it, five options at a boundary), the reader is scanning for the one row that matches their situation. A paragraph makes them read all of it to find out. A short markdown table (condition in the left column, what to do in the right) or a bulleted list gives it back in one glance. This applies wherever the branch appears, most often in `## When to reach for it` and the free-form middle.

<!-- zh-CN:begin 2a07f03e9a907465 -->

- **分支应放在表格或列表中，绝不放在段落里。**页面呈现选择时（技能可产生的两种制品、触发它的四种情形、边界上的五个选项），读者是在扫描与自己情境匹配的那一行。段落迫使他们通读。短 Markdown 表格（左列为条件，右列为操作）或项目符号列表可让人一眼找到。适用于分支出现之处，最常见于 `## When to reach for it` 和自由形式中间部分。

<!-- zh-CN:end 2a07f03e9a907465 -->
- Keep the page itself low-load. It is documentation *about* low-cognitive-load skills; furniture (spare headings, restated links) is the thing it is arguing against.

<!-- zh-CN:begin 68d9e7709116f440 -->

- 让页面本身负担轻。它是*关于*低认知负担技能的文档；家具式内容（无用的标题、重复的链接）正是它反对的东西。

<!-- zh-CN:end 68d9e7709116f440 -->

## Done when

<!-- zh-CN:begin 2eb123a90b6fa6b1 -->

## 完成标准

<!-- zh-CN:end 2eb123a90b6fa6b1 -->

- The page exists at `docs/<bucket>/<name>.md`, and no stale page survives a rename or bucket move.

<!-- zh-CN:begin 98e405b8d7d0fd7a -->

- 页面位于 `docs/<bucket>/<name>.md`，重命名或更换桶后不残留旧页面。

<!-- zh-CN:end 98e405b8d7d0fd7a -->
- The page carries no source link and writes no install command of its own.

<!-- zh-CN:begin de2354988517bd4a -->

- 页面不含来源链接，也不自行写安装命令。

<!-- zh-CN:end de2354988517bd4a -->
- `## What it does` states the defining constraint, as plain prose rather than a labelled aside.

<!-- zh-CN:begin 3346ac8d562024c6 -->

- `## What it does` 用平实文字陈述决定性约束，而非标签式旁白。

<!-- zh-CN:end 3346ac8d562024c6 -->
- The page names no author and quotes no author: every claim stands on its own.

<!-- zh-CN:begin d462f77e91c41070 -->

- 页面不提及、不引用任何作者：每项主张都能独立成立。

<!-- zh-CN:end d462f77e91c41070 -->
- `## When to reach for it` states invocation mode and the trigger boundary.

<!-- zh-CN:begin 5f7f556c4516523b -->

- `## When to reach for it` 说明调用模式和触发边界。

<!-- zh-CN:end 5f7f556c4516523b -->
- `## Where it fits` names the role and links to `ask-matt`.

<!-- zh-CN:begin 198114effdb74b5b -->

- `## Where it fits` 指明角色并链接到 `ask-matt`。

<!-- zh-CN:end 198114effdb74b5b -->
- A prerequisite (workspace, prior setup, tooling) is stated where one exists, and the section is absent where none does.

<!-- zh-CN:begin a5e1c2aebf8174bb -->

- 存在前置条件（工作区、先前设置、工具）时予以说明，不存在时省略该节。

<!-- zh-CN:end a5e1c2aebf8174bb -->
- The middle surfaces the leading word.

<!-- zh-CN:begin aff126d0c4264210 -->

- 中间部分呈现主导词。

<!-- zh-CN:end aff126d0c4264210 -->
- Every AI Coding Dictionary term the page uses is spelt the dictionary's way, and its first use (and only its first use) links to the dictionary entry.

<!-- zh-CN:begin 9bc59ec165b8376b -->

- 页面使用的每个 AI 编程词典术语均按词典拼写，首次使用（且仅首次）链接到词典条目。

<!-- zh-CN:end 9bc59ec165b8376b -->
- Every multi-way branch is a table or a list, not a paragraph the reader has to read in full.

<!-- zh-CN:begin b6f26b780223d5b1 -->

- 每个多路分支都用表格或列表表示，而非要求读者通读的段落。

<!-- zh-CN:end b6f26b780223d5b1 -->
- The hunt for real questions ran (the wiki, the issues, the changelog), and `## Common questions` is sized to what it found, not padded to match a richer skill's page.

<!-- zh-CN:begin 556f830dd82d4c08 -->

- 已执行真实问题调研（Wiki、issue、changelog），`## Common questions` 的篇幅与所得相符，不与其他内容丰富的技能页面攀比填充。

<!-- zh-CN:end 556f830dd82d4c08 -->
- Every `## It's working if` bullet is checkable without opening `SKILL.md`.

<!-- zh-CN:begin 549f9ff32f008c9d -->

- `## It's working if` 的每条都能无需打开 `SKILL.md` 检查。

<!-- zh-CN:end 549f9ff32f008c9d -->
- The sections appear in the template's order.

<!-- zh-CN:begin 9099345aaf12cf79 -->

- 各部分按模板顺序出现。

<!-- zh-CN:end 9099345aaf12cf79 -->
- Every link is absolute, and every one resolves.

<!-- zh-CN:begin c637d06dcc0a8a50 -->

- 每个链接都是绝对地址，且全部可解析。

<!-- zh-CN:end c637d06dcc0a8a50 -->
