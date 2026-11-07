# Pfp Bot

[Back to the catalog](../README.md#bots)

Turns a photo into a Playbook Icon that keeps hair, colors, and up to three signature features.

## What you use it for

Turns a photo of the user (X photo, upload, selfie, or a pet they own) into a stylized Playbook Icon that keeps hair, colors, and up to three signature features.
Playful and short: one line plus the image. Name what changed on a redo.

## Intended result

The package defines its intended work as:

- Turns a photo of the user (X photo, upload, selfie, or a pet they own) into a stylized Playbook Icon that keeps hair, colors, and up to three signature features.
- Playful and short: one line plus the image. Name what changed on a redo.
- The icon is a fictional character wearing someone's look, never their likeness.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **icon-finish**: Helps when the user picks Upscale, Edit, or Try again. Source: `skills/pfp-bot/icon-finish/SKILL.md`.
- **icon-guide**: Helps when a photo is too unclear to draft. Source: `skills/pfp-bot/icon-guide/SKILL.md`.
- **icon-prompt**: Helps when writing the Playbook Icon drawing prompt. Source: `skills/pfp-bot/icon-prompt/SKILL.md`.
- **icon-scripts**: Helps when running the icon helper script. Source: `skills/pfp-bot/icon-scripts/SKILL.md`.
- **icon-setup**: Helps when this is the first icon run or setup is missing. Source: `skills/pfp-bot/icon-setup/SKILL.md`.
- **icon-style**: Helps when asked how the Playbook Icon style works. Source: `skills/pfp-bot/icon-style/SKILL.md`.
- **make-icon**: Helps when making a new Playbook Icon from a photo. Source: `skills/pfp-bot/make-icon/SKILL.md`.
- **take-selfie**: Helps when the user wants a selfie for their icon. Source: `skills/pfp-bot/take-selfie/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.
- **icon.py**: Keeps icon source files, draft choices, and local settings organized, and exports images at selected sizes. Source: `skills/pfp-bot/icon-scripts/scripts/icon.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.

## Safety and limits

The package says to avoid the following:

- Never post. Never change a profile or avatar unasked.
- Never make a realistic portrait or likeness. Never copy face structure, expression, or eye shape from the photo.
- Never use photos of children, public figures, or strangers.
- Never share photos outside this bot's own folder.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`pfp-bot.tar.gz`](../packages/pfp-bot.tar.gz).
- Package SHA-256: `70c2509d5f7069e5925b802c276b90cea9b57912a1f95081719a765d5afe2f2b`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
