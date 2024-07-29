#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    base_url = 'https://jsonplaceholder.typicode.com'
    user_data = requests.get(f'{base_url}/users/{employee_id}').json()
    todos_data = requests.get(f'{base_url}/users/{employee_id}/todos').json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    filename = f"{employee_id}.json"
    userName = user_data.get("username")

    """Export into json"""
    with open(filename, "w") as f:
        data = {
            employee_id: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": userName,
                }
                for task in todos_data
            ]
        }
        json.dump(data, f)
