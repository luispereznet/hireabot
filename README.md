# Hireabot

Hire a ready-made bot for Hermes Agent. Tell Hermes what job you need done, and Hireabot finds a bot that fits, shows you what it does, and installs it as its own Hermes profile.

```
You:    I need a bot that can coach my sales calls
Hermes: (hireabot_search) Sales Call Coach scores your sales calls and tells you
        what to fix before the next one. Want me to install it?
You:    Yes, install it
Hermes: (hireabot_install) Installed sales-call-coach. Start it with: hermes -p sales-call-coach
```

Each bot is a complete Hermes profile: a personality (`SOUL.md`), skills, optional scheduled jobs, and a config. It installs next to your other profiles and starts with empty memory. Hireabot never overwrites a profile you already have.

> **Status: alpha and beta.** The bots in this catalog are in alpha and beta stages. Some may not do their job properly yet. They will be fully released in the coming days, and fixes land in this repo as they are made. Found a problem or have an improvement? Pull requests are welcome (see [Contributing](#contributing)).

Have a bot to share? [Submit your own bot to the catalog](CONTRIBUTING.md). Contributing is optional.

## Requirements

- [Hermes Agent](https://hermes-agent.nousresearch.com/) 0.22.5 or newer
- A working model in your current or `default` profile (Hireabot copies those model settings to the new bot so the first chat works)
- Internet access to `raw.githubusercontent.com` for the catalog and bot downloads (an offline copy of the catalog ships with the plugin)

No Python packages beyond the standard library are needed.

## Desktop app

Hermes Desktop gets a **Hire a Bot** sidebar section from this same plugin (`desktop/plugin.js`). Enable the Desktop switch under **Capabilities → Plugins**, then open **Hire a Bot** in the sidebar (or ⌘K → Open Hire a Bot). Browse or search the catalog and hire a bot as a new profile.

## Install

From GitHub:

```bash
hermes plugins install luispereznet/hireabot --enable
# same thing with the full URL:
hermes plugins install https://github.com/luispereznet/hireabot --enable
```

Pin an exact commit with `--ref <40-character sha>`. If you install without `--enable`, turn it on later with `hermes plugins enable hireabot`.

From your own clone (for development):

```bash
git clone https://github.com/luispereznet/hireabot ~/.hermes/plugins/hireabot
hermes plugins adopt hireabot     # track it like a git install (check-updates / update)
hermes plugins enable hireabot
```

Check it loaded:

```bash
hermes plugins list
hermes plugins show hireabot
```

Then start Hermes (`hermes`) and ask for a bot in plain words.

## Tools

| Tool | What it does | Changes anything? |
| --- | --- | --- |
| `hireabot_search` | Matches what you need against each bot's name, use cases, description and tags. Returns the best matches with slug, name, description, a relative match score, and whether it is already installed. Weak matches (most of your words not found, low score) are dropped. With no match, it offers to install Bot Designer instead (see [When no bot fits](#when-no-bot-fits)). | No |
| `hireabot_info` | Shows one bot's full details (summary, version, license, tags, use cases, package checksum) and the exact install steps. | No |
| `hireabot_install` | Downloads the bot package, checks its size and sha256 against the catalog, checks every file in it against an allowlist, then runs `hermes profile import`. After import it copies your model settings onto the new profile. | Yes: adds one new profile |

Hermes only calls `hireabot_install` when you clearly ask to install a specific bot.

Also included:

- Slash command: `/hireabot <what you need>` or `/hireabot info <slug>`
- Skill: `hireabot:find-a-bot`, which guides Hermes through search, info and install

## Example requests

- "I need a bot that can coach my sales calls"
- "Is there a bot that keeps an eye on my competitors' pricing pages?"
- "Find me something that rewrites drafts so they sound human"
- "What bots do you have for a daily news brief from X?"
- "Tell me more about tradbot"
- "Install competitor-watch"
- "I need a bot that files my receipts into a spreadsheet" (if nothing matches, Hermes offers to create one with you)

From the slash command:

```
/hireabot daily brief from accounts I follow
/hireabot info x-brief
```

## Bots

Every bot in the catalog, by name. Ask for one in plain words, or use its slug with `hireabot_info` / `hireabot_install`. Versions below 1.0 are alpha; 1.x bots are beta.

<!-- BOTS:START -->
91 bots.

| Bot | Slug | Version | What it does |
| --- | --- | --- | --- |
| [Account Research Desk](bots/account-research-desk.md) | `account-research-desk` | 0.1.0 | Researches the companies you sell to and writes your pre-call brief and account plan. |
| [Ad Spend Watch](bots/ad-spend-watch.md) | `ad-spend-watch` | 0.1.0 | Watches your ad spend and performance and flags what's breaking before it burns budget. |
| [AI Search Visibility](bots/ai-search-visibility.md) | `ai-search-visibility` | 0.1.0 | Checks whether AI assistants and Google recommend you, and who they name instead. |
| [Alfred](bots/alfred.md) | `alfred` | 0.1.0 | Designs, audits, and governs your Hermes bot organization so it matches real company outcomes, with clear human owners and no duplicate jobs. |
| [Apple Search Ads Review](bots/apple-search-ads-review.md) | `apple-search-ads-review` | 0.1.0 | Reviews your Apple Search Ads spend against your cost per install target. |
| [Bot Designer](bots/bot-designer.md) | `bot-designer` | 0.1.0 | Designs Hermes bots with a tight persona, real skills, and an audit before handoff. |
| [Call Follow-Ups](bots/call-follow-ups.md) | `call-follow-ups` | 0.1.0 | Turns each recorded call into a follow-up email in your voice, a next-steps note, and the CRM updates, including the qualification fields your team runs on. |
| [Chief Health Officer](bots/chief-health-officer.md) | `chief-health-officer` | 0.1.0 | Turns your health goals and notes into a dated plan, with unknowns marked and one next step. Early alpha. |
| [Clip Bot](bots/clip-bot.md) | `clip-bot` | 0.1.0 | Finds the best moments in a long recording and cuts them into short captioned clips. |
| [Company Docs Q&A](bots/company-docs-q-a.md) | `company-docs-q-a` | 0.1.0 | Answers product and how-to questions from live docs first, then connected knowledge sources, and always cites sources. |
| [Competitor Watch](bots/competitor-watch.md) | `competitor-watch` | 0.1.0 | Tracks competitor pricing, product, and hiring pages and briefs you on real changes. |
| [Cooper](bots/cooper.md) | `cooper` | 0.1.0 | News agent for AI, tech, venture capital, and business. |
| [Copy Humanizer](bots/copy-humanizer.md) | `copy-humanizer` | 0.1.0 | Edits and rewrites drafts so they read like a person wrote them, in your voice. |
| [Credit Card Max](bots/credit-card-max.md) | `credit-card-max` | 0.1.0 | Tells you which of your credit cards to use for each purchase to get the most points, cash back and perks. |
| [Critiquito: Design Critique](bots/critiquito-design-critique.md) | `critiquito-design-critique` | 0.1.0 | Turns a screenshot or Figma link into a design critique with ranked, concrete fixes. |
| [Customer Call Coach & Assistant](bots/customer-call-coach-assistant.md) | `customer-call-coach-assistant` | 0.1.0 | Briefs you before customer calls and coaches you after based on your performance. |
| [Customer Proof Desk](bots/customer-proof-desk.md) | `customer-proof-desk` | 0.1.0 | Turns call notes and transcripts into case studies, testimonials, and proof points. |
| [Deal Hunting](bots/deal-hunting.md) | `deal-hunting` | 0.1.0 | Landed-cost shopping: real prices, shipping and tax, preferred retailers. |
| [Deal Inspector](bots/deal-inspector.md) | `deal-inspector` | 0.1.0 | Checks every deal that moved stage against your qualification criteria using the actual call transcripts. |
| [dial bot](bots/dial-bot.md) | `dial-bot` | 0.1.0 | Places outbound Bland AI phone calls when you ask, then reports what happened. |
| [Director](bots/director.md) | `director` | 0.1.0 | Your video director: turn briefs into short films, ads, explainers, music videos, micro-dramas, and more — plan, shoot, cut, and deliver. |
| [Distro Bot](bots/distro-bot.md) | `distro-bot` | 0.1.0 | Runs your marketing loop end to end: campaigns on your ad accounts, fresh creative, real channel analysis, timely posts from X and web scans, and outbound until |
| [EBR & Value Deck Builder](bots/ebr-value-deck-builder.md) | `ebr-value-deck-builder` | 0.1.0 | Builds an executive business review or value deck for a named account from your CRM, call history, and usage data, on your brand, and hands you an editable file |
| [Engineer Bot](bots/engineer-bot.md) | `engineer-bot` | 0.1.0 | A hands-off engineering supervisor. |
| [Engineering Lead](bots/engineering-lead.md) | `engineering-lead` | 0.1.0 | An engineering lead that breaks work into small tasks, runs them with Hermes subagents or your coding tools, and chases tests, CI and reviews with the GitHub CLI. |
| [Event Producer](bots/event-producer.md) | `event-producer` | 0.1.0 | Turns your event details into a run of show, guest list, and day-of checklist. |
| [Event Request Desk](bots/event-request-desk.md) | `event-request-desk` | 0.1.0 | Scores every event, sponsorship, and speaking ask, then drafts your yes or no. |
| [Executive Assistant](bots/executive-assistant.md) | `executive-assistant` | 0.1.0 | EA chief-of-staff bot for exec support: conference rooms, interview prep, leadership outreach, Slack channel inventories, sheet↔calendar checks, and birthday/an |
| [figma bro](bots/figma-bro.md) | `figma-bro` | 0.1.0 | Turns a Figma frame into a build spec, and audits your components, tokens, and motion. |
| [Flora: Plant Care Log](bots/flora-plant-care-log.md) | `flora-plant-care-log` | 0.1.0 | Flora keeps a private houseplant care log and weekly reminders. |
| [Game Art Director](bots/game-art-director.md) | `game-art-director` | 0.1.0 | Turns a game concept into a style guide, palettes, and prompt sheets for your image tool. |
| [GTM Account Research](bots/gtm-account-research.md) | `gtm-account-research` | 0.1.0 | Researches one account before a meeting, deal review, or account plan. |
| [GTM Connections](bots/gtm-connections.md) | `gtm-connections` | 0.1.0 | Finds credible ways into a target account through mutual contacts, past conversations, shared history, and prior meetings. |
| [GTM Loop Closer](bots/gtm-loop-closer.md) | `gtm-loop-closer` | 0.1.0 | Finds promises, follow-ups, and customer details left behind in meetings, email, Slack, CRM, or task tools. |
| [GTM Prospecting](bots/gtm-prospecting.md) | `gtm-prospecting` | 0.1.0 | Turns an ideal customer profile into a focused prospect list, adds useful context, and checks for existing relationships. |
| [Haggle Bot](bots/haggle-bot.md) | `haggle-bot` | 0.1.0 | Inventories your SaaS spend from Ramp and bills, finds evidence-backed savings (unused seats, duplicates, cheaper alternatives), and drafts vendor counters for  |
| [Hiring Signals](bots/hiring-signals.md) | `hiring-signals` | 0.1.0 | Tracks hiring activity across selected companies and job sources. |
| [Home robots](bots/home-robots.md) | `home-robots` | 0.1.0 | Control home robots from chat: a Segway Navimow, a Matic vacuum, and other official vacuums, mowers, and Matter robots. |
| [Imogen](bots/imogen.md) | `imogen` | 0.1.0 | Imogen the Impala Image Interpreter writes brief, copyable alt text focused on the most important part of an image, so images are accessible to blind people. |
| [Import Bot](bots/import-bot.md) | `import-bot` | 0.1.0 | Imports Claude Cowork, Codex, ChatGPT, and OpenClaw setups into Hermes expert bots. |
| [last30days](bots/last30days.md) | `last30days` | 0.1.0 | Finds what people actually said about any topic in the last 30 days and writes a cited brief from public sources. |
| [Lead Pipeline Desk](bots/lead-pipeline-desk.md) | `lead-pipeline-desk` | 0.1.0 | Scores your inbound leads, merges duplicates, assigns an owner, and flags what's stuck. |
| [Love ❤️](bots/love.md) | `love` | 0.1.0 | Takes the admin out of being a good Partner so the attention can go where it counts. |
| [Luma Pages](bots/luma-pages.md) | `luma-pages` | 0.1.0 | Builds and updates private Luma event pages for field marketers — copy, branding, registration settings, capacity and waitlist, and registration-list hygiene. |
| [Market Researcher](bots/market-researcher.md) | `market-researcher` | 0.1.0 | Monitors your competitors' public websites, ads, marketing, pricing, and positioning on a standing cadence. |
| [Marketing Analyst](bots/marketing-analyst.md) | `marketing-analyst` | 0.1.0 | Google Ads–first performance analyst: turns exports into weekly and monthly reports with commentary, answers reporting asks with real numbers, and watches spend |
| [Meeting Recap Deck](bots/meeting-recap-deck.md) | `meeting-recap-deck` | 0.1.0 | Turns your meeting notes into a recap deck in your slide template. |
| [Nightly Audit Engineer](bots/nightly-audit-engineer.md) | `nightly-audit-engineer` | 0.1.0 | A nightly engineering auditor that researches a whole codebase, then ships one cleanup PR per area. |
| [NYC Parent](bots/nyc-parent.md) | `nyc-parent` | 0.1.0 | A family chief of staff for New York City parents. |
| [Office Ops Desk](bots/office-ops-desk.md) | `office-ops-desk` | 0.1.0 | Tracks office shipments, facilities issues, and team birthdays, then writes the digests. |
| [Outbound Prospecting](bots/outbound-prospecting.md) | `outbound-prospecting` | 0.1.0 | Finds prospects that match your ideal customer, then drafts a first message to each one. |
| [Overheard](bots/overheard.md) | `overheard` | 0.1.0 | Watches Reddit, Hacker News, news sites, and X for third-party mentions of your name, brand, and URLs, then sends a short weekday digest when something clears t |
| [Paid Media Report Desk](bots/paid-media-report-desk.md) | `paid-media-report-desk` | 0.1.0 | Turns your Google Ads, Meta, and LinkedIn exports into one weekly report with commentary. |
| [Partnerships Call Coach](bots/partnerships-call-coach.md) | `partnerships-call-coach` | 0.1.0 | Pitch and delivery coach for partnership, sponsorship, and high-stakes discovery calls. |
| [Performance Marketer](bots/performance-marketer.md) | `performance-marketer` | 0.1.0 | A performance marketer that turns Product Marketer ad copy into paused Maximize-clicks Google Ads Search shells for messaging tests — review sheets first, then  |
| [Pfp Bot](bots/pfp-bot.md) | `pfp-bot` | 0.1.0 | Turns a photo into a Playbook Icon that keeps hair, colors, and up to three signature features. |
| [Pipeline Pulse](bots/pipeline-pulse.md) | `pipeline-pulse` | 0.1.0 | Scans your full pipeline for movement, stale next steps, forecast risk, and CRM gaps. |
| [Pitch Deck Coach](bots/pitch-deck-coach.md) | `pitch-deck-coach` | 0.1.0 | Reviews a pitch deck and reports what an investor is likely to understand, believe, question, and remember, then helps strengthen the story, evidence, and slide |
| [PM bot](bots/pm-bot.md) | `pm-bot` | 0.1.0 | Acts as your PM. |
| [Product Idea Stress Test](bots/product-idea-stress-test.md) | `product-idea-stress-test` | 0.1.0 | Investigates a product or startup idea for founders. |
| [Product Marketer](bots/product-marketer.md) | `product-marketer` | 0.1.0 | Learns your product, brand, tone, and positioning principles; uses competitive research to sharpen how you stand out; drafts and crafts copy against those princ |
| [Product Support Inbox Assistant](bots/product-support-inbox-assistant.md) | `product-support-inbox-assistant` | 0.1.0 | Helps you find and draft answers to product questions. |
| [Project Manager](bots/project-manager.md) | `project-manager` | 0.1.0 | Marketing project manager that coordinates research, positioning, landing pages, ads, and analytics across specialist bots — with screenshot check-ins and human |
| [Projects Manager](bots/projects-manager.md) | `projects-manager` | 0.1.0 | Runs your team's projects from your own Notion: one row per project, an optional Slack channel per project, and tasks your specialist Hermes bots claim. You decide, agents execute, and it never does the specialist work itself. |
| [Proto Bot](bots/proto-bot.md) | `proto-bot` | 0.1.0 | Turns daily ideas into draft pull requests in your real app, with screenshots, a short video, mocks, and media. |
| [QA bot](bots/qa-bot.md) | `qa-bot` | 0.1.0 | Acts as your QA on the live deploy: runs the acceptance checklist and says pass or fail before you ship. |
| [Recruiting Coordinator](bots/recruiting-coordinator.md) | `recruiting-coordinator` | 0.1.0 | Schedules interview loops, preps your interviewers, and chases what's stalled. |
| [Researchy](bots/researchy.md) | `researchy` | 0.1.0 | A research and fact-check desk that runs every pass with live web search. |
| [Sales Call Coach](bots/sales-call-coach.md) | `sales-call-coach` | 0.1.0 | Scores your sales calls and tells you what to fix before the next one. |
| [Sell Bot](bots/sell-bot.md) | `sell-bot` | 0.1.0 | Works your whole customer journey: outreach in your voice, booked calls with prep and follow-ups, proposals and contracts, then activation, support and billing  |
| [SEO & AEO Desk](bots/seo-aeo-desk.md) | `seo-aeo-desk` | 0.1.0 | Turns your keywords into content ideas and writer-ready briefs for search and AI answers. |
| [Sequencer](bots/sequencer.md) | `sequencer` | 0.1.0 | Runs your outbound sequencer as a staff function. |
| [Signal Prospector](bots/signal-prospector.md) | `signal-prospector` | 0.1.0 | Finds the accounts and people in your CRM and product data that just showed intent, ranks them, and drafts the first touch. |
| [Site Audit](bots/site-audit.md) | `site-audit` | 0.1.0 | SEO + content + speed + a11y + CRO + schema audit. |
| [skippy](bots/skippy.md) | `skippy` | 0.1.0 | A San Francisco street-cleaning assistant. |
| [Stalk Bot](bots/stalk-bot.md) | `stalk-bot` | 0.1.0 | Signs up for your competitors' newsletters and products under its own research email, walks their onboarding on video, and watches their site, pricing, changelo |
| [Startup QA Bot](bots/startup-qa-bot.md) | `startup-qa-bot` | 0.1.0 | Walks your product every weekday in its own test account and tells you what shipped, what got unshipped, what broke (with repro steps and screenshots), and whic |
| [Stills & Clips Desk](bots/stills-clips-desk.md) | `stills-clips-desk` | 0.1.0 | Pulls stills, thumbnails, and short clips out of your footage, sized for where they go. |
| [SWE](bots/swe.md) | `swe` | 0.1.0 | Software engineer bot that implements a code change and verifies it. |
| [Talent Discovery](bots/talent-discovery.md) | `talent-discovery` | 0.1.0 | Finds candidates for open roles that match your criteria and aren't already in your ATS. |
| [Tech Demos](bots/tech-demos.md) | `tech-demos` | 0.1.0 | Weekday X-bookmark scout that picks one new library to demo, asks for approval, then plans and builds it in a sticky monorepo with a cloud coding agent. |
| [The Morning Newspaper](bots/the-morning-newspaper.md) | `the-morning-newspaper` | 0.1.0 | Puts together a personal morning newspaper for you to read each day. Early alpha. |
| [tinkabot](bots/tinkabot.md) | `tinkabot` | 0.1.0 | Wraps an HTTP API or OpenAPI/spec into a local MCP server plus Hermes skills. Proves it locally. Publishes only when you name a destination. |
| [Tradbot](bots/tradbot.md) | `tradbot` | 0.1.0 | Watches your personal email and family schedule so school forms, bills, and RSVPs don't slip. |
| [Video Edit Desk](bots/video-edit-desk.md) | `video-edit-desk` | 0.1.0 | Turns uploaded footage into cut clips, burned-in captions, and platform-sized exports. |
| [Video Editor](bots/video-editor.md) | `video-editor` | 0.1.0 | Edits short vertical talking-head videos from your raw footage: picks the best takes, captions what you actually said, and adds B-roll, motion graphics, and mus |
| [Webby](bots/webby.md) | `webby` | 0.1.0 | Website, newsletter, and public dashboard admin you configure for your own site. Create-only. Ships rather than plans. |
| [Website Ops](bots/website-ops.md) | `website-ops` | 0.1.0 | Website operations and content manager. |
| [Writing Bot](bots/writing-bot.md) | `writing-bot` | 0.1.0 | Drafts and revises any kind of writing so it is clearer, better structured, and right for its audience. |
| [WTD](bots/wtd.md) | `wtd` | 0.1.0 | WTD is a VIP hospitality planning partner for marketing ops — project-plan and status rhythm across tentpoles and ticket banks, nomination-sheet tracking, marke |
| [X Brief](bots/x-brief.md) | `x-brief` | 0.1.0 | Turns the X accounts and topics you pick into one short daily brief with a link on every line. |
<!-- BOTS:END -->

New bots are added to the catalog over time. You do not need to update the plugin to see them (see [How updates work](#how-updates-work)).

## When no bot fits

If `hireabot_search` finds nothing, or you ask about a bot that is not in the catalog, Hireabot says plainly that nothing in the catalog matches that area. The tool response includes a `bot_designer` handoff offering to install Bot Designer (`hireabot_install slug=bot-designer`). Bot Designer helps you create the bot you need through its own interview and build process; Hireabot does not create bots.

Nothing is installed until you say yes. The slash command offers the same handoff instead of direct bot-creation steps.

## After you install a bot

```bash
hermes -p <slug>          # start chatting with the new bot
hermes -p <slug> setup    # optional: add keys for the bot's extra connections
```

Hireabot copies `model.provider`, `model.base_url`, `model.default` and `model.api_mode` from the profile you are running (or from `default` if that one has no model). It never copies API keys or anything else. If the new profile already has model settings, they are left alone.

If the copy fails, or you imported a bot by hand, set the model yourself. Passing `-m` or `--provider` on the chat command is not enough for a profile that has no model yet:

```bash
hermes -p <slug> config set model.provider <provider>
hermes -p <slug> config set model.base_url <url>
hermes -p <slug> config set model.default <model-name>
hermes -p <slug> config set model.api_mode <api_mode>
```

Reinstalling a bot you deleted earlier works too: Hermes leaves a marker at `~/.hermes/profiles/.deleted/<slug>` when a profile is deleted, and `profile import` does not clear it, which makes `hermes -p <slug>` say the profile does not exist. Hireabot clears that marker for the bot it installs.

To remove a bot later, use Hermes's own profile commands (`hermes profile --help`).

## Install a bot by hand

Every bot is a plain `.tar.gz` in [`packages/`](packages/). You can install one without the plugin:

```bash
curl -LO https://raw.githubusercontent.com/luispereznet/hireabot/main/packages/sales-call-coach.tar.gz
shasum -a 256 sales-call-coach.tar.gz   # compare with "sha256" in data/catalog.json
hermes profile import sales-call-coach.tar.gz --name sales-call-coach
```

Then set the model as shown above. Swap `sales-call-coach` for any slug in the [bot list](#bots).

## How updates work

- **Catalog:** Hireabot reads `data/catalog.json` from this repo's `main` branch. It caches the file for 24 hours and revalidates with ETag, so new bots show up within a day without a plugin update. If GitHub cannot be reached, it uses the last cached copy, then the copy bundled with the plugin.
- **Bot packages:** each install downloads the package named in the catalog and checks it against the catalog's size and sha256 before import. Downloads are cached per bot version.
- **The plugin itself:** Hireabot never updates its own code. Update it with Hermes:

```bash
hermes plugins check-updates
hermes plugins update hireabot
```

## Settings

Under `plugins.entries.hireabot.settings` in your Hermes config:

| Setting | Default | Meaning |
| --- | --- | --- |
| `catalog_source` | `https://raw.githubusercontent.com/luispereznet/hireabot/main/data/catalog.json` | Where the bot list comes from. A local path or `file://` URL also works, for offline testing or a private catalog. |
| `max_results` | `5` | How many matches `hireabot_search` returns. |

## What Hireabot touches

- **Network:** HTTPS GET of the catalog and of one bot package per install, both from `raw.githubusercontent.com/luispereznet/hireabot`. No telemetry, no other services.
- **Files:** writes only in its own plugin data folder (catalog cache and downloaded packages). Reads `~/.hermes/profiles/` to see which bots are installed. Removes the `profiles/.deleted/<slug>` marker for the bot being installed, and nothing else.
- **Shell commands:** `hermes profile import`, then `hermes -p <profile> config get/set` for the four model keys. They run through Hermes's terminal tool, so your normal approval settings apply.
- **Package checks:** before import, every package is checked for absolute paths, `..`, links, and any file outside the expected profile layout (persona, config, skills, cron jobs, workspace files). Anything else, including `.env`, `auth.json` and session files, makes the install stop.
- **Credentials:** none are read, copied or stored.

## Develop and validate

```bash
hermes plugins validate /path/to/hireabot --install-deps
hermes plugins doctor /path/to/hireabot --ci
python3 tests/test_catalog_cache.py
```

The unit tests run against a local HTTP server and a temporary folder. They do not touch your Hermes profiles.

Bot detail pages describe the shipped archives, not unpublished source folders. After changing a package and its catalog checksum, run `python3 scripts/build_bot_docs.py`, then `python3 scripts/build_bot_docs.py --check` and `python3 tests/test_bot_docs.py`. This updates `bots/<slug>.md` and README catalog links without changing packages or catalog metadata. The catalog builder preserves these links; run the docs builder after adding catalog entries.

To publish a new set of bots, put their `<slug>.tar.gz` exports in a folder and rebuild the catalog, the packages and the bot list in this README:

```bash
python3 scripts/build_catalog.py --exports <exports-dir> [--source <metadata catalog.json>] --all
```

## Repository layout

```
plugin.yaml              plugin manifest
__init__.py              register(ctx): tools, slash command, skill
schemas.py               tool schemas the model reads
tools.py                 handlers (all return JSON, none raise)
skills/find-a-bot/       bundled skill
data/catalog.json        the bot catalog (also the offline fallback)
packages/                bot packages (.tar.gz) the catalog points to
scripts/build_catalog.py rebuilds the catalog and packages
tests/                   unit tests
```

## Contributing

Pull requests are welcome, especially fixes and improvements to the bots:

- **Update a bot:** each bot is a `.tar.gz` in [`packages/`](packages/). Unpack it, make your change (persona in `SOUL.md`, skills under `skills/`), bump `version` in its `distribution.yaml`, pack it again with the bot folder at the top level, then run `scripts/build_catalog.py` so `data/catalog.json` gets the new sha256 and size. Open a PR that says what the bot does better.
- **Add a bot:** follow the [submission guide](CONTRIBUTING.md) for new contributions, including a public loadable Hermes plugin pinned to a full commit SHA and passing local checks.
- **Plugin changes:** keep every tool returning JSON, and run the validate, doctor and unit test commands above before you open the PR.

## License

MIT. See [LICENSE](LICENSE).
