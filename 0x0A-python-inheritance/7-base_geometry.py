#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class"""

    def area(self):
        """raises an Exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value:
        args:
            name (str): always is a string
            value (int): raise a TypeError exception if is not integer
            or less than 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if not value > 0:
            raise ValueError(name + " must be greater than 0")
