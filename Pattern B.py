for count in range(7, 1, -1):

    display = 1
    for current_position in range(count, 1, -1):
        print(display, '', end='')

        display += 1

    print()  # Next line

'''
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
