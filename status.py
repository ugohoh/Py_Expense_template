from PyInquirer import prompt
from expense import get_users

def show_summary():
    # This function should show the summary of the expenses
    users = get_users()
    all_expenses = []

    with open("expense_report.csv", "r") as myfile:
        all_expenses = myfile.readlines()
        for i in range(len(all_expenses)):
            all_expenses[i] = all_expenses[i].replace("\n", "")
    
    for expense in all_expenses:
        expense = expense.split(",")
        amount = expense[0]
        label = expense[1]
        spender = expense[2]
        involved = expense[3:]

        print(f"{spender} spent {amount} on {label} with {involved}")