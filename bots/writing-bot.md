# Writing Bot

[Back to the catalog](../README.md#bots)

Drafts and revises any kind of writing so it is clearer, better structured, and right for its audience.

## What you use it for

The package gives only a brief role description. Its detailed workflow is limited; the skill inventory below shows the instructions actually included.

## Intended result

A more specific result is not documented beyond the role and the included skills. Confirm your intended output before relying on it.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **writing-revision**: Helps when draft or revise any kind of writing so it is clearer, better structured, and more effective for its audience. Source: `skills/writing-bot/writing-revision/SKILL.md`.

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

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`writing-bot.tar.gz`](../packages/writing-bot.tar.gz).
- Package SHA-256: `781a8eefe9cd56f54ea6a8ef7549e52e8c4dedb322151ab3d190d6124715a9a7`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
