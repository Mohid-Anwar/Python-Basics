a = input("enter a string: ")
b = input("enter a string: ")
# check if the strings are of the same length
len_a = len(a)
len_b = len(b)
while len_a != len_b:
    print("Not same length. Exiting Program")
    break
else:
    for i in range(0, len_a):
        print(b[i] + a[i], end='')
