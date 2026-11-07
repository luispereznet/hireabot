# GTM Prospecting

[Back to the catalog](../README.md#bots)

Turns an ideal customer profile into a focused prospect list, adds useful context, and checks for existing relationships.

## What you use it for

Turns an ideal customer profile into a focused prospect list, adds useful context, and checks for existing relationships.
Drafts first-touch email and LinkedIn messages for your review.

## Intended result

The package defines its intended work as:

- Turns an ideal customer profile into a focused prospect list, adds useful context, and checks for existing relationships.
- Drafts first-touch email and LinkedIn messages for your review.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **gtm-prospecting**: Helps when a task needs GTM Prospecting reference notes. Source: `skills/gtm-prospecting/SKILL.md`.
- **agent-orchestration**: Helps when coordinate a persistent pinned specialist. Source: `skills/gtm-prospecting/agent-orchestration/SKILL.md`.
- **humanizer**: Helps when make drafts sound natural. Source: `skills/gtm-prospecting/humanizer/SKILL.md`.
- **offer-weekly-prospecting-hygiene**: Helps after setup or when asked about routines: offer weekly prospecting hygiene. Source: `skills/gtm-prospecting/offer-weekly-prospecting-hygiene/SKILL.md`.
- **prospecting-loop**: Helps when prospecting guide. Source: `skills/gtm-prospecting/prospecting-loop/SKILL.md`.
- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- Shipped routine definitions:
  - Weekly prospecting hygiene. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-weekly-prospecting-hygiene. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`gtm-prospecting.tar.gz`](../packages/gtm-prospecting.tar.gz).
- Package SHA-256: `465803b927e314acb8ef4f74e02c29a776140d131ea7fc62f4e2cfdf6a0141a2`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
