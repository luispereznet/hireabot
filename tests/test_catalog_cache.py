#!/usr/bin/env python3
"""Unit tests for catalog fetch / ETag cache / offline fallback / sha256 check.

Runs a local http.server; does not touch Luis's real Hermes profiles.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tarfile
import tempfile
import threading
import time
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))  # load tools.py by path
sys.path.insert(0, str(ROOT))

import tools as T  # noqa: E402


class ETagHandler(SimpleHTTPRequestHandler):
    """Serves files; adds ETag; honours If-None-Match with 304."""

    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

    def log_message(self, fmt, *args):  # quiet
        pass

    def end_headers(self):
        # SimpleHTTPRequestHandler already chose the file; stamp an ETag from path.
        path = Path(self.translate_path(self.path))
        if path.is_file():
            etag = '"' + hashlib.sha256(path.read_bytes()).hexdigest()[:16] + '"'
            self.send_header("ETag", etag)
        super().end_headers()

    def do_GET(self):
        path = Path(self.translate_path(self.path))
        if path.is_file():
            etag = '"' + hashlib.sha256(path.read_bytes()).hexdigest()[:16] + '"'
            inm = self.headers.get("If-None-Match")
            if inm and inm == etag:
                self.send_response(304)
                self.send_header("ETag", etag)
                self.end_headers()
                return
        return super().do_GET()


def _start_server(directory: Path) -> tuple[ThreadingHTTPServer, str]:
    handler = partial(ETagHandler, directory=str(directory))
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd, f"http://127.0.0.1:{port}"


def _mini_tar(path: Path, slug: str = "demo-bot") -> None:
    with tarfile.open(path, "w:gz") as tf:
        info = tarfile.TarInfo(name=f"{slug}/README.md")
        data = b"# demo\n"
        info.size = len(data)
        import io

        tf.addfile(info, io.BytesIO(data))
        for name in ("SOUL.md", "config.yaml", "profile.yaml", "distribution.yaml"):
            info = tarfile.TarInfo(name=f"{slug}/{name}")
            body = b"x: 1\n" if name.endswith(".yaml") else b"# soul\n"
            info.size = len(body)
            tf.addfile(info, io.BytesIO(body))


class CatalogCacheTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="hireabot-cache-"))
        self.www = self.tmp / "www"
        self.www.mkdir()
        self.data_dir = self.tmp / "plugin-data"
        self.data_dir.mkdir()
        # Point plugin data + bundled catalog at the temp tree
        self.bundled = self.tmp / "bundled-catalog.json"
        self.bundled.write_text(
            json.dumps(
                {
                    "schema_version": "0.2",
                                        "bots": [
                        {
                            "slug": "bundled-only",
                            "name": "Bundled Only",
                            "description": "offline fallback bot",
                            "status": "available",
                            "version": "1.0.0",
                            "download": str(self.tmp / "missing.tar.gz"),
                        }
                    ],
                }
            )
            + "\n"
        )
        T.BUNDLED = self.bundled
        T._ctx = None
        T.CACHE_TTL = 24 * 3600

        def fake_data_dir():
            return self.data_dir

        T._data_dir = fake_data_dir  # type: ignore

        # Live catalog on the HTTP server
        self.tar = self.www / "demo-bot.tar.gz"
        _mini_tar(self.tar)
        digest = hashlib.sha256(self.tar.read_bytes()).hexdigest()
        self.catalog = {
            "schema_version": "0.2",
                        "download_base": "WILL_SET",
            "bots": [
                {
                    "slug": "demo-bot",
                    "name": "Demo Bot",
                    "description": "coaches sales calls for tests",
                    "status": "available",
                    "version": "1.0.0",
                    "download": "WILL_SET",
                    "sha256": digest,
                    "size": self.tar.stat().st_size,
                    "tags": ["sales", "coach"],
                    "use_cases": ["coach my sales calls"],
                }
            ],
        }
        self.httpd, self.base = _start_server(self.www)
        self.catalog["download_base"] = self.base
        self.catalog["bots"][0]["download"] = f"{self.base}/demo-bot.tar.gz"
        (self.www / "catalog.json").write_text(json.dumps(self.catalog) + "\n")

        # Override setting via monkeypatch of _setting
        self.catalog_url = f"{self.base}/catalog.json"
        real_setting = T._setting

        def setting(key, default):
            if key == "catalog_source":
                return self.catalog_url
            return real_setting(key, default)

        T._setting = setting  # type: ignore

    def tearDown(self):
        try:
            self.httpd.shutdown()
        except Exception:
            pass
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_fetch_and_cache(self):
        cat, src = T.load_catalog()
        self.assertEqual(cat["bots"][0]["slug"], "demo-bot")
        self.assertIn("fresh", src)
        cache = self.data_dir / "catalog-cache.json"
        self.assertTrue(cache.is_file())
        meta = json.loads((self.data_dir / "catalog-cache.meta.json").read_text())
        self.assertTrue(meta.get("etag"))

        # Within TTL: no re-fetch needed
        cat2, src2 = T.load_catalog()
        self.assertEqual(cat2["bots"][0]["slug"], "demo-bot")
        self.assertIn("cache", src2)

    def test_etag_not_modified(self):
        T.load_catalog()
        # Expire TTL so the next call revalidates with If-None-Match
        meta_path = self.data_dir / "catalog-cache.meta.json"
        meta = json.loads(meta_path.read_text())
        meta["fetched_at"] = time.time() - (T.CACHE_TTL + 10)
        meta_path.write_text(json.dumps(meta))
        cat, src = T.load_catalog()
        self.assertEqual(cat["bots"][0]["slug"], "demo-bot")
        self.assertIn("not_modified", src)

    def test_offline_falls_back_to_cache_then_bundled(self):
        T.load_catalog()  # seed cache
        self.httpd.shutdown()
        # Expire TTL so it tries the network
        meta_path = self.data_dir / "catalog-cache.meta.json"
        meta = json.loads(meta_path.read_text())
        meta["fetched_at"] = 0
        meta_path.write_text(json.dumps(meta))
        cat, src = T.load_catalog()
        self.assertEqual(cat["bots"][0]["slug"], "demo-bot")
        self.assertIn("stale-cache", src)

        # Remove cache -> bundled
        (self.data_dir / "catalog-cache.json").unlink()
        cat2, src2 = T.load_catalog()
        self.assertEqual(cat2["bots"][0]["slug"], "bundled-only")
        self.assertIn("bundled", src2)

    def test_sha_mismatch_rejected(self):
        # Restart server was shut down in previous test? Each test gets setUp.
        bot = self.catalog["bots"][0]
        bot = dict(bot)
        bot["sha256"] = "0" * 64
        with self.assertRaises(ValueError) as cm:
            T._archive_for(bot, self.catalog)
        self.assertIn("sha256 mismatch", str(cm.exception))

    def test_local_path_override(self):
        local = self.tmp / "local-catalog.json"
        local.write_text(json.dumps(self.catalog) + "\n")

        def setting(key, default):
            if key == "catalog_source":
                return str(local)
            return default

        T._setting = setting  # type: ignore
        cat, src = T.load_catalog()
        self.assertEqual(cat["bots"][0]["slug"], "demo-bot")
        self.assertEqual(src, str(local))

    def test_search_hits_demo(self):
        results = T.search("coach my sales calls", 5)
        self.assertTrue(results)
        self.assertEqual(results[0]["slug"], "demo-bot")


    def assert_designer_handoff(self, text):
        self.assertIn("Nothing in the catalog matches that area.", text)
        self.assertIn("hireabot_install slug=bot-designer", text)
        self.assertIn("interview and build process", text)
        self.assertIn("yes", text)
        for forbidden in ("create_a_bot", "hermes profile create", "SOUL.md", "hermes -p", "Describe the job"):
            self.assertNotIn(forbidden, text)

    def test_no_match_hands_off_to_designer(self):
        d = json.loads(T.hireabot_search({"query": "zzqx unicorn grooming"}))
        self.assertTrue(d["ok"])
        self.assertEqual(d["results"], [])
        self.assert_designer_handoff(json.dumps(d))

    def test_unknown_slug_hands_off_to_designer(self):
        d = json.loads(T.hireabot_info({"slug": "no-such-bot"}))
        self.assertFalse(d["ok"])
        self.assert_designer_handoff(json.dumps(d))

    def test_slash_no_match_text(self):
        self.assert_designer_handoff(T.slash_hireabot("zzqx unicorn grooming"))
        self.assert_designer_handoff(T.slash_hireabot("info no-such-bot"))

    def test_matching_handler_preserves_search_results(self):
        query = "coach my sales calls"
        expected = T.search(query, 5)
        self.assertTrue(expected)
        d = json.loads(T.hireabot_search({"query": query}))
        self.assertTrue(d["ok"])
        self.assertNotIn("bot_designer", d)
        self.assertEqual([{k: v for k, v in r.items() if k != "installed"} for r in d["results"]], expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
