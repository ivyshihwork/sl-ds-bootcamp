# Project 01 - Personal Tracker
  by Ivy Shih   2024-11-25

This document is created to show the requirement and actual implementation of the program.

## Global variables

|Name|Description|
|-|-|
|expenses|It is a list of dictionaries of each record of expenses.|
|filename|- It is the filename of saved experiences and where the program load expenses from in the beginning of execution.<br>- It has to be in the same execution directory as the program to be loaded/saved to.|

## Functions
Here are the list of steps and what are required with additional details of implementation:

|Step| Function Name| Requirements| Implementation Details |
| -|-|- | - |
| 1 | AddExpense | Create a function to prompt the user for expense details.<br>Ensure you ask for:<br>- The date of the expense in the format YYYY-MM-DD<br>- The category of the expense, such as Food or Travel<br>- The amount spent<br>- A brief description of the expense<br><br>Store the expense in a list as a dictionary, where each dictionary includes the date, category, amount, and description as key-value pairs<br>|A global variable list is initialized in the beginning of the script to track all expenses in dictionary format: expenses=[]<br><br>The entry variable is a dictionary that stores date, category, amount and description in key value pairs.  <br><br>There are also additional input checks for:<br>- null values for all 4 fields to re-prompt inputs<br>- invalid date format to re-prompt<br>- invalid amount check on numeric values and no decimal more than 2 will be allowed.<br>After all the values pass the check, they will be stored in **entry** variable, and append to **expenses** list
|2|viewExpenses|Write a function to retrieve and display all stored expenses<br>- Ensure the function loops through the list of expenses and displays the date, category, amount, and description for each entry<br>- Validate the data before displaying it - If any required details (date, category, amount, or description) are missing, skip the entry or notify the user that it’s incomplete|- This function retrieves all records from **expenses** list.<br>- There are already checks in place for fields, but as part of requirement, it still checked for no values for the keys and print a warning in the front stating "Note: If there's any entry with empty value, the record will be skipped." before printing all the validated records.  It is better practice just to print one instead of one for each record in case of many invalid records of data via import.
|3|trackBudget| Set and track the budget:<br>• Create a function that allows the user to input a monthly budget. Prompt the user to:<br>o Enter the total amount they want to budget for the month<br><br>• Create another function that calculates the total expenses recorded so far<br>- Compare the total with the user’s monthly budget<br>- If the total expenses exceed the budget, display a warning (Example: You have exceeded your budget!)<br>- If the expenses are within the budget, display the remaining balance(Example: You have 150 left for the month)|-|
|4.1|saveExpenses|Implement a function to save all expenses to a CSV file, with each row containing the date, category, amount, and description of each expens|- Global variable **filename** is used to save the file.|
|4.2|loadExpenses|Create another function to load expenses from the CSV file. When the program starts, it should:<br>- Read the saved data from the file<br>- Load it back into the list of expenses so the user can see their previous expenses and continue from where they left off|- Checks whether **fillename** exists.  If does not, it will show it doesn't and will be created.  If it does, it will show it loads from **fillename**.<br>To see the entries, View expenses option can be selected.|
|5|displayMenu|• Build a function to display a menu with the following options:<br>o Add expense<br>o View expenses<br>o Track budget<br>o Save expenses<br>o Exit<br><br>• Allow the user to enter a number to choose an option<br><br>• Implement the following conditions:<br>o If the user selects option 1, call the function to add an expense<br>o If the user selects option 2, call the function to view expenses<br>o If the user selects option 3, call the function to track the budget<br>o If the user selects option 4, call the function to save expenses to the file<br>o If the user selects option 5, save the expenses and exit the program|Implemented as requested|
