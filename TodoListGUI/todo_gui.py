import tkinter as tk
from tkinter import messagebox

tasks = []


# ADD TASK
def add_task():

    task = task_entry.get()

    if task != "":

        tasks.append(task)

        update_listbox()

        task_entry.delete(0, tk.END)

    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a task."
        )


# REMOVE TASK
def remove_task():

    try:

        selected = task_listbox.curselection()[0]

        tasks.pop(selected)

        update_listbox()

    except:
        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )


# UPDATE LISTBOX
def update_listbox():

    task_listbox.delete(0, tk.END)

    for task in tasks:

        task_listbox.insert(
            tk.END,
            task
        )


# MAIN WINDOW
root = tk.Tk()

root.title("To-Do List")

root.geometry("400x500")

root.resizable(False, False)


# TITLE
title_label = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=10)


# ENTRY
task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)

task_entry.pack(pady=10)


# ADD BUTTON
add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    width=15,
    command=add_task
)

add_button.pack(pady=5)


# REMOVE BUTTON
remove_button = tk.Button(
    root,
    text="Remove Task",
    font=("Arial", 12),
    width=15,
    command=remove_task
)

remove_button.pack(pady=5)


# TASK LISTBOX
task_listbox = tk.Listbox(
    root,
    font=("Arial", 12),
    width=35,
    height=15
)

task_listbox.pack(pady=20)


# RUN APP
root.mainloop()