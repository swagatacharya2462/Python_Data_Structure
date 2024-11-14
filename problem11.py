# Write a code to remove all occurrences of a specific element from a list.

lst = input("Enter a list of elements (comma separated): ").split(",")
element = input("Enter the element to remove: ")

lst = [item for item in lst if item != element]
print("Updated list:", lst)
