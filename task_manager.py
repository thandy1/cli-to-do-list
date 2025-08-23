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
             
# System launch 
def run_system():
    while True: 
        todo.clear_terminal()
        print("Run System\n")
        print("Current Tasks:\n")
        todo.display_task()

        user_input = input(
            "\nSelect from the list of options:\n" 
            "[1]: Add New Task\n" 
            "[2]: Edit Task List\n" 
            "[3]: View Task List\n" 
            "[4]: Exit\n"
            )
        if user_input == "1":
            add_task()
        elif user_input == "2":
            edit_task()
        elif user_input == "3":
            view_task()
        elif user_input == "4":
            break
            
def add_task():
    while True:
        todo.clear_terminal()
        print("Run System > Add New Task\n")
        
        title = todo.get_task_title(console)
        if title is None:
            break

        days = todo.get_days_to_complete(console)
        if days is None:
            break

        new_task = Task(title, days)
        todo.tasks.append(new_task)
        todo.clear_terminal()
        console.print(f"[bold green]Task added successfully![/]")
        time.sleep(1.5)   
        break

def edit_task():
    while True: 
        todo.clear_terminal()
        print("Run System > Edit Task List\n")
        print("Current Tasks:\n")
        todo.display_task()
        print("\nHow would you like to edit your tasks?")

        user_input = input(
            "\nSelect from the list of options:\n" 
            "[1]: Edit Task Property\n" 
            "[2]: Remove Task\n" 
            "[3]: Clear Task List\n" 
            "[4]: ..\n")
        
        if user_input == "1":
            edit_task_property()
        elif user_input == "2":
            todo.remove_task()
        elif user_input == "3":
            todo.clear_task_list()
        elif user_input == "4":
            break 

def view_task():
    todo.clear_terminal()
    print("Run System > View Task List\n")
    print("Current Tasks:")
    todo.display_task()
    pass

def edit_task_property():
    while True:
        todo.clear_terminal()
        print("Run System > Edit Task List > Edit Task Property\n")
        print("Current Tasks:\n")
        todo.display_task()
        print("\nPress 'q' to cancel.")

        try:
            task_number = input("\nWhich task would you like to edit?: ")
            if task_number.lower() == "q":
                return
            task_index = int(task_number) - 1
            if task_index < 0 or task_index >= len(todo.tasks):
                todo.clear_terminal()
                console.print(
                    f"[bold red]Invalid Input, '{task_number}.'\n"
                    "Please enter the number assigned to the task.[/]")
                time.sleep(1.5)
                continue
            break
        except ValueError:
            todo.clear_terminal()
            console.print("[bold red]Invalid Input:" 
                          "Please Enter task's number rank. (e.g., 1, 2)[/]")
            time.sleep(1.5)
            continue

    selected_task = todo.tasks[task_index]
    edit_selected_task(selected_task)


def edit_selected_task(task):

    while True:
        todo.clear_terminal()
        print("Run System > Edit Task List > Edit Task Property > Edit Selected Task\n")
        print("What would you like to edit?\n")

        edit_task_input = input(
            "Please select an option: \n"
            "[1]: Task Title\n"
            "[2]: Days To Complete\n"
            "[3]: ..\n")
        
        if edit_task_input == "1":
            todo.clear_terminal()
            print("Press 'q' to cancel.\n")
            new_title = input("Update Task Title: ").title().strip()
            if new_title.lower() == "q":
                return  # exits this edit and goes back to the previous menu
            task.update_title(new_title)
            todo.clear_terminal()
            console.print(f"[bold green]Title updated to: {task.title}[/]")
            time.sleep(1.5)
            continue

        elif edit_task_input == "2":
            while True:
                todo.clear_terminal()
                try:
                    new_days = (input("Update Days To Complete: "))
                    if new_days.lower() == "q":
                        return
                    task.update_days(int(new_days))
                    todo.clear_terminal()
                    console.print(f"[bold green]Days to complete updated to: {task.days_to_complete}[/]")
                    time.sleep(1.5)
                    break
                except ValueError:
                    todo.clear_terminal()
                    console.print("[bold red]Invalid Input, Please enter a number.[/]")
                    time.sleep(1.5)
                    continue
        elif edit_task_input == "3":
            break

# Function call to begin the program
if __name__ == "__main__":
    main()