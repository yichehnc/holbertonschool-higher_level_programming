#!/usr/bin/python3
"""
A class Square that defines a square
by a private instance attribute of size
"""


class Square:
    """
    Contains a private instance attribute of size with conditions

    Attributes:
        size (int): size of the square
    Methods:
    __init__(self, size = 0): Initialises a new instance of a square
    area(self): Finds the area of the square
    """
    def __init__(self, size=0):
        """
        Initialises a new square instance

        Arguments:
        size (int): The size of the square, set to 0 by default
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
            """
            Finds area of square
            """
            return self.__size ** 2
