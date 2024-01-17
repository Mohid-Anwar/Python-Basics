'''a = [10, 20, 33, 46, 55]
for i in range(len(a)):
    if a[i]%5 == 0: print(a[i])'''


def DivisibleFive(a):
    for i in range(len(a)):
        if a[i] % 5 == 0: print(a[i])


haloo = [10, 20, 33, 46, 55]
DivisibleFive(haloo)