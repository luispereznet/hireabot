# SEO & AEO Desk

[Back to the catalog](../README.md#bots)

Turns your keywords into content ideas and writer-ready briefs for search and AI answers.

## What you use it for

Turns your keywords into content ideas and writer-ready briefs for search and AI answers.
Works from a pasted keyword list or your Search Console.

## Intended result

The package defines its intended work as:

- Turns your keywords into content ideas and writer-ready briefs for search and AI answers.
- Works from a pasted keyword list or your Search Console.
- I run the search side of your content program.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **answer-engine-question-map**: Helps when the user wants to know what people ask AI assistants in their space. Source: `skills/seo-aeo-desk/answer-engine-question-map/SKILL.md`.
- **extra-recurring-checks**: Helps when the user asks for another scheduled check beyond the three routines. Source: `skills/seo-aeo-desk/extra-recurring-checks/SKILL.md`.
- **getting-started**: Use on the first conversation after setup, or whenever memory has no user prefs. Source: `skills/seo-aeo-desk/getting-started/SKILL.md`.
- **keyword-and-question-research**: Helps when the user pastes keywords, names a topic, gives you only a site. Source: `skills/seo-aeo-desk/keyword-and-question-research/SKILL.md`.
- **offer-content-ideas-digest**: Helps after setup or when asked about routines: offer content ideas digest. Source: `skills/seo-aeo-desk/offer-content-ideas-digest/SKILL.md`.
- **offer-topic-watch**: Helps after setup or when asked about routines: offer topic watch. Source: `skills/seo-aeo-desk/offer-topic-watch/SKILL.md`.
- **offer-weekly-search-report**: Helps after setup or when asked about routines: offer weekly search report. Source: `skills/seo-aeo-desk/offer-weekly-search-report/SKILL.md`.
- **page-audit-and-refresh-plan**: Helps when a page is slipping. Source: `skills/seo-aeo-desk/page-audit-and-refresh-plan/SKILL.md`.
- **weekly-search-report**: Helps when the user asks how their pages are doing in search. Source: `skills/seo-aeo-desk/weekly-search-report/SKILL.md`.
- **writer-content-brief**: Helps when the user picks a topic. Source: `skills/seo-aeo-desk/writer-content-brief/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-content-ideas-digest, offer-topic-watch, offer-weekly-search-report. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- I don't write the finished article, I don't publish anything, and I'm not a general marketing strategist.
- No filler openers.
- When my setup finishes I don't stop at "ready".
- I put a real ideas list, brief, or search read in front of you inside a minute, never "on it" and silence.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`seo-aeo-desk.tar.gz`](../packages/seo-aeo-desk.tar.gz).
- Package SHA-256: `ccd992e74c13314f2f9bbcf0719c2eb12a0659487ae40b0c8f4e1fbd700dcf70`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
