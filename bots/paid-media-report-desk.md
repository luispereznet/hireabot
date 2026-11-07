# Paid Media Report Desk

[Back to the catalog](../README.md#bots)

Turns your Google Ads, Meta, and LinkedIn exports into one weekly report with commentary.

## What you use it for

Turns your Google Ads, Meta, and LinkedIn exports into one weekly report with commentary.
When memory already holds your prefs I skip the questions and offer the two or three things useful today.

## Intended result

The package defines its intended work as:

- Turns your Google Ads, Meta, and LinkedIn exports into one weekly report with commentary.
- When memory already holds your prefs I skip the questions and offer the two or three things useful today.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **answer-a-reporting-ask**: Helps when someone asks for paid media numbers in a channel. Source: `skills/paid-media-report-desk/answer-a-reporting-ask/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/paid-media-report-desk/getting-started/SKILL.md`.
- **map-an-export**: Helps when the user hands over an ad platform export for the first time. Source: `skills/paid-media-report-desk/map-an-export/SKILL.md`.
- **monthly-paid-media-report**: Helps when the user asks for a monthly report. Source: `skills/paid-media-report-desk/monthly-paid-media-report/SKILL.md`.
- **offer-monthly-paid-media-report**: Helps after setup or when asked about routines: offer monthly paid media report. Source: `skills/paid-media-report-desk/offer-monthly-paid-media-report/SKILL.md`.
- **offer-reporting-ask-watch**: Helps after setup or when asked about routines: offer reporting ask watch. Source: `skills/paid-media-report-desk/offer-reporting-ask-watch/SKILL.md`.
- **offer-weekly-paid-media-report**: Helps after setup or when asked about routines: offer weekly paid media report. Source: `skills/paid-media-report-desk/offer-weekly-paid-media-report/SKILL.md`.
- **weekly-paid-media-report**: Helps when the user asks for a weekly report or a week-over-week read. Source: `skills/paid-media-report-desk/weekly-paid-media-report/SKILL.md`.
- **what-moved-and-why**: Helps when the user asks why a number changed. Source: `skills/paid-media-report-desk/what-moved-and-why/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-monthly-paid-media-report, offer-reporting-ask-watch, offer-weekly-paid-media-report. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Answers reporting asks in Slack with real numbers, and never posts without your yes.
- I don't buy media, change bids, or monitor accounts between reports.
- No filler.
- When my setup finishes I don't stop at "ready".
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`paid-media-report-desk.tar.gz`](../packages/paid-media-report-desk.tar.gz).
- Package SHA-256: `bc982eeb0bf6a957b7636f9d30dbe6e1a74771c9c00feb6b9fd1e3c2a89abd3c`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
