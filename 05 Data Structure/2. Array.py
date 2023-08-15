# Explanation of Arrays in Python

# Arrays in Python are implemented using lists or the built-in array module.
# Let's use lists to demonstrate accessing and manipulating arrays.

# 1. Accessing Array Elements

# Creating an array (list)
my_array = [10, 20, 30, 40, 50]

# Accessing array elements using indexing
first_element = my_array[0]     # Access the first element (10)
third_element = my_array[2]     # Access the third element (30)
last_element = my_array[-1]     # Access the last element (50)

print("Accessing Array Elements:")
print("First Element:", first_element)
print("Third Element:", third_element)
print("Last Element:", last_element)

# 2. Manipulating Array Elements

# Modifying array elements using indexing
my_array[1] = 25   # Change the second element to 25

# Adding elements to the array using append()
my_array.append(60)  # Append 60 to the end of the array

# Removing elements from the array using remove()
my_array.remove(30)  # Remove the element 30

print("\nManipulating Array Elements:")
print("Modified Array:", my_array)

# Slicing to get a subset of the array
subset_array = my_array[1:4]  # Get elements from index 1 to 3 (not inclusive)
print("Subset Array:", subset_array)

# Reversing the array using slicing
reversed_array = my_array[::-1]  # Reverse the entire array
print("Reversed Array:", reversed_array)
