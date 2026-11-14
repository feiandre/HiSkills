## What it does

<!-- zh-CN:begin 07e18bdbb122cf76 -->

## 功能

<!-- zh-CN:end 07e18bdbb122cf76 -->

`prototype` writes **throwaway code that answers a question**: does this state model feel right, or what should this screen look like. The question comes first and decides what you build. A prototype that answers the wrong question is wasted, however good it looks.

<!-- zh-CN:begin a077256db1d56391 -->

`prototype`编写**用来回答问题的丢弃式代码**：状态模型是否合理，或屏幕应长什么样。问题优先，并决定构建内容；回答错问题的原型即使漂亮也浪费。

<!-- zh-CN:end a077256db1d56391 -->

Throwaway is a constraint on how the code is *written*, not a promise to destroy it. No tests, no error handling beyond what makes it run, no abstractions, no persistence, because none of that helps you learn the one thing you're trying to learn. Two things survive. The answer goes into the real code, and the prototype goes onto a branch out of main as evidence for the answer.

<!-- zh-CN:begin 826b8070e509a380 -->

丢弃式约束的是代码*写法*，不是必须销毁。无需测试，除运行必需外无错误处理、无抽象、无持久化，因为它们都不帮助学习目标。有两样保留：答案进入真实代码，原型作为答案证据提交到 main 外的分支。

<!-- zh-CN:end 826b8070e509a380 -->

## When to reach for it

<!-- zh-CN:begin 23c0db0565d13bba -->

## 何时使用

<!-- zh-CN:end 23c0db0565d13bba -->

Type `/prototype`, or the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reaches for it automatically when a task fits.

<!-- zh-CN:begin be861a821d9240e1 -->

