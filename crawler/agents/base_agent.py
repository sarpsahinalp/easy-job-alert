from crewai import Agent, LLM

from auth.token_fetcher import fetch_gh_token
from tools.browser_tool import BrowserTool


def create_base_agent(role: str, goal: str, backstory: str) -> Agent:
    llm = LLM(
        model="openai/gpt-4o",
        base_url="https://api.githubcopilot.com",
        api_key=fetch_gh_token(),
    )

    return Agent(
        tools=[BrowserTool()],
        role=role,
        goal=goal,
        backstory=backstory,
        llm=llm,
        verbose=True,
    )
