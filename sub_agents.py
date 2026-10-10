# ==============================================================================
# SUB-AGENTS FOR MILESTONE 2:
# 1. OnboardingAgent: Handles new hire verification and profile lookup
# 2. OffboardingAgent: Handles exit clearance, final calculations, and leave balance deductions
# 3. MaintenanceAgent: Handles HR policy queries and general maintenance rules
# ==============================================================================

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

# Import your existing tools from tools.py
from tools import employee_lookup, search_policy_doc, calculate_leave_request


def build_onboarding_agent(llm):
    """SUB-AGENT 1: Onboarding Specialist"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an HR Onboarding Specialist. Your role is to look up employee records and verify onboarding details using 'employee_lookup'."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_tool_calling_agent(llm, [employee_lookup], prompt)
    return AgentExecutor(agent=agent, tools=[employee_lookup], verbose=True)


def build_offboarding_agent(llm):
    """SUB-AGENT 2: Offboarding Specialist"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an HR Offboarding Specialist. Your role is to compute final leave balances and exit clearance using 'calculate_leave_request'."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_tool_calling_agent(llm, [calculate_leave_request], prompt)
    return AgentExecutor(agent=agent, tools=[calculate_leave_request], verbose=True)


def build_maintenance_agent(llm):
    """SUB-AGENT 3: HR Maintenance & Policy Specialist"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an HR Maintenance & Policy Specialist. Your role is to answer company policy and rule queries using 'search_policy_doc'."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_tool_calling_agent(llm, [search_policy_doc], prompt)
    return AgentExecutor(agent=agent, tools=[search_policy_doc], verbose=True)