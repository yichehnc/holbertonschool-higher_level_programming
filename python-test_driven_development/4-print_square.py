#!/usr/bin/python3
""" This module contains one function to print a square"""


def print_square(size):
    """
    prints a square of '#' characters

    Args:
        size (int): size of the square, length and breadth

    Returns:
        Nothing
    """
    if any([isinstance(size, t) for t in [int, float]]):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            size = int(size)
            for i in range(size):
                print("#" * size)
    else:
        raise TypeError("size must be an integer")
