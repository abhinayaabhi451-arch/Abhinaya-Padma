import time
from agent import build_hr_agent


def run_milestone2_tests():
    print("=" * 60)
    print("  Enterprise HR Assistant - Multi-Agent System (Milestone 2)")
    print("=" * 60)

    # Initialize the Multi-Agent Supervisor System
    agent_system = build_hr_agent()

    # Define test cases corresponding to Onboarding, Maintenance, and Offboarding
    test_cases = [
        {
            "id": "TEST CASE 1 (Onboarding / Record Lookup)",
            "query": "What is the details and current leave balance for employee EMP101?"
        },
        {
            "id": "TEST CASE 2 (Maintenance / Policy Query)",
            "query": "What is our official company policy on maternity leave?"
        },
        {
            "id": "TEST CASE 3 (Offboarding / Leave Calculation)",
            "query": "Employee EMP101 wants to apply for 4 days of vacation. Check their eligibility and process the calculation."
        }
    ]

    for i, test in enumerate(test_cases, start=1):
        print(f"\n[{test['id']}]")
        print(f"Query: '{test['query']}'")
        print("-" * 60)

        try:
            response = agent_system.invoke({"input": test["query"]})
            print("\n[AGENT RESPONSE]:")
            print(response.get("output", response))
        except Exception as e:
            print(f"\n[EXECUTION ERROR]: {e}")

        print("=" * 60)

        # Pause between test cases to prevent Google API 429 Rate Limit errors
        if i < len(test_cases):
            print("\n[PAUSE] Waiting 40 seconds to respect API quota limits...\n")
            time.sleep(40)


if __name__ == "__main__":
    run_milestone2_tests()

    