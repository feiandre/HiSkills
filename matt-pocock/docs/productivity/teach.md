## What it does

<!-- zh-CN:begin 0368a2a9df4af20c -->

## 它做什么

<!-- zh-CN:end 0368a2a9df4af20c -->

`teach` turns the directory you run it in into a standing teaching workspace and teaches you one topic across many [sessions](https://www.aihero.dev/ai-coding-dictionary/session), in short self-contained HTML lessons.

<!-- zh-CN:begin 318889d035b3c581 -->

`teach` 将运行目录变成常驻教学空间，通过多[会话](https://www.aihero.dev/ai-coding-dictionary/session)以短小自含 HTML 课程教授一个主题。

<!-- zh-CN:end 318889d035b3c581 -->

It does not teach from what the [model](https://www.aihero.dev/ai-coding-dictionary/model) already knows. It treats [parametric knowledge](https://www.aihero.dev/ai-coding-dictionary/parametric-knowledge) as untrusted. Before it teaches, it finds high-trust resources, records them in `RESOURCES.md`, and cites them inside every lesson. It is also [stateful](https://www.aihero.dev/ai-coding-dictionary/stateful). The mission, the resources, the lessons and the record of what you have learned all live as files in the directory, so the next session continues from those files, not from what is left of the last conversation.

<!-- zh-CN:begin 0530e761051dfa32 -->

它不依据[模型](https://www.aihero.dev/ai-coding-dictionary/model)已知内容教学，而把[参数化知识](https://www.aihero.dev/ai-coding-dictionary/parametric-knowledge)视为不可信。教学前寻找可信资源，写入 `RESOURCES.md` 并在每课引用。它也是[有状态](https://www.aihero.dev/ai-coding-dictionary/stateful)的：使命、资源、课程和学习记录都存为文件，下次会话从文件继续，而非上次对话残留。

<!-- zh-CN:end 0530e761051dfa32 -->

## When to reach for it

<!-- zh-CN:begin 4d3d6fc77942e540 -->

## 何时使用

<!-- zh-CN:end 4d3d6fc77942e540 -->

You invoke this by typing `/teach`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own.

<!-- zh-CN:begin dc51a8a522c26021 -->

输入 `/teach` 调用；[代理](https://www.aihero.dev/ai-coding-dictionary/agent)不会自行使用。

<!-- zh-CN:end dc51a8a522c26021 -->

Reach for it when the learning is the project: a language, a framework, a codebase you have just joined, yoga, shaders, a certification. It is not the tool for one explanation in passing.

<!-- zh-CN:begin 6c0a4ccabbb7fd85 -->

学习本身就是项目时使用：语言、框架、刚加入的代码库、瑜伽、着色器、认证。它不是临时解释一个概念的工具。

<!-- zh-CN:end 6c0a4ccabbb7fd85 -->

| What you want | What to reach for |
| --- | --- |
| To learn a topic over weeks, with sessions that accumulate | `teach` |
| One idea explained inside the session you are already in | Just ask, in that session |
| The agent's last message re-pitched because it didn't land | [wait-what](https://aihero.dev/skills-wait-what) |
| To sharpen thinking you already have, rather than acquire new material | [grill-me](https://aihero.dev/skills-grill-me) |
| A background agent to read [primary sources](https://www.aihero.dev/ai-coding-dictionary/primary-source) and leave you a cited document | [research](https://aihero.dev/skills-research) |
| To learn something that came up mid-grilling, without derailing the [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) | [handoff](https://aihero.dev/skills-handoff) out to a teaching workspace, then `teach` there |

<!-- zh-CN:begin ce6cd905dc12089b -->

| 你想要 | 使用 |
| --- | --- |
| 数周内跨会话累积学习主题 | `teach` |
| 在当前会话解释一个想法 | 直接在会话中提问 |
| 代理上一条消息没讲清，需要重讲 | [wait-what](https://aihero.dev/skills-wait-what) |
| 深化已有思考，而非获取新材料 | [grill-me](https://aihero.dev/skills-grill-me) |
| 后台代理阅读[一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)并留下带引用文档 | [research](https://aihero.dev/skills-research) |
| 学习追问中出现的内容又不打断[追问](https://www.aihero.dev/ai-coding-dictionary/grilling) | 用 [handoff](https://aihero.dev/skills-handoff) 转到教学空间，在那里 `teach` |

<!-- zh-CN:end ce6cd905dc12089b -->

## Prerequisites

<!-- zh-CN:begin 63233af066c1a2d1 -->

## 前提

<!-- zh-CN:end 63233af066c1a2d1 -->

`teach` builds a directory rather than producing a file, and the skill assumes one mission per workspace, so run it somewhere you are happy to give over to a single topic. Keep it out of the project you are working in. A separate repo is the best home, better than a global `~/.learnings/` folder or the working project itself. A dedicated repo also lets you commit the lessons, which is how teams have shared them.

<!-- zh-CN:begin 35a04eac085888ae -->

`teach` 构建目录而非单文件，并假定一个工作区一个使命；应在愿意专用于单一主题的位置运行，放在工作项目外。独立仓库最佳，优于全局 `~/.learnings/` 或项目本身。独立仓库还能提交课程，便于团队共享。

<!-- zh-CN:end 35a04eac085888ae -->

What accumulates in that directory:

<!-- zh-CN:begin 4029f25e67de1a66 -->

目录累积内容：

<!-- zh-CN:end 4029f25e67de1a66 -->

| Path | What it holds |
| --- | --- |
| `MISSION.md` | Why you are learning this. Every other file depends on it. If it is missing, the first thing `teach` does is interview you until it isn't |
| `RESOURCES.md` | The vetted sources it teaches from, split into Knowledge and Wisdom (communities) |
| `lessons/*.html` | The numbered lessons: the primary unit of teaching |
| `reference/*.html` | Compressed cheat-sheets, algorithms, glossaries: the documents you return to |
| `learning-records/*.md` | ADR-style notes on what you have demonstrably learned, used to decide what to teach next |
| `assets/*` | Reusable components, starting with a shared stylesheet, so the lessons look like one course |
| `NOTES.md` | Your stated teaching preferences |

<!-- zh-CN:begin 6721a7accebc53b9 -->

| 路径 | 内容 |
| --- | --- |
| `MISSION.md` | 学习原因；其他文件依赖它。缺失时 `teach` 首先访谈直到补齐 |
| `RESOURCES.md` | 已审查资源，分为知识与智慧（社群） |
| `lessons/*.html` | 编号课程，主要教学单元 |
| `reference/*.html` | 压缩备忘单、算法、术语表，供回来查阅 |
| `learning-records/*.md` | ADR 风格记录已证明掌握内容，用于选择下一课 |
| `assets/*` | 可复用组件，首先是共享样式表，使课程像同一门课 |
| `NOTES.md` | 你声明的教学偏好 |

<!-- zh-CN:end 6721a7accebc53b9 -->

Two notes on that list. A glossary suits most topics, but the skill ships a `GLOSSARY-FORMAT.md` that `SKILL.md` no longer links to, so you only get one if you ask ([issue #559](https://github.com/mattpocock/skills/issues/559)). All of it lands in the directory you ran `/teach` in.

<!-- zh-CN:begin a66ecba6980187ae -->

两项说明：术语表适合多数主题，但 `SKILL.md` 已不再链接随附的 `GLOSSARY-FORMAT.md`，只有主动要求才生成（[议题 #559](https://github.com/mattpocock/skills/issues/559)）。所有内容都落在运行 `/teach` 的目录。

<!-- zh-CN:end a66ecba6980187ae -->

## Storage strength, not fluency

<!-- zh-CN:begin 4614b7974ef0aaf2 -->

## 存储强度而非流畅感

<!-- zh-CN:end 4614b7974ef0aaf2 -->

The word to think with is **storage strength**: long-term retention, as opposed to **fluency**, the in-the-moment recall that feels like mastery while you are reading and is gone a week later. `teach` builds the former through desirable difficulty: retrieval practice, spacing, interleaving. Knowledge comes first. At that stage difficulty works against you, because it uses up the working memory you need to understand. Then `teach` drills the skill through a tight feedback loop, and at that stage difficulty is the tool.

<!-- zh-CN:begin 988be4825658bdb2 -->

应记住的是**存储强度**：长期保留；相对的是**流畅感**，阅读时仿佛掌握的即时回忆，一周后消失。`teach` 通过合意困难建立前者：提取练习、间隔、交错。先学知识；此时困难会占用理解所需工作记忆，适得其反。随后通过紧凑反馈循环训练技能，此时困难是工具；其中相关的字段或标识包括 `teach`。

<!-- zh-CN:end 988be4825658bdb2 -->

Two things decide what you get taught. The **mission** (the concrete real-world reason you want this) is the basis of every lesson. Without it the lessons become abstract and nothing decides what comes next. From the mission and the learning records, `teach` picks the next lesson inside your **zone of proximal development**: hard enough to take effort, but not so far ahead that you cannot learn it.

<!-- zh-CN:begin 848babb5a14b4de7 -->

两项决定教学内容。**使命**（具体真实原因）是每课基础；缺失会使内容抽象、无法决定下一步。根据使命与学习记录，`teach` 在**最近发展区**选择下一课：需要努力但尚未远到学不会。

<!-- zh-CN:end 848babb5a14b4de7 -->

Storage strength is also why the skill pushes back instead of agreeing. A question that needs **wisdom** (real-world judgement) gets an attempted answer and then a pointer to a community where you can test it. The skill does not let you skip a quiz. One user reported saying "thanks a lot" and being told the drill was not finished.

<!-- zh-CN:begin ee726365fd4b5944 -->

存储强度也是技能会反驳而非附和的原因。需要**智慧**（现实判断）的问题先尝试回答，再指向可检验的社群。技能不允许跳过测验。一位用户说“非常感谢”，却被提示练习未完成。

<!-- zh-CN:end ee726365fd4b5944 -->

## Lessons, references and components

<!-- zh-CN:begin fe908b6af975845e -->

## 课程、参考与组件

<!-- zh-CN:end fe908b6af975845e -->

A **lesson** is one self-contained HTML file, short enough to finish in a sitting, tied to the mission, giving one tangible win. It cites its sources, recommends one primary source to go and read yourself, and links to sibling lessons and reference documents.

<!-- zh-CN:begin 83feec1c3ad2fac0 -->

**课程**是一个自含 HTML 文件，短到一次坐定即可完成，联系使命并带来一个实际成果。它引用来源，推荐一个自行阅读的一手来源，并链接同级课和参考文档。

<!-- zh-CN:end 83feec1c3ad2fac0 -->

You rarely go back to a lesson, but you do go back to reference documents. So the short form of a lesson (the syntax table, the algorithm, the pose sequence, the glossary) belongs in `reference/`, not buried in the lesson that introduced it.

<!-- zh-CN:begin 6e9aa2609dd71fd6 -->

课程很少重看，参考文档会重看。因此课程的短表（语法表、算法、姿势序列、术语表）放在 `reference/`，不要埋在首次介绍它的课中。

<!-- zh-CN:end 6e9aa2609dd71fd6 -->

Lessons are built from **components** in `assets/`: stylesheets, quiz widgets, simulators, diagram helpers. Reuse is the default. The agent reads `assets/` before authoring a lesson and builds from what is there. It writes anything new that a second lesson could use as a component, not inline. The shared stylesheet is the first component in every workspace, and it makes the lessons look like one course instead of many unrelated pages.

<!-- zh-CN:begin 306864c2d0b0889f -->

课程由 `assets/` 中**组件**构建：样式表、测验控件、模拟器、图示辅助。默认复用；代理编写前读取 `assets/` 并基于现有内容。第二个课程可用的新内容写成组件，不内联。共享样式表是每个空间首个组件，使课程像同一门课。

<!-- zh-CN:end 306864c2d0b0889f -->

## Common questions

<!-- zh-CN:begin d6646f71bf240880 -->

## 常见问题

<!-- zh-CN:end d6646f71bf240880 -->

**Where does it put the files? Mine ended up in `~/.claude/skills`.**
In the directory you ran `/teach` in ([#377](https://github.com/mattpocock/skills/issues/377)).

<!-- zh-CN:begin ce83dae8099bbcda -->

**文件放在哪里？我的到了 `~/.claude/skills`。**
应放在运行 `/teach` 的目录（[#377](https://github.com/mattpocock/skills/issues/377)）。

<!-- zh-CN:end ce83dae8099bbcda -->

**Do I stay in one session, or start a new one per lesson?**
All three approaches work: staying in the same session, re-invoking `/teach` in a new session, or opening a new session in the same folder. Each lesson is its own invocation. The course state lives in the folder, not in the conversation. Common practice is to open a fresh session in the workspace and say `/teach next lesson for <topic>`.

<!-- zh-CN:begin 528d09d100989c21 -->

**同一会话继续，还是每课新会话？**
都可：同会话、在新会话重新 `/teach`，或在同一文件夹新会话。每课各自调用；课程状态在文件夹，不在对话。常见做法是在工作区新会话说 `/teach next lesson for <topic>`。

<!-- zh-CN:end 528d09d100989c21 -->

**How do I know it isn't teaching me something it made up?**
You don't, on the skill's word alone. You read the primary sources. `teach` is not reliable enough to trust unchecked, and no skill built on an LLM is. The grounding (`RESOURCES.md`, citations in every lesson, one recommended primary source per lesson) makes it cheap to check a lesson. It does not remove the need to check. This failure has happened: one user learning a 2x2 Rubik's cube got made-up move sequences that don't solve it. In a case like that, check the model, the harness, the effort setting, and the source. Risk is highest in procedural domains with precise notation, and lowest where the output is immediately verifiable, like code you can run.

<!-- zh-CN:begin 7ea5a9e59b007431 -->

**怎么知道没有编造？**
仅凭技能说法不能知道，必须读一手来源。`teach` 不能未经检查就信任，基于 LLM 的技能都如此。资源、每课引用与一个推荐来源让检查成本降低，但不消除检查。曾有学 2×2 魔方得到无法还原的步骤。遇到此情况检查模型、平台、努力设置和来源。精确定义的程序领域风险最高；可立即验证的输出（如代码）最低；其中相关的字段或标识包括 `RESOURCES.md`。

<!-- zh-CN:end 7ea5a9e59b007431 -->

**The correct quiz answer is always the first option.**
Several people have confirmed this on Sonnet, Opus and GLM, and it is still unfixed. `SKILL.md` now requires every answer to be the same number of words. That removes a different clue (the correct answer used to be the only fully-reasoned one), but says nothing about position. One contributor tested an instruction-level fix for position, and the correct answer still landed in slot A 33 times out of 33 across nine lessons ([#335](https://github.com/mattpocock/skills/issues/335)). So the real fix is a quiz component in `assets/` that shuffles the answers, not better wording. Until that ships, ignore answer position. Your `assets/` directory is yours to change, so you can ask for a component that shuffles at render time as a local fix.

<!-- zh-CN:begin f0d1102f1d05eb25 -->

**正确测验答案总在第一个。**
多位用户在 Sonnet、Opus、GLM 确认，仍未修复。`SKILL.md` 现要求每个答案词数相同，去掉了另一线索（过去正确答案唯一充分论证），但没有处理位置。一次指令级修复测试中，九课的正确项 33/33 都在 A（[#335](https://github.com/mattpocock/skills/issues/335)）。真正修复是 `assets/` 中渲染时打乱答案的测验组件，不是改措辞。发布前忽略位置；可要求本地组件修复；其中相关的字段或标识包括 `assets/`。

<!-- zh-CN:end f0d1102f1d05eb25 -->

**It assumed I already knew things, and used terms it never defined.**
This is the most common real complaint. There is no assessment step. `teach` infers your level from the mission and the learning records, and in session one there are no learning records. One user running it inside a wayfinder pipeline put it plainly: "It never did grilling to establish my starting point so it made lots of assumptions of what I already knew." Another reported lessons that used undefined jargon, and a lesson about their hardware that covered what the hardware could do but never said what it couldn't. Two things help: state your prior knowledge and your gaps in the first message, and correct the level out loud when a lesson misses, because the correction becomes a learning record and steers the next one. An explicit knowledge-assessment step is a standing feature request ([#725](https://github.com/mattpocock/skills/issues/725)), not shipped behaviour.

<!-- zh-CN:begin d4b0349daba29a72 -->

**它假定我已知未定义术语。**
这是最常见真实抱怨。没有评估步骤，`teach` 从使命和学习记录推断水平，首课尚无记录。一位用户直说：“它没有追问确定起点，所以假定了我很多已知内容。” 另有人遇到未定义术语，以及只讲硬件能做、不讲不能做的课程。两条建议：首条消息说明既有知识和缺口；课程不合适时明确纠正，纠正会成为记录并影响下一课。显式知识评估是持续功能请求（[#725](https://github.com/mattpocock/skills/issues/725)），尚未发布。

<!-- zh-CN:end d4b0349daba29a72 -->

**Does it do spaced repetition, and does it know when to stop teaching?**
No to the first, and not reliably to the second. The skill designs lessons around spacing and interleaving, but nothing schedules a review, and there is no Anki or calendar integration. Users ask for both often. A related gap is exit criteria. As one user put it, `teach` "is good at making the next lesson, but not as good at knowing when to stop and switch to review or real practice." If you want review or drilling instead of new material, ask for it; the skill will not propose the switch on its own.

<!-- zh-CN:begin 4e033bbb1caebd28 -->

**支持间隔重复并知道何时停止吗？**
前者不支持，后者不可靠。课程按间隔和交错设计，但不安排复习，无 Anki 或日历集成。用户常请求两者。退出标准也缺：如用户所说，`teach` “擅长下一课，却不擅长判断何时停止并转复习或实践。” 想要复习或训练就明确要求，技能不会主动切换。

<!-- zh-CN:end 4e033bbb1caebd28 -->

**Is it only useful for code?**
No. Most reported use is outside coding: Korean, Japanese formal register, piano, guitar, board game design, OpenSCAD, film plots, Azure and CCNA certifications, university exams, and children of eight and ten getting printable books on escape rooms and fire salamanders. Nothing in the skill is specific to programming. Mission, resources, zone of proximal development and drill work the same way in any domain. Within code, users report the most value from getting oriented in an unfamiliar codebase or a new team's stack, more than from learning a language from scratch.

<!-- zh-CN:begin f76ef2bd7a7ddd6e -->

**只适合代码吗？**
不是。多数使用在编程外：韩语、日语正式语体、钢琴、吉他、桌游设计、OpenSCAD、电影情节、Azure/CCNA 认证、大学考试，以及八岁和十岁孩子关于密室逃脱和火蝾螈的可打印书。使命、资源、最近发展区和训练在各领域通用。代码中最有价值通常是熟悉陌生代码库或团队技术栈。

<!-- zh-CN:end f76ef2bd7a7ddd6e -->

**Which model should I run it with?**
There is no canonical answer, and the reported differences are large. Users report that higher [reasoning effort](https://www.aihero.dev/ai-coding-dictionary/effort) produces better lessons than the medium setting. One user ran the same skill through Copilot CLI with Codex and got a single 30-line HTML card where Claude Code produced a full lesson. It runs unmodified in Claude Cowork, if your organisation lets you add skills there. If the lessons come out thin, change model, [harness](https://www.aihero.dev/ai-coding-dictionary/harness) or effort before rewriting your prompt.

<!-- zh-CN:begin 52dcfead7fc3f884 -->

**用哪个模型？**
没有标准答案，差异很大。用户报告更高[推理努力](https://www.aihero.dev/ai-coding-dictionary/effort)比中等更好。有人用 Copilot CLI 加 Codex 只得到 30 行 HTML 卡，Claude Code 则生成完整课程。若组织允许可原样在 Claude Cowork 使用。课程太薄时先换模型、[平台](https://www.aihero.dev/ai-coding-dictionary/harness)或努力，不要先重写提示。

<!-- zh-CN:end 52dcfead7fc3f884 -->

## It's working if

<!-- zh-CN:begin 15bf1328239fb747 -->

## 怎样算正常工作

<!-- zh-CN:end 15bf1328239fb747 -->

- The first thing it does in an empty directory is interview you about why you want this, rather than produce a lesson.

<!-- zh-CN:begin 413ee7ff5e30a3a4 -->

- 空目录首次行为是访谈为何学习，而非直接出课。

<!-- zh-CN:end 413ee7ff5e30a3a4 -->
- `RESOURCES.md` fills up before the lessons do, and each lesson names one primary source worth reading yourself.

<!-- zh-CN:begin 3d858916ffc40396 -->

- 课程出现前 `RESOURCES.md` 已填充，每课推荐一个值得自读的一手来源。

<!-- zh-CN:end 3d858916ffc40396 -->
- Claims in a lesson carry links out. A lesson with no citations is the skill teaching from memory.

<!-- zh-CN:begin f5c50dd8c4916f59 -->

- 课程主张外链来源；无引用是凭记忆教学。

<!-- zh-CN:end f5c50dd8c4916f59 -->
- A lesson takes one sitting and leaves you able to do one thing you couldn't before.

<!-- zh-CN:begin 6f9c5ed359e78730 -->

- 一课一次完成，留下一个以前做不到的实际能力。

<!-- zh-CN:end 6f9c5ed359e78730 -->
- Opening a fresh session in the folder and saying "next lesson" continues the course instead of restarting it.

<!-- zh-CN:begin 60a84454184558da -->

- 在文件夹新会话说“下一课”能继续而非重开。

<!-- zh-CN:end 60a84454184558da -->
- `learning-records/` grows, and lessons stop re-teaching what you have already demonstrated.

<!-- zh-CN:begin 1d7174214ff90970 -->

- `learning-records/` 增长，课程不再重复已证明内容。

<!-- zh-CN:end 1d7174214ff90970 -->
- The lessons look like one course: they link the stylesheet in `assets/` rather than each carrying its own.

<!-- zh-CN:begin 96cd0a5d2539aa1f -->

- 课程像同一门课，链接 `assets/` 样式表，而非各自携带。

<!-- zh-CN:end 96cd0a5d2539aa1f -->
- A question that needs judgement gets you pointed at a forum, subreddit or class, not just an answer.

<!-- zh-CN:begin 4ee5d428b9a1b891 -->

- 需要判断的问题会指向论坛、子版块或课程，不只是一句答案。

<!-- zh-CN:end 4ee5d428b9a1b891 -->

## Where it fits

<!-- zh-CN:begin 54113ea6dfab2821 -->

## 适用范围

<!-- zh-CN:end 54113ea6dfab2821 -->

`teach` is a **reach-for-it-anytime standalone**. It is not a step in a build chain and shares no artifacts with the engineering flow; it works in its own directory for as long as you study the topic.

<!-- zh-CN:begin b9d39e43b9a14758 -->

`teach` 是无依赖独立技能，不属于构建链，不共享工程产物；只要学习，就在自己的目录工作。

<!-- zh-CN:end b9d39e43b9a14758 -->

Its one real neighbour is [handoff](https://aihero.dev/skills-handoff). Together they answer "what do I do if I'm being grilled about something I don't understand?" Don't stop the grilling to learn. `/handoff` to a teaching workspace, learn the topic there with `/teach`, then go back and continue where you left off. The nearby alternative is [research](https://aihero.dev/skills-research), for when what you want is a cited document rather than lessons and retention. When you are not sure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you over the whole set.

<!-- zh-CN:begin 2729efa90a522474 -->

唯一邻近者是 [handoff](https://aihero.dev/skills-handoff)。二者回答“被追问不懂内容怎么办”：不要停下追问学习；用 `/handoff` 转到教学空间，`/teach` 学习，再回来继续。邻近替代是 [research](https://aihero.dev/skills-research)，适合要带引用文档而非课程与记忆。不确定时 [ask-matt](https://aihero.dev/skills-ask-matt) 路由。

<!-- zh-CN:end 2729efa90a522474 -->
