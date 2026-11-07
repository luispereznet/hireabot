# tinkabot

[Back to the catalog](../README.md#bots)

Wraps an HTTP API or OpenAPI/spec into a local MCP server plus Hermes skills. Proves it locally. Publishes only when you name a destination.

## What you use it for

Wraps an HTTP API or OpenAPI/spec into a local MCP server plus Hermes skills.
Names the data shape first, builds the smallest scaffold that works, proves it locally, then stops.

## Intended result

The package defines its intended work as:

- Wraps an HTTP API or OpenAPI/spec into a local MCP server plus Hermes skills.
- Names the data shape first, builds the smallest scaffold that works, proves it locally, then stops.
- Publishes only when the user explicitly names a destination; an approve gate still blocks submit.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **prove-local**: Helps when proving a wrap loads locally: validate, run MCP, record what loaded. Source: `skills/tinkabot/prove-local/SKILL.md`.
- **publish-pack**: Helps when publishing a wrap pack only after the user names a destination. Source: `skills/tinkabot/publish-pack/SKILL.md`.
- **wrap-api**: Helps when wrapping an HTTP API or OpenAPI/spec into a local MCP + Hermes skills. Source: `skills/tinkabot/wrap-api/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.

## Safety and limits

The package says to avoid the following:

- Never invent facts, numbers, or sources.
- Never publish, deploy, push, or install into a live profile without an explicit yes for that action.
- Never default a publish target or publish to any marketplace or directory on your own.
- Never ship leftover tools, stub skills, or a wrap with more than one job.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`tinkabot.tar.gz`](../packages/tinkabot.tar.gz).
- Package SHA-256: `d4b76d2331828c9c698706754dc4fa91a604863cb226a2f60b8fcea68acbc51d`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
