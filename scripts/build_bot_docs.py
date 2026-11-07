#!/usr/bin/env python3
"""Build reader-friendly bot pages from shipped archives, without executing them.

Run from any directory: python3 scripts/build_bot_docs.py [--check]
Catalog metadata and packages are read-only. Unknown helpers require a reviewed
purpose before generation can proceed. Source prose is filtered, never executed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import tarfile
from pathlib import Path, PurePosixPath
from build_catalog import _yaml_field, _readme_table, START, END

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_SUFFIXES = {'.py', '.sh', '.bash', '.ps1', '.js', '.mjs', '.cjs', '.ts', '.rb', '.pl'}
PURPOSES = {
 'user_setup.py': 'Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent.',
 'collect_linux.sh': 'Creates a collection folder on Linux and prints instructions for copying and packing selected files. It warns against copying credentials.',
 'collect_macos.sh': 'Creates a collection folder on macOS and prints instructions for copying and packing selected files. It warns against copying credentials.',
 'collect_windows.ps1': 'Creates a collection folder on Windows and prints instructions for copying and packing selected files. It warns against copying credentials.',
 'collect_paths.py': 'Lists possible locations of assistant exports on your operating system so you can choose what to collect.',
 'normalize_transcript.py': 'Reformats common exported chat files into a consistent conversation format.',
 'scrub_secrets.py': 'Checks a folder for common secret patterns and reports findings without printing secret values. A pattern scan is not a guarantee that all private data was found.',
 'research.py': 'Collects dated public posts about a topic from supported keyless sources and saves notes for a last-30-days research brief.',
 'icon.py': 'Keeps icon source files, draft choices, and local settings organized, and exports images at selected sizes.',
 'projects.py': 'Keeps a local project and task list, status changes, and archived records. It does not itself contact the connected project or chat services.',
 'proto.py': 'Organizes prototype briefs, build evidence, generated media records, preferences, and local state.',
 'site.py': 'Organizes website settings, exclusive articles, daily digests, newsletter send records, and dashboard notes locally.',
}
# Rewrite legacy assistant names without carrying platform or creator identities
# into public descriptions. Legitimate job services (e.g. Figma) are preserved.
REWRITES = [
 (r'Claude Cowork|Cowork', 'another assistant workspace'),
 (r'Claude Code|Codex|Cursor|Antigravity', 'a coding assistant'),
 (r'ChatGPT|Claude|OpenClaw|OpenMausBot|Grok(?: Bot)?s?|x\.ai', 'another assistant'),
]
PRIVATE = re.compile(r'/Users/|/home/|(?:~|\$HOME)/|[A-Za-z]:\\|\b(?:author|creator)\s*:', re.I)
SECRET = re.compile(r'-----BEGIN .*PRIVATE KEY|\b(?:ghp|gho|ghu|github_pat)_[A-Za-z0-9_]{20,}|\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}')
CONVERSION = 'No script-conversion option is documented in this package.'


def clean(text: str) -> str:
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    for pattern, replacement in REWRITES:
        text = re.sub(pattern, replacement, text, flags=re.I)
    text = text.replace('`', '').replace('**', '').replace('|', ',')
    text = re.sub(r'\s+', ' ', text).strip(' -\t')
    text = text.replace('another assistant workspace, a coding assistant, another assistant, and another assistant', 'other assistant workspaces and chat exports').replace('another assistant or another assistant', 'other assistant')
    if PRIVATE.search(text) or SECRET.search(text):
        return ''
    return text


def section(text: str, title: str) -> str:
    m = re.search(r'^## '+re.escape(title)+r'\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    return m.group(1).strip() if m else ''


def source_notes(text: str, maximum: int = 3) -> list[str]:
    """Keep complete source statements, excluding paths and operational commands."""
    notes = []
    for line in text.splitlines():
        line = line.strip().lstrip('- ').strip()
        if not line or line.startswith(('#', '```')) or PRIVATE.search(line):
            continue
        line = clean(line)
        if line and line not in notes:
            notes.append(line)
        if len(notes) >= maximum:
            break
    return notes


def archive_files(archive: Path, slug: str) -> dict[str, bytes]:
    files = {}
    with tarfile.open(archive, 'r:gz') as tf:
        for member in tf.getmembers():
            parts = PurePosixPath(member.name).parts
            if not parts or parts[0] != slug or '..' in parts or member.name.startswith('/'):
                raise ValueError('Unsafe archive member')
            if member.issym() or member.islnk():
                raise ValueError('Linked archive member')
            if member.isfile():
                if member.size > 2_000_000:
                    raise ValueError('Oversize documentation source')
                files['/'.join(parts[1:])] = tf.extractfile(member).read()
    return files


def inventory(files: dict[str, bytes]) -> tuple[list[str], list[str]]:
    skills = sorted(p for p in files if p.startswith('skills/') and p.endswith('/SKILL.md'))
    scripts = sorted(p for p in files if PurePosixPath(p).suffix.lower() in SCRIPT_SUFFIXES)
    return skills, scripts


def skill_purpose(path: str, data: bytes) -> str:
    if path.endswith(('-core/SKILL.md',)):
        return 'Provides a generic workflow for organizing supplied goals, source material, deliverables, unknowns, and next steps. A specialized workflow is not detailed here.'
    if '/onboarding/user-setup/' in path:
        return 'Asks skippable first-chat questions and saves your preferences for future sessions.'
    text = data.decode('utf-8', 'replace')
    if path.endswith('/design-hermes-bot/SKILL.md') and 'Optional catalog invitation and final choice' in text:
        return 'Interviews you, drafts and audits a one-job bot, then offers one optional catalog invitation before your final install, package, or draft choice. Submission is not automatic.'
    front = text.split('---', 2)[1] if text.startswith('---') else ''
    description = clean(_yaml_field(front.splitlines(), 'description') or '')
    description = re.sub(r'^Use when\s+', 'Helps when ', description, flags=re.I)
    description = re.sub(r'^Use (?:for|before|after)\s+', lambda m: 'Helps '+m.group(0)[4:], description, flags=re.I)
    if not description:
        description = 'The package does not provide a plain-language skill description; review its instructions before use.'
    return description.rstrip('.') + '.'


def render(bot: dict, files: dict[str, bytes], digest: str) -> str:
    slug = bot['slug']
    dist = files.get('distribution.yaml', b'').decode('utf-8', 'replace').splitlines()
    soul = files.get('SOUL.md', b'').decode('utf-8', 'replace')
    skills, scripts = inventory(files)
    name = clean(bot['name'])
    identity = source_notes(section(soul, 'Identity'), 3)
    useful = [n for n in identity if len(n) > 45 and n.lower() != name.lower()]
    lines = [f'# {name}', '', '[Back to the catalog](../README.md#bots)', '', clean(bot['description']), '',
             '## What you use it for', '']
    if useful:
        lines += useful[:2]
    else:
        lines += ['The package gives only a brief role description. Its detailed workflow is limited; the skill inventory below shows the instructions actually included.']
    lines += ['', '## Intended result', '']
    if useful:
        lines += ['The package defines its intended work as:', ''] + ['- '+n for n in useful]
    else:
        lines += ['A more specific result is not documented beyond the role and the included skills. Confirm your intended output before relying on it.']
    lines += ['', '## Included skills', '', 'Skills are written instructions the bot follows, not necessarily runnable programs.', '']
    lines += [f'- **{PurePosixPath(p).parent.name}**: {skill_purpose(p, files[p])} Source: `{p}`.' for p in skills] or ['None. No skill instruction files are included.']
    lines += ['', '## Included scripts', '', 'Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.', '']
    for p in scripts:
        filename = PurePosixPath(p).name
        if filename not in PURPOSES:
            raise ValueError(f'Review purpose for new script: {slug}/{p}')
        lines += [f'- **{filename}**: {PURPOSES[filename]} Source: `{p}`.']
    if not scripts:
        lines += ['None. No runnable script files are included.']
    lines += ['', '## Optional skill-to-script conversion', '', CONVERSION,
              'Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.', '',
              '## Setup and routine notes', '']
    if any('/onboarding/user-setup/' in p for p in skills):
        lines += ['- First-chat setup instructions are included. You supply your own preferences and any required account access.']
    else:
        lines += ['- No first-chat setup skill is included. Review the package instructions before configuration.']
    jobs = json.loads(files.get('cron/jobs.json', b'{"jobs": []}')).get('jobs', [])
    if jobs:
        lines += ['- Shipped routine definitions:']
        for job in jobs:
            label = clean(re.sub(r'^\[bot:[^]]+\]\s*', '', job.get('name', 'Unnamed routine')))
            state = 'paused/disabled' if job.get('enabled') is False or job.get('state') == 'paused' else 'not confirmed paused'
            lines += [f'  - {label}. Package state: {state}.']
        lines += ['- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.']
    else:
        lines += ['- No saved routine definitions are included.']
    offers = [p for p in skills if PurePosixPath(p).parent.name.startswith('offer-')]
    if offers:
        lines += ['- Separate routine-offer instructions are included: '+', '.join(PurePosixPath(p).parent.name for p in offers)+'. An offer is not an active schedule.']
    env = files.get('distribution.yaml', b'').decode('utf-8', 'replace')
    if 'env_requires:' in env:
        lines += ['- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.']
    lines += ['', '## Safety and limits', '']
    avoid = source_notes(section(soul, 'Avoid'), 4)
    lines += ['The package says to avoid the following:', ''] + ['- '+n for n in avoid] if avoid else ['- No separate safety summary is documented in the package identity file. Review the included instructions and permissions before use.']
    lines += ['- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.']
    lines += ['', '## Package facts and sources', '']
    for key, label in [('version','Version'),('hermes_requires','Minimum Hermes requirement'),('license','License')]:
        value = _yaml_field(dist, key)
        lines += [f'- {label}: {clean(value) if value else "Not stated in the package manifest"}.']
    lines += [f'- Package: [`{slug}.tar.gz`](../packages/{slug}.tar.gz).', f'- Package SHA-256: `{digest}`.',
              '- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.',
              '- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.', '']
    result = '\n'.join(lines)
    if PRIVATE.search(result) or SECRET.search(result):
        raise ValueError('Unsafe generated description')
    return result


def generate(root: Path = ROOT, check: bool = False) -> int:
    bots = json.loads((root/'data/catalog.json').read_text())['bots']
    expected = {b['slug']+'.md' for b in bots}
    if len(expected) != len(bots):
        raise ValueError('Duplicate catalog slugs')
    directory = root/'bots'
    existing = {p.name for p in directory.glob('*.md')}
    if existing - expected:
        raise ValueError('Unexpected bot pages; review/archive explicitly: '+str(sorted(existing-expected)))
    changes = []
    for bot in bots:
        slug = bot['slug']
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', slug):
            raise ValueError('Invalid slug')
        archive = root/'packages'/f'{slug}.tar.gz'
        data = archive.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest != bot['sha256'] or len(data) != bot['size']:
            raise ValueError(f'Catalog/archive mismatch: {slug}')
        page = render(bot, archive_files(archive, slug), digest)
        path = directory/f'{slug}.md'
        if not path.exists() or path.read_text() != page:
            changes.append(str(path.relative_to(root)))
            if not check:
                directory.mkdir(exist_ok=True)
                path.write_text(page)
    readme = root/'README.md'
    text = readme.read_text()
    pre, rest = text.split(START, 1)
    post = rest.split(END, 1)[1]
    updated = pre+_readme_table(bots)+post
    if updated != text:
        changes.append('README.md')
        if not check:
            readme.write_text(updated)
    if check and changes:
        raise ValueError('Stale documentation: '+', '.join(changes))
    print(f'{len(bots)} bot pages; '+('all current' if check else f'{len(changes)} files updated'))
    return len(bots)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    generate(check=parser.parse_args().check)
