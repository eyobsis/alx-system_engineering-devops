#!/usr/bin/python3
"""
This script retrieves and displays information about
an employee's TODO list progress using a given employee ID.
It also exports the data in CSV format.
"""

import csv
import requests
from sys import argv


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


def display_progress(user_data, todo_data):
    """Display employee TODO list progress."""
    total_tasks = len(todo_data)
    done_tasks = sum(task['completed'] for task in todo_data)
    a = total_tasks
    b = done_tasks
    print(f"Employee {user_data['name']} is done with tasks({b}/{a}):")
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
        for task in todo_data:
            j = str(task['completed'])
            a = [user_id, user_data['username'], j, task['title']]
            csv_writer.writerow(a)
    print(f"Data exported to {csv_filename}")


def export_to_json(user_data, todo_data):
    """Export data to JSON file."""
    user_id = str(user_data['id'])
    json_filename = f"{user_id}.json"
    json_data = {user_id: []}
    for task in todo_data:
        json_data[user_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(argv[1])
        id = employee_id
        user_data, todo_data = display_progress(*get_employee_data(id))
        export_to_csv(user_data, todo_data)
        export_to_json(user_data, todo_data)
