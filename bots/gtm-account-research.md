# GTM Account Research

[Back to the catalog](../README.md#bots)

Researches one account before a meeting, deal review, or account plan.

## What you use it for

Owns: Deep sourced research and strategy for one named account: company signals, stakeholders, relationship history, competitive context, open questions, and meeting preparation.
Does not own: Bulk list creation, reusable voice training, channel execution, pipeline-wide monitoring, or prospect-database ownership.

## Intended result

The package defines its intended work as:

- Owns: Deep sourced research and strategy for one named account: company signals, stakeholders, relationship history, competitive context, open questions, and meeting preparation.
- Does not own: Bulk list creation, reusable voice training, channel execution, pipeline-wide monitoring, or prospect-database ownership.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **gtm-account-research**: Helps when a task needs GTM Account Research reference notes. Source: `skills/gtm-account-research/SKILL.md`.
- **account-research**: Helps when run adaptive single. Source: `skills/gtm-account-research/account-research/SKILL.md`.
- **account-sot-sync**: Helps when map research outputs into Notion or Sheets system-of-record fields. Source: `skills/gtm-account-research/account-sot-sync/SKILL.md`.
- **agent-orchestration**: Helps when coordinate a persistent pinned specialist. Source: `skills/gtm-account-research/agent-orchestration/SKILL.md`.
- **humanizer**: Helps when make drafts sound natural. Source: `skills/gtm-account-research/humanizer/SKILL.md`.
- **offer-weekly-account-monitor**: Helps after setup or when asked about routines: offer weekly account monitor. Source: `skills/gtm-account-research/offer-weekly-account-monitor/SKILL.md`.
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
  - Weekly account monitor. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-weekly-account-monitor. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Ask one question at a time when blocked. Never invent facts, numbers, sources, relationships or results. Disclose missing tools/connections; accept paste, CSV, export, URL or files. Require an explicit yes for the exact action before sending, posting, buying or changing external records. Keep drafts local; ordinary workflows never activate routines.
- PUBLIC AND ROUTINE SAFETY
- Never include creator names, private URLs, customer data, tokens, internal channels, or company assumptions. All routines ship disabled. Enabling requires explicit schedule, source scope, private destination, empty-result behavior, and approval boundary. Routines never send externally or silently write.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`gtm-account-research.tar.gz`](../packages/gtm-account-research.tar.gz).
- Package SHA-256: `c280e3e191141817a19c5a0bc3995bc59e90197c9aa6d15cbac982627557c276`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
