# Customer Proof Desk

[Back to the catalog](../README.md#bots)

Turns call notes and transcripts into case studies, testimonials, and proof points.

## What you use it for

Turns call notes and transcripts into case studies, testimonials, and proof points.
Quotes stay word for word from what you paste, and nothing publishes without your yes.

## Intended result

The package defines its intended work as:

- Turns call notes and transcripts into case studies, testimonials, and proof points.
- Quotes stay word for word from what you paste, and nothing publishes without your yes.
- I turn call notes, transcripts, and customer email into case studies, testimonials, and proof points, and every quote stays traceable to its source.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **add-sources-to-the-proof-bank**: Helps when the user pastes or uploads a call transcript. Source: `skills/customer-proof-desk/add-sources-to-the-proof-bank/SKILL.md`.
- **build-a-deal-proof-one-pager**: Helps when the user needs the proof for one prospect. Source: `skills/customer-proof-desk/build-a-deal-proof-one-pager/SKILL.md`.
- **check-a-draft-against-the-bank**: Helps when the user pastes a case study. Source: `skills/customer-proof-desk/check-a-draft-against-the-bank/SKILL.md`.
- **get-the-customer-s-approval**: Helps when a quote, name, logo. Source: `skills/customer-proof-desk/get-the-customer-s-approval/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/customer-proof-desk/getting-started/SKILL.md`.
- **lay-out-the-case-study**: Helps when a finished case study needs a page layout. Source: `skills/customer-proof-desk/lay-out-the-case-study/SKILL.md`.
- **mine-a-batch-of-calls**: Helps when the user hands over several transcripts. Source: `skills/customer-proof-desk/mine-a-batch-of-calls/SKILL.md`.
- **offer-monthly-proof-refresh**: Helps after setup or when asked about routines: offer monthly proof refresh. Source: `skills/customer-proof-desk/offer-monthly-proof-refresh/SKILL.md`.
- **offer-weekly-proof-roundup**: Helps after setup or when asked about routines: offer weekly proof roundup. Source: `skills/customer-proof-desk/offer-weekly-proof-roundup/SKILL.md`.
- **pull-proof-for-a-claim**: Helps when the user needs the right quote. Source: `skills/customer-proof-desk/pull-proof-for-a-claim/SKILL.md`.
- **run-the-case-study-pipeline**: Helps when the user wants the customers ready to write. Source: `skills/customer-proof-desk/run-the-case-study-pipeline/SKILL.md`.
- **testimonials-and-pull-quotes**: Helps when the user needs a short testimonial. Source: `skills/customer-proof-desk/testimonials-and-pull-quotes/SKILL.md`.
- **write-a-case-study**: Helps when the user wants a full customer case study or success story written. Source: `skills/customer-proof-desk/write-a-case-study/SKILL.md`.
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
- Separate routine-offer instructions are included: offer-monthly-proof-refresh, offer-weekly-proof-roundup. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I'm not a copywriter, a CRM, or a research tool.
- When my setup finishes I don't stop at "ready".
- I put a real draft or a real pull in front of you within a minute, never "on it" and silence.
- I never invent a customer, a number, a logo, or a quote.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`customer-proof-desk.tar.gz`](../packages/customer-proof-desk.tar.gz).
- Package SHA-256: `a21ddea840cbe2e76a43299dac80d835fc9846174aefae7adb6cd0d2e15a179c`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
