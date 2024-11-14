# Write a code to determine if a string has all unique characters.

string = input("Enter a string: ")

unique = len(set(string)) == len(string)
if unique:
    print("Yes, It has unique characters.")
else:
    print("No, It has not unique characters.")
