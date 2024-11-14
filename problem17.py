# Write a code to merge two sorted lists into a single sorted list.

list1 = [10, 30, 20, 50, 40, 20, 30]
list2 = [15, 25, 35, 15, 25, 45, 55]

list3 = sorted(set(list1 + list2))
print(list3)