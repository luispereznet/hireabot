# Product Marketer

[Back to the catalog](../README.md#bots)

Learns your product, brand, tone, and positioning principles; uses competitive research to sharpen how you stand out; drafts and crafts copy against those princ

## What you use it for

Learns your product, brand, tone, and positioning principles; uses competitive research to sharpen how you stand out; drafts and crafts copy against those principles; and hands off landing-page and Ads copy to the rest of the marketing team.

## Intended result

The package defines its intended work as:

- Learns your product, brand, tone, and positioning principles; uses competitive research to sharpen how you stand out; drafts and crafts copy against those principles; and hands off landing-page and Ads copy to the rest of the marketing team.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **product-marketer**: Helps when a task needs Product Marketer reference notes. Source: `skills/product-marketer/SKILL.md`.
- **anti-slop**: Use on every draft or revision before the user sees it so it sounds human. Source: `skills/product-marketer/anti-slop/SKILL.md`.
- **brief-out**: Helps when copy is ready to become a page or a campaign. Produces the landing. Source: `skills/product-marketer/brief-out/SKILL.md`.
- **copy-review**: Use to score a piece of copy against the principles doc and the voice profile. Source: `skills/product-marketer/copy-review/SKILL.md`.
- **draft-copy**: Helps for any copy ask: edit what they wrote. Source: `skills/product-marketer/draft-copy/SKILL.md`.
- **learn-from-shipped**: Helps when the user shares the copy they actually published or the edits they. Source: `skills/product-marketer/learn-from-shipped/SKILL.md`.
- **learn-the-product**: Use to learn what the product is and how the company already writes. Source: `skills/product-marketer/learn-the-product/SKILL.md`.
- **offer-principles-review**: Helps after setup or when asked about routines: offer principles review. Source: `skills/product-marketer/offer-principles-review/SKILL.md`.
- **principles**: Use to write or revise the positioning principles doc. Source: `skills/product-marketer/principles/SKILL.md`.
- **product-marketer-setup**: Use on first run, or when the user wants to change the product. Source: `skills/product-marketer/product-marketer-setup/SKILL.md`.
- **sharpen-positioning**: Helps when competitive findings arrive from the user or from a teammate. Source: `skills/product-marketer/sharpen-positioning/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-principles-review. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`product-marketer.tar.gz`](../packages/product-marketer.tar.gz).
- Package SHA-256: `7e267e6b599b8669ac26f345bd35fde120c067e0b6f760b9de628366a4c624c2`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
