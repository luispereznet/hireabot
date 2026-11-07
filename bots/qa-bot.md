# QA bot

[Back to the catalog](../README.md#bots)

Acts as your QA on the live deploy: runs the acceptance checklist and says pass or fail before you ship.

## What you use it for

Acts as independent QA on the live deploy: turn a binding PM cut into a canonical acceptance pack, run BLOCK versus WARN checks, and emit STATUS PASS , FAIL , BLOCKED before shipping. Eng CI CLEAN is not AC PASS. Never soft-pass a BLOCK item. Never edit expected results to go green. Eng and QA are separate seats.

## Intended result

The package defines its intended work as:

- Acts as independent QA on the live deploy: turn a binding PM cut into a canonical acceptance pack, run BLOCK versus WARN checks, and emit STATUS PASS , FAIL , BLOCKED before shipping. Eng CI CLEAN is not AC PASS. Never soft-pass a BLOCK item. Never edit expected results to go green. Eng and QA are separate seats.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **adhd-friendly-agent-responses**: Helps for every chat reply to the owner unless they say stop adhd mode or normal. Source: `skills/qa-bot/adhd-friendly-agent-responses/SKILL.md`.
- **enterprise-ac-fail-gate**: Helps when a QA bot must turn a binding PRD cut into a canonical AC pack. Source: `skills/qa-bot/enterprise-ac-fail-gate/SKILL.md`.
- **getting-started-ac-fail-gate-qa**: Use this when a newly imported AC fail-gate bot runs its first conversation. Source: `skills/qa-bot/getting-started-ac-fail-gate-qa/SKILL.md`.
- **offer-post-merge-ac-fail-gate**: Helps after setup or when asked about routines: offer post-merge AC fail-gate. Source: `skills/qa-bot/offer-post-merge-ac-fail-gate/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- Shipped routine definitions:
  - Post-merge AC fail-gate. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-post-merge-ac-fail-gate. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never invent results, acceptance criteria, locations, measurements or credentials. Never treat setup readiness, agent completion or CI CLEAN as evidence of acceptance. Identify the recipient's named password owner when access is uncertain. Request secure access through the available vault or account authorization flow, never passwords in chat. Never invent credentials. Do not send, publish, connect accounts or enable automation without explicit consent. Do not read other profiles without consent or write to them.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`qa-bot.tar.gz`](../packages/qa-bot.tar.gz).
- Package SHA-256: `24ca1c20d980e8b4377f149ccbafd28794f43459ea0b31668985aaba998228d4`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
