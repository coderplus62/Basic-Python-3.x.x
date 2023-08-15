# Explanation of Conditional Statements in Python

# Conditional statements allow you to control the flow of your program based on conditions.
# Let's explore the if statement, the elif clause, and the else clause.

# 1. The if Statement

x = 10

# Using the if statement to check a condition
if x > 5:
    print("x is greater than 5")

# 2. The elif Clause

y = 3

# Using the elif clause for multiple conditions
if y > 5:
    print("y is greater than 5")
elif y == 5:
    print("y is equal to 5")
else:
    print("y is less than 5")

# 3. The else Clause

z = 8

# Using the else clause to handle other cases
if z > 10:
    print("z is greater than 10")
else:
    print("z is not greater than 10")

# Combining conditions

a = 15
b = 20

# Using logical operators to combine conditions
if a > 10 and b > 10:
    print("Both 'a' and 'b' are greater than 10")
elif a > 10 or b > 10:
    print("At least one of 'a' or 'b' is greater than 10")
else:
    print("Neither 'a' nor 'b' is greater than 10")
