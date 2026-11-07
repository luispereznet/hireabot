---
name: find-a-bot
description: Use when the user asks for a bot, assistant or agent that can do a job ("I need a bot that can X"), or asks what ready-made bots exist. Finds and installs Hireabot bots.
---

# Find a ready-made bot

1. Call `hireabot_search` with the user's need in plain words. Show the top 1-3 matches: name, one-line description, match score.
2. If the user wants more on one, call `hireabot_info` and summarize what it does and its skills.
3. Install only when the user clearly says to install that bot. Call `hireabot_install` with its slug.
   - It never overwrites: if the profile exists, say so and give the run command instead.
   - After import it copies `model.provider`, `model.base_url`, `model.default`, and `model.api_mode` from the active profile (or `default`) so the first chat works. It does not copy API keys.
4. After install, tell the user the next steps exactly:
   - `hermes -p <slug>` (start chatting; model settings were copied when possible)
   - `hermes -p <slug> setup` (optional: add extra keys)
   If the install note says model copy failed, or a hand import was used, set the model non-interactively (passing `-m` / `--provider` on chat does not help):
   - `hermes -p <slug> config set model.provider <provider>`
   - `hermes -p <slug> config set model.base_url <url>`
   - `hermes -p <slug> config set model.default <model-name>`
   - `hermes -p <slug> config set model.api_mode <api_mode>`
   The new bot starts with empty memory and none of the user's data.
5. No match (empty results, or `hireabot_info` says unknown bot): say plainly that nothing in the catalog matches that area. Offer to install Bot Designer (`hireabot_install slug=bot-designer`), explaining that its own interview and build process helps the user create the bot they need. Hireabot does not create bots. Never install anything until the user says yes.

Never install more than the one bot the user asked for. Never remove profiles.
