# Critiquito: Design Critique

[Back to the catalog](../README.md#bots)

Turns a screenshot or Figma link into a design critique with ranked, concrete fixes.

## What you use it for

Turns a screenshot or Figma link into a design critique with ranked, concrete fixes.
I'm Critiquito, and I critique product screens.

## Intended result

The package defines its intended work as:

- Turns a screenshot or Figma link into a design critique with ranked, concrete fixes.
- I'm Critiquito, and I critique product screens.
- When memory already holds your prefs I skip the questions and ask for the screen.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **accessibility-pass**: Helps when the user asks for an accessibility review. Source: `skills/critiquito-design-critique/accessibility-pass/SKILL.md`.
- **compare-versions**: Helps when the user has two or more versions of the same screen. Source: `skills/critiquito-design-critique/compare-versions/SKILL.md`.
- **flow-critique**: Helps when the user hands you two or more screens in sequence. Source: `skills/critiquito-design-critique/flow-critique/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/critiquito-design-critique/getting-started/SKILL.md`.
- **hand-off-the-fixes**: Helps when the user wants findings turned into tickets. Source: `skills/critiquito-design-critique/hand-off-the-fixes/SKILL.md`.
- **offer-weekly-open-fixes**: Helps after setup or when asked about routines: offer weekly open fixes. Source: `skills/critiquito-design-critique/offer-weekly-open-fixes/SKILL.md`.
- **screen-critique**: Helps when the user hands you one screen as a screenshot. Source: `skills/critiquito-design-critique/screen-critique/SKILL.md`.
- **ui-copy-pass**: Helps when the user wants the words on a screen rewritten. Source: `skills/critiquito-design-critique/ui-copy-pass/SKILL.md`.
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
  - Weekly open fixes. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-weekly-open-fixes. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Covers hierarchy, type, color, copy, and accessibility, and never edits your files.
- I put a real critique in front of you within a minute, never "on it" and silence.
- I only judge what I can see, I never invent a hex value or a measurement, and I say when an image is too compressed to measure.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`critiquito-design-critique.tar.gz`](../packages/critiquito-design-critique.tar.gz).
- Package SHA-256: `c8f0cb4096f99a9a6c18fe4cc118944398bd3af557490b4b42060358977ff8d1`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
