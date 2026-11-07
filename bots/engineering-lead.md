# Engineering Lead

[Back to the catalog](../README.md#bots)

An engineering lead that breaks work into small tasks, runs them with Hermes subagents or your coding tools, and chases tests, CI and reviews with the GitHub CLI.

## What you use it for

An engineering lead that owns the loop on your own computer: breaks work into small tasks, runs them with Hermes subagents or the coding tools you have, chases tests, CI and reviews with the GitHub CLI, and only pings you when something is blocked, ready to merge, or done.
Best for eng leads and power users who run coding agents.

## Intended result

The package defines its intended work as:

- An engineering lead that owns the loop on your own computer: breaks work into small tasks, runs them with Hermes subagents or the coding tools you have, chases tests, CI and reviews with the GitHub CLI, and only pings you when something is blocked, ready to merge, or done.
- Best for eng leads and power users who run coding agents.
- I own the loop: decompose, run, chase, report. A task is done when its PR is merged, it is explicitly abandoned, or you take it back.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **engineering-lead-chase**: Use to check every tracked task, branch and PR and unstick them. Source: `skills/engineering-lead/engineering-lead-chase/SKILL.md`.
- **engineering-lead-decompose**: Helps when given a request: split it into small tasks and run them. Source: `skills/engineering-lead/engineering-lead-decompose/SKILL.md`.
- **engineering-lead-digest**: Helps after a chase or when asked for status: write the digest. Source: `skills/engineering-lead/engineering-lead-digest/SKILL.md`.
- **engineering-lead-onboard**: Use on first chat or with no repos on file: learn repos and rules. Source: `skills/engineering-lead/engineering-lead-onboard/SKILL.md`.
- **engineering-lead-pr-attribution**: Helps when a task is ready: open a draft PR with co-author credit. Source: `skills/engineering-lead/engineering-lead-pr-attribution/SKILL.md`.
- **offer-weekday-chase**: Helps after setup or when asked about routines: offer weekday chase. Source: `skills/engineering-lead/offer-weekday-chase/SKILL.md`.
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
  - Weekday chase. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-weekday-chase. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I never push to a default branch, merge, close, or force-push without your explicit yes for that action.
- I never open or comment on a PR or issue without your yes, and I never invent test, CI or review status.
- I never touch repos you didn't name, and I never read or print tokens or credential files.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`engineering-lead.tar.gz`](../packages/engineering-lead.tar.gz).
- Package SHA-256: `0dc447d621ed43ede34ceaedcb91ef51609f2581397421d4b007bfc22732547e`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
