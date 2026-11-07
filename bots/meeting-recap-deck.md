# Meeting Recap Deck

[Back to the catalog](../README.md#bots)

Turns your meeting notes into a recap deck in your slide template.

## What you use it for

Turns your meeting notes into a recap deck in your slide template.
I turn the notes from one meeting into a recap the other side can read: what we heard in their own words, next steps with owners and dates, in your slide template.

## Intended result

The package defines its intended work as:

- Turns your meeting notes into a recap deck in your slide template.
- I turn the notes from one meeting into a recap the other side can read: what we heard in their own words, next steps with owners and dates, in your slide template.
- When memory already holds your prefs I skip the questions and open on what matters most today.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **build-the-recap-deck**: Helps when the user hands you notes. Source: `skills/meeting-recap-deck/build-the-recap-deck/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/meeting-recap-deck/getting-started/SKILL.md`.
- **next-steps-to-tickets**: Helps when the user wants the next steps from a recap turned into tickets. Source: `skills/meeting-recap-deck/next-steps-to-tickets/SKILL.md`.
- **offer-friday-recap-roundup**: Helps after setup or when asked about routines: offer friday recap roundup. Source: `skills/meeting-recap-deck/offer-friday-recap-roundup/SKILL.md`.
- **offer-post-meeting-recap-draft**: Helps after setup or when asked about routines: offer post-meeting recap draft. Source: `skills/meeting-recap-deck/offer-post-meeting-recap-draft/SKILL.md`.
- **read-the-slide-template**: Helps when the user links, uploads. Source: `skills/meeting-recap-deck/read-the-slide-template/SKILL.md`.
- **recap-note-without-slides**: Helps when the user has no deck. Source: `skills/meeting-recap-deck/recap-note-without-slides/SKILL.md`.
- **share-the-approved-recap**: Helps when the user says a recap is ready to go out. Source: `skills/meeting-recap-deck/share-the-approved-recap/SKILL.md`.
- **themes-across-meetings**: Helps when the user wants what has come up across several meetings. Source: `skills/meeting-recap-deck/themes-across-meetings/SKILL.md`.
- **update-one-slide**: Helps when the user wants one slide changed. Source: `skills/meeting-recap-deck/update-one-slide/SKILL.md`.
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
  - Friday recap roundup. Package state: paused/disabled.
  - Post-meeting recap draft. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-friday-recap-roundup, offer-post-meeting-recap-draft. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Works from notes you paste or upload, and never invents a quote.
- I'm not a call coach or an account tracker.
- When my setup finishes I don't stop at "ready".
- I put real slide text in front of you within a minute, never "on it" and silence.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`meeting-recap-deck.tar.gz`](../packages/meeting-recap-deck.tar.gz).
- Package SHA-256: `549a3b66c7c86ecedae9c0e38afb37fe6f216f0cb1452947ac813617895ddf09`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
