#!/usr/bin/python3

"""
0-gather_data_from_an_API.py

Fetches and writes the TODO list progress for a given employee to a CSV file
using a REST API.
"""

import csv
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

    # Write to CSV file
    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"),
                             todo.get("title")])
