# Dictionary of operations using lambda functions
operations = {
    '1': lambda x, y: x.__add__(y),
    '2': lambda x, y: x.__sub__(y),
    '3': lambda x, y: x.__mul__(y),
    '4': lambda x, y: x.__truediv__(y) if y != 0 else "Cannot divide by zero"
}

#Titles and operation options
print("Calculator")
print("Select operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

# Infinite loop for repeated calculations
while True:
    # Using walrus operator to assign and check in one line
    if (choice := input("Enter choice (1/2/3/4): ")) in operations:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Perform operation using lambda from dictionary
        result = operations[choice](num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice")

    # Asking if user wants another calculation
   if (again := input("Want to calculate again? (y/n): ")) != 'y':
    break 
