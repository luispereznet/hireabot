# Startup QA Bot

[Back to the catalog](../README.md#bots)

Walks your product every weekday in its own test account and tells you what shipped, what got unshipped, what broke (with repro steps and screenshots), and whic

## What you use it for

Walks your product every weekday in its own test account and tells you what shipped, what got unshipped, what broke (with repro steps and screenshots), and which calls need you.

## Intended result

The package defines its intended work as:

- Walks your product every weekday in its own test account and tells you what shipped, what got unshipped, what broke (with repro steps and screenshots), and which calls need you.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **startup-qa-bot**: Helps when a task needs Startup QA Bot reference notes. Source: `skills/startup-qa-bot/SKILL.md`.
- **offer-morning-product-walk**: Helps after setup or when asked about routines: offer morning product walk. Source: `skills/startup-qa-bot/offer-morning-product-walk/SKILL.md`.
- **product-rundown**: Helps after a product walk: sort shipped. Source: `skills/startup-qa-bot/product-rundown/SKILL.md`.
- **product-walk**: Use to walk the user's product in the test account. Source: `skills/startup-qa-bot/product-walk/SKILL.md`.
- **qa-scripts**: Helps when the qa.py state tool. Source: `skills/startup-qa-bot/qa-scripts/SKILL.md`.
- **qa-setup**: Use on the first conversation after import. Source: `skills/startup-qa-bot/qa-setup/SKILL.md`.
- **test-account**: Use to start my own browser. Source: `skills/startup-qa-bot/test-account/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-morning-product-walk. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Reads its own verification emails or takes pasted codes, and never touches real data.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`startup-qa-bot.tar.gz`](../packages/startup-qa-bot.tar.gz).
- Package SHA-256: `e4302b45a061c85dc9f759c4915bb76f6d11cf3797f840f4b65d74921c149ae1`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
