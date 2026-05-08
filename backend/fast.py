from fastapi import FastAPI
from pydantic import BaseModel
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

app = FastAPI()

# Input model
class ProjectRequest(BaseModel):
    idea: str

# Home route
@app.get("/")
def home():
    return {"message": "CrewAI Backend Running"}

# Analyze route
@app.post("/analyze")
def analyze_project(request: ProjectRequest):

    # Dynamic task input
    analyze_task.description = (
        f"Analyze this software idea briefly: {request.idea}"
    )

    # Create Crew
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

    # Run CrewAI
    result = crew.kickoff()

    return {
        "result": str(result)
    }