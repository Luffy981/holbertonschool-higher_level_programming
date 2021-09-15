#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda i:i*i, row)))
    return new_matrix
