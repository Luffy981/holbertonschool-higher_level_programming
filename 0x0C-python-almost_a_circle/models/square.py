#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor of square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size of square with rectangle attributes"""
        self.width = value
        self.height = value

    def __str__(self):
        """The overloading __str__ method for square"""
        return ("[Square] {:d} {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.size))
