# AI Search Visibility

[Back to the catalog](../README.md#bots)

Checks whether AI assistants and Google recommend you, and who they name instead.

## What you use it for

Check whether AI assistants and search results recommend the user's company on real buyer questions, and name who appears instead. Use the prompt list, visibility check, pasted capture, weekly brief, citation audit, scoreboard and fix-drafting skills. Login-only answers supplied by the user are normal evidence, with explicit provenance.

## Intended result

The package defines its intended work as:

- Check whether AI assistants and search results recommend the user's company on real buyer questions, and name who appears instead. Use the prompt list, visibility check, pasted capture, weekly brief, citation audit, scoreboard and fix-drafting skills. Login-only answers supplied by the user are normal evidence, with explicit provenance.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **ai-search-visibility**: Helps when routing visibility work, storage or optional integrations. Source: `skills/ai-search-visibility/SKILL.md`.
- **build-the-prompt-list**: Helps when the user first describes what they sell, adds or drops a prompt. Source: `skills/ai-search-visibility/build-the-prompt-list/SKILL.md`.
- **capture-a-pasted-answer**: Helps when the user pastes what an assistant told them. Source: `skills/ai-search-visibility/capture-a-pasted-answer/SKILL.md`.
- **citation-source-audit**: Helps when the user asks why they are not showing up. Source: `skills/ai-search-visibility/citation-source-audit/SKILL.md`.
- **draft-the-fix**: Helps when the user picks something off the fix list and wants the page. Source: `skills/ai-search-visibility/draft-the-fix/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/ai-search-visibility/getting-started/SKILL.md`.
- **offer-top-prompt-spot-check**: Helps after setup or when asked about routines: offer top prompt spot check. Source: `skills/ai-search-visibility/offer-top-prompt-spot-check/SKILL.md`.
- **offer-weekly-visibility-brief**: Helps after setup or when asked about routines: offer weekly visibility brief. Source: `skills/ai-search-visibility/offer-weekly-visibility-brief/SKILL.md`.
- **run-a-visibility-check**: Helps when you need to see who AI assistants. Source: `skills/ai-search-visibility/run-a-visibility-check/SKILL.md`.
- **share-of-answer-comparison**: Helps when the user asks how often they come up compared to rivals. Source: `skills/ai-search-visibility/share-of-answer-comparison/SKILL.md`.
- **weekly-visibility-brief**: Helps when the user asks how their visibility changed. Source: `skills/ai-search-visibility/weekly-visibility-brief/SKILL.md`.
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
  - weekly-visibility-brief. Package state: paused/disabled.
  - top-prompt-spot-check. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-top-prompt-spot-check, offer-weekly-visibility-brief. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Do not diff competitor pricing or product pages, run ads or publish content. Draft by default; obtain explicit consent for sending, posting, account connections and schedule changes. Never invent claims, quotes, links, counts or successful checks. Each finding has exact evidence and a source link; for missing public links say unavailable and retain a local evidence reference. Absence is scoped to a complete capture, not an invented quotation. No plugin installs or paid calls.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`ai-search-visibility.tar.gz`](../packages/ai-search-visibility.tar.gz).
- Package SHA-256: `a1594a5b06805c33e4a4da02e27c0ee5b8f047e951991709a076d1f39f1826ff`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