输入`/prototype`，或任务适合时代理自动使用。 [链接](https://www.aihero.dev/ai-coding-dictionary/agent)

<!-- zh-CN:end be861a821d9240e1 -->

Reach for it the moment you hit a question you can't settle by talking: a state machine whose edge cases you can't hold in your head, a screen you can't picture until you see three versions side by side. [Grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) sessions grow long on these questions. The agent rephrases, you guess, and the scope grows. Stop grilling, build the throwaway version, look at it, then answer in one line. If instead something already built is misbehaving and you want to know why, use [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs); prototyping explores what to build, not why the built thing is broken.

<!-- zh-CN:begin c439f72c3a926188 -->

当问题靠讨论无法解决时使用：状态机边界无法在脑中把握，或屏幕不看并排三种版本就无法想象。追问会遇到这类长问题：代理改写、你猜测、范围膨胀。停止追问，构建丢弃版本，看它，然后用一句话回答。若是已构建内容出错，用[diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs)；原型探索要构建什么，不诊断已构建物。 [链接](https://www.aihero.dev/ai-coding-dictionary/grilling)

<!-- zh-CN:end c439f72c3a926188 -->

You will also arrive here without choosing to. [wayfinder](https://aihero.dev/skills-wayfinder) files `prototype` decision [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) on its map, and you work one with this skill.

<!-- zh-CN:begin 77b66feb006765a7 -->

你也会间接进入这里：[wayfinder](https://aihero.dev/skills-wayfinder)在地图中创建`prototype`决策[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)，再用本技能处理。

<!-- zh-CN:end 77b66feb006765a7 -->

## Two branches

<!-- zh-CN:begin 947bac53ac979f83 -->

## 两个分支

<!-- zh-CN:end 947bac53ac979f83 -->

The question picks the branch, and the branches produce different artifacts:

<!-- zh-CN:begin 2889365f04af5019 -->

问题决定分支，产物不同：

<!-- zh-CN:end 2889365f04af5019 -->

- **"Does this logic / state model feel right?"**: a **single shareable HTML file**. One self-contained page, no build and no server, that someone opens by double-clicking. It carries a labelled state panel that re-renders after every click, free-play buttons for poking at the model in any order, and tabbed **guided walkthroughs** (one scenario per tab, each with the ordered buttons to press underneath it). Everything is labelled in domain language, so you can hand it to a designer, a PM or a domain expert and let them try the model themselves. The logic behind the page is a small pure module (a reducer, a machine, a set of functions) with no DOM code in it, so you can move the validated version straight into the real code.

<!-- zh-CN:begin ae8eaf89fbd31d89 -->

- **“逻辑/状态模型是否合理？”**：一个**可分享HTML文件**。自包含页面，无构建和服务器，双击打开。含每次点击后重渲染的带标签状态面板、任意顺序操作的自由控制按钮，以及标签式**引导演示**（每场景一标签，下方列出按序按钮）。全部使用领域语言，可交给设计师、PM或领域专家试用。页面逻辑是小型纯模块（reducer、状态机、函数集），DOM代码隔离，经验证可移入真实代码。

<!-- zh-CN:end ae8eaf89fbd31d89 -->
- **"What should this look like?"**: several **radically different** UI variations on one route, switchable from a floating bottom bar and a `?variant=` URL param. Variants must disagree about structure, not colour; three card grids with small tweaks answer nothing. They render inside a real page wherever possible, against real data and real density, because a variant judged on an empty page always looks fine.

<!-- zh-CN:begin 70cc735cc5a74878 -->

- **“应该长什么样？”**：同一路由上的多个**结构明显不同**的UI变体，由底部浮动栏和`?variant=`参数切换。变体必须结构不同，不能只改颜色；三张略有差异的卡片毫无回答价值。尽量嵌入真实页面、真实数据和密度；空页面上的变体总显得不错。

<!-- zh-CN:end 70cc735cc5a74878 -->

Both keep state in memory, start with no setup, and show you the full state after every step. The moment you find yourself hardening one (adding a test, wiring the real database, generalising for a case you might want later), you have stopped prototyping.

<!-- zh-CN:begin 60c00259096231ed -->

两者状态只在内存、无设置、每步后显示完整状态。开始加固原型（加测试、接真实数据库、为未来情况泛化）时就停止原型。

<!-- zh-CN:end 60c00259096231ed -->

## The prototype is a primary source

<!-- zh-CN:begin a9a6e02b6b0ae7e7 -->

## 原型是主要来源

<!-- zh-CN:end a9a6e02b6b0ae7e7 -->

A finished prototype leaves two things, and they go to different places.

<!-- zh-CN:begin ccc99110a7c6b37a -->

完成原型留下两样东西，进入不同位置。

<!-- zh-CN:end ccc99110a7c6b37a -->

You record the **answer** (the verdict plus the question it settled) somewhere permanent: a commit message, an ADR, the implementation issue. Main keeps the answer, in the real code.

<!-- zh-CN:begin 5523c95528105525 -->

把**答案**（结论及回答的问题）记录到长期位置：提交信息、ADR或实施issue。main保留答案和真实代码。

<!-- zh-CN:end 5523c95528105525 -->

The **prototype** is the runnable evidence the answer came from, and you do not delete it. It doesn't belong in main either, because nobody maintains it and it goes stale fast. So you commit it to a throwaway `prototype/<name>` branch out of main, never merge it, and leave a [context pointer](https://www.aihero.dev/ai-coding-dictionary/context-pointer) to that branch on the implementation issue. Main stays clean, and whoever picks the work up next can find and re-run the prototype.

<!-- zh-CN:begin 8d69bad95c95d4ca -->

**原型**是可运行证据，不要删除；也不放main，因为无人维护且会过时。把它提交到main外丢弃式`prototype/<name>`分支，永不合并，在实施issue放它的[上下文指针](https://www.aihero.dev/ai-coding-dictionary/context-pointer)。main保持干净，下一位接手者能找到并重跑。

<!-- zh-CN:end 8d69bad95c95d4ca -->

## Common questions

<!-- zh-CN:begin 8ffe538aa061dd84 -->

## 常见问题

<!-- zh-CN:end 8ffe538aa061dd84 -->

**Wait, isn't the prototype supposed to be deleted?**
Not any more. It used to be: build it, keep the answer, bin the code. The strongest objection to that was not about speed. It was *who picks up the work next [session](https://www.aihero.dev/ai-coding-dictionary/session), and what do they have to work from?* A prose summary of a prototype loses the thing that made it convincing. So the skill now treats the prototype as a [primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source). It lands on a `prototype/<name>` branch out of main and the implementation issue points at it. What changed is where the code lives, not the discipline; it still never merges into main.

<!-- zh-CN:begin 7f1cfd7e34bee0dd -->

**原型不是要删除吗？**
现在不再。过去是构建、保留答案、扔掉代码。最强反对不在速度，而在*下一会话谁接手、依据什么？*原型文字总结会丢失说服力。因此原型现在作为[主要来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)，落在`prototype/<name>`分支，由实施issue引用。变的是代码位置，纪律不变：永不合并main。 [链接](https://www.aihero.dev/ai-coding-dictionary/session)

<!-- zh-CN:end 7f1cfd7e34bee0dd -->

**It used to build a terminal app. Where did that go?**
The logic branch now emits a single shareable HTML file instead. A terminal app can only be driven by someone with the repo cloned and a runtime installed, which rules out the people whose opinion the prototype needs: the designer, the PM, the domain expert who knows what the state model is supposed to mean. One self-contained file that opens by double-click and still works after being emailed can be driven by anyone. The pure logic module underneath is unchanged, and is still the part you move into the real code.

<!-- zh-CN:begin 958ab02bf1f64809 -->

**以前构建终端应用，现在为什么不？**
逻辑分支现在输出自包含HTML。终端应用需要克隆仓库和运行时，排除了原型最需要听取意见的人：设计师、PM、领域专家。双击即可打开、邮件传输后仍工作的单文件供任何人驱动；底层纯逻辑模块不变，仍移入真实代码。

<!-- zh-CN:end 958ab02bf1f64809 -->

**An agent told me to `/prototype` when I should have been implementing.**
This is a known naming problem. An agent that does not know the flow reads `prototype`, a generic and appealing word, as "the obvious next step" once tickets exist. So agents recommend it by name even where the design was settled in conversation. If you already know what to build, the next step is `/implement`, per ticket. Reach for a prototype only when a specific design question is unresolved and talking won't resolve it.

<!-- zh-CN:begin afda6c278082445b -->

**代理在应实施时让我`/prototype`。**
这是命名问题。不了解流程的代理把通用诱人的`prototype`当“明显下一步”，即使设计已定。若已知要构建什么，下一步是按工单`/implement`。只有具体设计问题尚未解决且讨论无法解决时用原型。

<!-- zh-CN:end afda6c278082445b -->

**Should I prototype the whole application before building any of its production features (say, to demo it to prospects)?**
That is a different artifact that happens to share this skill's name. A prototype here is scoped to one question, and "what is the whole app?" isn't one. A full-app prototype has no natural stopping point, so it drifts into being the production app: the cleanup pass never happens, and code written under prototype rules (no tests, no error handling) ends up in front of users. If you need a sales demo, build it as a demo on purpose and be explicit that none of it is production. If you need to settle a design question, cut it down to that question.

<!-- zh-CN:begin a033cb1e7f11c8db -->

**构建生产功能前先原型整个应用，演示给潜在客户？**
那是同名但不同的产物。这里的原型只回答一个问题，“整个应用是什么”不构成一个问题；全应用原型无自然终点，会漂成生产应用，清理永不发生，原型规则下无测试和错误处理的代码最终面向用户。销售演示应有明确演示目的并声明非生产；设计问题应缩小到该问题。

<!-- zh-CN:end a033cb1e7f11c8db -->

**How do I run it in its own session?**
A prototype lives in its own directory and generates a lot of [context](https://www.aihero.dev/ai-coding-dictionary/context) you don't want in the thread that asked the question, so run it somewhere else and bring back only the answer. Use [handoff](https://aihero.dev/skills-handoff) to move the work into that session and to bring the answer back.

<!-- zh-CN:begin 1cb7e90747482dc9 -->

**如何在独立会话运行？**
原型在独立目录产生大量[上下文](https://www.aihero.dev/ai-coding-dictionary/context)，不应塞满提问线程。在别处运行，只带回答案。用[handoff](https://aihero.dev/skills-handoff)把工作移入并带回答案。

<!-- zh-CN:end 1cb7e90747482dc9 -->

**Isn't this the fastest possible way to burn tokens?**
It can be, if you prototype questions you could have answered by talking, or let one prototype sprawl across a whole feature. The comparison that matters isn't tokens against zero; it's [tokens](https://www.aihero.dev/ai-coding-dictionary/token) against building the wrong state model and finding out after it has production callers. Keep the question narrow and the run short, and the spend stays proportionate.

<!-- zh-CN:begin 37d89f1672e8c2c8 -->

**这不是最烧token的方法吗？**
若原型回答本可讨论的问题，或一个原型蔓延整个功能，可能如此。应比较[token](https://www.aihero.dev/ai-coding-dictionary/token)成本和构建错状态模型、到已有生产调用者才发现之间的代价。保持问题小、运行短，支出合理。

<!-- zh-CN:end 37d89f1672e8c2c8 -->

## It's working if

<!-- zh-CN:begin fa10a66596e1fc4c -->

## 正常表现

<!-- zh-CN:end fa10a66596e1fc4c -->

- You can say in one sentence what question the prototype exists to answer, and it's written at the top of the demo, not just in your head.

<!-- zh-CN:begin 3ba477b58d7c1c78 -->

- 能用一句话说出原型要回答的问题，并写在演示顶部而非只在脑中。

<!-- zh-CN:end 3ba477b58d7c1c78 -->
- Someone who doesn't read code can drive the logic demo. They open the file, press the buttons in a walkthrough tab, and describe what they see in their own words.

<!-- zh-CN:begin 90e2ba4422b4b472 -->

- 不看代码的人也能驱动逻辑演示：打开文件、按引导标签按钮、用自己的话描述看到的内容。

<!-- zh-CN:end 90e2ba4422b4b472 -->
- Someone says "wait, that shouldn't be possible" or "huh, I assumed X". That's a bug in the *idea*, which is what the prototype is for.

<!-- zh-CN:begin e3f806ced77d0e02 -->

- 有人说“等等，这不该发生”或“我原以为X”，说明*想法*有bug，这正是原型目的。

<!-- zh-CN:end e3f806ced77d0e02 -->
- The UI variants disagree about layout and information hierarchy, not just colour and copy, and the feedback you get is "the header from B with the sidebar from C".

<!-- zh-CN:begin e9fd0eb32576fca3 -->

- UI变体在布局和信息层级上不同，不只是颜色文案；反馈会像“B的页头配C的侧栏”。

<!-- zh-CN:end e9fd0eb32576fca3 -->
- It is answered in one sitting. If you're still building it a day later, the question was too big; split it.

<!-- zh-CN:begin c1684723799280c4 -->

- 一次坐席内完成；隔一天仍在建说明问题太大，应拆分。

<!-- zh-CN:end c1684723799280c4 -->
- When it's over, main contains the decision and none of the prototype, and the implementation issue points at the branch that still holds it.

<!-- zh-CN:begin c7a17e76cdd12f5f -->

- 完成后main只有决策，无原型；实施issue指向仍保存它的分支。

<!-- zh-CN:end c7a17e76cdd12f5f -->

## Where it fits

<!-- zh-CN:begin db03b53cbd389542 -->

## 所处位置

<!-- zh-CN:end db03b53cbd389542 -->

`prototype` is a **reach-for-it-anytime standalone**: you use it to settle one design question, then go back to your work. Another skill also runs it.

<!-- zh-CN:begin 2c15df9ca25f764c -->

`prototype`是**随时可用的独立工具**：解决一个设计问题后回到工作。其他技能也会运行它。

<!-- zh-CN:end 2c15df9ca25f764c -->

The skill that runs it most is [wayfinder](https://aihero.dev/skills-wayfinder). A wayfinder map is made of **decision tickets**, and `prototype` is one of the four types a ticket can be: the one used when the blocking question is "how should this look" or "how should it behave", which no amount of discussion resolves. When a discussion is vague, wayfinder makes something concrete to react to, and this skill builds that thing. The answer resolves a prototype ticket, and the map links to the prototype as an asset.

<!-- zh-CN:begin 6921c2f3472d02af -->

最常运行它的是[wayfinder](https://aihero.dev/skills-wayfinder)。其地图由**决策工单**组成，`prototype`是四类之一：阻塞问题是“应该长什么样”或“应该怎样运行”、讨论无法解决时使用。讨论含糊时，wayfinder创造具体物件供反应，本技能构建该物件；答案解决原型工单，地图链接原型资产。

<!-- zh-CN:end 6921c2f3472d02af -->

The other neighbours are upstream and downstream of that. [grill-me](https://aihero.dev/skills-grill-me) and [grill-with-docs](https://aihero.dev/skills-grill-with-docs) answer grillable questions; the ungrillable ones come here instead, and the one-line answer goes back into the interview. Downstream, a validated state model or UI direction becomes settled input for [to-spec](https://aihero.dev/skills-to-spec), which can inline the decision-rich snippet the prototype produced rather than describing it in prose. For anything else, [ask-matt](https://aihero.dev/skills-ask-matt) routes you over the whole set.

<!-- zh-CN:begin 62687cab09496c8d -->

相邻工具在上游和下游：[grill-me](https://aihero.dev/skills-grill-me)和[grill-with-docs](https://aihero.dev/skills-grill-with-docs)回答可追问问题；不可追问问题来这里，单行答案回到访谈。下游，已验证状态模型或UI方向成为[to-spec](https://aihero.dev/skills-to-spec)的输入，规格可内联富含决策的片段而无需文字描述。其他路由见[ask-matt](https://aihero.dev/skills-ask-matt)。

<!-- zh-CN:end 62687cab09496c8d -->
