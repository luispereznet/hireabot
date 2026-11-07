# Competitor Watch

[Back to the catalog](../README.md#bots)

Tracks competitor pricing, product, and hiring pages and briefs you on real changes.

## What you use it for

Tracks competitor pricing, product, and hiring pages and briefs you on real changes.
I keep a short list of your competitors under watch on the public web and only flag the changes that matter to a founder, PM, marketer, or sales lead.

## Intended result

The package defines its intended work as:

- Tracks competitor pricing, product, and hiring pages and briefs you on real changes.
- I keep a short list of your competitors under watch on the public web and only flag the changes that matter to a founder, PM, marketer, or sales lead.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **build-the-watch-list**: Helps when the user names, adds or drops a competitor, or asks who is tracked. Source: `skills/competitor-watch/build-the-watch-list/SKILL.md`.
- **competitor-page-diff**: Helps for page diffs and launch checks, including first-run baselines. Source: `skills/competitor-watch/competitor-page-diff/SKILL.md`.
- **getting-started**: Use right after setup, or when memory has no user prefs. Source: `skills/competitor-watch/getting-started/SKILL.md`.
- **offer-daily-launch-check**: Helps after setup or when asked about routines: offer daily launch check. Source: `skills/competitor-watch/offer-daily-launch-check/SKILL.md`.
- **offer-weekly-competitor-brief**: Helps after setup or when asked about routines: offer weekly competitor brief. Source: `skills/competitor-watch/offer-weekly-competitor-brief/SKILL.md`.
- **pricing-and-packaging-comparison**: Helps when the user asks how their pricing compares, or after a price change. Source: `skills/competitor-watch/pricing-and-packaging-comparison/SKILL.md`.
- **weekly-competitor-brief**: Helps when the user asks for a competitor brief, or the weekly brief runs. Source: `skills/competitor-watch/weekly-competitor-brief/SKILL.md`.
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
  - Daily launch check. Package state: paused/disabled.
  - Weekly competitor brief. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-daily-launch-check, offer-weekly-competitor-brief. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I don't do general research, I never go behind a login, and I never invent a price, quote, or date.
- I show a real result within a minute, never "on it" and silence.
- I draft by default and never post, send, or publish without your yes.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`competitor-watch.tar.gz`](../packages/competitor-watch.tar.gz).
- Package SHA-256: `33aca7785959f9d7270cf1a4c4109b581dc6a92736caa40ed5682d1a6cc84f67`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
