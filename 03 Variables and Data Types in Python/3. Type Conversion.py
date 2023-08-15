# 1. Implicit Type Conversion (Coercion)
# Implicit type conversion, also known as coercion, occurs automatically
# when an operation involves different data types.
# Python converts the data type of the value to match the operation's requirements.
# Example:
int_num = 10
float_num = 3.5

result = int_num + float_num
# Here, Python implicitly converts 'int_num' to a float before the addition.

# 2. Explicit Type Conversion (Casting)
# Explicit type conversion, also known as casting, involves manually converting
# a value from one data type to another.
# This is done using built-in functions like int(), float(), str(), etc.
# Example:
age = "25"
age_as_int = int(age)
# The int() function explicitly converts the string 'age' to an integer.

height = 5.9
height_as_int = int(height)
# Trying to convert a float to an int truncates the decimal part.

# Examples of explicit type conversion:
float_value = 3.14
float_to_int = int(float_value)  # Converts float to int (truncates decimal)
int_value = 42
int_to_float = float(int_value)  # Converts int to float

# Note: Explicit conversion might lead to data loss or unintended behavior,
# so it should be used carefully.

# Print statements to see the results
print("Result of implicit conversion:", result)
print("Age as an integer:", age_as_int)
print("Height as an integer:", height_as_int)
print("Float to int conversion:", float_to_int)
print("Int to float conversion:", int_to_float)
