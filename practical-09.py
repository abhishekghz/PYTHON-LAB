# PRACTICAL 09
# Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
# [ Formula: c/5 = f-32/9]

print("1.) Convert Celsius to Fahrenheit \n")
print("2.) Convert Fahrenheit to Celsius \n")
opt=int(input("Choose any Option (1 or 2) : "))
if opt == 1:
    print("Convert Celsius to Fahrenheit \n")
    cel = float(input("Enter Temperature in Celsius: "))
    fahr = (cel*9/5)+32
    print("Temperature in Fahrenheit =",fahr)
elif opt == 2:
    print("Convert temperatures from Fahrenheit to Celsius \n")
    fahr = float(input("Enter Temperature in Fahrenheit: "))
    cel=(fahr-32)*5/9
    print("Temperature in Celsius =",cel)
else:
    print("Invalid Option")