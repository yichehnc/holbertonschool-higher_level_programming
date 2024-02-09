#!/usr/bin/python3
"""
Module: 2-append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars_written = f.write(text)
    return chars_written
