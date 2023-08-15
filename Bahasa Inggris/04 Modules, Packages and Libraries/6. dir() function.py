# The dir() Function
# The dir() function returns a sorted list of attributes and methods for an object.
# For built-in objects, it lists the available attributes and methods.

# Using dir() with a module
import math

# Get a list of attributes and methods in the math module
math_attributes = dir(math)
print("Attributes and methods in math module:")
for attribute in math_attributes:
    print(attribute)

# Using dir() with a custom object
class MyClass:
    def __init__(self):
        self.my_variable = 42
    
    def my_method(self):
        return "Hello, World!"

my_instance = MyClass()

# Get a list of attributes and methods in the MyClass instance
instance_attributes = dir(my_instance)
print("\nAttributes and methods in MyClass instance:")
for attribute in instance_attributes:
    print(attribute)
