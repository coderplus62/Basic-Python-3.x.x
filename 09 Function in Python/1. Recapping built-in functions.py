# Explanation of Recap: Built-in Functions in Python

# Python provides a rich set of built-in functions that perform various operations.
# Let's recap some of the important built-in functions.

# 1. len() - Returns the length (number of items) of an object

my_list = [10, 20, 30, 40, 50]
length = len(my_list)
print("Length of the list:", length)

# 2. max() - Returns the largest item in an iterable or among multiple arguments

numbers = [15, 25, 10, 35, 5]
maximum = max(numbers)
print("Maximum value:", maximum)

# 3. min() - Returns the smallest item in an iterable or among multiple arguments

minimum = min(numbers)
print("Minimum value:", minimum)

# 4. sum() - Returns the sum of all items in an iterable

total = sum(numbers)
print("Sum of values:", total)

# 5. sorted() - Returns a sorted list from the specified iterable

sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)

# 6. any() - Returns True if at least one element of an iterable is True

bool_values = [True, False, False, True]
has_true = any(bool_values)
print("Has True:", has_true)

# 7. all() - Returns True if all elements of an iterable are True

all_true = all(bool_values)
print("All True:", all_true)

# 8. map() - Applies a function to all items in an input list and returns an iterator

def square(x):
    return x ** 2

squared_values = map(square, numbers)
print("Squared values:", list(squared_values))

# 9. filter() - Filters elements from an iterable based on a condition

def is_even(x):
    return x % 2 == 0

even_values = filter(is_even, numbers)
print("Even values:", list(even_values))
