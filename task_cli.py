import sys
import os
import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def save_tasks(tasks):
    """Saves the list of tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def add_task(description):
    """Adds a new task with the given description."""
    tasks = load_tasks()

    if tasks:
        new_id = tasks[-1]["id"] + 1
    else:
        new_id = 1

    now = datetime.now().isoformat()
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def list_tasks(filter_status=None):
    """Lists tasks, optionally filtered by status (todo, in-progress, done)."""
    tasks = load_tasks()

    if tasks:
        for task in tasks:
            if filter_status and task["status"] != filter_status:
                continue
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print("No tasks found.")

def update_task(id, description):
    """Updates the description of the task with the given ID."""
    tasks = load_tasks()

    if tasks:
        for task in tasks:
            if task["id"] == id:
                task["description"] = description
                task["updatedAt"] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task updated successfully: {id}")
                return

        print(f"Task with ID {id} not found.")

def delete_task(id):
    """Deletes the task with the given ID."""
    tasks = load_tasks()

    if tasks:
        for task in tasks:
            if task["id"] == id:
                tasks.remove(task)
                save_tasks(tasks)
                print(f"Task deleted successfully: {id}")
                return

        print(f"Task with ID {id} not found.")

def mark_task(id, status):
    """Updates the status of the task with the given ID."""
    tasks = load_tasks()

    if tasks:
        for task in tasks:
            if task["id"] == id:
                task["status"] = status
                task["updatedAt"] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task marked successfully: {id}")
                return

        print(f"Task with ID {id} not found.")
    else:
        print("No tasks found.")

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        return

    command = args[1]

    if command == "add":
        if len(args) < 3:
            print("Error: You must provide a description. e.g.: python task_cli.py add 'Buy milk'")
        else:
            add_task(args[2])

    elif command == "list":
        if len(args) > 2:
            list_tasks(args[2])
        else:
            list_tasks()

    elif command == "update":
        if len(args) < 4:
            print("Error: You must provide an ID and a description. e.g.: python task_cli.py update 1 'Buy milk'")
        else:
            update_task(int(args[2]), args[3])

    elif command == "delete":
        if len(args) < 3:
            print("Error: You must provide an ID. e.g.: python task_cli.py delete 1")
        else:
            delete_task(int(args[2]))

    elif command == "mark-in-progress" or command == "mark-done":
        if len(args) < 3:
            print("Error: You must provide an ID. e.g.: python task_cli.py mark-in-progress 1")
        else:
            if command == "mark-in-progress":
                mark_task(int(args[2]), "in-progress")
            else:
                mark_task(int(args[2]), "done")
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()