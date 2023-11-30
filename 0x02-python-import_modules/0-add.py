#!/usr/bin/python3

# Import add function from add_0.py
from add_0 import add

if __name__ == "__main__":

    a = 1
    b = 2

    # Print the result of the addition with the string formatting method
    print("{} + {} = {}".format(a, b, add(a, b)))
