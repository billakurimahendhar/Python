# ------------------------------
# CONDITIONAL STATEMENTS IN PYTHON
# ------------------------------
# Conditional statements allow us to make decisions in code.
# Python has three main types:
# 1. if
# 2. if...else
# 3. if...elif...else

# Step 1: Take input from the user
num = int(input("Enter a number: "))

# 1. Simple if statement
if num > 0:
    print("The number is positive.")

# 2. if...else statement
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3. if...elif...else statement
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 4. Nested if statement
if num >= 0:
    if num == 0:
        print("The number is zero (inside nested if).")
    else:
        print("The number is positive (inside nested if).")
