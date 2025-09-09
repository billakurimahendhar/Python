# ------------------------------
# MORE MATH FUNCTIONS IN PYTHON
# ------------------------------
# Python's math module provides various functions for mathematical operations

import math

# Take a number from the user
num = float(input("Enter a number: "))
num2 = float(input("Enter another number (for min/max and power): "))

# 1. Square root
print("Square root:", math.sqrt(num))

# 2. Power
print(f"{num} raised to {num2} =", math.pow(num, num2))

# 3. Absolute value
print("Absolute value:", abs(num))

# 4. Ceiling and Floor
print("Ceiling:", math.ceil(num))
print("Floor:", math.floor(num))

# 5. Factorial (integer only, >=0)
n = int(num)
if n >= 0:
    print("Factorial:", math.factorial(n))
else:
    print("Factorial not defined for negative numbers")

# 6. Round
print("Rounded value:", round(num))

# 7. Trigonometric functions (input in radians)
print("sin:", math.sin(num))
print("cos:", math.cos(num))
print("tan:", math.tan(num))

# 8. Logarithmic functions
if num > 0:
    print("Natural log (ln):", math.log(num))       # ln(x)
    print("Log base 10:", math.log10(num))          # log10(x)
else:
    print("Log not defined for non-positive numbers")

# 9. Max and Min
print("Maximum:", max(num, num2))
print("Minimum:", min(num, num2))

# 10. Degrees and Radians
print("Degrees:", math.degrees(num))  # convert radians → degrees
print("Radians:", math.radians(num))  # convert degrees → radians

# 11. Exponential and e
print("Exponential e^x:", math.exp(num))
print("Value of e:", math.e)

# 12. Modf (fractional and integer part)
frac_part, int_part = math.modf(num)
print("Fractional part:", frac_part, "Integer part:", int_part)
