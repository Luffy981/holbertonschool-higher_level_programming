#!/usr/bin/python3
import numpy as np
"""
function to multiply matrix
parameters
matrix a, matrix b
"""


def lazy_matrix_mul(m_a, m_b):
    """
    multipy matrix
    """
#   result = np.dot(m_a, m_b)
    result = np.matmul(m_a, m_b)
#    result = m_a @ m_b
    return result
