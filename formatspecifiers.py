# ------------------------------
# FORMAT SPECIFIERS IN PYTHON
# ------------------------------

# 1. Using % operator
name = "Alice"
age = 20
marks = 95.6789

print("Name: %s, Age: %d, Marks: %.2f" % (name, age, marks))
# %s → string
# %d → integer
# %f → float (%.2f = 2 decimal places)

# 2. Using str.format()
print("Name: {}, Age: {}, Marks: {:.2f}".format(name, age, marks))
# {} → placeholder
# {:.2f} → 2 decimal places

# 3. Using f-strings (modern & preferred)
print(f"Name: {name}, Age: {age}, Marks: {marks:.2f}")

# More format specifiers
num = 255

print("Binary: {0:b}".format(num))    # binary
print("Octal: {0:o}".format(num))     # octal
print("Hexadecimal: {0:x}".format(num)) # hexadecimal (lowercase)
print("Hexadecimal: {0:X}".format(num)) # hexadecimal (uppercase)

# Width and alignment
print("Right aligned: {:>10}".format("Hi"))
print("Left aligned: {:<10}".format("Hi"))
print("Center aligned: {:^10}".format("Hi"))

# Padding with zeros
print("Number with leading zeros: {:05d}".format(42))
