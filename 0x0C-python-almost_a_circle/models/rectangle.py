#!/usr/bin/python3
"""class
rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        property width return
        """
        return self.__width

    @width.setter
    def width(self, new_width):
        """
        property setter width
        """
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """
        property height return
        """
        return self.__height

    @height.setter
    def height(self, new_height):
        """
        property setter height
        """
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """
        property x
        """
        return self.__x

    @x.setter
    def x(self, new_x):
        """
        property setter x
        """
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """
        property y
        """
        return self.__y

    @y.setter
    def y(self, new_y):
        """
        property setter y
        """
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """area value of the
        Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """that prints in
        stdout the Rectangle"""
        for y in range(0, self.y):
            print()
        for j in range(0, self.height):
            for x in range(0, self.x):
                print(" ", end="")
            for i in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method"""
        string = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        string = string.format(self.id, self.x, self.y,
                               self.width, self.height)
        return string

    def update(self, *args, **kwargs):
        """ public method def update that assigns an
        argument to each attribute
        -**kwargs must be skipped if *args exists and is not empty
        -Each key in this dictionary represents an attribute to the instance
        """
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        to dictionary
        """
        key_list = ["id", "width", "height", "x", "y"]
        value_list = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(key_list, value_list))
