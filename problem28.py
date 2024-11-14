# Create a code that defines two sets of integers.
# Then, print the union, intersection, and difference of these two sets.

string1 = input("Enter integers for set1: ")
set1 = set(map(int, string1.split()))

string2 = input("Enter integers for set2: ")
set2 = set(map(int, string2.split()))

print("Set1:", set1)
print("Set2:", set2)

print("Union of set1 and set2:", set1 | set2)
print("Intersection of set1 and set2:", set1 & set2)
print("Difference of set1 and set2:", set1 - set2)
