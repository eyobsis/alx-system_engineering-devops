#!/usr/bin/python3

"""
This script retrieves and displays information about employees' TODO list progress.
It also exports the data in JSON format for all employees.
"""

import requests
import json
from sys import argv

def get_all_employees_data():
    """Fetch TODO list data for all employees from the API."""
    user_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(user_url)
    users_data = users_response.json()

    all_employees_data = {}

    for user in users_data:
        employee_id = user['id']
        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        all_employees_data[str(employee_id)] = []

        for task in todo_data:
            all_employees_data[str(employee_id)].append({
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            })

    return all_employees_data

def export_to_json(all_employees_data):
    """Export data to JSON file."""
    json_filename = "todo_all_employees.json"

    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_data, json_file)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    all_employees_data = get_all_employees_data()
    export_to_json(all_employees_data)
