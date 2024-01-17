from random import randint

num = eval(input("Enter your guess between 0 and 2 : "))
guess = randint(0, 2)
if num == guess:
    print("correct")
elif num > 2 or num < 0:
    print("Out of range")
else:
    print("Incorrect. The correct answer was ", guess)
