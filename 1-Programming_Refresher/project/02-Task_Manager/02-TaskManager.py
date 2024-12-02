import os
import hashlib

# Global variable
loginFile='login.csv'   #Store user login and encrypted passwords
userLogin=""            #Store User login if authenticated successfully
taskFile=""             # Task file for the individual.  It should be {usrLogin}.csv since tasks are stored separately per requirment

# utility function
def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()

def loadTasks(login):
    tasks=[]
    taskFile=login + '.csv'
    if os.path.exists(taskFile):
        with open(taskFile, 'r+') as file:
            line = file.readline()
            while line:
                task={}
                task['taskID'], task['description'],task['status'] = line.strip().split(',')
                tasks.append(task)
                line = file.readline()
    return tasks


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
                if login in [ entry['login'] for entry in entries ]:
                    print("Login exists.  Please create pick a different user name or proceed to login instead.\n")
                else:
                    password=input(f'Pease enter a password for {login}: ')
                    if not password:
                        print("Password can not be empty.  Please try again.\n")
                    else:
                        file.write(f"{login},{encrypt(password)}\n")
                        print(f"User {login} has been created and saved successfully!\n")
                        break
                
# Step 1.2 login
def login():
    '''
    - Prompt the user for their username and password
    - Validate the credentials by comparing them with the stored data
    - Grant access to the task manager upon successful login
    '''
    global userLogin
    global taskFile
    
    if not os.path.exists(loginFile):
        print("There is no user in the system.  Please register a user firs!\n")
        return False
    while True:
        login=input("PLease enter your user name: ")
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
                if login in [ entry['login'] for entry in entries ]:
                    password=input(f'Pease enter password for {login}: ')
                    if not password:
                        print("Password can not be empty.  Please try again.\n")
                    else:
                        if encrypt(password) == [e['password'] for e in entries if e['login'] == login ][0]:
                            print(f"User {login} has been created and saved successfully!\n")
                            userLogin=login
                            taskFile=userLogin +'.csv'
                            displayMenu()
                            break
                        else:
                            print("Invalid password.  Please try again.\n")
                            break
                else:
                    print(f"\nUser name {login} does not exist.  Please register for user name.\n")
                    break

# Step 2   addTask
def addTask():
    '''
    • Prompts the user for a task description. 
    • Assign a unique task ID and set the status to Pending
    • Store the task in a file, and confirm that the task was added
    '''
    # TaskID, Description, Status
    global userLogin
    global taskFile
    tasks=loadTasks(userLogin)

    if not os.path.exists(taskFile):
        file = open(taskFile, 'w')
        file.close()
        newID=0
    else:
        newID=int(tasks[-1]['taskID'])+1
        
    with open(taskFile, 'a') as file:
        while True:
            description=input("Please enter task description: ")
            if not description:
                print("Task must have a description.  Please try again.\n")
            # elif description in [  task['description'] for task in tasks ]:
            #     print("There is already another task with exact description.  Please be specific./n")
            else:
                file.write(f"{newID},{description},Pending\n")
                print("\nTask has been added successfully.  Go to View Tasks option to see updated task list.\n")
                break

# Step 3    viewTasks
def viewTasks():
    '''
    • Create a function to retrieve and display all tasks for the logged-in user
    • Each task should show the task ID, description, and status (Pending or Completed)
    '''
    global userLogin
    tasks=loadTasks(userLogin)
    if not tasks:
        print(f"There's no task for {userLogin}\n")
    else:
        print("{:<5} {:<20} {:<10}".format('ID','Description','Status'))
        print("{:<5} {:<20} {:<10}".format('--','-----------','------'))
        for task in tasks:
            print("{:<5} {:<20} {:<10}".format(task['taskID'],task['description'],task['status']))

# Step 4    completeTask
def completeTask():
    '''
    This allows the user to select a task by its ID and update its status to Completed.
    '''
    global userLogin
    tasks=loadTasks(userLogin)
    viewTasks()
    while True:
        answer=input("Enter the task number to complete the task: ")
        if answer in [ task['taskID'] for task in tasks]:
            change=[ task for task in tasks if task['taskID']== answer][0]
            tasks.remove(change)
            change['status']='Completed'
            tasks.append(change)
            tasks=sorted(tasks, key=lambda k: k['taskID'])
            with open(taskFile, 'w') as file:
                for task in tasks:
                    file.write(f"{task['taskID']},{task['description']},{task['status']}\n")
            print("\nTask has been completed successfully.  Go to View Tasks option to see updated task list.\n")
            break
        else:
            print('\nInvalid selection.  Please try again.\n')
    

# Step 5    deleteTask
def deleteTask():
    '''
    This allows the user to select a task by its ID and delete it from their task list.
    '''
    global userLogin
    tasks=loadTasks(userLogin)
    viewTasks()
    while True:
        answer=input("Enter the task number to delete the task: ")
        if answer in [ task['taskID'] for task in tasks]:
            tasks=[ task for task in tasks if task['taskID']!= answer]
            with open(taskFile, 'w') as file:
                for task in tasks:
                    file.write(f"{task['taskID']},{task['description']},{task['status']}\n")
            print("\nTask {answer} has been deleted successfully.  Go to View Tasks option to see updated task list.\n")
            break
        else:
            print('\nInvalid selection.  Please try again.\n')

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
    global userLogin
    while True:
        print(f"""
            ######################################################
            ########## Welcome to Ivy's Task Manager #############
            ######################################################
            
            Hello, {userLogin}!
            
            Please select one of the options below to continue:
            
            1)    Add a Task
            2)    View Tasks
            3)    Mark a Task as Completed
            4)    Delete a Task
            0)    Log out
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
                userLogin=""
                break
            
if __name__ == "__main__":

    while True:
        print("""
        ######################################################
        ########## Welcome to Ivy's Task Manager ##########
        ######################################################
        
        Please select one of the options below to continue:
        
        1)    Create/Register for user 
        2)    Login
        0)    Exit Task Manager
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