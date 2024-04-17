#!/usr/bin/python3

"""
Fetches and displays an employee's completed tasks from the JSONPlaceholder API.

Usage: ./0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def main():
    """
    Main function to handle user input, API calls, and data processing.
    """

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    api_url = "https://jsonplaceholder.typicode.com/"

    try:
        # Get employee information
        employee_response = requests.get(f"{api_url}users/{employee_id}")
        employee_response.raise_for_status()  # Raise exception for non-2xx responses
        employee = employee_response.json()

        # Get todo list
        todo_list_response = requests.get(f"{api_url}todos?userId={employee_id}")
        todo_list_response.raise_for_status()
        todo_list = todo_list_response.json()

        # Filter completed tasks
        completed_tasks = [task["title"] for task in todo_list if task["completed"]]

        # Display progression
        total_tasks = len(todo_list)
        completed_count = len(completed_tasks)
        print(f"Employee {employee['name']} is done with tasks ({completed_count}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t {task}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Invalid data format: Missing key '{e}'")


if __name__ == "__main__":
    main()
