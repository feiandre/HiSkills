"""Build a Chinese reading index from the pinned source manifests."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLES = {
    "ask-matt": "技能导航：为当前问题选择合适的技能和流程",
    "code-review": "代码审查：检查规范与需求符合性",
    "codebase-design": "代码库设计：深模块、接口与职责边界",
    "diagnosing-bugs": "缺陷诊断：建立证据并定位根因",
    "domain-modeling": "领域建模：术语表与架构决策",
    "grill-with-docs": "结合文档进行追问（保留上游迁移说明）",
    "implement": "实现入口（保留上游迁移说明）",
    "implement-spec": "按照规格说明实施变更",
    "improve-codebase-architecture": "寻找并改善代码库的架构边界",
    "pr": "编写清楚、便于审查的 PR 说明",
    "prototype": "制作原型以验证设计问题",
    "research": "查阅一手资料并记录研究结论",
    "retro": "回顾工作并提炼可复用经验",
    "setup-matt-pocock-skills": "配置 Matt Pocock 技能在当前仓库中的使用方式",
    "tdd": "测试驱动开发：红、绿、重构循环",
    "to-spec": "将想法整理为规格说明",
    "to-tickets": "将规格拆解为可执行任务",
    "triage": "分诊、梳理并安排待办工作",
    "wayfinder": "探索代码与需求，找到下一步路径",
    "wizard": "生成引导用户操作的交互式向导",
    "chief-of-staff": "协调工作、信息和决策的参谋技能",
    "claude-handoff": "在代理会话之间交接上下文",
    "loop-me": "组织持续迭代的工作循环",
    "setup-ts-deep-modules": "配置 TypeScript 深模块实践",
    "writing-beats": "组织写作中的节奏与内容单元",
    "writing-fragments": "采集并使用写作片段",
    "writing-shape": "规划文章的结构和表达形态",
    "git-guardrails-claude-code": "通过钩子为危险 Git 操作设置保护",
    "migrate-to-shoehorn": "将测试数据断言迁移到 shoehorn",
    "scaffold-exercises": "搭建课程练习、解答和讲解目录",
    "setup-pre-commit": "配置提交前格式、类型与测试检查",
    "grill-me": "追问入口（保留上游迁移说明）",
    "grilling": "通过持续追问检验计划和想法",
    "handoff": "为后续代理整理工作交接",
    "teach": "用清楚的语言讲解代码和决策",
    "to-questionnaire": "把待澄清的问题整理为问卷",
    "wait-what": "澄清难以理解的上下文或说法",
    "writing-for-agents": "为代理编写可预测、可执行的文档",
    "brainstorming": "通过讨论明确需求并形成设计",
    "diagnosing-superpowers": "诊断 Superpowers 工作流出现的问题",
    "dispatching-parallel-agents": "将独立任务分派给并行子代理",
    "executing-plans": "按照既定实施计划逐项执行",
    "finishing-a-development-branch": "完成开发分支并选择整合方式",
    "receiving-code-review": "核实并处理代码审查反馈",
    "requesting-code-review": "在完成实现后请求代码审查",
    "subagent-driven-development": "以子代理实施并进行分阶段审查",
    "systematic-debugging": "按系统化流程复现、定位和修复问题",
    "test-driven-development": "通过测试驱动功能实现与缺陷修复",
    "using-git-worktrees": "建立隔离的 Git 工作目录",
    "using-superpowers": "理解并使用 Superpowers 技能体系",
    "verification-before-completion": "在宣告完成前提供实际验证证据",
    "writing-plans": "将需求拆解为详细实施计划",
    "writing-skills": "编写、验证和改进代理技能",
    "reproduce-and-fix-issues": "Benny 自动化：复现并修复问题",
    "setup-benny": "Benny 自动化：配置运行环境与流程",
    "triage-issue-reports": "Benny 自动化：分诊问题报告",
    "architect": "在实现前明确类型、接口和模块形态",
    "arena": "让多个方案竞争并整合优点",
    "automate-me": "把个人工作习惯整理成模式技能",
    "benchmark-checklist": "检查性能数据与基准测试是否可信",
    "blast-radius": "评估变更对差异之外代码的影响",
    "bro": "用直白语言重新说明上一条回复",
    "correct": "将反复出现的代理错误转为改进措施",
    "create-formal-verification-skill": "创建形式化验证技能",
    "create-verification-skill": "创建可验证实际应用行为的技能",
    "figure-it-out": "组织一次严谨的自主问题求解",
    "how": "调查代码当前如何工作",
    "in-your-own-words": "用自己的话复述并澄清需求",
    "interrogate": "通过质询审查代码变更",
    "ketchup": "补齐本次对话的进展与待决事项",
    "ketchup-video": "通过视频形式补齐任务进展",
    "maintain-formal-verification-skill": "维护与更新形式化验证技能",
    "maintain-verification-skill": "维护应用行为验证技能",
    "make-bot-ui": "构建能触发 Grok Bot 的界面",
    "no-comments": "让代码本身表达意图并清理多余注释",
    "poteto-help": "Pstack 导航与使用帮助",
    "poteto-mode": "Pstack 主入口：路由任务、执行流程与验证结果",
    "principle-attack-the-premise": "原则：先质疑问题的前提",
    "principle-boundary-discipline": "原则：严守模块与职责边界",
    "principle-build-the-lever": "原则：先建立能放大效率的工具",
    "principle-encode-lessons-in-structure": "原则：把经验落实到结构中",
    "principle-exhaust-the-design-space": "原则：充分探索可行设计",
    "principle-experience-first": "原则：优先关注实际使用体验",
    "principle-explain-the-number": "原则：说明数字的来源和含义",
    "principle-fix-root-causes": "原则：修复根因",
    "principle-foundational-thinking": "原则：从基础问题出发思考",
    "principle-guard-the-context-window": "原则：保护上下文窗口",
    "principle-laziness-protocol": "原则：用更省力的方法解决真正的问题",
    "principle-make-operations-idempotent": "原则：让操作具备幂等性",
    "principle-migrate-callers-then-delete-legacy-apis": "原则：先迁移调用方，再删除旧 API",
    "principle-minimize-reader-load": "原则：减轻阅读者的理解负担",
    "principle-model-the-domain": "原则：准确建模领域概念",
    "principle-never-block-on-the-human": "原则：继续推进不依赖用户答复的工作",
    "principle-outcome-oriented-execution": "原则：围绕结果执行任务",
    "principle-prove-it-works": "原则：用证据证明功能有效",
    "principle-redesign-from-first-principles": "原则：从第一性原理重新设计",
    "principle-separate-before-serializing-shared-state": "原则：串行化共享状态前先考虑分离状态",
    "principle-sequence-verifiable-units": "原则：按可验证单元安排工作顺序",
    "principle-subtract-before-you-add": "原则：增加东西之前先尝试删减",
    "principle-test-behavior-not-implementation": "原则：测试行为而非实现细节",
    "principle-type-system-discipline": "原则：严谨使用类型系统",
    "recall": "恢复近期工作与相关上下文",
    "reflect": "回顾任务并提炼技能改进",
    "setup-pstack": "配置 Pstack 的推理预算和模型角色",
    "sharpen": "将提示词改得明确而可执行",
    "show-me-your-work": "记录并展示决策过程与证据",
    "statechart": "通过状态图建模并验证状态行为",
    "swarm": "分配独立工作切片或并行尝试并汇总结果",
    "technical-writing": "撰写清晰、准确的技术说明",
    "typescript-best-practices": "TypeScript 类型与工程实践",
    "unslop": "删除空泛表达并提升文字质量",
    "why": "调查代码和设计形成的原因",
}

def main() -> None:
    lines = ["# Skills 中文阅读索引", "", "共 114 份 `SKILL.md`。每个链接打开对应技能文件，中文译文紧跟对应英文块，保留原有 Markdown 形式。以下中文用途用于导航，具体触发条件、限制和步骤请阅读技能全文。", "", "[返回资料说明](README.md) · [全部 Markdown 文档索引](DOCUMENTS.zh-CN.md)", ""]
    for project, title in [("matt-pocock", "Matt Pocock Skills"), ("superpowers", "Superpowers"), ("pstack", "Pstack")]:
        record = json.loads((ROOT / f"{project}.source.json").read_text(encoding="utf-8"))
        skills = sorted(path for path in record["original_files"] if path.endswith("/SKILL.md") or path == "SKILL.md")
        lines.extend([f"## {title}（{len(skills)} 份）", ""])
        previous_group = None
        for relative in skills:
            path = Path(relative)
            name = path.parent.name
            group = path.parent.parent.as_posix()
            if group != previous_group:
                lines.extend([f"### `{group}/`", "", "| 技能 | 中文用途 |", "| --- | --- |"])
                previous_group = group
            if name not in TITLES:
                raise ValueError(f"Missing Chinese title: {name}")
            lines.append(f"| [{name}]({project}/{relative}) | {TITLES[name]} |")
            # Separate groups without inserting blank lines into a single table.
            next_index = skills.index(relative) + 1
            if next_index == len(skills) or Path(skills[next_index]).parent.parent.as_posix() != group:
                lines.append("")
    (ROOT / "SKILLS.zh-CN.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Built SKILLS.zh-CN.md with 114 entries")

if __name__ == "__main__":
    main()
