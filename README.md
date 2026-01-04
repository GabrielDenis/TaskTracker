# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. Built with Python.

**Project URL**: [https://github.com/yourusername/task-tracker-cli](https://github.com/yourusername/task-tracker-cli)

## Features

- **Add** new tasks.
- **List** all tasks or filter by status (todo, in-progress, done).
- **Update** task descriptions.
- **Delete** tasks.
- **Mark** tasks as "in-progress" or "done".
- **Persistent storage** using a JSON file.

## Requirements

- Python 3.x

## Installation

1.  Clone this repository or download the source code.
2.  Navigate to the project directory:
    ```bash
    cd task-tracker-cli
    ```

## Usage

Run the application using `python task_cli.py` followed by a command.

### Add a Task
```bash
python task_cli.py add "Buy groceries"
```

### List Tasks
List all tasks:
```bash
python task_cli.py list
```
Filter by status:
```bash
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress
```

### Update a Task
Provide the Task ID and the new description:
```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task
Provide the Task ID:
```bash
python task_cli.py delete 1
```

### Mark Status
```bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
```

## Project Structure

- `task_cli.py`: The main application script.
- `tasks.json`: The database file where tasks are stored (created automatically).
