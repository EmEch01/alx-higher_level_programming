#!/usr/bin/python3

# run directly withoyt been executed by the function call import

# Import add function from add_0.py
from add_0 import add

# Assign a value to a variable called a
a = 1

# Assign a value to a variable called b
b = 2

# Call the function add with a and b as arguments
result = add(a, b)

# Print the result of the addition with the string formatting method
print("{} + {} = {}".format(a, b, add(a, b)))

