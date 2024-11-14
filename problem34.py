# Write a code that takes a dictionary as input and returns a sorted version of it based on the values.
# You can choose whether to sort in ascending or descending order.

string1 = input("Enter key & value (key:value): ")
pairs = string1.split(",")
dict1 = {}

for pair in pairs:
    key, value = pair.split(":")
    dict1[key.strip()] = value.strip()

order = input("Sort in ascending or descending order? (asc/desc): ").lower()

for key, value in dict1.items():
    try:
        dict1[key] = int(value)
    except ValueError:
        pass

if order == 'asc':
    sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
elif order == 'desc':
    sorted_tuples = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
else:
    print("Invalid input for sorting order.")
    sorted_tuples = []

sorted_dict = dict(sorted_tuples)
print(sorted_dict)
