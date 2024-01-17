"""
(Reverse number) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order. Here is a sample run:
"""
# Way 1
num = input("Enter 4 digit num: ")
while len(num) != 4:
    num = input("re-enter: ")
print(num[::-1], end='')
# End Way 1

print()

# Way 2
num2 = int(input("Enter 4 digit num (Way 2) : "))
one = num2 % 10
num2 //= 10
two = num2 % 10
num2 //= 10
three = num2 % 10
num2 //= 10
four = num2 % 10
num2 //= 10
order_reversed = (1000*one)+(100*two)+(10*three)+four
print('Reverse num Way 2: ', order_reversed)