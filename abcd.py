current_num = 0
for i in range(1, 1001):
    if i % 5 == 0 and i % 6 == 0:
        print(i, end=" ")
        current_num += 1

    if current_num == 10:
        print()
        current_num = 0