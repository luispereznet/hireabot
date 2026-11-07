# Product Support Inbox Assistant

[Back to the catalog](../README.md#bots)

Helps you find and draft answers to product questions.

## What you use it for

Helps you find and draft answers to product questions.

## Intended result

The package defines its intended work as:

- Helps you find and draft answers to product questions.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **product-support-inbox-assistant-core**: Provides a generic workflow for organizing supplied goals, source material, deliverables, unknowns, and next steps. A specialized workflow is not detailed here. Source: `skills/product-support-inbox-assistant/product-support-inbox-assistant-core/SKILL.md`.

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

- Never sends emails without you.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`product-support-inbox-assistant.tar.gz`](../packages/product-support-inbox-assistant.tar.gz).
- Package SHA-256: `6d4a7941d207900081e3d7b58885f7794d76894583e2be67af81c97f7f5db358`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
