#!/usr/bin/python3
"""Module for function from_json_strint"""
import json


def from_json_string(my_str):
    """
    Convents a JSON string to a Python object

    Args:
        my_str (str): the string to convert to JSON

    Returns:
        obj: a python object
    """
    return json.loads(my_str)
