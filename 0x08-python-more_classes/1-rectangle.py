#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """class rectangle
    - area
    - perimeter
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Property to width"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """To set property width"""
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width < 0:
            raise ValueError("width must be >=0")
        self.__width = new_width

    @property
    def height(self):
        """Property to height"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """Property to height"""
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        elif new_height < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = new_height
