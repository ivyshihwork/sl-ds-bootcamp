import os

# Global variable
login_file='login.csv'  #Store user login and encrypted passwords

# Step 1.1 registration
def registration():
    '''
    - Create a function to prompt the user to enter a username and password
    - Ensure that the username is unique, and hash the password for security before storing it in a file
    '''
    while True:
        login=input("PLease enter a login name: ")
        if not login:
            print("\nLogin name can not be empty.  Please try again.\n")
        # elif  - need to check if it's in the file
        else:
            break
        

# Step 1.2 login
def login():
    '''
    - Prompt the user for their username and password
    - Validate the credentials by comparing them with the stored data
    - Grant access to the task manager upon successful login
    '''
    pass

# Step 2   addTask
def addTask():
    '''
    • Prompts the user for a task description. 
    • Assign a unique task ID and set the status to Pending
    • Store the task in a file, and confirm that the task was added
    '''
    pass

# Step 3    viewTasks
def viewTasks():
    '''
    • Create a function to retrieve and display all tasks for the logged-in user
    • Each task should show the task ID, description, and status (Pending or Completed)
    '''
    pass

# Step 4    completeTask
def completeTask():
    '''
    This allows the user to select a task by its ID and update its status to Completed.
    '''
    pass

# Step 5    deleteTask
def deleteTask():
    '''
    This allows the user to select a task by its ID and delete it from their task list.
    '''
    pass

# Step 6    displayMenu()
def displayMenu():
    '''
    • Build a menu that allows users to choose between:
        o Add a Task
        o View Tasks
        o Mark a Task as Completed
        o Delete a Task
        o Logout

    For each option, call the corresponding function, and loop back to the menu until the user logs out.	
    '''
    pass

if __name__ == "__main__":
    # load login file
    if not os.path.exists(login_file):
    file = open(login_file, 'w')
    file.close()
    users={}    # contain login and password for each line
        
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            login, password = line.strip().split(',')
            users[login]=password
            line = file.readline()
