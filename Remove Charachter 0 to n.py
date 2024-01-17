"""
a = "pynative"
n = 4
print(a[n:len(a)])
"""


def removeChars(str, n):
    return str[n:]


print("Removing n number of chars")
print(removeChars("pynative", 4))
