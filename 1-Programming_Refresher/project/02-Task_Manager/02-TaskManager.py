import os
import hashlib

# Global variable
loginFile='login.csv'  #Store user login and encrypted passwords
userLogin=""            #Store User login if authenticated successfully

# utility function
def encrypt(password):
  return hashlib.sha256(password.encode()).hexdigest()

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
        else:
            if not os.path.exists(loginFile):
                file = open(loginFile, 'w')
                file.close()
            with open(loginFile, 'r+') as file:
                line = file.readline()
                entries=[]
                while line:
                    entry={}
                    entry['login'], entry['password'] = line.strip().split(',')
                    entries.append(entry)
                    line = file.readline()
                    print("\nCompleted.\n")
                if login in [ entry['login'] for entry in entries ]:
                    print("Login exists.  Please create pick a different user name or proceed to login instead.\n")
                else:
                    password=input(f'Pease enter a password for {login}: ')
                    if not password:
                        print("Password can not be empty.  Please try again.\n")
                    else:
                        file.write(f"{login},{encrypt(password)}")
                        print(f"User {login} has been created and saved successfully!\n")
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
    print("""
        ######################################################
        ########## Welcome to Ivy's Task Manager ##########
        ######################################################
        
        Please select one of the options below to continue:
        
        1)    Add a Task
        2)    View Tasks
        3)    Mark a Task as Completed
        4)    Delete a Task
        0)    Log out and exit the program
        """)
    while True:
            try:
                answer=int(input("Please enter the number of the option to continue (1-5): "))
            except ValueError:
                print("\nInvalid selection.  Please enter a number to continue (1-5): ")
                if not ( answer >0 and answer <=5 ):
                    print("\nInvalid selection.  Please enter a number to continue (1-5): ")
            else:
                break
            
    match answer:
        case 1:
            addTask()
        case 2:
            viewTasks()
        case 3:
            completeTask()
        case 4:
            deleteTask()
        case 0:
            exit


            
if __name__ == "__main__":

    while True:
        print("""
        ######################################################
        ########## Welcome to Ivy's Task Manager ##########
        ######################################################
        
        Please select one of the options below to continue:
        
        1)    Create/Register for user 
        2)    Login
        0)    Log out and exit the program
        """)
        while True:
            try:
                answer=int(input("Please enter the number of the option to continue (1-5): "))
            except ValueError:
                print("\nInvalid selection.  Please enter a number in 1-5 to continue.\n")
            else:
                break
        
        match answer:
            case 1:
                registration()
            case 2:
                login()
            case 0:
                break
            case _:
                print("\nInvalid selection.  Please enter a number in 1-5 to continue.\n")