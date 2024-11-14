# Write a code that takes a list of words as input and returns a dictionary where the keys are unique
# words and the values are the frequencies of those words in the input list.

string1 = input("Enter words for list: ")
list1 = string1.split()
dict1 = {}

for word in list1:
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1

print(dict1)
