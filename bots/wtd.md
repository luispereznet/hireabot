# WTD

[Back to the catalog](../README.md#bots)

WTD is a VIP hospitality planning partner for marketing ops — project-plan and status rhythm across tentpoles and ticket banks, nomination-sheet tracking, marke

## What you use it for

WTD is a VIP hospitality planning partner for marketing ops — project-plan and status rhythm across tentpoles and ticket banks, nomination-sheet tracking, marketing-visible status hubs, and decks or agendas.
Sales owns guest inviting; this bot keeps the plan and status clean without dumping private notes onto shared pages.

## Intended result

The package defines its intended work as:

- WTD is a VIP hospitality planning partner for marketing ops — project-plan and status rhythm across tentpoles and ticket banks, nomination-sheet tracking, marketing-visible status hubs, and decks or agendas.
- Sales owns guest inviting; this bot keeps the plan and status clean without dumping private notes onto shared pages.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **comms-source-of-truth**: Helps when before adding facts to a deck or project. Source: `skills/wtd/comms-source-of-truth/SKILL.md`.
- **deck-qa-standards**: Helps when standing QA checklist for every Google Slides deck this bot builds. Source: `skills/wtd/deck-qa-standards/SKILL.md`.
- **email-reply-standards**: Helps when standing rules for every draft or send of email on the owner's behalf. Source: `skills/wtd/email-reply-standards/SKILL.md`.
- **gtm-branded-deck**: Helps when always start a new slides deliverable by copying the team's current. Source: `skills/wtd/gtm-branded-deck/SKILL.md`.
- **offer-vip-plan-status-refresh**: Helps after setup or when asked about routines: offer VIP Plan status refresh. Source: `skills/wtd/offer-vip-plan-status-refresh/SKILL.md`.
- **outstanding-asks-review**: Helps when scan Slack, Gmail. Source: `skills/wtd/outstanding-asks-review/SKILL.md`.
- **vip-ae-nomination-sheet**: Helps when building or updating a VIP event sales-nomination Google Sheet. Source: `skills/wtd/vip-ae-nomination-sheet/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-vip-plan-status-refresh. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never send external Slack or email without the owner's explicit OK.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`wtd.tar.gz`](../packages/wtd.tar.gz).
- Package SHA-256: `fb840944b8b92a692dfc7f0cc97d96face77c10684493ff8f34c84b08624e12e`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
