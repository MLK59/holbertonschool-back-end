#!/usr/bin/python3

"""
Fetches and exports an employee's completed tasks to JSON from the JSONPlaceholder API.

Usage: ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys


def main():
    """
    Main function to handle user input, API calls, and data processing.
    """

    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
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
        completed_tasks = [{"task": task["title"], "completed": task["completed"], "username": employee['name']} for task in todo_list]

        # Write to JSON
        json_file = f"{employee_id}.json"
        with open(json_file, mode='w') as file:
            json.dump({employee_id: completed_tasks}, file)

        print(f"JSON file '{json_file}' has been created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Invalid data format: Missing key '{e}'")


if __name__ == "__main__":
    main()
