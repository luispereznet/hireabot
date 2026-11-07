# Clip Bot

[Back to the catalog](../README.md#bots)

Finds the best moments in a long recording and cuts them into short captioned clips.

## What you use it for

Finds the best moments in a long recording and cuts them into short captioned clips.
Works from an upload or a link, with transcript and timestamps on every clip.

## Intended result

The package defines its intended work as:

- Finds the best moments in a long recording and cuts them into short captioned clips.
- Works from an upload or a link, with transcript and timestamps on every clip.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **clip-captions-and-post-copy**: Helps when the user wants a title. Source: `skills/clip-bot/clip-captions-and-post-copy/SKILL.md`.
- **clip-pack-from-one-recording**: Helps when the user wants several clips out of one talk. Source: `skills/clip-bot/clip-pack-from-one-recording/SKILL.md`.
- **cut-a-clip**: Helps when the user picks a moment or gives you a timestamp range. Source: `skills/clip-bot/cut-a-clip/SKILL.md`.
- **find-the-clippable-moments**: Helps when a transcript exists. Source: `skills/clip-bot/find-the-clippable-moments/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/clip-bot/getting-started/SKILL.md`.
- **offer-clip-queue-pass**: Helps after setup or when asked about routines: offer clip queue pass. Source: `skills/clip-bot/offer-clip-queue-pass/SKILL.md`.
- **offer-friday-clip-recap**: Helps after setup or when asked about routines: offer friday clip recap. Source: `skills/clip-bot/offer-friday-clip-recap/SKILL.md`.
- **transcribe-a-recording**: Helps when the user hands over a recording. Source: `skills/clip-bot/transcribe-a-recording/SKILL.md`.
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
  - Clip queue pass. Package state: paused/disabled.
  - Friday clip recap. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-clip-queue-pass, offer-friday-clip-recap. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Claiming a tool exists or can transcribe without checking.
- I don't shoot or script video, I don't do multi-track edits, and I never post anywhere.
- When my setup finishes I don't stop at "ready".
- I show a transcript, a moment list, or a rendered clip within a minute, never "on it" and silence.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`clip-bot.tar.gz`](../packages/clip-bot.tar.gz).
- Package SHA-256: `bd0840be8f6ced73181edef9ea8102a8a2536f6fafcc3916a1ff558925a2a16b`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
