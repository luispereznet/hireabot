# Talent Discovery

[Back to the catalog](../README.md#bots)

Finds candidates for open roles that match your criteria and aren't already in your ATS.

## What you use it for

Finds candidates for open roles that match your criteria and aren't already in your ATS.
I source candidates for one open role at a time and keep a shortlist you can act on.

## Intended result

The package defines its intended work as:

- Finds candidates for open roles that match your criteria and aren't already in your ATS.
- I source candidates for one open role at a time and keep a shortlist you can act on.
- When memory already holds your bar, I skip the questions and open with the next batch.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **dedupe-against-your-pipeline**: Helps when the user already has candidates in play. Source: `skills/talent-discovery/dedupe-against-your-pipeline/SKILL.md`.
- **draft-outreach**: Helps when the user picks a candidate to contact. Source: `skills/talent-discovery/draft-outreach/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/talent-discovery/getting-started/SKILL.md`.
- **lookalike-search**: Helps when the user names someone whose work is the benchmark, links a profile. Source: `skills/talent-discovery/lookalike-search/SKILL.md`.
- **offer-daily-candidate-batch**: Helps after setup or when asked about routines: offer daily candidate batch. Source: `skills/talent-discovery/offer-daily-candidate-batch/SKILL.md`.
- **offer-weekly-sourcing-recap**: Helps after setup or when asked about routines: offer weekly sourcing recap. Source: `skills/talent-discovery/offer-weekly-sourcing-recap/SKILL.md`.
- **read-the-role**: Helps when the user pastes or links a job description. Source: `skills/talent-discovery/read-the-role/SKILL.md`.
- **role-market-read**: Helps when the user asks how hard this search will be. Source: `skills/talent-discovery/role-market-read/SKILL.md`.
- **share-the-shortlist**: Helps when the user wants to send the shortlist or the bar to their team. Source: `skills/talent-discovery/share-the-shortlist/SKILL.md`.
- **shortlist-review**: Helps when the user wants to go through the shortlist. Source: `skills/talent-discovery/shortlist-review/SKILL.md`.
- **source-a-batch**: Helps when the user asks for candidates. Source: `skills/talent-discovery/source-a-batch/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-daily-candidate-batch, offer-weekly-sourcing-recap. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I don't screen inbound applicants, run your ATS, or decide who to hire.
- When my setup finishes I don't stop at "ready".
- I put real candidate cards in front of you inside a minute, never "on it" and silence.
- I never record or guess age, gender, race, religion, health, or family status, and never invent a person or their interest in your role.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`talent-discovery.tar.gz`](../packages/talent-discovery.tar.gz).
- Package SHA-256: `a8da76ad0c2347840c686b426fff97b747db5d9e6810a4a56a72087d4c308e5b`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
