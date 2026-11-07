# Office Ops Desk

[Back to the catalog](../README.md#bots)

Tracks office shipments, facilities issues, and team birthdays, then writes the digests.

## What you use it for

Tracks office shipments, facilities issues, and team birthdays, then writes the digests.
I run office ops for a small company: shipments, facilities issues, new hire setups, and team celebrations.

## Intended result

The package defines its intended work as:

- Tracks office shipments, facilities issues, and team birthdays, then writes the digests.
- I run office ops for a small company: shipments, facilities issues, new hire setups, and team celebrations.
- When memory already holds your prefs I skip the questions and offer what matters today.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **build-the-office-ops-ledger**: Helps when the user first hands over shipments. Source: `skills/office-ops-desk/build-the-office-ops-ledger/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/office-ops-desk/getting-started/SKILL.md`.
- **late-shipment-follow-up**: Helps when a shipment is past its ETA. Source: `skills/office-ops-desk/late-shipment-follow-up/SKILL.md`.
- **new-hire-setup**: Helps when someone new is starting. Source: `skills/office-ops-desk/new-hire-setup/SKILL.md`.
- **offer-daily-shipment-status**: Helps after setup or when asked about routines: offer daily shipment status. Source: `skills/office-ops-desk/offer-daily-shipment-status/SKILL.md`.
- **offer-team-celebrations-reminder**: Helps after setup or when asked about routines: offer team celebrations reminder. Source: `skills/office-ops-desk/offer-team-celebrations-reminder/SKILL.md`.
- **offer-weekly-facilities-digest**: Helps after setup or when asked about routines: offer weekly facilities digest. Source: `skills/office-ops-desk/offer-weekly-facilities-digest/SKILL.md`.
- **sync-to-notion-linear-and-slack**: Helps when the user wants facilities issues filed as tickets. Source: `skills/office-ops-desk/sync-to-notion-linear-and-slack/SKILL.md`.
- **team-celebrations-list**: Helps when the user asks who has a birthday or work anniversary coming up. Source: `skills/office-ops-desk/team-celebrations-list/SKILL.md`.
- **weekly-facilities-digest**: Helps when the user asks for a facilities update or the weekly facilities digest. Source: `skills/office-ops-desk/weekly-facilities-digest/SKILL.md`.
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
- Separate routine-offer instructions are included: offer-daily-shipment-status, offer-team-celebrations-reminder, offer-weekly-facilities-digest. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Works from a pasted list or a spreadsheet, and never sends without you.
- I don't buy anything, approve spend, or triage email.
- No filler.
- When my setup finishes I don't stop at "ready".
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`office-ops-desk.tar.gz`](../packages/office-ops-desk.tar.gz).
- Package SHA-256: `1ea6f3a9b80de327d88d4d4971d0044289f1354f65c95f66b279a6b5009d3478`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
