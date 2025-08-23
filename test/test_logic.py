import os
import sys
# Add parent folder to module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime, timedelta
from logic import Task, TaskList


# Test helpers
def create_task(title, days):
    return Task(title, days)

# Tests
def test_update_title():
    t = create_task("Read Book", 5)
    t.update_title("Read Novel")
    assert t.title == "Read Novel", "Title should be updated"

def test_update_days():
    t = create_task("Read Book", 5)
    old_due = t.due_date
    t.update_days(10)
    assert t.days_to_complete == 10, "Days should be updated"
    assert t.due_date > old_due, "Due date should be updated"

def test_edit_task_combined():
    t = create_task("Read Book", 5)
    t.update_title("Read Novel")
    t.update_days(7)
    assert t.title == "Read Novel"
    assert t.days_to_complete == 7
    assert t.due_date > datetime.now(), "Due date should be in the future"

if __name__ == "__main__":
    test_update_title()
    test_update_days()
    test_edit_task_combined()
    print("All tests passed!")

