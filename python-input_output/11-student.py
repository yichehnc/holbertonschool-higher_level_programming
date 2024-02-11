#!/usr/bin/python3
"""
Module for Student class 11-student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialization method for instances

        Args:
            first_name (str): first name
            last_name (str): last name

            Return:
                Nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets dict of square.

            Returns:
                str: JSON version of class dict
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

    def reload_from_json(self, json):
        """
        replaces instance attrs with json values

        Args:
            json (dict): dict with attrs to replace

        Returns:
            str: json version of class dict
        """
        for key in json:
            self.__dict__[key] = json[key]
