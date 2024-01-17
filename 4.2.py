# Leap Year
leap_year = eval(input("Enter year: "))
if leap_year % 4 == 0:
    print("Leap Year")
else:
    if leap_year % 100 == 0 and leap_year % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")
