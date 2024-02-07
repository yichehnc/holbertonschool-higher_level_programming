#!/usr/bin/python3
"""
Module: A function that returns a list of avaliable
attributes and methods of an object
"""

def lookup(obj):
    """
    Returns a list of available attributes
    and methods of an object

    Args:
        obj(object): object to get the attributes of

    Returns:
        list: attributes of the object passed in as argument
    """
    return dir(obj)
