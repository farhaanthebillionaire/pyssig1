# Task 1: Perform Basic Mathematical Operations

# Step 1: Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division carefully to avoid division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero is not allowed)"

# Step 3: Display the results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
