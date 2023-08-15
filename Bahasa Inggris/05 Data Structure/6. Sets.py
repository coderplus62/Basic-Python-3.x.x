# Explanation of Sets in Python

# Sets are unordered collections of unique elements.
# Let's explore creating sets, set operations, and using set methods.

# 1. Creating Sets

# Creating a set
my_set = {10, 20, 30, 40, 50}

# Adding elements to the set using add()
my_set.add(60)  # Add 60 to the set

print("Creating Sets:")
print("Initial Set:", my_set)

# 2. Set Operations

# Checking membership using in
is_present = 30 in my_set  # Check if 30 is in the set
is_absent = 70 in my_set   # Check if 70 is in the set

print("\nSet Operations:")
print("Is 30 in the set?", is_present)
print("Is 70 in the set?", is_absent)

# Removing elements using remove()
my_set.remove(30)  # Remove 30 from the set

print("Modified Set after Removal:", my_set)

# 3. Set Methods

# Creating another set
another_set = {40, 50, 60, 70, 80}

# Union of sets using union()
union_result = my_set.union(another_set)

# Intersection of sets using intersection()
intersection_result = my_set.intersection(another_set)

# Difference of sets using difference()
difference_result = my_set.difference(another_set)

print("\nSet Methods:")
print("Union Result:", union_result)
print("Intersection Result:", intersection_result)
print("Difference Result:", difference_result)
