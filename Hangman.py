import random
play_again = "y"
lives = 5
word = "computer"
guessed = False
correct_letter_guessed = []

print("Welcome To Hangman")
print("_" * len(word))
index = [index for index in range(0, len(word))]
for dis in range(0, len(word)):
    print(index[dis], end="")
print("")

while guessed == False and lives > 0 and play_again == "y":
    letter_guess = input("Enter one Character or full word: ").lower()

    if len(letter_guess) == 1:
        if not letter_guess.isalpha():
            print("Invalid Character")
        elif letter_guess not in word:
            print("This letter is not in word")
            lives -= 1
        elif letter_guess in word:
            print("Correct letter guessed")

            correct_letter_guessed.append(letter_guess)
    elif len(letter_guess) == len(word):
        if letter_guess == word:
            guessed = True

        else:
            print("Incorrect attempt at word")
            lives -= 1
    else:
        print("Not the same length as guessed word")
    status = ""
    if guessed == False:
        for letter in word:
            if letter in correct_letter_guessed:
                status += letter
            else:
                status += "_"
        print(status)
        for dis in range(0, len(word)):
            print(index[dis], end="")
        print("")
        print(f"Your current lives are : {lives}")
    if status == word or guessed == True:
        guessed = True
        print("Congrats on guessing word!!!")
        play_again=input("Do you want to play again? y or n ").lower()
        if play_again == "y":
            lives = 5
            guessed = False
            correct_letter_guessed = []
            status = ""
            print("Welcome To Hangman")
            print("_" * len(word))
            index = [index for index in range(0, len(word))]
            for dis in range(0, len(word)):
                print(index[dis], end="")
            print("")
    elif lives == 0:
        print("Out of Lives")
