# ------------------------------
# TYPECASTING IN PYTHON
# ------------------------------
# Typecasting means converting one data type into another.
# Two types:
# 1. Implicit Typecasting (done automatically by Python)
# 2. Explicit Typecasting (done manually by the programmer)

# ----------------------------------------
# 1. Implicit Typecasting (automatic)
# ----------------------------------------
# Python automatically converts smaller data types into larger data types
# to avoid data loss.

a = 10          # int
b = 3.5         # float
c = a + b       # int + float → float
print("Implicit Typecasting: 10 + 3.5 =", c, "| Type:", type(c))

# ----------------------------------------
# 2. Explicit Typecasting (manual)
# ----------------------------------------
# Programmer explicitly converts one type into another using functions like:
# int(), float(), str(), bool()

# Integer to Float
num_int = 10
num_float = float(num_int)  # manually converting int → float
print("Explicit (int → float):", num_int, "→", num_float)

# Float to Integer
num_f = 12.78
num_i = int(num_f)  # removes decimal part (no rounding)
print("Explicit (float → int):", num_f, "→", num_i)

# Integer to String
num = 100
num_str = str(num)  # converts integer to string
print("Explicit (int → str):", num, "→", num_str, "| Type:", type(num_str))

# String to Integer
s = "123"
s_int = int(s)  # converts numeric string to integer
print("Explicit (str → int):", s, "→", s_int, "| After +10 =", s_int + 10)

# Boolean Conversion
print("Explicit (int → bool) 0:", bool(0))       # False (0 is treated as False)
print("Explicit (int → bool) 5:", bool(5))       # True (non-zero is True)
print("Explicit (str → bool ''):", bool(""))     # False (empty string is False)
print("Explicit (str → bool 'Hi'):", bool("Hi")) # True (non-empty string is True)
