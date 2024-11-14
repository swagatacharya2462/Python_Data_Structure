# Write a code to perform basic string compression using the counts of repeated characters

s = input("Enter a string to compress: ")

compressed = []
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        compressed.append(s[i - 1] + str(count))
        count = 1

compressed.append(s[-1] + str(count))

compressed_string = ''.join(compressed)

if len(compressed_string) < len(s):
    print("Compressed string:", compressed_string)
else:
    print("Compressed string:", s)
