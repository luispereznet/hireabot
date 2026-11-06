#!/usr/bin/env python3
"""Rebuild data/catalog.json, packages/ and the bot list in README.md.

Usage:
  python3 scripts/build_catalog.py --exports <dir> [--exports <dir> ...] \
      [--source <catalog.json with extra metadata>] [--all | slug ...]

For each slug it copies <exports>/<slug>.tar.gz (first dir that has it) to packages/<slug>.tar.gz
and writes a catalog entry with a public download URL, sha256 and size. Name, description and
use cases come from the package itself; --source adds summary and tags when it has the slug.
--all publishes every <slug>.tar.gz found in the exports dirs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO_RAW = "https://raw.githubusercontent.com/luispereznet/hireabot/main"
KEEP = ("summary", "tags", "use_cases", "hermes_requires", "license")
START, END = "<!-- BOTS:START -->", "<!-- BOTS:END -->"
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def _yaml_field(lines: list[str], key: str) -> str | None:
    """Value of a top-level `key:` (plain or folded over indented lines)."""
    for i, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            parts = [line.split(":", 1)[1].strip()]
            for nxt in lines[i + 1:]:
                if not nxt.startswith("  "):
                    break
                parts.append(nxt.strip())
            text = " ".join(p for p in parts if p).strip()
            if len(text) >= 2 and text[0] == text[-1] and text[0] in "'\"":
                text = text[1:-1]
            return text or None
    return None


def _package_meta(archive: Path) -> dict:
    meta: dict = {"use_cases": []}
    with tarfile.open(archive, "r:gz") as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            rel = Path(m.name).parts[1:]
            if rel in (("distribution.yaml",), ("profile.yaml",)) or (rel and rel[-1] == "SKILL.md"):
                lines = tf.extractfile(m).read().decode("utf-8", "replace").splitlines()
                if rel == ("distribution.yaml",):
                    for k in ("description", "version", "hermes_requires", "license"):
                        v = _yaml_field(lines, k)
                        if v:
                            meta[k] = v
                elif rel == ("profile.yaml",):
                    v = _yaml_field(lines, "display_name")
                    if v:
                        meta["name"] = v
                else:
                    body = lines[1:lines.index("---", 1)] if lines[:1] == ["---"] and "---" in lines[1:] else []
                    v = _yaml_field(body, "description")
                    if v and v.lower().startswith("use "):
                        meta["use_cases"].append(v)
    return meta


def _readme_table(bots: list[dict]) -> str:
    rows = ["| Bot | Slug | Version | What it does |", "| --- | --- | --- | --- |"]
    for b in sorted(bots, key=lambda b: b["name"].lower()):
        desc = b["description"].replace("|", "\\|")
        rows.append(f"| {b['name']} | `{b['slug']}` | {b['version']} | {desc} |")
    return f"{START}\n{len(bots)} bots.\n\n" + "\n".join(rows) + f"\n{END}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--exports", required=True, type=Path, action="append")
    ap.add_argument("--source", type=Path)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("slugs", nargs="*")
    a = ap.parse_args()

    found: dict[str, Path] = {}
    for d in a.exports:
        for f in sorted(d.glob("*.tar.gz")):
            slug = f.name[: -len(".tar.gz")]
            if SLUG_RE.match(slug):
                found.setdefault(slug, f)
    slugs = sorted(found) if a.all else a.slugs
    src = {b["slug"]: b for b in json.loads(a.source.read_text())["bots"]} if a.source else {}

    pkg_dir = ROOT / "packages"
    pkg_dir.mkdir(exist_ok=True)
    bots = []
    for slug in slugs:
        dest = pkg_dir / f"{slug}.tar.gz"
        shutil.copyfile(found[slug], dest)
        pm = _package_meta(dest)
        sm = src.get(slug, {})
        entry = {
            "slug": slug,
            "name": pm.get("name") or sm.get("name") or slug,
            "description": pm.get("description") or sm.get("description", ""),
            "version": pm.get("version") or sm.get("version", "0.1.0"),
        }
        for k in KEEP:
            if sm.get(k):
                entry[k] = sm[k]
        entry.setdefault("summary", entry["description"])
        entry.setdefault("tags", [])
        if not entry.get("use_cases"):
            entry["use_cases"] = pm["use_cases"]
        entry.setdefault("hermes_requires", pm.get("hermes_requires", ">=0.22.5"))
        entry.setdefault("license", pm.get("license", "MIT"))
        data = dest.read_bytes()
        entry.update(
            status="available",
            download=f"{REPO_RAW}/packages/{slug}.tar.gz",
            sha256=hashlib.sha256(data).hexdigest(),
            size=len(data),
        )
        bots.append(entry)

    catalog = {
        "schema_version": "0.2",
        "name": "Hireabot",
        "homepage": "https://github.com/luispereznet/hireabot",
        "updated": dt.date.today().isoformat(),
        "bots": bots,
    }
    out = ROOT / "data" / "catalog.json"
    out.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START in text and END in text:
        pre, rest = text.split(START, 1)
        post = rest.split(END, 1)[1]
        readme.write_text(pre + _readme_table(bots) + post, encoding="utf-8")
    print(f"wrote data/catalog.json and README bot list: {len(bots)} bots")


if __name__ == "__main__":
    main()
