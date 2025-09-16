# match-case statement in Python (introduced in Python 3.10)
# ----------------------------------------------------------
# It works like switch-case in other languages (C, Java, etc.).
# Used for pattern matching.
#
# Syntax:
# match variable:
#     case value1:
#         # code block
#     case value2:
#         # code block
#     case _:
#         # default case (like "else")

# Example 1: Simple number matching
num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("You entered ONE")
    case 2:
        print("You entered TWO")
    case 3:
        print("You entered THREE")
    case _:
        print("Invalid choice!")   # default case

# Example 2: Match strings
day = input("Enter a day (Mon/Tue/Wed): ")

match day:
    case "Mon":
        print("Start of the week!")
    case "Tue":
        print("Second day of the week!")
    case "Wed":
        print("Mid-week!")
    case _:
        print("Other day!")

# Example 3: Match multiple values in one case
vowel = input("Enter a letter: ").lower()

match vowel:
    case "a" | "e" | "i" | "o" | "u":
        print(f"{vowel} is a vowel")
    case _:
        print(f"{vowel} is a consonant")

# Example 4: Using conditions (guards) in case
age = int(input("Enter your age: "))

match age:
    case a if a < 18:
        print("You are a Minor")
    case a if 18 <= a < 60:
        print("You are an Adult")
    case a if a >= 60:
        print("You are a Senior Citizen")
    case _:
        print("Invalid age")
