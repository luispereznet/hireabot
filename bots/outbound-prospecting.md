# Outbound Prospecting

[Back to the catalog](../README.md#bots)

Finds prospects that match your ideal customer, then drafts a first message to each one.

## What you use it for

Finds prospects that match your ideal customer, then drafts a first message to each one.
Every name is researched on the public web, and nothing sends without your yes.

## Intended result

The package defines its intended work as:

- Finds prospects that match your ideal customer, then drafts a first message to each one.
- Every name is researched on the public web, and nothing sends without your yes.
- I build outbound prospect lists from the public web and write the first message to each name.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **build-the-target-list**: Helps when the user first describes who they sell to. Source: `skills/outbound-prospecting/build-the-target-list/SKILL.md`.
- **draft-a-first-touch**: Helps when the user wants the opening message to a prospect or a batch of them. Source: `skills/outbound-prospecting/draft-a-first-touch/SKILL.md`.
- **draft-a-follow-up**: Helps when the user says a first touch went out and got no reply. Source: `skills/outbound-prospecting/draft-a-follow-up/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/outbound-prospecting/getting-started/SKILL.md`.
- **handle-a-reply**: Helps when a prospect answers. Source: `skills/outbound-prospecting/handle-a-reply/SKILL.md`.
- **offer-friday-prospecting-recap**: Helps after setup or when asked about routines: offer friday prospecting recap. Source: `skills/outbound-prospecting/offer-friday-prospecting-recap/SKILL.md`.
- **offer-monday-list-top-up**: Helps after setup or when asked about routines: offer monday list top-up. Source: `skills/outbound-prospecting/offer-monday-list-top-up/SKILL.md`.
- **offer-weekday-draft-batch**: Helps after setup or when asked about routines: offer weekday draft batch. Source: `skills/outbound-prospecting/offer-weekday-draft-batch/SKILL.md`.
- **research-a-prospect**: Helps when a row needs research before anyone writes to it. Source: `skills/outbound-prospecting/research-a-prospect/SKILL.md`.
- **sharpen-what-is-working**: Helps when enough messages have gone out to read a pattern, when replies dry up. Source: `skills/outbound-prospecting/sharpen-what-is-working/SKILL.md`.
- **weekly-prospecting-recap**: Helps when the user asks how prospecting is going. Source: `skills/outbound-prospecting/weekly-prospecting-recap/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-friday-prospecting-recap, offer-monday-list-top-up, offer-weekday-draft-batch. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I don't work inbound leads, run your CRM, or manage a sequence past the first four touches.
- When my setup finishes I don't stop at "ready".
- I put a real list or a real draft in front of you inside a minute, never "on it" and silence.
- I never invent a person, a title, an email address, a funding round, or a quote.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`outbound-prospecting.tar.gz`](../packages/outbound-prospecting.tar.gz).
- Package SHA-256: `f0b3e5ade910fea42e8b38515f8e8d123027dccbf25f35d0198fba039f45f6ae`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
