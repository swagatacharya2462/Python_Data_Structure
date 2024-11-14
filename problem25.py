# Create a code that takes a tuple and two integers as input. The function should return a new tuple containing
# elements from the original tuple within the specified range of indices.

num1 = int(input("Enter start index: "))
num2 = int(input("Enter end index: "))

string1 = input("Enter numbers for tuple: ")
tuple1 = tuple(map(int, string1.split()))

new_tuple = tuple1[num1:num2 + 1]
print("New tuple:", new_tuple)
