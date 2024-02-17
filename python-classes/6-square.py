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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises a new square instance

        Arguments:
        size (int): The size of the square, set to 0 by default
        position (int): The position of the square
        must be a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrives itself
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Parameters:
        - value: New size value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """
        Retrieves itself
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Parameters:
        value: New position value (tuple of 2 positive integers)
        """
        error_message = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple):
            raise TypeError(error_message)
        if type(value) is not tuple:
            raise TypeError(error_message)
        if len(value) != 2:
            raise TypeError(error_message)
        if (not isinstance(value[0], int)) or (not isinstance(value[1], int)):
            raise TypeError(error_message)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(error_message)
        self.__position = value

    def area(self):
        """
        Finds area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' character based on size and position.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("_" * self.__position[0], end="")
                print("#" * self.__size, end="")
                print()
