# Event Producer

[Back to the catalog](../README.md#bots)

Turns your event details into a run of show, guest list, and day-of checklist.

## What you use it for

Turns your event details into a run of show, guest list, and day-of checklist.
When memory already holds your event I skip the questions and open with how many days out you are and what is unconfirmed.

## Intended result

The package defines its intended work as:

- Turns your event details into a run of show, guest list, and day-of checklist.
- When memory already holds your event I skip the questions and open with how many days out you are and what is unconfirmed.
- Timing goes to the run of show, suppliers to the vendor tracker, people to the guest list and guest travel, the day itself to the day-of checklist, and afterwards to the recap.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **build-the-event-brief**: Helps when the user starts a new event. Source: `skills/event-producer/build-the-event-brief/SKILL.md`.
- **day-of-checklist**: Use in the last week before the event. Source: `skills/event-producer/day-of-checklist/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/event-producer/getting-started/SKILL.md`.
- **guest-list-and-invites**: Helps when building the invite list. Source: `skills/event-producer/guest-list-and-invites/SKILL.md`.
- **guest-travel-and-hotels**: Helps when guests are travelling in. Source: `skills/event-producer/guest-travel-and-hotels/SKILL.md`.
- **offer-day-of-brief**: Helps after setup or when asked about routines: offer day-of brief. Source: `skills/event-producer/offer-day-of-brief/SKILL.md`.
- **offer-event-countdown-check**: Helps after setup or when asked about routines: offer event countdown check. Source: `skills/event-producer/offer-event-countdown-check/SKILL.md`.
- **offer-post-event-recap-draft**: Helps after setup or when asked about routines: offer post-event recap draft. Source: `skills/event-producer/offer-post-event-recap-draft/SKILL.md`.
- **post-event-recap**: Use in the days after the event, or when the recap routine runs. Source: `skills/event-producer/post-event-recap/SKILL.md`.
- **run-of-show**: Helps when the user needs the minute-by-minute schedule for the event day. Source: `skills/event-producer/run-of-show/SKILL.md`.
- **vendor-and-venue-tracker**: Helps when tracking venue, catering. Source: `skills/event-producer/vendor-and-venue-tracker/SKILL.md`.
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
  - Event countdown check. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-day-of-brief, offer-event-countdown-check, offer-post-event-recap-draft. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Tracks vendors, guests, dietary needs, and travel, and never sends a message without you.
- I don't take in requests for events that don't exist yet, and I don't book or pay anyone.
- When my setup finishes I don't stop at "ready".
- I put a real plan or tracker in front of you inside a minute, never "on it" and silence.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`event-producer.tar.gz`](../packages/event-producer.tar.gz).
- Package SHA-256: `40de278b64b33519a95aa690ba3b9fdfe1b363b514ee7121a50f88f2f0299856`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
