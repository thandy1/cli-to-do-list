import time
from logic import TaskList
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
        user_input = input(
            "Select from the list of options:\n" \
            "[1]: Add New Task\n" \
            "[2]: Edit Task List\n" \
            "[3]: View Task List\n" \
            "[4]: Exit\n")
        if user_input == "1":
            todo.add_task(console)
        elif user_input == "2":
            todo.edit_task(console)
        elif user_input == "3":
            todo.view_task()
        elif user_input == "4":
            break
        else: 
            console.print("[bold red]Invalid Input: Please enter one of the options above.[/]")
            time.sleep(1)
            

# Function call to begin the program
if __name__ == "__main__":
    main()