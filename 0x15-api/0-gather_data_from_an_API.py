#!/usr/bin/python3
"""0-gather_data_from_an_API Module"""
if __name__ == "__main__":
    import requests
    from sys import argv

    user_id = argv[1]
    # GET user info
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()

    # GET user task info
    user_task = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}").json()

    # GET completed tasks of the user
    done_tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}&completed=true").json()

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(user_task)))

    for task in user_task:
        print("\t "+task.get("title"))
