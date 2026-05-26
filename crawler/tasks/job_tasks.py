from crewai import Agent, Task


def create_job_search_task(agent: Agent) -> Task:
    return Task(
        description=(
            "Search for software engineering job postings from the last 24 hours. "
            "Focus on remote positions. Extract job title, company, location, and URL."
        ),
        expected_output=(
            "A structured list of job postings, each with: title, company, location, url."
        ),
        agent=agent,
    )
