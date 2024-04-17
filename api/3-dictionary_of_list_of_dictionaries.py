#!/bin/user/python3

import json
import requests
from sys import argv


def export_user_tasks(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()
    user_info = {}

    for task in tasks:
        user_info.setdefault(str(user_id), []).append({
            "username": users[user_id],
            "task": task["title"],
            "completed": task["completed"]
        })

    return user_info


def export_all_tasks():
    all_tasks = {}
    for user_id in users.keys():
        all_tasks.update(export_user_tasks(user_id))
    return all_tasks


def export_to_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()
    users = {user["id"]: user["username"] for user in users_data}

    if len(argv) == 1:
        all_tasks = export_all_tasks()
        export_to_json("todo_all_employees.json", all_tasks)
        print("Data exported to todo_all_employees.json")
    elif len(argv) == 2:
        user_id = int(argv[1])
        user_tasks = export_user_tasks(user_id)
        file_name = f"{user_id}.json"
        export_to_json(file_name, user_tasks)
        print(f"Data exported to {file_name}")
    else:
        print("Usage: python3 <script_name> [USER_ID]")
