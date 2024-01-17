speed = eval(input("What's your speed: "))
if speed > 70:
    print('Over speeding')
else:
    if speed > 60 and speed <=70:
        print('Slow down')
    else:
        print('Acceptable speed')
