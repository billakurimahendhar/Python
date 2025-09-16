# ----------------------------------------
# ARGUMENTS IN PYTHON FUNCTIONS
# ----------------------------------------

# THEORY:
# Python supports different types of arguments:
# 1. Positional Arguments     -> Values passed in order
# 2. Keyword Arguments        -> Values passed with parameter name
# 3. Default Arguments        -> Parameter has a default value
# 4. Variable-length Arguments:
#       - *args   -> to pass multiple positional arguments
#       - **kwargs -> to pass multiple keyword arguments


# ------------------------------
# 1. POSITIONAL ARGUMENTS
# ------------------------------
def add(a, b):
    print("Sum is:", a + b)

add(10, 20)   # arguments are matched by position
add(5, 15)


# ------------------------------
# 2. KEYWORD ARGUMENTS
# ------------------------------
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(name="Alice", age=21)
student_info(age=22, name="Bob")   # order doesn’t matter when using keywords


# ------------------------------
# 3. DEFAULT ARGUMENTS
# ------------------------------
def greet_user(name="Guest"):
    print("Hello,", name)

greet_user("Charlie")   # uses given value
greet_user()            # uses default value


# ------------------------------
# 4. VARIABLE-LENGTH ARGUMENTS
# ------------------------------

# (a) *args -> allows multiple positional arguments (stored as tuple)
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum of numbers:", total)

sum_numbers(10, 20)
sum_numbers(1, 2, 3, 4, 5)


# (b) **kwargs -> allows multiple keyword arguments (stored as dictionary)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details(name="David", age=25, city="New York")
print_details(course="Python", duration="3 months")


# ------------------------------
# 5. MIXING ARGUMENT TYPES
# ------------------------------
def mixed_example(a, b=5, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

mixed_example(10)
mixed_example(10, 20, 30, 40, x=100, y=200)
