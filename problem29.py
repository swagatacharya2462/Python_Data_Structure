# Write a code that takes a tuple and an element as input. The function should
# return the count of occurrences of the given element in the tuple.

ele1 = int(input("Enter a number: "))
string1 = input("Enter values for a tuple: ")
list1 = string1.split()
tuple1 = tuple(map(int, list1))

count = tuple1.count(ele1)

print(f"Tuple: {tuple1}")
print(f"The element {ele1} occurs {count} time(s) in the tuple.")
