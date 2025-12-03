# Simple Calculator in Python

# Asking the user for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Asking which operation to perform
print("Choose operation: +, -, *, /")
operation = input("Enter operation: ")

# Performing calculation using if/elif
if operation == "+":
    result = num1 + num2
    print("Answer:", result)

elif operation == "-":
    result = num1 - num2
    print("Answer:", result)

elif operation == "*":
    result = num1 * num2
    print("Answer:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Answer:", result)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operation")
