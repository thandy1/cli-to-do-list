# Gives access to operating system commands
import os
# Imports TaskList class from task_class.py
from task_class import TaskList

# Use the instance (todo) to access the methods
todo = TaskList() 

# Main function call to launch the system or close
def main():
    todo.clear_terminal()
    user_input = input(f"Welcome! Would you like to launch the system? \n[1]: Yes\n[2]: No\n")
    if user_input == "1":
        run_system()
    elif user_input == "2":
        todo.exit_system()
    else:
        print("Invalid Input")
        pass    

# System launch logic
def run_system():
    todo.clear_terminal()
    user_input = input(
        "Select from the list of options:\n" \
        "[1]: Add New Task\n" \
        "[2]: Edit Task List\n" \
        "[3]: View Task List\n" \
        "[4]: Exit\n")
    if user_input == "1":
        todo.add_task()

# Function call to begin the program
main()