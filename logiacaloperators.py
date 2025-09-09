# ------------------------------
# LOGICAL OPERATORS IN PYTHON
# ------------------------------
# Logical operators are used to combine conditional statements
# 1. and → True if BOTH conditions are True
# 2. or  → True if at least ONE condition is True
# 3. not → Reverses the result, True becomes False and vice versa

# Step 1: Take two integer inputs
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Step 2: Demonstrate logical operators

# AND operator
print("\nLogical AND (a > 0 and b > 0):", a > 0 and b > 0)

# OR operator
print("Logical OR (a > 0 or b > 0):", a > 0 or b > 0)

# NOT operator
print("Logical NOT (not (a > 0)):", not(a > 0))

# Combining multiple conditions
if a > 0 and b % 2 == 0:
    print(f"{a} is positive AND {b} is even")
else:
    print(f"Condition 'a > 0 and b even' not satisfied")

if a < 0 or b % 2 != 0:
    print(f"Either {a} is negative OR {b} is odd")
else:
    print("Condition 'a < 0 or b odd' not satisfied")
