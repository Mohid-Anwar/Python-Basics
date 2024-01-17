a = eval(input("Enter current time: "))
am_pm = input("AM or PM?? ")
am_pm = am_pm.lower()
if 2 <= a <= 5 and am_pm == 'pm':
    print("Open")
elif a < 2 or a > 5:
    print('Closed')
else:
    print('closed')
