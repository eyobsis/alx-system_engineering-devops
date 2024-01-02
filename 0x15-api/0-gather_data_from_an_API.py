#!/usr/bin/python3
"""
This script retrieves and displays information about an employee's
TODO list progress using a given employee ID.
"""

from sys import argv
import requests


def get_employee_data(emp_id):
    """Fetch user and TODO list data from the API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_resp = requests.get(user_url)
    user_data = user_resp.json()

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todo_resp = requests.get(todo_url)
    todo_data = todo_resp.json()

    return user_data, todo_data


def display_progress(user_data, todo_data):
    """Display employee TODO list progress."""
    total_tasks = len(todo_data)
    done_tasks = sum(task['completed'] for task in todo_data)
    i = total_tasks
    j = done_tasks
    message = f"{user_data['name']} is done with tasks ({j}/{i}):"
    print(message)
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 script_name.py <employee_id>")
    else:
        emp_id = int(argv[1])
        user_data, todo_data = get_employee_data(emp_id)
        display_progress(user_data, todo_data)
