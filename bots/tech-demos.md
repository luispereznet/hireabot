# Tech Demos

[Back to the catalog](../README.md#bots)

Weekday X-bookmark scout that picks one new library to demo, asks for approval, then plans and builds it in a sticky monorepo with a cloud coding agent.

## What you use it for

Weekday X-bookmark scout that picks one new library to demo, asks for approval, then plans and builds it in a sticky monorepo with a cloud coding agent.
For anyone who wants a daily public-tech playground, not a changelog digest.

## Intended result

The package defines its intended work as:

- Weekday X-bookmark scout that picks one new library to demo, asks for approval, then plans and builds it in a sticky monorepo with a cloud coding agent.
- For anyone who wants a daily public-tech playground, not a changelog digest.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **offer-daily-x-tech-scout**: Helps after setup or when asked about routines: offer daily X tech scout. Source: `skills/tech-demos/offer-daily-x-tech-scout/SKILL.md`.
- **project-planning**: Helps when starting a new project. Source: `skills/tech-demos/project-planning/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-daily-x-tech-scout. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`tech-demos.tar.gz`](../packages/tech-demos.tar.gz).
- Package SHA-256: `10ba0dd99c759b97590586ab986c37cfd0da19cfca147c0f5ce126fb586d5613`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
