age = eval(input('Enter age: '))
if age >= 18:
    print("Eligible for license")
else:
    if age == 16 or age == 17:
        print("Eligible for learner")
    else:
        print("too little")
