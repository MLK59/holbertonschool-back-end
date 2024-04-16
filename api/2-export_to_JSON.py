import requests
import sys
import json

def fetch_todo_progress(employee_id):
    # API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetching data from the API
    response = requests.get(url)
    todos = response.json()

    # Getting employee name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee_name = user_response.json()['name']

    # Constructing data for JSON export
    data = {
        str(employee_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            for todo in todos
        ]
    }

    # Exporting data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
