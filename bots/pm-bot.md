# PM bot

[Back to the catalog](../README.md#bots)

Acts as your PM.

## What you use it for

Writes the dated cut: what's in, what's out, and how you'll know it's done.
Engineering doesn't start until you approve it.

## Intended result

The package defines its intended work as:

- Writes the dated cut: what's in, what's out, and how you'll know it's done.
- Engineering doesn't start until you approve it.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **adhd-friendly-agent-responses**: Helps for every chat reply to the owner unless they say stop adhd mode or normal. Source: `skills/pm-bot/adhd-friendly-agent-responses/SKILL.md`.
- **enterprise-binding-prd-cut**: Helps when a PM bot must turn a vague product ask into a binding. Source: `skills/pm-bot/enterprise-binding-prd-cut/SKILL.md`.
- **getting-started-binding-prd-pm**: Use this when a newly imported standalone Binding PRD cuts bot runs its first. Source: `skills/pm-bot/getting-started-binding-prd-pm/SKILL.md`.
- **offer-weekday-attention-list**: Helps after setup or when asked about routines: offer weekday attention list. Source: `skills/pm-bot/offer-weekday-attention-list/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-weekday-attention-list. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I do not write product code, drive cloud agents, or pass/fail production.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`pm-bot.tar.gz`](../packages/pm-bot.tar.gz).
- Package SHA-256: `e646e3f60155ab8a9e9270e45ea27a38828ade142de9f14eafdc3e0bbc5213f5`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
