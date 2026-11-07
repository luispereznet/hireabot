# Video Edit Desk

[Back to the catalog](../README.md#bots)

Turns uploaded footage into cut clips, burned-in captions, and platform-sized exports.

## What you use it for

Turns uploaded footage into cut clips, burned-in captions, and platform-sized exports.
Upload footage and I trim it, pull clips out of it, resize it for a platform, burn in captions, and hand back a transcript.

## Intended result

The package defines its intended work as:

- Turns uploaded footage into cut clips, burned-in captions, and platform-sized exports.
- Upload footage and I trim it, pull clips out of it, resize it for a platform, burn in captions, and hand back a transcript.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **captions-and-transcript**: Helps when the user wants a transcript. Source: `skills/video-edit-desk/captions-and-transcript/SKILL.md`.
- **cut-from-your-notes**: Helps when the user wants trims. Source: `skills/video-edit-desk/cut-from-your-notes/SKILL.md`.
- **footage-intake**: Helps when the user uploads, links, or sends a new video or audio file. Source: `skills/video-edit-desk/footage-intake/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/video-edit-desk/getting-started/SKILL.md`.
- **offer-weekly-cut-queue**: Helps after setup or when asked about routines: offer weekly cut queue. Source: `skills/video-edit-desk/offer-weekly-cut-queue/SKILL.md`.
- **platform-versions-and-delivery-check**: Helps when a cut needs a platform's aspect, file size, or loudness. Source: `skills/video-edit-desk/platform-versions-and-delivery-check/SKILL.md`.
- **short-clips-from-a-long-video**: Helps when the user wants short clips pulled out of a longer video. Source: `skills/video-edit-desk/short-clips-from-a-long-video/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-weekly-cut-queue. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Works from your notes and never overwrites the original.
- I'm not a creative director, I don't grade a look or build motion graphics, and I don't post anything anywhere.
- When my setup finishes I don't stop at "ready".
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`video-edit-desk.tar.gz`](../packages/video-edit-desk.tar.gz).
- Package SHA-256: `33a9356878e0ccbb76023e20c467f92d1f5b2f0c6f3be49f9676661f31126dfa`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
