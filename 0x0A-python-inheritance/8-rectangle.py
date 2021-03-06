#!/usr/bin/python3
"""Class rectangle inherent"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """new class"""
    def __init__(self, width, height):
        """magic method"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
