import os
import time
from datetime import datetime

# This class represents a single task
class Task:
    def __init__(self, title, priority="Low", due_date=""):
        self.title = title
        self.priority = priority
        self.due_date = due_date

# This class manages a list of Task objects, handles add/edit/load/save
class TaskList:
    # Turn functions into methods
    # Add self as first parameter so they can access the instance's data
    def __init__(self):
        self.tasks = []   # List of Task objects

    # Add Task 
    def add_task(self):
        while True:
            self.clear_terminal()
            print("Current Tasks:\n")
            self.display_task()

            title = self.get_task_title()
            if title is None:
                break
            elif title in self.tasks:
                print("Warning: Task already exists.")
                time.sleep(1.5)
                continue    # Go back to the start of the loop

            priority = self.get_priority()
            if priority is None:
                break

            due_date = self.get_due_date()
            if due_date is None:
                break

            new_task = Task(title, priority, due_date)
            self.tasks.append(new_task)
               
    
    # Edit Tasks 
    def edit_task(self):
        while True: 
            self.clear_terminal()
            print("Current Tasks:\n")
            self.display_task()

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

    # View Task 
    def view_task(self):
        self.clear_terminal()
        pass

    # Clear terminal 
    def clear_terminal(self):
        # os.system runs a terminal command
        # conditional operator chooses the terminal command based on the users OS
        os.system("cls" if os.name == "nt" else "clear")

    # Display Tasks 
    def display_task(self):
        for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task.title}")

    # Edit Task Property 
    def edit_task_property(self):
        self.clear_terminal()
        # display tasks here
        # ask user which task they would like to edit
        pass

    # Remove Task 
    def remove_task(self):
        pass

    # Clear Task 
    def clear_task_list(self):
        pass

    # Existing Task 
    
    # Load Tasks 
    def load_tasks(self):
        pass

    # Save Tasks 
    def save_tasks(self):
        pass

    # Get Task Title
    def get_task_title(self):
        task_title = input("\nEnter Task Title or 'q' to cancel: ").strip()
        if task_title.lower() == "q":
            return None # signal to cancel
        return task_title.title()
    
    # Get Due Date 
    def get_due_date(self):
        while True:
            task_due_date = input("\nEnter Due Date (YYYY-MM-DD) or 'q' to cancel: ").strip()
            if task_due_date.lower() == "q":
                return None
            try:
                # try to parse the string into a datetime object according to format
                parsed_date = datetime.strptime(task_due_date, "%Y-%m-%d")
                # Convert the datetime back to a string before passing it to Task
                return parsed_date.strftime("%Y-%m-%d")
            except ValueError:
                # parsing failed, invalid format
                print("Invalid date format.")
                time.sleep(1.5)
                continue

    
    # Get Priority 
    def get_priority(self):
        while True:
            task_priority = input("\nEnter Priority (Low/Medium/High) or 'q' to cancel: ").strip()
            if task_priority.lower() == "q":
                return None
            elif task_priority.lower() not in ["low", "medium", "high"]:
                print("Warning: Invalid Input")
                time.sleep(1.5)
                continue
            else:
                return task_priority.title()
    