# Project 01 - Personal Tracker
  by Ivy Shih   2024-11-25


## Functions
Here are the list of steps and what are required with additional details of implementation:

|Step| Function Name| Description| Implementation Details |
| -|-|- | - |
| 1 | AddExpense | Create a function to prompt the user for expense details.<br>Ensure you ask for:<br>- The date of the expense in the format YYYY-MM-DD<br>- The category of the expense, such as Food or Travel<br>- The amount spent<br>- A brief description of the expense<br><br>Store the expense in a list as a dictionary, where each dictionary includes the date, category, amount, and description as key-value pairs<br>|A global variable list is initialized in the beginning of the script to track all expenses in dictionary format: expenses=[]<br><br>The entry variable is a dictionary that stores date, category, amount and description in key value pairs.  <br><br>There are also additional input checks for:<br>- null values for all 4 fields to re-prompt inputs<br>- invalid date format to re-prompt<br>- invalid amount check on numeric values and no decimal more than 2 will be allowed.<br>After all the values pass the check, they will be stored in **entry** variable, and append to **expenses** list
|2|viewExpenses|Write a function to retrieve and display all stored expenses<br>- Ensure the function loops through the list of expenses and displays the date, category, amount, and description for each entry<br>- Validate the data before displaying it - If any required details (date, category, amount, or description) are missing, skip the entry or notify the user that it’s incomplete|This function retrieves all records from **expenses** list.<br>There are already checks in place for fields, but as part of requirement, it still checked for no values for the key.