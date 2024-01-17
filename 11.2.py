a = eval(input("Enter current time: "))
am_pm = input("AM or PM?? ")
am_pm = am_pm.lower()
if 2 <= a <= 5:
    if am_pm == 'pm':
        print("Open")
    else:
        print('Closed')
else:
    print('Closed')

