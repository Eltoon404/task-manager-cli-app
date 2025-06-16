import json
import os

# Path to your local task storage file
TASKS_FILE = "tasks.json"

def load_tasks():
    #Load tasks from the JSON file.
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def add_task(description, due_date=None, priority=None):
    #Add a new task.
    tasks = load_tasks()
    task_id = 1 if not tasks else tasks[-1]['id'] + 1
    task = {
        "id": task_id,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print(f"Task added: {description}")