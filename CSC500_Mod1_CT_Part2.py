# 1. Get user input for two numbers.
try:
    # If the variables from Part 1 are still in memory, they are overwritten here.
    num1 = float(input("\nEnter the first number (num1) for Part 2: "))
    num2 = float(input("Enter the second number (num2) for Part 2: "))

    # 2. Perform multiplication
    prod_result = num1 * num2

    # 3. Perform division, with error handling for division by zero
    print("-" * 30)
    print(f"Multiplication Result (num1 * num2): {prod_result}")

    if num2 != 0:
        div_result = num1 / num2
        print(f"Division Result (num1 / num2): {div_result}")
    else:
        # Handle the case where the divisor (num2) is zero
        print("Division Result: Cannot divide by zero.")

    print("-" * 30)

except ValueError:
    print("Invalid input. Please enter valid numbers.")