# ----------------------------------------
# FUNCTIONS IN PYTHON
# ----------------------------------------

# THEORY:
# 1. A function is a block of code that performs a specific task.
# 2. Functions make code reusable, organized, and easier to read.
# 3. Types of functions:
#    - Built-in functions (print(), len(), type(), etc.)
#    - User-defined functions (created using def keyword)
# 4. Syntax:
#       def function_name(parameters):
#           # function body
#           return value
# 5. Function can:
#    - Take arguments (input)
#    - Return values (output)
#    - Or do both


# Example 1: Simple function (no parameters, no return)
def greet():
    print("Hello, welcome to Python functions!")

greet()  # function call


# Example 2: Function with parameters
def add_numbers(a, b):
    print("Sum is:", a + b)

add_numbers(5, 10)
add_numbers(7, 3)


# Example 3: Function with return value
def square(n):
    return n * n

result = square(6)
print("Square of 6 is:", result)


# Example 4: Function with default parameter
def greet_user(name="Guest"):
    print("Hello,", name)

greet_user("Alice")
greet_user()   # uses default value


# Example 5: Function with multiple return values
def calc(a, b):
    return a+b, a-b, a*b, a/b

add, sub, mul, div = calc(10, 5)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
