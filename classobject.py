# ----------------------------------------
# CLASSES AND OBJECTS IN PYTHON
# ----------------------------------------
# THEORY:
# 1. Class is a blueprint for creating objects.
# 2. Object is an instance of a class.
# 3. Classes help organize code using attributes (variables) and methods (functions).
# 4. Syntax:
#       class ClassName:
#           def __init__(self, parameters):
#               # constructor to initialize object
#           def method_name(self, parameters):
#               # method code
# 5. 'self' refers to the current instance of the class.

# Example 1: Simple class and object
class Student:
    # Constructor to initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display student info
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
s1 = Student("Alice", 21)
s2 = Student("Bob", 22)

# Accessing methods
s1.display()
s2.display()


# Example 2: Class with multiple methods
class Circle:
    pi = 3.14159  # class variable shared by all objects

    def __init__(self, radius):
        self.radius = radius  # instance variable

    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

# Creating object
c1 = Circle(5)

print("Circle radius:", c1.radius)
print("Area:", c1.area())
print("Circumference:", c1.circumference())


# Example 3: Modifying object attributes
c1.radius = 10
print("\nAfter modifying radius:")
print("New radius:", c1.radius)
print("New area:", c1.area())


# Example 4: Class and object with dynamic input
name = input("\nEnter student name: ")
age = int(input("Enter student age: "))
student = Student(name, age)
student.display()
