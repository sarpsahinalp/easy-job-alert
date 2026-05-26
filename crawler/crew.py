from crewai import Crew, Process

from agents.base_agent import create_base_agent
from tasks.job_tasks import create_job_search_task


def build_crew() -> Crew:
    job_searcher = create_base_agent(
        role="Job Search Specialist",
        goal="Find relevant software engineering job postings from the last 24 hours",
        backstory="You are an expert at sourcing and summarizing job listings efficiently.",
    )

    tasks = [
        create_job_search_task(job_searcher),
    ]

    return Crew(
        agents=[job_searcher],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )
