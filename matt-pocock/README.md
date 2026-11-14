<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

<!-- zh-CN:begin e22a116762d8e2d6 -->

<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

<!-- 图片：Skills 项目横幅。 -->

<!-- zh-CN:end e22a116762d8e2d6 -->

# Skills For Real Engineers

<!-- zh-CN:begin 18a736180d20703e -->

# 面向真正工程师的技能

<!-- zh-CN:end 18a736180d20703e -->

[![skills.sh](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

<!-- zh-CN:begin 79ebdb116a7dbbdf -->

[![skills.sh 技能徽章](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

<!-- zh-CN:end 79ebdb116a7dbbdf -->

My agent skills that I use every day to do real engineering - not vibe coding.

<!-- zh-CN:begin d52469eb5660c96a -->

我每天用于真正工程工作的代理技能——用于实际工程，并非凭感觉写代码。

<!-- zh-CN:end d52469eb5660c96a -->

Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.

<!-- zh-CN:begin 81236b08608fa9c8 -->

开发真实应用很难。GSD、BMAD 和 Spec-Kit 等方法尝试通过接管流程来帮忙，但也因此剥夺你的控制权，让流程中的缺陷难以解决。

<!-- zh-CN:end 81236b08608fa9c8 -->

These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience. Hack around with them. Make them your own. Enjoy.

<!-- zh-CN:begin 93b29c022cf35efd -->

这些技能刻意保持小巧、易调整且可组合。它们适用于任何模型，基于数十年工程经验。可以自行修改、变成你的工具并享受使用。

<!-- zh-CN:end 93b29c022cf35efd -->

If you want to keep up with changes to these skills, and any new ones I create, you can join ~60,000 other devs on my newsletter:

<!-- zh-CN:begin d2db179f698e43da -->

若想跟进这些技能及我创建的新技能，可加入我的简报，与约 6 万名其他开发者一同了解更新：

<!-- zh-CN:end d2db179f698e43da -->

[Sign Up To The Newsletter](https://www.aihero.dev/s/skills-newsletter)

<!-- zh-CN:begin e185a04d9c233d4b -->

[订阅简报](https://www.aihero.dev/s/skills-newsletter)

<!-- zh-CN:end e185a04d9c233d4b -->

## Installation (30-second setup)

<!-- zh-CN:begin e0924c8745838986 -->

## 安装（30 秒设置）

<!-- zh-CN:end e0924c8745838986 -->

A plugin updates itself. [skills.sh](https://skills.sh/mattpocock/skills) copies editable files into your project, and you update them by hand. Pick one per agent, because installing both gives you every skill twice.

<!-- zh-CN:begin 60e19d15902b75b0 -->

插件会自行更新。[skills.sh](https://skills.sh/mattpocock/skills) 会把可编辑文件复制到项目，需要你手动更新。每个代理只选一种方式，两种都装会让所有技能重复。

<!-- zh-CN:end 60e19d15902b75b0 -->

### 1. Get the skills

<!-- zh-CN:begin 86e27e0a27273087 -->

### 1. 获取技能

<!-- zh-CN:end 86e27e0a27273087 -->

<details>
<summary><strong>Claude Code</strong><!-- zh-CN:begin 1a99afedde5caf38 --><br><strong>Claude Code</strong>（安装方法）<!-- zh-CN:end 1a99afedde5caf38 --></summary>

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```

Updates itself by default.

<!-- zh-CN:begin 2c1a897eadc84fa7 -->

默认会自动更新。

<!-- zh-CN:end 2c1a897eadc84fa7 -->

</details>

<!-- zh-CN:begin 867deecd1c32cd07 -->

</details> <!-- Claude Code 安装结束 -->

<!-- zh-CN:end 867deecd1c32cd07 -->

<details>
<summary><strong>Codex</strong><!-- zh-CN:begin 6676499df2c75cc3 --><br><strong>Codex</strong>（安装方法）<!-- zh-CN:end 6676499df2c75cc3 --></summary>

```bash
codex plugin marketplace add mattpocock/skills
codex plugin add mattpocock-skills@mattpocock
```

Updates itself at startup.

<!-- zh-CN:begin e5722fd8fc48cb6e -->

启动时自动更新。

<!-- zh-CN:end e5722fd8fc48cb6e -->

</details>

<!-- zh-CN:begin 89748a9d18903c45 -->

</details> <!-- Codex 安装结束 -->

<!-- zh-CN:end 89748a9d18903c45 -->

<details>
<summary><strong>GitHub Copilot</strong> (CLI and VS Code)<!-- zh-CN:begin 42d022d4f7e499ca --><br><strong>GitHub Copilot</strong>（CLI 和 VS Code 安装方法）<!-- zh-CN:end 42d022d4f7e499ca --></summary>

```bash
copilot plugin marketplace add mattpocock/skills
copilot plugin install mattpocock-skills@mattpocock
```

Then, once, add to `~/.copilot/settings.json`:

<!-- zh-CN:begin 1dc15b8df6c6c05a -->

然后一次性把以下配置加入 `~/.copilot/settings.json`：

<!-- zh-CN:end 1dc15b8df6c6c05a -->

```json
{
  "extraKnownMarketplaces": {
    "mattpocock": { "source": { "source": "github", "repo": "mattpocock/skills" }, "autoUpdate": true }
  }
}
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/mattpocock/skills`. It updates daily.

<!-- zh-CN:begin fe0f6fa1b72f9565 -->

在 VS Code 中运行 **Chat: Install Plugin From Source**（从源安装聊天插件），输入 `https://github.com/mattpocock/skills`。它每天更新。

<!-- zh-CN:end fe0f6fa1b72f9565 -->

</details>

<!-- zh-CN:begin fe87db5621535cf9 -->

</details> <!-- GitHub Copilot 安装结束 -->

<!-- zh-CN:end fe87db5621535cf9 -->

<details>
<summary><strong>Gemini CLI</strong> (manual updates)<!-- zh-CN:begin ef2c3178da0dbbb9 --><br><strong>Gemini CLI</strong>（手动更新安装方法）<!-- zh-CN:end ef2c3178da0dbbb9 --></summary>

```bash
gemini skills install https://github.com/mattpocock/skills.git --path skills/engineering
gemini skills install https://github.com/mattpocock/skills.git --path skills/productivity
```

Re-run both commands to update.

<!-- zh-CN:begin 4a7bcb92b8d5c356 -->

重新运行两条命令即可更新。

<!-- zh-CN:end 4a7bcb92b8d5c356 -->

</details>

<!-- zh-CN:begin c07c00525a33e592 -->

</details> <!-- Gemini CLI 安装结束 -->

<!-- zh-CN:end c07c00525a33e592 -->

<details>
<summary><strong>Any other agent, or editable files</strong> (manual updates)<!-- zh-CN:begin 37e60647f530c5d2 --><br><strong>其他代理或可编辑文件</strong>（手动更新安装方法）<!-- zh-CN:end 37e60647f530c5d2 --></summary>

```bash
npx skills@latest add mattpocock/skills -a <agent>  # cursor, opencode, devin, windsurf, amp, pi; omit -a to choose
```

<!-- zh-CN:begin 8e9c74d43daccf36 -->

```bash
npx skills@latest add mattpocock/skills -a <agent>  # cursor、opencode、devin、windsurf、amp、pi；省略 -a 可交互选择
```

<!-- zh-CN:end 8e9c74d43daccf36 -->

When the installer asks which skills to take, include `setup-matt-pocock-skills`. To update, run `npx skills@latest update`, and re-run `add` to pick up new skills.

<!-- zh-CN:begin cf9183e358368f7d -->

安装器询问采用哪些技能时，请包含 `setup-matt-pocock-skills`。更新时运行 `npx skills@latest update`，再运行 `add` 获取新技能。

<!-- zh-CN:end cf9183e358368f7d -->

</details>

<!-- zh-CN:begin 8e4f58e8ee57bb9a -->

</details> <!-- 其他安装方法结束 -->

<!-- zh-CN:end 8e4f58e8ee57bb9a -->

### 2. Run `/setup-matt-pocock-skills`

<!-- zh-CN:begin ef211a554584b25a -->

### 2. 运行 `/setup-matt-pocock-skills`

<!-- zh-CN:end ef211a554584b25a -->

In your agent, run it once per repo. It will:

<!-- zh-CN:begin eafc29fb11740db2 -->

在代理中为每个仓库运行一次。它会：

<!-- zh-CN:end eafc29fb11740db2 -->

- Ask you which issue tracker you want to use (GitHub, GitLab, local files, or anything else you describe)

<!-- zh-CN:begin 9658a22ce8690987 -->

- 询问使用哪种问题跟踪器（GitHub、GitLab、本地文件或你描述的其他工具）

<!-- zh-CN:end 9658a22ce8690987 -->
- Ask you what labels you apply to tickets when you triage them (`/triage` uses labels)

<!-- zh-CN:begin 59f740fd7de206c4 -->

- 询问分诊工单时使用的标签（`/triage` 会使用这些标签）

<!-- zh-CN:end 59f740fd7de206c4 -->
- Ask you where you want to save any docs we create

<!-- zh-CN:begin c0c24b20ae498f86 -->

- 询问新文档的保存位置

<!-- zh-CN:end c0c24b20ae498f86 -->

### 3. Bam - you're ready to go.

<!-- zh-CN:begin fbf8e72e00f9bb88 -->

### 3. 完成了——准备就绪。

<!-- zh-CN:end fbf8e72e00f9bb88 -->

## Why These Skills Exist

<!-- zh-CN:begin 9b4768a11d7ae19c -->

## 这些技能为何存在

<!-- zh-CN:end 9b4768a11d7ae19c -->

I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents.

<!-- zh-CN:begin 3e4bb2e1481a9d2a -->

我构建这些技能，是为了修复使用 Claude Code、Codex 及其他编码代理时常见的失败模式。

<!-- zh-CN:end 3e4bb2e1481a9d2a -->

### #1: The Agent Didn't Do What I Want

<!-- zh-CN:begin 16e46549678e34e8 -->

### #1：代理没有做我想要的事

<!-- zh-CN:end 16e46549678e34e8 -->

> "No-one knows exactly what they want"
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

<!-- zh-CN:begin 1e216025fc9baf87 -->

> “没有人完全知道自己想要什么。”
>
> David Thomas 与 Andrew Hunt，[《程序员修炼之道》](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

<!-- zh-CN:end 1e216025fc9baf87 -->

**The Problem**. The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.

<!-- zh-CN:begin 288d8b28ee4aa682 -->

**问题。**软件开发中最常见的失败是预期不一致。你以为开发者知道需求，看到他做出来的东西，却意识到对方完全没懂。

<!-- zh-CN:end 288d8b28ee4aa682 -->

This is just the same in the AI age. There is a communication gap between you and the agent. The fix for this is a **grilling session** - getting the agent to ask you detailed questions about what you're building.

<!-- zh-CN:begin 66c2ad93ce678fdc -->

AI 时代仍然如此。你和代理之间存在沟通鸿沟。解决办法是**追问流程**，让代理详细询问你要构建什么。

<!-- zh-CN:end 66c2ad93ce678fdc -->

**The Fix** is to use:

<!-- zh-CN:begin 96d7965aaac7b8bf -->

**修复方法：**使用：

<!-- zh-CN:end 96d7965aaac7b8bf -->

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) - for non-code uses

<!-- zh-CN:begin 0becc3fcbe6145e3 -->

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md)——用于非代码任务

<!-- zh-CN:end 0becc3fcbe6145e3 -->
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) - same as [`/grill-me`](./skills/productivity/grill-me/SKILL.md), but adds more goodies (see below)

<!-- zh-CN:begin baa268ed0e8310c3 -->

- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md)——与 [`/grill-me`](./skills/productivity/grill-me/SKILL.md) 相同，并增加下文的额外能力

<!-- zh-CN:end baa268ed0e8310c3 -->

These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them _every_ time you want to make a change.

<!-- zh-CN:begin 34005145f68738e6 -->

这是我最受欢迎的技能。它们帮助你在开工前与代理对齐并深入思考改动。_每次_准备改动时都使用。

<!-- zh-CN:end 34005145f68738e6 -->

### #2: The Agent Is Way Too Verbose

<!-- zh-CN:begin 74c0f66c41f54c1d -->

### #2：代理过于冗长

<!-- zh-CN:end 74c0f66c41f54c1d -->

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

<!-- zh-CN:begin 2c3a5bd89fb68243 -->

> 有了通用语言，开发者之间的对话和代码表达都来自同一个领域模型。
>
> Eric Evans，[《领域驱动设计》](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

<!-- zh-CN:end 2c3a5bd89fb68243 -->

**The Problem**: At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.

<!-- zh-CN:begin 63199b6255e3b2d7 -->

**问题：**项目初期，开发者和交付软件的使用者（领域专家）通常使用不同语言。

<!-- zh-CN:end 63199b6255e3b2d7 -->

I felt the same tension with my agents. Agents are usually dropped into a project and asked to figure out the jargon as they go. So they use 20 words where 1 will do.

<!-- zh-CN:begin 955a7a76638fb3d8 -->

我与代理也有同样张力。代理通常被丢进项目，边做边猜术语，本来一个词就够，却用二十个。

<!-- zh-CN:end 955a7a76638fb3d8 -->

**The Fix** for this is a shared language. It's a document that helps agents decode the jargon used in the project.

<!-- zh-CN:begin 81f91b2bfe2cd8b9 -->

**修复方法：**建立共享语言，也就是一份帮助代理解读项目术语的文档。

<!-- zh-CN:end 81f91b2bfe2cd8b9 -->

<details>
<summary>
Example
<!-- zh-CN:begin ada705af3bf4fd85 --><br>
示例
<!-- zh-CN:end ada705af3bf4fd85 --></summary>

Here's an example [glossary](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) (still named `CONTEXT.md` at that pinned commit, from before the skills renamed the convention), from my `course-video-manager` repo. Which one is easier to read?

<!-- zh-CN:begin a21d355107a3c02b -->

以下是我 `course-video-manager` 仓库的[术语表](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md)示例（固定提交时仍叫 `CONTEXT.md`，早于技能改名约定）。哪个更容易读？

<!-- zh-CN:end a21d355107a3c02b -->

- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"

<!-- zh-CN:begin 8232b2e8ec52e9c9 -->

- **之前**：“若把课程章节中的一课设为‘真实’（即在文件系统分配位置），会出现问题”

<!-- zh-CN:end 8232b2e8ec52e9c9 -->
- **AFTER**: "There's a problem with the materialization cascade"

<!-- zh-CN:begin a2d56bf5c57f14bb -->

- **之后**：“具体化级联出了问题”

<!-- zh-CN:end a2d56bf5c57f14bb -->

This concision pays off session after session.

<!-- zh-CN:begin 59975a430bed75f4 -->

这种简洁在每次会话中都有回报。

<!-- zh-CN:end 59975a430bed75f4 -->

</details>

<!-- zh-CN:begin 7bec42c5913803cd -->

</details> <!-- 术语表示例结束 -->

<!-- zh-CN:end 7bec42c5913803cd -->

This is built into [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md). It's a grilling session, but that helps you build a shared language with the AI, and document hard-to-explain decisions in ADR's.

<!-- zh-CN:begin 0ee253c6f8697caf -->

这内置在 [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) 中。它执行追问，同时帮助与 AI 建立共享语言，并把难以解释的决策记录在 ADR 中。

<!-- zh-CN:end 0ee253c6f8697caf -->

It's hard to explain how powerful this is. It might be the single coolest technique in this repo. Try it, and see.

<!-- zh-CN:begin c6e5b7224db244b7 -->

它的威力很难讲清，可能是本仓库最酷的技术。试一次便知。

<!-- zh-CN:end c6e5b7224db244b7 -->

> [!TIP]
> A shared language has many other benefits than reducing verbosity:
>
> - **Variables, functions and files are named consistently**, using the shared language
> - As a result, the **codebase is easier to navigate** for the agent
> - The agent also **spends fewer tokens on thinking**, because it has access to a more concise language

<!-- zh-CN:begin 09f213fb8577f9f9 -->

> [!TIP]
> 共享语言除减少冗长外还有许多好处：
>
> - **变量、函数和文件命名一致**，都使用共享语言
> - 因此代理**更容易导航代码库**
> - 代理也能**减少思考 token**，因为它拥有更简练的语言

<!-- zh-CN:end 09f213fb8577f9f9 -->

### #3: The Code Doesn't Work

<!-- zh-CN:begin c201aeeadb399e04 -->

### #3：代码无法工作

<!-- zh-CN:end c201aeeadb399e04 -->

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

<!-- zh-CN:begin e92be6374b8f5ce4 -->

> “始终采取小而审慎的步骤。反馈速度就是速度上限。永远不要承担过大的任务。”
>
> David Thomas 与 Andrew Hunt，[《程序员修炼之道》](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

<!-- zh-CN:end e92be6374b8f5ce4 -->

**The Problem**: Let's say that you and the agent are aligned on what to build. What happens when the agent _still_ produces crap?

<!-- zh-CN:begin d962be5c8a3b113a -->

**问题：**假设你和代理对构建内容已经一致。若代理_仍然_产出垃圾怎么办？

<!-- zh-CN:end d962be5c8a3b113a -->

It's time to look at your feedback loops. Without feedback on how the code it produces actually runs, the agent will be flying blind.

<!-- zh-CN:begin 80147eead55637ae -->

该检查反馈循环了。如果得不到代码实际运行情况的反馈，代理就是在盲飞。

<!-- zh-CN:end 80147eead55637ae -->

**The Fix**: You need the usual tranche of feedback loops: static types, browser access, and automated tests.

<!-- zh-CN:begin 4f7b9a31601ebc85 -->

**修复方法：**需要常见反馈循环：静态类型、浏览器访问和自动测试。

<!-- zh-CN:end 4f7b9a31601ebc85 -->

For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code.

<!-- zh-CN:begin a8b5ceb4618c6f55 -->

自动测试必须采用红—绿—重构循环：代理先写失败测试，再修复。这给代理一致的反馈，产出好得多的代码。

<!-- zh-CN:end a8b5ceb4618c6f55 -->

I've built a **[`/tdd`](./skills/engineering/tdd/SKILL.md) skill** you can slot into any project. It encourages red-green-refactor and gives the agent plenty of guidance on what makes good and bad tests.

<!-- zh-CN:begin bad7e427a49d7720 -->

我构建了可接入任何项目的 **[`/tdd`](./skills/engineering/tdd/SKILL.md) 技能**，鼓励红—绿—重构，并指导代理识别好测试与坏测试。

<!-- zh-CN:end bad7e427a49d7720 -->

For debugging, I've also built a **[`/diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md)** skill that wraps best debugging practices into a disciplined loop, gated phase by phase.

<!-- zh-CN:begin bb05e8f97e913d87 -->

调试方面，我还构建了 **[`/diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md)**，把最佳调试实践组织为按阶段把关的有纪律循环。

<!-- zh-CN:end bb05e8f97e913d87 -->

### #4: We Built A Ball Of Mud

<!-- zh-CN:begin c28f79309cddcadd -->

### #4：我们造出了一团泥

<!-- zh-CN:end c28f79309cddcadd -->

> "Invest in the design of the system _every day_."
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

<!-- zh-CN:begin 3fb7befef3005ff8 -->

> “_每天_都投资于系统设计。”
>
> Kent Beck，[《解析极限编程》](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

<!-- zh-CN:end 3fb7befef3005ff8 -->

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

<!-- zh-CN:begin 940b0ec803c969c8 -->

> “最好的模块是深模块。它们让大量功能通过简单接口访问。”
>
> John Ousterhout，[《软件设计哲学》](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

<!-- zh-CN:end 940b0ec803c969c8 -->

**The Problem**: Most apps built with agents are complex and hard to change. Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate.

<!-- zh-CN:begin af68d2e73c4732da -->

**问题：**用代理构建的大多数应用复杂且难以修改。代理大幅加速编码，也加速软件熵，代码库以前所未有的速度变复杂。

<!-- zh-CN:end af68d2e73c4732da -->

**The Fix** for this is a radical new approach to AI-powered development: caring about the design of the code.

<!-- zh-CN:begin 3ba66c3ff3761403 -->

**修复方法：**采用面向 AI 开发的激进新方法——关心代码设计。

<!-- zh-CN:end 3ba66c3ff3761403 -->

This is built in to every layer of these skills:

<!-- zh-CN:begin 1a1a6670f9917a05 -->

这内置在每层技能中：

<!-- zh-CN:end 1a1a6670f9917a05 -->

- [`/to-spec`](./skills/engineering/to-spec/SKILL.md) quizzes you about which modules you're touching before creating a spec

<!-- zh-CN:begin d281ef7380a53f8b -->

- [`/to-spec`](./skills/engineering/to-spec/SKILL.md) 在创建规格前询问你要改动哪些模块

<!-- zh-CN:end d281ef7380a53f8b -->

And crucially, [`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) surveys a codebase for deepening opportunities and hands you the candidates. I recommend running it on your codebase once every few days. It is a survey, not a rescue: on a genuinely old codebase it will find real candidates, but it won't untangle the mud for you.

<!-- zh-CN:begin 0749a7d9e45a96af -->

关键工具是 [`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md)：扫描代码库的加深机会并给出候选。建议每隔几天运行一次。它是勘察，不是救援：真正古老的代码库会暴露真实候选，但它不会替你理清泥团。

<!-- zh-CN:end 0749a7d9e45a96af -->

### Summary

<!-- zh-CN:begin 7b557fbaee679cc1 -->

### 总结

<!-- zh-CN:end 7b557fbaee679cc1 -->

Software engineering fundamentals matter more than ever. These skills are my best effort at condensing these fundamentals into repeatable practices, to help you ship the best apps of your career. Enjoy.

<!-- zh-CN:begin e6256a6b1f30f238 -->

软件工程基础比以往更重要。这些技能是我把基础凝练为可重复实践的最大努力，帮助你交付职业生涯中最好的应用。祝你使用愉快。

<!-- zh-CN:end e6256a6b1f30f238 -->

## Reference

<!-- zh-CN:begin 1f7948c00958253c -->

## 参考

<!-- zh-CN:end 1f7948c00958253c -->

These split on one axis: who can invoke them. **User-invoked** skills are reachable only when you type them (e.g. `/grill-me`); their job is to orchestrate. **Model-invoked** skills can be invoked by you _or_ reached for automatically by the agent when the task fits; they hold the reusable discipline. A user-invoked skill may invoke model-invoked skills, but never another user-invoked one.

<!-- zh-CN:begin ceaea2d50179b944 -->

技能按调用者分两类。**用户调用**技能只能由你输入命令触发（如 `/grill-me`），其职责是编排。**模型调用**技能可由你调用，也可由代理在任务适合时自动选取，包含可复用的纪律。用户调用技能可调用模型调用技能，但绝不能调用另一个用户调用技能。

<!-- zh-CN:end ceaea2d50179b944 -->

### Engineering

<!-- zh-CN:begin d48815770652d5a2 -->

### 工程

<!-- zh-CN:end d48815770652d5a2 -->

Skills I use daily for code work.

<!-- zh-CN:begin 40c92ec2c24fa9f4 -->

我每天用于代码工作的技能。

<!-- zh-CN:end 40c92ec2c24fa9f4 -->

**User-invoked**

<!-- zh-CN:begin 6bb725089fa68639 -->

**用户调用**

<!-- zh-CN:end 6bb725089fa68639 -->

- **[ask-matt](./skills/engineering/ask-matt/SKILL.md)**: Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.

<!-- zh-CN:begin bb0fd502ff222e18 -->

- **[ask-matt](./skills/engineering/ask-matt/SKILL.md)**：询问哪种技能或流程适合当前情况，是本仓库用户调用技能的路由器。

<!-- zh-CN:end bb0fd502ff222e18 -->
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)**: Grilling session that also builds your project's domain model, sharpening terminology and updating `GLOSSARY.md` and ADRs inline.

<!-- zh-CN:begin a0fed1b96818e545 -->

- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)**：追问流程，同时建立项目领域模型，精炼术语并就地更新 `GLOSSARY.md` 和 ADR。

<!-- zh-CN:end a0fed1b96818e545 -->
- **[triage](./skills/engineering/triage/SKILL.md)**: Move issues through a state machine of triage roles.

<!-- zh-CN:begin ccd3c4998c714884 -->

- **[triage](./skills/engineering/triage/SKILL.md)**：让问题经过分诊角色组成的状态机。

<!-- zh-CN:end ccd3c4998c714884 -->
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.

<!-- zh-CN:begin a955d066aaef6563 -->

- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)**：扫描代码库的加深机会，以可视化 HTML 报告呈现，再追问你选中的一项。

<!-- zh-CN:end a955d066aaef6563 -->
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)**: Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo before using the other engineering skills.

<!-- zh-CN:begin 67dceeb70e0717a9 -->

- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)**：配置仓库以使用工程技能（问题跟踪器、分诊标签、领域文档布局）。使用其他工程技能前，每个仓库运行一次。

<!-- zh-CN:end 67dceeb70e0717a9 -->
- **[to-spec](./skills/engineering/to-spec/SKILL.md)**: Turn the current conversation into a spec and publish it to the issue tracker. No interview, just synthesizes what you've already discussed.

<!-- zh-CN:begin 4b4eff9a01746516 -->

- **[to-spec](./skills/engineering/to-spec/SKILL.md)**：把当前对话转为规格并发布到问题跟踪器。无需访谈，只汇总已讨论内容。

<!-- zh-CN:end 4b4eff9a01746516 -->
- **[to-tickets](./skills/engineering/to-tickets/SKILL.md)**: Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges, written as text in a local file, or as native blocking links on a real tracker.

<!-- zh-CN:begin dc55fccdb5376ac3 -->

- **[to-tickets](./skills/engineering/to-tickets/SKILL.md)**：把计划、规格或对话拆成曳光弹工单，每个声明阻塞关系；可写入本地文本或真实跟踪器原生阻塞链接。

<!-- zh-CN:end dc55fccdb5376ac3 -->
- **[implement](./skills/engineering/implement/SKILL.md)**: Build the work described by a spec or set of tickets, driving `/tdd` at pre-agreed seams and closing out with `/code-review` before committing.

<!-- zh-CN:begin fde6a02013e80f88 -->

- **[implement](./skills/engineering/implement/SKILL.md)**：实现规格或工单描述的工作，在预先约定接缝驱动 `/tdd`，提交前用 `/code-review` 收尾。

<!-- zh-CN:end fde6a02013e80f88 -->
- **[implement-spec](./skills/engineering/implement-spec/SKILL.md)**: Implement a whole spec on one integration branch. Works the tickets as a task graph, running implementer subagents across the ready frontier for maximum concurrency, then closes out with `/code-review`.

<!-- zh-CN:begin 04abd0ab7c189e7b -->

- **[implement-spec](./skills/engineering/implement-spec/SKILL.md)**：在一个集成分支实现整份规格。把工单当作任务图，跨就绪前沿运行实现子代理以最大化并发，最后用 `/code-review` 收尾。

<!-- zh-CN:end 04abd0ab7c189e7b -->
- **[wayfinder](./skills/engineering/wayfinder/SKILL.md)**: Plan a huge chunk of work, more than one agent session can hold, as a shared map of decision tickets on the issue tracker, and resolve them one at a time until the way to the destination is clear.

<!-- zh-CN:begin 6b85034f1fc8a489 -->

- **[wayfinder](./skills/engineering/wayfinder/SKILL.md)**：把超过一个代理会话容量的巨大工作规划成问题跟踪器上的决策工单共享地图，逐个解决直到路线清晰。

<!-- zh-CN:end 6b85034f1fc8a489 -->
- **[retro](./skills/engineering/retro/SKILL.md)**: Suggest improvements to the coding agent's environment (navigation, automated checks, coding standards, steering files, tooling) after a session, most severe first.

<!-- zh-CN:begin e449978fc3a186ed -->

- **[retro](./skills/engineering/retro/SKILL.md)**：会话后按严重程度建议改进编码代理环境（导航、自动检查、编码规范、引导文件、工具）。

<!-- zh-CN:end e449978fc3a186ed -->

**Model-invoked**

<!-- zh-CN:begin bb2a60c5cce36ced -->

**模型调用**

<!-- zh-CN:end bb2a60c5cce36ced -->

- **[prototype](./skills/engineering/prototype/SKILL.md)**: Build a throwaway prototype to answer a design question, either a single shareable HTML file for state/logic questions, or several radically different UI variations toggleable from one route.

<!-- zh-CN:begin c63ff0255a560821 -->

- **[prototype](./skills/engineering/prototype/SKILL.md)**：构建一次性原型回答设计问题；状态/逻辑问题可做成一个可分享 HTML 文件，UI 问题可做多个差异明显、可通过一个路由切换的变体。

<!-- zh-CN:end c63ff0255a560821 -->
- **[diagnosing-bugs](./skills/engineering/diagnosing-bugs/SKILL.md)**: Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.

<!-- zh-CN:begin 198c1059436ffb00 -->

- **[diagnosing-bugs](./skills/engineering/diagnosing-bugs/SKILL.md)**：针对难 bug 和性能回归的受控诊断循环：建立让 bug 变红的反馈 → 最小化 → 假设 → 插桩 → 修复 → 回归测试。

<!-- zh-CN:end 198c1059436ffb00 -->
- **[research](./skills/engineering/research/SKILL.md)**: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent.

<!-- zh-CN:begin 896ddaa602fd0368 -->

- **[research](./skills/engineering/research/SKILL.md)**：以高可信一手来源调查问题，将发现作为带引用的 Markdown 文件写入仓库，并作为后台代理运行。

<!-- zh-CN:end 896ddaa602fd0368 -->
- **[tdd](./skills/engineering/tdd/SKILL.md)**: Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.

<!-- zh-CN:begin 75ae7b993c2a345e -->

- **[tdd](./skills/engineering/tdd/SKILL.md)**：红—绿—重构循环的测试驱动开发，一次一个纵向切片构建功能或修复 bug。

<!-- zh-CN:end 75ae7b993c2a345e -->
- **[domain-modeling](./skills/engineering/domain-modeling/SKILL.md)**: Actively build and sharpen a project's domain model: challenge terms against the glossary, stress-test with edge-case scenarios, and update `GLOSSARY.md` and ADRs inline.

<!-- zh-CN:begin 0604b60ad02fca80 -->

- **[domain-modeling](./skills/engineering/domain-modeling/SKILL.md)**：主动建立并精炼项目领域模型：对照术语表质疑用词，用边界场景压力测试，就地更新 `GLOSSARY.md` 和 ADR。

<!-- zh-CN:end 0604b60ad02fca80 -->
- **[codebase-design](./skills/engineering/codebase-design/SKILL.md)**: Shared discipline and vocabulary for designing deep modules: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface.

<!-- zh-CN:begin a49e314f48f28d37 -->

- **[codebase-design](./skills/engineering/codebase-design/SKILL.md)**：设计深模块的共享纪律和词汇：小接口承载大量行为，放在清晰接缝处，并可通过该接口测试。

<!-- zh-CN:end a49e314f48f28d37 -->
- **[code-review](./skills/engineering/code-review/SKILL.md)**: Two-axis review of the diff since a fixed point: **Standards** (does it follow the repo's coding standards, plus a Fowler smell baseline?) and **Spec** (does it faithfully implement the originating issue/spec?), run as parallel sub-agents so neither pollutes the other.

<!-- zh-CN:begin 81e57157c064dde4 -->

- **[code-review](./skills/engineering/code-review/SKILL.md)**：对固定点以来的 diff 做双轴审查：**标准**（是否遵循仓库编码规范及 Fowler 气味基线）与**规格**（是否忠实实现来源 issue/规格），由并行子代理执行以免互相污染。

<!-- zh-CN:end 81e57157c064dde4 -->
- **[pr](./skills/engineering/pr/SKILL.md)**: The shape a pull request body should take: a summary as the smallest visual that makes the change clear, before/after evidence that it works, and a merge-danger call (one-way or two-way door, plus blast radius).

<!-- zh-CN:begin 479a5d79988022a3 -->

- **[pr](./skills/engineering/pr/SKILL.md)**：PR 正文的结构：最能说明改动的最小视觉摘要、证明有效的修改前后证据，以及合并风险判断（单向/双向门与影响范围）。

<!-- zh-CN:end 479a5d79988022a3 -->
- **[wizard](./skills/engineering/wizard/SKILL.md)**: Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.

<!-- zh-CN:begin e01f0f3e0872bc14 -->

- **[wizard](./skills/engineering/wizard/SKILL.md)**：生成交互式 bash 向导，带领用户完成只有他们能做的步骤：基础设施开通、凭据或 CI 密钥设置、操作陌生第三方仪表盘、或一次性迁移/切换。

<!-- zh-CN:end e01f0f3e0872bc14 -->

### Productivity

<!-- zh-CN:begin d8618c9312288969 -->

### 生产力

<!-- zh-CN:end d8618c9312288969 -->

General workflow tools, not code-specific.

<!-- zh-CN:begin 551e597b7cef533f -->

通用工作流工具，不限定代码。

<!-- zh-CN:end 551e597b7cef533f -->

**User-invoked**

<!-- zh-CN:begin ec907dfe6b398c4f -->

**用户调用**

<!-- zh-CN:end ec907dfe6b398c4f -->

- **[grill-me](./skills/productivity/grill-me/SKILL.md)**: Get relentlessly interviewed about a plan or design until every branch of the design tree is resolved.

<!-- zh-CN:begin cdeaf6f57cbab7d2 -->

- **[grill-me](./skills/productivity/grill-me/SKILL.md)**：围绕计划或设计连续追问，直到设计树每个分支都解决。

<!-- zh-CN:end cdeaf6f57cbab7d2 -->
- **[handoff](./skills/productivity/handoff/SKILL.md)**: Compact the current conversation into a handoff document so another agent can continue the work.

<!-- zh-CN:begin 915058b7ce7e40bc -->

- **[handoff](./skills/productivity/handoff/SKILL.md)**：把当前对话压缩成交接文档，让另一个代理继续。

<!-- zh-CN:end 915058b7ce7e40bc -->
- **[teach](./skills/productivity/teach/SKILL.md)**: Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.

<!-- zh-CN:begin fe39ecf927a6a53e -->

- **[teach](./skills/productivity/teach/SKILL.md)**：跨多次会话教授新技能或概念，以当前目录作为有状态教学工作区。

<!-- zh-CN:end fe39ecf927a6a53e -->
- **[to-questionnaire](./skills/productivity/to-questionnaire/SKILL.md)**: Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can, filled in async, or together over a meeting. It grills you about the send (who it's for, what you need back), not the subject.

<!-- zh-CN:begin dfb9fb0eb9739301 -->

- **[to-questionnaire](./skills/productivity/to-questionnaire/SKILL.md)**：把无法独自回答的决策变成 Markdown 问卷交给唯一能回答的人，异步填写或会议中完成。它追问发送方式，不追问主题。

<!-- zh-CN:end dfb9fb0eb9739301 -->
- **[wait-what](./skills/productivity/wait-what/SKILL.md)**: Fire this the moment a message doesn't land. The agent re-pitches it with the context you're missing, in plain English, using your `GLOSSARY.md` vocabulary.

<!-- zh-CN:begin 3790dc020d35c084 -->

- **[wait-what](./skills/productivity/wait-what/SKILL.md)**：消息没传达清楚时立即调用；代理用你的 `GLOSSARY.md` 词汇和缺失上下文以通俗语言重新解释。

<!-- zh-CN:end 3790dc020d35c084 -->

**Model-invoked**

<!-- zh-CN:begin bbd7714cbc5c4ffe -->

**模型调用**

<!-- zh-CN:end bbd7714cbc5c4ffe -->

- **[grilling](./skills/productivity/grilling/SKILL.md)**: Interview the user relentlessly about a plan, decision, or idea until every branch of the design tree is resolved. The reusable interview primitive behind `grill-me`, `grill-with-docs`, `triage`, `wayfinder` and `improve-codebase-architecture`.

<!-- zh-CN:begin 0f56384345b30651 -->

- **[grilling](./skills/productivity/grilling/SKILL.md)**：围绕计划、决策或想法连续访谈，直到设计树每个分支解决；它是 `grill-me`、`grill-with-docs`、`triage`、`wayfinder` 和 `improve-codebase-architecture` 背后的可复用访谈原语。

<!-- zh-CN:end 0f56384345b30651 -->
- **[writing-for-agents](./skills/productivity/writing-for-agents/SKILL.md)**: Writing documents for agents: skills, AGENTS.md/CLAUDE.md, and any doc an agent reaches by a pointer.

<!-- zh-CN:begin e01546506486d736 -->

- **[writing-for-agents](./skills/productivity/writing-for-agents/SKILL.md)**：为代理编写文档：技能、AGENTS.md/CLAUDE.md，以及代理通过指针访问的文档。

<!-- zh-CN:end e01546506486d736 -->
