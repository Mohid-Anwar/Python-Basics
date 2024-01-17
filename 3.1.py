"""
(Geometry: area of a pentagon) Write a program that prompts the user to enter the
length from the center of a pentagon to a vertex and computes the area of the pentagon,
as shown in the following figure.
"""
import math

radius = eval(input("Enter r of Pentagon: "))

area = (3 * math.sqrt(3) / 2) * (2 * radius * math.sin(math.pi / 5)) ** 2
print(round(area, 2))
