# Tradbot

[Back to the catalog](../README.md#bots)

Watches your personal email and family schedule so school forms, bills, and RSVPs don't slip.

## What you use it for

Watches your personal email and family schedule so school forms, bills, and RSVPs don't slip.
Drafts the reply, catches the pickup clash, and never sends without you.

## Intended result

The package defines its intended work as:

- Watches your personal email and family schedule so school forms, bills, and RSVPs don't slip.
- Drafts the reply, catches the pickup clash, and never sends without you.
- I watch your personal email and family schedule so the household things don't slip: school forms, family plans and RSVPs, bills and renewals, appointments, and who is doing pickup.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **family-calendar-briefs**: Helps when the user asks about the week or two ahead. Source: `skills/tradbot/family-calendar-briefs/SKILL.md`.
- **getting-started**: Use right after setup, or when memory has no user prefs. Source: `skills/tradbot/getting-started/SKILL.md`.
- **kitchen-table-newspaper**: Use to make the printable one-page kitchen table newspaper. Source: `skills/tradbot/kitchen-table-newspaper/SKILL.md`.
- **monthly-parent-note**: Helps for the monthly parent note: local events plus age-matched notes. Source: `skills/tradbot/monthly-parent-note/SKILL.md`.
- **offer-afternoon-pickup-check**: Helps after setup or when asked about routines: offer afternoon pickup check. Source: `skills/tradbot/offer-afternoon-pickup-check/SKILL.md`.
- **offer-kitchen-table-newspaper**: Helps after setup or when asked about routines: offer kitchen table newspaper. Source: `skills/tradbot/offer-kitchen-table-newspaper/SKILL.md`.
- **offer-monthly-parent-note**: Helps after setup or when asked about routines: offer monthly parent note. Source: `skills/tradbot/offer-monthly-parent-note/SKILL.md`.
- **offer-weekday-family-digest**: Helps after setup or when asked about routines: offer weekday family digest. Source: `skills/tradbot/offer-weekday-family-digest/SKILL.md`.
- **offer-weekend-preview**: Helps after setup or when asked about routines: offer weekend preview. Source: `skills/tradbot/offer-weekend-preview/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- Shipped routine definitions:
  - Afternoon pickup check. Package state: paused/disabled.
  - Kitchen table newspaper. Package state: paused/disabled.
  - Monthly parent note. Package state: paused/disabled.
  - Weekday family digest. Package state: paused/disabled.
  - Weekend preview. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-afternoon-pickup-check, offer-kitchen-table-newspaper, offer-monthly-parent-note, offer-weekday-family-digest, offer-weekend-preview. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I'm not work email triage, a finance app, or a general chatbot.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`tradbot.tar.gz`](../packages/tradbot.tar.gz).
- Package SHA-256: `936a665918e3143460884a243f7de194365cc7ea0747d05b6d2a45f4082ba050`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
