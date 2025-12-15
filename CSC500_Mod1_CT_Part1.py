# Part 1: Addition and Subtraction

# 1. Get user input for two numbers.
# We use float() to allow for both integers and decimal numbers.
try:
    num1 = float(input("Enter the first number (num1): "))
    num2 = float(input("Enter the second number (num2): "))

    # 2. Perform addition
    sum_result = num1 + num2

    # 3. Perform subtraction (num1 - num2)
    diff_result = num1 - num2

    # 4. Display the results
    print("-" * 30)
    print(f"Addition Result (num1 + num2): {sum_result}")
    print(f"Subtraction Result (num1 - num2): {diff_result}")
    print("-" * 30)

except ValueError:
    print("Invalid input. Please enter valid numbers.")