"""Prepare, render, and verify adjacent English/Chinese Markdown blocks.

Only local snapshots are read. Upstream instructions are never executed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".inline-translation"
PROJECTS = ("matt-pocock", "superpowers", "pstack")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def blocks(text: str):
    """Keep every source character; split headings, items, tables and fences."""
    lines = text.splitlines(keepends=True)
    index = 0
    if lines and lines[0].strip() == "---":
        end = next((n + 1 for n in range(1, len(lines)) if lines[n].strip() == "---"), None)
        if end:
            yield "frontmatter", "".join(lines[:end])
            index = end
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            yield "blank", line
            index += 1
            continue
        fence = re.match(r"^(\s*)(`{3,}|~{3,})(.*)", line)
        if fence:
            mark = fence.group(2)
            end = index + 1
            while end < len(lines):
                if re.match(r"^\s*" + re.escape(mark[0]) + "{" + str(len(mark)) + r",}\s*$", lines[end]):
                    end += 1
                    break
                end += 1
            yield "code", "".join(lines[index:end])
            index = end
            continue
        if re.match(r"^\s*\|", line) and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[index + 1]):
            end = index + 1
            while end < len(lines) and lines[end].strip() and "|" in lines[end]:
                end += 1
            yield "table", "".join(lines[index:end])
            index = end
            continue
        if re.match(r"^\s{0,3}#{1,6}\s+", line):
            yield "heading", line
            index += 1
            continue
        if re.match(r"^\s*(?:[-+*]|\d+[.)])\s+", line):
            end = index + 1
            while end < len(lines) and lines[end].strip():
                if re.match(r"^\s*(?:[-+*]|\d+[.)])\s+|^\s*#{1,6}\s+|^\s*(`{3,}|~{3,})|^\s*\|", lines[end]):
                    break
                end += 1
            yield "list", "".join(lines[index:end])
            index = end
            continue
        if line.lstrip().startswith(">"):
            end = index + 1
            while end < len(lines) and lines[end].lstrip().startswith(">"):
                end += 1
            yield "quote", "".join(lines[index:end])
            index = end
            continue
        if re.match(r"^\s*(?:[-*_]\s*){3,}$", line):
            yield "raw", line
            index += 1
            continue
        if re.match(r"^\s*\[[^]]+\]:\s*\S+", line):
            yield "raw", line
            index += 1
            continue
        end = index + 1
        while end < len(lines) and lines[end].strip():
            if re.match(r"^\s*(?:#{1,6}\s+|[-+*]\s+|\d+[.)]\s+|`{3,}|~{3,}|>|\|)", lines[end]):
                break
            end += 1
        yield "paragraph", "".join(lines[index:end])
        index = end


def prepare():
    if (WORK / "inventory.json").exists():
        raise SystemExit("Inventory already exists; refusing to replace work in progress")
    documents = []
    jobs = []
    for project in PROJECTS:
        record = read_json(ROOT / f"{project}.source.json")
        with zipfile.ZipFile(ROOT / record["archive_path"]) as archive:
            prefix = archive.namelist()[0].split("/")[0] + "/"
            if record["subdirectory"]:
                prefix += record["subdirectory"] + "/"
            for relative in sorted(record["original_files"]):
                if not relative.lower().endswith(".md"):
                    continue
                path = f"{project}/{relative}"
                raw = archive.read(prefix + relative)
                source = raw.decode("utf-8")
                existing = ROOT / path
                backup = WORK / "backup" / path
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(existing, backup)
                if b"<!-- BEGIN CHINESE TRANSLATION -->" in existing.read_bytes():
                    hint = existing.read_text(encoding="utf-8").split("<!-- BEGIN CHINESE TRANSLATION -->", 1)[1]
                    hint_path = WORK / "previous-translations" / (path + ".txt")
                    hint_path.parent.mkdir(parents=True, exist_ok=True)
                    hint_path.write_text(hint, encoding="utf-8")
                segments = []
                for number, (kind, original) in enumerate(blocks(source)):
                    identifier = hashlib.sha256(f"{path}:{number}".encode()).hexdigest()[:16]
                    translate = kind not in ("blank", "raw") and bool(re.search(r"[A-Za-z]{2,}", original))
                    segments.append({"id": identifier, "kind": kind, "original": original, "translate": translate})
                assert "".join(segment["original"] for segment in segments).encode("utf-8") == raw
                document = {"path": path, "sha256": hashlib.sha256(raw).hexdigest(), "source_bytes": len(raw), "segments": segments}
                documents.append(document)
                batch, size = [], 0
                for segment in (s for s in segments if s["translate"]):
                    batch.append(segment)
                    size += len(segment["original"].encode("utf-8"))
                    if size >= 13000:
                        jobs.append({"path": path, "segments": batch, "source_bytes": size})
                        batch, size = [], 0
                if batch:
                    jobs.append({"path": path, "segments": batch, "source_bytes": size})
    assignments = [[] for _ in range(6)]
    sizes = [0] * 6
    for index, job in enumerate(sorted(jobs, key=lambda job: job["source_bytes"], reverse=True)):
        job_id = f"{index:04d}"
        job["job_id"] = job_id
        write_json(WORK / "jobs" / f"{job_id}.json", job)
        worker = sizes.index(min(sizes))
        assignments[worker].append(job_id)
        sizes[worker] += job["source_bytes"]
    for worker, assignment in enumerate(assignments, 1):
        write_json(WORK / "assignments" / f"worker-{worker}.json", assignment)
    write_json(WORK / "inventory.json", documents)
    print(json.dumps({"documents": len(documents), "source_bytes": sum(d["source_bytes"] for d in documents), "jobs": len(jobs), "worker_bytes": sizes, "projects": dict(Counter(d["path"].split("/")[0] for d in documents))}, ensure_ascii=False))


def save(job_id: str, translations: dict):
    """Worker API: save a complete mapping id -> Chinese Markdown string.

