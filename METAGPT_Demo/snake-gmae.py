import os
os.environ["OPENAI_API_KEY"] ="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"
os.environ["OPENAI_API_MODEL"] = "gpt-4-1106-preview"

import asyncio
from metagpt.roles import (
    Architect,
    Engineer,
    ProductManager,
    ProjectManager,
)
from metagpt.team import Team


async def startup(idea: str):
    company = Team()
    company.hire(
        [
            ProductManager(),
            Architect(),
            ProjectManager(),
            Engineer(),
        ]
    )
    company.invest(investment=3.0)
    company.run_project(idea=idea)

    await company.run(n_round=5)

    await startup(idea="write a cli snake game based on pygame")