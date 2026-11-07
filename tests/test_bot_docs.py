#!/usr/bin/env python3
"""Archive/document contracts; no package code or live bot is executed."""
import hashlib
import json
import re
import subprocess
import sys
import tarfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import build_bot_docs as D
import build_catalog as C

class BotDocs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bots = json.loads((ROOT/'data/catalog.json').read_text())['bots']

    def test_exact_slug_set_and_readme_links(self):
        expected = {b['slug'] for b in self.bots}
        self.assertEqual(len(expected), len(self.bots))
        self.assertEqual({p.stem for p in (ROOT/'bots').glob('*.md')}, expected)
        readme = (ROOT/'README.md').read_text()
        links = re.findall(r'\]\(bots/([a-z0-9-]+)\.md\)', readme)
        self.assertEqual(set(links), expected)
        self.assertEqual(len(links), len(expected))
        self.assertIn(C._readme_table(self.bots), readme)

    def test_inventory_against_independent_archive_listing(self):
        totals = [0, 0]
        for bot in self.bots:
            slug = bot['slug']
            with tarfile.open(ROOT/'packages'/f'{slug}.tar.gz') as archive:
                names = [m.name.split('/', 1)[1] for m in archive.getmembers() if m.isfile()]
            skills = sorted(p for p in names if p.startswith('skills/') and p.endswith('/SKILL.md'))
            scripts = sorted(p for p in names if Path(p).suffix.lower() in {'.py','.sh','.bash','.ps1','.js','.mjs','.cjs','.ts','.rb','.pl'})
            page = (ROOT/'bots'/f'{slug}.md').read_text()
            skill_block = page.split('## Included skills',1)[1].split('## Included scripts',1)[0]
            script_block = page.split('## Included scripts',1)[1].split('## Optional skill-to-script conversion',1)[0]
            self.assertEqual(sorted(re.findall(r'Source: `([^`]+)`', skill_block)), skills, slug)
            self.assertEqual(sorted(re.findall(r'Source: `([^`]+)`', script_block)), scripts, slug)
            if not skills: self.assertIn('None.', skill_block)
            if not scripts: self.assertIn('None.', script_block)
            totals[0] += len(skills); totals[1] += len(scripts)
        print(f'Inventory verified: {totals[0]} skill files, {totals[1]} script files.')

    def test_local_links_and_private_material(self):
        for p in (ROOT/'bots').glob('*.md'):
            page = p.read_text()
            for target in re.findall(r'\]\(([^)]+)\)', page):
                if not target.startswith(('https://','http://')):
                    self.assertTrue((p.parent/target.split('#')[0]).exists(), (p, target))
            self.assertFalse(re.search(r'/Users/|/home/|(?:~|\$HOME)/|\b(?:Grok|Claude|Codex|ChatGPT|OpenClaw|Cursor|Antigravity)\b|x\.ai', page, re.I), p)
            self.assertFalse(D.SECRET.search(page), p)

    def test_archive_checksum_and_grounded_conversion_disclosure(self):
        for bot in self.bots:
            data = (ROOT/'packages'/f"{bot['slug']}.tar.gz").read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), bot['sha256'])
            self.assertEqual(len(data), bot['size'])
            page = (ROOT/'bots'/f"{bot['slug']}.md").read_text()
            self.assertIn(bot['sha256'], page)
            self.assertIn(D.CONVERSION, page)
            self.assertNotIn('automatically converts', page.lower())
            with tarfile.open(ROOT/'packages'/f"{bot['slug']}.tar.gz") as archive:
                for member in archive.getmembers():
                    if member.isfile() and member.name.endswith('.md'):
                        text = archive.extractfile(member).read().decode(errors='replace')
                        self.assertFalse(re.search(r'convert (?:this|the|a) skill (?:in)?to (?:a |an )?(?:runnable )?script', text, re.I), (bot['slug'], member.name))

    def test_no_skills_or_scripts_branch(self):
        bot = {'slug':'empty','name':'Empty','description':'A minimal test fixture.'}
        page = D.render(bot, {'distribution.yaml':b'version: 1.0.0\nlicense: MIT\nhermes_requires: ">=0.22.5"\n'}, '0'*64)
        self.assertIn('None. No skill instruction files are included.', page)
        self.assertIn('None. No runnable script files are included.', page)

    def test_unknown_script_refuses_unreviewed_purpose(self):
        with self.assertRaises(ValueError):
            D.render({'slug':'test','name':'Test','description':'Test'}, {'scripts/unknown.py':b''}, '0'*64)

    def test_idempotent_and_read_only_check(self):
        paths = [ROOT/'data/catalog.json', ROOT/'README.md', *sorted((ROOT/'packages').glob('*.tar.gz')), *sorted((ROOT/'bots').glob('*.md'))]
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
        self.assertEqual(D.generate(check=True), len(self.bots))
        D.generate()
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})

    def test_bot_designer_is_new_shipped_archive(self):
        page = (ROOT/'bots/bot-designer.md').read_text()
        self.assertIn('one optional catalog invitation', page)
        self.assertIn('Submission is not automatic.', page)

if __name__ == '__main__': unittest.main(verbosity=2)
