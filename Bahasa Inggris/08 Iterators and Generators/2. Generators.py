# Explanation of Generators in Python

# Generators provide a memory-efficient way to create iterators.
# Let's explore how to use generator functions and expressions to create generators.

# 1. Generator Functions

# Using a generator function to yield values one at a time
def count_up_to(limit):
    num = 1
    while num <= limit:
        yield num
        num += 1

# Using the generator function
counter = count_up_to(5)
print("Using Generator Function:")
for num in counter:
    print("Value:", num)

# 2. Generator Expressions

# Using a generator expression to create a generator on-the-fly
even_numbers = (x for x in range(1, 11) if x % 2 == 0)

print("Using Generator Expression:")
for num in even_numbers:
    print("Even Number:", num)

# 3. Memory Efficiency

# Comparing memory usage between list and generator
import sys

list_of_numbers = [x for x in range(1, 1000000)]
generator_of_numbers = (x for x in range(1, 1000000))

print("Memory usage for List:", sys.getsizeof(list_of_numbers), "bytes")
print("Memory usage for Generator:", sys.getsizeof(generator_of_numbers), "bytes")
