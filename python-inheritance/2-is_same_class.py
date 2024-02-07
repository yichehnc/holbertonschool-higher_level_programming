#!/usr/bin/python3
"""
A function that returns True if the object is exactly an instance of
the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    checks if an object is an instance of a class

    Args:
        obj (object): object to check instance of
        a_class (object): object to check if obj is of same type

    Returns:
        bool: True if the obj is an instance of a_class,
        otherwise False
    """
    return type(obj).__name__ == a_class.__name__
