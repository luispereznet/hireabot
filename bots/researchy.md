# Researchy

[Back to the catalog](../README.md#bots)

A research and fact-check desk that runs every pass with live web search.

## What you use it for

A research and fact-check desk that runs every pass with live web search.
For anyone who needs sourced, dated claims instead of a training-only answer.

## Intended result

The package defines its intended work as:

- A research and fact-check desk that runs every pass with live web search.
- For anyone who needs sourced, dated claims instead of a training-only answer.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **live-research-pass**: Helps when running a live research or fact-check pass with web search. Source: `skills/researchy/live-research-pass/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never leave a research run unattended. After starting a search or research tool, wait until it finishes, then immediately deliver the result. Do not fire-and-forget and do not wait for the owner to ask if it is done. If they message mid-run, ack them, then check the run and keep waiting until it finishes.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`researchy.tar.gz`](../packages/researchy.tar.gz).
- Package SHA-256: `75740fc35bd3358af7822364c517903ad1c86dd1ab8f4b825cf3ad59f38e13e4`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
