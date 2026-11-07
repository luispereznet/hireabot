# Lead Pipeline Desk

[Back to the catalog](../README.md#bots)

Scores your inbound leads, merges duplicates, assigns an owner, and flags what's stuck.

## What you use it for

Scores your inbound leads, merges duplicates, assigns an owner, and flags what's stuck.
I check what is already connected before I ask, and a pasted CSV works as well as any connector.

## Intended result

The package defines its intended work as:

- Scores your inbound leads, merges duplicates, assigns an owner, and flags what's stuck.
- I check what is already connected before I ask, and a pasted CSV works as well as any connector.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **build-the-lead-ledger**: Helps when the user first hands over leads. Source: `skills/lead-pipeline-desk/build-the-lead-ledger/SKILL.md`.
- **connect-a-tool-or-change-the-source**: Helps when the user asks how to get their leads in. Source: `skills/lead-pipeline-desk/connect-a-tool-or-change-the-source/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/lead-pipeline-desk/getting-started/SKILL.md`.
- **merge-duplicate-leads**: Helps when a new export lands, when the same person shows up twice. Source: `skills/lead-pipeline-desk/merge-duplicate-leads/SKILL.md`.
- **offer-daily-lead-triage**: Helps after setup or when asked about routines: offer daily lead triage. Source: `skills/lead-pipeline-desk/offer-daily-lead-triage/SKILL.md`.
- **offer-weekly-pipeline-report**: Helps after setup or when asked about routines: offer weekly pipeline report. Source: `skills/lead-pipeline-desk/offer-weekly-pipeline-report/SKILL.md`.
- **pipeline-health-report**: Helps when the user asks how the pipeline is doing. Source: `skills/lead-pipeline-desk/pipeline-health-report/SKILL.md`.
- **route-leads-and-draft-the-first-reply**: Helps when scored leads need an owner. Source: `skills/lead-pipeline-desk/route-leads-and-draft-the-first-reply/SKILL.md`.
- **score-and-qualify-leads**: Helps when leads need a fit score and a tier, on intake. Source: `skills/lead-pipeline-desk/score-and-qualify-leads/SKILL.md`.
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
  - Daily lead triage. Package state: paused/disabled.
  - Weekly pipeline report. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-daily-lead-triage, offer-weekly-pipeline-report. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Works from a CRM export, a sheet, or a paste, and never sends anything without you.
- I don't do outbound prospecting and I'm not a CRM.
- I put a real list, report, or draft in front of you within a minute, never "on it" and silence.
- I never invent a lead, a company, a score, an email, or a source, and I say so when a row is thin.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`lead-pipeline-desk.tar.gz`](../packages/lead-pipeline-desk.tar.gz).
- Package SHA-256: `8a872cd1bc8f15c60c86699942512e6c67bbdea24264e00735dec116ac9c28dd`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
