class MultiAgentSupervisor:
    """SUPERVISOR ORCHESTRATOR: Routes tasks across Onboarding, Offboarding, and Maintenance agents."""
    
    def __init__(self, onboarding_agent, offboarding_agent, maintenance_agent):
        self.onboarding_agent = onboarding_agent
        self.offboarding_agent = offboarding_agent
        self.maintenance_agent = maintenance_agent

    def invoke(self, inputs):
        query = inputs.get("input", "")
        query_lower = query.lower()

        # Strategy 1: Policy and Maintenance queries
        if "policy" in query_lower or "maternity" in query_lower or "rule" in query_lower:
            return self.maintenance_agent.invoke({"input": query})

        # Strategy 2: Offboarding / Leave calculation requests
        elif "apply" in query_lower or "vacation" in query_lower or "leave" in query_lower or "offboard" in query_lower:
            # Step A: Get employee info via Onboarding Agent
            emp_result = self.onboarding_agent.invoke({"input": query})
            
            # Step B: Calculate leave/exit clearance via Offboarding Agent
            combined_instruction = (
                f"Original request: '{query}'. "
                f"Employee details retrieved: {emp_result['output']}"
            )
            return self.offboarding_agent.invoke({"input": combined_instruction})

        # Strategy 3: Default Onboarding / Employee record lookups
        else:
            return self.onboarding_agent.invoke({"input": query})