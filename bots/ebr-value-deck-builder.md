# EBR & Value Deck Builder

[Back to the catalog](../README.md#bots)

Builds an executive business review or value deck for a named account from your CRM, call history, and usage data, on your brand, and hands you an editable file

## What you use it for

Build editable executive business reviews and value decks for named accounts from authorized CRM, call history and usage data. Deliver files for owner review.

## Intended result

The package defines its intended work as:

- Build editable executive business reviews and value decks for named accounts from authorized CRM, call history and usage data. Deliver files for owner review.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **brand-kit**: Helps when learns the owner's visual brand once from a sample deck or website. Source: `skills/ebr-value-deck-builder/brand-kit/SKILL.md`.
- **ebr-deck**: Helps when builds an executive business review deck for a customer account from. Source: `skills/ebr-value-deck-builder/ebr-deck/SKILL.md`.
- **getting-started**: Helps when first conversation with a new owner. Connects the CRM and data sources. Source: `skills/ebr-value-deck-builder/getting-started/SKILL.md`.
- **offer-renewal-deck-reminder**: Helps after setup or when asked about routines: offer renewal deck reminder. Source: `skills/ebr-value-deck-builder/offer-renewal-deck-reminder/SKILL.md`.
- **pptx-compat**: Helps when makes every generated pptx open cleanly in PowerPoint. Source: `skills/ebr-value-deck-builder/pptx-compat/SKILL.md`.
- **three-whys**: Helps when builds or updates a four-slide Why Change. Source: `skills/ebr-value-deck-builder/three-whys/SKILL.md`.
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
  - Renewal deck reminder. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-renewal-deck-reminder. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never invent facts, numbers, quotes, sources or test results. Every figure traces to a CRM record, call, usage report or owner statement; put sources in notes or the final slide. Never send a deck to a customer. Obtain explicit yes before external upload, send, post or buy, confirming exact content and destination, then read back the target. Connections and sampling ship disabled; routines ship paused. Assume no account access or user facts.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`ebr-value-deck-builder.tar.gz`](../packages/ebr-value-deck-builder.tar.gz).
- Package SHA-256: `d3a8d83c5f289cc3e7890aba903ea85953ad9a0afd7d1317223f2ec60cd26844`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
