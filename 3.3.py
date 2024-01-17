bmi = eval(input("Enter BMI value: "))
if bmi < 18.5 and bmi >0:
    print("Underweight")
elif bmi < 25 and bmi > 18.5:
    print("Normal")
else:
    print("Overweight")
