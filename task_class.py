import os

class TaskList:
    # Turn functions into methods
    # Add self as first parameter so they can access the instance's data
    def __init__(self):
        self.tasks = []

    # Add Task Logic
    def add_task(self):
        self.clear_terminal()
        task = input("Enter Task Title: ")
        self.tasks.append(task)
        pass
            
    # Edit Tasks Logic
    def edit_tasks(self):
        self.clear_terminal()
        pass 
    
    #  Exit Logic
    def exit_system(self):
        pass

    # Clear terminal logic
    def clear_terminal(self):
        # os.system runs a terminal command
        # conditional operator chooses the terminal command based on the users OS
        os.system("cls" if os.name == "nt" else "clear")