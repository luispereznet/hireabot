"""Tool handlers. Every handler accepts (args, **kwargs) and returns a JSON string; none raise."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shlex
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PLUGIN = "hireabot"
BUNDLED = Path(__file__).parent / "data" / "catalog.json"
DEFAULT_CATALOG_URL = (
    "https://raw.githubusercontent.com/luispereznet/hireabot/main/data/catalog.json"
)
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
CACHE_TTL = 24 * 3600
STOP = set(
    "a an and any are as at be bot bots can do for from get have help i in is it me my need of on "
    "or please some someone something that the to want with you your agent assistant would like into".split()
)
FIELDS = (("name", 8.0), ("use_cases", 5.0), ("description", 3.0), ("tags", 1.5), ("summary", 1.0))
# Archive allowlist: a clean bot archive holds only these. Anything else is refused.
TOP_FILES = {"SOUL.md", "README.md", "config.yaml", "profile.yaml", "distribution.yaml", ".gitignore"}
FILE_DIRS = {"skills", "cron", "workspace", "plans", "skins"}
EMPTY_DIRS = {"logs", "sessions", "memories"}
MEMORY_FILES = {"MEMORY.md", "USER.md"}

_ctx = None


def bind(ctx) -> None:
    global _ctx
    _ctx = ctx


def _ok(**data) -> str:
    return json.dumps({"ok": True, **data})


def _err(msg: str, **data) -> str:
    return json.dumps({"ok": False, "error": msg, **data})


def _setting(key, default):
    try:
        val = _ctx.get_config(key, default=default) if _ctx is not None else default
        return default if val in (None, "") else val
    except Exception:
        return default


def _data_dir() -> Path:
    from plugins.plugin_storage import plugin_data_dir

    return plugin_data_dir(PLUGIN)


def _url_allowed(url: str) -> bool:
    if url.startswith("https://"):
        return True
    # Local test servers only (unit tests / dry-run). Production catalogs stay on https.
    return url.startswith("http://127.0.0.1:") or url.startswith("http://localhost:")


# ---------- catalog fetch / cache ----------

def _cache_paths() -> tuple[Path, Path]:
    root = _data_dir()
    root.mkdir(parents=True, exist_ok=True)
    return root / "catalog-cache.json", root / "catalog-cache.meta.json"


def _read_meta(meta_path: Path) -> dict:
    if not meta_path.is_file():
        return {}
    try:
        return json.loads(meta_path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _write_meta(meta_path: Path, **fields) -> None:
    cur = _read_meta(meta_path)
    cur.update(fields)
    meta_path.write_text(json.dumps(cur, indent=2) + "\n", encoding="utf-8")


def _http_get(url: str, headers: dict, max_bytes: int) -> tuple[int, dict, bytes]:
    if not _url_allowed(url):
        raise ValueError("only https:// URLs are allowed (or http://localhost for local tests)")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:  # noqa: S310 (url allowlist above)
            data = resp.read(max_bytes + 1)
            if len(data) > max_bytes:
                raise ValueError("download too large")
            return resp.status, dict(resp.headers.items()), data
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return 304, dict(e.headers.items()) if e.headers else {}, b""
        raise


def _fetch_to(url: str, dest: Path, max_bytes: int, etag: str | None = None) -> tuple[str, str | None]:
    """GET url into dest. Returns (outcome, new_etag).
    outcome: 'fresh' | 'not_modified' | raises on hard failure.
    """
    headers = {"User-Agent": f"{PLUGIN}-hermes-plugin"}
    if etag:
        headers["If-None-Match"] = etag
    status, resp_headers, data = _http_get(url, headers, max_bytes)
    new_etag = resp_headers.get("ETag") or resp_headers.get("Etag")
    if status == 304:
        return "not_modified", etag
    tmp = dest.with_suffix(dest.suffix + ".part")
    tmp.write_bytes(data)
    tmp.replace(dest)
    return "fresh", new_etag


def _load_json_file(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_catalog() -> tuple[dict, str]:
    """Load catalog. Order: override path/file:// -> remote (ETag + 24h TTL) -> cache -> bundled."""
    src = str(_setting("catalog_source", DEFAULT_CATALOG_URL)).strip() or DEFAULT_CATALOG_URL

    # Local path or file:// override (dev / offline testing)
    if src.startswith("file://"):
        p = Path(urllib.parse.urlparse(src).path)
        return _load_json_file(p), f"file:{p}"
    if not src.startswith(("https://", "http://")):
        p = Path(os.path.expanduser(src))
        return _load_json_file(p), str(p)

    cache, meta_path = _cache_paths()
    meta = _read_meta(meta_path)
    age = time.time() - float(meta.get("fetched_at", 0) or 0)
    fresh_enough = cache.is_file() and age < CACHE_TTL

    if not fresh_enough:
        try:
            outcome, new_etag = _fetch_to(
                src, cache, 5 * 1024 * 1024, etag=meta.get("etag") if cache.is_file() else None
            )
            _write_meta(
                meta_path,
                etag=new_etag or meta.get("etag"),
                fetched_at=time.time(),
                source=src,
                outcome=outcome,
            )
            return _load_json_file(cache), f"{src} ({outcome})"
        except Exception:
            if cache.is_file():
                return _load_json_file(cache), f"{src} (stale-cache)"
            return _load_json_file(BUNDLED), "bundled (offline)"
    return _load_json_file(cache), f"{src} (cache)"


