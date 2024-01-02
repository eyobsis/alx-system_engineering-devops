#!/usr/bin/python3

"""
This script retrieves and displays information about an employee's TODO list progress using a given employee ID.
"""

import requests
from sys import argv

def get_employee_data(employee_id):
    """Fetch user and TODO list data from the API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    return user_data, todo_data

def display_progress(user_data, todo_data):
    """Display employee TODO list progress."""
    total_tasks = len(todo_data)
    done_tasks = sum(task['completed'] for task in todo_data)

    print(f"Employee {user_data['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(argv[1])
        user_data, todo_data = get_employee_data(employee_id)
        display_progress(user_data, todo_data)
