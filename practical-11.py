# PRACTICAL 11
# Write a Python script that prints prime numbers less than 20.

print("Prime numbers between 1 and 20 :")
number = 20
for num in range(number):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
              print(num)
