"""
this file creates the login interface.
here we provide the user with two options.
1. existing user :
    > if selected the user is asked to enter the username and password.
    > if the username and password do not match then the user is prompoted the same and is asked to enter the same again.
    > upon 3 unsuccessful attempts the application ends.
2. new user :
    > if selected, the user should be prompted to create a new account by adding username and password.
    > the username and password are added to the database object with a default empty ToDoList.
"""
from users import User, Database 
from to_do_list import ToDoList

def invalidSelectionError():
    """
    this error is raised if the user makes an invalid selection in any menu
    currently only configured for login feature
    """
    return "Invalid Entry!"

def maximumAttemptsReachedError():
    """
    this error is raised if the user has reached the maximum attempts of invalid entries.
    currenlty only configured for login feature.
    """
    return "Maximum Attempts Reached, Please Restart the Application"


def get_user_credentials():
    """
    input function that reads the input from user in form of a string.
    this function reads and returns username and password.
    can be used to 
    """
    username = input("Username: ")
    password = input("Password: ")
    return username, password

def login(database: Database):
    """
    this function is the main logic for login functionality of the to-do-app
    """
    print("1: Existing User")
    print("2: New User")
    selection = input("Please Enter Your Choice: ")
    if selection == "1":
        invalid_attempts = 0
        username, password = get_user_credentials()
        if username in database.database.keys():
            if password != database.database[username].password and invalid_attempts <= 3:
                invalid_attempts += 1
                print("Invalid Username or Password, Try Again!")
                username, password = get_user_credentials()
            elif invalid_attempts > 3:
                raise maximumAttemptsReachedError
            else:
                return database, database.database[username].to_do_list
    elif selection == "2":
        username, password = get_user_credentials()
        new_todo_list = ToDoList([])
        new_user = User(username, password, new_todo_list)
        database.database.update({username: new_user})
        return database, database.database[username].to_do_list
    else:
        raise invalidSelectionError


def logout(database: Database):
    print("Thanks for Using! You Have Been Logged Out Successfully!")
    login(database)