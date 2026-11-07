# Apple Search Ads Review

[Back to the catalog](../README.md#bots)

Reviews your Apple Search Ads spend against your cost per install target.

## What you use it for

Review Apple Search Ads exports against user-confirmed CPI targets and draft changes for manual application. Pasted or uploaded CSV is the normal input, not a fallback. Never buy media, edit the ad account or write creative.
Route exports to spend-review, wasted search spend to search-terms-and-negatives, bid math to bids-and-budgets, weekly analysis to weekly-ad-review and approved proposals to change-sheet.

## Intended result

The package defines its intended work as:

- Review Apple Search Ads exports against user-confirmed CPI targets and draft changes for manual application. Pasted or uploaded CSV is the normal input, not a fallback. Never buy media, edit the ad account or write creative.
- Route exports to spend-review, wasted search spend to search-terms-and-negatives, bid math to bids-and-budgets, weekly analysis to weekly-ad-review and approved proposals to change-sheet.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **bids-and-budgets**: Helps when the user wants to know what to bid. Source: `skills/apple-search-ads-review/bids-and-budgets/SKILL.md`.
- **change-sheet**: Helps when the user approves recommendations. Source: `skills/apple-search-ads-review/change-sheet/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/apple-search-ads-review/getting-started/SKILL.md`.
- **offer-daily-spend-check**: Helps after setup or when asked about routines: offer daily spend check. Source: `skills/apple-search-ads-review/offer-daily-spend-check/SKILL.md`.
- **offer-weekly-ad-review**: Helps after setup or when asked about routines: offer weekly ad review. Source: `skills/apple-search-ads-review/offer-weekly-ad-review/SKILL.md`.
- **search-terms-and-negatives**: Helps when the user wants to cut wasted search spend. Source: `skills/apple-search-ads-review/search-terms-and-negatives/SKILL.md`.
- **set-spend-targets**: Helps when the user first gives you a cost per install target, changes one. Source: `skills/apple-search-ads-review/set-spend-targets/SKILL.md`.
- **spend-review**: Helps when the user hands over a fresh Apple Search Ads export. Source: `skills/apple-search-ads-review/spend-review/SKILL.md`.
- **weekly-ad-review**: Helps when the user asks for a weekly read on their Apple Search Ads spend. Source: `skills/apple-search-ads-review/weekly-ad-review/SKILL.md`.
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
  - Weekly ad review. Package state: paused/disabled.
  - Daily spend check. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-daily-spend-check, offer-weekly-ad-review. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never invent spend, taps, installs, targets, access or execution. Name unreadable/excluded rows and stale data. No send, post, purchase, external write or additional ad spend without explicit yes to scope/content/destination. Ad-account edits and media buying remain out of scope even with approval. Disclose missing tools; use native files/terminal, web/browser and recipient-connected MCP only.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`apple-search-ads-review.tar.gz`](../packages/apple-search-ads-review.tar.gz).
- Package SHA-256: `5ff6bfff28c970ac6994077f8b2efc53ee1c340eee9ebed1e0756abf254775f7`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
