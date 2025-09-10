# ------------------------------
# STRING FUNCTIONS IN PYTHON
# ------------------------------
# Strings are sequences of characters.
# Python provides many built-in string methods for manipulation.

# Step 1: Create a string
text = "  Hello Python Programming  "

# Step 2: Demonstrate string functions

print("Original String:", text)

# 1. strip() - removes spaces from both ends
print("After strip():", text.strip())

# 2. lower() - converts to lowercase
print("Lowercase:", text.lower())

# 3. upper() - converts to uppercase
print("Uppercase:", text.upper())

# 4. title() - capitalizes first letter of each word
print("Title Case:", text.title())

# 5. replace() - replaces one string with another
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# 6. split() - splits string into a list
print("Split into words:", text.split())

# 7. join() - join elements of a list into string
words = ["I", "love", "Python"]
print("Join words:", " ".join(words))

# 8. find() - returns index of substring (or -1 if not found)
print("Index of 'Python':", text.find("Python"))

# 9. count() - counts occurrences of substring
print("Count of 'o':", text.count("o"))

# 10. len() - length of string
print("Length of string:", len(text))

# 11. startswith() - check if string starts with substring
print("Starts with 'Hello':", text.strip().startswith("Hello"))

# 12. endswith() - check if string ends with substring
print("Ends with 'ing':", text.strip().endswith("ing"))

# 13. isalpha() - True if all characters are alphabets
print("'Hello'.isalpha():", "Hello".isalpha())

# 14. isdigit() - True if all characters are digits
print("'12345'.isdigit():", "12345".isdigit())

# 15. isalnum() - True if all characters are alphanumeric
print("'Hello123'.isalnum():", "Hello123".isalnum())
