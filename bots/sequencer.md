# Sequencer

[Back to the catalog](../README.md#bots)

Runs your outbound sequencer as a staff function.

## What you use it for

Runs your outbound sequencer as a staff function.
Connects your tools, learns voice and ICP from Gmail and CRM, keeps sequence state on a sheet, and stages drafts you send.

## Intended result

The package defines its intended work as:

- Runs your outbound sequencer as a staff function.
- Connects your tools, learns voice and ICP from Gmail and CRM, keeps sequence state on a sheet, and stages drafts you send.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **sequencer**: Helps when a task needs Sequencer reference notes. Source: `skills/sequencer/SKILL.md`.
- **auto-discovery**: Use this when a connector lands or a fallback is accepted. Source: `skills/sequencer/auto-discovery/SKILL.md`.
- **connect-accounts**: Use this when a platform account is needed and not yet signed in. Source: `skills/sequencer/connect-accounts/SKILL.md`.
- **crm-adapter**: Use this before reading or writing any CRM. Source: `skills/sequencer/crm-adapter/SKILL.md`.
- **getting-started**: Use this on the first turn after import. Source: `skills/sequencer/getting-started/SKILL.md`.
- **humanizer**: Use this as the final pass on every outbound draft. Source: `skills/sequencer/humanizer/SKILL.md`.
- **offer-crm-sequence-guard**: Helps after setup or when asked about routines: offer CRM sequence guard. Source: `skills/sequencer/offer-crm-sequence-guard/SKILL.md`.
- **offer-daily-prospects**: Helps after setup or when asked about routines: offer daily prospects. Source: `skills/sequencer/offer-daily-prospects/SKILL.md`.
- **offer-inbox-triage**: Helps after setup or when asked about routines: offer inbox triage. Source: `skills/sequencer/offer-inbox-triage/SKILL.md`.
- **offer-sequencer-daily**: Helps after setup or when asked about routines: offer sequencer daily. Source: `skills/sequencer/offer-sequencer-daily/SKILL.md`.
- **outbound-voice**: Use this to learn the user's outbound voice from their own sent mail. Source: `skills/sequencer/outbound-voice/SKILL.md`.
- **prospect-queue**: Use this to turn the confirmed ICP into new rows on the tracker. Source: `skills/sequencer/prospect-queue/SKILL.md`.
- **sequencer-core**: Provides a generic workflow for organizing supplied goals, source material, deliverables, unknowns, and next steps. A specialized workflow is not detailed here. Source: `skills/sequencer/sequencer-core/SKILL.md`.
- **sheet-brain**: Use this when creating or mapping the tracker, when writing state back. Source: `skills/sequencer/sheet-brain/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-crm-sequence-guard, offer-daily-prospects, offer-inbox-triage, offer-sequencer-daily. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`sequencer.tar.gz`](../packages/sequencer.tar.gz).
- Package SHA-256: `5d4fa54f239411d77043fdde60b9f081b5e6c25ce12a83ad14dfd42df5550df7`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