def _bots(cat: dict) -> list[dict]:
    return [b for b in cat.get("bots", []) if b.get("status", "available") == "available" and not b.get("example")]


def _find(cat: dict, slug: str) -> dict | None:
    return next((b for b in _bots(cat) if b.get("slug") == slug), None)


# ---------- search ----------

def _stem(w: str) -> str:
    for suf in ("ing", "ers", "er", "es", "ed", "s"):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def _terms(text: str) -> list[str]:
    return [_stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) > 1]


def _field_text(bot: dict, field: str) -> str:
    v = bot.get(field, "")
    return " ".join(v) if isinstance(v, list) else str(v)


def score(bot: dict, q_terms: list[str], q_raw: str) -> float:
    """Weighted field overlap. Unbounded relative score so close matches stay ordered."""
    if not q_terms:
        return 0.0
    q_set = set(q_terms)
    total = 0.0
    for field, w in FIELDS:
        toks = set(_terms(_field_text(bot, field)))
        if not toks:
            continue
        hits = sum(1 for term in q_set if term in toks)
        total += w * (hits / len(q_set)) * (1.0 + hits / max(len(toks), 1))
    name = bot.get("name", "").lower()
    if name and name in q_raw.lower():
        total += 4.0
    blob = " ".join(_terms(" ".join(_field_text(bot, f) for f, _ in FIELDS)))
    q_join = " ".join(q_terms)
    if len(q_terms) >= 2 and q_join in blob:
        total += 2.5
    return round(total, 3)


# A result must cover more than half of the query's words, or score high on the
# weighted fields. Below that it is noise, and the user is offered Bot Designer.
MIN_COVERAGE = 0.5
STRONG_SCORE = 8.0


def coverage(bot: dict, q_terms: list[str]) -> float:
    q_set = set(q_terms)
    if not q_set:
        return 0.0
    toks: set[str] = set()
    for field, _w in FIELDS:
        toks |= set(_terms(_field_text(bot, field)))
    return sum(1 for t in q_set if t in toks) / len(q_set)


def search(query: str, limit: int) -> list[dict]:
    cat, _ = load_catalog()
    q_terms = _terms(query)
    ranked = sorted(((score(b, q_terms, query), b) for b in _bots(cat)), key=lambda x: -x[0])
    return [
        {"slug": b["slug"], "name": b.get("name"), "description": b.get("description"), "score": s}
        for s, b in ranked
        if s > 0 and (s >= STRONG_SCORE or coverage(b, q_terms) > MIN_COVERAGE)
    ][:limit]


