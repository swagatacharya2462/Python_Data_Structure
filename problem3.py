# Write a code to check if a given string is a palindrome or not

string = input("Enter a string: ")
revString = ""

for i in string:
    revString = i + revString

if revString == string:
    print("Yes palindrome...")
else:
    print("Not palindrome...")
