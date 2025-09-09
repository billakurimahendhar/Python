# ------------------------------
# INPUT() FUNCTION IN PYTHON
# ------------------------------
# The input() function is used to take input from the user.
# By default, input() always returns data as a STRING type.
# So, if we need integers or floats, we must use TYPECASTING.

# Example 1: Taking a string input (default behavior)
name = input("Enter your name: ")  # user types something, e.g., Mahi
print("Hello,", name, "| Type:", type(name))  # always <class 'str'>

# Example 2: Taking integer input
# Since input() returns a string, we must convert it into int
age = int(input("Enter your age: "))  # e.g., user types 21
print("Your age:", age, "| Type:", type(age))

# Example 3: Taking float input
height = float(input("Enter your height in feet: "))  # e.g., 5.9
print("Your height:", height, "| Type:", type(height))

# Example 4: Taking multiple inputs in one line
# Using split() method to separate values by space
x, y = input("Enter two numbers separated by space: ").split()
print("x:", x, "| y:", y)  # Note: x and y are still strings

# Convert them into integers
x, y = map(int, input("Enter two numbers again (space separated): ").split())
print("Sum =", x + y, "| Type of x:", type(x), "| Type of y:", type(y))
