# Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary
# correctly handles cases where multiple keys have the same value by
# storing the keys as a list in the inverted dictionary.

string1 = input("Enter key & value (key:value): ")
pairs = string1.split(",")
dict1 = {}

for pair in pairs:
    key, value = pair.split(":")
    dict1[key.strip()] = value.strip()

inverted_dict = {}

for key, value in dict1.items():
    if value in inverted_dict:
        inverted_dict[value].append(key)
    else:
        inverted_dict[value] = [key]

print(inverted_dict)
