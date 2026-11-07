# Overheard

[Back to the catalog](../README.md#bots)

Watches Reddit, Hacker News, news sites, and X for third-party mentions of your name, brand, and URLs, then sends a short weekday digest when something clears t

## What you use it for

Watches Reddit, Hacker News, news sites, and X for third-party mentions of your name, brand, and URLs, then sends a short weekday digest when something clears the bar.

## Intended result

The package defines its intended work as:

- Watches Reddit, Hacker News, news sites, and X for third-party mentions of your name, brand, and URLs, then sends a short weekday digest when something clears the bar.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **offer-daily-mention-monitor**: Helps after setup or when asked about routines: offer daily mention monitor. Source: `skills/overheard/offer-daily-mention-monitor/SKILL.md`.
- **overheard-setup**: Helps when first-run watch-list interview. Also use when the user. Source: `skills/overheard/overheard-setup/SKILL.md`.
- **overheard**: Helps when core instructions on every turn. Source: `skills/overheard/overheard/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-daily-mention-monitor. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Stays quiet on dead days and never posts on your behalf.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`overheard.tar.gz`](../packages/overheard.tar.gz).
- Package SHA-256: `c1a3f903870dd463853aeabf8ac8c85d8a87027d3c98a74d0f5c444470f30a30`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
