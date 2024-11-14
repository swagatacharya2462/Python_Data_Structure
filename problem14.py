# Write a code to reverse a list in-place without using any built-in reverse functions.

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) // 2):
    list1[i], list1[len(list1) - 1 - i] = list1[len(list1) - 1 - i], list1[i]

print("Reversed list:", list1)
