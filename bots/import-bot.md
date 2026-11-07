# Import Bot

[Back to the catalog](../README.md#bots)

Imports other assistant workspaces and chat exports setups into Hermes expert bots.

## What you use it for

One job: import the user's setup from other assistant workspaces and chat exports, then set up expert Hermes bots that cover it, or propose additions to bots they already have.
Scrubs secrets before anything is saved. Changes nothing in the old tools, except an opt-in retention fix when asked.

## Intended result

The package defines its intended work as:

- One job: import the user's setup from other assistant workspaces and chat exports, then set up expert Hermes bots that cover it, or propose additions to bots they already have.
- Scrubs secrets before anything is saved. Changes nothing in the old tools, except an opt-in retention fix when asked.
- Portable: never greets anyone by name. Works alone; needs no connectors of its own. Experts are siblings named by role.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **adjust-experts**: Helps when renaming, merging, splitting, or adding experts. Source: `skills/import-bot/adjust-experts/SKILL.md`.
- **bot-design-standard**: Helps when checking an expert before spawn. Source: `skills/import-bot/bot-design-standard/SKILL.md`.
- **cleanup-fix**: Helps when another assistant workspace or a coding assistant retention needs care. Source: `skills/import-bot/cleanup-fix/SKILL.md`.
- **collect-accounts**: Helps when pulling other assistant account data. Source: `skills/import-bot/collect-accounts/SKILL.md`.
- **collect-local**: Helps when packing allowed files on the user's computer. Source: `skills/import-bot/collect-local/SKILL.md`.
- **connectors-encourage**: Helps when mapping connectors to Hermes integrations. Source: `skills/import-bot/connectors-encourage/SKILL.md`.
- **expert-packet**: Helps when writing the packet each expert is built from. Source: `skills/import-bot/expert-packet/SKILL.md`.
- **fallback-collect-script**: Helps when local filesystem access is unavailable. Source: `skills/import-bot/fallback-collect-script/SKILL.md`.
- **import-receipt**: Helps when finishing an import and writing the receipt. Source: `skills/import-bot/import-receipt/SKILL.md`.
- **import-scripts**: Helps when running pack, scrub, or normalize helpers. Source: `skills/import-bot/import-scripts/SKILL.md`.
- **import-setup**: Helps when starting or resuming an import. Source: `skills/import-bot/import-setup/SKILL.md`.
- **interview-fallback**: Helps when little was importable and answers must fill gaps. Source: `skills/import-bot/interview-fallback/SKILL.md`.
- **parse-import**: Helps when turning packs into scrubbed inventory notes. Source: `skills/import-bot/parse-import/SKILL.md`.
- **plan-experts**: Helps when choosing the smallest expert set. Source: `skills/import-bot/plan-experts/SKILL.md`.
- **project-folders**: Helps when placing imported project folders. Source: `skills/import-bot/project-folders/SKILL.md`.
- **resync**: Helps when bringing over only what changed later. Source: `skills/import-bot/resync/SKILL.md`.
- **routines-roster**: Helps when listing paused opt-in routines across experts. Source: `skills/import-bot/routines-roster/SKILL.md`.
- **spawn-experts**: Helps when writing audited Hermes expert profiles. Source: `skills/import-bot/spawn-experts/SKILL.md`.
- **transcript-toolkit**: Helps when normalizing transcripts into one shape. Source: `skills/import-bot/transcript-toolkit/SKILL.md`.
- **write-user-memory**: Helps when distilling old-tool facts into Hermes memory. Source: `skills/import-bot/write-user-memory/SKILL.md`.
- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **collect_linux.sh**: Creates a collection folder on Linux and prints instructions for copying and packing selected files. It warns against copying credentials. Source: `skills/import-bot/import-scripts/scripts/collect_linux.sh`.
- **collect_macos.sh**: Creates a collection folder on macOS and prints instructions for copying and packing selected files. It warns against copying credentials. Source: `skills/import-bot/import-scripts/scripts/collect_macos.sh`.
- **collect_paths.py**: Lists possible locations of assistant exports on your operating system so you can choose what to collect. Source: `skills/import-bot/import-scripts/scripts/collect_paths.py`.
- **collect_windows.ps1**: Creates a collection folder on Windows and prints instructions for copying and packing selected files. It warns against copying credentials. Source: `skills/import-bot/import-scripts/scripts/collect_windows.ps1`.
- **normalize_transcript.py**: Reformats common exported chat files into a consistent conversation format. Source: `skills/import-bot/import-scripts/scripts/normalize_transcript.py`.
- **scrub_secrets.py**: Checks a folder for common secret patterns and reports findings without printing secret values. A pattern scan is not a guarantee that all private data was found. Source: `skills/import-bot/import-scripts/scripts/scrub_secrets.py`.
- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.

## Safety and limits

The package says to avoid the following:

- Never draft the user's daily work. Not a daily assistant.
- Never change the old tools (the opt-in retention fix aside).
- Never store a key, token, or password. Never send, spend, or publish for the user.
- Never create or install a live Hermes profile without an explicit yes for that bot.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`import-bot.tar.gz`](../packages/import-bot.tar.gz).
- Package SHA-256: `e1954cfd350a2dd64aa0c1ec2435ad36e00de902d83f8e19541d88357c0d3ffb`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
