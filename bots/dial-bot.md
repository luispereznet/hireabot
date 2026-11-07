# dial bot

[Back to the catalog](../README.md#bots)

Places outbound Bland AI phone calls when you ask, then reports what happened.

## What you use it for

Places outbound Bland AI phone calls when you ask, then reports what happened.
On first use it asks for a Bland API key and voice.

## Intended result

The package defines its intended work as:

- Places outbound Bland AI phone calls when you ask, then reports what happened.
- On first use it asks for a Bland API key and voice.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **bland-phone-calls**: Helps when placing, checking. Source: `skills/dial-bot/bland-phone-calls/SKILL.md`.
- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.

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
- Package: [`dial-bot.tar.gz`](../packages/dial-bot.tar.gz).
- Package SHA-256: `63b26e1192a9c5620dc007a5dcf4d6c7beeddd43f032dbd13ec710702f86285e`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
