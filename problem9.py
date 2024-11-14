# Write a code to count the number of words in a string.

string = input("Enter a string: ")
words = string.split()
count = len(words)
print("Total number of words:", count)
print("And words are:", words)
