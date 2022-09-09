# PRACTICAL 09
# Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
# [ Formula: c/5 = f-32/9]

print("1.) Convert Celsius to Fahrenheit \n")
print("2.) Convert Fahrenheit to Celsius \n")
option = int(input("Choose any Option (1 or 2) : "))
if option == 1:
    print("Convert Celsius to Fahrenheit \n")
    Celsius = float(input("Enter Temperature in Celsius: "))
    Fahrenheit = (Celsius*9/5)+32
    print("Temperature in Fahrenheit = ", Fahrenheit)
elif option == 2:
    print("Convert temperatures from Fahrenheit to Celsius \n")
    Fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5/9
    print("Temperature in Celsius = ", Celsius)
else:
    print("Invalid Option.")
