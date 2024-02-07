#!/usr/bin/python3
"""
Module: A function that return True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class, else False
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, else False
    """
    if (type(obj).__name__ == a_class.__name__):
        return False
    return issubclass(type(obj), a_class)
