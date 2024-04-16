#!bin/user/python3

import requests
import sys

def fetch_todo_progress(employee_id):
    # API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetching data from the API
    response = requests.get(url)
    todos = response.json()

    # Counting completed and total tasks
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Getting employee name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee_name = user_response.json()['name']

    # Printing progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
