#!/usr/bin/python3i

""" class Square that defines a square """


class Square:
    """ class Square """

    def __init__(self, size=0):
        """ initial new square
        Args:
             size (int): the size of new square
        """

        self.__size = size

    @property
    def size(self):
        """get the current square size"""

        return self.__size

    @size.setter
    def size(self, value):
        """ set Square size
        Args:
             value (int): the new size to set of square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area """

        return self.__size ** 2
