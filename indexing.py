# ------------------------------
# STRING INDEXING IN PYTHON
# ------------------------------

# Step 1: Create a string
text = "PYTHON"

# Step 2: Access characters using positive indexing
print("Original String:", text)
print("Character at index 0:", text[0])   # P
print("Character at index 1:", text[1])   # Y
print("Character at index 2:", text[2])   # T
print("Character at index 5:", text[5])   # N

# Step 3: Access characters using negative indexing
print("\nUsing Negative Indexing:")
print("Character at index -1 (last):", text[-1])   # N
print("Character at index -2:", text[-2])         # O
print("Character at index -3:", text[-3])         # H
print("Character at index -6 (first):", text[-6]) # P

# Step 4: Loop through string using index
print("\nLooping with index:")
for i in range(len(text)):
    print(f"Index {i} → {text[i]}")

# Step 5: Trying to access invalid index (will cause error)
# Uncomment the below line to test
# print(text[10])  # IndexError: string index out of range
