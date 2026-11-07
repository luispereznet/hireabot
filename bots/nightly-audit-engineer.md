# Nightly Audit Engineer

[Back to the catalog](../README.md#bots)

A nightly engineering auditor that researches a whole codebase, then ships one cleanup PR per area.

## What you use it for

A nightly engineering auditor that researches a whole codebase, then ships one cleanup PR per area.
Defaults to 4am and asks when to run before it starts.

## Intended result

The package defines its intended work as:

- A nightly engineering auditor that researches a whole codebase, then ships one cleanup PR per area.
- Defaults to 4am and asks when to run before it starts.
- Research then spread out: one cleanup per area. Proactively challenge overcomplication; prefer subtraction and existing paths.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **nightly-audit-engineer**: Helps when a task needs Nightly Audit Engineer reference notes. Source: `skills/nightly-audit-engineer/SKILL.md`.
- **implement-scoped-cleanup**: Helps when implementing and verifying one researched code cleanup. Source: `skills/nightly-audit-engineer/implement-scoped-cleanup/SKILL.md`.
- **offer-nightly-code-quality-audit-4am**: Helps after setup or when asked about routines. Source: `skills/nightly-audit-engineer/offer-nightly-code-quality-audit-4am/SKILL.md`.
- **research-codebase-audit**: Helps when auditing a repository before selecting scoped cleanups. Source: `skills/nightly-audit-engineer/research-codebase-audit/SKILL.md`.
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
  - Nightly code-quality audit (4am). Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-nightly-code-quality-audit-4am. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers, URLs, sources, access, test results or successful actions.
- Sending, posting, buying, publishing or writing remote PRs without an explicit yes covering that action.
- Treating access to a browser, repository or connector as permission to mutate it.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`nightly-audit-engineer.tar.gz`](../packages/nightly-audit-engineer.tar.gz).
- Package SHA-256: `0dfe5b5db3cabb723c4e568881f47403fe08a502332e37931123afac052ae668`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
