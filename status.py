from PyInquirer import prompt
from expense import get_users

def show_summary():
    # This function should show the summary of the expenses
    users = get_users()
    owes = []
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

        #computes how involved people should pay to the spender
        for user in involved:
            added = False
            for owe in owes:
                if(owe['name'] == user and owe['to'] == spender):
                    owe['amount'] += int(amount) / (len(involved) + 1)
                    added = True
            if added == False:
                owes.append({
                    "name": user,
                    "amount": int(amount) / (len(involved) + 1),
                    "to": spender
                })

    for owe in owes:
        print(f"{owe['name']} owes {owe['amount']} to {owe['to']}")

    for user in users:
        #if user not in owes
        if not any(d['name'] == user for d in owes):
            print(f"{user} owes nothing")

    #for owe in owes:
     #   print(f"{owe['name']} owes {owe['amount']} to {owe['to']}")