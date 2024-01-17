a = input('hot or cold? or normal')
a = a.lower()
if a == 'hot':
    hot = True
    cold = False
elif a == 'cold':
    hot = False
    cold = True
else:
    hot = False
    cold = False

if hot:
    print("Hot day")
    print('AC Turned on')

elif cold:
    print("Cold day")
    print('Heater on')

else:
    print("It's a lovely weather")
