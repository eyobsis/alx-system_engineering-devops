#!/usr/bin/python3

"""
This script retrieves and displays information about an employee's TODO list progress using a given employee ID.
It also exports the data in CSV format.
"""

import requests
import csv
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
    return user_data, todo_data

def export_to_csv(user_data, todo_data):
    """Export data to CSV file."""
    user_id = user_data['id']
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            csv_writer.writerow([user_id, user_data['username'], str(task['completed']), task['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(argv[1])
        user_data, todo_data = display_progress(*get_employee_data(employee_id))
        export_to_csv(user_data, todo_data)
