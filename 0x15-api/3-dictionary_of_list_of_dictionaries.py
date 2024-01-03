#!/usr/bin/python3

"""
Export JSON data from API endpoints and organize it by user.
"""

from requests import get
import json


def fetch_data(api_url):
    """
    Fetch data from the specified API endpoint.

    Parameters:
    - api_url (str): The URL of the API endpoint.

    Returns:
    - dict: The JSON response.
    """
    response = get(api_url)
    data = response.json()
    return data


def organize_data_by_user(tasks, users):
    """
    Organize tasks data by user.

    Parameters:
    - tasks (list): List of tasks.
    - users (list): List of user data.

    Returns:
    - dict: Organized data by user ID.
    """
    organized_data = {}

    for user in users:
        user_tasks = []
        for task in tasks:
            task_data = {}
            if user['id'] == task['userId']:
                task_data['username'] = user['username']
                task_data['task'] = task['title']
                task_data['completed'] = task['completed']
                user_tasks.append(task_data)

        organized_data[user['id']] = user_tasks

    return organized_data


def export_to_json(filename, data):
    """
    Export organized data to a JSON file.

    Parameters:
    - filename (str): The name of the output JSON file.
    - data (dict): The organized data.

    Returns:
    - None
    """
    with open(filename, "w") as file:
        json_obj = json.dumps(data)
        file.write(json_obj)


if __name__ == "__main__":
    # Fetch tasks and users data
    tasks_data = fetch_data('https://jsonplaceholder.typicode.com/todos/')
    users_data = fetch_data('https://jsonplaceholder.typicode.com/users')

    # Organize tasks data by user
    organized_data = organize_data_by_user(tasks_data, users_data)

    # Export organized data to JSON file
    export_to_json("todo_all_employees.json", organized_data)
