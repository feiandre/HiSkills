"""Index every upstream Markdown document, including reference material."""
import re
from collections import defaultdict
from inline_translation import ROOT, WORK, load_translations, read_json


def main():
    translations, _ = load_translations()
    projects = defaultdict(list)
    for document in read_json(WORK / "inventory.json"):
        title = ""
        for segment in document["segments"]:
            if segment["kind"] == "heading":
                title = translations.get(segment["id"], {}).get("zh", "")
                if title:
                    title = re.sub(r"^\s*#+\s*", "", title).strip().replace("|", "\\|").replace("\n", " ")
                    break
        projects[document["path"].split("/")[0]].append((document["path"], title))
    lines = ["# 全部 Markdown 文档中文索引", "", "本索引覆盖三个上游项目的全部 399 份 `.md` 文件，包括技能、README、参考资料、操作手册、设计文档、实施计划、测试说明和版本记录。中文紧跟对应英文，形式与原文对应。", "", "[资料说明](README.md) · [114 份技能索引](SKILLS.zh-CN.md)", ""]
    for project in ("matt-pocock", "superpowers", "pstack"):
        entries = projects[project]
        lines.extend([f"## {project}（{len(entries)} 份）", "", "| 文档路径 | 中文标题 |", "| --- | --- |"])
        for path, title in entries:
            relative = path.split("/", 1)[1]
            lines.append(f"| [{relative}]({path}) | {title or '按原文件路径阅读'} |")
        lines.append("")
    (ROOT / "DOCUMENTS.zh-CN.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Indexed {sum(len(v) for v in projects.values())} Markdown documents")


if __name__ == "__main__":
    main()
