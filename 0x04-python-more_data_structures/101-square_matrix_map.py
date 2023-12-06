#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Squares all elements of a matrix using map.

    Args:
        matrix: A two-dimensional list of integers.

    Returns:
        A new matrix with squared elements.
    """
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
