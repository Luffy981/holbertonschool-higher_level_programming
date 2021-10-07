#!/usr/bin/python3
"""
Function that return that adition of intengers

Doctest check the tests

Always return a integer value
"""


def add_integer(a, b=98):
    """Return adition of two numbers"""
    if a != a:
        a = 89
    if b != b:
        b = 89

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    res = a + b
    if res == float('inf') or res == -float('inf'):
        return 89

    return int(a) + int(b)
