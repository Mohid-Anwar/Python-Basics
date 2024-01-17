descending_new = int(input("Enter the integer with bse 10: "))
compare_previous = descending_new
count = 0
descending_old = 0
while True:
    descending_new = str(descending_new)
    descending_new = list(descending_new)
    descending_new.sort()
    descending_new.reverse()
    descending_new = "".join(descending_new)
    b = int(descending_new)

    c = b

    b = str(descending_new)
    b = list(b)
    b.sort()
    b = "".join(b)
    b = int(b)

    descending_new = c - b

    if descending_new == descending_old:
        count += 1
        break
    count += 1
    descending_old = descending_new

print(f"The number of chain lenghts for the number {compare_previous} are : {count}")