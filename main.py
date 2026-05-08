from crewai import Crew

# Agents
from agents.product_manager import product_manager
from agents.architect import architect
from agents.backend_dev import backend_dev
from agents.qa_tester import qa_tester

# Tasks
from tasks.product_tasks import analyze_task
from tasks.architect_tasks import architecture_task
from tasks.backend_tasks import backend_task
from tasks.qa_tasks import qa_task

crew = Crew(
    agents=[
        product_manager,
        architect,
        backend_dev,
        qa_tester
    ],

    tasks=[
        analyze_task,
        architecture_task,
        backend_task,
        qa_task
    ],

    verbose=False
)

result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)