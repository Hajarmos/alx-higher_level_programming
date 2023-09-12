#!/usr/bin/python3
"""function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified class
otherwise False."""


def inherits_from(obj, a_class):
    """func"""
    return not issubclass(a_class, obj.__class__)
