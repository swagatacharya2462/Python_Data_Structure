# Write a code that takes two dictionaries as input and merges them into a single dictionary.
# If there are common keys, the values should be added together.

string1 = input("Enter key value pairs (key:value): ")
pairs1 = string1.split(",")
dict1 = {}
for pair1 in pairs1:
    key1, value1 = pair1.split(":")
    dict1[key1.strip()] = int(value1.strip())

print("Dictionary 1:", dict1)

string2 = input("Enter key value pairs (key:value): ")
pairs2 = string2.split(",")
dict2 = {}
for pair2 in pairs2:
    key2, value2 = pair2.split(":")
    dict2[key2.strip()] = int(value2.strip())

print("Dictionary 2:", dict2)

merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value

print("Merged Dictionary:", merged_dict)
