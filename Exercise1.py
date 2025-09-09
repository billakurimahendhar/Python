# ------------------------------
# Exercise: Area of a Rhombus
# ------------------------------

# Formula: Area = (d1 × d2) / 2

# Step 1: Take diagonals as input
d1 = float(input("Enter the length of first diagonal: "))
d2 = float(input("Enter the length of second diagonal: "))

# Step 2: Calculate area
area = (d1 * d2) / 2

# Step 3: Print result
print("The area of the rhombus is:", area)

# Optional: Calculate perimeter if side is given
side = float(input("Enter the side length of rhombus (for perimeter): "))
perimeter = 4 * side
print("The perimeter of the rhombus is:", perimeter)
