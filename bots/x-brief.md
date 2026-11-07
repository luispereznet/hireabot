# X Brief

[Back to the catalog](../README.md#bots)

Turns the X accounts and topics you pick into one short daily brief with a link on every line.

## What you use it for

Turns the accounts and topics you pick on X into one short daily brief.
Reads your X connection or handles you paste, and never posts on your behalf.

## Intended result

The package defines its intended work as:

- Turns the accounts and topics you pick on X into one short daily brief.
- Reads your X connection or handles you paste, and never posts on your behalf.
- I read the accounts, topics, and searches you care about on X and turn them into one short brief with a link on every line.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **build-the-x-watch-list**: Helps when the user first names accounts or topics to watch, adds or drops one. Source: `skills/x-brief/build-the-x-watch-list/SKILL.md`.
- **daily-x-brief**: Helps when the user asks what is happening on X, asks to be caught up. Source: `skills/x-brief/daily-x-brief/SKILL.md`.
- **draft-a-post-or-reply**: Helps when the user asks for a post. Source: `skills/x-brief/draft-a-post-or-reply/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/x-brief/getting-started/SKILL.md`.
- **offer-daily-x-brief**: Helps after setup or when asked about routines: offer daily X brief. Source: `skills/x-brief/offer-daily-x-brief/SKILL.md`.
- **offer-weekly-x-recap**: Helps after setup or when asked about routines: offer weekly X recap. Source: `skills/x-brief/offer-weekly-x-recap/SKILL.md`.
- **read-a-thread-or-post**: Helps when the user pastes a post. Source: `skills/x-brief/read-a-thread-or-post/SKILL.md`.
- **weekly-x-recap**: Helps when the user asks what happened this week on X. Source: `skills/x-brief/weekly-x-recap/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- Shipped routine definitions:
  - Daily X brief. Package state: paused/disabled.
  - Weekly X recap. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-daily-x-brief, offer-weekly-x-recap. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- When X access is missing, I refer to README Setup for X access, which you configure yourself. I never suggest scraping or a logged-in browser, never ask for keys in chat, and never make up a docs link.
- When X is not readable, I say so, refer to README Setup, and offer to brief pasted posts and links.
- I'm not a general research assistant, I don't post for you, and I don't give growth advice.
- I put a real brief or answer in front of you within a minute, never "on it" and silence.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`x-brief.tar.gz`](../packages/x-brief.tar.gz).
- Package SHA-256: `1013cdf7a2d7b2ea8b842b462e8ee88daa34ad7d411ed81a286ee18730ad911d`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
