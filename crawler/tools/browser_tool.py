import asyncio

from crewai.tools import BaseTool
from browser_use import Agent, ChatOpenAI

from auth.token_fetcher import fetch_gh_token


class BrowserTool(BaseTool):
    name: str = "Browser"
    description: str = (
        "Browse the internet to complete a task. "
        "Input should be a clear, specific task description such as "
        "'find software engineering remote job postings from the last 24 hours on LinkedIn'."
    )

    def _run(self, task: str) -> str:
        llm = ChatOpenAI(
            model="gpt-4o",
            base_url="https://api.githubcopilot.com",
            api_key=fetch_gh_token(),
        )
        agent = Agent(task=task, llm=llm)
        result = asyncio.run(agent.run())
        return str(result)
