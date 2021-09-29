#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""
    def __init__(self, size=0):
        """Size is a private attribute :
            - size must be an integer, otherwise raise a TypeError exception
              with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the
              message size must be >= 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instances  method:
            * Return: The current  square are"""
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def my_print(self):
        """Print Square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
