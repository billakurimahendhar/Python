# TUPLE
# ------------------------------
# 1. Tuple is an ordered collection of items.
# 2. It is IMMUTABLE (cannot be changed).
# 3. It allows DUPLICATES.
# 4. Syntax: tuple_name = (item1, item2, ...)
# 5. Common functions: count(), index()

numbers = (10, 20, 30, 10, 40)
print("\nTUPLE EXAMPLES")
print("Tuple:", numbers)

# Accessing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Functions
print("Count of 10:", numbers.count(10))
print("Index of 30:", numbers.index(30))

# Slicing
print("Tuple slice (1:4):", numbers[1:4])

