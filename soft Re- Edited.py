import random

randNumber = random.randint(1, 10)
userGuess = 0
guesses = 0

while userGuess != randNumber and guesses < 3:

    userGuess = int(input("Enter your Guess "))
    guesses += 1

    if userGuess > randNumber:
        print("You guessed it Wrong...Too large number..")

    elif userGuess < randNumber:
        print("You guessed it Wrong...Too small number..")

if guesses >= 3:
    print(f"Lives Khtm. Asl number {randNumber} tha ")
else:
    print(f"you guessed it in {guesses} Guesses")
