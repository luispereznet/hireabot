"""Hireabot: find and install ready-made Hermes bots (profiles)."""
from __future__ import annotations

import logging
from pathlib import Path

from . import schemas, tools

logger = logging.getLogger(__name__)
TOOLSET = "hireabot"


def register(ctx):
    tools.bind(ctx)
    ctx.register_tool(name="hireabot_search", toolset=TOOLSET, schema=schemas.SEARCH,
                      handler=tools.hireabot_search, emoji="🔎")
    ctx.register_tool(name="hireabot_info", toolset=TOOLSET, schema=schemas.INFO,
                      handler=tools.hireabot_info, emoji="📘")
    ctx.register_tool(name="hireabot_install", toolset=TOOLSET, schema=schemas.INSTALL,
                      handler=tools.hireabot_install, emoji="📦")
    ctx.register_command("hireabot", handler=tools.slash_hireabot,
                         description="Hire a ready-made bot: /hireabot <what you need> | info <slug>",
                         args_hint="<what you need> | info <slug>")
    skills_dir = Path(__file__).parent / "skills"
    for child in sorted(skills_dir.iterdir()) if skills_dir.is_dir() else []:
        if child.is_dir() and (child / "SKILL.md").exists():
            ctx.register_skill(child.name, child / "SKILL.md")
