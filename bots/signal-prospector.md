# Signal Prospector

[Back to the catalog](../README.md#bots)

Finds the accounts and people in your CRM and product data that just showed intent, ranks them, and drafts the first touch.

## What you use it for

Finds the accounts and people in your CRM and product data that just showed intent, ranks them, and drafts the first touch.
Runs on a schedule, explains every signal, and nothing sends without your yes.

## Intended result

The package defines its intended work as:

- Finds the accounts and people in your CRM and product data that just showed intent, ranks them, and drafts the first touch.
- Runs on a schedule, explains every signal, and nothing sends without your yes.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **account-tiering**: Helps when scores and tiers accounts inside each motion using weighted signal. Source: `skills/signal-prospector/account-tiering/SKILL.md`.
- **contact-ranking**: Helps when picks and ranks the people to contact at each tiered account. Source: `skills/signal-prospector/contact-ranking/SKILL.md`.
- **first-touch-drafts**: Helps when drafts one short first-touch email per ranked contact with the signal. Source: `skills/signal-prospector/first-touch-drafts/SKILL.md`.
- **getting-started**: Helps when first conversation with a new owner. Connects the CRM and product data. Source: `skills/signal-prospector/getting-started/SKILL.md`.
- **offer-monday-signal-digest**: Helps after setup or when asked about routines: offer monday signal digest. Source: `skills/signal-prospector/offer-monday-signal-digest/SKILL.md`.
- **signal-scan**: Helps when pulls every intent signal across the owner's accounts from the CRM. Source: `skills/signal-prospector/signal-scan/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-monday-signal-digest. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`signal-prospector.tar.gz`](../packages/signal-prospector.tar.gz).
- Package SHA-256: `ab6bbc68d411ae75da8ede3bb66b2597167e3593e141e12865c3a6e3a947dacf`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
