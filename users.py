

users = {}
status = ""


def display_menu():
    status = ""
    while status != "quit":
        status = input("Are you a registered user? yes/no Press quit to quit").lower()
        if status == "yes":
            olduser()
        elif status == "no":
            newuser()
        elif status == "quit":
            print("Ty and Allah Hafiz")



def newuser():
        createlogin = input("Create login name: ")
        if createlogin in users:
            print("Name Already Taken")
        else:
            createpassw = input("Create Password: ")
            users[createlogin] = createpassw
            print("User Created")


def olduser():
        login = input("Enter login name: ")
        passw = input("Enter login password: ")

        if login in users and users[login] == passw:
            print("Login Successful")
        else:
            print("User doesn't exist or wrong")


display_menu()
print(users)