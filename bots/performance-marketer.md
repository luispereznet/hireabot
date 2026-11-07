# Performance Marketer

[Back to the catalog](../README.md#bots)

A performance marketer that turns Product Marketer ad copy into paused Maximize-clicks Google Ads Search shells for messaging tests — review sheets first, then

## What you use it for

A performance marketer that turns Product Marketer ad copy into paused Maximize-clicks Google Ads Search shells for messaging tests — review sheets first, then traffic with live screenshots, no spend until you say so.

## Intended result

The package defines its intended work as:

- A performance marketer that turns Product Marketer ad copy into paused Maximize-clicks Google Ads Search shells for messaging tests — review sheets first, then traffic with live screenshots, no spend until you say so.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **performance-marketer**: Helps when a task needs Performance Marketer reference notes. Source: `skills/performance-marketer/SKILL.md`.
- **build-shells**: Helps after the user approves the review sheet. Creates the campaign. Source: `skills/performance-marketer/build-shells/SKILL.md`.
- **connect-accounts**: Use this when a platform account is needed and not yet signed in. Source: `skills/performance-marketer/connect-accounts/SKILL.md`.
- **evidence-media**: Helps before taking a single screenshot. Source: `skills/performance-marketer/evidence-media/SKILL.md`.
- **launch-gate**: Use only when the user raises turning a campaign on. The single path. Source: `skills/performance-marketer/launch-gate/SKILL.md`.
- **messaging-test-design**: Helps when planning a test, when the user asks how long to run one. Source: `skills/performance-marketer/messaging-test-design/SKILL.md`.
- **offer-traffic-watch**: Helps after setup or when asked about routines: offer traffic watch. Source: `skills/performance-marketer/offer-traffic-watch/SKILL.md`.
- **performance-marketer-setup**: Use on first run, or when the user wants to change the product. Source: `skills/performance-marketer/performance-marketer-setup/SKILL.md`.
- **review-sheet**: Helps before anything is built. Source: `skills/performance-marketer/review-sheet/SKILL.md`.
- **traffic-watch**: Use at 24 hours and 72 hours after a campaign is enabled. Source: `skills/performance-marketer/traffic-watch/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-traffic-watch. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`performance-marketer.tar.gz`](../packages/performance-marketer.tar.gz).
- Package SHA-256: `bbda290feced4fe56e3f35c63cb4e7bec28fb3411e1e531497ca363ba1495736`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
