#!/usr/bin/python3

"""
Fetches and exports an employee's completed tasks to JSON from the JSONPlaceholder API.
"""

import json
import requests
import sys

def fetch_todo_data():
    """
    Fetches user and todo data from JSONPlaceholder API.

    Returns:
        tuple: A tuple containing lists of user data and todo data.
    """
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    users = response_users.json()
    todos = response_todos.json()

    return users, todos

def generate_todo_dict(users, todos):
    """
    Generates a dictionary of todos for each user.

    Args:
        users (list): List of user data dictionaries.
        todos (list): List of todo data dictionaries.

    Returns:
        dict: A dictionary where keys are user IDs and values are lists of todo dictionaries.
    """
    todo_dict = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        todo_dict[user_id] = []
        for todo in todos:
            if todo['userId'] == user_id:
                todo_dict[user_id].append({
                    'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']
                })

    return todo_dict

def write_todo_json(todo_dict):
    """
    Writes todo data dictionary to a JSON file.

    Args:
        todo_dict (dict): Dictionary containing todo data.
    """
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_dict, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    # Fetch data from API
    users, todos = fetch_todo_data()

    # Generate todo dictionary
    todo_dict = generate_todo_dict(users, todos)

    # Write todo dictionary to JSON file
    write_todo_json(todo_dict)
