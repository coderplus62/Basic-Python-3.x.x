# Function for General Mathematics
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the result of dividing one number by another."""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Function for Basic Physics Concepts
def velocity(distance, time):
    """Calculates velocity given distance and time."""
    return distance / time

def acceleration(initial_velocity, final_velocity, time):
    """Calculates acceleration using initial and final velocity, and time."""
    return (final_velocity - initial_velocity) / time

def force(mass, acceleration):
    """Calculates force using mass and acceleration."""
    return mass * acceleration

# General Mathematics Examples
print("Sum:", add(5, 3))
print("Difference:", subtract(10, 4))
print("Product:", multiply(6, 2))
print("Quotient:", divide(15, 3))

# Basic Physics Examples
print("Velocity:", velocity(100, 20))
print("Acceleration:", acceleration(10, 30, 5))
print("Force:", force(5, 10))
