#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class"""

    def __init__(self, size):
        """ init new square
        arg:
            size (int): square size
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """print Square description: [Square] <width>/<height>"""
        return ("[Square] " + str(self.__size)
                + "/" + str(self.__size))
