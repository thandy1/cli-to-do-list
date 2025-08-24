import os
from datetime import datetime, timedelta
import csv

# This class represents a single task
class Task:
    def __init__(self, title, days_to_complete):
        self.title = title
        self.days_to_complete = days_to_complete
        self.due_date = datetime.now() + timedelta(days=days_to_complete)
        
    def update_title(self, new_title):
        self.title = new_title  
       
    def update_days(self, new_days):
        self.days_to_complete = new_days
        self.due_date = datetime.now() + timedelta(days=new_days)
        
# This class manages a list of task objects, handles add/edit/load/save
class TaskList:
    def __init__(self):
        self.tasks = []   # List of task objects
        
    def clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_task(self):
        for i, task in enumerate(self.tasks, start=1):
                due_date = task.due_date.strftime("%Y-%m-%d") 
                print(f"\t{i}. {task.title} | Due: {due_date}")
    
    def remove_selected_task(self, task_index):
        self.tasks.pop(task_index)

    def clear_task_list(self):
        self.tasks.clear()

    def existing_task(self, title_input):
        for task in self.tasks:
            if task.title.lower() == title_input.lower():
                return True
        return False

    # Restore everything back into memory in the CSV
    def load_tasks(self, filename="storage.csv"):
        self.tasks = [] # Create a fresh list to avoid duplicates
        try:
            with open(filename, mode="r") as file:
                # Reads the CSV file as a dictionary per row
                reader = csv.DictReader(file)   
                for row in reader:
                    title = row["title"]
                    days = int(row["days_to_complete"])
                    # Rebuild the Task object in memory from the CSV data
                    task = Task(title, days)
                    # Overwrite the calculated due_date with stored one
                    task.due_date = datetime.strptime(row["due_date"], "%Y-%m-%d" "%H-%M-%S")
                    self.tasks.append(task)
        except FileNotFoundError:
            # If no storage file exists yet, just ignore
            pass

    # Dump everything from memory into the CSV
    def save_tasks(self, filename="storage.csv"):
        with open(filename, mode="w", newline="") as file:
            # Creates a CSV writer object to let us write rows into the file
            writer = csv.writer(file)
            # Write header row 
            writer.writerow(["title", "days_to_complete", "due_date"])
            for task in self.tasks:
                # Each task written as a row
                writer.writerow([task.title, task.days_to_complete, task.due_date.strftime("%Y-%m-%d" "%H-%M-%S")])
        
    def positive_number_check(self, days_input):
        days = int(days_input)
        if days < 1:
            return True
        
"""
Storage file format:

title,days_to_complete,due_date
Read Book,5,2025-08-28 10:45:12
Study Python,3,2025-08-26 10:45:12
"""