# List Comprehension in Python
# -----------------------------
# It is a concise way to create lists.
# Syntax:
#   [expression for item in iterable if condition]

# Example 1: Create a list of numbers from 0 to 9
numbers = [x for x in range(10)]
print("Numbers:", numbers)

# Example 2: Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# Example 3: Even numbers from 0 to 20
evens = [x for x in range(21) if x % 2 == 0]
print("Even Numbers:", evens)

# Example 4: Odd numbers from 0 to 20
odds = [x for x in range(21) if x % 2 != 0]
print("Odd Numbers:", odds)

# Example 5: First letter of each word in a list
words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words]
print("First Letters:", first_letters)

# Example 6: Convert all strings to uppercase
upper_words = [word.upper() for word in words]
print("Uppercase Words:", upper_words)

# Example 7: Create a list of common elements using condition
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [x for x in list1 if x in list2]
print("Common Elements:", common)

# Example 8: Nested list comprehension (multiplication table)
table = [[x*y for y in range(1, 6)] for x in range(1, 6)]
print("Multiplication Table (1 to 5):")
for row in table:
    print(row)

nums=[x for x in range(0,100) if x%2==0]
print(nums)
