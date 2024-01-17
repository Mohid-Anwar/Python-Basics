"""
(Check SSN) Write a program that prompts the user to enter a Social Security
number in the format ddd-dd-dddd, where d is a digit. The program displays
Valid SSN for a correct Social Security number or Invalid SSN otherwise.
"""


def ssn():
    usr_input = input('Enter SSN format: ddd-dd-dddd: ')
    valid = False
    if usr_input.count('-') == 2 and len(usr_input) == 11:
        digit_only = usr_input.split('-')
        digit_check = digit_only[0].isdigit()
        digit_check = digit_only[1].isdigit()
        digit_check = digit_only[2].isdigit()

        if len(digit_only[2]) == 4 and len(digit_only[1]) == 2 and len(digit_only[0]) == 3 and digit_check== True:
            valid = True
    if valid:
        print('Valid')

    else:
        print('invalid')


ssn()

