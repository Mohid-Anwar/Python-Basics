def indexOfSmallestElement(lst):
   smallest_index = 0
   element_value = lst[0]
   for i in range (1, len(lst)):
       if lst[i] < element_value:
           element_value = lst[i]
           smallest_index = i
   return smallest_index
lst = list(map(int, input('Enter a list of numbers: ').split()))
smallestIndex = indexOfSmallestElement(lst)
print('Smallest index is:', smallestIndex)