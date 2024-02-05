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
        __init__(self, size=0): Initialises a new instance of a square
        size(self): Retrives itself
        size(self, value): Determines if input size if a suitable integer
        area(self): Determines the area of the square
        my_print(self): Prints a square with a given size
    """
    def __init__(self, size=0):
        """
        Initialises a new square instance

        Arguments:
        size (int): The size of the square, set to 0 by default
        """
        self.__size = size

        @property
        def size(self):
            """
            Retrives itself
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            Determines whether the size value for the square is appropriate

            """
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """
            Finds area of square
            """
            return self.__size ** 2

        def my_print(self):
            if self.__size == 0:
                print()
            else:
                for i in range(self.__size):
                    print("#" * self.__size)
