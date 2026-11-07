# Pitch Deck Coach

[Back to the catalog](../README.md#bots)

Reviews a pitch deck and reports what an investor is likely to understand, believe, question, and remember, then helps strengthen the story, evidence, and slide

## What you use it for

Reviews a pitch deck and reports what an investor is likely to understand, believe, question, and remember, then helps strengthen the story, evidence, and slides.

## Intended result

The package defines its intended work as:

- Reviews a pitch deck and reports what an investor is likely to understand, believe, question, and remember, then helps strengthen the story, evidence, and slides.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **pitch-deck-coach**: Helps when a task needs Pitch Deck Coach reference notes. Source: `skills/pitch-deck-coach/SKILL.md`.
- **pdc-methodology**: Use with pitch-deck-coach for the v3.1 fundraising methodology. Source: `skills/pitch-deck-coach/pdc-methodology/SKILL.md`.
- **pdc-modes**: Use with pitch-deck-coach for runtime modes. Source: `skills/pitch-deck-coach/pdc-modes/SKILL.md`.
- **pdc-workspace**: Use with pitch-deck-coach for the Deck Model schema. Source: `skills/pitch-deck-coach/pdc-workspace/SKILL.md`.
- **pitch-deck-coach**: Helps when reviewing, coaching. Source: `skills/pitch-deck-coach/pitch-deck-coach/SKILL.md`.

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

- Never invent missing facts, traction, customers, market data, investor reactions, or evidence. Classify every load-bearing claim as FACT, INFERENCE, HYPOTHESIS, or UNKNOWN, and distinguish facts from inference, hypotheses, and unknowns.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`pitch-deck-coach.tar.gz`](../packages/pitch-deck-coach.tar.gz).
- Package SHA-256: `11b32c2c811cf1a874134659f253d00690b1a939605be38df5746c32d291f846`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
