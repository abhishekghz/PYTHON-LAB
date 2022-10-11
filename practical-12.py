# PRACTICAL 12
# Write a python program to find factorial of a number using Recursion.
# Factorial of a number using recursion

def rec_fact(n):
    if n == 1:
        return n
    else:
        return n * rec_fact(n - 1)


num = int(input("Enter a no. : "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", rec_fact(num))
