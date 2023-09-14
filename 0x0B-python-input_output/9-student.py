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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
