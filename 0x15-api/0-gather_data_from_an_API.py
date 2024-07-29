#!/usr/bin/python3
"""0-gather_data_from_an_API Module"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 2:
        try:
            user_id = argv[1]
            user_id = int(user_id)
        except ValueError:
            exit()

    # GET user info
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))

    if user.status_code == 200:
        user_data = user.json()
    else:
        print("Error occured fetching user")
        print("Status code: {}".format(user.status_code))
        exit()

    # GET user task info
    user_task = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")

    if user_task.status_code == 200:
        task_data = user_task.json()
    else:
        print("Error occured fetching user task")
        exit()

    done_tasks = []

    for task in task_data:
        if task['completed']:
            done_tasks.append(task)
        else:
            continue

    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], len(done_tasks), len(task_data)))

    for task in task_data:
        print("\t {}".format(task["title"]))
