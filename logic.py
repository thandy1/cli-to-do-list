import os
from datetime import datetime, timedelta

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
                # Format for nice display
                due_date = task.due_date.strftime("%Y-%m-%d") 
                print(f"\t{i}. {task.title} | Due: {due_date}")
    
    def remove_selected_task(self):
        pass

    def clear_task_list(self):
        pass

    def existing_task(self, title_input):
        for task in self.tasks:
            if task.title.lower() == title_input.lower():
                return True
        return False

    def load_tasks(self):
        pass

    def save_tasks(self):
        pass

    def positive_number_check(self, days_input):
        days = int(days_input)
        if days < 1:
            return True
    
     