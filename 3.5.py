"""
Write a program that prompts the user to enter the
number of sides and their length of a regular polygon and displays its area.
"""

import math

n = eval(input("Enter the number of sides: "))
s = eval(input("Enter the side: "))
area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))
print("The area of the the polygon is ", area)
