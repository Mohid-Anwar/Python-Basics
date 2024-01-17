def indexOfSmallestElement(lst):
    min_element = min(lst)
    smallest = lst.index(min_element)
    print(smallest)
    return smallest


lst_input = input("values seperated by spaces :").split()
for i in range(0,len(lst_input)):
    lst_input[i] = eval(lst_input[i])

index = indexOfSmallestElement(lst_input)
