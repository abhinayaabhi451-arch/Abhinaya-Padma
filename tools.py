from langchain.tools import tool
from pydantic import BaseModel, Field
from config import EMPLOYEE_DATABASE, POLICY_DATABASE, logger

class EmployeeLookupInput(BaseModel):
    emp_id: str = Field(description="Unique Employee Identifier, e.g., 'EMP101'")

@tool("employee_lookup", args_schema=EmployeeLookupInput)
def employee_lookup(emp_id: str) -> str:
    """Retrieves employee profile information and current leave balance using Employee ID."""
    logger.info(f"Executing employee_lookup for ID: {emp_id}")
    try:
        emp_id_clean = emp_id.upper().strip()
        if emp_id_clean in EMPLOYEE_DATABASE:
            emp = EMPLOYEE_DATABASE[emp_id_clean]
            return (f"Employee Record Found: Name: {emp['name']} | Role: {emp['role']} | "
                    f"Department: {emp['department']} | Leave Balance: {emp['leave_balance']} days.")
        return f"Error: Employee ID '{emp_id}' not found in enterprise records."
    except Exception as e:
        logger.error(f"Error in employee_lookup: {str(e)}")
        return "System Exception: Failed to retrieve employee data."

class PolicySearchInput(BaseModel):
    topic: str = Field(description="The HR policy keyword or topic, e.g., 'maternity', 'sick', 'vacation'")

@tool("search_policy_doc", args_schema=PolicySearchInput)
def search_policy_doc(topic: str) -> str:
    """Searches HR policy documentation for official company policy guidelines."""
    logger.info(f"Executing search_policy_doc for topic: {topic}")
    try:
        topic_clean = topic.lower().strip()
        for key, details in POLICY_DATABASE.items():
            if key in topic_clean:
                return f"Official Policy Document: {details}"
        return f"Policy Lookup: No explicit guidelines found for topic '{topic}'. Manual HR review needed."
    except Exception as e:
        logger.error(f"Error in search_policy_doc: {str(e)}")
        return "System Exception: Failed to search policy database."

class LeaveCalculationInput(BaseModel):
    current_balance: int = Field(description="The available leave balance of the employee in days.")
    requested_days: int = Field(description="Number of leave days requested.")

@tool("calculate_leave_request", args_schema=LeaveCalculationInput)
def calculate_leave_request(current_balance: int, requested_days: int) -> str:
    """Validates leave availability and calculates updated leave balances post-request."""
    logger.info(f"Executing calculate_leave_request: Balance={current_balance}, Requested={requested_days}")
    try:
        if requested_days <= 0:
            return "Validation Failure: Leave request days must be greater than 0."
        if requested_days > current_balance:
            return (f"Validation Failure: Insufficient leave balance. Requested ({requested_days} days) "
                    f"exceeds current balance ({current_balance} days).")

        remaining = current_balance - requested_days
        return f"Validation Success: Request approved. Remaining leave balance will be {remaining} days."
    except Exception as e:
        logger.error(f"Error in calculate_leave_request: {str(e)}")
        return "System Exception: Failed to complete leave calculation."

hr_tools = [employee_lookup, search_policy_doc, calculate_leave_request]