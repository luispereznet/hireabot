# Recruiting Coordinator

[Back to the catalog](../README.md#bots)

Schedules interview loops, preps your interviewers, and chases what's stalled.

## What you use it for

Schedules interview loops, preps your interviewers, and chases what's stalled.
I coordinate hiring for one recruiter or hiring manager: loops scheduled, interviewers prepped, follow-ups chased.

## Intended result

The package defines its intended work as:

- Schedules interview loops, preps your interviewers, and chases what's stalled.
- I coordinate hiring for one recruiter or hiring manager: loops scheduled, interviewers prepped, follow-ups chased.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **build-the-hiring-tracker**: Helps when the user first hands over roles, candidates, or scheduled loops. Source: `skills/recruiting-coordinator/build-the-hiring-tracker/SKILL.md`.
- **candidate-message-drafts**: Helps when the user needs a message written to a candidate or an interviewer. Source: `skills/recruiting-coordinator/candidate-message-drafts/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/recruiting-coordinator/getting-started/SKILL.md`.
- **interviewer-coaching**: Helps when the user wants to sharpen their own interviewing. Source: `skills/recruiting-coordinator/interviewer-coaching/SKILL.md`.
- **interviewer-prep-packet**: Helps when interviews are coming up and the panel needs a packet. Source: `skills/recruiting-coordinator/interviewer-prep-packet/SKILL.md`.
- **offer-afternoon-loop-check**: Helps after setup or when asked about routines: offer afternoon loop check. Source: `skills/recruiting-coordinator/offer-afternoon-loop-check/SKILL.md`.
- **offer-candidate-reply-drafts**: Helps after setup or when asked about routines: offer candidate reply drafts. Source: `skills/recruiting-coordinator/offer-candidate-reply-drafts/SKILL.md`.
- **offer-daily-hiring-brief**: Helps after setup or when asked about routines: offer daily hiring brief. Source: `skills/recruiting-coordinator/offer-daily-hiring-brief/SKILL.md`.
- **offer-evening-interview-prep**: Helps after setup or when asked about routines: offer evening interview prep. Source: `skills/recruiting-coordinator/offer-evening-interview-prep/SKILL.md`.
- **offer-interview-coaching-review**: Helps after setup or when asked about routines: offer interview coaching review. Source: `skills/recruiting-coordinator/offer-interview-coaching-review/SKILL.md`.
- **offer-urgent-thread-check**: Helps after setup or when asked about routines: offer urgent thread check. Source: `skills/recruiting-coordinator/offer-urgent-thread-check/SKILL.md`.
- **offer-weekly-pipeline-review**: Helps after setup or when asked about routines: offer weekly pipeline review. Source: `skills/recruiting-coordinator/offer-weekly-pipeline-review/SKILL.md`.
- **run-the-debrief**: Helps after a loop finishes and the user needs the scorecards collated. Source: `skills/recruiting-coordinator/run-the-debrief/SKILL.md`.
- **schedule-an-interview-loop**: Helps when the user needs to book. Source: `skills/recruiting-coordinator/schedule-an-interview-loop/SKILL.md`.
- **stalled-loop-follow-ups**: Helps when the user asks what is stuck. Source: `skills/recruiting-coordinator/stalled-loop-follow-ups/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- Shipped routine definitions:
  - Afternoon loop check. Package state: paused/disabled.
  - Candidate reply drafts. Package state: paused/disabled.
  - Daily hiring brief. Package state: paused/disabled.
  - Evening interview prep. Package state: paused/disabled.
  - Interview coaching review. Package state: paused/disabled.
  - Urgent thread check. Package state: paused/disabled.
  - Weekly pipeline review. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-afternoon-loop-check, offer-candidate-reply-drafts, offer-daily-hiring-brief, offer-evening-interview-prep, offer-interview-coaching-review, offer-urgent-thread-check, offer-weekly-pipeline-review. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Works from your calendar or a pasted list, and never emails a candidate without you.
- I don't source candidates, decide who to hire, or coach candidates.
- I put a real slate, packet, or draft in front of you within a minute, never "on it" and silence.
- I work only from what you give me and public professional profiles, and never record a candidate's age, gender, race, religion, health, or family situation.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`recruiting-coordinator.tar.gz`](../packages/recruiting-coordinator.tar.gz).
- Package SHA-256: `81c6a21eaadb2ad8e9524722e5074c5ad1f4c4075f773063a734f0b85554654a`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
