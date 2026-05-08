from crewai import Task
from agents.product_manager import product_manager

analyze_task = Task(
    description="Analyze software idea briefly.",
    expected_output="5 short feature points only.",
    agent=product_manager
)