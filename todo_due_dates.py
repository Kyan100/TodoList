tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            task_data = line.strip().split(" | ")
            tasks.append({
                "task": task_data[0],
                "due": task_data[1]
            })
except FileNotFoundError:
    pass

while True:
    print("\n--- TO-DO LIST ---")
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
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} (Due: {task['due']})")

    # ADD TASK
    elif choice == "2":
        new_task = input("Enter task: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        tasks.append({
            "task": new_task,
            "due": due_date
        })

        # Save to file
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"{task['task']} | {task['due']}\n")

        print("Task added!")

    # REMOVE TASK
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} (Due: {task['due']})")

            remove = int(input("Enter task number to remove: "))

            if 1 <= remove <= len(tasks):
                deleted = tasks.pop(remove - 1)

                # Save updated file
                with open("tasks.txt", "w") as file:
                    for task in tasks:
                        file.write(f"{task['task']} | {task['due']}\n")

                print(f"Removed: {deleted['task']}")
            else:
                print("Invalid number.")

    # EXIT
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")