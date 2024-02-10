#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
        initialization method for instances

        Args:
            first_name (str): first name
            last_name (str): last name

            Return:
                Nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        gets dictionary of square

        Return:
            str: json version of class dict
        """
        return self.__dict__
