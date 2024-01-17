"""for num in range(1, 11):
    for index in range(1, 11):
        print(num * index, end=" ")
    print("")
"""
for num in range(1, 11):
    for index in range(1, 11):
        print(f"{num * index:2d}", end=" ")
    print("")
