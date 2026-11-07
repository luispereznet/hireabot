# Home robots

[Back to the catalog](../README.md#bots)

Control home robots from chat: a Segway Navimow, a Matic vacuum, and other official vacuums, mowers, and Matter robots.

## What you use it for

Control home robots from chat: a Segway Navimow, a Matic vacuum, and other official vacuums, mowers, and Matter robots.
Connect each once, then say start, pause, dock, or how's it doing.

## Intended result

The package defines its intended work as:

- Control home robots from chat: a Segway Navimow, a Matic vacuum, and other official vacuums, mowers, and Matter robots.
- Connect each once, then say start, pause, dock, or how's it doing.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **connect-home-robot**: use this when the user wants to connect a robot vacuum. Source: `skills/home-robots/connect-home-robot/SKILL.md`.
- **connect-matic**: use this when the user needs to connect a Matic robot vacuum. Source: `skills/home-robots/connect-matic/SKILL.md`.
- **connect-navimow**: use this when the user needs to connect a Segway Navimow robot mower. Source: `skills/home-robots/connect-navimow/SKILL.md`.
- **control-home-robot**: use this when the user wants to start. Source: `skills/home-robots/control-home-robot/SKILL.md`.
- **control-matic**: use this when the user wants to start. Source: `skills/home-robots/control-matic/SKILL.md`.
- **control-navimow**: use this when the user wants to start. Source: `skills/home-robots/control-navimow/SKILL.md`.
- **share-this-bot**: use this when explaining how someone else should import this bot. Source: `skills/home-robots/share-this-bot/SKILL.md`.
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

- Never start or resume mowing without confirming the lawn is clear of people and pets. Pause, stop, and dock do not need confirmation.
- Never start Matic cleaning without confirming floors are clear of pets, cables, and small objects. Pause, stop, and dock do not need confirmation.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`home-robots.tar.gz`](../packages/home-robots.tar.gz).
- Package SHA-256: `42ae7829e2a3eaf907127d885259e659d66330e8b9db04716dd12e06695c1987`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
