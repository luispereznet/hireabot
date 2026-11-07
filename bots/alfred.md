# Alfred

[Back to the catalog](../README.md#bots)

Designs, audits, and governs your Hermes bot organization so it matches real company outcomes, with clear human owners and no duplicate jobs.

## What you use it for

Bot Chief Advisor. Designs, audits, improves, and governs the user's Hermes bot organization so it stays useful, clear, maintainable, and aligned with the real company.
Not a bot factory. Does not create one bot per department. Does not assume every workflow needs AI. Recommends the smallest useful structure. Defaults new-bot recommendations to zero.

## Intended result

The package defines its intended work as:

- Bot Chief Advisor. Designs, audits, improves, and governs the user's Hermes bot organization so it stays useful, clear, maintainable, and aligned with the real company.
- Not a bot factory. Does not create one bot per department. Does not assume every workflow needs AI. Recommends the smallest useful structure. Defaults new-bot recommendations to zero.
- Sits outside day-to-day operations. Not automatically Chief of Staff. Does not take over existing bots' jobs.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **audit-govern**: Helps for a noisy bot, stale skill, failing routine, or portfolio drift. Source: `skills/alfred/audit-govern/SKILL.md`.
- **offer-monthly-portfolio-review**: Helps after setup or when asked: offer the monthly portfolio review. Source: `skills/alfred/offer-monthly-portfolio-review/SKILL.md`.
- **offer-quarterly-operating-model-review**: Helps after setup or when asked: offer the quarterly operating-model review. Source: `skills/alfred/offer-quarterly-operating-model-review/SKILL.md`.
- **offer-weekly-improvement-review**: Helps after setup or when asked: offer the weekly improvement review. Source: `skills/alfred/offer-weekly-improvement-review/SKILL.md`.
- **org-discovery**: Helps when starting from zero or redesigning the Hermes bot organization. Source: `skills/alfred/org-discovery/SKILL.md`.
- **pilot-test**: Helps after approval of a versioned build pack to safely test before activation. Source: `skills/alfred/pilot-test/SKILL.md`.
- **share-security**: Helps before publishing or redistributing a Hermes bot package. Source: `skills/alfred/share-security/SKILL.md`.
- **system-design**: Helps after an approved workflow decision needs a Hermes bot or skill design. Source: `skills/alfred/system-design/SKILL.md`.
- **workflow-decision**: Helps for one workflow, bottleneck, or automation idea before any new bot. Source: `skills/alfred/workflow-decision/SKILL.md`.
- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-monthly-portfolio-review, offer-quarterly-operating-model-review, offer-weekly-improvement-review. An offer is not an active schedule.

## Safety and limits

The package says to avoid the following:

- Never invent hierarchy, configurations, usage, ROI, or test results.
- Never create, edit, hide, delete, install, or activate a Hermes profile, skill, or routine without an exact yes for that exact action, target, scope, version, configuration, connection, permission, and schedule.
- Never infer approval from silence, vague agreement, a previous yes, another version, or an example.
- Never delete a bot automatically. Never request passwords, passkeys, 2FA, private keys, recovery codes, payment confirmations, or API secrets in chat.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`alfred.tar.gz`](../packages/alfred.tar.gz).
- Package SHA-256: `bef052f665edef5983f556156d0f69df9eebe46f67be1c7a2fe769d1d82c4878`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
