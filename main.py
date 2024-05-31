"""
this is the main runner for the application. 
This is a console application for now.
"""
from to_do_list import ToDoList

def run():
    """
    main runner function
    """
    print("Hello! Welcome To Your Todo List")
    todo = ToDoList([])
    while True:
        print("\n===== ToDo List Menu =====")
        print("1. Add a new task")
        print("2. Edit an existing task")
        print("3. Delete a task")
        print("4. View all tasks")
        print("5. Mark a task as complete/incomplete")
        print("6. Set the priority of a task")
        print("7. Sort tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(todo)
        elif choice == '2':
            edit_task(todo)
        elif choice == '3':
            delete_task(todo)
        elif choice == '4':
            view_all_tasks(todo)
        elif choice == '5':
            change_completion_status(todo)
        elif choice == '6':
            set_priority(todo)
        elif choice == '7':
            sort_todo_list(todo)
        else:
            break
def add_task(todo: ToDoList):
    """
    this function is used to add a task to todo list
    """
    title = input("Enter Title: " )
    description = input("Enter Description: ")
    due_date = input("Enter Due Date: ")
    priority = int(input("Enter Priority: "))
    todo.add_new_task(title=title, description=description, due_date= due_date, completion_status=False, priority=priority)

def edit_task(todo: ToDoList):
    """
    this function is used to edit and existing task
    """
    title = input("Enter Task Title to edit: ")
    task = todo.get_one_task(title)
    title = input("Enter Title: " )
    description = input("Enter Description: ")
    due_date = input("Enter Due Date: ")
    priority = int(input("Enter Priority: "))
    todo.edit_task(task, title=title, description=description, due_date= due_date, priority=priority)

def delete_task(todo: ToDoList):
    """
    this function is used to detele an existing task.
    """
    title = input("Enter Task Title to Delete: ")
    task = todo.get_one_task(title)
    todo.delete_task(task)

def view_all_tasks(todo: ToDoList):
    """
    this function is used to view all tasks currently added in the list
    """
    todo.show_all_tasks()

def change_completion_status(todo: ToDoList):
    """
    this function is used to change the completion status of the task
    """
    title = input("Enter Task Title to Mark Completed: ")
    task = todo.get_one_task(title)
    todo.mark_as_completed(task, not task.get_completion_status())

def set_priority(todo: ToDoList):
    """
    this function is used to update the priority of the task.
    """
    title = input("Enter Task Title to Change Priority: ")
    task = todo.get_one_task(title)
    new_priority = int(input("Enter new value for Priority: "))
    todo.set_priority(task, new_priority)

def sort_todo_list(todo: ToDoList):
    """
    dummuy fuction
    """
    pass

if __name__ == "__main__":
    run()
