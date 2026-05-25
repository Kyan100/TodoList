from datetime import datetime
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

tasks = []

# LOAD TASKS
try:
    with open("task.txt", "r") as f:
        for line in f:

            task_data = line.strip().split(" | ")

            if len(task_data) == 4:

                tasks.append({
                    "task": task_data[0],
                    "due": task_data[1],
                    "priority": task_data[2],
                    "completed": task_data[3] == "True"
                })

except FileNotFoundError:
    pass


# SAVE TASKS
def save_tasks():

    with open("task.txt", "w") as f:

        for task in tasks:

            f.write(
                f"{task['task']} | "
                f"{task['due']} | "
                f"{task['priority']} | "
                f"{task['completed']}\n"
            )


# SORT TASKS
def sort_tasks():

    tasks.sort(
        key=lambda task:
        datetime.strptime(
            task["due"],
            "%Y-%m-%d"
        )
    )


while True:

    sort_tasks()

    print(Fore.CYAN + "\n====== TO-DO LIST ======")
    print(Fore.YELLOW + "1. View Tasks")
    print(Fore.GREEN + "2. Add Task")
    print(Fore.BLUE + "3. Complete Task")
    print(Fore.RED + "4. Remove Task")
    print(Fore.MAGENTA + "5. Exit")

    choice = input(
        Fore.WHITE +
        "\nChoose an option: "
    )

    # VIEW TASKS
    if choice == "1":

        if len(tasks) == 0:

            print(
                Fore.RED +
                "No tasks found."
            )

        else:

            print(
                Fore.CYAN +
                "\n===== YOUR TASKS =====\n"
            )

            today = datetime.today()

            for i, task in enumerate(tasks, start=1):

                due_date = datetime.strptime(
                    task["due"],
                    "%Y-%m-%d"
                )

                overdue = ""

                if (
                    due_date < today
                    and not task["completed"]
                ):
                    overdue = (
                        Fore.RED +
                        "⚠ OVERDUE"
                    )

                # CHECKBOX
                checkbox = "❌"

                if task["completed"]:
                    checkbox = "✅"

                # PRIORITY COLOR
                priority_color = Fore.WHITE

                if task["priority"].lower() == "high":
                    priority_color = Fore.RED

                elif task["priority"].lower() == "medium":
                    priority_color = Fore.YELLOW

                elif task["priority"].lower() == "low":
                    priority_color = Fore.GREEN

                print(
                    Fore.CYAN +
                    f"{i}. "
                    + checkbox +
                    " "
                    + Fore.WHITE +
                    task["task"]
                )

                print(
                    Fore.BLUE +
                    f"   Due: {task['due']}"
                )

                print(
                    priority_color +
                    f"   Priority: {task['priority']}"
                )

                if overdue:
                    print(overdue)

                print()

    # ADD TASK
    elif choice == "2":

        new_task = input(
            Fore.WHITE +
            "Enter task: "
        )

        due_date = input(
            Fore.WHITE +
            "Enter due date (YYYY-MM-DD): "
        )

        priority = input(
            Fore.WHITE +
            "Enter priority (Low/Medium/High): "
        )

        tasks.append({
            "task": new_task,
            "due": due_date,
            "priority": priority,
            "completed": False
        })

        save_tasks()

        print(
            Fore.GREEN +
            "Task added successfully!"
        )

    # COMPLETE TASK
    elif choice == "3":

        if len(tasks) == 0:

            print(
                Fore.RED +
                "No tasks available."
            )

        else:

            for i, task in enumerate(tasks, start=1):

                status = "✅" if task["completed"] else "❌"

                print(
                    f"{i}. {status} {task['task']}"
                )

            try:

                complete = int(input(
                    Fore.WHITE +
                    "Enter task number to complete: "
                ))

                if 1 <= complete <= len(tasks):

                    tasks[complete - 1]["completed"] = True

                    save_tasks()

                    print(
                        Fore.GREEN +
                        "Task marked as completed!"
                    )

                else:

                    print(
                        Fore.RED +
                        "Invalid task number."
                    )

            except ValueError:

                print(
                    Fore.RED +
                    "Please enter a valid number."
                )

    # REMOVE TASK
    elif choice == "4":

        if len(tasks) == 0:

            print(
                Fore.RED +
                "No tasks to remove."
            )

        else:

            for i, task in enumerate(tasks, start=1):

                print(
                    f"{i}. {task['task']}"
                )

            try:

                remove = int(input(
                    Fore.WHITE +
                    "Enter task number to remove: "
                ))

                if 1 <= remove <= len(tasks):

                    deleted = tasks.pop(remove - 1)

                    save_tasks()

                    print(
                        Fore.GREEN +
                        f"Removed: {deleted['task']}"
                    )

                else:

                    print(
                        Fore.RED +
                        "Invalid task number."
                    )

            except ValueError:

                print(
                    Fore.RED +
                    "Please enter a valid number."
                )

    # EXIT
    elif choice == "5":

        print(
            Fore.MAGENTA +
            "Goodbye!"
        )

        break

    else:

        print(
            Fore.RED +
            "Invalid option."
        )