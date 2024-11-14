# Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys
# and their counts as values.

lst = input("Enter a list of elements (comma separated): ").split(",")
count_dict = {}

for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1

print("Occurrences:", count_dict)
