import sys
import os
import json
from datetime import datetime

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    else:
        return []

def add_task(description):
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
    print(f"Task added successfully: {new_task['id']}")

def main():
    args = sys.argv

    if len(args) < 2:
        print("Uso: python task_cli.py <comando> [argumentos]")

        return

    command = args[1]

    if command == "add":
        if len(args) < 3:
            print("Error: Debes poner una descripcion. Ej: python task_cli.py add 'Comprar leche'")
        else:
            add_task(args[2])

    print(f"Comando recibido: {command}")

if __name__ == "__main__":
    main()