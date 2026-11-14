## What it does

<!-- zh-CN:begin 429e596ef941a315 -->

## 它的作用

<!-- zh-CN:end 429e596ef941a315 -->

`pr` defines the shape of a pull request body: a **Summary** that shows the change, **Evidence** that it works, and a **Merge Danger** call on how risky it is to land. It is a format reference, not a workflow. It does not push a branch, open the PR, or decide what goes into it. It tells the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) what the body should look like when it writes one.

<!-- zh-CN:begin 652949ba4c7fa6f5 -->

`pr` 定义拉取请求正文的形态：展示变更的**摘要**、证明可用的**证据**，以及对合并风险的 **Merge Danger** 判断。它是格式参考，不是工作流，不推送分支、不打开 PR，也不决定内容。它告诉[代理](https://www.aihero.dev/ai-coding-dictionary/agent)编写正文时应该是什么样子。

<!-- zh-CN:end 652949ba4c7fa6f5 -->

The summary is a visual, not a paragraph. A default PR body describes the diff in prose. This one picks the **smallest view** that makes the key point clear (pseudocode, a call tree, a component tree, a file tree, a Mermaid diagram, or a shaped diff) and keeps the words around it brief. The reviewer already has the diff open, so the body shows them its shape before they read it.

<!-- zh-CN:begin 9ae3e72fcef6403d -->

摘要采用可视化而非段落。默认 PR 正文用文字描述差异；这里选出能说清要点的**最小视图**（伪代码、调用树、组件树、文件树、Mermaid 图或有形差异），周围文字保持简短。审阅者已打开差异，正文让他们读前先看到形状。

<!-- zh-CN:end 9ae3e72fcef6403d -->

## When to reach for it

<!-- zh-CN:begin 29c83cebb752e84a -->

## 何时使用

<!-- zh-CN:end 29c83cebb752e84a -->

Type `/pr`, or the agent reaches for it automatically whenever it is writing a PR body.

<!-- zh-CN:begin 8f87eb0c4ff0ac82 -->

输入 `/pr`，或代理在编写 PR 正文时自动使用。

<!-- zh-CN:end 8f87eb0c4ff0ac82 -->

| Your situation | Reach for |
| --- | --- |
| A branch is ready and needs a body a reviewer can scan | `pr` |
| The code is written but nobody has reviewed it yet | [code-review](https://aihero.dev/skills-code-review) first, then `pr` |
| The PR is open and review comments are coming back | Nothing in this set yet; `pr` only writes the body |

<!-- zh-CN:begin 7774c8a56448b32c -->

| 你的情形 | 使用 |
| --- | --- |
| 分支已就绪，需要审阅者能快速浏览的正文 | `pr` |
| 代码已写，但尚无人审阅 | 先 [code-review](https://aihero.dev/skills-code-review)，再 `pr` |
| PR 已打开，审查评论正在返回 | 此集合暂不覆盖；`pr` 只写正文 |

<!-- zh-CN:end 7774c8a56448b32c -->

## The template

<!-- zh-CN:begin df1c655095156262 -->

## 模板

<!-- zh-CN:end df1c655095156262 -->

Three sections, in this order:

<!-- zh-CN:begin e4e9e71be82b2c1b -->

三个章节，按此顺序：

<!-- zh-CN:end e4e9e71be82b2c1b -->

- **Summary**: one or more small visuals, each placed next to the short text it supports. Use one, sometimes several, rarely all of them. Keep only the calls, files, props, and boundaries the reviewer needs.

<!-- zh-CN:begin 3b3e7076040eceb0 -->

- **摘要**：一个或多个小视图，各紧邻其支持的短文本。通常一个，有时几个，很少全用。只保留审阅者需要的调用、文件、属性与边界。

<!-- zh-CN:end 3b3e7076040eceb0 -->
- **Evidence**: a before and after. A screenshot is the strongest evidence when the change is visual and the [environment](https://www.aihero.dev/ai-coding-dictionary/environment) can take one. Otherwise, use the exact test that failed and now passes, written as pseudocode, or the console output that changed.

<!-- zh-CN:begin 9c9429a71514fe78 -->

- **证据**：前后对照。变更涉及视觉且[环境](https://www.aihero.dev/ai-coding-dictionary/environment)能截图时，截图是最强证据。否则使用先前失败、现在通过的确切测试（写成伪代码），或发生变化的控制台输出。

<!-- zh-CN:end 9c9429a71514fe78 -->
- **Merge Danger**: whether the change is a **one-way door** or a **two-way door**, and its **blast radius**. A two-way door is cheap to reverse; a one-way door (a destructive migration, a public API removal, a hard-to-reverse decision) is not. Blast radius names what could break if the change is wrong: layout shift, consumers of an API, mobile responsiveness.

<!-- zh-CN:begin 9b8f4d2192fa09b0 -->

- **Merge Danger**：变更是**单向门**还是**双向门**，以及**影响半径**。双向门容易逆转；单向门（破坏性迁移、移除公共 API、难以逆转的决定）则不是。影响半径说明出错时可能破坏什么：布局偏移、API 消费者、移动端响应式。

<!-- zh-CN:end 9b8f4d2192fa09b0 -->

The door call is the leading idea. It changes "is this safe to merge?" from a gut feeling into a stated claim the reviewer can disagree with. It also tells them where to spend their [human review](https://www.aihero.dev/ai-coding-dictionary/human-review). Skim a two-way door with a small blast radius, and read a one-way door slowly.

<!-- zh-CN:begin 95fb9d4275c97962 -->

门的判断是首要观点。它把“能安全合并吗”从直觉变为审阅者可以反驳的明确主张，也告诉他们应在哪里投入[人工审查](https://www.aihero.dev/ai-coding-dictionary/human-review)。小影响半径的双向门可略读，单向门应缓慢细读。

<!-- zh-CN:end 95fb9d4275c97962 -->

## Common questions

<!-- zh-CN:begin f4dd8d8a6a4b7132 -->

## 常见问题

<!-- zh-CN:end f4dd8d8a6a4b7132 -->

**Can I trust the agent's own door call?**

<!-- zh-CN:begin 7bcd0ce16b39cd68 -->

**能信任代理自己的门的判断吗？**

<!-- zh-CN:end 7bcd0ce16b39cd68 -->

Not blindly, and that is the point of stating it. The agent that wrote the change is the one grading it, so be most suspicious when it says "two-way, small blast radius". The diff also often hides whether a change can be reversed. As one user put it, "rolling back a commit won't unsend a batch of emails", and a flagged rollout stays two-way only until the first write lands in the new format. The skill gives the agent a definition (destructive actions and hard-to-reverse decisions are one-way), not a checklist, so check the Merge Danger line most carefully. Two things help: make sure the agent has the [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) or [spec](https://www.aihero.dev/ai-coding-dictionary/spec) in front of it, not just the diff, and write down the changes your repo always treats as one-way (schema migrations, anything that ships outward or deletes) where the agent will read them before it makes the call.

<!-- zh-CN:begin db102be27376065e -->

不能盲信，这正是写明的作用。编写变更的代理在给自己评分，因此它说“双向、影响小”时最应怀疑。差异也常掩盖变更能否逆转。正如用户所说，“回滚提交无法撤回一批邮件”，已标记的上线在第一次以新格式写入后也会变成单向。技能给代理定义（破坏性动作和难逆决定是单向），而非检查清单，因此 Merge Danger 一行要格外检查。两点有帮助：确保代理面前有[工单](https://www.aihero.dev/ai-coding-dictionary/ticket)或[规格](https://www.aihero.dev/ai-coding-dictionary/spec)，不只看差异；并将仓库始终视为单向的变更（模式迁移、任何向外发布或删除的操作）写进代理作判断前会读取的位置。

<!-- zh-CN:end db102be27376065e -->

**Does it open the PR for me?**

<!-- zh-CN:begin d10885953fb3a419 -->

**它会替我打开 PR 吗？**

<!-- zh-CN:end d10885953fb3a419 -->

No. `pr` covers only the body. [implement](https://aihero.dev/skills-implement) ends by committing to the current branch. Requests for a skill or option that opens the PR (a `/to-pr`, or `implement` opening a PR instead of committing) are still open proposals. One user's workaround is a one-sentence local override of `implement` that tells it to open a PR. [implement-spec](https://aihero.dev/skills-implement-spec) is the exception: it opens a draft PR when your issue tracker closes work through PRs or when you ask for one. Because `pr` is model-invoked, the agent uses this shape for the body whenever you ask it to open a PR.

<!-- zh-CN:begin 1db9f9cec035af59 -->

不会。`pr` 只管正文。[implement](https://aihero.dev/skills-implement) 以提交到当前分支结束。请求打开 PR 的技能或选项（`/to-pr`，或 `implement` 改为打开 PR）仍是开放提案。有用户的变通方法是给 `implement` 添加一句本地覆盖，让它打开 PR。[implement-spec](https://aihero.dev/skills-implement-spec) 是例外：问题跟踪器通过 PR 关闭工作或你要求时，它会打开草稿 PR。因为 `pr` 由模型调用，代理在其被要求打开 PR 时总会采用此正文形态。

<!-- zh-CN:end 1db9f9cec035af59 -->

**Won't it just produce another wall of text and diagrams?**

<!-- zh-CN:begin af1966564e4f7cfc -->

**它难道不会又产出一大堆文字和图吗？**

<!-- zh-CN:end af1966564e4f7cfc -->

The skill is designed to prevent that, but it can still happen. Users' complaint about agent PR bodies is consistent: "a long summary but all I need to know is what changed, how it was verified, what could break, and whether it's safe to merge." The skill tells the agent to skip preambles, keep prose brief, and pick the smallest view, usually one visual and rarely all of them. If you still get a stack of diagrams, the agent has ignored that. If the body is huge because the diff is huge, the problem is the size of the PR, and `pr` will not split it for you.

<!-- zh-CN:begin 8eb3d2b2f138cef5 -->

技能用于防止这种情况，但仍可能发生。用户对代理 PR 正文的抱怨很一致：“摘要很长，我只想知道改了什么、怎么验证、可能破坏什么、能否安全合并。”技能要求代理省略前言、文字简短并选最小视图，通常一个可视化，很少全用。若仍得到一堆图，是代理忽略了要求。正文因差异巨大而巨大时，问题是 PR 尺寸，`pr` 不会替你拆分。

<!-- zh-CN:end 8eb3d2b2f138cef5 -->

**My repo already has a PR template. Which one wins?**

<!-- zh-CN:begin 46c8ca48fcbb6e97 -->

**仓库已有 PR 模板时以哪个为准？**

<!-- zh-CN:end 46c8ca48fcbb6e97 -->

Neither, by default. `pr` has its own template and does not look for `.github/pull_request_template.md` or anything like it. Several users asked for the skill to use the repo's template. If you do nothing, the agent has two competing instructions for the same document. Settle it in your repo's agent docs, for example by filling the repo template and putting Summary, Evidence and Merge Danger under it.

<!-- zh-CN:begin 6f04ec99d04b4a00 -->

默认两者都不优先。`pr` 有自己的模板，不查找 `.github/pull_request_template.md` 或类似文件。多位用户要求技能使用仓库模板。若什么都不做，代理会对同一文档得到两条竞争指令。应在仓库代理文档中解决，例如填写仓库模板，并在其下放置摘要、证据和 Merge Danger。

<!-- zh-CN:end 6f04ec99d04b4a00 -->

**Is the output HTML? Why doesn't the Mermaid diagram render?**

<!-- zh-CN:begin e3e0d26d0c455985 -->

**输出是 HTML 吗？为什么 Mermaid 图不渲染？**

<!-- zh-CN:end e3e0d26d0c455985 -->

The output is a markdown PR body, not an HTML page. GitHub and GitLab render Mermaid blocks in a PR description, but a terminal does not, so the diagram looks like raw text while the agent is still showing it to you locally. Users on CLI harnesses have worked around that with an ASCII Mermaid renderer or by having the agent attach an HTML version to the PR. Mermaid is one of six views. A call tree, file tree or shaped diff reads the same everywhere.

<!-- zh-CN:begin 6d372b771449130c -->

输出是 Markdown PR 正文，不是 HTML 页面。GitHub 和 GitLab 会渲染 PR 描述中的 Mermaid，终端不会，因此代理在本地展示时像原始文本。CLI 用户使用 ASCII Mermaid 渲染器，或让代理给 PR 附加 HTML 版。Mermaid 只是六种视图之一；调用树、文件树或有形差异在各处都可读。

<!-- zh-CN:end 6d372b771449130c -->

**Can it sort through the review comments that come back?**

<!-- zh-CN:begin 828bf803b87ab80f -->

**能整理返回的审查评论吗？**

<!-- zh-CN:end 828bf803b87ab80f -->

No. It writes the body and stops. Users have asked more than once for a way to triage comments from other developers or review bots (which are worth acting on, which are non-issues). This skill does not do that.

<!-- zh-CN:begin 9046ddd0d53f2675 -->

不能。它写完正文就停止。用户多次要求分诊其他开发者或审查机器人评论（哪些值得处理、哪些不是问题），此技能不做。

<!-- zh-CN:end 9046ddd0d53f2675 -->

**Does it keep the body up to date as the PR changes?**

<!-- zh-CN:begin 5e9949c68762d447 -->

**PR 变化时它保持正文最新吗？**

<!-- zh-CN:end 5e9949c68762d447 -->

No. It writes the body at one point in time, and a PR that changes under review leaves that body stale. Ask the agent to rewrite the body after a large change. The agent is writing a PR body again, so it uses the same shape.

<!-- zh-CN:begin 9bcf590306290cf4 -->

不。正文只在一个时点写出，审查中变化的 PR 会使正文过时。大幅变更后请求代理重写正文；代理再次编写正文时会采用相同形态。

<!-- zh-CN:end 9bcf590306290cf4 -->

**My change has no UI. What goes in Evidence?**

<!-- zh-CN:begin 0a129f004e512ae9 -->

**变更没有 UI，证据写什么？**

<!-- zh-CN:end 0a129f004e512ae9 -->

Everything except the screenshot. The screenshot is the strongest evidence only when the change is visual. For a migration, a background job or a refactor, the evidence is the exact test that failed before and passes now, or the console output that changed. "Tests are green" on its own is a claim, not a before and after.

<!-- zh-CN:begin fe7accd0822858a4 -->

除截图外的所有内容都写。截图只在视觉变更时是最强证据。迁移、后台任务或重构的证据是先前失败、现通过的确切测试，或发生变化的控制台输出。单说“测试全绿”是主张，不是前后对照。

<!-- zh-CN:end fe7accd0822858a4 -->

**Can it mark the body as written by an LLM?**

<!-- zh-CN:begin 10a73497a1f6e13b -->

**能把正文标为 LLM 撰写吗？**

<!-- zh-CN:end 10a73497a1f6e13b -->

Not by itself. One user's approach is a standing instruction in the repo's agent docs that every issue, comment, and PR the agent writes ends with a disclosure line. That rule belongs in the repo, where it covers everything the agent posts, rather than in a template for one kind of document.

<!-- zh-CN:begin 954c76338c90919c -->

不能自动。某用户的方法是在仓库代理文档中加入常驻指令：每个问题、评论和 PR 末尾都有披露行。规则属于仓库，可覆盖代理发布的一切，而非只为一种文档设置模板。

<!-- zh-CN:end 954c76338c90919c -->

## It's working if

<!-- zh-CN:begin 3f27556d45c758ce -->

## 正常工作的表现

<!-- zh-CN:end 3f27556d45c758ce -->

- You can tell what the PR changes from the Summary visual alone, before opening the diff.

<!-- zh-CN:begin 4fbd907c66bc609c -->

- 打开差异前，单看摘要视图就能知道 PR 改了什么。

<!-- zh-CN:end 4fbd907c66bc609c -->
- The body has no preamble: it starts at the Summary heading.

<!-- zh-CN:begin e937e5ec9c42f52a -->

- 正文没有前言，直接从摘要标题开始。

<!-- zh-CN:end e937e5ec9c42f52a -->
- The Evidence section shows a before and an after, not a claim that tests pass.

<!-- zh-CN:begin 8d26ff2e434801fa -->

- 证据展示前后对照，而不是声称测试通过。

<!-- zh-CN:end 8d26ff2e434801fa -->
- Every PR states a door and a blast radius, and the one-way doors are the ones you slow down on.

<!-- zh-CN:begin dde75333e1844e01 -->

- 每个 PR 都说明门类型和影响半径，单向门是你会放慢检查的那些。

<!-- zh-CN:end dde75333e1844e01 -->

## Where it fits

<!-- zh-CN:begin 81a6758990b97d99 -->

## 所处位置

<!-- zh-CN:end 81a6758990b97d99 -->

`pr` comes between review and retro when the build ships as a pull request: `to-spec → to-tickets → implement → code-review → pr → retro`. It is model-invoked, so it also fires on its own any time the agent writes a PR body outside that chain.

<!-- zh-CN:begin 6840a9cbf84f01ab -->

以拉取请求交付构建时，`pr` 位于审查与回顾之间：`to-spec → to-tickets → implement → code-review → pr → retro`。它由模型调用，因此代理在该链之外编写 PR 正文时也会触发。

<!-- zh-CN:end 6840a9cbf84f01ab -->

- [code-review](https://aihero.dev/skills-code-review) runs before it, because a PR body should describe a diff that has already been reviewed.

<!-- zh-CN:begin b1d98d0f3d4a8c80 -->

- [code-review](https://aihero.dev/skills-code-review) 先运行，因为 PR 正文应描述已审查的差异。

<!-- zh-CN:end b1d98d0f3d4a8c80 -->
- [implement](https://aihero.dev/skills-implement) produces the commits the body describes.

<!-- zh-CN:begin 7298131029560d3a -->

- [implement](https://aihero.dev/skills-implement) 产生正文描述的提交。

<!-- zh-CN:end 7298131029560d3a -->

[ask-matt](https://aihero.dev/skills-ask-matt) routes across the whole set when you are unsure which skill the situation wants.

<!-- zh-CN:begin 9508bfb2586dd7f7 -->

不确定情形需要哪个技能时，[ask-matt](https://aihero.dev/skills-ask-matt) 在整个技能集中路由。

<!-- zh-CN:end 9508bfb2586dd7f7 -->
