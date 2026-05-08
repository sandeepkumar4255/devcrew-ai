from crewai import Task
from agents.backend_dev import backend_dev

# Backend Development Task
backend_task = Task(
    description="Create backend API structure and database plan briefly.",
    expected_output="Short backend API and database summary in 3 points.",
    agent=backend_dev
)