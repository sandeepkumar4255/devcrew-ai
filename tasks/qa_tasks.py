from crewai import Task
from agents.qa_tester import qa_tester

qa_task = Task(
    description="Find possible bugs briefly.",
    expected_output="Short QA report in 3 points.",
    agent=qa_tester
)