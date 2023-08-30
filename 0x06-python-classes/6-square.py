#!/usr/bin/python3i

""" class Square that defines a square """


class Square:
    """ class Square """

    def __init__(self, size=0, position=(0, 0)):
        """ initial new square
        Args:
             size (int): the size of new square
             position (int, int): The position of the new square
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ to retrieve it"""

        return self.__position

    @position.setter
    def position(self, value):
        """ to set it"""

        if (type(value) is not tuple or len(value) != 2 or
                (type(n) is not int for n in value)
                or (n < 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the current square area """

        return self.__size ** 2

    def my_print(self):
        """
            prints in position of stdout the square with the character #
            if size is equal to 0, print an empty line
        """

        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
