"""
Find the GPS locations for Atlanta, Georgia;
Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
www.gps-data-team.com/map/ and compute the estimated area enclosed by these
four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
distance between two cities. Divide the polygon into two triangles and use the formula
in Programming Exercise 2.14 to compute the area of a triangle.)
s = (side1 + side2 + side3) / 2
area = (2s(s - side1)(s - side2)(s - side3))**0.5
"""
import math
from math import radians
x1, y1 = radians(33.8),radians(84.4)
x2, y2 = radians(28.5),radians(81.4)
x3, y3 = radians(32),radians(81.12)
x4, y4 = radians(35.2),radians(80.8)

radius = 6371.01
d12 = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
d13 = radius * math.acos(math.sin(x1) * math.sin(x3) + math.cos(x1) * math.cos(x3) * math.cos(y1 - y3))
d23 = radius * math.acos(math.sin(x2) * math.sin(x3) + math.cos(x2) * math.cos(x3) * math.cos(y2 - y3))

s= (d12+d13+d23)/2
area123 = math.sqrt(s*(s-d12)*(s-d13)*(s-d23))

d14 = radius * math.acos(math.sin(x1) * math.sin(x4) + math.cos(x1) * math.cos(x4) * math.cos(y2 - y4))
d13 = radius * math.acos(math.sin(x1) * math.sin(x3) + math.cos(x1) * math.cos(x3) * math.cos(y2 - y3))
d43 = radius * math.acos(math.sin(x4) * math.sin(x3) + math.cos(x4) * math.cos(x3) * math.cos(y2 - y3))

s= (d14+d13+d43)/2
area134 = math.sqrt(s*(s-d14)*(s-d13)*(s-d43))

total_area = area123+area134
print('Area enclosed approx ',total_area, ' sq.kms')
