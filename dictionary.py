# ----------------------------------------
# DICTIONARY IN PYTHON
# ----------------------------------------

# THEORY:
# 1. Dictionary is an UNORDERED collection of key-value pairs.
# 2. Keys must be UNIQUE and IMMUTABLE (int, str, tuple).
# 3. Values can be of ANY type (homogeneous or heterogeneous).
# 4. Dictionary is MUTABLE (we can add, update, delete key-value pairs).
# 5. Syntax: dict_name = {key1: value1, key2: value2, ...}
# 6. Common functions:
#    - keys(), values(), items()
#    - get()
#    - update()
#    - pop(), popitem()
#    - clear()

# Example of Dictionary
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science"
}

print("DICTIONARY EXAMPLES")
print("Original Dictionary:", student)

# Accessing values
print("Name:", student["name"])          # direct access
print("Course (using get):", student.get("course"))  # safer access

# Adding new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Updating value
student["age"] = 22
print("After updating age:", student)

# Removing elements
student.pop("course")       # remove specific key
print("After pop:", student)
student.popitem()           # remove last inserted item
print("After popitem:", student)

# Dictionary functions
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Updating with another dictionary
student.update({"city": "New York", "age": 23})
print("After update:", student)

# Clearing dictionary
student.clear()
print("After clear:", student)


# ----------------------------------------
# SUMMARY:
# Dictionary -> Unordered, Mutable, Stores key-value pairs
# Keys   -> must be unique & immutable
# Values -> can be any type
# ----------------------------------------
