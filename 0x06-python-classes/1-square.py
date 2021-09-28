#!/usr/bin/python3
"""Class square"""


class Square:
    """class Square that defines a square by:
    -Private instance attribute: size
    -Instantiation with size (no type/value verification)
    -You are not allowed to import any module"""
    def __init__(self, size):
        """Private attribute size,
        The size of a square is crucial for a square"""
        self.__size = size
