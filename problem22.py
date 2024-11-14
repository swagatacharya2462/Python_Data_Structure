# Create a code that prompts the user to enter two sets of integers separated by commas.
# Then, print the intersection of these two sets.

string1 = input("Enter numbers for set1 (separated by commas): ")
set1 = set(map(int, string1.split(',')))

string2 = input("Enter numbers for set2 (separated by commas): ")
set2 = set(map(int, string2.split(',')))

print(set1 & set2)