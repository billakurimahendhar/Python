# ------------------------------
# SET
# ------------------------------
# 1. Set is an UNORDERED collection of UNIQUE elements.
# 2. It is MUTABLE (we can add/remove elements).
# 3. It does NOT allow DUPLICATES.
# 4. Syntax: set_name = {item1, item2, ...}
# 5. Common functions: add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference()

colors = {"red", "green", "blue", "red"}  # duplicate 'red' will be removed
print("\nSET EXAMPLES")
print("Original Set:", colors)

# Adding & Removing
colors.add("yellow")        # add element
colors.discard("green")     # remove if present (no error if absent)
print("After add & discard:", colors)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Other methods
set1.remove(2)   # remove specific element
print("After remove:", set1)
set1.pop()       # removes random element
print("After pop:", set1)
set1.clear()     # empties the set
print("After clear:", set1)


# ----------------------------------------