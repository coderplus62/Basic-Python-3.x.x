# Explanation of Lists in Python

# Lists are ordered collections that can hold items of different types.
# Let's explore accessing list items, updating lists, list manipulation,
# and using lists as stacks and queues.

# 1. Accessing List Items

# Creating a list
my_list = [10, 20, 30, 40, 50]

# Accessing list items using indexing
first_item = my_list[0]     # Access the first item (10)
third_item = my_list[2]     # Access the third item (30)
last_item = my_list[-1]     # Access the last item (50)

print("Accessing List Items:")
print("First Item:", first_item)
print("Third Item:", third_item)
print("Last Item:", last_item)

# 2. Updating List

# Modifying list items using indexing
my_list[1] = 25   # Change the second item to 25

print("\nUpdating List:")
print("Modified List:", my_list)

# 3. List Manipulation

# Adding items to the end of the list using append()
my_list.append(60)  # Append 60 to the end of the list

# Removing items from the list using remove()
my_list.remove(30)  # Remove the item 30

print("\nList Manipulation:")
print("Modified List:", my_list)

# 4. Stacks and Queues using Lists

# Using a list as a stack (Last In, First Out)
stack = []
stack.append(1)   # Push 1
stack.append(2)   # Push 2
stack.append(3)   # Push 3

popped_item = stack.pop()   # Pop the top item (3)
print("\nStack:")
print("Popped Item:", popped_item)
print("Remaining Stack:", stack)

# Using a list as a queue (First In, First Out)
queue = []
queue.append(1)   # Enqueue 1
queue.append(2)   # Enqueue 2
queue.append(3)   # Enqueue 3

dequeued_item = queue.pop(0)   # Dequeue the front item (1)
print("\nQueue:")
print("Dequeued Item:", dequeued_item)
print("Remaining Queue:", queue)
