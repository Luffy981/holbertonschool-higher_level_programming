#!/usr/bin/python3

def add_integer(a, b=98):
    """ Function to add 2 integers"""
    if type(a) is not int and type(a) is not float:
        """ raise a TypeError if a isn't a integer or float'"""
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        """ raise a TypeError if a isn't a integer or float'"""
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b