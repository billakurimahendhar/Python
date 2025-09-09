# ------------------------------
# CONDITIONAL EXPRESSION / TERNARY OPERATOR
# ------------------------------
# It is a one-line if-else statement
# Syntax:
# value_if_true if condition else value_if_false

# Example 1: Check if a number is even or odd
num = int(input("Enter a number: "))

result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}")

# Example 2: Find the maximum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max_num = a if a > b else b
print(f"The maximum number is {max_num}")

# Example 3: Check if a person is adult or minor
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(f"You are an {status}")
