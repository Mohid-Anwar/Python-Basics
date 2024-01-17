"""
User inputs a positive base 10 integer, greater than zero,

determine how many one bits are in the binary equivalent.

Then determine how many numbers between zero and the given number contain the same number of one bits.

For example, the number 12 expressed as a binary number (1100) has 2 one bits. Between 0 and
12 there are 5 other numbers having 2 one bits when expressed as a binary number. These are: 3
(11), 5 (101), 6 (110), 9 (1001), 10 (1010).

8 in binary has 1 1-bits. There are 3 other numbers with 1 1-bits between 0 and 8.
"""

userInput = 0
while userInput <= 0:
    userInput = int(input("inputs a positive base 10 integer, greater than zero "))

num = userInput
one_bits = 0
binary_equivalent = ""

while num != 0:
    remainder = num % 2
    if remainder == 1:
        one_bits += 1
    num //= 2
    binary_equivalent += str(remainder)
binary_equivalent = int(binary_equivalent[::-1])


count_ones_same = 0
for x in range(1,userInput):
    bits_one_for_x = 0
    binary_check = ""
    while x != 0:
        remainder = x % 2
        if remainder == 1:
            bits_one_for_x += 1
        x //= 2
        binary_check += str(remainder)
    binary_check = int(binary_check[::-1])
    if one_bits == bits_one_for_x:
        count_ones_same += 1

print(f"{userInput} in binary has {one_bits} 1-bits. There are {count_ones_same} other numbers with {one_bits} 1-bits between 0 and {userInput}.")

