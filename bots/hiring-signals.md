# Hiring Signals

[Back to the catalog](../README.md#bots)

Tracks hiring activity across selected companies and job sources.

## What you use it for

Hiring-trigger specialist: scoped ingestion, normalization, dedupe, fit scoring, account matching, freshness and evidence-backed handoffs. Not general account research, prospect selection or outreach.

## Intended result

The package defines its intended work as:

- Hiring-trigger specialist: scoped ingestion, normalization, dedupe, fit scoring, account matching, freshness and evidence-backed handoffs. Not general account research, prospect selection or outreach.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **hiring-signals**: Helps when a task needs Hiring Signals reference notes. Source: `skills/hiring-signals/SKILL.md`.
- **agent-orchestration**: Helps when coordinate a persistent pinned specialist. Source: `skills/hiring-signals/agent-orchestration/SKILL.md`.
- **hiring-signals**: Helps when connect sources into normalized hiring-signal rows. Source: `skills/hiring-signals/hiring-signals/SKILL.md`.
- **humanizer**: Helps when make drafts sound natural. Source: `skills/hiring-signals/humanizer/SKILL.md`.
- **offer-weekday-hiring-signal-digest**: Helps after setup or when asked about routines. Source: `skills/hiring-signals/offer-weekday-hiring-signal-digest/SKILL.md`.
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
  - Weekday hiring signal digest. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-weekday-hiring-signal-digest. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- No purchases, signatures, POs or financial commitments. Require explicit yes before each send/post/forward, including internal messages and another agent; drafts alone are not permission. Missing tools or stale/partial data must be disclosed. No other-profile reads without consent.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`hiring-signals.tar.gz`](../packages/hiring-signals.tar.gz).
- Package SHA-256: `5ee088a46ed2dbbc20f6bfcda359ded2d62ba9f384bfef33d101946443f8b733`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
