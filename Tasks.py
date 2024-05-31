"""
Objects to Create
Task

Attributes:
Title
Description
Due date
Completion status
Priority level
Methods:
Mark as complete
Mark as incomplete
Update task details (title, description, due date, priority)
"""
class Task:
    """
    base class for Task Object
    """
    def __init__(self, title: str, description: str = ' ', due_date : str = ' ', completion_status: bool = False, priority: int = 3) -> None:
        """
        initilizer
        """
        self._title = title
        self._description = description
        self._due_date = due_date
        self._completion_status = completion_status
        self._priority = priority

    def get_title(self):
        """
        returns the title
        """
        return self._title

    def get_description(self):
        """
        returns the description
        """
        return self._description
    

    def get_due_date(self):
        """
        returns the due date
        """
        return self._due_date


    def get_completion_status(self):
        """
        returns if the task has been marked as competed
        """
        return self._completion_status
    
    def get_priority(self):
        """
        returns priority of the task
        """
        return self._priority
    
    def set_title(self, title: str):
       """
       can be used to change the title of the Task
       """
       self._title = title

    def set_description(self, description: str):
        """
        can be used to change the description of the task
        """
        self._description = description
    
    def set_due_date(self, due_date: str):
        """
        can be use to change the due date of the task
        """
        self._due_date = due_date
    
    def set_priority(self, priority: int):
        """
        can be used to change the priority of the task
        """
        self._priority = priority
    
    def set_completion_status(self, completion_status: bool):
        """
        can be used to change the completion status of the task
        """
        self._completion_status = completion_status

    def mark_as_complete(self):
        """
        marks the task as complete
        """
        self.set_completion_status(True)

    def mark_as_incomplete(self):
        """
        marks the task as incomplete
        """
        self.set_completion_status(False)

    def update_task_details(self, title: str = None, description: str = None, due_date: str = None, priority: str = None):
        """
        updates the tasks as per provided input
        """
        if title is not None:
            self.set_title(title= title)
        if description is not None: 
            self.set_description(description=description)
        if due_date is not None:
            self.set_due_date(due_date=due_date)
        if priority is not None:
            self.set_priority(priority=priority)

    def __str__(self) -> str:
        status = "Complete" if self.get_completion_status() else "Incomplete"
        return f"Task: {self.get_title()}, Description: {self.get_description()}, Due: {self.get_due_date()}, Status: {status}, Priority: {self.get_priority()}"