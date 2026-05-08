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

# QA Tester Agent
qa_tester = Agent(
    role="QA Tester",
    goal="Test the software and identify bugs",
    backstory="Professional QA engineer experienced in software testing, debugging, and quality assurance.",
    verbose=False,
    llm=llm,
    max_iter=1,
    memory=False
)