# GTM Connections

[Back to the catalog](../README.md#bots)

Finds credible ways into a target account through mutual contacts, past conversations, shared history, and prior meetings.

## What you use it for

Owns: Relationship-path discovery, connector ranking, intro drafts, status, stalled-request follow-through, and outcome learning.
Does not own: Cold prospecting, invented mutuals, canonical data ownership, sending asks, or general account research.

## Intended result

The package defines its intended work as:

- Owns: Relationship-path discovery, connector ranking, intro drafts, status, stalled-request follow-through, and outcome learning.
- Does not own: Cold prospecting, invented mutuals, canonical data ownership, sending asks, or general account research.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **gtm-connections**: Helps when a task needs GTM Connections reference notes. Source: `skills/gtm-connections/SKILL.md`.
- **agent-orchestration**: Helps when coordinate a persistent pinned specialist. Source: `skills/gtm-connections/agent-orchestration/SKILL.md`.
- **connections-and-intros**: Helps when find evidenced connections into target accounts. Source: `skills/gtm-connections/connections-and-intros/SKILL.md`.
- **humanizer**: Helps when make drafts sound natural. Source: `skills/gtm-connections/humanizer/SKILL.md`.
- **offer-warm-path-follow-through-queue**: Helps after setup or when asked about routines. Source: `skills/gtm-connections/offer-warm-path-follow-through-queue/SKILL.md`.
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
  - Warm-path follow-through queue. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-warm-path-follow-through-queue. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Ask one question at a time when blocked. Never invent facts, numbers, sources, relationships or results. Disclose missing tools/connections; accept paste, CSV, export, URL or files. Require an explicit yes for the exact action before sending, posting, buying or changing external records. Keep drafts local; ordinary workflows never activate routines.
- PUBLIC AND ROUTINE SAFETY
- Never include creator names, private URLs, customer data, tokens, internal channels, or company assumptions. All routines ship disabled. Enabling requires explicit schedule, source scope, private destination, empty-result behavior, and approval boundary. Routines never send externally or silently write.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`gtm-connections.tar.gz`](../packages/gtm-connections.tar.gz).
- Package SHA-256: `13c3b5f7aa2aa5b0382e0ab18ad279875b3f03b847878e816c688fa232f9068c`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
