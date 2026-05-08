from crewai import Task
from agents.architect import architect

architecture_task = Task(
    description="Design simple architecture briefly.",
    expected_output="Short architecture summary in 3 points.",
    agent=architect
)