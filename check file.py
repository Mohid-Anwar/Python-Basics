Customer_info = [{'Name': 'Irfan', 'Pin': 123, 'Balance': 100}, {'Name': 'Imran', 'Pin': 321, 'Balance': 200},
                 {'Name': 'Ahmed', 'Pin': 322, 'Balance': 300}]

print(type(Customer_info))
pin = int(input("Input Pin:"))

flag = True
for i in Customer_info:

    if flag:
        temp = i['Pin']
        if temp == pin:
            print("a.Check Balance")
            print("b.Deposit Money")
            print("c.Return Card")
            option = input("Select any option:")

            if option == 'a':
                for customer in Customer_info:
                    t_pin = customer['Pin']
                    if t_pin == pin:
                        print("Your balacne is " + str(customer['Balance']))
                        flag = False
            elif option == 'b':
                deposit = int(input("Enter the amount: "))
                for customer in Customer_info:
                    t_pin = customer['Pin']
                    if t_pin == pin:
                        temp_d = customer['Balance']
                        temp_d = temp_d + deposit
                        customer['Balance'] = temp_d
                        flag = False
                        print("Balance Deposit Successfull. New Balance is " + str(customer['Balance']))
            elif option == 'c':
                for i in range(len(Customer_info)):
                    if Customer_info[i]['Pin'] == pin:
                        del Customer_info[i]
                        print("Customer Data Deleted Succesfully")
                        flag = False
                        break
            else:
                print('You Entered a Wrong Option')
                flag = False

if flag:
    print("Wrong Pin.No Data Found")
else:
    print('Thanks for Using Our ATM')
