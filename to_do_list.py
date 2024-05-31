"""
ToDoList

Attributes:
List of tasks (a collection of Task objects)

Methods:
Add a new task
Edit an existing task
Delete a task
View all tasks
Mark a task as complete/incomplete
Set the priority of a task
Sort tasks
"""

from Tasks import Task

class ToDoList:
    """
    base class for a ToDo List
    """
    def __init__(self, tasks: list[Task]) -> None:
        self._tasks = {}
        for task in tasks:
            self._tasks[task.get_title()] =  tasks
            
    def get_all_tasks(self):
        """
        fetches all tasks currently added
        """
        return self._tasks

    def get_one_task(self, task):
        """
        fetches a particular task
        """
        return self._tasks[task]
    
    def show_all_tasks(self):
        """
        displays all tasks added in console
        """
        for _ , task_object in self.get_all_tasks().items():
            print(task_object)
    
    def update_key_value(self, old_key: str, new_key: str):
        """
        updates the key to new title
        """
        tasks = self.get_all_tasks()
        tasks[new_key] = tasks.pop(old_key)
    
    def add_new_task(self, title: str, description: str = ' ', due_date : str = ' ', completion_status: bool = False, priority: int = 3):
        """
        adds new task to the list
        """
        task = Task(title=title, description=description, due_date=due_date, completion_status=completion_status, priority=priority)
        self._tasks[task.get_title()] = task
    
    def delete_task(self, task: Task):
        """
        deletes a task
        """
        if task.get_title() in self.get_all_tasks().keys():
            del self._tasks[task.get_title()]

    def edit_task(self, task: Task, title: str = None, description: str = None, due_date: str = None, priority: int = None):
        """
        edits an existing task
        """
        if task.get_title() in self.get_all_tasks().keys():
            old_title = task.get_title()
            task.update_task_details(title=title, description=description, due_date=due_date, priority=priority)
            self.update_key_value(old_key=old_title, new_key=task.get_title())
        else:
            print("Task is not added!")
    
    def mark_as_completed(self, task: Task, completed: bool):
        """
        marks the task as complete
        """
        return task.mark_as_complete() if completed else task.mark_as_incomplete()
    
    def set_priority(self, task: Task, priority: int):
        """
        marks the task as incomplete
        """
        return task.set_priority(priority)
    
    def sort_tasks(self):
        """
        dummy function
        """
        pass
    