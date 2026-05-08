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

# Architect Agent
architect = Agent(
    role="Software Architect",
    goal="Design scalable software architecture",
    backstory="Expert software architect skilled in system design, databases, APIs, and scalable applications.",
    verbose=False,
    llm=llm,
    max_iter=1,
    memory=False
)