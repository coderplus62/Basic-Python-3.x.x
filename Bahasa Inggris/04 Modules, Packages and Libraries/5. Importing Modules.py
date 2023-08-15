# 1. Import Statement
# The import statement allows you to import an entire module.
# You can access the module's attributes using the module name as a prefix.
import math

# Using the math module
print("Pi:", math.pi)
print("Square Root of 16:", math.sqrt(16))

# 2. Selective Import
# Selective import allows you to import specific attributes from a module.
# This can reduce memory usage and make your code more readable.
from random import randint

# Using the randint function directly
random_number = randint(1, 10)
print("Random Number:", random_number)

# 3. The Module Search Path
# Python searches for modules in specific directories.
# The sys.path list shows the directories where Python looks for modules.
import sys

print("Module search path:")
for path in sys.path:
    print(path)

# You can also modify sys.path to add custom directories for module search.

# Note: Make sure the module you're importing is installed or located in a directory listed in sys.path.
