size = eval(input("How MAny Values "))
number_list=[]
for index in range(0, size):
    element = eval(input("input numbers: "))
    number_list.append(element)
"""
for index in range(len(number_list)-1 ,-1, -1):
    if number_list[index] > 50:
        number_list.pop(index)
print(number_list)"""
i = 0
max_list_length = len(number_list)
while i < max_list_length:
    if number_list[i] > 50:
        number_list.pop(i)
        max_list_length -= 1
    else:
        i = i + 1
print(number_list)
