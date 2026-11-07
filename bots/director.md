# Director

[Back to the catalog](../README.md#bots)

Your video director: turn briefs into short films, ads, explainers, music videos, micro-dramas, and more — plan, shoot, cut, and deliver.

## What you use it for

Your video director: turn briefs into short films, ads, explainers, music videos, micro-dramas, and more — plan, shoot, cut, and deliver.

## Intended result

The package defines its intended work as:

- Your video director: turn briefs into short films, ads, explainers, music videos, micro-dramas, and more — plan, shoot, cut, and deliver.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **getting-started**: Use on the first conversation after someone imports this Director template \u2014. Source: `skills/director/getting-started/SKILL.md`.
- **video-director**: Use first whenever the user asks for a video. Source: `skills/director/video-director/SKILL.md`.
- **video-format-music-video**: Helps for a music video or song-driven clip \u2014 the song is the spine and the clock. Source: `skills/director/video-format-music-video/SKILL.md`.
- **video-frames**: Helps before drawing any character. Source: `skills/director/video-frames/SKILL.md`.
- **video-look**: Helps before the first image or video of any film to set its style line. Source: `skills/director/video-look/SKILL.md`.
- **video-plan-produce**: Use once a plan is approved to run production end to end. Source: `skills/director/video-plan-produce/SKILL.md`.
- **video-plan-questions**: Helps when a video brief leaves something open. Source: `skills/director/video-plan-questions/SKILL.md`.
- **video-plan-script**: Helps after the questions to pitch three ideas the user picks from. Source: `skills/director/video-plan-script/SKILL.md`.
- **video-project-folder**: Helps when setting up or resuming a video project. Source: `skills/director/video-project-folder/SKILL.md`.
- **video-takes**: Helps before every the video generation tool call: image-to-video from a checked first frame. Source: `skills/director/video-takes/SKILL.md`.
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
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`director.tar.gz`](../packages/director.tar.gz).
- Package SHA-256: `3316fb179534d998f1a48e8be0d45e7a2931ae9d8b82489e690a8ae91febf324`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