For a block consisting solely of executable code/identifiers/URLs, use
{"zh": "", "skip_reason": "specific explanation"}; prose cannot be skipped.
"""
    job = read_json(WORK / "jobs" / f"{job_id}.json")
    expected = {s["id"] for s in job["segments"]}
    if set(translations) != expected:
        raise ValueError(f"{job_id}: missing={expected-set(translations)}, extra={set(translations)-expected}")
    for segment in job["segments"]:
        entry = translations[segment["id"]]
        if isinstance(entry, str):
            entry = {"zh": entry}
            translations[segment["id"]] = entry
        zh = entry["zh"]
        if not zh.strip():
            if not entry.get("skip_reason"):
                raise ValueError(f"{job_id}/{segment['id']}: empty translation requires explanation")
            readable = re.sub(r"`[^`]*`|https?://\S+|<[^>]*>", "", segment["original"])
            readable = re.sub(r"\]\([^)]*\)", "]", readable)
            if segment["kind"] not in ("code", "frontmatter") and len(re.findall(r"\b[A-Za-z]{2,}\b", readable)) >= 3:
                raise ValueError(f"{job_id}/{segment['id']}: natural-language prose must be translated")
        elif not re.search(r"[\u4e00-\u9fff]", zh):
            raise ValueError(f"{job_id}/{segment['id']}: Chinese text required")
        if "\ufffd" in zh:
            raise ValueError(f"{job_id}/{segment['id']}: replacement characters")
        if zh.strip():
            original = segment["original"]
            tokens = lambda value: Counter(re.findall(r"`([^`\n]+)`", value))
            if segment["kind"] != "frontmatter" and any(tokens(original)[token] > tokens(zh)[token] for token in tokens(original)):
                raise ValueError(f"{job_id}/{segment['id']}: preserve inline-code identifiers and values")
            destinations = lambda value: Counter(re.findall(r"\]\((?:<)?([^\s)>]+)", value))
            if any(destinations(original)[url] > destinations(zh)[url] for url in destinations(original)):
                raise ValueError(f"{job_id}/{segment['id']}: preserve Markdown link destinations")
            html_tags = lambda value: Counter(re.findall(r"</?([A-Za-z][\w-]*)\b", value))
            if any(html_tags(original)[tag] > html_tags(zh)[tag] for tag in html_tags(original)):
                raise ValueError(f"{job_id}/{segment['id']}: preserve HTML tag structure")
            if segment["kind"] == "heading":
                prefix = re.match(r"^(\s*#{1,6}\s+)", original).group(1)
                if not zh.startswith(prefix):
                    raise ValueError(f"{job_id}/{segment['id']}: preserve heading level")
            if segment["kind"] == "list":
                prefix = re.match(r"^(\s*(?:[-+*]|\d+[.)])\s+)", original).group(1)
                if not zh.startswith(prefix):
                    raise ValueError(f"{job_id}/{segment['id']}: preserve list indentation and marker {prefix!r}")
            if segment["kind"] == "table":
                rows = lambda value: [line.strip() for line in value.strip().splitlines() if line.strip()]
                if len(rows(original)) != len(rows(zh)) or [line.count('|') for line in rows(original)] != [line.count('|') for line in rows(zh)]:
                    raise ValueError(f"{job_id}/{segment['id']}: preserve table row/column structure")
            if segment["kind"] == "code":
                first = original.splitlines()[0]
                if zh.splitlines()[0] != first:
                    raise ValueError(f"{job_id}/{segment['id']}: preserve code fence and language")
            if segment["kind"] == "quote" and not zh.lstrip().startswith('>'):
                raise ValueError(f"{job_id}/{segment['id']}: preserve blockquote")
    write_json(WORK / "translations" / f"{job_id}.json", translations)
    return {"job": job_id, "segments": len(expected), "path": job["path"]}


def load_translations():
    result, complete_jobs = {}, 0
    for path in sorted((WORK / "translations").glob("*.json")) if (WORK / "translations").exists() else []:
        values = read_json(path)
        values = {key: ({"zh": value} if isinstance(value, str) else value) for key, value in values.items()}
        if result.keys() & values.keys():
            raise ValueError("Duplicate segment translation")
        result.update(values)
        complete_jobs += 1
    return result, complete_jobs


def addition(segment, zh):
    identifier = segment["id"]
    if segment["kind"] == "frontmatter":
        comments = "\n".join("# " + line for line in zh.rstrip().splitlines())
        return f"\n# zh-CN:begin {identifier}\n{comments}\n# zh-CN:end {identifier}\n"
    if segment["kind"] != "code" and re.search(r"<summary\b[^>]*>.*?</summary>", segment["original"], re.S):
        match = re.search(r"<summary\b[^>]*>(.*?)</summary>", zh, re.S)
        inner = match.group(1) if match else re.sub(r"</?details[^>]*>", "", zh).strip()
        return f"<!-- zh-CN:begin {identifier} --><br>{inner}<!-- zh-CN:end {identifier} -->"
    indent = re.match(r"[ \t]*", segment["original"]).group()
    return f"\n{indent}<!-- zh-CN:begin {identifier} -->\n\n{zh.rstrip()}\n\n{indent}<!-- zh-CN:end {identifier} -->\n"


def render():
    translations, _ = load_translations()
    rendered = 0
    for document in read_json(WORK / "inventory.json"):
        if any(s["translate"] and s["id"] not in translations for s in document["segments"]):
            continue
        output = []
        for segment in document["segments"]:
            original = segment["original"]
            entry = translations.get(segment["id"], {})
            zh = entry.get("zh", "")
            if zh.strip() and segment["kind"] == "frontmatter":
                lines = original.splitlines(keepends=True)
                output.append("".join(lines[:-1]) + addition(segment, zh) + lines[-1])
            elif zh.strip() and segment["kind"] != "code" and re.search(r"<summary\b[^>]*>.*?</summary>", original, re.S):
                position = original.index("</summary>")
                output.append(original[:position] + addition(segment, zh) + original[position:])
            else:
                output.append(original)
                if zh.strip():
                    output.append(addition(segment, zh))
        target = ROOT / document["path"]
        data = "".join(output).encode("utf-8")
        if target.read_bytes() != data:
            temporary = target.with_name(target.name + ".inline-tmp")
            temporary.write_bytes(data)
            temporary.replace(target)
        rendered += 1
    print(f"Rendered {rendered} documents")


def verify():
    translations, complete_jobs = load_translations()
    failures, entries = [], []
    frontmatter_checked = 0
    try:
        import yaml
    except ImportError:
        yaml = None
    for document in read_json(WORK / "inventory.json"):
        target = ROOT / document["path"]
        actual = target.read_bytes().decode("utf-8")
        restored = actual
        missing, skipped, translated = [], [], 0
        for segment in document["segments"]:
            if not segment["translate"]:
                continue
            entry = translations.get(segment["id"])
            if entry is None:
                missing.append(segment["id"])
                continue
            zh = entry.get("zh", "")
            if not zh.strip():
                skipped.append({"id": segment["id"], "kind": segment["kind"], "reason": entry.get("skip_reason", "")})
                continue
            inserted = addition(segment, zh)
            if actual.count(inserted) != 1:
                failures.append(f"{document['path']}: translation missing or duplicated for {segment['id']}")
            restored = restored.replace(inserted, "", 1)
            translated += 1
        preserved = hashlib.sha256(restored.encode("utf-8")).hexdigest() == document["sha256"]
        if missing:
            failures.append(f"{document['path']}: {len(missing)} segments untranslated")
        if not preserved:
            failures.append(f"{document['path']}: source reconstruction hash mismatch")
        if "<!-- BEGIN CHINESE TRANSLATION -->" in actual:
            failures.append(f"{document['path']}: old appended translation remains")
        frontmatter = next((segment for segment in document["segments"] if segment["kind"] == "frontmatter"), None)
        if frontmatter and yaml:
            try:
                source_yaml = frontmatter["original"].split("---", 2)[1]
                rendered_yaml = actual.split("---", 2)[1]
                if yaml.safe_load(source_yaml) != yaml.safe_load(rendered_yaml):
                    failures.append(f"{document['path']}: frontmatter value changed")
                frontmatter_checked += 1
            except yaml.YAMLError as error:
                failures.append(f"{document['path']}: frontmatter cannot be parsed: {error}")
        entries.append({"path": document["path"], "source_preserved": preserved, "translated_blocks": translated, "skipped_blocks": skipped, "missing_blocks": len(missing)})
    for project in PROJECTS:
        record = read_json(ROOT / f"{project}.source.json")
        for path, sha in record["original_files"].items():
            if path.lower().endswith(".md"):
                continue
            actual = (ROOT / project / path).read_bytes()
            if hashlib.sha256(actual).hexdigest() != sha:
                failures.append(f"{project}/{path}: non-Markdown source changed")
    audit_path = ROOT / "translation-audit.json"
    audit_report = read_json(audit_path) if audit_path.exists() else {}
    audit_signals = len(audit_report.get("signals", []))
    if audit_signals:
        failures.append(f"Structural translation audit has {audit_signals} unresolved signals")
    report = {"verified_at_utc": datetime.now(timezone.utc).isoformat(), "format": "adjacent bilingual Markdown blocks", "passed": not failures, "document_count": len(entries), "completed_jobs": complete_jobs, "projects": dict(Counter(e["path"].split("/")[0] for e in entries)), "translated_blocks": sum(e["translated_blocks"] for e in entries), "skipped_nonlanguage_blocks": sum(len(e["skipped_blocks"]) for e in entries), "structural_audit_signals": audit_signals, "frontmatter_values_checked": frontmatter_checked, "failures": failures, "documents": entries}
    write_json(ROOT / "verification-report.json", report)
    print(json.dumps({k:v for k,v in report.items() if k != "documents"}, ensure_ascii=False, indent=2))
    return not failures


def status():
    values, done = load_translations()
    jobs = list((WORK / "jobs").glob("*.json"))
    documents = read_json(WORK / "inventory.json")
    complete = [d for d in documents if all(not s["translate"] or s["id"] in values for s in d["segments"])]
    print(json.dumps({"jobs": f"{done}/{len(jobs)}", "documents": f"{len(complete)}/{len(documents)}", "blocks": len(values), "projects_complete": dict(Counter(d["path"].split('/')[0] for d in complete))}, ensure_ascii=False))


def audit():
    """Report structural or coverage risks in saved translations."""
    try:
        from markdown_it import MarkdownIt
        parser = MarkdownIt("commonmark", {"html": True}).enable("table")
    except ImportError:
        parser = None
    values, _ = load_translations()
    signals, skipped = [], 0
    for document in read_json(WORK / "inventory.json"):
        for segment in document["segments"]:
            if not segment["translate"] or segment["id"] not in values:
                continue
            original = segment["original"]
            zh = values[segment["id"]].get("zh", "")
            if not zh.strip():
                skipped += 1
                readable = re.sub(r"`[^`]*`|https?://\S+|<[^>]*>", "", original)
                readable = re.sub(r"\]\([^)]*\)", "]", readable)
                if len(re.findall(r"\b[A-Za-z]{2,}\b", readable)) >= 3:
                    signals.append({"path": document["path"], "id": segment["id"], "kind": segment["kind"], "risk": "Natural-language prose marked as untranslatable", "text": original[:180]})
                continue
            codes = lambda value: Counter(re.findall(r"`([^`\n]+)`", value))
            for token in codes(original):
                if codes(original)[token] > codes(zh)[token]:
                    signals.append({"path": document["path"], "id": segment["id"], "kind": segment["kind"], "risk": "Inline code missing", "value": token[:100]})
            urls = lambda value: Counter(re.findall(r"\]\((?:<)?([^\s)>]+)", value))
            for url in urls(original):
                if urls(original)[url] > urls(zh)[url]:
                    signals.append({"path": document["path"], "id": segment["id"], "kind": segment["kind"], "risk": "Link target missing", "value": url})
            if parser and segment["kind"] != "frontmatter":
                choice = {"heading_open", "paragraph_open", "list_item_open", "table_open", "blockquote_open", "fence"}
                structure = lambda value: Counter(token.type for token in parser.parse(value) if token.type in choice)
                source_structure, translation_structure = structure(original), structure(zh)
                for token_type in source_structure:
                    if source_structure[token_type] != translation_structure[token_type]:
                        signals.append({"path": document["path"], "id": segment["id"], "kind": segment["kind"], "risk": "Markdown token structure differs", "value": f"{token_type}: {source_structure[token_type]} -> {translation_structure[token_type]}"})
    report = {"saved_blocks": len(values), "skipped_blocks": skipped, "structural_review_signals": len(signals), "signals": signals}
    write_json(ROOT / "translation-audit.json", report)
    print(json.dumps({k:v for k,v in report.items() if k != 'signals'}, ensure_ascii=False, indent=2))
    for signal in signals[:20]:
        print(signal)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["prepare", "render", "verify", "status", "audit"])
    command = parser.parse_args().command
    if command == "verify":
        raise SystemExit(0 if verify() else 1)
    globals()[command]()
