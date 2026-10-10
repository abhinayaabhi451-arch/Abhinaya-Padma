import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("HR_Engine")

EMPLOYEE_DATABASE = {
    "EMP101": {
        "name": "Alice Smith",
        "role": "Senior Software Engineer",
        "department": "Engineering",
        "leave_balance": 12,
        "email": "alice.smith@company.com"
    },
    "EMP102": {
        "name": "Bob Johnson",
        "role": "HR Manager",
        "department": "Human Resources",
        "leave_balance": 5,
        "email": "bob.johnson@company.com"
    }
}

POLICY_DATABASE = {
    "maternity": "Maternity leave policy grants up to 26 weeks of fully paid leave.",
    "paternity": "Paternity leave policy grants 2 weeks of paid leave.",
    "sick": "Employees are entitled to 10 days of paid sick leave annually.",
    "vacation": "Standard paid vacation allowance is 15 days per year."
}
