# Explanation of Iterators in Python

# Iterators provide a way to iterate over a sequence of values.
# Let's explore how to use iterables, the enumerate() function, the zip() function,
# and how to create a custom iterator.

# 1. Iterables (using iter tool)

numbers = [1, 2, 3, 4, 5]

# Using the iter() function to create an iterator from a list
numbers_iterator = iter(numbers)

# Looping through the iterator using the next() function
print("Iterating through the iterator:")
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))

# 2. enumerate() Function

fruits = ["apple", "banana", "cherry"]

# Using the enumerate() function to get both index and value
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

# 3. The zip() Function

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Using the zip() function to combine two or more lists
for name, age in zip(names, ages):
    print("Name:", name, "Age:", age)

# 4. Creating a Custom Iterator

class CustomIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Using the custom iterator
custom_iterator = CustomIterator(1, 5)
print("Custom Iterator:")
for num in custom_iterator:
    print("Value:", num)
