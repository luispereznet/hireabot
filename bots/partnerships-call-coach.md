# Partnerships Call Coach

[Back to the catalog](../README.md#bots)

Pitch and delivery coach for partnership, sponsorship, and high-stakes discovery calls.

## What you use it for

Pitch and delivery coach for partnership, sponsorship, and high-stakes discovery calls.
Reviews real call transcripts and returns sharp, evidence-based coaching — what landed, what to tighten, and exact phrasing upgrades — so feedback compounds over time.

## Intended result

The package defines its intended work as:

- Pitch and delivery coach for partnership, sponsorship, and high-stakes discovery calls.
- Reviews real call transcripts and returns sharp, evidence-based coaching — what landed, what to tighten, and exact phrasing upgrades — so feedback compounds over time.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **offer-post-pitch-call-review**: Helps after setup or when asked about routines: offer post-pitch call review. Source: `skills/partnerships-call-coach/offer-post-pitch-call-review/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-post-pitch-call-review. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`partnerships-call-coach.tar.gz`](../packages/partnerships-call-coach.tar.gz).
- Package SHA-256: `53b2e7a2d542e75fd91c4f2857d5ce1037cbcf9800e095e21236e231abdebc6f`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
