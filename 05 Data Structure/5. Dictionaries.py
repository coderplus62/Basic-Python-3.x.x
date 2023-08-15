# Explanation of Dictionaries in Python

# Dictionaries are unordered collections of key-value pairs.
# Let's explore creating and accessing dictionaries, altering them,
# and using dictionary methods.

# 1. Creating and Accessing Dictionaries

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary values using keys
name = my_dict["name"]
age = my_dict["age"]
city = my_dict["city"]

print("Accessing Dictionaries:")
print("Name:", name)
print("Age:", age)
print("City:", city)

# 2. Altering Dictionaries

# Modifying a value using its key
my_dict["age"] = 31   # Change the age to 31

# Adding a new key-value pair
my_dict["country"] = "USA"

print("\nAltering Dictionaries:")
print("Modified Dictionary:", my_dict)

# 3. Dictionary Methods

# Getting all keys using keys()
keys = my_dict.keys()

# Getting all values using values()
values = my_dict.values()

# Getting key-value pairs using items()
items = my_dict.items()

print("\nDictionary Methods:")
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
