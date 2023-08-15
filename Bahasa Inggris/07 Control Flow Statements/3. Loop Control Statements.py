# Explanation of Loop Control Statements in Python

# Loop control statements allow you to control the execution of loops.
# Let's explore the break keyword, the continue keyword, and the pass keyword.

# 1. The break Keyword

# Using the break keyword to exit the loop prematurely
for i in range(5):
    if i == 3:
        break
    print("Value:", i)

# 2. The continue Keyword

# Using the continue keyword to skip the current iteration and proceed to the next
for i in range(5):
    if i == 2:
        continue
    print("Value:", i)

# 3. The pass Keyword

# Using the pass keyword as a placeholder for future code
for i in range(3):
    pass  # This loop doesn't do anything yet

# Using pass in an empty function or class
def my_function():
    pass  # Function without any code

class MyClass:
    pass  # Class definition without any attributes/methods
