# ------------------------------
# ARITHMETIC OPERATORS IN PYTHON
# ------------------------------
# Arithmetic operators are used to perform basic math operations
# +  : Addition
# -  : Subtraction
# *  : Multiplication
# /  : Division (returns float)
# // : Floor Division (returns integer part of division)
# %  : Modulus (returns remainder)
# ** : Exponentiation (power)

# Step 1: Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_div = num1 // num2
modulus = num1 % num2
exponent = num1 ** num2

# Step 3: Print results
print("\n--- Arithmetic Operations ---")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {floor_div}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {exponent}")
