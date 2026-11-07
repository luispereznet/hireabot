# GTM Loop Closer

[Back to the catalog](../README.md#bots)

Finds promises, follow-ups, and customer details left behind in meetings, email, Slack, CRM, or task tools.

## What you use it for

Finds promises, follow-ups, and customer details left behind in meetings, email, Slack, CRM, or task tools.
Shows the evidence and prepares the reply, task, or update needed to close each loop.

## Intended result

The package defines its intended work as:

- Finds promises, follow-ups, and customer details left behind in meetings, email, Slack, CRM, or task tools.
- Shows the evidence and prepares the reply, task, or update needed to close each loop.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **gtm-loop-closer**: Helps when a task needs GTM Loop Closer reference notes. Source: `skills/gtm-loop-closer/SKILL.md`.
- **agent-orchestration**: Helps when coordinate a persistent pinned specialist. Source: `skills/gtm-loop-closer/agent-orchestration/SKILL.md`.
- **conversation-to-action**: Helps when turn a meeting, thread. Source: `skills/gtm-loop-closer/conversation-to-action/SKILL.md`.
- **follow-through-drafts**: Helps when draft the reply, task. Source: `skills/gtm-loop-closer/follow-through-drafts/SKILL.md`.
- **humanizer**: Helps when make drafts sound natural. Source: `skills/gtm-loop-closer/humanizer/SKILL.md`.
- **offer-commitment-strand-audit**: Helps after setup or when asked about routines: offer commitment-strand audit. Source: `skills/gtm-loop-closer/offer-commitment-strand-audit/SKILL.md`.
- **open-loop-audit**: Helps when find explicit commitments. Source: `skills/gtm-loop-closer/open-loop-audit/SKILL.md`.
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
  - Commitment strand audit. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-commitment-strand-audit. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`gtm-loop-closer.tar.gz`](../packages/gtm-loop-closer.tar.gz).
- Package SHA-256: `59a5b30879546e7ddb3fe1a7640cfeebe0da444f1260e31a64cb7a2ad77a6bca`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
