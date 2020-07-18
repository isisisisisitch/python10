#1.Write a Python program to remove an item from a tuple.
tuple1 = ('B','y','t','e','T','u','b','e')
print(tuple1)
# tuple2 = tuple1[0:4] + tuple1[5:]
# print(tuple2)
list1 = list(tuple1)
list1.remove("T")
tuple1 = tuple(list1)
print(tuple1)