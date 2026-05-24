Python To-Do List Application
Overview

This is a simple command-line To-Do List application built using Python. The program allows users to manage daily tasks by adding, viewing, and removing tasks. Tasks are saved into a file so they remain available even after the program is closed.

Features
Add new tasks
View all saved tasks
Remove completed tasks
Save tasks automatically using a text file
Beginner-friendly Python project
Technologies Used
Python 3
File Handling
Lists and Loops
Conditional Statements
How to Run the Program
Install Python on your computer.
Open the project folder in Visual Studio Code or any Python IDE.
Run the Python file:
python todo.py
Example Menu
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
Sample Code Snippet
with open("tasks.txt", "a") as file:
    file.write(task + "\n")
Learning Objectives

This project helps beginners practice:

Python syntax
User input handling
File saving and reading
Basic program organization
Future Improvements
Add task deadlines
Add task priority levels
Create a graphical user interface (GUI)
Add task completion status
Author

Created by Kyan Clerigo as a beginner Python project.
