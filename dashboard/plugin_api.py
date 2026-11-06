"""Hireabot desktop/dashboard backend — mounted at /api/plugins/hireabot/.

Reuses the same catalog search + install helpers as the agent tools.
"""
from __future__ import annotations

import json
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import tools as T  # noqa: E402

router = APIRouter()


def _bot_card(bot: dict, *, score: float | None = None) -> dict[str, Any]:
    card = {
        "slug": bot.get("slug"),
        "name": bot.get("name") or bot.get("slug"),
        "description": bot.get("description") or "",
        "version": bot.get("version") or "0.1.0",
        "tags": bot.get("tags") or [],
        "installed": T._installed(str(bot.get("slug") or "")),
    }
    if score is not None:
        card["score"] = score
    return card


@router.get("/health")
def health() -> dict[str, Any]:
    return {"ok": True, "plugin": "hireabot"}


@router.get("/bots")
def list_or_search_bots(
    q: str = Query("", description="Search query; empty lists the catalog"),
    limit: int = Query(40, ge=1, le=200),
) -> dict[str, Any]:
    try:
        cat, source = T.load_catalog()
        bots = T._bots(cat)
        query = (q or "").strip()
        if query:
            ranked = T.search(query, limit)
            by_slug = {b["slug"]: b for b in bots}
            results = []
            for row in ranked:
                full = by_slug.get(row["slug"]) or row
                results.append(_bot_card(full, score=row.get("score")))
        else:
            results = [_bot_card(b) for b in sorted(bots, key=lambda b: (b.get("name") or b["slug"]).lower())[:limit]]
        return {"ok": True, "source": source, "count": len(results), "bots": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"catalog failed: {e}") from e


@router.get("/bots/{slug}")
def bot_info(slug: str) -> dict[str, Any]:
    slug = slug.strip().lower()
    if not T.SLUG_RE.match(slug):
        raise HTTPException(status_code=400, detail="invalid slug")
    try:
        cat, source = T.load_catalog()
        bot = T._find(cat, slug)
        if not bot:
            raise HTTPException(status_code=404, detail=f"unknown bot '{slug}'")
        card = _bot_card(bot)
        card.update(
            {
                "source": source,
                "summary": bot.get("summary") or bot.get("description") or "",
                "use_cases": bot.get("use_cases") or [],
                "hermes_requires": bot.get("hermes_requires"),
                "license": bot.get("license"),
                "download": bot.get("download"),
                "sha256": bot.get("sha256"),
                "size": bot.get("size"),
                "next_steps": T._next_steps(slug) if card["installed"] else [
                    f"POST /api/plugins/hireabot/bots/{slug}/install",
                    *T._next_steps(slug),
                ],
            }
        )
        return {"ok": True, "bot": card}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"info failed: {e}") from e


class InstallBody(BaseModel):
    dry_run: bool = Field(False, description="If true, verify archive only; do not import a profile")


@router.post("/bots/{slug}/install")
def install_bot(slug: str, body: Optional[InstallBody] = None) -> dict[str, Any]:
    """Install a catalog bot as a Hermes profile (same path as hireabot_install)."""
    slug = slug.strip().lower()
    dry_run = bool(body.dry_run) if body else False
    if not T.SLUG_RE.match(slug):
        raise HTTPException(status_code=400, detail="invalid slug")
    try:
        cat, _ = T.load_catalog()
        bot = T._find(cat, slug)
        if not bot:
            raise HTTPException(status_code=404, detail=f"unknown bot '{slug}'")
        if T._installed(slug):
            raise HTTPException(
                status_code=409,
                detail=f"a profile named '{slug}' already exists; not overwriting it",
            )
        archive = T._archive_for(bot, cat)
        T._check_archive(archive, slug)
        cmd = f"hermes profile import {shlex.quote(str(archive))} --name {slug}"
        if dry_run:
            return {
                "ok": True,
                "dry_run": True,
                "slug": slug,
                "name": bot.get("name"),
                "archive": str(archive),
                "command": cmd,
                "note": "Archive verified. Pass dry_run=false to import.",
            }
        cleared = T._clear_profile_tombstone(slug)
        proc = subprocess.run(
            ["hermes", "profile", "import", str(archive), "--name", slug],
            capture_output=True,
            text=True,
            timeout=180,
        )
        cleared = T._clear_profile_tombstone(slug) or cleared
        out = ((proc.stdout or "") + "\n" + (proc.stderr or "")).strip()
        if proc.returncode != 0 or not T._installed(slug):
            raise HTTPException(
                status_code=500,
                detail={
                    "message": "import did not create a live profile",
                    "command": cmd,
                    "output": out[-1500:],
                    "cleared_tombstone": cleared,
                },
            )
        try:
            model_copy = T._copy_model_settings(slug)
        except Exception as e:
            return {
                "ok": False,
                "installed": slug,
                "name": bot.get("name"),
                "error": str(e),
                "next_steps": T._model_fallback_commands(slug) + T._next_steps(slug),
                "note": "Profile imported but model settings were not copied.",
            }
        return {
            "ok": True,
            "installed": slug,
            "name": bot.get("name"),
            "command": cmd,
            "model": model_copy,
            "cleared_tombstone": cleared,
            "next_steps": T._next_steps(slug),
            "output": out[-800:],
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"install failed: {e}") from e
