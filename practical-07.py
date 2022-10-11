# PRACTICAL 07
# Write a program to demonstrate working with dictionaries in python.

dictionary = {'StdNo': '2007477', 'Name': 'Abhishek', 'Age': 21, 'City': 'Bihar'}
print("\n Dictionary is :", dictionary)
print("\n Student Name is :", dictionary['Name'])
print("\n City is :", dictionary['City'])
print("\n All Keys in Dictionary ")
for x in dictionary:
    print(x)
print("\n All Values in Dictionary ")
for x in dictionary:
    print(dictionary[x])
dictionary["contact"] = 6202123608
print("\n Updated Dictionary is :", dictionary)
dictionary["Name"] = "Sunny"
print("\n Updated Dictionary is :", dictionary)
dictionary.pop("Age")
print("\n Updated Dictionary is :", dictionary)
print("Length of Dictionary is :", len(dictionary))
dictionary2 = dictionary.copy()
print("\n New Dictionary is :", dictionary2)
dictionary.clear()
print("\n Updated Dictionary is :", dictionary)

