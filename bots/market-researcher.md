# Market Researcher

[Back to the catalog](../README.md#bots)

Monitors your competitors' public websites, ads, marketing, pricing, and positioning on a standing cadence.

## What you use it for

Monitors your competitors' public websites, ads, marketing, pricing, and positioning on a standing cadence.
Collects what changed, flags moves you should know about, and suggests concrete strategy adjustments or pivots.

## Intended result

The package defines its intended work as:

- Monitors your competitors' public websites, ads, marketing, pricing, and positioning on a standing cadence.
- Collects what changed, flags moves you should know about, and suggests concrete strategy adjustments or pivots.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **market-researcher**: Helps when a task needs Market Researcher reference notes. Source: `skills/market-researcher/SKILL.md`.
- **ad-and-creative-analysis**: Use this when you need to know what a competitor is advertising. Source: `skills/market-researcher/ad-and-creative-analysis/SKILL.md`.
- **capture-and-report**: Use this when capturing anything visual or building the report that closes. Source: `skills/market-researcher/capture-and-report/SKILL.md`.
- **connect-accounts**: Use this when a platform account is needed and not yet signed in. Source: `skills/market-researcher/connect-accounts/SKILL.md`.
- **content-and-social-cadence**: Use this when you need a competitor's publishing rhythm and share of voice. Source: `skills/market-researcher/content-and-social-cadence/SKILL.md`.
- **landing-page-and-offer-watch**: Use this when you need a competitor's page. Source: `skills/market-researcher/landing-page-and-offer-watch/SKILL.md`.
- **market-researcher-setup**: Use this when the bot is first imported. Source: `skills/market-researcher/market-researcher-setup/SKILL.md`.
- **messaging-matrix**: Use this when the user asks how they compare. Source: `skills/market-researcher/messaging-matrix/SKILL.md`.
- **offer-monthly-strategy-read**: Helps after setup or when asked about routines: offer monthly strategy read. Source: `skills/market-researcher/offer-monthly-strategy-read/SKILL.md`.
- **offer-weekly-marketing-brief**: Helps after setup or when asked about routines: offer weekly marketing brief. Source: `skills/market-researcher/offer-weekly-marketing-brief/SKILL.md`.
- **search-overlap**: Use this when you need to know who shares the results with the user on their. Source: `skills/market-researcher/search-overlap/SKILL.md`.
- **strategy-read**: Use this when the monthly routine fires. Source: `skills/market-researcher/strategy-read/SKILL.md`.
- **weekly-brief**: Use this when the weekly routine fires or the user says run the brief. Per. Source: `skills/market-researcher/weekly-brief/SKILL.md`.
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
- Separate routine-offer instructions are included: offer-monthly-strategy-read, offer-weekly-marketing-brief. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never posts or contacts anyone.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`market-researcher.tar.gz`](../packages/market-researcher.tar.gz).
- Package SHA-256: `365644cb19680a85b79f481063293ba968b33c3aa93a5b1cf0f401ff02a954bf`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
