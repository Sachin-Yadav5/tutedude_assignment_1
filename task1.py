# Performing Basic Mathematical Operations


# Taking two numbers as input from the user
number1 = float(input('Enter your first number: '))
number2 = float(input('Enter your second number: '))


#Performing Action
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2

#Handling division for safety

if number2!=0:
    division = number1 / number2

else:
    division = "This number cannot divided by zero or Please check the numbers again)"
    

# Displaying results
print("\nAddition:", (addition))
print("Subtraction:", (subtraction))
print("Multiplication:", (multiplication))
print("Division:", (division))

