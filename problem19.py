# Create a code to find the union of two lists without duplicates.

list1 = [1, 2, 3, 4, 5, 1, 4]
list2 = [1, 3, 5, 7, 9, 8, 6, 7]

list3 = list1 + list2
list3 = list(dict.fromkeys(list3))
print(list3)