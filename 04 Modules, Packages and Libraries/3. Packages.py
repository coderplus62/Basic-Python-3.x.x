# Importing Modules from Packages
# Suppose you have a package named 'my_package' with submodules 'module1' and 'module2'.
# The package structure should be like:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Importing modules from the package
from my_package import module1, module2

# Using modules from the package
print(module1.add(5, 3))  # Using a function from module1
print(module2.multiply(6, 2))  # Using a function from module2

# Importing the Entire Package
import my_package

# Using modules from the package using the package name
print(my_package.module1.subtract(10, 4))
print(my_package.module2.divide(15, 3))

# Renaming Modules and Packages
import my_package.module1 as m1
import my_package.module2 as m2

# Using the renamed modules
print(m1.add(7, 2))
print(m2.multiply(4, 5))
