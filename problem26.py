# Write a code that prompts the user to input two sets of characters.
# Then, print the union of these two sets.

string1 = input("Enter characters for set1 (separated by spaces): ")
set1 = set(string1.split())

string2 = input("Enter characters for set2 (separated by spaces): ")
set2 = set(string2.split())

print("Union of the two sets:", set1.union(set2))
