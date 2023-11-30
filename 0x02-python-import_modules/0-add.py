#!/usr/bin/python3


# Import add function from add_0.py
from add_0 import add

# run directly without executing when called via import
if __name__ == "__main__":

    # Assign a value to a variable called a
    a = 1

    # Assign a value to a variable called b
    b = 2

# Print the result of the addition with the string formatting method
print("{} + {} = {}".format(a, b, add(a, b)))
