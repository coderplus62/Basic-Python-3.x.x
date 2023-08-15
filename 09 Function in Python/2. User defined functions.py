# Explanation of User-Defined Functions in Python

# User-defined functions allow you to create reusable blocks of code.
# Let's explore creating functions with single and multiple arguments,
# default arguments, variable length arguments, docstrings, and nested functions.

# 1. Functions with a Single Argument

def greet(name):
    print("Hello,", name)

greet("Alice")

# 2. Functions with Multiple Arguments and a Return Statement

def add_numbers(x, y):
    return x + y

result = add_numbers(5, 3)
print("Sum:", result)

# 3. Functions with Default Arguments

def power(base, exponent=2):
    return base ** exponent

squared = power(3)
cubed = power(3, 3)
print("Squared:", squared)
print("Cubed:", cubed)

# 4. Functions with Variable Length Arguments

def print_numbers(*args):
    for num in args:
        print("Number:", num)

print_numbers(10, 20, 30)

# 5. DocStrings

def my_function():
    """
    This is a docstring.
    It provides a description of the function's purpose and usage.
    """
    print("Function executed")

print(my_function.__doc__)  # Display the docstring

# 6. Nested Functions and Non-Local Variables

def outer_function(x):
    def inner_function():
        nonlocal x  # Access the outer function's variable
        x += 10
        print("Inner:", x)
    inner_function()
    print("Outer:", x)

outer_function(5)
