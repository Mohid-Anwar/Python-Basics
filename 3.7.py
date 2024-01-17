"""
(Random character) Write a program that displays a random uppercase letter
using the time.time() function.
"""
import time
import math

num = time.time()
num = round(num)
random_num = 65 + num % 26     # adding 65 to ensure capital, % 26 as 26 alphabets
print('Random uppercase letter generated is ', chr(random_num))
