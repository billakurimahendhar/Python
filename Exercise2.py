# ------------------------------
# SIMPLE SHOPPING CART PROGRAM
# ------------------------------
# Using only 3 variables: item_name, price, total

# Step 1: Take item details
item_name = input("Enter the item name: ")
price = float(input(f"Enter the price of {item_name}: "))

# Step 2: Take another item
item_name2 = input("Enter second item name: ")
price2 = float(input(f"Enter the price of {item_name2}: "))

# Step 3: Take third item
item_name3 = input("Enter third item name: ")
price3 = float(input(f"Enter the price of {item_name3}: "))

# Step 4: Calculate total
total = price + price2 + price3

# Step 5: Print summary
print("\n--- Shopping Cart ---")
print(f"1. {item_name}: ${price}")
print(f"2. {item_name2}: ${price2}")
print(f"3. {item_name3}: ${price3}")
print("Total Amount: $", total)
