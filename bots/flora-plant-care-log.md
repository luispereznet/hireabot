# Flora: Plant Care Log

[Back to the catalog](../README.md#bots)

Flora keeps a private houseplant care log and weekly reminders.

## What you use it for

Flora keeps a private houseplant care log and weekly reminders.

## Intended result

The package defines its intended work as:

- Flora keeps a private houseplant care log and weekly reminders.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **houseplant-care-card**: use this when making a generalized species care card after the owner named. Source: `skills/flora-plant-care-log/houseplant-care-card/SKILL.md`.
- **houseplant-care-first-run**: use this on the first chat after someone adds the houseplant care Bot. Source: `skills/flora-plant-care-log/houseplant-care-first-run/SKILL.md`.
- **houseplant-weekly-collection-news**: use this during the weekly houseplant check to look up a few cheap news items. Source: `skills/flora-plant-care-log/houseplant-weekly-collection-news/SKILL.md`.
- **private-houseplant-journal**: use this when creating or updating the private houseplant journal on. Source: `skills/flora-plant-care-log/private-houseplant-journal/SKILL.md`.
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

- She builds a plant journal on her computer that you can page through, and your plants do not copy if someone else installs her.
- Do not call yourself a plant care expert.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`flora-plant-care-log.tar.gz`](../packages/flora-plant-care-log.tar.gz).
- Package SHA-256: `00cd5474b94a07a6739851cfda9ff8388fb998d95d2183c6b43a02f5a19b6721`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
