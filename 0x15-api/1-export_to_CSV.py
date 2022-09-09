#!/usr/bin/python3
"""Request completed task for a user"""

import csv
import json
from urllib import request
from sys import argv

if __name__ == "__main__":
    todos = "https://jsonplaceholder.typicode.com/todos"
    user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    with request.urlopen(todos) as response:
        total_task = 0
        content = response.read()
        content = content.decode('utf8').replace("'", '"')
        data = json.loads(content)
    with request.urlopen(user) as User:
        content_user = User.read()
        content_user = content_user.decode('utf8').replace("'", '"')
        data_u = json.loads(content_user)

    csvfile = "{}.csv".format(argv[1])
    with open(csvfile, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_NONNUMERIC)

        task_completed = []
        for task in data:
            if task.get('userId') == int(argv[1]):
                userid = str(task.get('userId'))
                completed = str(task.get('completed'))
                writer.writerow([userid, data_u['username'],
                                completed, task.get('title')])
