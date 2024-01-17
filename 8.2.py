"""
(Check substrings) You can check whether a string is a substring of another string
by using the find method in the str class. Write your own function to implement
find. Write a program that prompts the user to enter two strings and then checks
whether the first string is a substring of the second string.
"""


def string_check(s1, s2):
    subset = False
    length_s1 = len(s1)
    length_s2 = len(s2)
    for check in range(length_s2 - length_s1 + 1):
        if s2[check:check + length_s1] == s1:
            subset = True
            break
    return subset


check1 = 'ab'
check2 = 'abcd'
print(string_check(check1, check2))
check3 = 'abcd'
check4 = 'ab'
print(string_check(check3, check4))
