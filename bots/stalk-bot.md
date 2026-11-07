# Stalk Bot

[Back to the catalog](../README.md#bots)

Signs up for your competitors' newsletters and products under its own research email, walks their onboarding on video, and watches their site, pricing, changelo

## What you use it for

Signs up for your competitors' newsletters and products under its own research email, walks their onboarding on video, and watches their site, pricing, changelog, jobs, and X.

## Intended result

The package defines its intended work as:

- Signs up for your competitors' newsletters and products under its own research email, walks their onboarding on video, and watches their site, pricing, changelog, jobs, and X.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **stalk-bot**: Helps when a task needs Stalk Bot reference notes. Source: `skills/stalk-bot/SKILL.md`.
- **add-competitor**: Helps when the user names a new competitor. Provisions an identity. Source: `skills/stalk-bot/add-competitor/SKILL.md`.
- **battlecard**: Use on demand to turn a competitor dossier into a battlecard draft. Draft only. Source: `skills/stalk-bot/battlecard/SKILL.md`.
- **competitor-churn**: Helps when opt-in module. Detect the user's customers lost to a watched. Source: `skills/stalk-bot/competitor-churn/SKILL.md`.
- **demo-pulse**: Helps when run the full delivery shape on clearly labeled EXAMPLE data for a demo. Source: `skills/stalk-bot/demo-pulse/SKILL.md`.
- **drop-competitor**: Helps when the user stops watching a competitor. Unsubscribes the research. Source: `skills/stalk-bot/drop-competitor/SKILL.md`.
- **evidence-media**: Helps when how I capture visual evidence. Source: `skills/stalk-bot/evidence-media/SKILL.md`.
- **feature-matrix**: Use on demand or in the pulse when enabled. Features by competitor from. Source: `skills/stalk-bot/feature-matrix/SKILL.md`.
- **html-report**: Helps when build the self-contained HTML report that closes every teardown. Source: `skills/stalk-bot/html-report/SKILL.md`.
- **identity-ladder**: Helps when how I obtain and run research identities. Source: `skills/stalk-bot/identity-ladder/SKILL.md`.
- **modules**: Helps when the 13 per-competitor modules. Source: `skills/stalk-bot/modules/SKILL.md`.
- **offer-competitor-churn-watch**: Helps after setup or when asked about routines: offer competitor churn watch. Source: `skills/stalk-bot/offer-competitor-churn-watch/SKILL.md`.
- **offer-competitor-pulse**: Helps after setup or when asked about routines: offer competitor pulse. Source: `skills/stalk-bot/offer-competitor-pulse/SKILL.md`.
- **offer-weekly-deep-dive**: Helps after setup or when asked about routines: offer weekly deep dive. Source: `skills/stalk-bot/offer-weekly-deep-dive/SKILL.md`.
- **profile-us**: Use at setup and whenever the user's own positioning. Source: `skills/stalk-bot/profile-us/SKILL.md`.
- **pulse**: Helps for the scheduled pulse. Source: `skills/stalk-bot/pulse/SKILL.md`.
- **read-the-mail**: Helps for the newsletter pulse. Source: `skills/stalk-bot/read-the-mail/SKILL.md`.
- **snapshot-site**: Helps when default-on modules for website. Source: `skills/stalk-bot/snapshot-site/SKILL.md`.
- **stalk-setup**: Use on first run or to change company. Source: `skills/stalk-bot/stalk-setup/SKILL.md`.
- **subscribe**: Use to get a competitor's research identity onto their newsletter. Source: `skills/stalk-bot/subscribe/SKILL.md`.
- **teardown**: Use on demand for a side-by-side onboarding comparison between one competitor. Source: `skills/stalk-bot/teardown/SKILL.md`.
- **walk-the-product**: Helps when default-on module. Sign up. Source: `skills/stalk-bot/walk-the-product/SKILL.md`.
- **watch-x**: Helps when default-on module. Uses the X connector to track competitor product. Source: `skills/stalk-bot/watch-x/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-competitor-churn-watch, offer-competitor-pulse, offer-weekly-deep-dive. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Each pulse reports what changed against your positioning and closes with counterpositioning moves, and it never posts or contacts anyone.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`stalk-bot.tar.gz`](../packages/stalk-bot.tar.gz).
- Package SHA-256: `0358e4f9bab0d9265ce54bafb17544c3d6b382adefbed2210dc55d41b6489f89`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
