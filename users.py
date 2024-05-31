"""
this file contains classes that will create the use objects.
here we will have two classes.
Class User : containing information related to a signle user
Class Database : containing information related to all the users which are available
"""

from dataclasses import dataclass, field
from Tasks import Task
from to_do_list import ToDoList

@dataclass
class User:
    """
    this class is used to create a user.
    A user will have a username, password and lists of Tasks
    """
    username: str = field(default_factory=str)
    password: str =  field(default_factory=str)
    to_do_list : ToDoList =  field(default_factory=ToDoList)


@dataclass
class Database:
    """
    this class is a dictionary which stores the information related to each user.
    the username of the User (from class User) is used as a key and the other user data is stored in form or values.
    this will be a a dictionary of User objects.
    when a new user is added, it should get appended to this class object.
    """
    database : dict = field(default_factory= dict)
