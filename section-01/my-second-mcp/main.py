from typing import List
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("MyMCPServer")

employee_leaves = {
    "E001": {"balance": 18, "history": ["2024-12-25", "2025-01-01"]},
    "E002": {"balance": 20, "history": ["2025-05-21"]}
}

@mcp.tool()
def get_leaves_balance(employee_id: str) -> str:
    data = employee_leaves.get(employee_id)
    
    if data:
        return employee_leaves.get(employee_id)
    return "Employee ID not found"

@mcp.tool()
def apply_leave(employee_id: str, leave_datas : List[str]) -> str:
    """
    Apply leave for specifi dates (e.g. , ["2025-04-17", "2025-05-01"])
    """
    if employee_id not in employee_leaves:
        return "employee ID is not found"
    
    requested_days = len(leave_datas)
    available_balance = employee_leaves[employee_id]["balance"]
    
    if available_balance < requested_days:
        return f"Insufficient leave balance. You requested {requested_days} days(s)"
    
    employee_leaves[employee_id]["balance"] -= requested_days
    employee_leaves[employee_id]["histwory"].extend(leave_datas)
    
@mcp.tool()
def get_leave_history(employee_id: str) -> str:
    """Get leave history for the employee"""
    data = employee_leaves.get(employee_id)
    
    if data:
        history = ', '.join(data['history']) if data['history'] else "No leave"
        return f"Leave history for {employee_id}: {history}"
    
    return "Employee ID not found"

@mcp.resource("greeting://{name}")
def get_greeting(name: str)-> str:
    """Get a personalized greeting"""
    return  f"Hello, {name} !How can I assist you with leave management today?"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run()
