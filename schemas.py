"""Tool schemas: what the model reads."""

SEARCH = {
    "name": "hireabot_search",
    "description": (
        "Search the Hireabot catalog of ready-made Hermes bots. Use when the user wants a bot, "
        "assistant or agent for a job (e.g. 'I need a bot that can coach my sales calls'). Returns the best "
        "matches with slug, name, description and a relative match score. With no match it returns create_a_bot: steps to offer the user for creating a new bot. Read-only."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "What the user needs the bot to do, in plain words."},
            "limit": {"type": "integer", "description": "Max results (default from plugin settings, usually 5)."},
        },
        "required": ["query"],
    },
}

INFO = {
    "name": "hireabot_info",
    "description": (
        "Show one catalog bot's full details (what it does, its skills, version, whether it is already "
        "installed) and the exact install steps. Use after hireabot_search, before installing. Read-only."
    ),
    "parameters": {
        "type": "object",
        "properties": {"slug": {"type": "string", "description": "Bot slug from hireabot_search."}},
        "required": ["slug"],
    },
}

INSTALL = {
    "name": "hireabot_install",
    "description": (
        "Install one catalog bot as a new Hermes profile using Hermes's own `hermes profile import`. "
        "Only call when the user has clearly asked to install that specific bot. Refuses if a profile with "
        "that name already exists (never overwrites). Returns the next steps: `hermes -p <slug> setup`, "
        "then `hermes -p <slug>`."
    ),
    "parameters": {
        "type": "object",
        "properties": {"slug": {"type": "string", "description": "Bot slug from hireabot_search."}},
        "required": ["slug"],
    },
}
