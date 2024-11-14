# Develop a code that prompts the user to input two sets of strings.
# Then, print the symmetric difference of these two sets.

string1 = input("Enter strings for set1: ")
set1 = set(string1.split())

string2 = input("Enter strings for set2: ")
set2 = set(string2.split())

print("Set1:", set1)
print("Set2:", set2)

set3 = set1.symmetric_difference(set2)
print("Symmetric Difference (Method 1):", set3)

set4 = set1 ^ set2
print("Symmetric Difference (Method 2):", set4)
