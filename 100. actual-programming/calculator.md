def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    elif operation == "mod":
        return num1 % num2
    else:
        return "Invalid operation"


# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide, mod): ")

# Call the calculator function
result = calculator(num1, num2, operation)

print("Result:", result)
