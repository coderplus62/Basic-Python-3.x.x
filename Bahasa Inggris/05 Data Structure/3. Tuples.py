# Explanation of Tuples in Python

# Tuples are similar to lists, but they are immutable (cannot be changed after creation).
# Let's explore accessing tuple elements, immutability, concatenating tuples,
# unpacking tuples, and using tuple methods.

# 1. Accessing Tuple Elements

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Accessing tuple elements using indexing
first_element = my_tuple[0]     # Access the first element (10)
third_element = my_tuple[2]     # Access the third element (30)
last_element = my_tuple[-1]     # Access the last element (50)

print("Accessing Tuple Elements:")
print("First Element:", first_element)
print("Third Element:", third_element)
print("Last Element:", last_element)

# 2. Immutability

# Uncommenting the following line will result in an error
# my_tuple[1] = 25  # Error: Tuples are immutable

# 3. Concatenating Tuples

# Creating another tuple
another_tuple = (60, 70)

# Concatenating tuples
concatenated_tuple = my_tuple + another_tuple

print("\nConcatenating Tuples:")
print("Concatenated Tuple:", concatenated_tuple)

# 4. Unpacking Tuples

# Unpacking a tuple into variables
x, y, z, *rest = concatenated_tuple

print("\nUnpacking Tuples:")
print("x:", x)
print("y:", y)
print("z:", z)
print("Rest:", rest)

# 5. Tuple Methods

# Count occurrences of an element
count_20 = my_tuple.count(20)
print("\nTuple Methods:")
print("Count of 20:", count_20)

# Find the index of an element
index_40 = my_tuple.index(40)
print("Index of 40:", index_40)