#!/usr/bin/python3

"""
Fetches and exports an employee's completed tasks to CSV from the JSONPlaceholder API.

Usage: ./1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys


def main():
    """
    Main function to handle user input, API calls, and data processing.
    """

    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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
        completed_tasks = [(task["title"], str(task["completed"])) for task in todo_list]

        # Write to CSV
        csv_file = f"{employee_id}.csv"
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task, completed in completed_tasks:
                writer.writerow([employee_id, employee['name'], completed, task])

        print(f"CSV file '{csv_file}' has been created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Invalid data format: Missing key '{e}'")


if __name__ == "__main__":
    main()
