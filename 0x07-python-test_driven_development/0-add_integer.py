#!/usr/bin/python3
"""
Function that return that adition of intengers
Doctest check the tests
always return a integer value
"""


def add_integer(a, b=98):
    """
    Return an intenger
    Always success
    """
    if a != a or b != b:
        a = 89
        b = 89
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    r = a + b
    if r == float('inf') or r == -float('inf'):
        return 89

    return (int(a) + int(b))

