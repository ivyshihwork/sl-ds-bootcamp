import datetime
from datetime import datetime as dt
import os
# Store the expense in a list as a dictionary
expenses=[]

# expense csv
filename="expenses.csv"

# utility function
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)

def addExpense(): 
    # eDate, eCategory,eAmount, eDescription
    # {'date': '2024-09-18', 'category': 'Food', 'amount': 15.50, 'description': 'Lunch with friends'}
    entry={}
    
    # eDate
    eDate=input("Enter expense date (YYYY-MM-DD): ")
    date_format = "%Y-%m-%d"
    result = False
    while result == False:
        try:
            result = bool(datetime.datetime.strptime(eDate, date_format))
        except ValueError:
            print("\nInvalid date format/range.  Please try again.\n")
            eDate=input("Enter expense date (YYYY-MM-DD): ")
    entry['date']=eDate
    
    # eCategory
    eCategory=input("Enter expense category: ")
    while not eCategory:
        print("\nThis field can not be empty.  Please enter a value.\n")
        eCategory=input("Enter expense category: ")
    entry['category']=eCategory
    # eAmount
    result=False
    while result == False:
        # 2 cond:  number w !=2 dec, string
        try:
            eAmount=float(input("Enter expense amount ($$.$$): "))
        except ValueError:
            print("\nInvalid value.  Please enter a numeric value.\n")
            eAmount=float(input("Enter expense amount: "))

        stringEAmount=str(eAmount)
        if len(stringEAmount[stringEAmount.rfind('.')+1:]) > 2:
            print("\nInvalid value. Please enter less than 2 decimals.\n")
            continue

        if isinstance(eAmount, float):
            result=True
    entry['amount']=eAmount
    # eDescription
    eDescription=input("Enter expense description: ")
    while not eDescription:
        print("\nThis field can not be empty.  Please enter a value.\n")
        eDescription=input("Enter expense description: ")
    entry['description']=eDescription
    
    expenses.append(entry)

def viewExpenses():
    if not expenses:
        print("\nThere is no expense recorded so far.\n")
    else:
        print("Note: If there's any entry with empty value, the record will be skipped.\n")
        for entry in expenses:
            if not ( entry['date'] or entry['category']  or entry['amount'] or entry['description'] ):
                continue
            print(f"\nDate: {entry['date']}\tCategory: {entry['category']}\tAmount: {entry['amount']}\tDescription: {entry['description']}")
    
def trackBudget():
    result=False
   
    while result == False:
        # 2 cond:  number w !=2 dec, string
        try:
            budget=float(input("Enter the budget for this month ($$.$$): "))
        except ValueError:
            print("\nInvalid value.  Please enter a numeric value.\n")
            budget=float(input("Enter the budget for this month ($$.$$): "))

        if str(budget)[::-1].find('.') > 2:
            print("\nInvalid value. Please enter less than 2 decimals.\n")
            continue
        
        if isinstance(budget, float):
            result=True
            
    appliedExpenses=[]
    currentMonth=dt.now().month
    currentYear=dt.now().year
    lastCurrentMonth=last_day_of_month(datetime.date(currentYear, currentMonth, 1))
    firstCurrentMonth = datetime.date(currentYear, currentMonth, 1)

    for entry in expenses:
        date=datetime.datetime.strptime(entry['date'],"%Y-%m-%d")

        if (date.date()>= firstCurrentMonth and date.date()<= lastCurrentMonth):
            appliedExpenses.append(entry)
        
    amount=sum([ float(entry['amount']) for entry in appliedExpenses])
    if amount > budget:
        print("Wanring: You have exceeded your budget by ", round(amount-budget, 2), ' this month!')
    else:
        print(f"You still have {round(budget - amount,2)} left in your budget for the month.")

def saveExpenses():
    with open(filename, 'w') as file:
        for entry in expenses:
            # date, category, amount, and description of each expense
            file.write(f"{entry['date']},{entry['category']},{entry['amount']},{entry['description']}\n")
    print(f"Expenses are written to {filename}")

def loadExpenses():
    entry={}
    
    print(f"\nLoading previous saved expenses in {filename}...\n")
    
    if not os.path.exists(filename):
        file = open(filename, 'w')
        print(f"\n{filename} does not exist.  Creating one...\n")
        file.close()
        
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            entry['date'], entry['category'], entry['amount'], entry['description'] = line.strip().split(',')
            expenses.append(entry)
            entry={}
            line = file.readline()
    print("\nCompleted.\n")
            
def displayMenu():
    loadExpenses()
    while True:
        print("""
        ######################################################
        ########## Welcome to Ivy's Expense Manager ##########
        ######################################################
        
        Please select one of the options below to continue:
        
        1)    Add expense
        2)    View expenses
        3)    Track budget
        4)    Save expenses
        5)    Exit
        
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
                addExpense()
            case 2:
                viewExpenses()
            case 3:
                trackBudget()
            case 4:
                saveExpenses()
            case 5:
                break

if __name__ == "__main__":
    displayMenu()