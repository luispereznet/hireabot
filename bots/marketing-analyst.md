# Marketing Analyst

[Back to the catalog](../README.md#bots)

Google Ads–first performance analyst: turns exports into weekly and monthly reports with commentary, answers reporting asks with real numbers, and watches spend

## What you use it for

Google Ads–first performance analyst: turns exports into weekly and monthly reports with commentary, answers reporting asks with real numbers, and watches spend against your thresholds so you catch what’s breaking before it burns budget.

## Intended result

The package defines its intended work as:

- Google Ads–first performance analyst: turns exports into weekly and monthly reports with commentary, answers reporting asks with real numbers, and watches spend against your thresholds so you catch what’s breaking before it burns budget.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **marketing-analyst**: Helps when a task needs Marketing Analyst reference notes. Source: `skills/marketing-analyst/SKILL.md`.
- **answer-a-reporting-ask**: Helps when someone asks a paid media question in chat or by email. Turns. Source: `skills/marketing-analyst/answer-a-reporting-ask/SKILL.md`.
- **connect-accounts**: Helps when a platform account is needed and not yet signed in. Source: `skills/marketing-analyst/connect-accounts/SKILL.md`.
- **evidence-media**: Helps before attaching anything visual. How charts. Source: `skills/marketing-analyst/evidence-media/SKILL.md`.
- **html-report**: Use to build the self-contained HTML report that closes every weekly. Source: `skills/marketing-analyst/html-report/SKILL.md`.
- **ingest-exports**: Helps before every report, every reporting ask, and every spend check. Source: `skills/marketing-analyst/ingest-exports/SKILL.md`.
- **marketing-analyst-setup**: Use on first run, or when the user changes platforms. Source: `skills/marketing-analyst/marketing-analyst-setup/SKILL.md`.
- **monthly-report**: Helps for the monthly routine. Source: `skills/marketing-analyst/monthly-report/SKILL.md`.
- **offer-monthly-paid-media-report**: Helps after setup or when asked about routines: offer monthly paid media report. Source: `skills/marketing-analyst/offer-monthly-paid-media-report/SKILL.md`.
- **offer-reporting-ask-watch**: Helps after setup or when asked about routines: offer reporting ask watch. Source: `skills/marketing-analyst/offer-reporting-ask-watch/SKILL.md`.
- **offer-weekly-paid-media-report**: Helps after setup or when asked about routines: offer weekly paid media report. Source: `skills/marketing-analyst/offer-weekly-paid-media-report/SKILL.md`.
- **spend-watch**: Helps when setting, changing. Source: `skills/marketing-analyst/spend-watch/SKILL.md`.
- **weekly-report**: Helps for the weekly routine. Source: `skills/marketing-analyst/weekly-report/SKILL.md`.
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
- Separate routine-offer instructions are included: offer-monthly-paid-media-report, offer-reporting-ask-watch, offer-weekly-paid-media-report. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never posts or touches a campaign without your yes.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`marketing-analyst.tar.gz`](../packages/marketing-analyst.tar.gz).
- Package SHA-256: `3a6012fea625ca2aa7d90353520c53a4d91139e67613a9c45f7345492fb47fb2`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
