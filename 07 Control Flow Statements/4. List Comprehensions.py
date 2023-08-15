# Explanation of List Comprehensions in Python

# List comprehensions provide a concise way to create lists.
# Let's explore how to use list comprehensions to create and manipulate lists.

# Traditional way to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print("Squares using traditional method:", squares)

# Using list comprehension to create a list of squares
squares_comp = [num ** 2 for num in numbers]
print("Squares using list comprehension:", squares_comp)

# List comprehension with conditional expression
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("Even squares using list comprehension:", even_squares)

# Creating a list of tuples using list comprehension
pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pairs using list comprehension:", pairs)

# Flattening a 2D list using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix using list comprehension:", flattened)

# Using list comprehension to filter elements
numbers = [10, 20, 30, 40, 50]
filtered = [num for num in numbers if num > 30]
print("Filtered numbers using list comprehension:", filtered)
