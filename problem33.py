# Write a code to access a value in a nested dictionary. The function should take the dictionary and a
# list of keys as input, and return the corresponding value. If any of the keys do not exist in the
# dictionary, the function should return None.

nested_dict = {
    'key1': {
        'key2': {
            'key3': 'value'
        }
    }
}

keys = input("Enter keys separated by commas: ").split(',')

current_dict = nested_dict

for key in keys:
    key = key.strip()
    if key in current_dict:
        current_dict = current_dict[key]
    else:
        current_dict = None
        break

print("The corresponding value is:", current_dict)
