# Webby

[Back to the catalog](../README.md#bots)

Website, newsletter, and public dashboard admin you configure for your own site. Create-only. Ships rather than plans.

## What you use it for

I am a website, newsletter, and public dashboard admin the user configures for their own site.
I write long-form exclusives from a playlist or transcripts they name, short daily digests from their social pulse, newsletter emails for both, and a public weekday dashboard from a data source they name.

## Intended result

The package defines its intended work as:

- I am a website, newsletter, and public dashboard admin the user configures for their own site.
- I write long-form exclusives from a playlist or transcripts they name, short daily digests from their social pulse, newsletter emails for both, and a public weekday dashboard from a data source they name.
- Create-only. Cost-lean. I ship rather than plan.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **offer-close-dashboard**: Helps after setup or when asked about routines: offer the close dashboard. Source: `skills/webby/offer-close-dashboard/SKILL.md`.
- **offer-daily-digest**: Helps after setup or when asked about routines: offer the daily digest. Source: `skills/webby/offer-daily-digest/SKILL.md`.
- **offer-daily-exclusive**: Helps after setup or when asked about routines: offer the daily exclusive. Source: `skills/webby/offer-daily-exclusive/SKILL.md`.
- **offer-post-fill-dashboard**: Helps after setup or when asked about routines: offer the post-fill dashboard. Source: `skills/webby/offer-post-fill-dashboard/SKILL.md`.
- **offer-site-pr-follow-up**: Helps after setup or when asked about routines: offer the site PR follow-up. Source: `skills/webby/offer-site-pr-follow-up/SKILL.md`.
- **offer-weekday-dashboard**: Helps after setup or when asked about routines: offer the weekday dashboard. Source: `skills/webby/offer-weekday-dashboard/SKILL.md`.
- **send-newsletter**: Helps when emailing an exclusive or yesterday's digest. Source: `skills/webby/send-newsletter/SKILL.md`.
- **ship-dashboard**: Helps when shipping the public weekday dashboard from the user's data source. Source: `skills/webby/ship-dashboard/SKILL.md`.
- **ship-site**: Helps when pushing site content and running the user's deploy. Source: `skills/webby/ship-site/SKILL.md`.
- **site-scripts**: Helps when running or reinstalling the site.py helper. Source: `skills/webby/site-scripts/SKILL.md`.
- **site-setup**: Helps when this is the first run or the user asks to set up Webby again. Source: `skills/webby/site-setup/SKILL.md`.
- **strip-ai-isms**: Helps when drafting or editing site, script, digest, or idea copy. Source: `skills/webby/strip-ai-isms/SKILL.md`.
- **write-digest**: Helps when writing today's short social-pulse digest. Source: `skills/webby/write-digest/SKILL.md`.
- **write-exclusive**: Helps when writing a long-form exclusive from YouTube or transcripts. Source: `skills/webby/write-exclusive/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.
- **site.py**: Organizes website settings, exclusive articles, daily digests, newsletter send records, and dashboard notes locally. Source: `skills/webby/site-scripts/scripts/site.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.
- Separate routine-offer instructions are included: offer-close-dashboard, offer-daily-digest, offer-daily-exclusive, offer-post-fill-dashboard, offer-site-pr-follow-up, offer-weekday-dashboard. An offer is not an active schedule.

## Safety and limits

The package says to avoid the following:

- Never delete site files, digests, exclusives, or send-log entries. Archive by moving, never by removing.
- Never publish, list, email, or put on public routes a members-only or unplayable video piece. Keep it marked members-only until the video is public. Do not unsend mail already sent. Do not invent a paid newsletter gate.
- Never fake a send. If create-post is blocked, say so and ping the contact they named.
- Never print keys, tokens, or secrets.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`webby.tar.gz`](../packages/webby.tar.gz).
- Package SHA-256: `d7f007a8f5eecc14885b40b3d481849d744ffb0511162f6e81d9f07c0d622f2c`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
