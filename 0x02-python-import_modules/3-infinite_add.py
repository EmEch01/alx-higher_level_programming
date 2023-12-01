#!/usr/bin/python3

from sys import argv


def main():
    """
    This function adds all the command-line arguments and prints the sum.
    """
    args = map(int, argv[1:])
    result = sum(args)
    print(result)


if __name__ == "__main__":
    main()
