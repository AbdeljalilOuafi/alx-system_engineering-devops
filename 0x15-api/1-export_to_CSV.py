#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    base_url = 'https://jsonplaceholder.typicode.com'
    user_data = requests.get(f'{base_url}/users/{employee_id}').json()
    todos_data = requests.get(f'{base_url}/users/{employee_id}/todos').json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    filename = f"{employee_id}.csv"
    userName = user_data.get("username")

    """Export into csv"""
    with open(filename, 'w') as f:
        for todo in todos_data:
            data = f'"{employee_id}","{userName}","{todo.get("completed")}",'
            data2 = f'"{todo.get("title")}"\n'
            f.write(data+data2)