# ---------- profiles / archives ----------

def _profiles_root() -> Path:
    home = Path(os.environ.get("HERMES_HOME") or Path.home() / ".hermes")
    if home.parent.name == "profiles":
        home = home.parent.parent
    return home / "profiles"


def _profile_tombstone(slug: str) -> Path:
    """Hermes marks deleted profiles under profiles/.deleted/<slug>; import does not clear it."""
    return _profiles_root() / ".deleted" / slug


def _clear_profile_tombstone(slug: str) -> bool:
    """Remove a delete-tombstone so a freshly imported profile is live for hermes -p.

    Hermes profile import recreates the folder but leaves profiles/.deleted/<slug> in place,
    so profile_exists / hermes -p still say the profile does not exist. Returns True if a
    tombstone was cleared.
    """
    marker = _profile_tombstone(slug)
    if not marker.exists():
        return False
    marker.unlink()
    return True


def _has_identity(profile_dir: Path) -> bool:
    return any(
        (profile_dir / m).is_file() or (profile_dir / m).is_symlink()
        for m in ("config.yaml", ".env", "SOUL.md", "profile.yaml", "auth.json", "state.db")
    )


def _installed(slug: str) -> bool:
    """True when the profile is live (folder + identity, not tombstoned)."""
    if slug == "default":
        return True
    d = _profiles_root() / slug
    if not d.is_dir() or not _has_identity(d):
        return False
    if _profile_tombstone(slug).exists():
        return False
    return True


def _next_steps(slug: str) -> list[str]:
    return [f"hermes -p {slug}", f"hermes -p {slug} setup"]


# Model keys needed for a fresh profile to chat (same ones the first-10 test set by hand).
MODEL_KEYS = ("model.provider", "model.base_url", "model.default", "model.api_mode")


def _terminal(cmd: str, timeout: int = 60) -> str:
    if _ctx is None:
        raise RuntimeError("plugin context unavailable")
    return str(_ctx.dispatch_tool("terminal", {"command": cmd, "timeout": timeout}))


def _config_get(profile: str, key: str) -> str | None:
    """Return the value of hermes -p <profile> config get <key>, or None if unset."""
    cmd = f"hermes -p {shlex.quote(profile)} config get {shlex.quote(key)}"
    out = _terminal(cmd)
    lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
    if not lines:
        return None
    last = lines[-1]
    if last.startswith("Config key not set") or last.startswith("Error"):
        return None
    # Ignore wrapping noise; hermes prints the bare value on the last line.
    if ":" in last and last.split(":", 1)[0].endswith("key not set"):
        return None
    return last


def _config_set(profile: str, key: str, value: str) -> None:
    cmd = (
        f"hermes -p {shlex.quote(profile)} config set "
        f"{shlex.quote(key)} {shlex.quote(value)}"
    )
    out = _terminal(cmd)
    if "✓ Set" not in out and "Set " + key not in out and f"{key} =" not in out:
        # Hermes prints "✓ Set model.provider = ..." on success; treat other text as failure.
        lower = out.lower()
        if "error" in lower or "failed" in lower or "not set" in lower:
            raise RuntimeError(f"config set failed for {key}: {out[-500:]}")


def _active_profile_slug() -> str | None:
    """Profile Hermes is running as, if HERMES_HOME points at ~/.hermes/profiles/<slug>."""
    home = Path(os.environ.get("HERMES_HOME") or Path.home() / ".hermes")
    if home.parent.name == "profiles" and home.name and home.name != "profiles":
        return home.name
    return None


def _model_fallback_commands(slug: str) -> list[str]:
    return [
        f"hermes -p {slug} config set model.provider <provider>",
        f"hermes -p {slug} config set model.base_url <url>",
        f"hermes -p {slug} config set model.default <model-name>",
        f"hermes -p {slug} config set model.api_mode <api_mode>",
    ]


