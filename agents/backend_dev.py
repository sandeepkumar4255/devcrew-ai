from crewai import Agent
from crewai import LLM
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)

# Configure Groq LLM
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

# Backend Developer Agent
backend_dev = Agent(
    role="Backend Developer",
    goal="Develop backend logic and APIs",
    backstory="Experienced backend developer specializing in FastAPI, databases, APIs, and authentication systems.",
    verbose=False,
    llm=llm,
    max_iter=1,
    memory=False
)