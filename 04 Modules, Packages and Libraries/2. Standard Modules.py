# Importing Standard Modules
import math
import random
import datetime
import sys

# Using the math Module
angle = 45  # in degrees
radians = math.radians(angle)  # Convert degrees to radians
sin_value = math.sin(radians)
cos_value = math.cos(radians)
print(f"Sin({angle}°): {sin_value}")
print(f"Cos({angle}°): {cos_value}")

# Using the random Module
random_number = random.randint(1, 10)  # Generate a random integer between 1 and 10
print(f"Random Number: {random_number}")

# Using the datetime Module
current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()
print(f"Current Date: {current_date}")
print(f"Current Time: {current_time}")

# Using the sys Module
print("Python Version:", sys.version)
print("Platform:", sys.platform)
print("Command Line Arguments:", sys.argv)
