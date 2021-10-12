#!/usr/bin/python3
"""Cass definition"""


class BaseGeometry:
    """improve geometry"""
    def area(self):
        """Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Class rectangle inherent"""


class Rectangle(BaseGeometry):
    """new class"""
    def __init__(self, width, height):
        """magic method"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
