#!/usr/bin/python3
"""Request completed task for a user"""

from asyncio import tasks
import json
import requests
from sys import argv

if __name__ == "__main__":

    todos = "https://jsonplaceholder.typicode.com/todos"
    user = "https://jsonplaceholder.typicode.com/users/{}".format(2)

    data = requests.get(todos).json()
    data_user = requests.get(user).json()
    total_task = 0
    dict_completed = {}
    task_completed = []
    for task in data:
        if task['userId'] == int(argv[1]):
            task_format = {
                'task': task['title'],
                'completed': task['completed'],
                'username': data_user['username']
            }
            task_completed.append(task_format)

    dict_completed[argv[1]] = task_completed
    with open("{}.json".format(argv[1]), 'w',) as file:
        json_string = json.dumps(dict_completed)
        file.write(json_string)
