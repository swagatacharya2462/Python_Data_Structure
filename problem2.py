# Write a code to count the number of vowels in a string

string = input("Enter a string : ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0

for i in string:
    if i in vowels:
        count = count + 1

print("Total number of vowels are present in string is", count)
