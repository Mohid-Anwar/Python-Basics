number = 7536
while number>0:
    digit = number%10
    number //= 10
    print("%.1d" % digit, end=" " )