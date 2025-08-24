# CLI Task Manager

A simple command-line task manager written in Python.  
Allows users to add, edit, view, remove, and clear tasks, with CSV-based persistent storage. Uses [Rich](https://github.com/Textualize/rich) for colored text and better CLI presentation.

---

### Features

- Add new tasks
- Edit existing tasks
- View task list
- Remove tasks
- Clear all tasks
- Load and save tasks to a CSV file (`storage.csv`)
- CLI interface with Rich for colored font decorations
- Test file included as boilerplate to run your own tests

---

### Installation

1. **Clone the repository**:

```bash
# HTTPS
git clone https://github.com/thandy1/task-manager.git

# SSH
git clone git@github.com:thandy1/task-manager.git
```

2. **Install Rich** (required for colored CLI output):
```bash
pip install rich
```

3. **Ensure Python is installed** (tested on Python 3.10+).

---

### Usage

1. Open your terminal and navigate to the project folder:
```bash
cd task-manager
```

2. Run the main program:
```bash
python task_manager.py
```

3. Follow the CLI prompts to add, edit, view, remove, or clear tasks.

4. All tasks are automatically saved to `storage.csv` and loaded when the program starts.

---

### Quick Start Example

1. Add a new task:
```text
Enter Task Title: Finish Project
Days to complete (e.g., 1, 5, 10): 7
```

2. View tasks:
```text
Current Tasks:
    1. Finish Project | Due: 2025-09-01
```

3. Edit or remove tasks using the corresponding menu options.

---

### Testing

- A test file is included for running your own basic tests.
- No additional libraries required for the boilerplate test.
- You can run it via:
```bash
python test/test_logic.py
```

---

### Notes

- Fully CLI-based, no GUI.
- The only external library required is Rich for terminal styling.
- Tasks are automatically saved after each change.

---

### Contributing

I’m new to Python and GitHub, so this is a beginner-friendly project.  
If you’d like to contribute, feel free to fork the repository, make changes, and submit a pull request.  
Any feedback or tips are welcome!
