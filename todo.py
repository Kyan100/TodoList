# File name: advanced_todo.py

from datetime import datetime

tasks = []

# LOAD TASKS
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            task_data = line.strip().split(" | ")

            tasks.append({
                "task": task_data[0],
                "due": task_data[1],
                "priority": task_data[2]
            })

except FileNotFoundError:
    pass


# SAVE FUNCTION
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(
                f"{task['task']} | {task['due']} | {task['priority']}\n"
            )


# SORT TASKS BY DATE
def sort_tasks():
    tasks.sort(
        key=lambda task: datetime.strptime(task["due"], "%Y-%m-%d")
    )


while True:

    sort_tasks()

    print("\n--- ADVANCED TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    # VIEW TASKS
    if choice == "1":

        if len(tasks) == 0:
            print("No tasks found.")

        else:
            print("\nYour Tasks:\n")

            today = datetime.today()

            for i, task in enumerate(tasks, start=1):

                due_date = datetime.strptime(
                    task["due"],
                    "%Y-%m-%d"
                )

                overdue = ""

                if due_date < today:
                    overdue = "⚠️ OVERDUE"

                print(
                    f"{i}. {task['task']}"
                    f"\n   Due: {task['due']}"
                    f"\n   Priority: {task['priority']}"
                    f"\n   {overdue}\n"
                )

    # ADD TASK
    elif choice == "2":

        new_task = input("Enter task: ")

        due_date = input(
            "Enter due date (YYYY-MM-DD): "
        )

        priority = input(
            "Enter priority (Low / Medium / High): "
        )

        tasks.append({
            "task": new_task,
            "due": due_date,
            "priority": priority
        })

        save_tasks()

        print("Task added!")

    # REMOVE TASK
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove.")

        else:

            for i, task in enumerate(tasks, start=1):
                print(
                    f"{i}. {task['task']} "
                    f"({task['priority']})"
                )

            remove = int(
                input("Enter task number to remove: ")
            )

            if 1 <= remove <= len(tasks):

                deleted = tasks.pop(remove - 1)

                save_tasks()

                print(
                    f"Removed: {deleted['task']}"
                )

            else:
                print("Invalid number.")

    # EXIT
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")