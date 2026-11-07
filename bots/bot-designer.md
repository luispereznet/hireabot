# Bot Designer

[Back to the catalog](../README.md#bots)

Designs Hermes bots with a tight persona, real skills, and an audit before handoff.

## What you use it for

Designs Hermes bots: one job, one voice, explicit anti-jobs, no leftover tools.
Asks a few preference questions, writes a tight persona, builds the profile files, audits, then hands it over only after a clean pass.

## Intended result

The package defines its intended work as:

- Designs Hermes bots: one job, one voice, explicit anti-jobs, no leftover tools.
- Asks a few preference questions, writes a tight persona, builds the profile files, audits, then hands it over only after a clean pass.
- Coding bots get the same quality bar: one job, concise, verified. Never ship filler skills or unverified work.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **design-hermes-bot**: Interviews you, drafts and audits a one-job bot, then offers one optional catalog invitation before your final install, package, or draft choice. Submission is not automatic. Source: `skills/bot-designer/design-hermes-bot/SKILL.md`.
- **offer-routine-healthcheck**: Helps after setup or when asked about routines: offer routine check. Source: `skills/bot-designer/offer-routine-healthcheck/SKILL.md`.
- **offer-transcript-healthcheck**: Helps after setup or when asked about routines: offer transcript check. Source: `skills/bot-designer/offer-transcript-healthcheck/SKILL.md`.
- **routine-healthcheck**: Helps when auditing Hermes scheduled jobs for wasted usage. Source: `skills/bot-designer/routine-healthcheck/SKILL.md`.
- **transcript-healthcheck**: Helps when scanning Hermes chats for friction or corrections. Source: `skills/bot-designer/transcript-healthcheck/SKILL.md`.
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
- Separate routine-offer instructions are included: offer-routine-healthcheck, offer-transcript-healthcheck. An offer is not an active schedule.

## Safety and limits

The package says to avoid the following:

- Never invent facts, numbers, or sources.
- Never publish, deploy, push, or install into a live profile without an explicit yes for that action.
- Never ship leftover tools, stub skills, or a bot with more than one job.
- Never create a routine or a bot from a healthcheck report until the user picks an item.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`bot-designer.tar.gz`](../packages/bot-designer.tar.gz).
- Package SHA-256: `d98a440616191190949e4080392bb29218dadde3b220182a6ea340e170fbe8bf`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
