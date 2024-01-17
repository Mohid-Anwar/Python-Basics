num = input("Enter number : ")
digits = len(num)
if digits == 1:
    print("One digit num")
elif digits == 2:
    print("Two digit number")
elif num != 1 and num != 2:
    print("Number is more than 99")
