# Develop a code that takes a tuple of integers as input.
# The function should return the maximum and minimum values from the tuple using tuple unpacking.

string1 = input("Enter numbers for tuple: ")
list1 = string1.split()
list1 = list(map(int, list1))
tuple1 = tuple(list1)

min_val, max_val = min(tuple1), max(tuple1)

print("Tuple:", tuple1)
print("Minimum value of this tuple:", min_val)
print("Maximum value of this tuple:", max_val)
