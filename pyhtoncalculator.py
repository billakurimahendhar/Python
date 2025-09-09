# ------------------------------
# SIMPLE CALCULATOR IN PYTHON
# ------------------------------
# This calculator performs addition, subtraction, multiplication, and division

# Step 1: Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Show options to the user
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 3: Take the choice as input
choice = input("Enter choice (1/2/3/4): ")

# Step 4: Perform operation using if-elif-else
if choice == "1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == "2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == "3":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == "4":
    if num2 != 0:  # check to avoid division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid choice. Please select 1/2/3/4.")
