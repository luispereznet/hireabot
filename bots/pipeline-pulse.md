# Pipeline Pulse

[Back to the catalog](../README.md#bots)

Scans your full pipeline for movement, stale next steps, forecast risk, and CRM gaps.

## What you use it for

Scans your full pipeline for movement, stale next steps, forecast risk, and CRM gaps.
Shows what changed across the book and drafts the updates needed to keep the forecast honest.

## Intended result

The package defines its intended work as:

- Scans your full pipeline for movement, stale next steps, forecast risk, and CRM gaps.
- Shows what changed across the book and drafts the updates needed to keep the forecast honest.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **pipeline-pulse**: Helps when a task needs Pipeline Pulse reference notes. Source: `skills/pipeline-pulse/SKILL.md`.
- **agent-orchestration**: Helps when coordinate a persistent pinned specialist. Source: `skills/pipeline-pulse/agent-orchestration/SKILL.md`.
- **humanizer**: Helps when make drafts sound natural. Source: `skills/pipeline-pulse/humanizer/SKILL.md`.
- **offer-weekday-pipeline-pulse**: Helps after setup or when asked about routines: offer weekday pipeline pulse. Source: `skills/pipeline-pulse/offer-weekday-pipeline-pulse/SKILL.md`.
- **pipeline-pulse**: Helps when pull multi-source signals. Source: `skills/pipeline-pulse/pipeline-pulse/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-weekday-pipeline-pulse. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`pipeline-pulse.tar.gz`](../packages/pipeline-pulse.tar.gz).
- Package SHA-256: `76f8668b1cf5f5c9ad878c61fe73085e3e2fb842aab8af831fd71b0a7883a6e4`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
