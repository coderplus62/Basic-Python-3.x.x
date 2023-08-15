# Explanation of Keywords in Python

# Keywords are reserved words that have special meanings in Python.
# Let's explore some common Python keywords and their usage.

# Defining a function using the 'def' keyword
def my_function():
    return "Hello, World!"

# 'if' statement to check a condition
x = 10
if x > 5:
    print("x is greater than 5")

# 'for' loop to iterate over a sequence
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# 'while' loop to execute code repeatedly
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# 'break' and 'continue' to control loop flow
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    elif i == 3:
        continue  # Skip iteration when i is 3
    print(i)

# 'return' statement to exit a function and return a value
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print("Result:", result)

# 'in' keyword for membership testing
my_string = "Python"
if 'y' in my_string:
    print("Letter 'y' is in the string")

# 'is' keyword for object identity comparison
x = [1, 2, 3]
y = x
if x is y:
    print("x and y refer to the same object")

# 'and', 'or', and 'not' for boolean operations
a = True
b = False
if a and not b:
    print("a is True and b is False")

# 'None' keyword for representing absence of a value
value = None
if value is None:
    print("Value is None")

# 'assert' keyword for debugging assertions
assert 5 > 2, "Assertion failed: 5 is not greater than 2"

# 'with' keyword for context management
with open("file.txt", "r") as file:
    content = file.read()
    print("File Content:", content)
