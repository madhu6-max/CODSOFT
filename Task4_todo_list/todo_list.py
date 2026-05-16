import json
import os

tasks = []

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


# Load tasks
def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)


# Add task
def add_task():
    title = input("Enter task name: ")
    priority = input("Priority (High/Medium/Low): ")
    due_date = input("Due date: ")
    task = {"title": title,"priority": priority,"due": due_date,"status": "Pending"}
    tasks.append(task)
    save_tasks()
    print("\nTask Added Successfully!")


# View tasks
def view_tasks():

    if len(tasks) == 0:
        print("No Tasks Found")
    else:
        print("\n===== TASK LIST =====")

        for i, task in enumerate(tasks, start=1):
            print(f"""{i}. Task      : {task['title']}
   Priority  : {task['priority']}
   Due Date  : {task['due']}
   Status    : {task['status']}
-----------------------
""")


# Remove task
def remove_task():

    view_tasks()
    if len(tasks) == 0:
        return

    num = int(input("Task number: "))

    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        save_tasks()
        print("Task Removed")
    else:
        print("Invalid Task Number")


# Mark complete
def complete_task():

    view_tasks()
    if len(tasks) == 0:
        return

    num = int(input("Task number completed: "))

    if 1 <= num <= len(tasks):
        tasks[num - 1]["status"] = "Completed"
        save_tasks()
        print("Task Completed")
    else:
        print("Invalid Task Number")


# Search task
def search_task():

    keyword = input("Search: ")
    found = False

    for task in tasks:
        if keyword.lower() in task["title"].lower():
            print(task)
            found = True

    if not found:
        print("No Task Found")


# Main program
load_tasks()
while True:

    print("""======== TO DO APP ========

1 Add Task
2 View Tasks
3 Remove Task
4 Complete Task
5 Search Task
6 Exit

===========================""")

    choice = input("Choose: ")
    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        search_task()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")