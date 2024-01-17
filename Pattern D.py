"""Note to Sir. As Pattern B and D were the same I have attempted the Sequence I believe was intended to be put
there.
    654321
     54321
      4321
       321
        21
         1"""

for row in range(7, 0, -1):
    space = row - 1
    for space_string in range(0, 7 - row):  # spaces required
        print(" ", end="")
    for display in range(row, 1, -1):  # Values in row 1 to 6
        print(display - 1, end="")
    print()
