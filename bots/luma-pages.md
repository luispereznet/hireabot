# Luma Pages

[Back to the catalog](../README.md#bots)

Builds and updates private Luma event pages for field marketers — copy, branding, registration settings, capacity and waitlist, and registration-list hygiene.

## What you use it for

Builds and updates private Luma event pages for field marketers — copy, branding, registration settings, capacity and waitlist, and registration-list hygiene.
Pairs with a Notion docs agent so the event brief and Luma page stay in sync.

## Intended result

The package defines its intended work as:

- Builds and updates private Luma event pages for field marketers — copy, branding, registration settings, capacity and waitlist, and registration-list hygiene.
- Pairs with a Notion docs agent so the event brief and Luma page stay in sync.
- Draft only until the owner explicitly OKs publish. Guest-invite outreach and sales sends are out of scope.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **luma-pages**: Helps when a task needs Luma Pages reference notes. Source: `skills/luma-pages/SKILL.md`.
- **draft-private-event-page**: Helps when drafting or updating a private Luma event page. Source: `skills/luma-pages/draft-private-event-page/SKILL.md`.
- **reconcile-registration-and-brief**: Helps when reconciling a Luma guest list and Notion event brief. Source: `skills/luma-pages/reconcile-registration-and-brief/SKILL.md`.
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
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers, URLs, sources, access, test results or successful actions.
- Sending, posting, buying, publishing or writing remote PRs without an explicit yes covering that action.
- Treating access to a browser, repository or connector as permission to mutate it.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`luma-pages.tar.gz`](../packages/luma-pages.tar.gz).
- Package SHA-256: `315cca8259987391346cba44c3bcdefb7befd8c3e144df99ba791c1f1fac30c5`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
