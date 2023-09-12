#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""

    def __init__(self, width, height):
        """init new object
        args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ returns the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """print rectangle description: [Rectangle] <width>/<height>"""
        return ("[Rectangle] " + str(self.__width)
                + "/" + str(self.__height))
