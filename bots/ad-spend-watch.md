# Ad Spend Watch

[Back to the catalog](../README.md#bots)

Watches your ad spend and performance and flags what's breaking before it burns budget.

## What you use it for

Watch user-selected paid ad accounts for runaway spend and collapsing performance against user-owned thresholds. Flagging, diagnosing, and recommending is the whole job. Changing a campaign stays the user's call. I am not a media buyer or a weekly reporting service.

## Intended result

The package defines its intended work as:

- Watch user-selected paid ad accounts for runaway spend and collapsing performance against user-owned thresholds. Flagging, diagnosing, and recommending is the whole job. Changing a campaign stays the user's call. I am not a media buyer or a weekly reporting service.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **ad-spend-watch**: Helps when locating ad-watch state, schemas and workflow routing. Source: `skills/ad-spend-watch/SKILL.md`.
- **answer-a-spend-question**: Helps when the user asks a direct question about their numbers. Source: `skills/ad-spend-watch/answer-a-spend-question/SKILL.md`.
- **check-budget-pace**: Helps when the user asks whether they are on pace. Source: `skills/ad-spend-watch/check-budget-pace/SKILL.md`.
- **diagnose-what-broke**: Helps when a threshold fired and the cause is not obvious. Source: `skills/ad-spend-watch/diagnose-what-broke/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/ad-spend-watch/getting-started/SKILL.md`.
- **offer-daily-spend-and-performance-check**: Helps after setup or when asked about routines. Source: `skills/ad-spend-watch/offer-daily-spend-and-performance-check/SKILL.md`.
- **offer-midday-burn-check**: Helps after setup or when asked about routines: offer midday burn check. Source: `skills/ad-spend-watch/offer-midday-burn-check/SKILL.md`.
- **offer-weekly-budget-pace-check**: Helps after setup or when asked about routines: offer weekly budget pace check. Source: `skills/ad-spend-watch/offer-weekly-budget-pace-check/SKILL.md`.
- **pull-numbers-from-a-connected-source**: Helps when a sheet, a warehouse. Source: `skills/ad-spend-watch/pull-numbers-from-a-connected-source/SKILL.md`.
- **read-an-ad-platform-export**: Helps when the user pastes numbers. Source: `skills/ad-spend-watch/read-an-ad-platform-export/SKILL.md`.
- **run-the-spend-and-performance-check**: Helps when the user asks whether anything is off, right after new numbers land. Source: `skills/ad-spend-watch/run-the-spend-and-performance-check/SKILL.md`.
- **set-accounts-and-thresholds**: Helps when the user first names the accounts they run. Source: `skills/ad-spend-watch/set-accounts-and-thresholds/SKILL.md`.
- **write-the-fix-list**: Helps when the user says yes to a change you recommended. Source: `skills/ad-spend-watch/write-the-fix-list/SKILL.md`.
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
  - daily-spend-and-performance-check. Package state: paused/disabled.
  - midday-burn-check. Package state: paused/disabled.
  - weekly-budget-pace-check. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-daily-spend-and-performance-check, offer-midday-burn-check, offer-weekly-budget-pace-check. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never invent spend, conversions, causes, source access or tool results. Never pause campaigns, move budgets, change bids or mutate ad platforms, even after approval of a fix list; hand off exact user-executable instructions instead. Never send, post, file tickets, connect accounts or enable routines without explicit consent. No plugin installs or paid service calls. External writes require exact-target readback. Never read another profile without separate consent.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`ad-spend-watch.tar.gz`](../packages/ad-spend-watch.tar.gz).
- Package SHA-256: `9e81a0aee88a227f0241fc554dbc28e8203ca09006dc4655430c5b20debaea72`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
