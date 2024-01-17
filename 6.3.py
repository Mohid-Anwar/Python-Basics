num = eval(input("Enter num: "))
ten = 10
twenty = 20
if num > ten and num > twenty:
    print("num larger then 10 and 20")
elif num > ten and num < twenty:
    print("num is larger 10 and smaller than 20")
else:
    print("num smaller then 10 and 20")
