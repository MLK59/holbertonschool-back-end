#!/bin/user/python3

import requests
import sys

def fetch_todo_progress(employee_id):
    """
    Fetches to-do progress information for a given employee ID from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee whose progress to be retrieved.

    Returns:
        None
    """

    # API endpoints for user and to-do list (using f-strings)
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user information (including name)
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise an exception for non-2xx status codes
        user_data = user_response.json()
        employee_name = user_data['name']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user information: {e}")
        sys.exit(1)

    # Fetch to-do list
    try:
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todos = todo_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching to-do list: {e}")
        sys.exit(1)

    # Calculate completed and total tasks
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Print progress report
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_progress(employee_id)
    except ValueError:
        print("Error: Invalid employee ID (must be an integer).")
        sys.exit(1)
