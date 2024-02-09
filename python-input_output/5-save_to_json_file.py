#!/usr/bin/python3
"""
Module for the function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation:

    Args:
        my_obj (obj): python object to write to file
        filename (str): name of the file to write to

    Return:
        Nothing
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
