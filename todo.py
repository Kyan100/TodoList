from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

tasks = []

# LOAD TASKS
try:
    with open("task.txt", "r") as f:
        for line in f:
            task_data = line.strip().split(" | ")

            if len(task_data) == 3:
                tasks.append({
                    "task": task_data[0],
                    "due": task_data[1],
                    "priority": task_data[2]
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
                f"{task['priority']}\n"
            )


# SORT TASKS
def sort_tasks():
    tasks.sort(
        key=lambda task:
        datetime.strptime(task["due"], "%Y-%m-%d")
    )


while True:

    sort_tasks()

    print(Fore.CYAN + "\n====== TO-DO LIST ======")
    print(Fore.YELLOW + "1. View Tasks")
    print(Fore.GREEN + "2. Add Task")
    print(Fore.RED + "3. Remove Task")
    print(Fore.MAGENTA + "4. Exit")

    choice = input(
        Fore.WHITE + "\nChoose an option: "
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

                # OVERDUE CHECK
                if due_date < today:
                    overdue = (
                        Fore.RED +
                        "⚠ OVERDUE"
                    )

                # PRIORITY COLORS
                priority_color = Fore.WHITE

                if task["priority"].lower() == "high":
                    priority_color = Fore.RED

                elif task["priority"].lower() == "medium":
                    priority_color = Fore.YELLOW

                elif task["priority"].lower() == "low":
                    priority_color = Fore.GREEN

                print(
                    Fore.CYAN + f"{i}. "
                    + Fore.WHITE + task["task"]
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
            "priority": priority
        })

        save_tasks()

        print(
            Fore.GREEN +
            "Task added successfully!"
        )

    # REMOVE TASK
    elif choice == "3":

        if len(tasks) == 0:
            print(
                Fore.RED +
                "No tasks to remove."
            )

        else:

            for i, task in enumerate(tasks, start=1):
                print(
                    Fore.CYAN +
                    f"{i}. "
                    + Fore.WHITE +
                    task["task"]
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
                    "Please enter a number."
                )

    # EXIT
    elif choice == "4":

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