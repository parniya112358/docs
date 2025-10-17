#  Simple calculator

# Get two numbers from the user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display available operations
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user choice
choice = input("Enter choice number (1/2/3/4): ")

# Perform operation based on user's choice
if choice == '1':
    result = num1 + num2
    print("Result of Addition =", result)

elif choice == '2':
    result = num1 - num2
    print("Result of Subtraction =", result)

elif choice == '3':
    result = num1 * num2
    print("Result of Multiplication =", result)

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result of Division =", result)
    else:
        print("Error: Division by zero is not allowed!")

else:
    print("Invalid choice!")
