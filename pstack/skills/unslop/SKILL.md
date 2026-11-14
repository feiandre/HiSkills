---
name: unslop
description: 去除任何写作中的 AI 痕迹。
disable-model-invocation: true
---

# 去 AI 腔

编辑文本以移除 AI 模式。扫描下方模式，然后重写。保留含义并匹配预期语气。

## 要检测并修复的模式

规则编号是其他技能引用的稳定 ID。删除规则会留下空缺。

### 内容

3. **表面化的 -ing 短语。**“highlighting...”“ensuring...”“reflecting...”“showcasing...”“fostering...”。删除，或用真实来源展开。

5. **含糊的归因。**“专家认为”“行业报告表明”“一些批评者主张”。点名来源或删除。

### 语言

7. **AI 词汇。**Additionally、crucial、delve、enduring、enhance、fostering、garner、interplay、intricate、landscape（抽象用法）、pivotal、showcase、tapestry（抽象用法）、testament、underscore、vibrant。换成平实词。

8. **表达“是”的花哨方式。**“serves as”“stands as”“boasts”“features”。说“is”或“has”。

9. **“不只是 X，而是 Y。”**改为直接陈述要点。

10. **三法则。**不要强行把观点分成三组。使用自然数量。

11. **同义词轮换。**Protagonist、main character、central figure、hero 全在一段里。选择一个并重复。

12. **虚假范围。**“from X to Y”中 X 与 Y 不在有意义尺度上。直接列出主题。

### 风格

13. **滥用破折号。**完全避免长破折号。只用句号或逗号（不用括号、短破折号或连字符充当破折号）。若要分隔想法，结束句子或使用逗号。

14. **滥用冒号。**列表中或示例前可用冒号，但不要用作句中连接器。“If you're coming from traditional automation: instead of registering event handlers, you describe conditions”中的冒号没有增加价值。重写以不靠比较框架让论点独立。“Describing when the scheduler should fire works best as plain English.”含义相同，无需标点拐杖。

15. **滥用粗体。**不要给每个专有名词或缩写加粗。

16. **行内标题列表。**迹象是粗体标签加冒号后重述该行：“**Performance:** Performance improved...”。改为正文。以句号结束、点名条目并跟随真正新细节的粗体引导（“**TypeScript 中的 Schema。**表位于一个文件。”）可以接受，不是问题。

17. **标题大写格式。**使用句首大写。

18. **装饰性 emoji。**从标题和项目符号删除。

19. **弯引号。**使用直引号。

### 沟通制品

20. **聊天机器人短语。**“I hope this helps!”“Let me know if...”“Of course!”“Certainly!”“Found the smoking gun!”删除。

22. **讨好语气。**“Great question! You're absolutely right!”直接回应。

### 填充

23. **填充短语。**“In order to”改为“To”。“Due to the fact that”改为“Because”。删除“It is important to note that”。

24. **过度含糊。**“could potentially possibly be argued that it might”改为“may”。

25. **泛泛结论。**“The future looks bright.”陈述具体计划或事实。

### 术语

26. **抽象隐喻名词。**Substrate（base）、wedge、wedge in（add）、vector（way, method）、locus、vantage、nexus、作为名词的 primitive、作为隐喻的 harness、“API surface”中的 surface、bedrock、作为隐喻的 scaffolding、modality、paradigm、gold-plating（超过工作需要）、作为隐喻的 ratchet（机制的真正名称，或只会收紧的限制）、用于移动代码的 evacuate（move out）、endgame（最后阶段）、north star、flywheel。这些看似技术化，但通常有更平实具体的词。选择具体词。

### 平实表达

27. **说它做什么，不说它给人什么感觉。**“the database stays close at hand”“SQL you can read”“types that follow your schema”表达感受。修复应点名机制或数字：“`.toSQL()` returns the exact string sent to the database”“a column rename fails the build”。问这句话告诉读者做什么或知道什么，然后写出它。若不能改写为具体指令、事实或数字，删掉。再检查：若这句话原样出现在另一个项目文档中也成立，它没有说明本项目，删掉。

28. **缩短或拆分密集句子。**若读者必须回读才能解析，就拆成两句或删去从句。一句一个想法。

29. **主动语态。**优先使用。标记“is/are/was/were + 过去分词”并点名执行者：“queries are validated”改为“the compiler validates queries”，“the file is parsed by the loader”改为“the loader parses the file”。只有执行者未知或确实无关时才可被动。

30. **删掉副词，或用更强动词。**“runs quickly”改为“is fast”或数字，“significantly improves”改为测得的增量。副词支撑弱动词，说明动词错了。

31. **优先平实词。**“utilize”和“leverage”改为“use”，“facilitate”改为“help”，“numerous”改为“many”，“in the event that”改为“if”。更花哨的同义词很少更清楚。

32. **做作表达。**存在字面短语时不要用隐喻或修饰：格言（“wire it or delete it”）、为效果使用修辞片段、把代码拟人化（“the plan holds it”）、比喻性动词（“rides along”“stands on”）、套话框架。“A dial worth turning”改为“a parameter worth varying”。直接说意思。规则 26 涵盖隐喻名词。

33. **过度压缩。**省略冠词、无动词片段、符号语言和缩写会让读者破译而非阅读。“Parser rejects bad date → exit 2, no write”改为“The parser rejects a bad date, exits with code 2, and writes nothing.”用完整句子写冠词和动词，展开箭头与缩写。
