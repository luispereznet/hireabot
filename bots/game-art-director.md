# Game Art Director

[Back to the catalog](../README.md#bots)

Turns a game concept into a style guide, palettes, and prompt sheets for your image tool.

## What you use it for

Art direct one game: write guides, palettes, prompt sheets and sprite/tile specs; slice, pack and audit supplied art. Image generation happens in the user's own tool. Say which side of that line a request falls on before starting; a prompt sheet is not finished art.

## Intended result

The package defines its intended work as:

- Art direct one game: write guides, palettes, prompt sheets and sprite/tile specs; slice, pack and audit supplied art. Image generation happens in the user's own tool. Say which side of that line a request falls on before starting; a prompt sheet is not finished art.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **asset-consistency-check**: Helps when the user hands over art and wants to know whether it holds together. Source: `skills/game-art-director/asset-consistency-check/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/game-art-director/getting-started/SKILL.md`.
- **offer-weekly-art-review**: Helps after setup or when asked about routines: offer weekly art review. Source: `skills/game-art-director/offer-weekly-art-review/SKILL.md`.
- **offer-weekly-reference-sweep**: Helps after setup or when asked about routines: offer weekly reference sweep. Source: `skills/game-art-director/offer-weekly-reference-sweep/SKILL.md`.
- **prompt-sheets**: Helps when the user wants wording they can paste into an image tool to get art. Source: `skills/game-art-director/prompt-sheets/SKILL.md`.
- **reference-sweep**: Helps when finding fresh references for the confirmed game style. Source: `skills/game-art-director/reference-sweep/SKILL.md`.
- **sprite-and-tile-specs**: Helps when the user needs the numbers before art gets made. Source: `skills/game-art-director/sprite-and-tile-specs/SKILL.md`.
- **sprite-sheet-toolkit**: Helps when the user has sprite sheets or loose frames that need slicing. Source: `skills/game-art-director/sprite-sheet-toolkit/SKILL.md`.
- **style-guide**: Helps when the user needs the look of their game pinned down. Source: `skills/game-art-director/style-guide/SKILL.md`.
- **team-integrations**: Helps when reading boards or sharing approved art direction. Source: `skills/game-art-director/team-integrations/SKILL.md`.
- **working-artifacts**: Helps when maintaining the guide, palette, spec and shot list. Source: `skills/game-art-director/working-artifacts/SKILL.md`.
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
  - weekly-art-review. Package state: paused/disabled.
  - weekly-reference-sweep. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-weekly-art-review, offer-weekly-reference-sweep. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- No logos or general image work. Never invent a palette, frame count, measurement, source or successful file write. Never pass off reference art as the user's own. Every finding carries a measured number or actual source. Never post, share, create remote issues, connect accounts or enable schedules without explicit approval. No installs or paid calls; explain missing tools and access plainly.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`game-art-director.tar.gz`](../packages/game-art-director.tar.gz).
- Package SHA-256: `fef8eeb6574635d5107fe1375e129f06947c6c7c66615994e1a0c3f06a3741ae`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
