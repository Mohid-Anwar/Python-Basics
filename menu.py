name_lst = []
age_lst = []
nationality_lst = []

while True:
    menu = input("Enter A to add information \n"
               "Enter S to search for Record \n "
               "Enter D to delete a record \n"
               "Enter E to exit : \n")
    menu = menu.upper

    if menu == "E":
        break

    elif menu == "A":
        while True:
            name = input("Enter the name of the tourist: ")
            name = name.upper()
            age = int(input("Enter the age of the tourist: "))
            nation = input("Enter the nationality of the tourist: ")
            name_lst.append(name)
            age_lst.append(age)
            nationality_lst.append(nation)

            next = input("Enter 1 to add more information: \n"
                         "ENter 0 to exit: ")
            if next == "0":
                break

    elif menu == "S":
        search = input("Enter the name of tourist to search: \n")
        if name_lst._contains_(search):
            ind = name_lst.index(search)

            print(f"Name : {name_lst[ind]}\n"
                  f"Age : {age_lst[ind]}\n"
                  f"Nationality : {nationality_lst[ind]}")

        else:
            print("_The name you entered is not in our records.__")

    elif menu == "D":
        removal = input("Enter the name of Tourist whose data you want to remove: ")
        removal = removal.upper()
        if name_lst._contains_(removal):
            ind = name_lst.index(removal)
            print(f"Name : {name_lst[ind]}\n"
                  f"Age : {age_lst[ind]}\n"
                  f"Nationality : {nationality_lst[ind]}")

            con = input("Enter R to delete this record: ")
            if con == "R":
                name_lst.pop(ind)
                age_lst.pop(ind)
                nationality_lst.pop(ind)
                print("THE RECORD HAS BEEN REMOVED.")
            else:
                print("The record is not deleted.")
        else:
            print("The name you searched is not in our records.")