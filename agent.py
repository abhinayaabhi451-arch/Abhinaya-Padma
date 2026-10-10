import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from sub_agents import (
    build_onboarding_agent,
    build_offboarding_agent,
    build_maintenance_agent
)
from supervisor import MultiAgentSupervisor

load_dotenv()

def build_hr_agent():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY missing! Check your .env file.")

    # Shared Gemini Model
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash", 
        temperature=0,
        google_api_key=api_key
    )

    # Instantiate the 3 Specialized Domain Sub-Agents
    onboarding_agent = build_onboarding_agent(llm)
    offboarding_agent = build_offboarding_agent(llm)
    maintenance_agent = build_maintenance_agent(llm)

    # Connect them to the Supervisor Manager
    return MultiAgentSupervisor(
        onboarding_agent=onboarding_agent,
        offboarding_agent=offboarding_agent,
        maintenance_agent=maintenance_agent
    )