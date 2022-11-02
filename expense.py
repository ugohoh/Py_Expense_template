from PyInquirer import prompt

def get_users():
    with open("users.csv", "r") as myfile:
        users = myfile.readlines()
    return users





def new_expense(*args):
    expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },]
    expense_questions.append({
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_users()
    })

    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open("expense_report.csv", "a") as myfile:
        myfile.write(f"{infos['amount']},{infos['label']},{infos['spender']}")
    print("Expense Added !")
    return True


