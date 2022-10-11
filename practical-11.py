# PRACTICAL 11
# Write a Python script that prints prime numbers less than 20.

print("Prime numbers between 1 and 20 :")
num = 20
for a in range(num):
    if a > 1:
       for i in range(2, a):
           if (a % i) == 0:
               break
       else:
           print(a)
