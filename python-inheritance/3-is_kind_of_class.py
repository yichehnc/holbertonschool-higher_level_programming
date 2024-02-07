#!/usr/bin/python3
"""
Module: A function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited from,
the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of a class that
    has been inherited from, else False
    """
    return isinstance(obj, a_class)
