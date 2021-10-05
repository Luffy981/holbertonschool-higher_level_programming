#!/usr/bin/python3
"""
function to multiply matrix
parameters
matrix a, matrix b
"""


def matrix_mul(m_a, m_b):
    """
    multipy matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in (m_a):
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row2 in (m_b):
        if type(row2) is not list:
            raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    elif len(m_a) == 1:
        if not m_a[0]:
            raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    elif len(m_b) == 1:
        if not m_b[0]:
            raise ValueError("m_b can't be empty")
    message = "m_a should contain only integers or floats"
    message2 = "m_b should contain only integers or floats"
    if type(m_a[0]) is not list:
        for i in m_a:
            if type(i) not in [int, float]:
                raise TypeError(message)
    else:
        len_r = len(m_a[0])
        for row in m_a:
            if len_r != len(row):
                raise TypeError("each row of m_a must be of the same size")
            len_r = len(row)
            for item in row:
                if type(item) not in [int, float]:
                    raise TypeError(message)

    if type(m_b[0]) is not list:
        for j in m_a:
            if type(j) not in [int, float]:
                raise TypeError(message2)
    else:
        len_r = len(m_b[0])
        for row2 in m_b:
            if len_r != len(row2):
                raise TypeError("each row of m_b must be of the same size")
            len_r = len(row2)
            for item2 in row2:
                if type(item2) not in [int, float]:
                    raise TypeError(message2)
#   for i in range(len(m_a)):
#   for j in range(len(m_b[0])):
#       for k in range(len(m_b)):
#           result[i][j] += m_a[i][k] * m_b[k][j]
#   result = [[sum(a * b for a, b in zip(m_a_row, m_b_column))
#   for m_b_column in zip(*m_b)] for m_a_row in m_a]
    res = [[sum(a * b for a, b in zip(r, c)) for c in zip(*m_b)] for r in m_a]
    return res
