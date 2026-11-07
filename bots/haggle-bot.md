# Haggle Bot

[Back to the catalog](../README.md#bots)

Inventories your SaaS spend from Ramp and bills, finds evidence-backed savings (unused seats, duplicates, cheaper alternatives), and drafts vendor counters for

## What you use it for

SaaS procurement savings specialist: competitive quotes first; unused seats, duplicates and zombie SaaS second. Not an ERP administrator or general finance assistant.

## Intended result

The package defines its intended work as:

- SaaS procurement savings specialist: competitive quotes first; unused seats, duplicates and zombie SaaS second. Not an ERP administrator or general finance assistant.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **haggle-bot**: Helps when a task needs Haggle Bot reference notes. Source: `skills/haggle-bot/SKILL.md`.
- **build-spend-inventory**: Helps when pull live spend from Ramp or an export. Source: `skills/haggle-bot/build-spend-inventory/SKILL.md`.
- **draft-vendor-counter**: Helps when draft the renegotiation email or Slack note to a vendor. Source: `skills/haggle-bot/draft-vendor-counter/SKILL.md`.
- **google-sheets-final-check**: Helps when mandatory live re-read QA after any Google Sheets write. Source: `skills/haggle-bot/google-sheets-final-check/SKILL.md`.
- **haggle-setup**: Helps when first-run interview. Source: `skills/haggle-bot/haggle-setup/SKILL.md`.
- **offer-monthly-inventory-refresh**: Helps after setup or when asked about routines: offer monthly inventory refresh. Source: `skills/haggle-bot/offer-monthly-inventory-refresh/SKILL.md`.
- **offer-renewal-window-watch**: Helps after setup or when asked about routines: offer renewal window watch. Source: `skills/haggle-bot/offer-renewal-window-watch/SKILL.md`.
- **research-alternatives**: Helps when find 3+ named alternatives tied to real usage with cited. Source: `skills/haggle-bot/research-alternatives/SKILL.md`.
- **score-savings-opportunity**: Helps when apply the opportunity bar to one vendor. Source: `skills/haggle-bot/score-savings-opportunity/SKILL.md`.
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
  - Monthly inventory refresh. Package state: paused/disabled.
  - Renewal window watch. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-monthly-inventory-refresh, offer-renewal-window-watch. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- No purchases, signatures, POs or financial commitments. Require explicit yes before each send/post/forward, including internal messages and another agent; drafts alone are not permission. Missing tools or stale/partial data must be disclosed. No other-profile reads without consent.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`haggle-bot.tar.gz`](../packages/haggle-bot.tar.gz).
- Package SHA-256: `9acf859fe29a410bdf6db73845d62e86973bd74c7ef7627fe9ffa082c9f3bb7f`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
