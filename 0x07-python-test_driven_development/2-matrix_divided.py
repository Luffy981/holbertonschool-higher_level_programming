#!/usr/bin/python3
"""
function matrix_divided
parametres: matrix, div
Return: new matrix
"""


def matrix_divided(matrix, div):
    """
    function use matrix and div
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    message1 = "Each row of the matrix must have the same size"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    i = 0
    if type(matrix) is not list:
        raise TypeError(message)
    if not isinstance(matrix[0], list):
        for item in matrix:
            if type(item) not in [int, float]:
                raise TypeError(message)
        re = list(map(lambda item: round(item/div, 2), matrix))
    else:
        for row in matrix:
            if i >= 1:
                if len(matrix[i]) != len(matrix[i - 1]):
                    raise TypeError(message1)
            for item in row:
                if type(item) not in [int, float]:
                    raise TypeError(message)
            i += 1
        my = matrix.copy()
        re = list(map(lambda r: list(map(lambda i: round(i/div, 2), r)), my))
    return re
