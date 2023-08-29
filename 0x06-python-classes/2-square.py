#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    """ class Square """

    def __init__(self, size=0):
        """ initial new square
        Args:
             size (int): the size of new square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
