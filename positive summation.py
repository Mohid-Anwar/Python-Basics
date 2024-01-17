from math import sqrt

"""
One of your customer demanded you to write a program that input n positive values from the
user
add all values to a list.
This input process should terminate when user insert negative value.
 This program should calculate and display the result of following equation.
"""

userInput = 0
n = 0
user_lst = list()
while userInput > -1:
    userInput = int(input("Input Value to be appended: "))
    if userInput > -1:
        user_lst.append(userInput)
        n += 1
xi = sum(user_lst)
print(xi)
print(n)
ans = sqrt((xi+5)/n)
print(ans)


