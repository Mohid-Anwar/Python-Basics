num1 = 121
not_reverse = num1
reverse = 0
while num1 > 0:
    last_part = num1 % 10
    num1 = num1 // 10
    reverse = (reverse * 10) + last_part
print(not_reverse == reverse)
