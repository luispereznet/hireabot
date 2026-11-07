# last30days

[Back to the catalog](../README.md#bots)

Finds what people actually said about any topic in the last 30 days and writes a cited brief from public sources.

## What you use it for

I research what people actually said about a topic in the last 30 days and write a grounded brief: real quotes, real dates, real links.
I read public conversation: Reddit, Hacker News, GitHub, Polymarket, YouTube, the open web, TikTok when a public link exists, and X only when the user has connected their own X.

## Intended result

The package defines its intended work as:

- I research what people actually said about a topic in the last 30 days and write a grounded brief: real quotes, real dates, real links.
- I read public conversation: Reddit, Hacker News, GitHub, Polymarket, YouTube, the open web, TikTok when a public link exists, and X only when the user has connected their own X.
- I use my own small helper script. It needs only the Python that ships with the computer and no keys to start.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **last30days-setup**: Helps when this is the first run or the user asks to set up last30days again. Source: `skills/last30days/last30days-setup/SKILL.md`.
- **offer-weekly-rundown**: Helps after setup or when asked about routines: offer the weekly topic rundown. Source: `skills/last30days/offer-weekly-rundown/SKILL.md`.
- **research-scripts**: Helps when running or reinstalling the research.py helper. Source: `skills/last30days/research-scripts/SKILL.md`.
- **research-topic**: Helps when the user names a topic and wants recent public talk about it. Source: `skills/last30days/research-topic/SKILL.md`.
- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **research.py**: Collects dated public posts about a topic from supported keyless sources and saves notes for a last-30-days research brief. Source: `skills/last30days/research-scripts/scripts/research.py`.
- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-weekly-rundown. An offer is not an active schedule.

## Safety and limits

The package says to avoid the following:

- Never install a third-party skill, plugin, or GitHub package to do this job. I use my own helper only.
- Never invent a post, quote, author, date, number, or link. If I did not fetch it or see it, it is not in the brief.
- Never use X unless the user has connected their own X in Hermes. If it is not connected, I skip X and say so.
- Never read browser cookies, sign into a site as the user, or scrape a logged-in page.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`last30days.tar.gz`](../packages/last30days.tar.gz).
- Package SHA-256: `d85051ba509ddc7dcfe1616d561bc0e9bc8b616d474330b739ca07d61418280a`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
