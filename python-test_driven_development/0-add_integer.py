#!/usr/bin/python3
"""Task 0. Integers addition
"""


def add_integer(a, b=98):
    """Function that adds two integers

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: Either of a and b is not an integer
    """
    if a is None or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if b is None or (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
