# PRACTICAL 06
# Write a program to demonstrate working with tuples in python.

fruits = ("apple", "banana", "cherry", "mango", "grape", "orange")
print("\n Tuple is :", fruits)
print("\n Second fruit is :", fruits[1])
print("\n From 3-6 fruits are :", fruits[3:6])
print("\n List of all items in Tuple :")
for x in fruits:
    print(x)
if "apple" in fruits:
    print("\n Yes, 'apple' is in the fruits.")
print("\n Length of Tuple is :", len(fruits))
