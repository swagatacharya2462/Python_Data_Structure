# Write a code to find all occurrences of a given substring within another string.

text = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

occurrences = []
start = 0

while True:
    start = text.find(substring, start)
    if start == -1:
        break
    occurrences.append(start)
    start += 1

if occurrences:
    print("Occurrences at indices:", occurrences)
else:
    print("No occurrences found.")
