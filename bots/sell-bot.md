# Sell Bot

[Back to the catalog](../README.md#bots)

Works your whole customer journey: outreach in your voice, booked calls with prep and follow-ups, proposals and contracts, then activation, support and billing

## What you use it for

Works your whole customer journey: outreach in your voice, booked calls with prep and follow-ups, proposals and contracts, then activation, support and billing answers, and expansion.
Drafts everything for your review and sends only what you approve, one message at a time.

## Intended result

The package defines its intended work as:

- Works your whole customer journey: outreach in your voice, booked calls with prep and follow-ups, proposals and contracts, then activation, support and billing answers, and expansion.
- Drafts everything for your review and sends only what you approve, one message at a time.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **sell-bot**: Helps when a task needs Sell Bot reference notes. Source: `skills/sell-bot/SKILL.md`.
- **account-watch**: Helps for credit runway, expansion signals. Source: `skills/sell-bot/account-watch/SKILL.md`.
- **accounts**: Helps for setup.md, ledgers, account files, stages, number sources, and teammates. Source: `skills/sell-bot/accounts/SKILL.md`.
- **call-wrap**: Helps after watched calls: learnings, asks, signals, follow-ups, digest. Source: `skills/sell-bot/call-wrap/SKILL.md`.
- **draft-email**: Helps for every email, sending after a yes, the sent check, and the Friday review. Source: `skills/sell-bot/draft-email/SKILL.md`.
- **follow-through**: Helps for check-ins, wow moments, feature series, and the Monday impact read. Source: `skills/sell-bot/follow-through/SKILL.md`.
- **offer-confirm-notes**: Helps after setup or when asked about routines: offer confirm notes. Source: `skills/sell-bot/offer-confirm-notes/SKILL.md`.
- **offer-daily-account-watch**: Helps after setup or when asked about routines: offer daily account watch. Source: `skills/sell-bot/offer-daily-account-watch/SKILL.md`.
- **offer-daily-follow-through**: Helps after setup or when asked about routines: offer daily follow-through. Source: `skills/sell-bot/offer-daily-follow-through/SKILL.md`.
- **offer-daily-prospect-follow-up**: Helps after setup or when asked about routines: offer daily prospect follow-up. Source: `skills/sell-bot/offer-daily-prospect-follow-up/SKILL.md`.
- **offer-evening-wrap-up**: Helps after setup or when asked about routines: offer evening wrap-up. Source: `skills/sell-bot/offer-evening-wrap-up/SKILL.md`.
- **offer-friday-writing-review**: Helps after setup or when asked about routines: offer friday writing review. Source: `skills/sell-bot/offer-friday-writing-review/SKILL.md`.
- **offer-launch-heads-ups**: Helps after setup or when asked about routines: offer launch heads-ups. Source: `skills/sell-bot/offer-launch-heads-ups/SKILL.md`.
- **offer-monday-impact-read**: Helps after setup or when asked about routines: offer monday impact read. Source: `skills/sell-bot/offer-monday-impact-read/SKILL.md`.
- **offer-morning-prep**: Helps after setup or when asked about routines: offer morning prep. Source: `skills/sell-bot/offer-morning-prep/SKILL.md`.
- **offer-weekly-pipeline-review**: Helps after setup or when asked about routines: offer weekly pipeline review. Source: `skills/sell-bot/offer-weekly-pipeline-review/SKILL.md`.
- **prep-page**: Helps before a watched call: prep page and confirm note. Source: `skills/sell-bot/prep-page/SKILL.md`.
- **proposal-desk**: Helps for proposals, quotes, expansion deals, contracts, and won or lost. Source: `skills/sell-bot/proposal-desk/SKILL.md`.
- **schedule**: Use to book, move, or cancel a call. Source: `skills/sell-bot/schedule/SKILL.md`.
- **sell-setup**: Use on the first conversation, to resume setup, or to set up again. Source: `skills/sell-bot/sell-setup/SKILL.md`.
- **support-desk**: Helps for customer questions, billing traces, bugs, and fix heads-ups. Source: `skills/sell-bot/support-desk/SKILL.md`.
- **watch-on-x**: Use to find X handles, give follow links, and read posts. Source: `skills/sell-bot/watch-on-x/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-confirm-notes, offer-daily-account-watch, offer-daily-follow-through, offer-daily-prospect-follow-up, offer-evening-wrap-up, offer-friday-writing-review, offer-launch-heads-ups, offer-monday-impact-read, offer-morning-prep, offer-weekly-pipeline-review. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Inventing facts, numbers or sources.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`sell-bot.tar.gz`](../packages/sell-bot.tar.gz).
- Package SHA-256: `c9cd1df149330b673a3f2b516bc73192dfc987153b469952fbd595f099a02e6f`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
