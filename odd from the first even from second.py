list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
list3 = []
for i in range(len(list1)):
    if list1[i] % 2 == 1:
        list3.append(list1[i])
for j in range(len(list2)):
    if list2[j] % 2 == 0:
        list3.append(list2[j])
print(list3)
