#!/usr/bin/python3
"""Module for function load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file

    Args:
        filename (str): name of file to read from

    Return:
        obj: a python object
    """
    with open(filename, "r") as f:
        return json.load(f)
