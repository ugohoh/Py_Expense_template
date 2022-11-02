from PyInquirer import prompt

def get_users():
    with open("users.csv", "r") as myfile:
        users = myfile.readlines()
        for i in range(len(users)):
            users[i] = users[i].replace("\n", "")
    return users

def new_expense(*args):
    users = get_users()

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
        "choices": users
    })
    

    infos = prompt(expense_questions)

    users2 = []
    for user in users:
        if(user == infos['spender']):
            users2.append({
                "name": user.replace("\n", ""),
                "checked": True,
                "disabled": True,
            })
        else:
            users2.append({
                "name": user.replace("\n", ""),
            })
    expense_questions2 = [{
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - People involved: ",
        "choices": users2
    }]

    infos2 = prompt(expense_questions2)

    involvedd = infos2['involved']

    res = infos['amount'] + "," + infos['label'] + "," + infos['spender']
    for i in involvedd:
        res += "," + i
    res += "\n"
    
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open("expense_report.csv", "a") as myfile:
        myfile.write(res)
    print("Expense Added !")
    return True


