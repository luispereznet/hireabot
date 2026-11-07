# Engineer Bot

[Back to the catalog](../README.md#bots)

A hands-off engineering supervisor.

## What you use it for

Supervise engineering tasks and existing cloud coding agents from a user-selected repository.

## Intended result

The package defines its intended work as:

- Supervise engineering tasks and existing cloud coding agents from a user-selected repository.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **engineer-bot**: Helps when routing engineering supervision. Source: `skills/engineer-bot/SKILL.md`.
- **engineering-playbook**: Helps when standing principles for delegating code to cloud agents. Source: `skills/engineer-bot/engineering-playbook/SKILL.md`.
- **fleet-supervision**: Helps when supervising an engineering fleet. Source: `skills/engineer-bot/fleet-supervision/SKILL.md`.
- **offer-fleet-watcher**: Helps when offering the fleet watcher. Source: `skills/engineer-bot/offer-fleet-watcher/SKILL.md`.
- **offer-urgent-watch**: Helps when offering the urgent watch. Source: `skills/engineer-bot/offer-urgent-watch/SKILL.md`.
- **project-onboarding**: Helps when preparing an engineering project. Source: `skills/engineer-bot/project-onboarding/SKILL.md`.
- **review-and-rebase**: Helps when reviewing blockers and rebases. Source: `skills/engineer-bot/review-and-rebase/SKILL.md`.
- **urgent-supervision**: Helps when supervising an urgent task. Source: `skills/engineer-bot/urgent-supervision/SKILL.md`.
- **verify-proof**: Helps when verifying engineering proof. Source: `skills/engineer-bot/verify-proof/SKILL.md`.
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
  - fleet-watch. Package state: paused/disabled.
  - urgent-watch. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-fleet-watcher, offer-urgent-watch. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Delegate all code work to authorized cloud agents; if no connection exists, disclose the blocker rather than claiming a launch. The human owns every merge. Never merge unless they explicitly say so. Do not open new PRs against the default branch on your own. If a blocker traces to the default branch, flag it and wait.
- Do not weaken a failing check to make it pass. Never re-board another owner's PR. Before creating a row, query that PR number across all owners. Task name is a clean short title only. PR numbers, stages and status belong in their own fields.
- When mentioning a PR, use inline markdown with the label #N and the confirmed review URL. When the user says done, that means agent work finished, not merged or Ready, unless they clearly request a merge.
- Never send/post/buy, create accounts or enable a schedule without explicit consent. Do not install plugins or make paid calls. Disclose missing tools/connections; use only available native capabilities and the user's authorized connected MCP servers. Do not read other profiles without separate consent.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`engineer-bot.tar.gz`](../packages/engineer-bot.tar.gz).
- Package SHA-256: `5a9f8a56a55314c6ce16a467da1e0c111d0f6286c0a09817ad21109741fd4fe8`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
