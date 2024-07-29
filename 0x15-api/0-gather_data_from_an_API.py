#!/usr/bin/python3
"""
0-gather_data_from_an_API Module

This module fetches and displays information about an employee's TODO list progress
using a REST API. Given an employee ID, it retrieves the employee's name and their
tasks, indicating how many tasks have been completed and listing the titles of
completed tasks.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>
"""
if __name__ == "__main__":
    from sys import argv
    import requests


    if len(argv) == 2:
        try:
            user_id = argv[1]
            user_id = int(user_id)
        except ValueError:
            exit()

    # GET user info

    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")

    if user.status_code == 200:
        user_data = user.json()

    # GET user task info


    user_task = requests.get(f"https://jsonplaceholder.typicode.com/\
        ?userId={user_id}")

    if user_task.status_code == 200:
        task_data = user_task.json()

    done_tasks = []

    for task in task_data:
        if task['completed']:
            done_tasks.append(task)
        else:
            continue

    print("Employee {} is done with tasks({}/{}):"
        .format(user_data["name"], len(done_tasks), len(task_data)))

    for task in task_data:
        print("\t {}".format(task["title"]))
