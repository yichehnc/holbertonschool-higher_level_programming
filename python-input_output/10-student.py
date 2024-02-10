#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """initialization method for instances

        Args:
            first_name (str): first  name
            last_name (str): last name

            Return:
                Nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        gets dict of square

        Return:
            str: JSON version of class dictionary
        """

        dict = self.__dict__
        filtered = {}
        if attrs is not None:
            for key in dict:
                if key in attrs:
                    filtered[key] = dict[key]
        else:
            filtered = dict

        return filtered
