import os
import time
from datetime import datetime
import sys

# This class represents a single task
class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date

# This class manages a list of task objects, handles add/edit/load/save
class TaskList:
    # Turn functions into methods
    # Add self as first parameter so they can access the instance's data
    def __init__(self):
        self.tasks = []   # List of task objects
        

    # Add Task 
    def add_task(self, console):
        while True:
            self.clear_terminal()
            print("Current Tasks:")
            print()
            self.display_task()
            print() # Extra space to separate tasks from input

            title = self.get_task_title(console)
            if title is None:
                break

            priority = self.get_priority(console)
            if priority is None:
                break

            due_date = self.get_due_date(console)
            if due_date is None:
                break

            new_task = Task(title, priority, due_date)
            self.tasks.append(new_task)

            console.print(f"[bold green]Task added successfully![/]")
            time.sleep(1)   
            
               
    
    # Edit Tasks 
    def edit_task(self, console):
        while True: 
            self.clear_terminal()
            print("Current Tasks:")
            print()
            self.display_task()
            print() # Extra space to separate tasks from input

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
                console.print("[bold red]Invalid Input[/]")
                time.sleep(1)

    # View Task 
    def view_task(self):
        self.clear_terminal()
        print("Current Tasks:")
        print()
        self.display_task()
        print() # Extra space to separate tasks from input
        pass

    # Clear terminal 
    def clear_terminal(self):
        # os.system runs a terminal command
        # conditional operator chooses the terminal command based on the users OS
        os.system("cls" if os.name == "nt" else "clear")

    # Display Tasks 
    def display_task(self):
        for i, task in enumerate(self.tasks, start=1):
                print(f"\t{i}. {task.title} | Priority: {task.priority} | Due: {task.due_date}")

    # Edit Task Property 
    def edit_task_property(self):
        self.clear_terminal()
        # display tasks here
        # ask user which task they would like to edit
        pass

    # Filter Task
    def filter_task(self):
        pass
    
    # Remove Task 
    def remove_task(self):
        pass

    # Clear Task 
    def clear_task_list(self):
        pass

    # Existing Task
    def existing_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return True
        return False

    # Load Tasks 
    def load_tasks(self):
        pass

    # Save Tasks 
    def save_tasks(self):
        pass

    # Get Task Title
    def get_task_title(self, console):
        while True:
            task_title = input("Enter Task Title or 'q' to cancel: ").strip()
            if task_title.lower() == "q":
                return None 
            
            if self.existing_task(task_title):
                    console.print("[bold red]Warning: Task already exists.[/]")
                    time.sleep(1)
                    self.clear_last_two_lines()
                    continue    # Go back to the start of the loop
            
            return task_title.title()
    
    # Get Due Date 
    def get_due_date(self, console):
        while True:
            task_due_date = input("Enter Due Date (YYYY-MM-DD) or 'q' to cancel: ").strip()
            if task_due_date.lower() == "q":
                return None
            try:
                # try to parse the string into a datetime object according to format
                parsed_date = datetime.strptime(task_due_date, "%Y-%m-%d")
                # Convert the datetime back to a string before passing it to Task
                return parsed_date.strftime("%Y-%m-%d")
            except ValueError:
                # parsing failed, invalid format
                console.print("[bold red]Invalid date format.[/]")
                time.sleep(1)
                self.clear_last_two_lines()
                continue

    # Get Priority 
    def get_priority(self, console):
        while True:
            task_priority = input("Enter Priority (Low/Medium/High) or 'q' to cancel: ").strip()
            if task_priority.lower() == "q":
                return None
            elif task_priority.lower() not in ["low", "medium", "high"]:
                # Show warning below
                # Console object prints warning message with bold red font color
                console.print("[bold red]Warning: Invalid Input[/]")
                time.sleep(1)
                self.clear_last_two_lines()
                continue
            else:
                return task_priority.title()
            
    # Help function to clear lines
    def clear_last_two_lines(self):
        sys.stdout.write("\033[F\033[K")
        sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

        