def _profile_has_model(profile: str) -> bool:
    return bool(_config_get(profile, "model.provider") or _config_get(profile, "model.default"))


def _copy_model_settings(dest_slug: str) -> dict:
    """Copy model.provider / base_url / default / api_mode from the active profile (or default).

    Skips when dest already has model settings. Does not copy API keys or unrelated config.
    Raises RuntimeError with fallback commands on failure.
    """
    if _profile_has_model(dest_slug):
        return {"copied": False, "reason": "destination already has model settings", "source": None}

    active = _active_profile_slug()
    source = None
    if active and active != dest_slug and _profile_has_model(active):
        source = active
    elif _profile_has_model("default"):
        source = "default"
    if not source:
        cmds = "\n  ".join(_model_fallback_commands(dest_slug))
        raise RuntimeError(
            "no source profile has model settings to copy; set them by hand:\n  " + cmds
        )

    values: dict[str, str] = {}
    for key in MODEL_KEYS:
        val = _config_get(source, key)
        if val:
            values[key] = val
    if "model.provider" not in values and "model.default" not in values:
        cmds = "\n  ".join(_model_fallback_commands(dest_slug))
        raise RuntimeError(
            f"source profile '{source}' has no model.provider/default; set them by hand:\n  " + cmds
        )

    try:
        for key, val in values.items():
            _config_set(dest_slug, key, val)
    except Exception as e:
        cmds = "\n  ".join(_model_fallback_commands(dest_slug))
        raise RuntimeError(
            f"failed copying model settings from '{source}' to '{dest_slug}': {e}\n"
            f"Set them by hand:\n  " + cmds
        ) from e

    # Verify at least provider or default landed.
    if not _profile_has_model(dest_slug):
        cmds = "\n  ".join(_model_fallback_commands(dest_slug))
        raise RuntimeError(
            f"model copy from '{source}' did not stick on '{dest_slug}'. Set by hand:\n  " + cmds
        )
    return {"copied": True, "source": source, "keys": sorted(values.keys())}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _verify_sha(path: Path, expected: str | None) -> None:
    if not expected:
        return
    got = _sha256(path)
    if got.lower() != expected.lower():
        raise ValueError(f"sha256 mismatch for {path.name}: expected {expected}, got {got}")


def _resolve_download_url(bot: dict, cat: dict) -> str:
    dl = str(bot.get("download", ""))
    if dl.startswith(("https://", "http://")):
        return dl
    if dl.startswith("/"):
        site = str(cat.get("site", "")).rstrip("/")
        return site + dl if site else ""
    base = str(cat.get("download_base", "")).rstrip("/")
    if base and bot.get("slug"):
        return f"{base}/{bot['slug']}.tar.gz"
    return ""


def _archive_for(bot: dict, cat: dict) -> Path:
    dl = str(bot.get("download", ""))
    p = Path(os.path.expanduser(dl))
    if dl and not dl.startswith(("https://", "http://", "/")) and p.is_file():
        _verify_sha(p, bot.get("sha256"))
        return p
    if dl.startswith("/") and not dl.startswith("//"):
        # Absolute local path (local test catalogs)
        if p.is_file():
            _verify_sha(p, bot.get("sha256"))
            return p
    url = _resolve_download_url(bot, cat)
    if not url:
        # Last resort: treat download as a local path
        if p.is_file():
            _verify_sha(p, bot.get("sha256"))
            return p
        raise FileNotFoundError(f"no archive available for {bot['slug']}")
    if not _url_allowed(url) and not url.startswith("https://"):
        raise ValueError("archive URL must be https:// (or http://localhost for tests)")
    dest_dir = _data_dir() / "downloads"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{bot['slug']}-{bot.get('version', '0')}.tar.gz"
    expected = bot.get("sha256")
    if dest.is_file() and expected:
        try:
            _verify_sha(dest, expected)
            return dest
        except ValueError:
            dest.unlink(missing_ok=True)
    elif dest.is_file() and not expected:
        return dest
    _fetch_to(url, dest, 50 * 1024 * 1024)
    expected_size = bot.get("size")
    if expected_size is not None:
        got_size = dest.stat().st_size
        if got_size != int(expected_size):
            dest.unlink(missing_ok=True)
            raise ValueError(f"size mismatch for {bot['slug']}: expected {expected_size}, got {got_size}")
    try:
        _verify_sha(dest, expected)
    except ValueError:
        dest.unlink(missing_ok=True)
        raise
    return dest


