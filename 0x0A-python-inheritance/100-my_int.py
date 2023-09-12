#!/usr/bin/python3
""" class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """ == operators inverted"""
        return self.real != value

    def __ne__(self, value):
        """ != operators inverted"""
        return self.real == value
