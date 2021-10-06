#!/usr/bin/python3
"""
function return addition
values: a, b
Return: a + b
"""


def add_integer(a, b=98):
    """
    function return addition
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return a + b
