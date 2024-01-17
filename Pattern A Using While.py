
for count in range(1, 7):

    current_position = 0
    display = 1
    while current_position < count:
        print(display, '', end='')

        display += 1
        current_position += 1
    print()  # Next line

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
'''