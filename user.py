from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New User - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open("users.csv", "a") as myfile:
        myfile.write(f"{infos['Name']}\n")
    print("User Added !")
    return