import os
import time
from datetime import datetime, timedelta

# This class represents a single task
class Task:
    def __init__(self, title, days_to_complete):
        self.title = title
        self.days_to_complete = days_to_complete
        self.due_date = datetime.now() + timedelta(days=days_to_complete)
        # automatically calculate priority
        self.priority = self.set_priority()

    def set_priority(self):
        if self.days_to_complete <= 2:
            return "High"
        elif self.days_to_complete <= 5:
            return "Medium"
        else:
            return "Low"
        
# This class manages a list of task objects, handles add/edit/load/save
class TaskList:
    # Add self as first parameter so they can access the instance's data
    def __init__(self):
        self.tasks = []   # List of task objects
        
    def clear_terminal(self):
        # os.system runs a terminal command
        # conditional operator chooses the terminal command based on the users OS
        os.system("cls" if os.name == "nt" else "clear")

    def display_task(self):
        for i, task in enumerate(self.tasks, start=1):
                # Format for nice display
                due_date = task.due_date.strftime("%Y-%m-%d") 
                print(f"\t{i}. {task.title} | Priority: {task.priority} | Due: {due_date}")

    def edit_task_property(self):
        self.clear_terminal()
        # display tasks here
        # ask user which task they would like to edit
        pass

    def filter_task(self):
        pass
    
    def remove_task(self):
        pass

    def clear_task_list(self):
        pass

    def existing_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return True
        return False

    def load_tasks(self):
        pass

    def save_tasks(self):
        pass

    def get_task_title(self, console):
        while True:
            title_input = input("Enter Task Title: ").strip()
            if title_input.lower() == "q":
                return None 
            
            if self.existing_task(title_input):
                    console.print("[bold red]Warning: Task already exists.[/]")
                    time.sleep(1) 
                    continue   
            
            return title_input.title()
    
    def get_days_to_complete(self, console):
        while True:
            days_input = input("Days to complete (number): ").strip()
            if days_input.lower() == "q":
                return None
            try:
                days = int(days_input)
                if days < 1:
                    raise ValueError
                return days
            except ValueError:
                console.print("[bold red]Please enter a valid positive number.[/]")
                time.sleep(1)


    

        