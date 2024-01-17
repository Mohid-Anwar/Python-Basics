"""for i in range(5,0,-1):
    print("* "*i)"""
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
