import os
import time


class TaskList:
    # Turn functions into methods
    # Add self as first parameter so they can access the instance's data
    def __init__(self):
        self.tasks = []

    # Add Task Logic
    def add_task(self):
        while True:
            self.clear_terminal()
            task_title = input("Enter Task (or 'q' to cancel): \n").title().strip()
            if task_title.lower() == "q":
                print("Add task canceled")
                time.sleep(1.5)
                break       
            elif task_title in self.tasks:
                print("Warning: Task already exists.")
                time.sleep(1.5)
            else:
                self.tasks.append(task_title)
                print("Task added!")
                time.sleep(1.5)
                break
    
    # Edit Tasks Logic
    def edit_task(self):
        while True: 
            self.clear_terminal()
            user_input = input(
                "Select from the list of options:\n" \
                "[1]: Edit Task Property\n" \
                "[2]: Remove Task\n" \
                "[3]: Clear Task List\n" \
                "[4]: Main Menu\n")
            if user_input == "1":
                self.edit_task_property()
            elif user_input == "2":
                self.remove_task()
            elif user_input == "3":
                self.clear_task_list()
            elif user_input == "4":
                break # goes back to run_system()
            else: 
                print("Invalid Input: Please enter one of the options above.")
                time.sleep(1.5)

    # View Task Logic
    def view_task(self):
        self.clear_terminal()
        pass

    # Clear terminal logic
    def clear_terminal(self):
        # os.system runs a terminal command
        # conditional operator chooses the terminal command based on the users OS
        os.system("cls" if os.name == "nt" else "clear")

    # Display Tasks Logic
    def display_task(self):
        pass

    # Edit Task Property Logic
    def edit_task_property(self):
        self.clear_terminal()
        # display tasks here
        # ask user which task they would like to edit
        pass

    # Remove Task Logic
    def remove_task(self):
        pass

    # Clear Task Logic
    def clear_task_list(self):
        pass

    # Existing Task Logic
    