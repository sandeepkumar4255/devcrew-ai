from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv(override=True)

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

product_manager = Agent(
    role="Product Manager",
    goal="Analyze software requirements",
    backstory="Expert software product manager",
    verbose=False,
    memory=False,
    max_iter=1,
    llm=llm
)