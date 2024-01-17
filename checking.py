import random

word = "computer"

correct_letter_guessed = []
for start in range(3):
    correct_letter_guessed.append(random.choice(word))
print(correct_letter_guessed)