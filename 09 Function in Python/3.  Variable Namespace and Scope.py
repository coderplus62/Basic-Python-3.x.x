# Explanation of Variable Namespace and Scope in Python

# Variables in Python have their own namespaces and scopes.
# Let's explore how names, namespaces, and scopes work.

# 1. Names in the Python World

# Names are used to refer to variables, functions, classes, modules, etc.

variable_name = "Hello"
function_name = len
module_name = math

# 2. Namespace

# A namespace is a mapping of names to objects.
# Each module has its own namespace.

import math

print("Namespace of math module:", math.__dict__)

# 3. Scopes

# Scopes determine where a name can be accessed.
# There are four types of scopes: Local, Enclosing, Global, and Built-in.

x = 10  # Global scope

def my_function():
    y = 5  # Local scope
    print("Local variable y:", y)

my_function()

# Global and Local scopes example

global_var = 15  # Global scope

def outer_function():
    outer_var = 20  # Enclosing scope

    def inner_function():
        inner_var = 25  # Local scope
        print("Inner variable inner_var:", inner_var)
        print("Enclosing variable outer_var:", outer_var)
        print("Global variable global_var:", global_var)

    inner_function()

outer_function()

# Accessing Built-in scope

import builtins

print("Built-in scope names:", dir(builtins))
