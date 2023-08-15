# 1. Integer
# Integers are whole numbers without a fractional component.
# Example:
age = 30

# 2. Float
# Floats are numbers with a decimal point or exponent notation.
# Example:
height = 5.9

# 3. String
# Strings are sequences of characters, enclosed in single or double quotes.
# Example:
name = "Alice"

# 4. Boolean
# Booleans represent the truth values True or False.
# They are often used for logical operations and comparisons.
# Example:
is_student = True

# 5. Operations on Strings
# Strings can be concatenated (combined) and multiplied.
# Various string methods are available for manipulation.
# Example:
greeting = "Hello"
full_greeting = greeting + ", " + name  # Concatenation
repeated_greeting = greeting * 3  # Multiplication

# 6. type() Function
# The type() function returns the data type of a value.
# It's useful for checking the type of a variable.
# Example:
age_type = type(age)  # Returns <class 'int'>
height_type = type(height)  # Returns <class 'float'>
name_type = type(name)  # Returns <class 'str'>
is_student_type = type(is_student)  # Returns <class 'bool'>

# Print statements to see the results
print(full_greeting)
print(repeated_greeting)
print("Age is of type:", age_type)
print("Height is of type:", height_type)
print("Name is of type:", name_type)
print("is_student is of type:", is_student_type)
