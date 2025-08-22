import time
from logic import TaskList, Task
from rich.console import Console

# Instances
todo = TaskList() 
console = Console()

# Main function call to launch the system or close
def main():
    while True:
        todo.clear_terminal()
        user_input = input(f"Welcome! Would you like to launch the system? \n[1]: Yes\n[2]: No\n")
        if user_input == "1":
            run_system()
        elif user_input == "2":
            break
        else:
            console.print("[bold red]Invalid Input: Please enter one of the options above.[/]")
            time.sleep(1) 
              
# System launch 
def run_system():
    while True: 
        todo.clear_terminal()
        print("Current Tasks:\n")
        todo.display_task()
        user_input = input(
            "\nSelect from the list of options:\n" \
            "[1]: Add New Task\n" \
            "[2]: Edit Task List\n" \
            "[3]: View Task List\n" \
            "[4]: Exit\n")
        if user_input == "1":
            add_task(console)
        elif user_input == "2":
            edit_task(console)
        elif user_input == "3":
            view_task()
        elif user_input == "4":
            break
        else: 
            console.print("[bold red]Invalid Input: Please enter one of the options above.[/]")
            time.sleep(1)
            
# Add Task 
def add_task(console):
    todo.clear_terminal()
    print("Press 'q' to cancel.\n")
    while True:
        
        title = todo.get_task_title(console)
        if title is None:
            break

        priority = todo.get_priority(console)
        if priority is None:
            break

        due_date = todo.get_due_date(console)
        if due_date is None:
            break

        new_task = Task(title, priority, due_date)
        todo.tasks.append(new_task)
        console.print(f"[bold green]Task added successfully![/]")
        time.sleep(1)   
        break

# Edit Tasks 
def edit_task(console):
    todo.clear_terminal()
    while True: 
        print("Current Tasks:\n")
        todo.display_task()

        user_input = input(
            "\nSelect from the list of options:\n" \
            "[1]: Edit Task Property\n" \
            "[2]: Remove Task\n" \
            "[3]: Clear Task List\n" \
            "[4]: Main Menu\n")
        if user_input == "1":
            todo.edit_task_property()
        elif user_input == "2":
            todo.remove_task()
        elif user_input == "3":
            todo.clear_task_list()
        elif user_input == "4":
            break 
        else: 
            console.print("[bold red]Invalid Input[/]")
            time.sleep(1)

# View Task 
def view_task():
    todo.clear_terminal()
    print("Current Tasks:")
    todo.display_task()
    pass

# Function call to begin the program
if __name__ == "__main__":
    main()