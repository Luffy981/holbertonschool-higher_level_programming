#!/usr/bin/python3
"""Class square"""


class Square:
    """class Square that defines a square by:
        -Private instance attribute: size
        -Instantiation with optional size: def __init__(self, size=0)"""
    def __init__(self, size=0):
        """size is a private attribute:
            -size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
            -if size is less than 0, raise a ValueError exception
            with the message size must be >= 0"""
        if not isinstance(size, int):
            raise Typerror("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self__size = size
