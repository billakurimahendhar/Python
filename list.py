# LIST
# ------------------------------
# 1. List is an ordered collection of items.
# 2. It is MUTABLE (we can change elements).
# 3. It allows DUPLICATES.
# 4. Syntax: list_name = [item1, item2, ...]
# 5. Common functions: append(), insert(), remove(), pop(), sort(), reverse(), count(), index(), extend()

# Example of List
fruits = ["apple", "banana", "cherry", "apple"]
print("LIST EXAMPLES")
print("Original List:", fruits)

# Accessing elements using index
print("First element:", fruits[0])     
print("Last element:", fruits[-1])     

# Modifying element
fruits[1] = "orange"
print("After modification:", fruits)

# Adding elements
fruits.append("grape")      # add at end
fruits.insert(1, "mango")   # insert at index
print("After append & insert:", fruits)

# Removing elements
fruits.remove("apple")   # removes first occurrence
fruits.pop(2)            # removes element at index 2
print("After remove & pop:", fruits)

# Functions
print("Count of 'apple':", fruits.count("apple"))
print("Index of 'grape':", fruits.index("grape"))
fruits.extend(["kiwi", "melon"])   # add multiple elements
print("After extend:", fruits)
fruits.sort()   # sort ascending
print("After sort:", fruits)
fruits.reverse() # reverse list
print("After reverse:", fruits)

