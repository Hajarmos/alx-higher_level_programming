#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ rectangle difine whith width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialez new object whith whdth and height
        args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the current Rectangle width"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the current Rectangle height"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter
        if width or height is equal to 0, perimeter is equal to 0
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ print the rectangle with the character #"""

        rect = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += str(self.print_symbol)
                if i != self.__height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return ("Rectangle(" + str(self.__width)
                + ", " + str(self.__height) + ")")

    def __del__(self):
        """when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): first Rectangle
            rect_2 (Rectangle): second Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with
        width == height == size
        args:
            size (in): size of square
        """
        new = cls()
        new.width = size
        new.height = size
        return new
