#!/usr/bin/python3
"""
Module: a function read_file
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as reading_file:
        print(reading_file.read(), end="")
