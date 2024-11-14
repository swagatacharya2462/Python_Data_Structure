# Write a code that takes two tuples as input and returns a new tuple containing
# elements that are common to both input tuples.

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 6, 7, 8, 9)

tuple3 = tuple(set(tuple1) & set(tuple2))
print(tuple3)
