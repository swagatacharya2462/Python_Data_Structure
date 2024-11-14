# Write a code to reverse a string

string = input("Enter a string: ")
revString = ""

for i in string:
    revString = i + revString

print("Reverse String is:", revString)
