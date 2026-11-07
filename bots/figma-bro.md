# figma bro

[Back to the catalog](../README.md#bots)

Turns a Figma frame into a build spec, and audits your components, tokens, and motion.

## What you use it for

Turns a Figma frame into a build spec, and audits your components, tokens, and motion.
Builds screens from a brief too, and works from a pasted link when Figma isn't connected.

## Intended result

The package defines its intended work as:

- Turns a Figma frame into a build spec, and audits your components, tokens, and motion.
- Builds screens from a brief too, and works from a pasted link when Figma isn't connected.
- When memory already holds your prefs I skip the questions and offer what is most useful today.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **build-a-screen-from-a-brief**: Helps when the user wants a screen made rather than read. Source: `skills/figma-bro/build-a-screen-from-a-brief/SKILL.md`.
- **component-library-audit**: Helps when the user asks about the health of their component library. Source: `skills/figma-bro/component-library-audit/SKILL.md`.
- **design-to-code-handoff-notes**: Helps when a frame is going to an engineer. Source: `skills/figma-bro/design-to-code-handoff-notes/SKILL.md`.
- **design-token-audit**: Helps when the user asks about their variables, styles, or design tokens. Source: `skills/figma-bro/design-token-audit/SKILL.md`.
- **file-structure-cleanup-plan**: Helps when a frame's structure fights the design. Source: `skills/figma-bro/file-structure-cleanup-plan/SKILL.md`.
- **frame-to-build-spec**: Helps when the user wants a spec for a screen or component. Source: `skills/figma-bro/frame-to-build-spec/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/figma-bro/getting-started/SKILL.md`.
- **motion-and-prototype-notes**: Helps when a screen has movement to spec or review. Source: `skills/figma-bro/motion-and-prototype-notes/SKILL.md`.
- **offer-ready-for-dev-sweep**: Helps after setup or when asked about routines: offer ready for dev sweep. Source: `skills/figma-bro/offer-ready-for-dev-sweep/SKILL.md`.
- **offer-weekly-library-check**: Helps after setup or when asked about routines: offer weekly library check. Source: `skills/figma-bro/offer-weekly-library-check/SKILL.md`.
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
- Separate routine-offer instructions are included: offer-ready-for-dev-sweep, offer-weekly-library-check. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- No filler openers, and I never mention how I was set up.
- When my setup finishes I don't stop at "ready".
- I show a real spec, table, or plan inside a minute, never "on it" and silence.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`figma-bro.tar.gz`](../packages/figma-bro.tar.gz).
- Package SHA-256: `97eb1a53c5abce595b501beb0818e869776bceb6c621a5ea50b52f1a45922bab`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
