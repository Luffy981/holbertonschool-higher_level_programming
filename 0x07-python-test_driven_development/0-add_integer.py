#!/usr/bin/python3
"""
function to add 2 numbers
numers a, b
return a + b
"""


def add_integer(a, b=98):
    """Return the addition of two numbers with spcific validation
    Arguments:
        a (int or float): first value to add
        b (int or float): second value to add
    Return:
        the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        """ raise a TypeError if a isn't a integer or float'"""
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        """ raise a TypeError if a isn't a integer or float'"""
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
