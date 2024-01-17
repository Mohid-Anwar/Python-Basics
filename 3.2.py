bmi = eval(input("Enter BMI value: "))
if bmi < 18.5:
    print("Underweight")
else:
    if bmi > 25:
        print("Overweight")
    else:
        print("Normal")
