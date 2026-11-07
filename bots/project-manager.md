# Project Manager

[Back to the catalog](../README.md#bots)

Marketing project manager that coordinates research, positioning, landing pages, ads, and analytics across specialist bots — with screenshot check-ins and human

## What you use it for

Marketing project manager that coordinates research, positioning, landing pages, ads, and analytics across specialist bots — with screenshot check-ins and human gates on merge and spend.

## Intended result

The package defines its intended work as:

- Marketing project manager that coordinates research, positioning, landing pages, ads, and analytics across specialist bots — with screenshot check-ins and human gates on merge and spend.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **project-manager**: Helps when a task needs Project Manager reference notes. Source: `skills/project-manager/SKILL.md`.
- **check-in**: Helps for the scheduled status pass. Source: `skills/project-manager/check-in/SKILL.md`.
- **delegate**: Helps when a work item is ready to be worked by someone other than me. Writes. Source: `skills/project-manager/delegate/SKILL.md`.
- **gates**: Use whenever something needs a merge. Source: `skills/project-manager/gates/SKILL.md`.
- **html-report**: Use to build the self-contained status or retro report that closes a check-in. Source: `skills/project-manager/html-report/SKILL.md`.
- **offer-friday-week-ahead**: Helps after setup or when asked about routines: offer friday week ahead. Source: `skills/project-manager/offer-friday-week-ahead/SKILL.md`.
- **offer-weekday-status-check-in**: Helps after setup or when asked about routines: offer weekday status check-in. Source: `skills/project-manager/offer-weekday-status-check-in/SKILL.md`.
- **plan**: Helps when building or changing the plan. Source: `skills/project-manager/plan/SKILL.md`.
- **project-manager-setup**: Use on first run, or when the user changes the goal. Source: `skills/project-manager/project-manager-setup/SKILL.md`.
- **retro**: Helps after the launch date. Source: `skills/project-manager/retro/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-friday-week-ahead, offer-weekday-status-check-in. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`project-manager.tar.gz`](../packages/project-manager.tar.gz).
- Package SHA-256: `936f04d270c94a492367c3512ea73e80133a08cc81d7fe5288c2c21e95570ef3`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
