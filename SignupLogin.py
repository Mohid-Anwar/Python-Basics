import sys

users_data = [
    {
        "fname": "Usman",
        "lname": "Rehman",
        "email": "usman@outlook.com",
        "password": "usman"
    },
    {
        "fname": "Ali",
        "lname": "Rehman",
        "email": "ali@outlook.com",
        "password": "outlook"
    }, ]


def signing_up():
    print("Welcome to Sign Up")
    print()
    fname = input("Enter First Name : ")
    lname = input("Enter last Name : ")
    email = input("Enter Email : ")
    password = input("Enter Paassword: ")
    user_data = {"fname": fname,
                 "lname": lname,
                 "email": email,
                 "password": password}
    users_data.append(user_data)
    print("You have successfully registered!")


def siging_in():
    print("Welcome to sign In.")
    print()
    email = input("Enter  Email : ")
    password = input("Enter Password: ")
    login_check = False
    for data_entered in users_data:
        if data_entered['email'] == email and data_entered['password'] == password:
            login_check = True
            print("Logged in")

    if not login_check:
        print("Un successful login")


def exit_program():
    print("Good Bye")
    sys.exit()


def main():
    while True:
        print("""Welcome to menu\n1. press 1 to sign up\n2. press 2 to sign in\n3. press 3 to Exit""")
        usr_input = input("Enter Choice :")
        if usr_input == "1":
            signing_up()
            print(users_data)
        elif usr_input == "2":
            siging_in()
        elif usr_input == "3":
            exit_program()
        else:
            print("Enter num between 1 to 3")


main()
