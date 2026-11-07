# Executive Assistant

[Back to the catalog](../README.md#bots)

EA chief-of-staff bot for exec support: conference rooms, interview prep, leadership outreach, Slack channel inventories, sheet↔calendar checks, and birthday/an

## What you use it for

Support executive-assistant work: conference rooms, interview prep, leadership outreach, Slack inventories, sheet-calendar reconciliation and birthday/anniversary loads. Do not assume the recipient is an EA, lives in Pacific time or supports a particular executive. Learn role, scope, zone and preferences through skippable setup.

## Intended result

The package defines its intended work as:

- Support executive-assistant work: conference rooms, interview prep, leadership outreach, Slack inventories, sheet-calendar reconciliation and birthday/anniversary loads. Do not assume the recipient is an EA, lives in Pacific time or supports a particular executive. Learn role, scope, zone and preferences through skippable setup.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **executive-assistant**: Helps when route executive support work. Source: `skills/executive-assistant/SKILL.md`.
- **birthday-anniversary-load**: Helps when load birthdays and anniversaries. Source: `skills/executive-assistant/birthday-anniversary-load/SKILL.md`.
- **conference-room-rundown**: Helps when build conference-room rundowns. Source: `skills/executive-assistant/conference-room-rundown/SKILL.md`.
- **executive-correspondence**: Helps when draft executive correspondence. Source: `skills/executive-assistant/executive-correspondence/SKILL.md`.
- **interview-prep**: Helps when check interview preparation. Source: `skills/executive-assistant/interview-prep/SKILL.md`.
- **leadership-outreach**: Helps when reconcile leadership outreach. Source: `skills/executive-assistant/leadership-outreach/SKILL.md`.
- **offer-exec-conference-room-rundown-2-business**: Helps after setup or when asked about routines. Source: `skills/executive-assistant/offer-exec-conference-room-rundown-2-business/SKILL.md`.
- **offer-exec-interview-prep-reminder**: Helps after setup or when asked about routines. Source: `skills/executive-assistant/offer-exec-interview-prep-reminder/SKILL.md`.
- **offer-exec-same-day-conference-room-check**: Helps after setup or when asked about routines. Source: `skills/executive-assistant/offer-exec-same-day-conference-room-check/SKILL.md`.
- **offer-weekly-leadership-outreach-check**: Helps after setup or when asked about routines. Source: `skills/executive-assistant/offer-weekly-leadership-outreach-check/SKILL.md`.
- **sheet-calendar-reconcile**: Helps when reconcile sheets and calendars. Source: `skills/executive-assistant/sheet-calendar-reconcile/SKILL.md`.
- **slack-channel-inventory**: Helps when inventory slack channels. Source: `skills/executive-assistant/slack-channel-inventory/SKILL.md`.
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
  - Exec interview-prep reminder. Package state: paused/disabled.
  - Exec conference-room rundown (2 business days ahead). Package state: paused/disabled.
  - Exec same-day conference-room check. Package state: paused/disabled.
  - Weekly leadership-outreach check. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-exec-conference-room-rundown-2-business, offer-exec-interview-prep-reminder, offer-exec-same-day-conference-room-check, offer-weekly-leadership-outreach-check. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Draft only until the user has read the exact email or Slack draft and explicitly says yes to send it. Require explicit yes before posting, buying, booking or changing shared records; read back exact changed targets. Never invent numbers, evidence, availability or access. Do not mark outreach sent from a draft or inference. Keep confidential calendar/interview data within authorized scope.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`executive-assistant.tar.gz`](../packages/executive-assistant.tar.gz).
- Package SHA-256: `36be04ff8fd03d7ec8dafb1fe79bf59f1e5b5f343c4b86395368da801108acc6`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
