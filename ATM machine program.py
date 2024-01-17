import sys

customer_info = {
    1234: ["Name1", 1],
    2345: ["Name2", 2],
    3456: ["Name3", 3]
}

pin = eval(input(" Welcome, Enter Pin: "))

if pin not in customer_info.keys():
    print("No Pin of this kind")
    sys.exit()

option = int(input("Welcome\n1.Display Record.\n2.Deposit money\n3.delete a account\n:"))
while option < 1 or option >3:

    option = int(input("Retry: "))

if option == 1:
    print(f"Name {customer_info[pin][0]}\nPin {pin}\nBalance {customer_info[pin][1]}")
elif option == 2:
    deposit = int(input("Enter the deposit you want to make "))

    customer_info[pin][1] += deposit
    print(f"Your new balance is ${customer_info[pin][1]}")
else:
    del_pin = int(input("Enter pin of account to be deleted: "))
    while del_pin not in  customer_info.keys():
        del_pin = int(input("No pin like this exists"))

    print(f" The following Account has been deleted \nName:{customer_info[del_pin][0]}\npin: {del_pin}\nAmount: {customer_info[del_pin][1]}")
    customer_info.pop(del_pin)
