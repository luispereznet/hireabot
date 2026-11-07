# Video Editor

[Back to the catalog](../README.md#bots)

Edits short vertical talking-head videos from your raw footage: picks the best takes, captions what you actually said, and adds B-roll, motion graphics, and mus

## What you use it for

Edits short vertical talking-head videos from your raw footage: picks the best takes, captions what you actually said, and adds B-roll, motion graphics, and music.

## Intended result

The package defines its intended work as:

- Edits short vertical talking-head videos from your raw footage: picks the best takes, captions what you actually said, and adds B-roll, motion graphics, and music.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **cut-and-render**: Helps after the user approves an edit plan, and for every revision. Source: `skills/video-editor/cut-and-render/SKILL.md`.
- **delivery-check**: Helps before every delivery. Source: `skills/video-editor/delivery-check/SKILL.md`.
- **edit-plan**: Helps before starting any new edit, or when a change alters the cut. Source: `skills/video-editor/edit-plan/SKILL.md`.
- **video-editor-getting-started**: Use on the first conversation after import, to resume an unfinished setup. Source: `skills/video-editor/video-editor-getting-started/SKILL.md`.
- **video-tools**: Helps before an edit to get raw footage onto my computer. Source: `skills/video-editor/video-tools/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Sends an edit plan for your yes before cutting, checks every cut for sync and glitches, and never posts.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`video-editor.tar.gz`](../packages/video-editor.tar.gz).
- Package SHA-256: `e5a12aa6d75640721d8dbb65487b0e61e3f4f47a0f6dd64504e4f951469b26fe`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
