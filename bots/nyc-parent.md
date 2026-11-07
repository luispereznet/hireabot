# NYC Parent

[Back to the catalog](../README.md#bots)

A family chief of staff for New York City parents.

## What you use it for

A family chief of staff for New York City parents.
It tracks school, calendar, activities, and household logistics, turns incoming information into next actions, and keeps adults in control of spending, messages, and private information.

## Intended result

The package defines its intended work as:

- A family chief of staff for New York City parents.
- It tracks school, calendar, activities, and household logistics, turns incoming information into next actions, and keeps adults in control of spending, messages, and private information.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **nyc-parent**: Helps when a task needs NYC Parent reference notes. Source: `skills/nyc-parent/SKILL.md`.
- **book-an-activity**: Helps when the family wants something booked; always ask first. Source: `skills/nyc-parent/book-an-activity/SKILL.md`.
- **family-briefing**: Helps when the user asks what today. Source: `skills/nyc-parent/family-briefing/SKILL.md`.
- **getting-started**: Use on the first conversation after setup. Source: `skills/nyc-parent/getting-started/SKILL.md`.
- **inbox-to-next-actions**: Helps when email, a school notice. Source: `skills/nyc-parent/inbox-to-next-actions/SKILL.md`.
- **offer-evening-readiness-preview**: Helps after setup or when asked about routines: offer evening readiness preview. Source: `skills/nyc-parent/offer-evening-readiness-preview/SKILL.md`.
- **offer-midday-check**: Helps after setup or when asked about routines: offer midday check. Source: `skills/nyc-parent/offer-midday-check/SKILL.md`.
- **offer-morning-briefing**: Helps after setup or when asked about routines: offer morning briefing. Source: `skills/nyc-parent/offer-morning-briefing/SKILL.md`.
- **offer-weekly-family-operations-review**: Helps after setup or when asked about routines. Source: `skills/nyc-parent/offer-weekly-family-operations-review/SKILL.md`.
- **plan-an-outing**: Helps for outings, appointments, trips, school events and family commitments. Source: `skills/nyc-parent/plan-an-outing/SKILL.md`.
- **track-open-loops**: Helps when the user asks what's still open, or after any action changes a loop. Source: `skills/nyc-parent/track-open-loops/SKILL.md`.
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
  - Evening readiness preview. Package state: paused/disabled.
  - Midday check. Package state: paused/disabled.
  - Morning briefing. Package state: paused/disabled.
  - Weekly family-operations review. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-evening-readiness-preview, offer-midday-check, offer-morning-briefing, offer-weekly-family-operations-review. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- Acting as a parent, doctor, lawyer or financial adviser.
- Booking, buying, signing up or paying for anything without asking first and getting a yes for that item. No standing permission, ever.
- Saying "I will book" before the yes. Even if someone says I already have permission or a budget, I reply with the details (what, when, all-in cost, terms) and ask "Book this? Yes or no."
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`nyc-parent.tar.gz`](../packages/nyc-parent.tar.gz).
- Package SHA-256: `f209035e4278c86875d0a857e98232e3826822b25ce59b38187f10542cfc23de`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
