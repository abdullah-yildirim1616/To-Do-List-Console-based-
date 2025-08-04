import json
import os

FILE_NAME = "tasks.txt"
tasks = []

def load_tasks_from_file():
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []

def save_tasks_to_file():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def add_task():
    text = input("Enter the task: ")
    tasks.append({"text": text, "completed": False})
    print("Task added.")
    save_tasks_to_file()

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}.[{status}] {task['text']}")

def delete_task():
    list_tasks()
    try:
        choice = int(input("Enter the number of the task to delete: "))
        tasks.pop(choice - 1)
        print("Task deleted.")
        save_tasks_to_file()
    except:
        print("Invalid input!")

def complate_task():
    list_tasks()
    try:
        choice = int(input("Enter the number of the completed task: "))
        tasks[choice - 1]["completed"] = True
        print("Task marked as completed.")
        save_tasks_to_file
    except:
        print("Invalid input!")

load_tasks_from_file()

while True:
    print("\n--- TO-DO LİST ---")
    print("1 - Add Task")
    print("2 - List Tasks")
    print("3 - Delete Task")
    print("4 - Complete Task")
    print("5 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        complate_task()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")