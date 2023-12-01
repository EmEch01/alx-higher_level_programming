#!/usr/bin/python3

if __name__ == "__main__":

    # Import the add function from the add_0 module
    from add_0 import add
    """Print the sum of 1 and 2."""

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
