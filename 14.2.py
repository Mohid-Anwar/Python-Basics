num = eval(input('Enter num '))
four = num % 4
two = num % 2
if two == 0:
    if four == 0:
        print('num is divisible by 4 and 2')
    else:
        print('divisible by 2')
else:
    print('not divisible by 2 or 4')
