# Project 02- Task Manager
  by Ivy Shih   2024-12-01

This document is created to show the requirement and actual implementation of the program.

## Mission Statement

In today’s world, individuals often need to keep track of various tasks in a structured way. 
You are tasked with building a Task Manager that allows users to manage their tasks. 

The system should include user authentication, meaning each user has to log in with a username and password. 
Once logged in, users can create, view, update, and delete their tasks. Each user’s tasks should be stored separately, and only the authenticated user can access their tasks.


## Global variables

|Name|Description|
|-|-|
|loginFile|Store user login and encrypted passwords.  Default value is login.csv|
|userLogin|Store User login if authenticated successfully|
|taskFile|Task file for the individual.  It should be {usrLogin}.csv since tasks are stored separately per requirment.|

## Functions
Here are the list of required steps/function names with additional details of implementation:

|Step| Function Name| Requirements| Implementation Details|
|-|-|-|-|
|1.1|registration|- Create a function to prompt the user to enter a username and password<br>- Ensure that the username is unique, and hash the password for security before storing it in a file|- Implement as requested<br>- Additional checks on username and password can't be empty|
|1.2|login|Create a function to prompt the user for their username and password, validate the credentials by comparing them with the stored data, and grant access to the task manager upon successful login|- Implement as requested|
|2|addTask|• Create a function that prompts the user for a task description. Assign a unique task ID and set the status to Pending<br>• Store the task in a file, and confirm that the task was added|- Implement as requested|
|3|viewTasks|• Create a function to retrieve and display all tasks for the logged-in user<br>• Each task should show the task ID, description, and status (Pending or Completed)|- Implement as requested|
|4|completeTask|Create a function that allows the user to select a task by its ID and update its status to Completed|- Implement as requested|
|5|deleteTask|Create a function that allows the user to select a task by its ID and delete it from their task list|- Implement as requested||
|6|displayMenu|• Build a menu that allows users to choose between:<br>o Add a Task<br>o View Tasks<br>o Mark a Task as Completed<br>o Delete a Task<br>o Logout<br><br>For each option, call the corresponding function, and loop back to the menu until the user logs out.|- Implement as requested||