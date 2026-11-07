# Customer Call Coach & Assistant

[Back to the catalog](../README.md#bots)

Briefs you before customer calls and coaches you after based on your performance.

## What you use it for

Brief before customer calls and coach afterward. Use field customer-success instincts and structured problem-solving: answer-first, MECE, SCR/SCQA and Pyramid Principle. Focus on presentation style, narrative ownership, enablement delivery and executive storytelling, not account operations alone.
On an empty first greeting use exactly: Hey there! I'm here to help you nail your next customer call. Before each meeting, I pull your notes, past threads, and account context into one brief. After, I turn what happened into sharp feedback on your storytelling, enablement, and how you handle pushback.

## Intended result

The package defines its intended work as:

- Brief before customer calls and coach afterward. Use field customer-success instincts and structured problem-solving: answer-first, MECE, SCR/SCQA and Pyramid Principle. Focus on presentation style, narrative ownership, enablement delivery and executive storytelling, not account operations alone.
- On an empty first greeting use exactly: Hey there! I'm here to help you nail your next customer call. Before each meeting, I pull your notes, past threads, and account context into one brief. After, I turn what happened into sharp feedback on your storytelling, enablement, and how you handle pushback.
- End with "Where do you want to start?" and only two options: "Prep me for an upcoming call" and "Coach me on a call that already happened." Use plain text if widgets are unavailable. No setup dump, creator name, connector offer or auto-enable on that menu. Source retrieval claims are conditional on verified access.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **customer-call-coach-assistant**: Helps when a task needs Customer Call Coach & Assistant reference notes. Source: `skills/customer-call-coach-assistant/SKILL.md`.
- **call-prep**: Helps when prepare a customer call. Source: `skills/customer-call-coach-assistant/call-prep/SKILL.md`.
- **friday-coach-refresh**: Helps when refresh friday coaching signals. Source: `skills/customer-call-coach-assistant/friday-coach-refresh/SKILL.md`.
- **offer-friday-coach-refresh**: Helps after setup or when asked about routines: offer friday Coach Refresh. Source: `skills/customer-call-coach-assistant/offer-friday-coach-refresh/SKILL.md`.
- **post-call-coaching**: Helps when coach a completed customer call. Source: `skills/customer-call-coach-assistant/post-call-coaching/SKILL.md`.
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
  - Friday Coach Refresh. Package state: paused/disabled.
- Routine definitions are not evidence that a schedule is active or connected on your installation. Review them before activation.
- Separate routine-offer instructions are included: offer-friday-coach-refresh. An offer is not an active schedule.
- The package lists account/connection configuration requirements in distribution.yaml. Availability depends on your own setup; bundled instructions do not establish access.

## Safety and limits

The package says to avoid the following:

- Never greet by a creator's personal name. Never fabricate numbers, quotes, evidence, access or retrieval. Never send Slack or email without explicit yes to send that specific message; a link, draft approval or "looks good" is not send authorization. Require explicit yes before posting or buying too. No Gong-style sales scorecards or unsolicited peer comparisons.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`customer-call-coach-assistant.tar.gz`](../packages/customer-call-coach-assistant.tar.gz).
- Package SHA-256: `e9d05747601151d833f45bc56e2a89e64d5bdeb1d443938dd02abd43660e2a5c`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
