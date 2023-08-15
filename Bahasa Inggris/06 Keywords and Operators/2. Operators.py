# Explanation of Operators in Python

# Operators perform various operations on values and variables.
# Let's explore arithmetic, comparison, logical, bitwise, assignment,
# membership, identity operators, and operator precedence.

# 1. Arithmetic Operators

x = 10
y = 3

# Addition
addition = x + y

# Subtraction
subtraction = x - y

# Multiplication
multiplication = x * y

# Division
division = x / y

# Floor Division
floor_division = x // y

# Modulus
modulus = x % y

# Exponentiation
exponentiation = x ** y

print("Arithmetic Operators:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

# 2. Comparison Operators

a = 5
b = 7

# Equal to
equal_to = a == b

# Not equal to
not_equal_to = a != b

# Greater than
greater_than = a > b

# Less than
less_than = a < b

# Greater than or equal to
greater_than_equal = a >= b

# Less than or equal to
less_than_equal = a <= b

print("\nComparison Operators:")
print("Equal to:", equal_to)
print("Not equal to:", not_equal_to)
print("Greater than:", greater_than)
print("Less than:", less_than)
print("Greater than or equal to:", greater_than_equal)
print("Less than or equal to:", less_than_equal)

# 3. Logical Operators

p = True
q = False

# Logical AND
logical_and = p and q

# Logical OR
logical_or = p or q

# Logical NOT
logical_not_p = not p
logical_not_q = not q

print("\nLogical Operators:")
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT p:", logical_not_p)
print("Logical NOT q:", logical_not_q)

# 4. Bitwise Operators

x = 5
y = 3

# Bitwise AND
bitwise_and = x & y

# Bitwise OR
bitwise_or = x | y

# Bitwise XOR
bitwise_xor = x ^ y

# Bitwise NOT
bitwise_not_x = ~x

# Left Shift
left_shift = x << y

# Right Shift
right_shift = x >> y

print("\nBitwise Operators:")
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT x:", bitwise_not_x)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)

# 5. Assignment Operators

a = 10

# Assign
assign = a

# Add and Assign
add_and_assign = a
add_and_assign += 5

# Subtract and Assign
subtract_and_assign = a
subtract_and_assign -= 3

# Multiply and Assign
multiply_and_assign = a
multiply_and_assign *= 2

# Divide and Assign
divide_and_assign = a
divide_and_assign /= 4

print("\nAssignment Operators:")
print("Assign:", assign)
print("Add and Assign:", add_and_assign)
print("Subtract and Assign:", subtract_and_assign)
print("Multiply and Assign:", multiply_and_assign)
print("Divide and Assign:", divide_and_assign)

# 6. Membership Operators

my_list = [1, 2, 3, 4, 5]

# Membership - 'in'
membership_in = 3 in my_list

# Membership - 'not in'
membership_not_in = 6 not in my_list

print("\nMembership Operators:")
print("Membership in:", membership_in)
print("Membership not in:", membership_not_in)

# 7. Identity Operators

x = 5
y = 5

# Identity - 'is'
identity_is = x is y

# Identity - 'is not'
identity_is_not = x is not y

print("\nIdentity Operators:")
print("Identity is:", identity_is)
print("Identity is not:", identity_is_not)

# 8. Operator Precedence

result = 10 + 3 * 2 ** 2  # Operator precedence: Exponentiation > Multiplication > Addition

print("\nOperator Precedence:")
print("Result:", result)
