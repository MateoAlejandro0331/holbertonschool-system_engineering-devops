#!/usr/bin/python3
"""Request completed task for a user"""

import json
from sys import argv
import requests

if __name__ == "__main__":

    todos = "https://jsonplaceholder.typicode.com/todos"
    user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])

    data = requests.get(todos).json()
    data_user = requests.get(user).json()
    total_task = 0
    task_completed = []

    for task in data:
        if task.get('userId') == int(argv[1]):
            total_task += 1
            if task.get('completed') is True:
                task_completed.append(task)
    line = "Employee {} is done with tasks({}/{}):"\
        .format(data_user['name'], len(task_completed), total_task)
    print(line)
    for instance in task_completed:
        print("\t {}".format(instance.get('title')))
