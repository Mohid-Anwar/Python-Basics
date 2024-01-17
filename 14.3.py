num = eval(input('Enter num '))
four = num % 4
two = num % 2
if two == 0 and four == 0:
        print('num is divisible by 4 and 2')
elif two == 0:
        print('divisible by 2')
else:
    print('not divisible by 2 or 4')
