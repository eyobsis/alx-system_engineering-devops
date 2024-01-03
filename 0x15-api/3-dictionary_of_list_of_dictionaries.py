#!/usr/bin/python3
"""
This script retrieves and displays information about
an employee's TODO list progress using a given employee ID.
It also exports the data in JSON format for all employees.
"""

import csv
import json as json_module
import requests
from sys import argv

def get_all_employees_data():
    """Fetch data for all employees from the API."""
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    users_data = user_response.json()
    
    all_employees_data = {}
    
    for user_data in users_data:
        user_id = user_data['id']
        _, todo_data = get_employee_data(user_id)
        all_employees_data[user_id] = format_todo_data(user_data, todo_data)
    
    return all_employees_data

def get_employee_data(employee_id):
    """Fetch user and TODO list data from the API."""
    id = employee_id
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    return user_data, todo_data

def format_todo_data(user_data, todo_data):
    """Format TODO data for a single employee."""
    formatted_data = []
    for task in todo_data:
        formatted_data.append({
            "username": user_data['username'],
            "task": task['title'],
            "completed": task['completed']
        })
    return formatted_data

def export_all_to_json(all_employees_data):
    """Export data for all employees to a single JSON file."""
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json_module.dump(all_employees_data, json_file, indent=2)
    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(argv) != 1:
        print("Usage: python3 script_name.py")
    else:
        all_employees_data = get_all_employees_data()
        export_all_to_json(all_employees_data)
