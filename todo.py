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
            for idx, t in enumerate(task, 1):
                print(f"{idx}. {t}")