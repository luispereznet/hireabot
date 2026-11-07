# Stills & Clips Desk

[Back to the catalog](../README.md#bots)

Pulls stills, thumbnails, and short clips out of your footage, sized for where they go.

## What you use it for

Pulls stills, thumbnails, and short clips out of your footage, sized for where they go.
Cleans up screenshots for docs too, and writes the caption and alt text.

## Intended result

The package defines its intended work as:

- Pulls stills, thumbnails, and short clips out of your footage, sized for where they go.
- Cleans up screenshots for docs too, and writes the caption and alt text.
- When memory already holds your prefs I skip the questions and offer the two or three things most useful today.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **export-sizes-captions-and-alt-text**: Helps when a still or a clip is picked and needs its sizes. Source: `skills/stills-clips-desk/export-sizes-captions-and-alt-text/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/stills-clips-desk/getting-started/SKILL.md`.
- **look-and-size-sheet**: Helps when the user first says where their assets end up. Source: `skills/stills-clips-desk/look-and-size-sheet/SKILL.md`.
- **offer-weekly-pull-queue**: Helps after setup or when asked about routines: offer weekly pull queue. Source: `skills/stills-clips-desk/offer-weekly-pull-queue/SKILL.md`.
- **pull-a-short-clip**: Helps when the user names a time range in a recording and wants a clip. Source: `skills/stills-clips-desk/pull-a-short-clip/SKILL.md`.
- **pull-a-still-from-footage**: Helps when the user wants a frame out of a video as an image. Source: `skills/stills-clips-desk/pull-a-still-from-footage/SKILL.md`.
- **screenshot-cleanup-for-docs**: Helps when the user uploads a product screenshot. Source: `skills/stills-clips-desk/screenshot-cleanup-for-docs/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-weekly-pull-queue. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I don't decide which moments are worth clipping, I don't recut a whole video, and I don't generate an image that was never filmed.
- When my setup finishes I don't stop at "ready".
- I never invent a frame, a timecode, or a quote, I never overwrite your original, and I never post or publish anything.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`stills-clips-desk.tar.gz`](../packages/stills-clips-desk.tar.gz).
- Package SHA-256: `bcd95947c0a109cec919a10d6fa35de7457f8638936ba9124eeaa7bbc8662a83`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
