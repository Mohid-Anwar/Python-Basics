num1 = eval(input("Enter 1st number: "))
num2 = eval(input("Enter 2nd number: "))
num3 = eval(input("Enter 3rd number: "))
if num1 > num2 and num1 > num3:
    print("a is greatest among the following which is ", num1)
elif num2 > num1 and num2 > num3:
    print("b is greatest among the following which is ", num2)
elif num3 > num1 and num3 > num2:
    print("c is greatest among the following which is ", num3)
elif num1 == num2 and num1 > num3:
    print("a and b are equal having value greater than c. Thus, the greatest value is ", num1)
elif num2 == num3 and num2 > num1:
    print("b and c are equal having value greater than a. Thus, the greatest value is ", num2)
elif num1 == num3 and num3 > num2:
    print("a and c are equal having greater value than b. Thus, the greatest value is ", num3)
elif num1 == num2 == num3:
    print("All three values are equal which is ", num1)
