# Explanation of Loops in Python

# Loops allow you to execute a block of code repeatedly.
# Let's explore the while loop, the for loop, the range() function,
# and how to loop through lists, strings, dictionaries, and nested loops.

# 1. The while Statement

count = 0

# Using the while loop to repeat code while a condition is true
while count < 5:
    print("Count:", count)
    count += 1

# 2. The for Statement

# Using the for loop to iterate over a sequence (e.g., range)
for i in range(5):
    print("Value:", i)

# 3. The range() Function

# Using the range() function to create a sequence
numbers = list(range(1, 6))  # Create a list of numbers from 1 to 5
print("Numbers:", numbers)

# 4. Looping Through Lists

my_list = [10, 20, 30, 40, 50]

# Using the for loop to iterate through a list
for item in my_list:
    print("Item:", item)

# 5. Looping Through Strings

my_string = "Python"

# Using the for loop to iterate through a string
for char in my_string:
    print("Character:", char)

# 6. Looping Through Dictionaries

my_dict = {"a": 1, "b": 2, "c": 3}

# Using the for loop to iterate through dictionary keys
for key in my_dict:
    value = my_dict[key]
    print("Key:", key, "Value:", value)

# 7. Nested Loops

# Using nested loops to create a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{i} * {j} = {result}")
