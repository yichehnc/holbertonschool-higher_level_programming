#!/usr/bin/python3
"""
Module: A function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Returns the number of characters written
    """
    with open(filename, "w+", encoding="utf-8") as writing:
        chars_written = writing.write(text)
    return chars_written
