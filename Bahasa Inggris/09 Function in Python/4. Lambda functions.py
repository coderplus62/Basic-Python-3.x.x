# Explanation of Lambda Functions in Python

# Lambda functions are small, anonymous functions used for simple tasks.
# Let's explore lambda functions and how they are used with map(), filter(), and zip().

# 1. Using Lambda Functions with map() Function

numbers = [1, 2, 3, 4, 5]

# Using a lambda function to square each number using map()
squared_numbers = map(lambda x: x ** 2, numbers)
print("Squared numbers using map():", list(squared_numbers))

# 2. Using Lambda Functions with filter() Function

# Using a lambda function to filter even numbers using filter()
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers using filter():", list(even_numbers))

# 3. Using Lambda Functions with zip() Function

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Using a lambda function with zip() to combine two lists
person_info = list(zip(names, ages))
print("Person info using zip():", person_info)
