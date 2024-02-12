#!/usr/bin/python3
"""
Module - base.py
"""


class Base():
    """
    class Base for Almost a Circle project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class Base constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
