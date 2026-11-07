# Credit Card Max

[Back to the catalog](../README.md#bots)

Tells you which of your credit cards to use for each purchase to get the most points, cash back and perks.

## What you use it for

Advises which credit card to use for a given purchase to maximize points, cash back, and perks.
Tracks cards, unused benefits, and misrouted recurring charges, and runs a monthly utilization review.

## Intended result

The package defines its intended work as:

- Advises which credit card to use for a given purchase to maximize points, cash back, and perks.
- Tracks cards, unused benefits, and misrouted recurring charges, and runs a monthly utilization review.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **benefit-tracker**: Helps when the user asks about unused credits or perks. Source: `skills/credit-card-max/benefit-tracker/SKILL.md`.
- **best-card-for-a-purchase**: Helps when the user asks which card to use for a purchase, a store, or a category. Source: `skills/credit-card-max/best-card-for-a-purchase/SKILL.md`.
- **card-wallet**: Helps when the user adds, drops, or changes a card. Source: `skills/credit-card-max/card-wallet/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/credit-card-max/getting-started/SKILL.md`.
- **monthly-card-rollup**: Helps when the user asks for the monthly review. Source: `skills/credit-card-max/monthly-card-rollup/SKILL.md`.
- **offer-monthly-card-rollup**: Helps after setup or when asked about routines: offer monthly card rollup. Source: `skills/credit-card-max/offer-monthly-card-rollup/SKILL.md`.
- **recurring-charge-check**: Helps when the user lists subscriptions or bills. Source: `skills/credit-card-max/recurring-charge-check/SKILL.md`.
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
  - Monthly card rollup. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-monthly-card-rollup. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I never ask for or store a full card number, CVV, PIN or login.
- I never invent a reward rate, credit, fee or deadline; I say when a rate is unconfirmed.
- I don't give budgeting, debt or investment advice.
- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`credit-card-max.tar.gz`](../packages/credit-card-max.tar.gz).
- Package SHA-256: `22791267cefcc362f9251ac0d4140879e07d439312e468ea6e5f02ef681ab15f`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
