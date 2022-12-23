# -*- coding: utf-8 -*-
# Code copied from https://github.com/Doist/todoist-api-python

from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI


def main():
    create_task()


# Fetch tasks asynchronously
async def get_tasks_async():
    api = TodoistAPIAsync("ca1e79a4844418ee1fe0ad6a49953e60becc03dd")
    try:
        tasks = await api.get_tasks()
        print(tasks)
    except Exception as error:
        print(error)


# Fetch tasks synchronously
def get_tasks_sync():
    api = TodoistAPI("ca1e79a4844418ee1fe0ad6a49953e60becc03dd")
    try:
        tasks = api.get_tasks()
        print(tasks)
    except Exception as error:
        print(error)


def create_task():
    api = TodoistAPI("ca1e79a4844418ee1fe0ad6a49953e60becc03dd")
    try:
        task = api.add_task(content="Test task")
        print(task)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
