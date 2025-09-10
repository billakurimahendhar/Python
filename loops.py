# ------------------------------
# LOOPS IN PYTHON (Examples)
# ------------------------------

print("===== FOR LOOP EXAMPLES =====")

# Example 1: Print numbers 1 to 5
for i in range(1, 6):
    print("For loop number:", i)

# Example 2: Print characters in a string
word = "PYTHON"
for ch in word:
    print("Character:", ch)

# Example 3: Multiplication table
num = 3
print(f"\nMultiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Example 4: Using continue
print("\nNumbers from 1 to 10 except 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Example 5: Using break
print("\nStop loop when number is 7:")
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# Example 6: For loop with else
print("\nFor loop with else (no break):")
for i in range(3):
    print("Iteration:", i)
else:
    print("For loop finished successfully!")


print("\n===== WHILE LOOP EXAMPLES =====")

# Example 1: Counting 1 to 5
i = 1
while i <= 5:
    print("While loop number:", i)
    i += 1

# Example 2: Sum of digits
n = 1234
sum_digits = 0
temp = n
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print(f"Sum of digits of {n} = {sum_digits}")

# Example 3: Factorial
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n} = {fact}")

# Example 4: Using break
print("\nWhile loop with break:")
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

# Example 5: Using continue
print("\nWhile loop with continue (skip 3):")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Example 6: While loop with else
print("\nWhile loop with else:")
i = 1
while i <= 3:
    print("Iteration:", i)
    i += 1
else:
    print("While loop finished successfully!")
