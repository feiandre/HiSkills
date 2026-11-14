"""Download pinned upstream snapshots without running upstream code."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import urllib.request
import zipfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]

def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "SkillLearning-source-downloader", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("repo")
    parser.add_argument("--subdir", default="")
    args = parser.parse_args()
    destination = ROOT / args.name
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing destination: {destination}")
    metadata = json.loads(fetch(f"https://api.github.com/repos/{args.repo}"))
    branch = metadata["default_branch"]
    commit = json.loads(fetch(f"https://api.github.com/repos/{args.repo}/commits/{branch}"))["sha"]
    archive_url = f"https://codeload.github.com/{args.repo}/zip/{commit}"
    archive = fetch(archive_url)
    archive_dir = ROOT / ".downloads"
    archive_dir.mkdir(exist_ok=True)
    archive_path = archive_dir / f"{args.name}-{commit}.zip"
    archive_path.write_bytes(archive)
    originals = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        archive_root = bundle.namelist()[0].split("/")[0] + "/"
        prefix = archive_root + (args.subdir.strip("/") + "/" if args.subdir else "")
        for member in bundle.infolist():
            if member.is_dir() or not member.filename.startswith(prefix):
                continue
            relative = PurePosixPath(member.filename[len(prefix):])
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError(f"Unsafe archive path: {relative}")
            data = bundle.read(member)
            target = destination.joinpath(*relative.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            originals[str(relative)] = hashlib.sha256(data).hexdigest()
    license_name = metadata.get("license", {}).get("spdx_id") if metadata.get("license") else None
    snapshot_license_file = destination / "LICENSE"
    snapshot_license = None
    if snapshot_license_file.is_file():
        if snapshot_license_file.read_text(encoding="utf-8").lstrip().startswith("MIT License"):
            snapshot_license = "MIT"
    record = {
        "name": args.name, "repository": args.repo,
        "source_url": f"https://github.com/{args.repo}" + (f"/tree/{commit}/{args.subdir}" if args.subdir else ""),
        "default_branch": branch, "commit": commit, "subdirectory": args.subdir,
        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
        "archive_url": archive_url,
        "archive_path": archive_path.relative_to(ROOT).as_posix(),
        "archive_sha256": hashlib.sha256(archive).hexdigest(),
        "repository_license": license_name,
        "snapshot_license": snapshot_license,
        "snapshot_license_file": "LICENSE" if snapshot_license_file.is_file() else None,
        "original_files": originals,
    }
    (ROOT / f"{args.name}.source.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    skills = list(destination.rglob("SKILL.md"))
    print(json.dumps({"name": args.name, "commit": commit, "files": len(originals), "skills": len(skills), "skill_bytes": sum(p.stat().st_size for p in skills), "license": license_name}, ensure_ascii=False))

if __name__ == "__main__":
    main()
