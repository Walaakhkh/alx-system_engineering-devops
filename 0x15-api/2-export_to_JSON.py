#!/usr/bin/python3

"""
0-gather_data_from_an_API.py

Fetches and writes the TODO list progress for a given employee to a JSON file
using a REST API.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(f"{url}users/{user_id}")
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user = user_response.json()
    username = user.get("username")

    # Fetch todos data
    todos_response = requests.get(f"{url}todos", params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Todos not found")
        sys.exit(1)

    todos = todos_response.json()

    # Prepare data for JSON export
    data_to_export = {user_id: []}

    for todo in todos:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        data_to_export[user_id].append(task_info)

    # Write to JSON file
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
