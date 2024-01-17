count = 6
for row in range(1, count):
    print(" " * (count - row -1), end="")
    for display in range(row, 0, -1):
        print(display, end="")
    print()

'''
    1
   21
  321
 4321
54321
'''
