#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        """init new student
        args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        arg:
            attrs: list of strings
        """
        latt = {}
        if type(attrs) is list:
            for i in attrs:
                if i in self.__dict__:
                    latt[i] = self.__dict__[i]
            return latt
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance
        arg:
            json: dictionary
        """
        self.__dict__ = json
