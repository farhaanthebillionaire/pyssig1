# Task 1: Perform Basic Mathematical Operations

# Take two numbers as input
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    if num2 != 0:
        division = num1 / num2  # Division will still give float result
    else:
        division = "Undefined (cannot divide by zero)"

    # Display results
    print("\n--- Results ---")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)

except ValueError:
    print("Invalid input! Please enter valid integers.")
