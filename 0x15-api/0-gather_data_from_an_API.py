#!/usr/bin/python3

"""
0-gather_data_from_an_API.py

Fetches and displays the TODO list progress for a given employee
using a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_response = requests.get(f"{url}users/{employee_id}")

    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user = user_response.json()

    todos_response = requests.get(f"{url}todos", params=
            {"userId": employee_id})

    if todos_response.status_code != 200:
        print("Todos not found")
        sys.exit(1)

    todos = todos_response.json()

    completed = [
        todo.get("title") for todo in todos if todo.get("completed")
    ]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(completed),
        len(todos)
    ))

    for complete in completed:
        print("\t {}".format(complete))
