#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squares
    squared_matrix = []
    for subset in matrix:
        squared_subset = [num ** 2 for num in subset]
        squared_matrix.append(squared_subset)
    return squared_matrix
