# -----------------------------
# SCOPE IN PYTHON
# -----------------------------
# Scope means the region where a variable is recognized and can be used.
# Python uses the "LEGB Rule" for scope resolution:
#   L → Local (inside a function)
#   E → Enclosing (functions inside functions)
#   G → Global (declared outside functions)
#   B → Built-in (reserved names like print, len, etc.)

# Example 1: Global Scope
x = 10  # Global variable

def show_global():
    print("Inside function, accessing global x:", x)

show_global()
print("Outside function, global x:", x)


# Example 2: Local Scope
def local_example():
    y = 20  # Local variable
    print("Inside function, local y:", y)

local_example()
# print(y)   # ❌ ERROR, y not accessible outside function


# Example 3: Enclosing Scope (Nested Functions)
def outer_function():
    z = 30  # Enclosing variable

    def inner_function():
        print("Inside inner function, accessing enclosing z:", z)

    inner_function()

outer_function()


# Example 4: Using 'global' keyword
a = 50

def modify_global():
    global a   # declare that we want to use the global 'a'
    a = 100
    print("Inside function, modified global a:", a)

modify_global()
print("Outside function, global a after modification:", a)


# Example 5: Using 'nonlocal' keyword
def outer():
    b = 200

    def inner():
        nonlocal b   # refers to 'b' in enclosing scope
        b = 300
        print("Inside inner(), modified enclosing b:", b)

    inner()
    print("Inside outer(), after inner() call, b:", b)

outer()
