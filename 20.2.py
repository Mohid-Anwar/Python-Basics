a = input('hot or cold? or normal')
a = a.lower()
if a == 'hot':
    hot = True
    cold = False
else:
    if a == 'cold':
        hot = False
        cold = True
    else:
        hot = False
        cold = False

if hot:
    print("Hot day")
    print('AC Turned on')

else:
    if cold:
        print("Cold day")
        print('Heater on')

if a == 'normal':
    print("It's a lovely weather")
