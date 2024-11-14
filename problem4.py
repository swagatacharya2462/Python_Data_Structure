# Write a code to check if two given strings are anagrams of each other

string1 = input("Enter 1st string: ")
string2 = input("Enter 2nd string: ")

if sorted(string1) == sorted(string2):
    print("Yes, both are anagrams")
else:
    print("No, both are not anagrams")
