task = [] # this is  a list or an array that store the txt file.

#load task from file task.txt
try: 
    with open("task.txt", "r") as f:
        for line in f:
            task.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n ------ To Do List ------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(task) == 0:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for i, t in enumerate(task, 1):
                print(f"{i}. {t}")
        
    elif choice == "2":
        new_task = input("Enter a new task: ")
        task.append(new_task)

        #saeve task to file task.txt
        with open("task.txt", "w") as f:
            for t in task:
                f.write(t + "\n")

        print("Task added successfully.")
    
    elif choice == "3":
        if len(task) == 0:
            print("No task to remove.")
        else:
            print("\nTasks:")
            for i, t in enumerate(task, 1):
                print(f"{i}. {t}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(task):
                    removed_task = task.pop(task_num - 1)

                    #save task to file task.txt
                    with open("task.txt", "w") as f:
                        for t in task:
                            f.write(t + "\n")

                    print(f"Task '{removed_task}' removed successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please choose a valid option.")