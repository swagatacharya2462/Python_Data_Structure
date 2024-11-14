# Develop a code that prompts the user to input two sets of strings. Then,
# print the elements that are present in the first set but not in the second set.

string1 = input("Enter strings for set1 (separated by spaces): ")
set1 = set(string1.split())

string2 = input("Enter strings for set2 (separated by spaces): ")
set2 = set(string2.split())

print("Elements in set1 but not in set2 (Method 1):", set1 - set2)