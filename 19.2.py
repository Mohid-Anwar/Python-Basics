speed = eval(input("What's your speed: "))
if speed > 70:
    print('Over speeding')
else:
    if speed > 60:
        print('Slow down')
    else:
        print('Acceptable speed')
