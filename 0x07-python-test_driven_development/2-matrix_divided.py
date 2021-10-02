#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
#    formatted_list = []
#    for i in new_list:
#        for item in i:
#            formatted_list.append("%.2f" % item)
#    new_list = [round(x, 2) for i in new_list for x in i]
    message = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    i = 0
    if not isinstance(matrix[0], list):
        for item in matrix:
            if type(item) not in [int, float]:
                raise TypeError(message)
        new_list = list(map(lambda item: round(item/div, 2), matrix))
    else:
        for row in matrix:
            if i >= 1:
                if len(matrix[i]) != len(matrix[i - 1]):
                    raise TypeError(message2)
            for item in row:
                if type(item) not in [int, float]:
                    raise TypeError(message)
            i += 1
        new_list = list(map(lambda row: list(map(lambda i: round(i/div, 2), row)), matrix))
    return new_list
