"""Verify source integrity and Chinese-translation coverage; no upstream code runs."""
from __future__ import annotations
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BEGIN = b"<!-- BEGIN CHINESE TRANSLATION -->"
END = b"<!-- END CHINESE TRANSLATION -->"

def main() -> None:
    failures = []
    projects = []
    for name in ("matt-pocock", "superpowers", "pstack"):
        record = json.loads((ROOT / f"{name}.source.json").read_text(encoding="utf-8"))
        archive_path = ROOT / record["archive_path"]
        if hashlib.sha256(archive_path.read_bytes()).hexdigest() != record["archive_sha256"]:
            failures.append(f"{name}: archive checksum mismatch")
        entries = []
        unchanged = 0
        with zipfile.ZipFile(archive_path) as bundle:
            prefix = bundle.namelist()[0].split("/")[0] + "/"
            if record["subdirectory"]:
                prefix += record["subdirectory"] + "/"
            for relative, expected_hash in record["original_files"].items():
                path = ROOT / name / relative
                if not path.is_file():
                    failures.append(f"Missing: {name}/{relative}")
                    continue
                original = bundle.read(prefix + relative)
                actual = path.read_bytes()
                if hashlib.sha256(original).hexdigest() != expected_hash:
                    failures.append(f"{name}/{relative}: archive/manifest disagreement")
                if path.name != "SKILL.md":
                    if actual != original:
                        failures.append(f"{name}/{relative}: upstream supporting file changed")
                    else:
                        unchanged += 1
                    continue
                file_failures = []
                if not actual.startswith(original):
                    file_failures.append("Original bytes changed")
                suffix = actual[len(original):]
                if suffix.count(BEGIN) != 1 or suffix.count(END) != 1:
                    file_failures.append("Missing or duplicate translation markers")
                if not suffix.rstrip().endswith(END):
                    file_failures.append("Translation end marker not at EOF")
                try:
                    source = original.decode("utf-8-sig")
                    translation = suffix.decode("utf-8")
                except UnicodeDecodeError as error:
                    file_failures.append(f"UTF-8 error: {error}")
                    source, translation = "", ""
                cjk = len(re.findall(r"[\u4e00-\u9fff]", translation))
                if cjk < 15:
                    file_failures.append("Too little Chinese text")
                if "\ufffd" in translation:
                    file_failures.append("Unicode replacement characters")
                headings = lambda text: len(re.findall(r"(?m)^#{1,6}\s+", re.sub(r"(?ms)^```.*?^```[^\n]*", "", text)))
                if source and headings(translation) < headings(source):
                    file_failures.append("Fewer translated headings than source headings; review coverage")
                code_blocks = lambda text: len(re.findall(r"(?m)^```[^`\n]*$", text)) // 2
                # Missing links/code can reveal accidental summaries. Keep these
                # as review signals: a faithful translation may reformat either.
                source_links = set(re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", source))
                translated_links = set(re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", translation))
                for reason in file_failures:
                    failures.append(f"{name}/{relative}: {reason}")
                entries.append({
                    "path": f"{name}/{relative}",
                    "original_sha256": expected_hash,
                    "original_bytes": len(original),
                    "translation_bytes": len(suffix),
                    "chinese_characters": cjk,
                    "source_headings": headings(source),
                    "translation_headings": headings(translation),
                    "source_code_blocks": code_blocks(source),
                    "translation_code_blocks": code_blocks(translation),
                    "links_to_review": sorted(source_links - translated_links),
                    "original_preserved": actual.startswith(original),
                    "status": "pass" if not file_failures else "fail",
                })
        expected_paths = {entry["path"] for entry in entries}
        for path in (ROOT / name).rglob("SKILL.md"):
            if path.relative_to(ROOT).as_posix() not in expected_paths:
                failures.append(f"Unexpected SKILL.md: {path.relative_to(ROOT)}")
        projects.append({"name": name, "commit": record["commit"], "original_file_count": len(record["original_files"]), "skill_count": len(entries), "unchanged_supporting_files": unchanged, "skills": entries})
    review_signals = []
    for project in projects:
        for entry in project["skills"]:
            if entry["chinese_characters"] < 15:
                continue
            if entry["translation_bytes"] < entry["original_bytes"] * 0.65:
                review_signals.append({"path": entry["path"], "reason": "Short translation; check completeness"})
            if entry["source_code_blocks"] > entry["translation_code_blocks"]:
                review_signals.append({"path": entry["path"], "reason": "Fewer code blocks; check examples"})
            if entry["links_to_review"]:
                review_signals.append({"path": entry["path"], "reason": "Source link targets absent from translation", "links": entry["links_to_review"]})
    report = {"verified_at_utc": datetime.now(timezone.utc).isoformat(), "passed": not failures, "skill_count": sum(p["skill_count"] for p in projects), "projects": projects, "failures": failures, "review_signals": review_signals,
              "scope": "Local source integrity, UTF-8, translation markers and heading coverage. Semantic completeness needs review; upstream workflows were not executed."}
    (ROOT / "verification-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": report["passed"], "skill_count": report["skill_count"], "projects": [{k:v for k,v in project.items() if k != "skills"} for project in projects], "failures": failures}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] else 1)

if __name__ == "__main__":
    if (ROOT / ".inline-translation" / "inventory.json").exists():
        from inline_translation import verify
        raise SystemExit(0 if verify() else 1)
    main()
