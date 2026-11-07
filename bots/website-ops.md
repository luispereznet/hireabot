# Website Ops

[Back to the catalog](../README.md#bots)

Website operations and content manager.

## What you use it for

Ships site changes as PRs from your website repo, runs evidence-backed site audits (SEO, content, speed, a11y, CRO, schema), and turns Product Marketer briefs into landing-page PRs with in-chat screenshots.

## Intended result

The package defines its intended work as:

- Ships site changes as PRs from your website repo, runs evidence-backed site audits (SEO, content, speed, a11y, CRO, schema), and turns Product Marketer briefs into landing-page PRs with in-chat screenshots.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **website-ops**: Helps when a task needs Website Ops reference notes. Source: `skills/website-ops/SKILL.md`.
- **connect-accounts**: Helps when a platform account is needed and not yet signed in. Source: `skills/website-ops/connect-accounts/SKILL.md`.
- **content-update**: Helps for copy edits, redirects. Source: `skills/website-ops/content-update/SKILL.md`.
- **evidence-media**: Helps before taking any screenshot. Source: `skills/website-ops/evidence-media/SKILL.md`.
- **html-report**: Use to close an audit or a test drive with a self contained HTML report. Every. Source: `skills/website-ops/html-report/SKILL.md`.
- **landing-page-from-brief**: Helps when a brief arrives from the user. Source: `skills/website-ops/landing-page-from-brief/SKILL.md`.
- **offer-weekly-site-audit**: Helps after setup or when asked about routines: offer weekly site audit. Source: `skills/website-ops/offer-weekly-site-audit/SKILL.md`.
- **ship-a-change**: Use whenever a change to the site has been agreed and needs to land. Branches. Source: `skills/website-ops/ship-a-change/SKILL.md`.
- **site-audit**: Helps when the user asks for a site audit. Source: `skills/website-ops/site-audit/SKILL.md`.
- **website-ops-setup**: Use on the first turn after import. Source: `skills/website-ops/website-ops-setup/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-weekly-site-audit. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`website-ops.tar.gz`](../packages/website-ops.tar.gz).
- Package SHA-256: `7b82792d2308c74484c43b23d1beeab0d42951d3552bf56789e9dc925e01ac99`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
