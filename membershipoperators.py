# Membership Operators in Python
# They are used to test whether a value or variable is found in a sequence (like string, list, tuple, set, dictionary).
# Two operators:
#   in      → Returns True if value is present
#   not in  → Returns True if value is NOT present

# Example with string
text = "Python Programming"
print("P" in text)        # True, because "P" exists in the string
print("Java" in text)     # False, because "Java" does not exist
print("Code" not in text) # True, because "Code" is not in the string

# Example with list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)       # True
print("grape" not in fruits)   # True

# Example with tuple
numbers = (10, 20, 30, 40)
print(20 in numbers)       # True
print(50 not in numbers)   # True

# Example with set
colors = {"red", "green", "blue"}
print("green" in colors)     # True
print("yellow" not in colors) # True

# Example with dictionary
student = {"name": "Mahi", "age": 21, "city": "Hyderabad"}
print("name" in student)       # True (checks keys by default)
print("Mahi" in student)       # False (because it only checks keys, not values)
print("city" not in student)   # False