def _check_archive(path: Path, slug: str) -> None:
    with tarfile.open(path, "r:gz") as tf:
        for m in tf.getmembers():
            parts = Path(m.name).parts
            if m.name.startswith("/") or ".." in parts:
                raise ValueError(f"unsafe path in archive: {m.name}")
            if m.issym() or m.islnk() or not (m.isdir() or m.isfile()):
                raise ValueError(f"unexpected entry type in archive: {m.name}")
            rel = parts[1:]
            if not rel or m.isdir():
                if rel and rel[0] not in FILE_DIRS | EMPTY_DIRS:
                    raise ValueError(f"unexpected folder in archive: {m.name}")
                continue
            if len(rel) == 1:
                ok = rel[0] in TOP_FILES or rel[0].endswith(".EXAMPLE")
            elif rel[0] == "memories":
                ok = len(rel) == 2 and rel[1] in MEMORY_FILES
            else:
                ok = rel[0] in FILE_DIRS
            if not ok:
                raise ValueError(f"archive carries an unexpected file ({m.name}); refusing")


# ---------- no match: hand off bot creation to Bot Designer ----------

def _bot_designer_prompt() -> dict:
    """Offer the designer, not a direct bot-building workflow."""
    return {
        "message": "Nothing in the catalog matches that area.",
        "offer": (
            "Would you like to install Bot Designer (hireabot_install slug=bot-designer)? "
            "Bot Designer helps you create the bot you need through its own interview and build process. "
            "Install only after the user says yes."
        ),
    }


# ---------- handlers ----------

def hireabot_search(args: dict, **kwargs) -> str:
    try:
        query = str(args.get("query", "")).strip()
        if not query:
            return _err("query is required")
        limit = int(args.get("limit") or _setting("max_results", 5))
        results = search(query, max(1, min(limit, 20)))
        for r in results:
            r["installed"] = _installed(r["slug"])
        if not results:
            return _ok(
                query=query,
                results=[],
                hint="Nothing in the catalog matches that area. Offer to install Bot Designer only with the user's yes.",
                bot_designer=_bot_designer_prompt(),
            )
        return _ok(
            query=query,
            results=results,
            hint="Use hireabot_info for details; install only if the user asks.",
        )
    except Exception as e:
        return _err(f"search failed: {e}")


def hireabot_info(args: dict, **kwargs) -> str:
    try:
        slug = str(args.get("slug", "")).strip().lower()
        cat, source = load_catalog()
        bot = _find(cat, slug)
        if not bot:
            return _err(
                f"unknown bot '{slug}'",
                hint="Try hireabot_search with what the user needs. If nothing fits, offer to install Bot Designer with the user's yes.",
                bot_designer=_bot_designer_prompt(),
            )
        info = {
            k: bot.get(k)
            for k in (
                "slug",
                "name",
                "description",
                "summary",
                "version",
                "hermes_requires",
                "license",
                "tags",
                "use_cases",
                "sha256",
                "size",
            )
        }
        page = bot.get("page")
        if page:
            info["page"] = str(cat.get("site", "")).rstrip("/") + page
        installed = _installed(slug)
        return _ok(
            bot=info,
            installed=installed,
            catalog=source,
            install_steps=(
                []
                if installed
                else [f"hireabot_install slug={slug}  (runs: hermes profile import <archive>)"]
            )
            + _next_steps(slug),
        )
    except Exception as e:
        return _err(f"info failed: {e}")


