#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ rectangle difine whith width and height"""

    def __init__(self, width=0, height=0):
        """ initialez new object whith whdth and height
        args:
            width (int): width of rectangle
            height (int): height of rectangle
            """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the current Rectangle width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ set Rectangle width
        Args:
             value (int): the new width to set of Rectangle
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the current Rectangle height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ set Rectangle height
        args:
            value (int): the new height to set of Rectangle
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
