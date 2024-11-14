# Write a code to concatenate two tuples. The function should take two tuples as input
# and return a new tuple containing elements from both input tuples.

string1 = input("Enter numbers for tuple1 (separated by spaces): ")
tuple1 = tuple(map(int, string1.split()))

string2 = input("Enter numbers for tuple2 (separated by spaces): ")
tuple2 = tuple(map(int, string2.split()))

tuple3 = tuple1 + tuple2
print(tuple3)