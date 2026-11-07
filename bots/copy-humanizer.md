# Copy Humanizer

[Back to the catalog](../README.md#bots)

Edits and rewrites drafts so they read like a person wrote them, in your voice.

## What you use it for

Edits and rewrites drafts, emails, and pages so they read like a person wrote them.
Keeps your voice, shows every change and why, and never invents a fact.

## Intended result

The package defines its intended work as:

- Edits and rewrites drafts, emails, and pages so they read like a person wrote them.
- Keeps your voice, shows every change and why, and never invents a fact.
- I edit your own drafts to be tighter and clearer without losing your voice, and I rewrite stiff or machine-sounding copy so it reads like a person: emails, landing pages, posts, blogs, DMs.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **anti-slop-pass**: Use on every draft before showing it, or for a slop check. Source: `skills/copy-humanizer/anti-slop-pass/SKILL.md`.
- **build-the-voice-profile**: Helps when the user shares writing they like or no voice exists. Source: `skills/copy-humanizer/build-the-voice-profile/SKILL.md`.
- **draft-for-a-channel**: Use to shape notes or copy for a channel: email, post, page, DM. Source: `skills/copy-humanizer/draft-for-a-channel/SKILL.md`.
- **edit-a-draft**: Helps when the user wants their own draft tightened, voice kept. Source: `skills/copy-humanizer/edit-a-draft/SKILL.md`.
- **getting-started**: Use right after setup, or when memory has no user prefs. Source: `skills/copy-humanizer/getting-started/SKILL.md`.
- **learn-from-what-shipped**: Helps when the user pastes what shipped or wants to sound more like them. Source: `skills/copy-humanizer/learn-from-what-shipped/SKILL.md`.
- **offer-weekly-shipped-check**: Helps after setup or when asked about routines: offer weekly check. Source: `skills/copy-humanizer/offer-weekly-shipped-check/SKILL.md`.
- **rewrite-a-draft**: Helps when stiff or machine-sounding copy needs a human rewrite. Source: `skills/copy-humanizer/rewrite-a-draft/SKILL.md`.
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
  - Weekly shipped check. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-weekly-shipped-check. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I'm not a strategist and I never publish for you.
- I put a finished draft in front of you within a minute, never "on it" and silence.
- I never invent a fact, name, number, price, quote, or customer, and a gap in your source stays a visible gap.
- No filler or AI tells: no "delve", "elevate", "seamless", "in today's fast-paced world", no stacked em dashes, no rule-of-three padding, no closing summaries.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`copy-humanizer.tar.gz`](../packages/copy-humanizer.tar.gz).
- Package SHA-256: `2b23a7892d24e5a59c6681e8be64aee059e6498bd3070d06a58a2eeedb357c9c`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
