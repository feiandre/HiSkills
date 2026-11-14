"""Split independent translation files into balanced, disjoint batches."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
jobs = ROOT / ".translation-jobs"
jobs.mkdir(exist_ok=True)
for project, count in [("matt-pocock", 2), ("superpowers", 2), ("pstack", 2)]:
    batches = [[] for _ in range(count)]
    sizes = [0] * count
    for path in sorted((ROOT / project).rglob("SKILL.md"), key=lambda p: p.stat().st_size, reverse=True):
        index = sizes.index(min(sizes))
        batches[index].append(path.relative_to(ROOT).as_posix())
        sizes[index] += path.stat().st_size
    for index, paths in enumerate(batches, 1):
        name = f"{project}-{index}"
        (jobs / f"{name}.json").write_text(json.dumps(paths, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{name}: {len(paths)} files, {sizes[index-1]} source bytes")
