## What it does

<!-- zh-CN:begin 86f0cda7748eeaa8 -->

## 作用

<!-- zh-CN:end 86f0cda7748eeaa8 -->

You type `wait-what` when you did not understand a message. The [agent](https://www.aihero.dev/ai-coding-dictionary/agent) then re-pitches what it just said. It adds the context you were missing, writes in plain English, and uses the vocabulary from your project's `GLOSSARY.md`.

<!-- zh-CN:begin 17c11f6dae0be3c7 -->

当你没听懂一条消息时，输入 `wait-what`。[代理](https://www.aihero.dev/ai-coding-dictionary/agent)会重新解释刚说的话。它补充你缺少的上下文，用平实英语书写，并使用项目 `GLOSSARY.md` 中的词汇。

<!-- zh-CN:end 17c11f6dae0be3c7 -->

The skill is three lines long. That is the design, not an unfinished draft. Skills against verbosity usually fail because they grow too long. A four-hundred-line concision skill still leaves the [model](https://www.aihero.dev/ai-coding-dictionary/model) verbose, because the model copies the length of the skill, not its request. This one has a single precise leading word and nothing else.

<!-- zh-CN:begin 96e3009b88cb4d84 -->

该技能只有三行。这是设计，不是未完成草稿。反对冗长的技能通常失败，因为它们本身太长。四百行的“简洁”技能仍会让[模型](https://www.aihero.dev/ai-coding-dictionary/model)冗长，因为模型会复制技能长度，而不是其请求。这个技能只有一个精确的主导词，别无其他。

<!-- zh-CN:end 96e3009b88cb4d84 -->

## When to reach for it

<!-- zh-CN:begin 02b55d1e9c6561e3 -->

## 何时使用

<!-- zh-CN:end 02b55d1e9c6561e3 -->

You invoke it by typing `/wait-what`. The agent will not reach for it on its own, and it shouldn't. Only you know when you stopped following.

<!-- zh-CN:begin 47b52658ce0ee143 -->

通过输入 `/wait-what` 调用。代理不会自行使用，也不应如此。只有你知道自己何时跟丢了。

<!-- zh-CN:end 47b52658ce0ee143 -->

Use it as soon as you notice you're skimming. For example, the agent has started to use jargon it invented, put five acronyms in one sentence, or explained a decision whose premise you never saw. It fixes the conversation you're already in. To stop the jargon arriving at all, use [grill-with-docs](https://aihero.dev/skills-grill-with-docs), which builds the shared language upfront.

<!-- zh-CN:begin dbbd9382cd6803e4 -->

一旦察觉自己在略读就使用。例如代理开始使用自造术语，在一句里放五个缩写，或解释一个你从未见过前提的决定。它修复你已经在进行的对话。要从源头阻止术语出现，使用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，它提前建立共享语言。

<!-- zh-CN:end dbbd9382cd6803e4 -->

## The name is the mechanism

<!-- zh-CN:begin 5923a01b8eaa57ed -->

## 名称就是机制

<!-- zh-CN:end 5923a01b8eaa57ed -->

The leading word is **wait**. "Be concise" is an instruction about the agent's output, and the model obeys it by clipping words and losing you further. **Wait** is about *your* state. It says you stopped understanding here. An agent that hears "be brief" writes clipped fragments. An agent that hears "wait, you lost me" backs up and explains.

<!-- zh-CN:begin 445a555e7f7bfcb2 -->

主导词是 **wait**（等一下）。“Be concise”是关于代理输出的指令，模型会删词来服从，反而让你更困惑。**Wait** 描述*你的*状态：你在这里停止理解了。听到“be brief”的代理会写残缺片段；听到“wait, you lost me”的代理会回退并解释。

<!-- zh-CN:end 445a555e7f7bfcb2 -->

That difference is the whole skill. Every popular fix for verbosity names the *output*: `/tldr`, `/no-fluff`, `/talk-normal`. The model over-corrects into clipped fragments that are shorter and no clearer. Naming the *listener* asks for both halves at once: fewer words **and** the context you were missing.

<!-- zh-CN:begin 48a19cddf685925a -->

这个区别就是整个技能。流行的冗长修复都命名*输出*：`/tldr`、`/no-fluff`、`/talk-normal`。模型会过度纠正成更短却不更清楚的残缺片段。命名*听者*同时要求两半：更少词 **且** 补充缺失上下文。

<!-- zh-CN:end 48a19cddf685925a -->

The skill says re-pitch **that**, not "that last message". What lost you is usually bigger than one paragraph, so the agent decides how far back to go.

<!-- zh-CN:begin f8080307c13ae301 -->

技能说重新解释**那个**，而不是“最后一条消息”。让你困惑的内容通常超过一段，因此代理决定回溯多远。

<!-- zh-CN:end f8080307c13ae301 -->

## It plugs into the language you already have

<!-- zh-CN:begin c52e87f61a66d576 -->

## 接入你已有的语言

<!-- zh-CN:end c52e87f61a66d576 -->

The body reuses the leading words already in your global `CLAUDE.md` and your project's `GLOSSARY.md`. ASD-STE100 Simplified Technical English sets the register. The ubiquitous language supplies the nouns. The skill, `CLAUDE.md` and `GLOSSARY.md` use the same [tokens](https://www.aihero.dev/ai-coding-dictionary/token), so invoking it is not a new instruction. It is a reminder of one the agent already agreed to.

<!-- zh-CN:begin a0976e86e8386cd7 -->

正文复用全局 `CLAUDE.md` 和项目 `GLOSSARY.md` 中已有的主导词。ASD-STE100 简化技术英语设定语域，通用语言提供名词。技能、`CLAUDE.md` 与 `GLOSSARY.md` 使用相同 [token](https://www.aihero.dev/ai-coding-dictionary/token)，所以调用它不是新指令，而是提醒代理已同意的指令。

<!-- zh-CN:end a0976e86e8386cd7 -->

If you have no `GLOSSARY.md` (and no `GLOSSARY-MAP.md` pointing to one for the context at hand), the skill still works. You lose only the domain-vocabulary half.

<!-- zh-CN:begin 811896744b5e1450 -->

若没有 `GLOSSARY.md`（也没有为当前上下文指向它的 `GLOSSARY-MAP.md`），技能仍工作。你只会失去领域词汇的那一半。

<!-- zh-CN:end 811896744b5e1450 -->

## It's working if

<!-- zh-CN:begin 817e0c6614d4bb8b -->

## 怎样算有效

<!-- zh-CN:end 817e0c6614d4bb8b -->

- The re-pitch is **shorter and clearer**, not shorter and blunter.

<!-- zh-CN:begin 953ffcee34a32e41 -->

- 重新解释**更短且更清楚**，而不是更短却更生硬。

<!-- zh-CN:end 953ffcee34a32e41 -->
- It adds the premise you were missing, instead of only deleting words.

<!-- zh-CN:begin 2f944b88e265db09 -->

- 它补充你缺少的前提，而不只是删词。

<!-- zh-CN:end 2f944b88e265db09 -->
- Project nouns replace invented ones. The terms in your `GLOSSARY.md` come back.

<!-- zh-CN:begin afca27d50b8ae6d2 -->

- 项目名词取代自造词。`GLOSSARY.md` 中的术语会回来。

<!-- zh-CN:end afca27d50b8ae6d2 -->
- You can use it twice in a row, and it does not degrade into terseness.

<!-- zh-CN:begin e35b014ee8c3d539 -->

- 可连续使用两次，而且不会退化成过度简短。

<!-- zh-CN:end e35b014ee8c3d539 -->

## Where it fits

<!-- zh-CN:begin 9f7ced9767b219e4 -->

## 所处位置

<!-- zh-CN:end 9f7ced9767b219e4 -->

You can use `wait-what` at any point, in any conversation, inside any other skill. It repairs one message after the fact. The real fix is a shared language agreed upfront, and that is [grill-with-docs](https://aihero.dev/skills-grill-with-docs): a [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) session that runs [domain-modeling](https://aihero.dev/skills-domain-modeling) as it goes, so it records the words you both use in your `GLOSSARY.md`. If you're unsure which skill fits the moment, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.

<!-- zh-CN:begin f723f34f6e972241 -->

你可在任何时刻、任何对话、任何其他技能内使用 `wait-what`。它事后修复一条消息。真正的修复是提前约定共享语言，即 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)：一场同时运行 [domain-modeling](https://aihero.dev/skills-domain-modeling) 的 [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) 会话，把双方使用的词记录到 `GLOSSARY.md`。若不确定此刻适合哪项技能，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你路由。

<!-- zh-CN:end f723f34f6e972241 -->
