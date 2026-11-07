# Love ❤️

[Back to the catalog](../README.md#bots)

Takes the admin out of being a good Partner so the attention can go where it counts.

## What you use it for

Takes the admin out of being a good Partner so the attention can go where it counts.
Reminds, researches, and queues dates, tables, and presents; you book, buy, and show up.

## Intended result

The package defines its intended work as:

- Takes the admin out of being a good Partner so the attention can go where it counts.
- Reminds, researches, and queues dates, tables, and presents; you book, buy, and show up.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **offer-monday-date-check**: Helps after setup or when asked about routines: offer monday date check. Source: `skills/love/offer-monday-date-check/SKILL.md`.
- **offer-monthly-small-gift**: Helps after setup or when asked about routines: offer monthly small gift. Source: `skills/love/offer-monthly-small-gift/SKILL.md`.
- **offer-wednesday-question**: Helps after setup or when asked about routines: offer wednesday question. Source: `skills/love/offer-wednesday-question/SKILL.md`.
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
- Separate routine-offer instructions are included: offer-monday-date-check, offer-monthly-small-gift, offer-wednesday-question. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`love.tar.gz`](../packages/love.tar.gz).
- Package SHA-256: `1871bc75c3317b31a7cde2f07cd18ca8aefdbd8bb8e3d67886a3d03b87e23fc5`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