def hireabot_install(args: dict, **kwargs) -> str:
    try:
        slug = str(args.get("slug", "")).strip().lower()
        if not SLUG_RE.match(slug):
            return _err("invalid slug")
        cat, _ = load_catalog()
        bot = _find(cat, slug)
        if not bot:
            return _err(f"unknown bot '{slug}'")
        if _installed(slug):
            return _err(
                f"a profile named '{slug}' already exists; not overwriting it",
                next_steps=_next_steps(slug),
            )
        archive = _archive_for(bot, cat)
        _check_archive(archive, slug)
        cmd = f"hermes profile import {shlex.quote(str(archive))} --name {slug}"
        if _ctx is None:
            return _err("plugin context unavailable", command=cmd)
        # Import does not clear profiles/.deleted/<slug>; without this, hermes -p fails
        # after reinstalling a previously deleted bot.
        cleared_tombstone = _clear_profile_tombstone(slug)
        out = _ctx.dispatch_tool("terminal", {"command": cmd, "timeout": 180})
        # Import may recreate the tombstone race; clear again and require a live profile.
        cleared_tombstone = _clear_profile_tombstone(slug) or cleared_tombstone
        if not _installed(slug):
            return _err(
                "import did not create a live profile (folder missing, no identity, or still tombstoned)",
                command=cmd,
                output=str(out)[-1500:],
                cleared_tombstone=cleared_tombstone,
            )
        try:
            model_copy = _copy_model_settings(slug)
        except Exception as e:
            return _err(
                str(e),
                installed=slug,
                name=bot.get("name"),
                command=cmd,
                next_steps=_model_fallback_commands(slug) + _next_steps(slug),
                note=(
                    "Profile was imported but model settings were not copied. "
                    "Chat will fail until a model is set. Use the next_steps config set "
                    "commands (passing -m / --provider on chat does not help)."
                ),
            )
        note = (
            f"Model settings copied from '{model_copy['source']}' "
            f"({', '.join(model_copy['keys'])}). "
            "Optional: hermes -p "
            f"{slug} setup for extra keys. The bot starts with empty memory."
            if model_copy.get("copied")
            else (
                "Destination already had model settings; left them unchanged. "
                f"The bot starts with empty memory."
            )
        )
        return _ok(
            installed=slug,
            name=bot.get("name"),
            command=cmd,
            model=model_copy,
            cleared_tombstone=cleared_tombstone,
            next_steps=_next_steps(slug),
            note=note,
            fallback_model_commands=_model_fallback_commands(slug),
        )
    except Exception as e:
        return _err(f"install failed: {e}")


def _bot_designer_text(prompt: dict) -> str:
    return prompt["message"] + "\n" + prompt["offer"]


def slash_hireabot(raw_args: str, **kwargs) -> str:
    raw = (raw_args or "").strip()
    if not raw:
        return "Usage: /hireabot <what you need>  |  /hireabot info <slug>"
    if raw.startswith("info "):
        d = json.loads(hireabot_info({"slug": raw[5:]}))
        if not d.get("ok"):
            return d.get("error", "error") + ("\n" + _bot_designer_text(d["bot_designer"]) if d.get("bot_designer") else "")
        b = d["bot"]
        return (
            f"{b['name']} ({b['slug']}) v{b['version']}\n{b['description']}\n\n"
            "Install: ask me to install it, then:\n  " + "\n  ".join(d["install_steps"][-2:])
        )
    d = json.loads(hireabot_search({"query": raw}))
    if not d.get("ok"):
        return d.get("error", "error")
    if not d["results"]:
        return _bot_designer_text(d.get("bot_designer") or _bot_designer_prompt())
    return "\n".join(
        f"{r['score']:.2f}  {r['slug']}  {r['description']}"
        + ("  [installed]" if r["installed"] else "")
        for r in d["results"]
    )
