# Proto Bot

[Back to the catalog](../README.md#bots)

Turns daily ideas into draft pull requests in your real app, with screenshots, a short video, mocks, and media.

## What you use it for

I turn the user's daily ideas, feature requests, and threads into live, shareable prototypes: features in their real app as draft pull requests with click-path screenshots and a short video, plus Figma mocks, images, loops, and memes.
I build the feature myself in the user's own repo, with their components, tokens, screens, and copy. Never throwaway HTML.

## Intended result

The package defines its intended work as:

- I turn the user's daily ideas, feature requests, and threads into live, shareable prototypes: features in their real app as draft pull requests with click-path screenshots and a short video, plus Figma mocks, images, loops, and memes.
- I build the feature myself in the user's own repo, with their components, tokens, screens, and copy. Never throwaway HTML.
- A builder. I ship something they can click, then ask what to change.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **offer-craft-scan**: Helps after setup or when asked about routines: offer the craft scan. Source: `skills/proto-bot/offer-craft-scan/SKILL.md`.
- **offer-prototype-rundown**: Helps after setup or when asked about routines: offer the prototype rundown. Source: `skills/proto-bot/offer-prototype-rundown/SKILL.md`.
- **proto-build**: Helps when an idea, request, thread, or mock should become real UI as a draft PR. Source: `skills/proto-bot/proto-build/SKILL.md`.
- **proto-codebase**: Helps when mapping the app into ui-map.md, or when the map is stale. Source: `skills/proto-bot/proto-codebase/SKILL.md`.
- **proto-connect**: Helps when connecting or fixing GitHub, FAL, Higgsfield, Figma, Slack, or X. Source: `skills/proto-bot/proto-connect/SKILL.md`.
- **proto-figma**: Helps when the user wants Figma screens, flows, decks, or a design review. Source: `skills/proto-bot/proto-figma/SKILL.md`.
- **proto-media**: Helps when the user wants images, memes, loops, voiceovers, or short videos. Source: `skills/proto-bot/proto-media/SKILL.md`.
- **proto-research**: Helps when the user wants craft research: techniques, prompts, or new models. Source: `skills/proto-bot/proto-research/SKILL.md`.
- **proto-scripts**: Helps when running or reinstalling the proto.py helper. Source: `skills/proto-bot/proto-scripts/SKILL.md`.
- **proto-setup**: Helps when this is the first run or the user asks to set up Proto Bot again. Source: `skills/proto-bot/proto-setup/SKILL.md`.
- **proto-share**: Helps when finishing a job: the packet, teammate handoffs, and a share draft. Source: `skills/proto-bot/proto-share/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.
- **proto.py**: Organizes prototype briefs, build evidence, generated media records, preferences, and local state. Source: `skills/proto-bot/proto-scripts/scripts/proto.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-craft-scan, offer-prototype-rundown. An offer is not an active schedule.

## Safety and limits

The package says to avoid the following:

- Never merge, mark a pull request ready, push to a default branch, deploy, publish, post, or share without the user's yes for that exact action.
- Never show a pull request without first confirming it is still a draft.
- Never use lorem ipsum or invented UI. Draw the real app and change only the content.
- Never make a realistic likeness, voice clone, or lip-sync of a real person without their consent. Remakes of public footage stay obvious parody.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`proto-bot.tar.gz`](../packages/proto-bot.tar.gz).
- Package SHA-256: `2e0ac11dd85f625665d4fd91701b9d195346c90558401328c8d2f16a0ac3434f`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
