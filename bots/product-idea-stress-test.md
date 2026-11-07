# Product Idea Stress Test

[Back to the catalog](../README.md#bots)

Investigates a product or startup idea for founders.

## What you use it for

Investigates a product or startup idea for founders.
Surfaces what has to be true, evidence for and against, the assumption most likely to kill it, and what to test next.

## Intended result

The package defines its intended work as:

- Investigates a product or startup idea for founders.
- Surfaces what has to be true, evidence for and against, the assumption most likely to kill it, and what to test next.
- I am a rigorous product and startup idea investigator.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **product-idea-stress-test**: Helps when a task needs Product Idea Stress Test reference notes. Source: `skills/product-idea-stress-test/SKILL.md`.
- **pist-evidence-investigator**: Use this when Product Idea Stress Test has already selected this skill because. Source: `skills/product-idea-stress-test/pist-evidence-investigator/SKILL.md`.
- **pist-experiment-designer**: Use this when Product Idea Stress Test has already named a Bottleneck Belief. Source: `skills/product-idea-stress-test/pist-experiment-designer/SKILL.md`.
- **pist-method-codifier**: Use this when Product Idea Stress Test has classified substantial user-provided. Source: `skills/product-idea-stress-test/pist-method-codifier/SKILL.md`.

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

- I am not here to encourage, discourage, generate generic startup advice, or produce a superficial score.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`product-idea-stress-test.tar.gz`](../packages/product-idea-stress-test.tar.gz).
- Package SHA-256: `bd4cb2ee71462d22928a9881022a3609d07ef92a24199b957e848a6d46d0c8e5`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
