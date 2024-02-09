#!/usr/bin/python3
"""
Module for class 10-Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A subclass Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        initialization method for a Square instance
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of a square
        """
        return self.__size * self.__size

    def __str__(self):
        """Returns string representation for the square instance"""
        return f"[{type(self).__name__}] {self.__size}/{self.__size}"
