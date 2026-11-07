# Projects Manager

[Back to the catalog](../README.md#bots)

Runs your team's projects from your own Notion: one row per project, an optional Slack channel per project, and tasks your specialist Hermes bots claim. You decide, agents execute, and it never does the specialist work itself.

## What you use it for

Project ops lead for the user's team. Runs projects from the user's own Notion: one Project row per project, Task rows under it, and an optional Slack channel per project.
Staffs, tracks, pings and routes. Specialist Hermes bots do the work; the user decides. This bot is not a specialist and never does the specialist work itself.

## Intended result

The package defines its intended work as:

- Project ops lead for the user's team. Runs projects from the user's own Notion: one Project row per project, Task rows under it, and an optional Slack channel per project.
- Staffs, tracks, pings and routes. Specialist Hermes bots do the work; the user decides. This bot is not a specialist and never does the specialist work itself.
- Every Project and Task row has a page icon. Blocked is a Status value, and the Note field holds the question or context.

## Included skills

Skills are written instructions the bot follows, not necessarily runnable programs.

- **user-setup**: Asks skippable first-chat questions and saves your preferences for future sessions. Source: `skills/onboarding/user-setup/SKILL.md`.
- **blocked-ping**: Helps when a task is Blocked: ping the user with its Note and wait. Source: `skills/projects-manager/blocked-ping/SKILL.md`.
- **project-ops**: Use to start a project, add tasks, change status, archive, or show status. Source: `skills/projects-manager/project-ops/SKILL.md`.
- **project-scripts**: Use to run the local project list helper (projects.py). Source: `skills/projects-manager/project-scripts/SKILL.md`.
- **project-setup**: Use to set up Notion, optional Slack, specialist bots and icons. Source: `skills/projects-manager/project-setup/SKILL.md`.
- **staff-and-claim**: Use to assign a task to a Hermes bot or record a claim. Never does the work. Source: `skills/projects-manager/staff-and-claim/SKILL.md`.

## Included scripts

Scripts are bundled helper programs. This inventory does not execute them or grant permission to run them.

- **user_setup.py**: Runs first-chat setup, saves your preferences, and stops repeating setup once it is complete. Reading another bot requires consent. Source: `skills/onboarding/user-setup/scripts/user_setup.py`.
- **projects.py**: Keeps a local project and task list, status changes, and archived records. It does not itself contact the connected project or chat services. Source: `skills/projects-manager/project-scripts/scripts/projects.py`.

## Optional skill-to-script conversion

No script-conversion option is documented in this package.
Bundled scripts listed above already exist; their presence does not mean a skill can be converted into a new script.

## Setup and routine notes

- First-chat setup instructions are included. You supply your own preferences and any required account access.
- No saved routine definitions are included.

## Safety and limits

The package says to avoid the following:

- Never do the specialist work: no writing, coding, designing or research for a task. Assign or route it instead.
- Never decide for the user: scope, priority, staffing changes and approvals are the user's call.
- Never invent an answer to a blocked task. Ping the user with the Note and wait.
- Never require or install an editor plugin, a Notion plugin or a Slack plugin. Use only the connections the user already set up in Hermes.
- These are documented instructions, not proof of enforcement or a live test of the bot. Required tools, accounts, and permissions still need verification.

## Package facts and sources

- Version: 0.1.0.
- Minimum Hermes requirement: >=0.22.5.
- License: MIT.
- Package: [`projects-manager.tar.gz`](../packages/projects-manager.tar.gz).
- Package SHA-256: `baaadd96e0a7d36b761108879154578e922a9488b9f7635cdf6f3d600087438e`.
- Descriptions use the catalog label and the shipped SOUL.md, distribution.yaml, skill instructions, script headers/behavior, and any cron/jobs.json. Author fields and private working paths are not reproduced.
- Generated from the archive linked above, not from an installed bot or an unpublished source folder. No live Desktop rendering or bot execution is implied.
